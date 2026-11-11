"""NEW. CLI: one JSONL row per (model, probe settings, image). Checkpoint after every chunk
of images; --resume skips keys already in --out (a torn last line is ignored).

  python -m rope_runner.run --model qwen3vl-8b-thinking --probe default --split validation \
      --subset AAAAB mixed --limit 100 --greedy --out runs/x.jsonl --resume
"""
import argparse
import datetime
import json
import os
import sys
import time

import yaml

from . import budget as budget_mod
from .data import SUBSETS, candidates, gold_labels, image_path, iter_items, load_image
from .prompts import PLACES, PROBES, SINGLE_PROBES, TF_MODES, build_calls
from .scoring import error_types, strict_score, tolerant_score

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIGS = os.path.join(os.path.dirname(HERE), "configs")


def variant(args):
    v = [("greedy" if args.greedy else "recommended"), f"seed={args.seed}"]
    if args.probe == "teacher_forcing":
        v.append(f"tf={args.tf_mode}")
    if args.no_think:
        v.append("no_think")
    if args.budget:
        v.append(f"budget={args.budget}")
    if args.n_given is not None:
        v.append(f"given={args.n_given}")
    if args.prefix_place != "user":
        v.append(f"place={args.prefix_place}")
    if args.prefix_caching != "auto":
        v.append(f"pc={args.prefix_caching}")
    return ",".join(v)


def row_key(model, probe, var, split, subset, entry_idx, image_id):
    return f"{model}|{probe}|{var}|{split}|{subset}|{entry_idx}|{image_id}"


def repair_tail(path):
    """Drop a torn last line (job killed mid-write) so the next append starts on a fresh line."""
    with open(path, "rb+") as f:
        data = f.read()
        if data and not data.endswith(b"\n"):
            f.truncate(data.rfind(b"\n") + 1)


def done_keys(path):
    keys = set()
    if not os.path.exists(path):
        return keys
    repair_tail(path)
    with open(path) as f:
        for line in f:
            try:
                keys.add(json.loads(line)["key"])
            except (json.JSONDecodeError, KeyError):
                continue  # torn line from a killed job
    return keys


def append_rows(path, rows):
    with open(path, "a") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def score_row(probe, tf_mode, subset, entry, split, calls, gens, meta):
    gold5 = gold_labels(entry)
    cands = candidates(split, entry["data_source"])
    answers = [g["stripped_answer"] for g in gens]
    ask = calls[0]["obj_index"] if len(calls) == 1 and calls[0]["obj_index"] else 5
    parsed, correct, moh_total = strict_score(probe, answers, gold5, tf_mode, ask)
    tparsed, tcorrect = tolerant_score(probe, answers, gold5, cands, tf_mode, ask)
    one_obj = len(parsed) == 1
    obj_idx = [ask] if one_obj else [1, 2, 3, 4, 5]
    cf = meta.get("counterfactual_class")
    return {
        "parsed_labels": parsed,
        "gold_labels": [gold5[ask - 1]] if one_obj else gold5,
        "obj_indices": obj_idx,
        "correct_flags": correct,
        "error_types": error_types(parsed, obj_idx, gold5, subset, cands, cf),
        "tolerant_labels": tparsed,
        "tolerant_correct_flags": tcorrect,
        "tolerant_error_types": error_types(tparsed, obj_idx, gold5, subset, cands, cf),
        "moh_total": moh_total,
        "all_gold_labels": gold5,
        "data_source": entry["data_source"],
    }


def make_model(args, models_cfg):
    pc = {"auto": None, "on": True, "off": False}[args.prefix_caching]
    if args.dry_run:
        from .models import FakeModel
        return FakeModel(name=args.model, prefix_caching=pc)
    from .models import VLLMModel
    return VLLMModel(args.model, models_cfg["models"][args.model], models_cfg["defaults"],
                     greedy=args.greedy, seed=args.seed, prefix_caching=pc)


def fake_answer(probe, entry, call):
    """--dry-run only: the gold answer in moh's format (after an assistant-turn prefill: the
    prefill followed by the asked object's gold class)."""
    g = gold_labels(entry)
    if probe in SINGLE_PROBES:
        return g[call["obj_index"] - 1]
    if call.get("prefill") is not None:
        return f"{call['prefill']} {g[call['obj_index'] - 1]}"
    return ", ".join(f"obj{i}: {c}" for i, c in enumerate(g, 1))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="key in configs/models.yaml")
    ap.add_argument("--probe", required=True, choices=PROBES)
    ap.add_argument("--split", required=True, choices=["train", "validation"], help="train=Seen, validation=Unseen")
    ap.add_argument("--subset", nargs="+", default=None, help=f"subset(s) from {SUBSETS}; default from probes.yaml")
    ap.add_argument("--limit", type=int, default=None, help="first N images per subset")
    ap.add_argument("--greedy", action="store_true")
    ap.add_argument("--budget", type=int, default=None, help="thinking budget N (truncate-and-close)")
    ap.add_argument("--tf-mode", choices=TF_MODES, default=None)
    ap.add_argument("--no-think", action="store_true", help="append /no_think (MiMo 2508)")
    ap.add_argument("--n-given", type=int, choices=range(5), default=None,
                    help="one-shot teacher_forcing / counterfactual: give only the first N of the four "
                         "other objects (dose-response); default all four")
    ap.add_argument("--prefix-place", choices=PLACES, default="user",
                    help="one-shot teacher_forcing / counterfactual: put the given labels in the user "
                         "turn (moh, default) or prefill them as the start of the model's answer")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", required=True)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--data-dir", default=os.environ.get("ROPE_DIR", os.path.expanduser("~/cse595/data/ROPE")))
    ap.add_argument("--chunk", type=int, default=64, help="images per checkpoint")
    ap.add_argument("--models-config", default=os.path.join(CONFIGS, "models.yaml"))
    ap.add_argument("--probes-config", default=os.path.join(CONFIGS, "probes.yaml"))
    ap.add_argument("--dry-run", action="store_true", help="CPU: fake model that answers gold; no images loaded")
    ap.add_argument("--prefix-caching", choices=["auto", "on", "off"], default="auto",
                    help="vLLM prefix caching; auto = vLLM default (on in 0.11 V1)")
    args = ap.parse_args(argv)

    models_cfg = yaml.safe_load(open(args.models_config))
    probes_cfg = yaml.safe_load(open(args.probes_config))["probes"][args.probe]
    if args.tf_mode is None:
        args.tf_mode = probes_cfg.get("tf_mode", "oneshot")
    subsets = args.subset or probes_cfg.get("subsets", SUBSETS)
    cf_seed = probes_cfg.get("seed", 0)
    one_shot = args.probe == "counterfactual" or (args.probe == "teacher_forcing" and args.tf_mode == "oneshot")
    if (args.n_given is not None or args.prefix_place != "user") and not one_shot:
        sys.exit("--n-given and --prefix-place apply to one-shot teacher_forcing and counterfactual only")
    if args.prefix_place == "assistant" and args.budget:
        sys.exit("--prefix-place assistant cannot be combined with --budget")

    if not args.dry_run and args.model not in models_cfg["models"]:
        sys.exit(f"unknown model {args.model}")
    mcfg = models_cfg["models"].get(args.model, {})
    max_tokens = mcfg.get("max_tokens", 8192)
    answer_max = models_cfg.get("defaults", {}).get("answer_max_tokens", 128)

    if os.path.dirname(args.out):
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
    if os.path.exists(args.out) and not args.resume:
        sys.exit(f"{args.out} exists; pass --resume to continue it")
    seen = done_keys(args.out)
    var = variant(args)

    todo = []
    for subset in subsets:
        for idx, image_id, entry in iter_items(args.data_dir, args.split, subset, args.limit):
            key = row_key(args.model, args.probe, var, args.split, subset, idx, image_id)
            if key not in seen:
                todo.append((subset, idx, image_id, entry, key))
    print(f"[run] {len(todo)} images to do ({len(seen)} keys already in {args.out})", flush=True)
    if not todo:
        return

    model = make_model(args, models_cfg)
    missing = []
    for start in range(0, len(todo), args.chunk):
        chunk = todo[start:start + args.chunk]
        prompts, images, spans, per_item, prefills = [], [], [], [], []
        for subset, idx, image_id, entry, key in chunk:
            calls, meta = build_calls(args.probe, entry, args.split, args.tf_mode, args.no_think,
                                      image_key=f"{subset}/{idx}/{image_id}", seed=cf_seed, subset=subset,
                                      n_given=args.n_given, place=args.prefix_place)
            path = image_path(args.data_dir, entry)
            if args.dry_run and not os.path.exists(path):
                missing.append(path)
            img = path if args.dry_run else load_image(path)
            s = len(prompts)
            for c in calls:
                p = model.render(c["text"])
                if args.dry_run:
                    model.answer_for[(p, img)] = fake_answer(args.probe, entry, c)
                prompts.append(p)
                images.append(img)
                prefills.append(c.get("prefill"))
            spans.append((s, len(prompts)))
            per_item.append((subset, idx, image_id, entry, key, calls, meta, path))
        t0 = time.time()
        if args.prefix_place == "assistant":
            thinking = getattr(model, "thinking", mcfg.get("thinking", False))
            gens = budget_mod.run_prefilled(model, prompts, images, prefills, thinking, max_tokens, answer_max)
        else:
            gens = budget_mod.run_calls(model, prompts, images, max_tokens, args.budget, answer_max)
        chunk_wall = time.time() - t0
        ts = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        chunk_id = f"{ts}#{start}"
        rows = []
        for (s, e), (subset, idx, image_id, entry, key, calls, meta, path) in zip(spans, per_item):
            g = gens[s:e]
            row = {
                "key": key, "image_id": image_id, "entry_idx": idx, "image_path": path,
                "subset": subset, "split": args.split, "probe": args.probe,
                "tf_mode": args.tf_mode if args.probe == "teacher_forcing" else None,
                "no_think": args.no_think, "budget": args.budget, "variant": var,
                "counterfactual_class": meta.get("counterfactual_class"),
                "n_given": meta.get("n_given"), "prefix_place": args.prefix_place,
                "prefix_used": [c["prefix"] for c in calls],
                "raw_output": [x["raw_output"] for x in g],
                "stripped_answer": [x["stripped_answer"] for x in g],
                "trace_text": [x["trace_text"] for x in g],
                "think_closed": [x["think_closed"] for x in g],
                "forced_close": [x["forced_close"] for x in g],
                "thinking_tokens": [x["thinking_tokens"] for x in g],
                "answer_tokens": [x["answer_tokens"] for x in g],
                "finish_reason": [x["finish_reason"] for x in g],
                "prompt_tokens": [x.get("prompt_tokens") for x in g],
                "cached_tokens": [x.get("cached_tokens") for x in g],
                "asked_objects": [c["obj_index"] for c in calls],
                "prefix_caching": args.prefix_caching,
                "chunk_id": chunk_id, "chunk_images": len(chunk), "chunk_wall_s": round(chunk_wall, 3),
                "model": args.model, "model_path": model.path, "sampling": model.sampling,
                "run_timestamp": ts,
            }
            row.update(score_row(args.probe, args.tf_mode, subset, entry, args.split, calls, g, meta))
            rows.append(row)
        append_rows(args.out, rows)
        print(f"[run] wrote {start + len(chunk)}/{len(todo)}", flush=True)
    if args.dry_run:
        print(f"[run] dry run: {len(missing)} image files missing" + (f", e.g. {missing[0]}" if missing else ""))


if __name__ == "__main__":
    main()
