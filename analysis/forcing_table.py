#!/usr/bin/env python
"""Table 4 (RQ2 forcing probes) and Figure 4 (dose-response), read-only.

Unit: the odd object B of each Adversarial image (box 5 in AAAAB, box 1 in BAAAA). For each model,
split and order, B is compared under every condition on the same images:
  single, default                   from results/*/rq1_*.jsonl
  TF incremental, TF one-shot, CF   from results/*/forcing_*.jsonl, plus the --n-given and
                                    --prefix-place assistant variants of the one-shot probes, and
                                    CF near / CF far (--cf-class: C most / least similar to A)
Outcomes per B: correct; labelled A (inertia: the class of the other four objects); labelled C
(counterfactual: the injected class). Rows with --budget, --no-think or non-greedy decoding are left out.
Homogeneous control: when a forcing run on `homogenous` exists, box 5 (the object the one-shot probes
ask) is compared the same way; there all five objects share one class, so following the labels is right.

  source harness/env.sh
  python analysis/forcing_table.py [--out-dir DIR] [jsonl ...] > table4.md
  # default input: results/*/rq1_*.jsonl and results/*/forcing_*.jsonl; default DIR: results/

Writes DIR/forcing_table4.csv and, when --n-given runs exist, DIR/forcing_fig4_dose.png and
DIR/forcing_fig4_tests.csv (each dose against given=0, and the per-image slope over labels given).

Conventions (as analysis/rq1_table.py): tolerant parse primary, strict beside it; a call with
finish_reason == 'length' makes B wrong (and neither A nor C), kept in the denominator. CIs are 95%
percentile bootstraps over images (2,000 reps). Paired tests against default, and separately against
single (B asked alone), on the same images: exact McNemar on B correct (and on B labelled A); Holm over
all comparisons of one model with that reference, per outcome.
Strict labels of one-shot TF and counterfactual rows are re-read from the answer with
rope_runner.scoring.keyed_segment (the segment keyed objK), whatever scorer wrote the row.
Assistant-turn prefill rows are read with rope_runner.scoring.prefill_labels: Table 4 uses the label
written right after the prefill, and a row counts as cut only when thinking never closed (the model
may keep writing after the label until the token limit; that later text is a re-check, not the label).
A second table reports what follows the forced line: how often the model kept writing, and its final
label for B.
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
from rope_runner.data import candidates  # noqa: E402
from rope_runner.scoring import keyed_segment, prefill_labels  # noqa: E402

ORDERS = [("Adversarial", ("AAAAB", "BAAAA")), ("AAAAB", ("AAAAB",)), ("BAAAA", ("BAAAA",)),
          ("Homogeneous control", ("homogenous",))]
# Homogeneous control: all five objects share one class, so following the given labels is correct.
# The one-shot probes ask box 5 there; its rows appear only when a forcing run on homogenous exists.
CONTROL = "Homogeneous control"
BASE = ["single", "default", "TF incremental", "TF one-shot", "CF", "CF near", "CF far"]


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
    if p == "counterfactual" and r.get("cf_mode") in ("near", "far"):
        name += " " + r["cf_mode"]  # C most / least similar to A (run.py --cf-class)
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
    tol, strict = r["tolerant_labels"][i], r["parsed_labels"][i]
    if len(objs) == 1:  # one-shot TF / counterfactual: read strict by key
        strict = keyed_segment(r["stripped_answer"][0], b)
    out = lambda lab: {"ok": int(lab == gold[b - 1]), "A": int(lab == a_cls), "C": int(cf is not None and lab == cf)}
    rec = {}
    if r.get("prefix_place", "user") == "assistant":
        # the label written right after the prefill; cut only when thinking never closed
        pl = prefill_labels(r["stripped_answer"][0], r["prefix_used"][0], b,
                            candidates(r["split"], r["data_source"]), fr[0])
        cut = pl is None
        tol, strict = (pl["first_t"], pl["first_s"]) if pl else (None, None)
        rec["more"] = int(bool(pl and pl["more"]))
        # wrote no label after the forced "objK:" and started its own list on a new line instead
        rec["restart"] = int(bool(pl and pl["first_s"] is None and pl["more"]))
        rec["f"] = out(pl["final_t"] if pl else None)
        rec["unresolved"] = int(bool(pl and pl["more"] and pl["final_t"] is None))
    rec["cut"] = cut
    for tag, lab in (("t", tol), ("s", strict)):
        rec[tag] = {"ok": 0, "A": 0, "C": 0} if cut else out(lab)
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
                alone = cell(data, m, "single", sp, subs)
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
                        # sensitivity: only images where neither call for B hit the token limit
                        keep = [k for k in base if k in g and not base[k]["cut"] and not g[k]["cut"]]
                        bu, gu = {k: base[k] for k in keep}, {k: g[k] for k in keep}
                        row["vs_ok_uncut"] = paired(bu, gu, "t", "ok")
                        if oname != CONTROL:
                            row["vs_A"] = paired(base, g, "t", "A")
                            row["vs_A_uncut"] = paired(bu, gu, "t", "A")
                    if cond != "single" and alone:
                        # against B asked alone (the proposal's reference for inertia from context)
                        row["vs1_ok"] = paired(alone, g, "t", "ok")
                        if oname != CONTROL:
                            row["vs1_A"] = paired(alone, g, "t", "A")
                    rows.append(row)
    # Holm: per model, over its comparisons with default (or with single), per outcome
    for m in {r["model"] for r in rows}:
        for key in ("vs_ok", "vs_A", "vs_ok_s", "vs_ok_uncut", "vs_A_uncut", "vs1_ok", "vs1_A"):
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


def print_uncut(rows):
    """Sensitivity for Table 4: a cut call scores B wrong and never A, so a condition with fewer cuts
    than default gains B=A from that alone. Here only images where neither call was cut count."""
    rows = [r for r in rows if r.get("vs_ok_uncut")]
    if not rows:
        return
    print("## Table 4, sensitivity: images where neither call for B hit the token limit\n")
    print("Same comparisons with default as Table 4 (tolerant, y - x in points, exact McNemar, Holm over the "
          "model's comparisons), on the images where neither the condition's nor default's call for B was cut.\n")
    print("| model | split | order | condition | n img | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        acc_d, acc_p = cmp_s(r["vs_ok_uncut"])
        a_d, a_p = cmp_s(r.get("vs_A_uncut"))
        print(f"| {r['model']} | {r['split']} | {r['order']} | {r['condition']} | {r['vs_ok_uncut']['n']} | "
              f"{acc_d} | {acc_p} | {a_d} | {a_p} |")
    print()


def print_vs_single(rows):
    """Table 4 against Single-object: B asked alone, with no other answer or label in context."""
    rows = [r for r in rows if r.get("vs1_ok")]
    if not rows:
        return
    print("## Table 4, against Single-object (B asked alone)\n")
    print("Same images, tolerant, y - x in points, exact McNemar, Holm over the model's comparisons with "
          "Single-object. Single-object asks one box per turn with the official single-object prompt, so this "
          "gap holds both the multi-object format (default) and the given labels.\n")
    print("| model | split | order | condition | n img | acc vs single [CI] | p (Holm) | B=A vs single [CI] | p (Holm) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        acc_d, acc_p = cmp_s(r["vs1_ok"])
        a_d, a_p = cmp_s(r.get("vs1_A"))
        print(f"| {r['model']} | {r['split']} | {r['order']} | {r['condition']} | {r['vs1_ok']['n']} | "
              f"{acc_d} | {acc_p} | {a_d} | {a_p} |")
    print()


def after_prefill(data):
    """Assistant-turn prefill conditions: what the model does after writing the forced line."""
    rows = []
    for m in sorted({k[0] for k in data}):
        for sp in rq1.SPLITS:
            for oname, subs in ORDERS:
                for cond in conditions_of(data, m):
                    if not cond.endswith(", assistant"):
                        continue
                    recs = list(cell(data, m, cond, sp, subs).values())
                    if not recs:
                        continue
                    row = dict(model=m, split=rq1.SPLIT_NAME[sp], order=oname, condition=cond, n_images=len(recs),
                               n_cut=sum(r["cut"] for r in recs))
                    for what in ("more", "restart", "unresolved"):
                        row[what] = rate([{"x": {"v": r[what]}} for r in recs], "x", "v")
                    for what in ("ok", "A", "C"):
                        row[f"first_{what}"] = rate(recs, "t", what)
                        row[f"final_{what}"] = rate(recs, "f", what)
                    rows.append(row)
    return rows


def print_after_prefill(rows):
    print("## Assistant-turn prefill: the forced line, then the model's own re-check (%)\n")
    print("first = the label written right after the prefill (the one Table 4 uses); kept writing = the model "
          "went on after it (typically \"Wait, no, that's wrong\" and a re-check); restarted = wrote no label "
          "after the forced \"objK:\" and began its own five-label list on a new line (counted in kept writing; "
          "first counts as wrong and not A); final = obj K's last "
          "\"objK: <class>\" in the answer (= first when it stopped); unresolved = kept writing but gave no final "
          "label for B, or hit the token limit. cut = thinking never closed. All over n img, tolerant.\n")
    print("| model | split | order | condition | n img | cut | first: B acc | first: B=A | first: B=C | kept writing | "
          "restarted | final: B acc | final: B=A | final: B=C | unresolved |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        cf = r["condition"].startswith("CF")
        c = lambda k: rq1.pct(r[k][0])
        print(f"| {r['model']} | {r['split']} | {r['order']} | {r['condition']} | {r['n_images']} | {r['n_cut']} | "
              f"{c('first_ok')} | {c('first_A')} | {c('first_C') if cf else '-'} | {c('more')} | {c('restart')} | "
              f"{c('final_ok')} | {c('final_A')} | {c('final_C') if cf else '-'} | {c('unresolved')} |")
    print()


def write_csv(rows, path):
    cols = ["model", "split", "order", "condition", "n_images", "n_cut"]
    for tag in ("t", "s"):
        for what in ("ok", "A", "C"):
            cols += [f"{what}_{tag}", f"{what}_{tag}_lo", f"{what}_{tag}_hi"]
    cols += ["acc_vs_default", "acc_vs_default_lo", "acc_vs_default_hi", "acc_vs_default_p", "acc_vs_default_holm",
             "A_vs_default", "A_vs_default_p", "A_vs_default_holm",
             "n_uncut", "acc_vs_default_uncut", "acc_vs_default_uncut_p", "acc_vs_default_uncut_holm",
             "A_vs_default_uncut", "A_vs_default_uncut_p", "A_vs_default_uncut_holm",
             "acc_vs_single", "acc_vs_single_lo", "acc_vs_single_hi", "acc_vs_single_p", "acc_vs_single_holm",
             "A_vs_single", "A_vs_single_lo", "A_vs_single_hi", "A_vs_single_p", "A_vs_single_holm"]
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
            vu, au = r.get("vs_ok_uncut"), r.get("vs_A_uncut")
            d.update(n_uncut=vu and vu["n"], acc_vs_default_uncut=vu and vu["diff"],
                     acc_vs_default_uncut_p=vu and vu["p"], acc_vs_default_uncut_holm=vu and vu["holm"],
                     A_vs_default_uncut=au and au["diff"], A_vs_default_uncut_p=au and au["p"],
                     A_vs_default_uncut_holm=au and au["holm"])
            for what, key in (("acc", "vs1_ok"), ("A", "vs1_A")):
                v = r.get(key)
                d.update({f"{what}_vs_single": v and v["diff"], f"{what}_vs_single_lo": v and v["ci"][0],
                          f"{what}_vs_single_hi": v and v["ci"][1], f"{what}_vs_single_p": v and v["p"],
                          f"{what}_vs_single_holm": v and v["holm"]})
            w.writerow([round(d[c], 6) if isinstance(d[c], float) else ("" if d[c] is None else d[c]) for c in cols])


# ------------------------------------------------------------------ Figure 4: dose-response
def dose(data):
    """Per model, split, probe (TF / CF), order (pooled Adversarial, AAAAB, BAAAA) and n given labels
    (0-4): B acc, B=A, B=C."""
    out = []
    for m in sorted({k[0] for k in data}):
        for sp in rq1.SPLITS:
            for probe in ("TF one-shot", "CF"):
                for oname, subs in ORDERS:
                    if oname == CONTROL:
                        continue
                    pts = []
                    for n in range(5):
                        cond = probe if n == 4 else f"{probe}, given={n}"
                        recs = list(cell(data, m, cond, sp, subs).values())
                        if recs:
                            pts.append(dict(n=n, n_img=len(recs), **{w: rate(recs, "t", w) for w in ("ok", "A", "C")}))
                    if len(pts) >= 2:
                        out.append(dict(model=m, split=sp, probe=probe, order=oname, pts=pts))
    return out


def slope_test(x, y, reps=10000, seed=0):
    """y: images x doses (0/1), x: the doses. Per-image least-squares slope of y over x; returns its
    mean (per label given), a bootstrap CI over images, and a two-sided permutation p with the doses
    shuffled within each image (under no dose effect an image's outcomes are exchangeable)."""
    xc = x - x.mean()
    ss = float(xc @ xc)
    s = y @ xc / ss
    obs = float(s.mean())
    rng = np.random.default_rng(seed)
    hits, done = 0, 0
    while done < reps:
        k = min(1000, reps - done)
        perm = np.argsort(rng.random((k,) + y.shape), axis=2)
        stat = (np.take_along_axis(np.broadcast_to(y, perm.shape), perm, axis=2) @ xc).mean(axis=1) / ss
        hits += int(np.sum(np.abs(stat) >= abs(obs) - 1e-12))
        done += k
    return dict(n=len(s), diff=obs, ci=rq1.boot_mean(s), p=(hits + 1) / (reps + 1))


def dose_tests(data):
    """Tests for Figure 4, per model, split, probe and order (pooled, AAAAB, BAAAA), on the images that
    have every dose point: each n labels given against given=0 (paired, exact McNemar), and the per-image
    slope over n = 0-4 (points per label, permutation p). Holm per model and outcome, separately over the
    against-0 comparisons and over the slopes. given=0 asks B alone with no labels, so it holds the prompt
    format fixed and isolates the effect of the labels themselves."""
    rows = []
    for m in sorted({k[0] for k in data}):
        for sp in rq1.SPLITS:
            for probe in ("TF one-shot", "CF"):
                for oname, subs in ORDERS:
                    if oname == CONTROL:
                        continue
                    pts = {n: cell(data, m, probe if n == 4 else f"{probe}, given={n}", sp, subs) for n in range(5)}
                    have = [n for n in range(5) if pts[n]]
                    if 0 not in have or len(have) < 2:
                        continue
                    keys = sorted(set.intersection(*(set(pts[n]) for n in have)), key=str)
                    row = dict(model=m, split=rq1.SPLIT_NAME[sp], probe=probe, order=oname, n_images=len(keys),
                               doses=have)
                    for what in ("A", "ok"):
                        for n in have[1:]:
                            row[f"vs0_{what}_{n}"] = paired({k: pts[0][k] for k in keys}, {k: pts[n][k] for k in keys},
                                                            "t", what)
                        y = np.array([[pts[n][k]["t"][what] for n in have] for k in keys], dtype=float)
                        row[f"slope_{what}"] = slope_test(np.array(have, dtype=float), y)
                    rows.append(row)
    for m in {r["model"] for r in rows}:
        for what in ("A", "ok"):
            for fam in ([f"vs0_{what}_{n}" for n in range(1, 5)], [f"slope_{what}"]):
                tests = [r[k] for r in rows if r["model"] == m for k in fam if r.get(k)]
                for t, a in zip(tests, rq1.holm([t["p"] for t in tests])):
                    t["holm"] = a
    return rows


def print_dose_tests(rows):
    print("## Figure 4 tests: labels given against none\n")
    print("Images with every dose point (tolerant). slope = per-image least-squares change per label given "
          "(0-4), in points, permutation p (doses shuffled within image). 4 vs 0 = all four labels against "
          "none, paired, exact McNemar. Holm per model and outcome.\n")
    print("| model | split | probe | order | n img | B=A slope / label [CI] | p (Holm) | B=A 4 vs 0 [CI] | p (Holm) | "
          "acc slope / label [CI] | p (Holm) | acc 4 vs 0 [CI] | p (Holm) |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        cells = []
        for what in ("A", "ok"):
            cells += cmp_s(r[f"slope_{what}"]) + cmp_s(r.get(f"vs0_{what}_4"))
        print(f"| {r['model']} | {r['split']} | {r['probe']} | {r['order']} | {r['n_images']} | " + " | ".join(cells) + " |")
    print()


def write_dose_csv(rows, path):
    cols = ["model", "split", "probe", "order", "n_images"]
    tests = [f"slope_{w}" for w in ("A", "ok")] + [f"vs0_{w}_{n}" for w in ("A", "ok") for n in range(1, 5)]
    for t in tests:
        cols += [t, t + "_lo", t + "_hi", t + "_p", t + "_holm"]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            vals = [r[c] for c in cols[:5]]
            for t in tests:
                v = r.get(t)
                vals += [round(v["diff"], 6), round(v["ci"][0], 6), round(v["ci"][1], 6), v["p"], v["holm"]] if v else [""] * 5
            w.writerow(vals)


PLOT = r'''
import json, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
d = json.load(sys.stdin)
# rows: order; columns: outcome. Colour = model, solid = Unseen, dashed = Seen (shifted right a little).
orders = [("AAAAB", "AAAAB (B in box 5)"), ("BAAAA", "BAAAA (B in box 1)")]
cols = [("A", "B labelled A (inertia)"), ("ok", "B named correctly")]
series = [s for s in d["series"] if s["probe"] == "TF one-shot"]
models = sorted(set(s["model"] for s in series))
colors = dict(zip(models, ["#1f77b4", "#d62728", "#2ca02c", "#9467bd"]))
style = {"validation": ("-", "o", -0.06, "Unseen"), "train": ("--", "s", 0.06, "Seen")}
fig, axes = plt.subplots(2, 2, figsize=(9, 7), sharex=True, squeeze=False)
for i, (order, otitle) in enumerate(orders):
    for j, (what, ctitle) in enumerate(cols):
        ax = axes[i][j]
        for s in series:
            if s["order"] != order:
                continue
            ls, mk, dx, sname = style[s["split"]]
            x = [p["n"] + dx for p in s["pts"]]
            y = [100 * p[what][0] for p in s["pts"]]
            lo = [100 * (p[what][0] - p[what][1][0]) for p in s["pts"]]
            hi = [100 * (p[what][1][1] - p[what][0]) for p in s["pts"]]
            ax.errorbar(x, y, yerr=[lo, hi], linestyle=ls, marker=mk, markersize=4, capsize=2, linewidth=1.3,
                        color=colors[s["model"]], label=f"{s['model']}, {sname}")
        ax.set_title(f"{otitle}: {ctitle}", fontsize=9)
        ax.set_xticks(range(5))
        ax.grid(alpha=0.3)
        if i == 1:
            ax.set_xlabel("true labels given before B (of the other 4)")
    axes[i][0].set_ylabel("% of B objects (tolerant, 95% CI)")
h, l = [], []
for ax in axes.flat:
    for hh, ll in zip(*ax.get_legend_handles_labels()):
        if ll not in l:
            h.append(hh); l.append(ll)
fig.legend(h, l, loc="lower center", ncol=4, fontsize=8)
fig.tight_layout(rect=(0, 0.07, 1, 1))
fig.savefig(d["out"], dpi=150)
'''


def print_dose(series):
    print("## Figure 4 data: dose-response (tolerant, %)\n")
    print("| model | split | probe | order | labels given | n img | B acc [95% CI] | B=A [95% CI] | B=C [95% CI] |")
    print("|---|---|---|---|---|---|---|---|---|")
    for s in series:
        for p in s["pts"]:
            cells = " | ".join(f"{rq1.pct(p[w][0])} {rq1.ci_s(p[w][1])}" for w in ("ok", "A", "C"))
            print(f"| {s['model']} | {rq1.SPLIT_NAME[s['split']]} | {s['probe']} | {s['order']} | {p['n']} | "
                  f"{p['n_img']} | {cells} |")
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
    print_uncut(rows)
    print_vs_single(rows)
    write_csv(rows, os.path.join(out_dir, "forcing_table4.csv"))
    ap = after_prefill(data)
    if ap:
        print_after_prefill(ap)
    series = dose(data)
    if series:
        print_dose(series)
        dt = dose_tests(data)
        print_dose_tests(dt)
        write_dose_csv(dt, os.path.join(out_dir, "forcing_fig4_tests.csv"))
        plot(series, os.path.join(out_dir, "forcing_fig4_dose.png"))


if __name__ == "__main__":
    main()
