"""Labels in the answer against labels in the user turn, paired, for a model without an RQ1 run.

  python analysis/place_tests.py <model> <jsonl ...>   (from the repository root)

For each split and order: B=A under "TF one-shot, assistant" against "TF one-shot" (labels in the user
turn) and against "TF one-shot, given=0" (no labels, same one-shot format), and B=C under
"CF, assistant" against "CF". Paired on the same images, exact McNemar, Holm over the rows printed for
one split; "uncut" repeats each on the images where neither call was cut.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "analysis"))
import forcing_table as ft  # noqa: E402

model, paths = sys.argv[1], sys.argv[2:]
data = ft.load(paths)
COMPARE = [("TF one-shot, assistant", "TF one-shot", "A"), ("TF one-shot, assistant", "TF one-shot, given=0", "A"),
           ("CF, assistant", "CF", "C")]


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    out, run = [None] * len(ps), 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i]))
        out[i] = run
    return out


print("| split | order | y | x | what | n | x % | y % | y - x [CI] | b/c | p | p (Holm) | uncut n | uncut y - x | uncut p |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for split in ("Unseen", "Seen"):
    sp = "validation" if split == "Unseen" else "train"
    rows = []
    for order in ("AAAAB", "BAAAA"):
        for ycond, xcond, what in COMPARE:
            x = ft.cell(data, model, xcond, sp, [order])
            y = ft.cell(data, model, ycond, sp, [order])
            if not x or not y:
                continue
            r = ft.paired(x, y, "t", what)
            keep = [k for k in set(x) & set(y) if not x[k]["cut"] and not y[k]["cut"]]
            u = ft.paired({k: x[k] for k in keep}, {k: y[k] for k in keep}, "t", what)
            xr = sum(x[k]["t"][what] for k in set(x) & set(y)) / r["n"]
            rows.append([split, order, ycond, xcond, what, r, xr, u])
    hp = holm([r[5]["p"] for r in rows])
    for (split, order, ycond, xcond, what, r, xr, u), h in zip(rows, hp):
        print(f"| {split} | {order} | {ycond} | {xcond} | B={what} | {r['n']} | {100*xr:.1f} | {100*(xr+r['diff']):.1f} "
              f"| {100*r['diff']:+.1f} [{100*r['ci'][0]:+.1f}, {100*r['ci'][1]:+.1f}] | {r['b']}/{r['c']} | {r['p']:.2g} "
              f"| {h:.2g} | {u['n']} | {100*u['diff']:+.1f} | {u['p']:.2g} |")
