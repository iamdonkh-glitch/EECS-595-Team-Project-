"""Tests for analysis/box_swap.py on hand-made rows (run: python analysis/test_box_swap.py, or pytest)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import box_swap as bs  # noqa: E402

GOLD = ["person", "person", "person", "person", "handbag"]


def row(probe, answer, order="AAAAB", labels=None, finish="stop", **kw):
    gold = GOLD if order == "AAAAB" else GOLD[4:] + GOLD[:4]
    r = dict(subset=order, split="validation", data_source="COCO", model="m", image_id="1",
             entry_idx=0, probe=probe, raw_output=[answer], stripped_answer=[answer],
             finish_reason=[finish], all_gold_labels=gold, tf_mode=None, cf_class=None)
    r.update(kw)
    if probe == "single":
        r["obj_indices"] = [1, 2, 3, 4, 5]
        r["finish_reason"] = [finish] * 5
        r["raw_output"] = r["stripped_answer"] = [answer] * 5
    r["tolerant_labels"] = labels
    return r


def test_swap_counts():
    swapped = row("default", "obj1: person, obj2: handbag, obj3: person, obj4: person, obj5: person")
    missed = row("default", "obj1: person, obj2: person, obj3: person, obj4: person, obj5: person")
    right = row("default", "obj1: person, obj2: person, obj3: person, obj4: person, obj5: handbag")
    cut = row("default", "obj1: person, obj2: handbag, obj3: person, obj4: person, obj5: person", finish="length")
    short = row("teacher_forcing", "obj5: person", tf_mode="oneshot")
    c = bs.swap_counts([swapped, missed, right, cut, short])[("m", "validation", "AAAAB", "default")]
    assert (c["n"], c["B=A"], c["B=A, B on an A box"], c["B on an A box"]) == (3, 2, 1, 1)
    assert ("m", "validation", "AAAAB", "TF one-shot") not in bs.swap_counts([short])
    near = row("counterfactual", "obj1: car, obj2: person, obj3: person, obj4: person, obj5: person",
               cf_mode="near", prefix_place="user")
    plain = row("counterfactual", "obj1: car, obj2: person, obj3: person, obj4: person, obj5: person")
    keys = set(bs.swap_counts([near, plain]))
    assert keys == {("m", "validation", "AAAAB", "CF near"), ("m", "validation", "AAAAB", "CF")}


def test_baaaa_uses_box_1():
    r = row("default", "obj1: person, obj2: person, obj3: person, obj4: person, obj5: handbag", order="BAAAA")
    c = bs.swap_counts([r])[("m", "validation", "BAAAA", "default")]
    assert (c["B=A"], c["B=A, B on an A box"]) == (1, 1)


def test_default_vs_single():
    labels_d = ["person", "handbag", "person", "person", "person"]
    d = row("default", "obj1: person, obj2: handbag, obj3: person, obj4: person, obj5: person", labels=labels_d)
    s = row("single", "handbag", labels=["person", "person", "person", "person", "handbag"])
    n, gain, gain2, up, sw, down = bs.default_vs_single([d, s])[("m", "validation", "AAAAB")]
    assert (n, up, sw, down) == (1, 1, 1, 0) and gain == 100.0 and gain2 == 0.0
    # a cut Default call is not A
    d["finish_reason"] = ["length"]
    assert bs.default_vs_single([d, s])[("m", "validation", "AAAAB")][1] == 0.0


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
