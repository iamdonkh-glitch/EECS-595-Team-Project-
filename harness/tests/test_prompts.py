"""Our prompts must equal the strings moh actually sends to the model."""
import copy

from rope_runner.data import load_subset
from rope_runner.prompts import build_calls, counterfactual_class
from conftest import FIXTURE


class Recorder:
    def __init__(self, reply=lambda p: "obj1: a, obj2: b, obj3: c, obj4: d, obj5: e"):
        self.prompts, self.reply = [], reply

    def generate_response(self, prompt, image):
        self.prompts.append(prompt)
        return self.reply(prompt)


def moh_prompts(moh, cls, entry, split, root):
    rec = Recorder()
    ev = cls(rec, moh_image_processor(), root, split)
    ev.process_entry(copy.deepcopy(entry), [0] * 5, {})
    return rec.prompts


def moh_image_processor():
    import image_processor
    return image_processor.ImageProcessor()


def test_default_single_tf_match_moh(moh, png_root):
    for split in ["train", "validation"]:
        for subset in ["AAAAB", "BAAAA", "heterogenous", "homogenous", "mixed"]:
            for entry in load_subset(FIXTURE, split, subset):
                for probe, cls, mode in [("default", moh.MultiObjectEvaluation, None),
                                         ("single", moh.SingleObjectEvaluation, None),
                                         ("teacher_forcing", moh.TeacherForcingEvaluation, "incremental")]:
                    ours = [c["text"] for c in build_calls(probe, entry, split, mode or "oneshot")[0]]
                    assert ours == moh_prompts(moh, cls, entry, split, png_root), (split, subset, probe)


def test_train_split_uses_train_classes(moh, tmp_path):
    from rope_runner.constant import TRAIN_CLASSES
    e = load_subset(FIXTURE, "train", "mixed")[0]
    text = build_calls("default", e, "train")[0][0]["text"]
    assert ", ".join(TRAIN_CLASSES[e["data_source"]]) in text
    ev = moh.MultiObjectEvaluation(None, None, "", "train")
    assert text == ev._generate_prompt(e["data_source"])


def test_oneshot_is_moh_index5_prompt(moh, png_root, entries):
    e = entries["AAAAB"][0]
    tf_all = moh_prompts(moh, moh.TeacherForcingEvaluation, e, "validation", png_root)
    calls, _ = build_calls("teacher_forcing", e, "validation", "oneshot")
    assert len(calls) == 1 and calls[0]["text"] == tf_all[4] and calls[0]["obj_index"] == 5
    g = [o["name"].lower() for o in e["objects"]]
    assert calls[0]["prefix"] == f" obj1: {g[0]}, obj2: {g[1]}, obj3: {g[2]}, obj4: {g[3]}, obj5:"


def test_counterfactual(entries):
    from rope_runner.data import candidates
    for e in entries["AAAAB"] + entries["BAAAA"]:
        c1 = counterfactual_class(e, "validation", "k", seed=0)
        assert c1 == counterfactual_class(e, "validation", "k", seed=0)  # deterministic
        assert c1 not in {x.lower() for x in e["object_set"]}
        assert c1 in candidates("validation", e["data_source"])
        calls, meta = build_calls("counterfactual", e, "validation", image_key="k")
        assert meta["counterfactual_class"] == c1
        assert calls[0]["prefix"] == f" obj1: {c1}, obj2: {c1}, obj3: {c1}, obj4: {c1}, obj5:"


def test_no_think_suffix(entries):
    e = entries["mixed"][0]
    for probe in ["default", "single", "teacher_forcing", "counterfactual"]:
        for c in build_calls(probe, e, "validation", no_think=True)[0]:
            assert c["text"].endswith(" /no_think")
