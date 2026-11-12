#!/usr/bin/env python
"""Box swaps inside B=A (read-only). When B is labelled A, does the answer still name B's class, but on
one of the other four boxes? Such an answer saw B and put it on the wrong box, so it is box confusion
rather than a missed object. Works on Adversarial (AAAAB / BAAAA) rows of any model.

  python analysis/box_swap.py <jsonl> [<jsonl> ...] > box_swap.md
  # e.g. results/<model>/rq1_<model>_adversarial_{default,single}_*.jsonl
  #      results/<model>/forcing_<model>_{tf-oneshot,cf}_*.jsonl results/<model>/forcing_cf{near,far}_*.jsonl

Standard library only (the class lists and the tolerant parser come from harness/rope_runner).

Table 1, per model x split x order x condition, over calls that label all five boxes in one answer
(Default; one-shot forcing with the labels in the user turn when the answer rewrites the list): B=A,
how many of those B=A answers write B's class on another box, and how many answers write B's class on
an A box at all. A call cut by the token limit is left out here.

Table 2, Default against Single-object on the same images (as in rq1_table / forcing_table: tolerant,
a cut call is wrong and not A): the B=A gain in points, and the gain left when a Default B=A answer
that writes B's class on another box is not counted as A.
"""
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "harness"))
from rope_runner.data import candidates  # noqa: E402
from rope_runner.scoring import tolerant_multi  # noqa: E402

ORDERS = ("AAAAB", "BAAAA")


def b_index(order):
    """0-based box of B."""
    return 0 if order == "BAAAA" else 4


def five(r):
    """{box (1-5): label} from the row's single answer, or None if it does not label all five."""
    found = tolerant_multi(r["stripped_answer"][0], candidates(r["split"], r["data_source"]))
    return found if all(k in found for k in range(1, 6)) else None


def condition(r):
    if r["probe"] == "default":
        return "default"
    if r["probe"] == "teacher_forcing" and r.get("tf_mode") == "oneshot":
        return "TF one-shot"
    if r["probe"] == "counterfactual":
        return "CF" + (" " + r["cf_mode"] if r.get("cf_mode") in ("near", "far") else "")
    return None


def swap_counts(rows):
    """Table 1 counts: {(model, split, order, condition): Counter}."""
    out = defaultdict(Counter)
    for r in rows:
        order = r["subset"]
        cond = condition(r)
        if order not in ORDERS or cond is None or len(r["raw_output"]) != 1:
            continue
        if r.get("prefix_place") == "assistant" or r.get("n_given") is not None:
            continue
        if r["finish_reason"][0] == "length":
            continue
        lab = five(r)
        if lab is None:
            continue
        gold = [g.lower() for g in r["all_gold_labels"]]
        b = b_index(order)
        a, gb = gold[1 if b == 0 else 0], gold[b]
        others = [lab[k] for k in range(1, 6) if k != b + 1]
        c = out[(r["model"], r["split"], order, cond)]
        c["n"] += 1
        c["B on an A box"] += gb in others
        if lab[b + 1] == a:
            c["B=A"] += 1
            c["B=A, B on an A box"] += gb in others
    return out


def b_is_a(r, j=0):
    """Tolerant B=A for call j of a row (a cut call is not A)."""
    if r["finish_reason"][j] == "length":
        return False
    gold = [g.lower() for g in r["all_gold_labels"]]
    b = b_index(r["subset"])
    a = gold[1 if b == 0 else 0]
    k = r["obj_indices"].index(b + 1) if r["probe"] == "single" else b
    return (r["tolerant_labels"][k] or "").lower() == a


def default_vs_single(rows):
    """Table 2: {(model, split, order): (n, gain points, gain points without swaps)}."""
    by = defaultdict(dict)
    for r in rows:
        if r["subset"] in ORDERS and r["probe"] in ("default", "single"):
            by[(r["model"], r["split"], r["subset"])].setdefault(r["probe"], {})[
                (r["image_id"], r["entry_idx"])] = r
    out = {}
    for key, d in sorted(by.items()):
        if "default" not in d or "single" not in d:
            continue
        both = sorted(set(d["default"]) & set(d["single"]))
        b = b_index(key[2])
        up = down = swapped = 0
        for img in both:
            rd, rs = d["default"][img], d["single"][img]
            jd = rs["obj_indices"].index(b + 1)
            da, sa = b_is_a(rd), b_is_a(rs, jd)
            if da and not sa:
                up += 1
                lab = five(rd)
                gb = rd["all_gold_labels"][b].lower()
                swapped += lab is not None and gb in [lab[k] for k in range(1, 6) if k != b + 1]
            elif sa and not da:
                down += 1
        n = len(both)
        out[key] = (n, 100 * (up - down) / n, 100 * (up - swapped - down) / n, up, swapped, down)
    return out


def main(paths):
    rows = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            rows += [json.loads(line) for line in f if line.strip()]
    print("# Box swaps inside B=A\n")
    print("Calls that label all five boxes in one answer, not cut. \"B on an A box\": the gold class of B is "
          "written on one of the four A boxes.\n")
    print("| model | split | order | condition | n | B=A | of which B on an A box | B on an A box (all answers) |")
    print("|---|---|---|---|---|---|---|---|")
    for key, c in sorted(swap_counts(rows).items()):
        n, ba, mv, any_ = c["n"], c["B=A"], c["B=A, B on an A box"], c["B on an A box"]
        split = "Seen" if key[1] == "train" else "Unseen"
        print(f"| {key[0]} | {split} | {key[2]} | {key[3]} | {n} | {ba} ({100 * ba / n:.1f}%) | "
              f"{mv} ({100 * mv / ba if ba else 0:.0f}% of B=A) | {any_} ({100 * any_ / n:.1f}%) |")
    t2 = default_vs_single(rows)
    if t2:
        print("\n## Default against Single-object: how much of the B=A gain is box swaps\n")
        print("Same images, tolerant, a cut call is wrong and not A. \"Without swaps\": a Default B=A answer that "
              "writes B's class on an A box is not counted as A.\n")
        print("| model | split | order | n img | Default up / Single up | of the Default up: B on an A box | "
              "B=A gain (points) | gain without swaps |")
        print("|---|---|---|---|---|---|---|---|")
        for (m, sp, o), (n, g, g2, up, sw, down) in t2.items():
            split = "Seen" if sp == "train" else "Unseen"
            print(f"| {m} | {split} | {o} | {n} | {up} / {down} | {sw} | {g:+.1f} | {g2:+.1f} |")


if __name__ == "__main__":
    main(sys.argv[1:])
