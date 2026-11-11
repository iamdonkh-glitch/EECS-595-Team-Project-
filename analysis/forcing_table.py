#!/usr/bin/env python
"""Table 4 (RQ2 forcing probes) and Figure 4 (dose-response), read-only.

Unit: the odd object B of each Adversarial image (box 5 in AAAAB, box 1 in BAAAA). For each model,
split and order, B is compared under every condition on the same images:
  single, default                   from results/*/rq1_*.jsonl
  TF incremental, TF one-shot, CF   from results/*/forcing_*.jsonl, plus the --n-given and
                                    --prefix-place assistant variants of the one-shot probes
Outcomes per B: correct; labelled A (inertia: the class of the other four objects); labelled C
(counterfactual: the injected class). Rows with --budget, --no-think or non-greedy decoding are left out.
Homogeneous control: when a forcing run on `homogenous` exists, box 5 (the object the one-shot probes
ask) is compared the same way; there all five objects share one class, so following the labels is right.

  source harness/env.sh
  python analysis/forcing_table.py [--out-dir DIR] [jsonl ...] > table4.md
  # default input: results/*/rq1_*.jsonl and results/*/forcing_*.jsonl; default DIR: results/

Writes DIR/forcing_table4.csv and, when --n-given runs exist, DIR/forcing_fig4_dose.png.

Conventions (as analysis/rq1_table.py): tolerant parse primary, strict beside it; a call with
finish_reason == 'length' makes B wrong (and neither A nor C), kept in the denominator. CIs are 95%
percentile bootstraps over images (2,000 reps). Paired tests against default on the same images:
exact McNemar on B correct (and on B labelled A); Holm over all comparisons of one model, per outcome.
Strict labels of one-shot TF and counterfactual rows are re-read from the answer with
rope_runner.scoring.keyed_segment (the segment keyed objK), whatever scorer wrote the row.
"""
import csv
import glob
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rq1_table as rq1  # noqa: E402  (also puts harness/ on sys.path)
from rope_runner.scoring import keyed_segment  # noqa: E402

ORDERS = [("Adversarial", ("AAAAB", "BAAAA")), ("AAAAB", ("AAAAB",)), ("BAAAA", ("BAAAA",)),
          ("Homogeneous control", ("homogenous",))]
# Homogeneous control: all five objects share one class, so following the given labels is correct.
# The one-shot probes ask box 5 there; its rows appear only when a forcing run on homogenous exists.
CONTROL = "Homogeneous control"
BASE = ["single", "default", "TF incremental", "TF one-shot", "CF"]


def default_paths():
    pats = [os.path.join(rq1.RESULTS, "*", "rq1_*.jsonl"), os.path.join(rq1.RESULTS, "*", "forcing_*.jsonl")]
    return sorted(p for pat in pats for p in glob.glob(pat) if "parser_audit" not in os.path.basename(p))


def condition(r):
    """Condition name of a row, or None when the row is out of scope."""
    if r.get("budget") or r.get("no_think") or not str(r.get("variant", "")).startswith("greedy"):
        return None
    p = r["probe"]
    if p in ("default", "single"):
        return p
    if p == "teacher_forcing" and r.get("tf_mode") == "incremental":
        return "TF incremental"
    if p not in ("teacher_forcing", "counterfactual"):
        return None
    name = "TF one-shot" if p == "teacher_forcing" else "CF"
    if r.get("n_given") is not None and r["n_given"] != 4:
        name += f", given={r['n_given']}"
    if r.get("prefix_place", "user") == "assistant":
        name += ", assistant"
    return name


def b_record(r):
    """Outcomes for B in one row: {t,s: {ok, A, C}, cut}. None if the row does not score B.
    On homogenous (the control) "B" is box 5, the object the one-shot probes ask."""
    sub = r["subset"]
    if sub not in ("AAAAB", "BAAAA", "homogenous"):
        return None
    b = 1 if sub == "BAAAA" else 5
    objs = r["obj_indices"]
    if b not in objs:
        return None
    i = objs.index(b)
    fr = r["finish_reason"]
    call = 0 if len(fr) == 1 else (r.get("asked_objects") or objs).index(b)
    cut = fr[call] == "length"
    gold = r["all_gold_labels"]
    a_cls = gold[1] if b == 1 else gold[0]
    cf = r.get("counterfactual_class")
    strict = r["parsed_labels"][i]
    if len(objs) == 1:  # one-shot TF / counterfactual: read strict by key
        strict = keyed_segment(r["stripped_answer"][0], b)
    rec = {"cut": cut}
    for tag, lab in (("t", r["tolerant_labels"][i]), ("s", strict)):
        rec[tag] = {"ok": 0, "A": 0, "C": 0} if cut else {
            "ok": int(lab == gold[b - 1]), "A": int(lab == a_cls), "C": int(cf is not None and lab == cf)}
    return rec


def load(paths):
    """{(model, condition, split, subset): {(entry_idx, image_id): rec}}"""
    data = {}
    for r in rq1.load_rows(paths):
        c = condition(r)
        if c is None:
            continue
        rec = b_record(r)
        if rec is None:
            continue
        data.setdefault((r["model"], c, r["split"], r["subset"]), {})[(r["entry_idx"], r["image_id"])] = rec
    return data


def cell(data, model, cond, split, subs):
    out = {}
    for sub in subs:
        for k, rec in data.get((model, cond, split, sub), {}).items():
            out[(sub,) + k] = rec
    return out


def rate(recs, tag, what):
    v = [r[tag][what] for r in recs]
    return float(np.mean(v)) if v else float("nan"), rq1.boot_mean(v)


def paired(x, y, tag, what):
    """y - x on common images: mean diff, bootstrap CI, McNemar (b = 1 only under x, c = only under y)."""
    keys = sorted(set(x) & set(y), key=str)
    if not keys:
        return None
    xv = [x[k][tag][what] for k in keys]
    yv = [y[k][tag][what] for k in keys]
    b = sum(1 for a, c in zip(xv, yv) if a and not c)
    c = sum(1 for a, cc in zip(xv, yv) if cc and not a)
    d = [cc - a for a, cc in zip(xv, yv)]
    return dict(n=len(keys), diff=float(np.mean(d)), ci=rq1.boot_mean(d), b=b, c=c, p=rq1.mcnemar_exact(b, c))


def conditions_of(data, model):
    have = {k[1] for k in data if k[0] == model}
    extra = sorted(c for c in have if c not in BASE)
    return [c for c in BASE if c in have] + extra


def table4(data):
    rows = []
    for m in sorted({k[0] for k in data}):
        for sp in rq1.SPLITS:
            for oname, subs in ORDERS:
                if oname == CONTROL and not any(cell(data, m, c, sp, subs) for c in conditions_of(data, m)
                                                if c not in ("default", "single")):
                    continue
                base = cell(data, m, "default", sp, subs)
                for cond in conditions_of(data, m):
                    g = cell(data, m, cond, sp, subs)
                    if not g:
                        continue
                    recs = list(g.values())
                    row = dict(model=m, split=rq1.SPLIT_NAME[sp], order=oname, condition=cond, n_images=len(recs),
                               n_cut=sum(r["cut"] for r in recs))
                    for tag in ("t", "s"):
                        for what in ("ok", "A", "C"):
                            row[f"{what}_{tag}"], row[f"{what}_{tag}_ci"] = rate(recs, tag, what)
                    if cond != "default" and base:
                        row["vs_ok"] = paired(base, g, "t", "ok")
                        row["vs_ok_s"] = paired(base, g, "s", "ok")
                        if oname != CONTROL:
                            row["vs_A"] = paired(base, g, "t", "A")
                    rows.append(row)
    # Holm: per model, over its comparisons with default, per outcome
    for m in {r["model"] for r in rows}:
        for key in ("vs_ok", "vs_A", "vs_ok_s"):
            rs = [r for r in rows if r["model"] == m and r.get(key)]
            for r, a in zip(rs, rq1.holm([r[key]["p"] for r in rs])):
                r[key]["holm"] = a
    return rows


def cmp_s(v):
    if not v:
        return "-", "-"
    return f"{rq1.pp(v['diff'])} {rq1.ci_s(v['ci'], rq1.pp)}", f"{rq1.fp(v['p'])} ({rq1.fp(v['holm'])})"


def print_table4(rows):
    print("## Table 4: the odd object B under each condition (%)\n")
    print("B acc = B named correctly; B=A = B given the class of the other four (inertia); B=C = B given the "
          "counterfactual class. Tolerant parse, strict in parentheses. cut = calls for B at the token limit "
          "(scored wrong). vs default = paired on the same images, y - x in points; p = exact McNemar, Holm over "
          "the model's comparisons.\n")
    print("| model | split | order | condition | n img | cut | B acc [95% CI] | B=A [95% CI] | B=C | "
          "acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        acc_d, acc_p = cmp_s(r.get("vs_ok"))
        a_d, a_p = cmp_s(r.get("vs_A"))
        c_cell = f"{rq1.pct(r['C_t'])} ({rq1.pct(r['C_s'])})" if r["condition"].startswith("CF") else "-"
        a_cell = f"{rq1.pct(r['A_t'])} ({rq1.pct(r['A_s'])}) {rq1.ci_s(r['A_t_ci'])}"
        if r["order"] == CONTROL:  # B = A there: inertia is not defined
            a_cell, a_d, a_p = "-", "-", "-"
        print(f"| {r['model']} | {r['split']} | {r['order']} | {r['condition']} | {r['n_images']} | {r['n_cut']} | "
              f"{rq1.pct(r['ok_t'])} ({rq1.pct(r['ok_s'])}) {rq1.ci_s(r['ok_t_ci'])} | "
              f"{a_cell} | {c_cell} | {acc_d} | {acc_p} | {a_d} | {a_p} |")
    print()


def write_csv(rows, path):
    cols = ["model", "split", "order", "condition", "n_images", "n_cut"]
    for tag in ("t", "s"):
        for what in ("ok", "A", "C"):
            cols += [f"{what}_{tag}", f"{what}_{tag}_lo", f"{what}_{tag}_hi"]
    cols += ["acc_vs_default", "acc_vs_default_lo", "acc_vs_default_hi", "acc_vs_default_p", "acc_vs_default_holm",
             "A_vs_default", "A_vs_default_p", "A_vs_default_holm"]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            d = dict(r)
            for tag in ("t", "s"):
                for what in ("ok", "A", "C"):
                    d[f"{what}_{tag}_lo"], d[f"{what}_{tag}_hi"] = r[f"{what}_{tag}_ci"]
            v, a = r.get("vs_ok"), r.get("vs_A")
            d.update(acc_vs_default=v and v["diff"], acc_vs_default_lo=v and v["ci"][0], acc_vs_default_hi=v and v["ci"][1],
                     acc_vs_default_p=v and v["p"], acc_vs_default_holm=v and v["holm"],
                     A_vs_default=a and a["diff"], A_vs_default_p=a and a["p"], A_vs_default_holm=a and a["holm"])
            w.writerow([round(d[c], 6) if isinstance(d[c], float) else ("" if d[c] is None else d[c]) for c in cols])


# ------------------------------------------------------------------ Figure 4: dose-response
def dose(data):
    """Pooled Adversarial: per model, split, probe (TF / CF) and n given labels (0-4): B acc, B=A, B=C."""
    out = []
    for m in sorted({k[0] for k in data}):
        for sp in rq1.SPLITS:
            for probe in ("TF one-shot", "CF"):
                pts = []
                for n in range(5):
                    cond = probe if n == 4 else f"{probe}, given={n}"
                    recs = list(cell(data, m, cond, sp, ("AAAAB", "BAAAA")).values())
                    if recs:
                        pts.append(dict(n=n, n_img=len(recs), **{w: rate(recs, "t", w) for w in ("ok", "A", "C")}))
                if len(pts) >= 2:
                    out.append(dict(model=m, split=sp, probe=probe, pts=pts))
    return out


PLOT = r'''
import json, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
d = json.load(sys.stdin)
panels = [("TF one-shot", "ok", "TF: B named correctly"), ("TF one-shot", "A", "TF: B labelled A (inertia)"),
          ("CF", "C", "CF: B labelled C (copied)")]
models = sorted(set(s["model"] for s in d["series"]))
colors = dict(zip(models, ["#1f77b4", "#d62728", "#2ca02c", "#9467bd"]))
fig, axes = plt.subplots(2, 3, figsize=(12, 7), sharex=True, squeeze=False)
for i, sp in enumerate(["train", "validation"]):
    for j, (probe, what, title) in enumerate(panels):
        ax = axes[i][j]
        for s in d["series"]:
            if s["split"] != sp or s["probe"] != probe:
                continue
            x = [p["n"] for p in s["pts"]]
            y = [100 * p[what][0] for p in s["pts"]]
            lo = [100 * (p[what][0] - p[what][1][0]) for p in s["pts"]]
            hi = [100 * (p[what][1][1] - p[what][0]) for p in s["pts"]]
            ax.errorbar(x, y, yerr=[lo, hi], marker="o", capsize=3, color=colors[s["model"]], label=s["model"])
        ax.set_title(title + " - " + {"train": "Seen", "validation": "Unseen"}[sp], fontsize=9)
        ax.set_xticks(range(5))
        ax.grid(alpha=0.3)
        if i == 1:
            ax.set_xlabel("labels given before B (of 4)")
    axes[i][0].set_ylabel("% of B objects (tolerant)")
h, l = [], []
for ax in axes.flat:
    for hh, ll in zip(*ax.get_legend_handles_labels()):
        if ll not in l:
            h.append(hh); l.append(ll)
fig.legend(h, l, loc="lower center", ncol=4, fontsize=8)
fig.tight_layout(rect=(0, 0.06, 1, 1))
fig.savefig(d["out"], dpi=150)
'''


def print_dose(series):
    print("## Figure 4 data: dose-response (pooled Adversarial, tolerant, %)\n")
    print("| model | split | probe | labels given | n img | B acc [95% CI] | B=A [95% CI] | B=C [95% CI] |")
    print("|---|---|---|---|---|---|---|---|")
    for s in series:
        for p in s["pts"]:
            cells = " | ".join(f"{rq1.pct(p[w][0])} {rq1.ci_s(p[w][1])}" for w in ("ok", "A", "C"))
            print(f"| {s['model']} | {rq1.SPLIT_NAME[s['split']]} | {s['probe']} | {p['n']} | {p['n_img']} | {cells} |")
    print()


def plot(series, out):
    payload = json.dumps(dict(out=out, series=series))
    try:
        import matplotlib  # noqa: F401
        py = sys.executable
    except ImportError:
        py = "/usr/bin/python3"  # the venv has no matplotlib
    subprocess.run([py, "-c", PLOT], input=payload.encode(), check=True)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    out_dir = rq1.RESULTS
    if "--out-dir" in argv:
        i = argv.index("--out-dir")
        out_dir = argv[i + 1]
        del argv[i:i + 2]
    paths = argv or default_paths()
    data = load(paths)
    print(f"# RQ2 forcing probes\n\nFiles ({len(paths)}): " + ", ".join(os.path.basename(p) for p in paths) + "\n")
    rows = table4(data)
    print_table4(rows)
    write_csv(rows, os.path.join(out_dir, "forcing_table4.csv"))
    series = dose(data)
    if series:
        print_dose(series)
        plot(series, os.path.join(out_dir, "forcing_fig4_dose.png"))


if __name__ == "__main__":
    main()
