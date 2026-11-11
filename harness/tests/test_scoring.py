"""Strict scorer must reproduce moh's own counters on the same responses."""
import copy

from rope_runner.data import candidates, gold_labels
from rope_runner.scoring import error_type, strict_score, tolerant_score


class Canned:
    def __init__(self, fn):
        self.fn = fn

    def generate_response(self, prompt, image):
        return self.fn(prompt)


def run_moh(moh, cls, entries, reply, root):
    import image_processor
    ev = cls(Canned(reply), image_processor.ImageProcessor(), root, "validation")
    acc = [0] * 5
    for e in entries:
        ev.process_entry(copy.deepcopy(e), acc, {})
    return ev.correct_predictions, ev.total_predictions, acc


def run_ours(probe, entries, replies_per_entry, tf_mode="oneshot"):
    c = t = 0
    acc = [0] * 5
    for e, answers in zip(entries, replies_per_entry):
        parsed, correct, tot = strict_score(probe, answers, gold_labels(e), tf_mode)
        c += sum(correct)
        t += tot
        for i, ok in enumerate(correct):
            acc[i] += ok
    return c, t, acc


def fmt(labels):
    return ", ".join(f"obj{i}: {c}" for i, c in enumerate(labels, 1))


DEFAULT_VARIANTS = [
    lambda g: fmt(g),                                  # perfect
    lambda g: fmt(g[:4] + ["zebra"]),                  # one wrong
    lambda g: fmt(g[:3]),                              # only three objects
    lambda g: "The objects are " + " and ".join(g),    # parse failure -> all wrong, total += 10
    lambda g: fmt([x.upper() for x in g]),             # case-insensitive in moh
    lambda g: fmt(g) + ".",                            # trailing period breaks obj5 (strict)
    lambda g: "\n".join(f"obj{i}: {c}" for i, c in enumerate(g, 1)),  # newlines: parse failure
]


def test_default_matches_moh(moh, entries, png_root):
    es = [e for v in entries.values() for e in v]
    for variant in DEFAULT_VARIANTS:
        replies = [[variant(gold_labels(e))] for e in es]
        it = iter(replies)
        theirs = run_moh(moh, moh.MultiObjectEvaluation, es, lambda p: next(it)[0], png_root)
        assert run_ours("default", es, replies) == theirs


def test_parse_failure_is_all_wrong(entries):
    e = entries["mixed"][0]
    parsed, correct, tot = strict_score("default", ["I think obj1 is a dog"], gold_labels(e))
    assert parsed == [None] * 5 and correct == [False] * 5 and tot == 10


def test_single_matches_moh(moh, entries, png_root):
    es = [e for v in entries.values() for e in v]
    for variant in [lambda g: g, lambda g: g.upper(), lambda g: g + ".", lambda g: "obj: " + g]:
        replies = [[variant(x) for x in gold_labels(e)] for e in es]
        flat = iter([r for rs in replies for r in rs])
        theirs = run_moh(moh, moh.SingleObjectEvaluation, es, lambda p: next(flat), png_root)
        assert run_ours("single", es, replies) == theirs


def test_teacher_forcing_incremental_matches_moh(moh, entries, png_root):
    es = [e for v in entries.values() for e in v]
    variants = [
        lambda g, k: fmt(g),                       # model restates all five: k-th taken
        lambda g, k: g[k - 1],                     # bare class: moh parse failure at k=1, break
        lambda g, k: fmt(g[:k]) if k < 4 else fmt(g[:2]),  # too few segments at k=4 -> break
        lambda g, k: fmt(g[:k - 1] + ["zebra"] + g[k:]),   # always wrong at k
    ]
    for variant in variants:
        replies = [[variant(gold_labels(e), k) for k in range(1, 6)] for e in es]
        # moh calls entry by entry, k = 1.. until a break; a call for obj1 starts a new entry
        state = {"i": -1}

        def reply(prompt):
            k = prompt.rsplit("response.", 1)[1].count("obj")
            if k == 1:
                state["i"] += 1
            return replies[state["i"]][k - 1]
        theirs = run_moh(moh, moh.TeacherForcingEvaluation, es, reply, png_root)
        assert run_ours("teacher_forcing", es, replies, "incremental") == theirs, variant


def test_oneshot_and_counterfactual_strict(entries):
    e = entries["AAAAB"][0]
    g = gold_labels(e)
    assert strict_score("teacher_forcing", [fmt(g)], g) == ([g[4]], [True], 1)
    assert strict_score("counterfactual", [g[4]], g) == ([None], [False], 1)  # bare answer fails strict


def test_oneshot_strict_takes_asked_key_not_position():
    gold = ["drawer", "door", "door", "door", "door"]  # BAAAA: B = obj1
    prefix_order = "obj2: door, obj3: door, obj4: door, obj5: door, obj1: drawer"
    assert strict_score("teacher_forcing", [prefix_order], gold, ask_index=1) == (["drawer"], [True], 1)
    canonical = "obj1: drawer, obj2: door, obj3: door, obj4: door, obj5: door"
    assert strict_score("counterfactual", [canonical], gold, ask_index=1) == (["drawer"], [True], 1)
    assert strict_score("teacher_forcing", ["obj1: drawer"], gold, ask_index=1)[0] == ["drawer"]
    assert strict_score("teacher_forcing", ["obj2: door, obj3: door"], gold, ask_index=1)[0] == [None]
    assert strict_score("teacher_forcing", ["obj1: drawer, door"], gold, ask_index=1)[0] == [None]  # moh parse fails


def test_tolerant_is_separate_and_lenient(entries):
    e = entries["mixed"][0]
    g, cands = gold_labels(e), candidates("validation", e["data_source"])
    md = "\n".join(f"**obj{i}:** {c.title()}." for i, c in enumerate(g, 1))
    assert strict_score("default", [md], g)[1] == [False] * 5
    tp, tc = tolerant_score("default", [md], g, cands)
    assert tp == g and all(tc)
    tp, tc = tolerant_score("counterfactual", [f"The answer is {g[4]}."], g, cands)
    assert tp == [g[4]] and tc == [True]
    tp, _ = tolerant_score("single", [f"Obj.{k}: {x}" for k, x in enumerate(g, 1)], g, cands)
    assert tp == g


def test_error_types():
    cands = ["door", "drawer", "zebra", "cup"]
    gold = ["door", "door", "door", "door", "drawer"]
    assert error_type("drawer", 5, gold, "AAAAB", cands) is None
    assert error_type("door", 5, gold, "AAAAB", cands) == "inertia"
    assert error_type("door", 5, gold, "mixed", cands) == "borrowed"
    assert error_type("drawer", 1, gold, "AAAAB", cands) == "borrowed"
    assert error_type("zebra", 2, gold, "AAAAB", cands) == "invented"
    assert error_type("zebra", 5, gold, "AAAAB", cands, counterfactual_class="zebra") == "copied_prefix"
    assert error_type("dining table.", 3, gold, "AAAAB", cands) == "off_list"
    assert error_type(None, 3, gold, "AAAAB", cands) == "unparsed"
