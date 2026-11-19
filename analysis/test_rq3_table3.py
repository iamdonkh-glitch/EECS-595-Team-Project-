"""CPU test for analysis/rq3_table3.py: every category of the error taxonomy on hand-made labels, the
mapping back to the harness's stored error types, and the build() checks on a tiny fixture."""
import importlib.util
import json
import os

spec = importlib.util.spec_from_file_location(
    "rq3_table3", os.path.join(os.path.dirname(os.path.abspath(__file__)), "rq3_table3.py"))
rq3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rq3)

from rope_runner.constant import VALIDATION_CLASSES  # noqa: E402  (rq3_table3 put harness/ on sys.path)
from rope_runner.scoring import error_type  # noqa: E402

CANDS = {c.lower() for c in VALIDATION_CLASSES["ADE"]}
GOLD = ["chair", "table", "vase", "door", "window"]  # all in the ADE validation list
OSET = {"chair", "table", "vase", "door", "window", "plant", "wall"}  # plant: annotated, not a target
AAAAB = ["chair", "chair", "chair", "chair", "door"]
BAAAA = ["door", "chair", "chair", "chair", "chair"]


def cat(label, obj, gold=GOLD, subset="mixed", cut=False):
    return rq3.categorize(label, obj, gold, subset, CANDS, OSET, cut)


def test_categories():
    assert cat("chair", 1) == "correct"
    assert cat("chair", 1, cut=True) == "truncated"  # cut call: wrong even when the label matches
    assert cat(None, 1) == "unparsed"
    assert cat(None, 1, cut=True) == "truncated"
    assert cat("table", 1) == "borrowed"
    assert cat("dog", 1) == "off_list"  # not an ADE validation class
    assert cat("plant", 1) == "in_image"
    assert cat("tree", 1) == "invented"  # a candidate, not in OSET
    # Adversarial: B labelled A in both orders; an A box labelled B is borrowed
    assert cat("chair", 5, AAAAB, "AAAAB") == "b_eq_a"
    assert cat("chair", 1, BAAAA, "BAAAA") == "b_eq_a"
    assert cat("door", 2, BAAAA, "BAAAA") == "borrowed"
    # B=A only exists for the B box
    assert cat("chair", 5, AAAAB, "BAAAA") == "borrowed"


def test_mapping_to_harness_types():
    cases = [("chair", 1, GOLD, "mixed"), (None, 1, GOLD, "mixed"), ("table", 1, GOLD, "mixed"),
             ("dog", 1, GOLD, "mixed"), ("plant", 1, GOLD, "mixed"), ("tree", 1, GOLD, "mixed"),
             ("chair", 5, AAAAB, "AAAAB"), ("chair", 1, BAAAA, "BAAAA"), ("door", 2, BAAAA, "BAAAA")]
    for label, obj, gold, subset in cases:
        c = rq3.categorize(label, obj, gold, subset, CANDS, OSET, False)
        assert rq3.harness_type(c, subset) == error_type(label, obj, gold, subset, VALIDATION_CLASSES["ADE"])


def test_build_checks():
    labels = ["chair", "plant", "tree", None, "window"]
    stored = [error_type(x, k, GOLD, "mixed", VALIDATION_CLASSES["ADE"]) for k, x in enumerate(labels, 1)]
    row = {"key": "m|default|g|validation|mixed|0|img0", "model": "m", "probe": "default", "split": "validation",
           "subset": "mixed", "entry_idx": 0, "image_id": "img0", "data_source": "ADE",
           "obj_indices": [1, 2, 3, 4, 5], "asked_objects": [None], "finish_reason": ["stop"],
           "all_gold_labels": GOLD, "tolerant_labels": labels, "tolerant_error_types": stored,
           "parsed_labels": labels, "error_types": stored}
    cut_row = dict(row, key="m|single|g|validation|mixed|0|img0", probe="single", asked_objects=[1, 2, 3, 4, 5],
                   finish_reason=["length", "stop", "stop", "stop", "stop"])
    rope = {("validation", "mixed", 0): ("img0", OSET)}
    cells, chk = rq3.build([row, cut_row], rope)
    assert cells[("m", "default", "validation", "mixed", "tolerant")][(0, "img0")] == \
        ["correct", "in_image", "invented", "unparsed", "correct"]
    assert cells[("m", "single", "validation", "mixed", "tolerant")][(0, "img0")][0] == "truncated"
    assert chk["tolerant_harness_recomputed_mismatch"] == 0 and chk["tolerant_mapping_mismatch"] == 0
    assert chk["tolerant_mapping_checked"] == 9  # 5 + 4 objects outside the cut call
    assert chk["image_id_mismatch"] == 0
    json.dumps(rq3.counts(cells[("m", "default", "validation", "mixed", "tolerant")])[0])
