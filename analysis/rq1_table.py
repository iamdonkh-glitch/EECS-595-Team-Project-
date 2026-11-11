#!/usr/bin/env python
"""RQ1 tables (read-only). Per-object accuracy by model x subset x probe x split, strict (moh) and
tolerant side by side; paired tests (single vs default, and inside each model pair); accuracy by
box position; Seen vs Unseen gap. Works on any model's `default` / `single` JSONL.

  source harness/env.sh                       # the venv: numpy; harness/rope_runner for the class lists
  python analysis/rq1_table.py [--out-dir DIR] [jsonl ...] > tables.md
  # default input: results/*/rq1_*.jsonl (parser-audit files are skipped); default DIR: results/

Writes DIR/rq1_table1.csv and DIR/rq1_fig1_position.png. The figure needs matplotlib: it is drawn by
the running python if it has matplotlib, otherwise by /usr/bin/python3 (the Great Lakes system
python 3.6, which has matplotlib; the team venv does not) in a subprocess.
Model pairs tested against each other: MiMo-VL SFT vs RL, Qwen3-VL Instruct vs Thinking (PAIRS);
a pair with a model missing is skipped with a note. Add results/<model>/rq1_*.jsonl to include a model.

Conventions: tolerant parse is primary, strict (moh) beside it. Token-limit rule: a call with
finish_reason == 'length' makes every object it answers wrong (default: all five; single: that
call's object), kept in the denominator, for both parsers. CIs are 95% percentile bootstraps over
images (2,000 reps); Holm inside each stated family. Images are paired on (split, subset,
entry_idx, image_id).
"""
import csv
import glob
import json
import math
import os
import subprocess
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the repository
RESULTS = os.path.join(ROOT, "results")
sys.path.insert(0, os.path.join(ROOT, "harness"))  # harness/rope_runner (class lists)
PROBES = ["default", "single"]
SPLITS = ["train", "validation"]
SPLIT_NAME = {"train": "Seen", "validation": "Unseen"}
# (name, ROPE subsets pooled into it)
GROUPS = [("In-the-Wild", ("mixed",)), ("Homogeneous", ("homogenous",)), ("Heterogeneous", ("heterogenous",)),
          ("Adversarial", ("AAAAB", "BAAAA")), ("Adversarial AAAAB", ("AAAAB",)), ("Adversarial BAAAA", ("BAAAA",))]
TEST_GROUPS = GROUPS[:4]  # paired and gap tests: the four ROPE subsets (Adversarial pooled)
POS_SUBSETS = ["mixed", "homogenous", "heterogenous", "AAAAB", "BAAAA"]
POS_NAME = {"mixed": "In-the-Wild", "homogenous": "Homogeneous", "heterogenous": "Heterogeneous",
            "AAAAB": "Adversarial AAAAB", "BAAAA": "Adversarial BAAAA"}
PAIRS = [("mimo-sft-2508", "mimo-rl-2508"), ("qwen3vl-8b-instruct", "qwen3vl-8b-thinking")]
REPS = 2000


def default_paths():
    return sorted(p for p in glob.glob(os.path.join(RESULTS, "*", "rq1_*.jsonl")) if "parser_audit" not in os.path.basename(p))


# ------------------------------------------------------------------ copied helpers
# load_rows and mcnemar_exact are copied unchanged from the owner's rope_runner/adv.py (not part of harness/),
# except that load_rows skips rows without a probe field.
def load_rows(paths):
    rows = {}
    for p in paths:
        with open(p) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if "probe" not in r:
                    continue
                rows[r["key"]] = r  # last write wins
    return list(rows.values())


def mcnemar_exact(b, c):
    """Two-sided exact McNemar p-value: b = pairs right under cond 1 only, c = under cond 2 only.
    Binomial(b + c, 0.5) test, doubled one tail, capped at 1."""
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return min(1.0, 2 * tail)


# ------------------------------------------------------------------ rows -> per-image records
def load(paths):
    """{(model, probe, split, subset): {(entry_idx, image_id): rec}}; rec has per-box 0/1 lists
    t, s (index 0 = box 1) after the token-limit rule, trunc (any cut call), n_cut_calls, flipped (objects
    the rule turned from correct to wrong, per parser) and parse-failure counts t_fail, s_fail."""
    from rope_runner.constant import TRAIN_CLASSES, VALIDATION_CLASSES
    data = {}
    for r in load_rows(paths):
        if r.get("probe") not in PROBES or r.get("no_think") or r.get("budget"):
            continue
        cs = {c.lower() for c in (TRAIN_CLASSES if r["split"] == "train" else VALIDATION_CLASSES)[r["data_source"]]}
        # Token-limit rule (team rule, standard scoring for both parsers): a call with finish_reason
        # 'length' makes every object it answers wrong, even if the cut answer parses. One call
        # answers all objects (default); otherwise call i answers asked_objects[i] (single).
        fr = r["finish_reason"]
        if len(fr) == 1:
            cut = set(r["obj_indices"]) if fr[0] == "length" else set()
        else:
            cut = {o for f, o in zip(fr, r.get("asked_objects") or r["obj_indices"]) if f == "length"}
        t, s, flipped = [None] * 5, [None] * 5, {"t": 0, "s": 0}
        for i, o in enumerate(r["obj_indices"]):
            for tag, flags in (("t", r["tolerant_correct_flags"]), ("s", r["correct_flags"])):
                ok = int(bool(flags[i]))
                flipped[tag] += ok and o in cut
                (t if tag == "t" else s)[o - 1] = 0 if o in cut else ok
        rec = {"t": t, "s": s, "trunc": bool(cut), "n_cut_calls": sum(f == "length" for f in fr), "flipped": flipped,
               "t_fail": sum(x is None for x in r["tolerant_labels"]),
               "s_fail": sum(x is None or x not in cs for x in r["parsed_labels"])}
        data.setdefault((r["model"], r["probe"], r["split"], r["subset"]), {})[(r["entry_idx"], r["image_id"])] = rec
    return data


def group(data, model, probe, split, subsets):
    """Records of one Table 1 cell, keyed (subset, entry_idx, image_id)."""
    out = {}
    for sub in subsets:
        for k, rec in data.get((model, probe, split, sub), {}).items():
            out[(sub,) + k] = rec
    return out


def img_acc(rec, tag):
    v = [x for x in rec[tag] if x is not None]
    return sum(v) / len(v)


# ------------------------------------------------------------------ statistics (copied unchanged from the owner's analysis script)
rng = np.random.default_rng(0)


def boot_mean(v):
    v = np.asarray(v, dtype=float)
    if len(v) == 0:
        return (float("nan"), float("nan"))
    idx = rng.integers(0, len(v), size=(REPS, len(v)))
    means = np.sort(v[idx].mean(axis=1))
    return (float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5)))


def boot_unpaired(v1, v2):
    a, b = np.asarray(v1, float), np.asarray(v2, float)
    ia = rng.integers(0, len(a), size=(REPS, len(a)))
    ib = rng.integers(0, len(b), size=(REPS, len(b)))
    d = b[ib].mean(axis=1) - a[ia].mean(axis=1)
    return (float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5)))


def perm_unpaired(v1, v2, reps=10000):
    a, b = np.asarray(v1, float), np.asarray(v2, float)
    obs = abs(b.mean() - a.mean())
    pool = np.concatenate([a, b])
    cnt = 0
    for _ in range(reps // 1000):
        perm = np.argsort(rng.random((1000, len(pool))), axis=1)
        x = pool[perm]
        dd = np.abs(x[:, len(a):].mean(axis=1) - x[:, :len(a)].mean(axis=1))
        cnt += int((dd >= obs - 1e-12).sum())
    return (cnt + 1) / (reps + 1)


def holm(ps):
    n = len(ps)
    order = sorted(range(n), key=lambda i: ps[i])
    adj, run = [0.0] * n, 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (n - rank) * ps[i]))
        adj[i] = run
    return adj


def pct(x):
    return "n/a" if x is None or x != x else f"{100 * x:.1f}"


def pp(x):
    return "n/a" if x != x else f"{100 * x:+.1f}"


def ci_s(ci, f=pct):
    return f"[{f(ci[0])}, {f(ci[1])}]"


def fp(p):
    return "n/a" if p != p else (f"{p:.1e}" if p < 1e-3 else f"{p:.3g}")


# ------------------------------------------------------------------ (a) Table 1
def table1(data):
    models = sorted({k[0] for k in data})
    rows = []
    for m in models:
        for gname, subs in GROUPS:
            for pr in PROBES:
                for sp in SPLITS:
                    g = group(data, m, pr, sp, subs)
                    if not g:
                        continue
                    recs = list(g.values())
                    t = [img_acc(r, "t") for r in recs]
                    s = [img_acc(r, "s") for r in recs]
                    kept = [img_acc(r, "t") for r in recs if not r["trunc"]]
                    nobj = sum(sum(x is not None for x in r["t"]) for r in recs)
                    rows.append(dict(model=m, subset=gname, probe=pr, split=SPLIT_NAME[sp], n_images=len(recs),
                                     n_objects=nobj, n_truncated=sum(r["trunc"] for r in recs),
                                     n_token_limit_calls=sum(r["n_cut_calls"] for r in recs),
                                     acc_tolerant=float(np.mean(t)), ci_tolerant=boot_mean(t),
                                     acc_strict=float(np.mean(s)), ci_strict=boot_mean(s),
                                     acc_tolerant_trunc_dropped=float(np.mean(kept)) if kept else float("nan"),
                                     parse_fail_tolerant=sum(r["t_fail"] for r in recs) / nobj,
                                     parse_fail_strict=sum(r["s_fail"] for r in recs) / nobj))
    return rows


def print_table1(rows):
    print("## (a) Table 1: per-object accuracy (%)\n")
    print("Tolerant parse is primary, strict (moh) beside it. Accuracy = correct boxes / scored boxes; 95% CI = "
          "bootstrap over images. Token-limit rule: every object answered by a call that hit max_tokens is wrong "
          "(kept in the denominator). Cut calls = calls at max_tokens; cut rows = rows with at least one; 'tol, trunc dropped' "
          "drops those rows. Parse fail = share of boxes with no tolerant label / with a strict label that is not a "
          "candidate name (single: raw answer is not exactly a candidate).\n")
    print("| model | subset | probe | split | n img | n obj | cut calls / rows | tolerant [95% CI] | strict [95% CI] "
          "| tol, trunc dropped | parse fail tol / strict |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['model']} | {r['subset']} | {r['probe']} | {r['split']} | {r['n_images']} | {r['n_objects']} | "
              f"{r['n_token_limit_calls']} / {r['n_truncated']} | {pct(r['acc_tolerant'])} {ci_s(r['ci_tolerant'])} | {pct(r['acc_strict'])} "
              f"{ci_s(r['ci_strict'])} | {pct(r['acc_tolerant_trunc_dropped'])} | "
              f"{pct(r['parse_fail_tolerant'])} / {pct(r['parse_fail_strict'])} |")
    print()


def write_csv(rows, path):
    cols = ["model", "subset", "probe", "split", "n_images", "n_objects", "n_token_limit_calls", "n_truncated", "acc_tolerant",
            "ci_tolerant_lo", "ci_tolerant_hi", "acc_strict", "ci_strict_lo", "ci_strict_hi",
            "acc_tolerant_trunc_dropped", "parse_fail_tolerant", "parse_fail_strict"]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            d = dict(r, ci_tolerant_lo=r["ci_tolerant"][0], ci_tolerant_hi=r["ci_tolerant"][1],
                     ci_strict_lo=r["ci_strict"][0], ci_strict_hi=r["ci_strict"][1])
            w.writerow([round(d[c], 6) if isinstance(d[c], float) else d[c] for c in cols])


# ------------------------------------------------------------------ (b) paired tests
def paired_test(x, y):
    """x, y: {image key: rec}. Unit = box on the same image. diff = acc(y) - acc(x)."""
    keys = sorted(set(x) & set(y), key=str)
    if not keys:
        return None
    out = {"n_img": len(keys)}
    for tag in ("t", "s"):
        b = c = 0
        for k in keys:
            for xi, yi in zip(x[k][tag], y[k][tag]):
                if xi is not None and yi is not None:
                    b += xi and not yi
                    c += yi and not xi
        d = [img_acc(y[k], tag) - img_acc(x[k], tag) for k in keys]
        out[tag] = dict(x=float(np.mean([img_acc(x[k], tag) for k in keys])),
                        y=float(np.mean([img_acc(y[k], tag) for k in keys])),
                        diff=float(np.mean(d)), ci=boot_mean(d), b=b, c=c, p=mcnemar_exact(b, c))
    kk = [k for k in keys if not x[k]["trunc"] and not y[k]["trunc"]]
    out["t_kept"] = (float(np.mean([img_acc(y[k], "t") - img_acc(x[k], "t") for k in kk])) if kk else float("nan"), len(kk))
    return out


def print_family(title, header_note, rows):
    for tag in ("t", "s"):
        for r, a in zip(rows, holm([r["res"][tag]["p"] for r in rows])):
            r["res"][tag]["holm"] = a
    print(f"### {title}\n\n{header_note}\n")
    print("| comparison | subset | probe | split | n img | tolerant x -> y | diff [95% CI] | b / c | p | Holm p "
          "| strict diff [95% CI] | strict p (Holm) | tol diff, trunc dropped (n img) |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        t, s, kept = r["res"]["t"], r["res"]["s"], r["res"]["t_kept"]
        print(f"| {r['label']} | {r['subset']} | {r['probe']} | {r['split']} | {r['res']['n_img']} | {pct(t['x'])} -> "
              f"{pct(t['y'])} | {pp(t['diff'])} {ci_s(t['ci'], pp)} | {t['b']} / {t['c']} | {fp(t['p'])} | "
              f"{fp(t['holm'])} | {pp(s['diff'])} {ci_s(s['ci'], pp)} | {fp(s['p'])} ({fp(s['holm'])}) | "
              f"{pp(kept[0])} ({kept[1]}) |")
    print()


UNIT = ("Paired unit: the box (image x box position) on the same image, images matched on (split, subset, "
        "entry_idx, image_id). McNemar = exact two-sided test on discordant boxes (b = right only under x, c = right "
        "only under y; it treats the 5 boxes of an image as independent). CI = paired bootstrap over images of the "
        "per-image accuracy difference. diff = y - x in points.")


def paired_section(data):
    print("## (b) Paired tests on the same images\n")
    models = sorted({k[0] for k in data})
    rows = []
    for m in models:
        for gname, subs in TEST_GROUPS:
            for sp in SPLITS:
                res = paired_test(group(data, m, "single", sp, subs), group(data, m, "default", sp, subs))
                if res:
                    rows.append(dict(label=f"{m}: single -> default", subset=gname, probe="-", split=SPLIT_NAME[sp], res=res))
    if rows:
        print_family("single (x) vs default (y), each model",
                     UNIT + " Holm family = all rows of this table, separately per parser.", rows)
    for a, b in PAIRS:
        if a not in models or b not in models:
            print(f"Note: pair {a} vs {b} skipped: no file for {b if a in models else a}.\n")
            continue
        rows, missing = [], []
        for gname, subs in TEST_GROUPS:
            for pr in PROBES:
                for sp in SPLITS:
                    res = paired_test(group(data, a, pr, sp, subs), group(data, b, pr, sp, subs))
                    if res:
                        rows.append(dict(label=f"{a} -> {b}", subset=gname, probe=pr, split=SPLIT_NAME[sp], res=res))
                    else:
                        missing.append(f"{gname}/{pr}/{SPLIT_NAME[sp]}")
        if missing:
            print(f"Note: {a} vs {b}: no common images for {', '.join(missing)} (one model has no file); skipped.\n")
        if rows:
            print_family(f"{a} (x) vs {b} (y)", UNIT + " Holm family = all rows of this table, separately per parser.", rows)


# ------------------------------------------------------------------ (c) positions
def positions(data):
    out = {}
    for (m, pr, sp, sub), d in sorted(data.items()):
        if sub not in POS_SUBSETS:
            continue
        acc = {}
        for tag in ("t", "s"):
            acc[tag] = [float(np.mean([r[tag][i] for r in d.values() if r[tag][i] is not None] or [float("nan")]))
                        for i in range(5)]
        out[(m, pr, sp, sub)] = dict(n=len(d), **acc)
    return out


def print_positions(pos):
    print("## (c) Accuracy by box position (%), tolerant (strict)\n")
    print("| model | subset | probe | split | n img | box 1 | box 2 | box 3 | box 4 | box 5 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for (m, pr, sp, sub), v in pos.items():
        cells = " | ".join(f"{pct(t)} ({pct(s)})" for t, s in zip(v["t"], v["s"]))
        print(f"| {m} | {POS_NAME[sub]} | {pr} | {SPLIT_NAME[sp]} | {v['n']} | {cells} |")
    print()


PLOT = r'''
import json, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
d = json.load(sys.stdin)
subs, out = d["subsets"], d["out"]
models = sorted(set(r["model"] for r in d["rows"]))
colors = dict(zip(models, ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#8c564b"]))
fig, axes = plt.subplots(2, len(subs), figsize=(max(3.4 * len(subs), 10), 7), sharey=True, squeeze=False)
for i, sp in enumerate(["train", "validation"]):
    for j, sub in enumerate(subs):
        ax = axes[i][j]
        for r in d["rows"]:
            if r["split"] == sp and r["subset"] == sub:
                ax.plot(range(1, 6), [100 * x for x in r["t"]], marker="o", color=colors[r["model"]],
                        linestyle="-" if r["probe"] == "default" else "--", label=r["model"] + ", " + r["probe"])
        ax.set_title(d["names"][sub] + " - " + {"train": "Seen", "validation": "Unseen"}[sp], fontsize=9)
        ax.set_xticks(range(1, 6))
        ax.set_xlabel("box position")
        ax.grid(alpha=0.3)
    axes[i][0].set_ylabel("per-object accuracy, tolerant (%)")
h, l = [], []
for ax in axes.flat:
    for hh, ll in zip(*ax.get_legend_handles_labels()):
        if ll not in l:
            h.append(hh); l.append(ll)
fig.legend(h, l, loc="lower center", ncol=4, fontsize=8)
fig.tight_layout(rect=(0, 0.1, 1, 1))
fig.savefig(out, dpi=150)
'''


def plot(pos, out):
    payload = json.dumps(dict(out=out, subsets=[s for s in POS_SUBSETS if any(k[3] == s for k in pos)], names=POS_NAME,
                              rows=[dict(model=m, probe=pr, split=sp, subset=sub, t=v["t"]) for (m, pr, sp, sub), v in pos.items()]))
    try:
        import matplotlib  # noqa: F401
        py = sys.executable
    except ImportError:
        py = "/usr/bin/python3"  # the venv has no matplotlib
    subprocess.run([py, "-c", PLOT], input=payload.encode(), check=True)


# ------------------------------------------------------------------ (d) Seen vs Unseen
def gap_section(data):
    print("## (d) Seen vs Unseen gap (unpaired: different images and candidate lists)\n")
    print("gap = Unseen - Seen, points, per-object accuracy. CI = bootstrap resampling each split's images "
          "separately; p = two-sided permutation test on per-image accuracy (10,000 reps). Holm family = the rows "
          "of one model.\n")
    print("| model | subset | probe | n Seen / Unseen | tolerant Seen -> Unseen | gap [95% CI] | p | Holm p | strict gap [95% CI] |")
    print("|---|---|---|---|---|---|---|---|---|")
    for m in sorted({k[0] for k in data}):
        rows = []
        for gname, subs in TEST_GROUPS:
            for pr in PROBES:
                g = {sp: list(group(data, m, pr, sp, subs).values()) for sp in SPLITS}
                if not g["train"] or not g["validation"]:
                    continue
                r = dict(subset=gname, probe=pr, n=(len(g["train"]), len(g["validation"])))
                for tag in ("t", "s"):
                    a, b = [img_acc(x, tag) for x in g["train"]], [img_acc(x, tag) for x in g["validation"]]
                    r[tag] = dict(a=float(np.mean(a)), b=float(np.mean(b)), gap=float(np.mean(b) - np.mean(a)),
                                  ci=boot_unpaired(a, b))
                r["p"] = perm_unpaired([img_acc(x, "t") for x in g["train"]], [img_acc(x, "t") for x in g["validation"]])
                rows.append(r)
        for r, a in zip(rows, holm([r["p"] for r in rows])):
            t, s = r["t"], r["s"]
            print(f"| {m} | {r['subset']} | {r['probe']} | {r['n'][0]} / {r['n'][1]} | {pct(t['a'])} -> {pct(t['b'])} | "
                  f"{pp(t['gap'])} {ci_s(t['ci'], pp)} | {fp(r['p'])} | {fp(a)} | {pp(s['gap'])} {ci_s(s['ci'], pp)} |")
    print()


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    out_dir = RESULTS
    if "--out-dir" in argv:
        i = argv.index("--out-dir")
        out_dir = argv[i + 1]
        del argv[i:i + 2]
    paths = argv or default_paths()
    data = load(paths)
    print(f"# RQ1 tables\n\nFiles ({len(paths)}): " + ", ".join(os.path.basename(p) for p in paths) + "\n")
    rows = table1(data)
    print_table1(rows)
    write_csv(rows, os.path.join(out_dir, "rq1_table1.csv"))
    paired_section(data)
    pos = positions(data)
    print_positions(pos)
    plot(pos, os.path.join(out_dir, "rq1_fig1_position.png"))
    gap_section(data)


if __name__ == "__main__":
    main()
