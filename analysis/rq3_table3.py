#!/usr/bin/env python
"""RQ3 Table 3 (read-only): error taxonomy of every scored object in the RQ1 runs, per model x subset x
probe x split, for the tolerant parse (primary) and the strict (moh) parse side by side.

  source harness/env.sh                       # the venv (numpy) and $ROPE_DIR
  python analysis/rq3_table3.py [--out-dir DIR] [--rope-dir DIR] [jsonl ...] > tables.md
  # default input: results/*/rq1_*.jsonl (parser-audit files are skipped); default DIR: results/rq3

Writes DIR/rq3_table3.csv (counts per category, both parsers). Reads ROPE's JSON files for each image's
object_set (every class annotated in the image, not only the five boxes).

Each scored object gets exactly one category, checked in this order:
  truncated  the call that answers the object hit max_tokens (finish_reason == 'length'). Team rule: the
             object is wrong even if the cut answer parses or matches the gold label.
  unparsed   no label recovered from an answer that was not cut
  correct    label == gold
  b_eq_a     Adversarial only: the odd box B (AAAAB box 5, BAAAA box 1) labelled A, the class of the other
             four boxes. Both orders count; AAAAB and BAAAA are reported as separate subsets.
  borrowed   label = the class of another of the five target boxes
  off_list   label not in the split's 50-class candidate list (a formatting failure, not a hallucination)
  in_image   in the candidate list, not a target class, but in the image's object_set (an object that is
             annotated elsewhere in the image)
  invented   in the candidate list and not in the image's object_set

Relation to the harness's stored error types (rope_runner/scoring.py): inertia = b_eq_a on AAAAB;
borrowed = borrowed + b_eq_a on BAAAA; invented = in_image + invented; unparsed and off_list are the same,
except that this script moves every object of a cut call to truncated. Section (e) checks this mapping row
by row against the stored types.

Conventions as in analysis/rq1_table.py: rows are deduplicated by key; rows with no_think or budget are
skipped; a single-probe call answers asked_objects[i]. Percentages are of scored objects unless stated.
CIs are 95% percentile bootstraps over images (2,000 reps, seed 0).
"""
import argparse
import collections
import csv
import glob
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the repository
RESULTS = os.path.join(ROOT, "results")
sys.path.insert(0, os.path.join(ROOT, "harness"))  # harness/rope_runner (class lists, error_type)

MODELS = ["mimo-sft-2508", "mimo-rl-2508", "qwen3vl-8b-instruct", "qwen3vl-8b-thinking"]
PROBES = ["default", "single"]
SPLITS = ["train", "validation"]
SPLIT_NAME = {"train": "Seen", "validation": "Unseen"}
SUBSETS = [("mixed", "In-the-Wild"), ("homogenous", "Homogeneous"), ("heterogenous", "Heterogeneous"),
           ("AAAAB", "Adversarial AAAAB"), ("BAAAA", "Adversarial BAAAA")]
JSON_FILES = {"AAAAB": "AAAAB_data.json", "BAAAA": "BAAAA_data.json",
              "heterogenous": "merged_heterogenous_data.json", "homogenous": "merged_homogenous_data.json",
              "mixed": "merged_mixed_data.json"}
CATS = ["correct", "truncated", "unparsed", "b_eq_a", "borrowed", "off_list", "in_image", "invented"]
ERR_CATS = CATS[1:]
CAT_HEAD = {"correct": "correct", "truncated": "truncated", "unparsed": "unparsed", "b_eq_a": "B=A",
            "borrowed": "borrowed", "off_list": "off-list", "in_image": "in-image", "invented": "invented"}
PARSERS = [("tolerant", "tolerant_labels", "tolerant_error_types"), ("strict", "parsed_labels", "error_types")]
B_BOX = {"AAAAB": 5, "BAAAA": 1}
REPS = 2000


def default_paths():
    return sorted(p for p in glob.glob(os.path.join(RESULTS, "*", "rq1_*.jsonl"))
                  if "parser_audit" not in os.path.basename(p))


def load_rows(paths):
    rows = {}
    for p in paths:
        with open(p) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if r.get("probe") not in PROBES or r.get("no_think") or r.get("budget"):
                    continue
                rows[r["key"]] = r  # last write wins
    return list(rows.values())


def load_rope(rope_dir):
    """{(split, subset, entry_idx): (image_id, object_set)} from ROPE's JSON files."""
    out = {}
    for split in SPLITS:
        for sub, fn in JSON_FILES.items():
            with open(os.path.join(rope_dir, split, fn)) as f:
                for i, e in enumerate(json.load(f)):
                    stem = os.path.splitext(os.path.basename(e["folder"]))[0]
                    out[(split, sub, i)] = (stem, {x.lower() for x in e["object_set"]})
    return out


def a_class(subset, gold5):
    """Class A of an Adversarial image (the class of the four non-B boxes), or None if they disagree."""
    others = [g for j, g in enumerate(gold5, 1) if j != B_BOX[subset]]
    return others[0] if len(set(others)) == 1 else None


def categorize(label, obj, gold5, subset, cands, oset, cut):
    if cut:
        return "truncated"
    if label is None:
        return "unparsed"
    if label == gold5[obj - 1]:
        return "correct"
    if subset in B_BOX and obj == B_BOX[subset] and label == a_class(subset, gold5):
        return "b_eq_a"
    if label in [g for j, g in enumerate(gold5, 1) if j != obj]:
        return "borrowed"
    if label not in cands:
        return "off_list"
    if label in oset:
        return "in_image"
    return "invented"


def harness_type(cat, subset):
    """The stored harness error type implied by a category (None = correct). Not defined for truncated."""
    if cat == "b_eq_a":
        return "inertia" if subset == "AAAAB" else "borrowed"
    if cat in ("in_image", "invented"):
        return "invented"
    return None if cat == "correct" else cat


def build(rows, rope):
    """{(model, probe, split, subset, parser): {image: [categories of its scored objects]}} and checks."""
    from rope_runner.constant import TRAIN_CLASSES, VALIDATION_CLASSES
    from rope_runner.scoring import error_type
    cells = collections.defaultdict(dict)
    chk = collections.Counter()
    for r in rows:
        split, sub, idx = r["split"], r["subset"], r["entry_idx"]
        stem, oset = rope[(split, sub, idx)]
        chk["rows"] += 1
        chk["image_id_mismatch"] += stem != r["image_id"]
        cands_list = (TRAIN_CLASSES if split == "train" else VALIDATION_CLASSES)[r["data_source"]]
        cands = {c.lower() for c in cands_list}
        gold5 = r["all_gold_labels"]
        if sub in B_BOX and a_class(sub, gold5) is None:
            chk["adversarial_rows_without_single_A"] += 1
        fr = r["finish_reason"]
        if len(fr) == 1:
            cut = set(r["obj_indices"]) if fr[0] == "length" else set()
        else:
            cut = {o for f, o in zip(fr, r.get("asked_objects") or r["obj_indices"]) if f == "length"}
        img = (idx, r["image_id"])
        for pname, lab_field, type_field in PARSERS:
            cats = []
            for k, obj in enumerate(r["obj_indices"]):
                label, stored = r[lab_field][k], r[type_field][k]
                # (1) the harness's own error_type on the stored label must give the stored type
                chk[f"{pname}_harness_recomputed_mismatch"] += error_type(label, obj, gold5, sub, cands_list) != stored
                cat = categorize(label, obj, gold5, sub, cands, oset, obj in cut)
                # (2) outside cut calls, the new category must map back to the stored type
                if cat != "truncated":
                    chk[f"{pname}_mapping_checked"] += 1
                    chk[f"{pname}_mapping_mismatch"] += harness_type(cat, sub) != stored
                cats.append(cat)
            cells[(r["model"], r["probe"], split, sub, pname)][img] = cats
    return cells, chk


def counts(cell):
    c = collections.Counter(cat for cats in cell.values() for cat in cats)
    return c, sum(c.values())


def pct(x, n):
    return f"{100 * x / n:.1f}" if n else "-"


def boot_ci(v, rng):
    v = np.asarray(v, dtype=float)
    if len(v) == 0:
        return (float("nan"), float("nan"))
    m = v[rng.integers(0, len(v), size=(REPS, len(v)))].mean(axis=1)
    return tuple(np.percentile(m, [2.5, 97.5]))


def models_in(cells):
    present = {k[0] for k in cells}
    return [m for m in MODELS if m in present] + sorted(present - set(MODELS))


def print_table3(cells, models, pname):
    letter = "a" if pname == "tolerant" else "b"
    print(f"## ({letter}) Table 3, {pname} parse: category of each scored object (% of scored objects)\n")
    if pname == "tolerant":
        print("Each row sums to 100 (up to rounding). Categories and their order are defined in the script "
              "docstring and the README. correct equals Table 1's accuracy (token-limit rule applied).\n")
    print("| model | subset | probe | split | n img | n obj | " + " | ".join(CAT_HEAD[c] for c in CATS) + " |")
    print("|---|---|---|---|---|---|" + "---|" * len(CATS))
    for m in models:
        for sub, sname in SUBSETS:
            for probe in PROBES:
                for split in SPLITS:
                    cell = cells.get((m, probe, split, sub, pname))
                    if not cell:
                        continue
                    c, n = counts(cell)
                    vals = " | ".join(pct(c[x], n) for x in CATS)
                    print(f"| {m} | {sname} | {probe} | {SPLIT_NAME[split]} | {len(cell)} | {n} | {vals} |")
    print()


def print_b_eq_a(cells, models, rng):
    print("## (c) The odd box B on Adversarial (tolerant)\n")
    print("One B box per image: box 5 in AAAAB, box 1 in BAAAA. B=A = B labelled with A, the class of the "
          "other four boxes. A truncated B box counts as truncated, not as B=A. CI = bootstrap over images.\n")
    print("| model | order | probe | split | n img | B correct | B=A [95% CI] | B truncated | B other error |")
    print("|---|---|---|---|---|---|---|---|---|")
    for m in models:
        for sub in B_BOX:
            for probe in PROBES:
                for split in SPLITS:
                    cell = cells.get((m, probe, split, sub, "tolerant"))
                    if not cell:
                        continue
                    b = [cats[B_BOX[sub] - 1] for cats in cell.values()]
                    n = len(b)
                    is_ba = [x == "b_eq_a" for x in b]
                    lo, hi = boot_ci(is_ba, rng)
                    n_ok, n_ba, n_tr = b.count("correct"), sum(is_ba), b.count("truncated")
                    print(f"| {m} | {sub} | {probe} | {SPLIT_NAME[split]} | {n} | {pct(n_ok, n)} | "
                          f"{pct(n_ba, n)} [{100 * lo:.1f}, {100 * hi:.1f}] | {pct(n_tr, n)} | "
                          f"{pct(n - n_ok - n_ba - n_tr, n)} |")
    print()


def print_composition(cells, models):
    print("## (d) Composition of the errors, all five subsets pooled (tolerant, % of wrong objects)\n")
    print("Same items for every model, so rows of one split are comparable across models. B=A only exists "
          "on Adversarial, which is 1,680 of 12,935 Seen and 3,340 of 12,880 Unseen objects.\n")
    print("| model | probe | split | n wrong / n obj | " + " | ".join(CAT_HEAD[c] for c in ERR_CATS) + " |")
    print("|---|---|---|---|" + "---|" * len(ERR_CATS))
    for m in models:
        for probe in PROBES:
            for split in SPLITS:
                c, n = collections.Counter(), 0
                for sub, _ in SUBSETS:
                    cell = cells.get((m, probe, split, sub, "tolerant"))
                    if cell:
                        cc, nn = counts(cell)
                        c.update(cc)
                        n += nn
                if not n:
                    continue
                wrong = n - c["correct"]
                vals = " | ".join(pct(c[x], wrong) for x in ERR_CATS)
                print(f"| {m} | {probe} | {SPLIT_NAME[split]} | {wrong} / {n} | {vals} |")
    print()


def print_checks(chk, cells, models):
    print("## (e) Checks\n")
    print(f"- Rows read (after deduplication): {chk['rows']}. Image ids that do not match the ROPE entry: "
          f"{chk['image_id_mismatch']}. Adversarial rows whose four non-B boxes do not share one class: "
          f"{chk['adversarial_rows_without_single_A']}.")
    for pname, _, _ in PARSERS:
        print(f"- {pname}: the harness's error_type, rerun on the stored labels, differs from the stored type for "
              f"{chk[f'{pname}_harness_recomputed_mismatch']} objects. Outside cut calls, the category here maps "
              f"back to a different stored type for {chk[f'{pname}_mapping_mismatch']} of "
              f"{chk[f'{pname}_mapping_checked']} objects.")
    print()
    print("| model | probe | split | rows | objects |")
    print("|---|---|---|---|---|")
    for m in models:
        for probe in PROBES:
            for split in SPLITS:
                n_img = n_obj = 0
                for sub, _ in SUBSETS:
                    cell = cells.get((m, probe, split, sub, "tolerant"), {})
                    n_img += len(cell)
                    n_obj += sum(len(v) for v in cell.values())
                if n_img:
                    print(f"| {m} | {probe} | {SPLIT_NAME[split]} | {n_img} | {n_obj} |")
    print()


def write_csv(cells, models, path):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["model", "subset", "probe", "split", "parser", "n_images", "n_objects"] + CATS)
        for m in models:
            for sub, sname in SUBSETS:
                for probe in PROBES:
                    for split in SPLITS:
                        for pname, _, _ in PARSERS:
                            cell = cells.get((m, probe, split, sub, pname))
                            if not cell:
                                continue
                            c, n = counts(cell)
                            w.writerow([m, sname, probe, SPLIT_NAME[split], pname, len(cell), n] + [c[x] for x in CATS])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--out-dir", default=os.path.join(RESULTS, "rq3"))
    ap.add_argument("--rope-dir", default=os.environ.get("ROPE_DIR"))
    args = ap.parse_args(argv)
    if not args.rope_dir:
        sys.exit("pass --rope-dir or set ROPE_DIR (source harness/env.sh)")
    paths = args.paths or default_paths()
    rows = load_rows(paths)
    cells, chk = build(rows, load_rope(args.rope_dir))
    models = models_in(cells)
    rng = np.random.default_rng(0)
    print(f"# RQ3 Table 3: error taxonomy\n\nFiles ({len(paths)}): "
          + ", ".join(os.path.basename(p) for p in paths) + "\n")
    print_table3(cells, models, "tolerant")
    print_table3(cells, models, "strict")
    print_b_eq_a(cells, models, rng)
    print_composition(cells, models)
    print_checks(chk, cells, models)
    os.makedirs(args.out_dir, exist_ok=True)
    write_csv(cells, models, os.path.join(args.out_dir, "rq3_table3.csv"))


if __name__ == "__main__":
    main()
