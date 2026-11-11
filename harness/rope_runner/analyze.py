"""NEW. Aggregate run JSONL(s): per-object accuracy by split/subset/position (strict = moh,
tolerant = new), moh's official accuracy (with its denominator quirks), and error-type rates.

  python -m rope_runner.analyze runs/x.jsonl [more.jsonl ...] [--tolerant-errors]
"""
import argparse
import json
from collections import Counter, defaultdict

TYPES = ["inertia", "borrowed", "invented", "copied_prefix", "off_list", "unparsed"]


def load(paths):
    rows = {}
    for p in paths:
        with open(p) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                rows[r["key"]] = r  # last write wins
    return list(rows.values())


def pct(a, b):
    return f"{100 * a / b:5.1f}" if b else "  n/a"


def summarize(rows, tolerant_errors=False):
    groups = defaultdict(list)
    for r in rows:
        groups[(r["model"], r["probe"], r["variant"], r["split"], r["subset"])].append(r)
    out = []
    for g, rs in sorted(groups.items()):
        pos_c, pos_n = Counter(), Counter()
        s_c = t_c = n_obj = moh_tot = 0
        et = Counter()
        think, forced, calls = [], 0, 0
        for r in rs:
            for k, c, tc in zip(r["obj_indices"], r["correct_flags"], r["tolerant_correct_flags"]):
                pos_n[k] += 1
                pos_c[k] += c
                s_c += c
                t_c += tc
                n_obj += 1
            moh_tot += r["moh_total"]
            et.update(e for e in r["tolerant_error_types" if tolerant_errors else "error_types"] if e)
            think += r["thinking_tokens"]
            forced += sum(r["forced_close"])
            calls += len(r["forced_close"])
        out.append({
            "group": g, "n_images": len(rs), "n_obj": n_obj,
            "strict": pct(s_c, n_obj), "tolerant": pct(t_c, n_obj), "moh_official": pct(s_c, moh_tot),
            "pos": {k: pct(pos_c[k], pos_n[k]) for k in sorted(pos_n)},
            "errors": {t: pct(et[t], n_obj) for t in TYPES},
            "mean_think": sum(think) / len(think) if think else 0, "forced_close": pct(forced, calls),
        })
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", nargs="+")
    ap.add_argument("--tolerant-errors", action="store_true", help="type errors on the tolerant parse")
    args = ap.parse_args(argv)
    res = summarize(load(args.jsonl), args.tolerant_errors)
    hdr = ("model", "probe", "variant", "split", "subset", "imgs", "strict", "toler", "moh",
           "p1", "p2", "p3", "p4", "p5") + tuple(TYPES) + ("think", "forced")
    print("\t".join(hdr))
    for s in res:
        pos = [s["pos"].get(k, "    -") for k in range(1, 6)]
        print("\t".join(list(s["group"]) + [str(s["n_images"]), s["strict"], s["tolerant"], s["moh_official"]]
                        + pos + [s["errors"][t] for t in TYPES] + [f"{s['mean_think']:.0f}", s["forced_close"]]))
    print(f"\naccuracy and error rates in % of scored objects; 'moh' = correct / moh's total_predictions "
          f"(counts a default-probe parse failure as 10); error types on the "
          f"{'tolerant' if args.tolerant_errors else 'strict'} parse.")


if __name__ == "__main__":
    main()
