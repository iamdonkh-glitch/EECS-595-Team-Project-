"""How often a thinking model's reasoning refers back to the given labels, by what the labels do to B.

    python analysis/think_cite.py <dose_<model>_<split>.jsonl> <forcing_<model>_tf-oneshot_<split>.jsonl>

Pairs each Adversarial image's one-shot teacher-forcing call with all four true labels given (n = 4) with
its dose call with none (n = 0), keeping images where neither call for B reached the token limit. Groups the
images by B's tolerant label at n = 0 and n = 4 ("flip to A": not A with none, A with four; "stays
correct": correct in both) and prints, per group, the share of n = 4 reasoning traces (text before
</think>) that
  - refer to the given labels: a keyword match (given, example, problem says / states / statement, the
    question / prompt / user says, provided, ...). This is rough: "example" can also mean the format
    example of the official prompt, and "given" the candidate list.
  - say that all five boxes share a class ("all five ... are"), the conclusion that usually ends in B=A.
Used for the Qwen-Thinking BAAAA paragraph of the Discussion; a keyword count, not a mechanism test.
"""
import json
import re
import sys
from collections import Counter, defaultdict

CITE = re.compile(r"\b(given|example|problem (says|states|statement)|the (question|prompt|user) (says|states|gives|lists)"
                  r"|already (labeled|labelled|given)|provided|as (stated|listed))\b", re.I)
ALL_SAME = re.compile(r"\ball (five|5|of them|the objects|objects)\b[^.\n]{0,40}\b(are|is)\b", re.I)
ORDERS = ("AAAAB", "BAAAA")


def b_call(r):
    """Return (state of B: 'A' / 'ok' / 'other', reasoning text), or None if B's call was cut."""
    gold = r["all_gold_labels"]
    a = Counter(gold).most_common(1)[0][0]
    b = next(i for i, g in enumerate(gold) if g != a)
    j = r["obj_indices"].index(b + 1)
    if r["finish_reason"][j] == "length":
        return None
    lab = r["tolerant_labels"][j]
    state = "A" if lab == a else ("ok" if lab == gold[b] else "other")
    raw = r["raw_output"]
    raw = raw[j] if isinstance(raw, list) else raw
    return state, raw.split("</think>")[0]


def load(path, want_n):
    out = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r.get("probe") != "teacher_forcing" or r.get("tf_mode") != "oneshot" or r["subset"] not in ORDERS:
                continue
            if (r.get("prefix_place") or "user") != "user":
                continue
            n = r.get("n_given")
            if (4 if n is None else n) != want_n:
                continue
            got = b_call(r)
            if got is not None:
                out[(r["subset"], r["entry_idx"])] = got
    return out


def group(s0, s4):
    if s4 == "A" and s0 != "A":
        return "flip to A"
    if s4 == "ok" and s0 == "ok":
        return "stays correct"
    if s4 == "A" and s0 == "A":
        return "A at both"
    return "other"


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    n0, n4 = load(argv[0], 0), load(argv[1], 4)
    print("| order | images (n=4 vs n=0) | n | refers to given labels | 'all five ... are' |")
    print("|---|---|---|---|---|")
    for order in ORDERS:
        groups = defaultdict(list)
        for k, (s4, think) in n4.items():
            if k[0] == order and k in n0:
                groups[group(n0[k][0], s4)].append(think)
        for g in ("flip to A", "stays correct", "A at both", "other"):
            ts = groups.get(g, [])
            if not ts:
                continue
            cite = 100 * sum(bool(CITE.search(t)) for t in ts) / len(ts)
            same = 100 * sum(bool(ALL_SAME.search(t)) for t in ts) / len(ts)
            print(f"| {order} | {g} | {len(ts)} | {cite:.1f} | {same:.1f} |")


if __name__ == "__main__":
    main()
