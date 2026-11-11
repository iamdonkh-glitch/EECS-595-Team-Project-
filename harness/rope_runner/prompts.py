"""Prompt construction for the probes (default, single, teacher_forcing, counterfactual).

Prompt strings and the teacher-forcing cumulative logic are copied from sled-group/moh
@ 9483f2e4a69a90aee339b2305c1f5866daeba1a0, evaluation.py (no license upstream; attribution
only). Only the counterfactual prefix and the /no_think suffix are new.
"""
import hashlib
import random

from .data import candidates, get_class_list, gold_labels

# Official (moh prompt text unchanged): default, single, teacher_forcing (incremental = moh).
# New: one-shot teacher_forcing and counterfactual.
PROBES = ["default", "single", "teacher_forcing", "counterfactual"]
# Probes with one call per object, scored like moh's single-object probe.
SINGLE_PROBES = ("single",)
TF_MODES = ["incremental", "oneshot"]
NO_THINK_SUFFIX = " /no_think"  # MiMo-VL 2508 card: "/no_think" as the very last text of the user turn


def multi_object_prompt(data_type, dataset_name):
    # MOH: evaluation.py MultiObjectEvaluation._generate_prompt (verbatim string).
    prompt = "Given the classes: <50 classes>. There are five red bounding boxes in this image. For each object within the red bounding boxes, identify its class from the list. Provide the class names in the format: 'obj1: <class1>, obj2: <class2>, obj3: <class3>, obj4: <class4>, obj5: <class5>', with no additional words or punctuation. For example: obj1: class, obj2: class, obj3: class, obj4: class, obj5: class. Replace class with the actual names of the classes from your class list. Ensure that no placeholders or brackets are used around the class names and that no additional words or punctuation are added to the response."
    class_list = get_class_list(data_type, dataset_name)
    return prompt.replace("<50 classes>", class_list)


def single_object_prompt(obj_num, data_type, dataset_name):
    # MOH: evaluation.py SingleObjectEvaluation._generate_prompt (verbatim f-string).
    class_list = get_class_list(data_type, dataset_name)
    return f"User: Select the single, most appropriate class for Obj.{obj_num} located within the red bounding box from the following list: {class_list}. Your response should consist solely of the class name that Obj.{obj_num} belongs to, formatted as only the class name, without any extra characters or punctuation."


def b_index(subset):
    """1-based position of the odd object B: AAAAB -> 5, BAAAA -> 1. Other subsets have no B;
    the one-shot probes then ask object 5 (moh's index-5 call)."""
    return 1 if subset == "BAAAA" else 5


def given_prefix(ask, given):
    """NEW. One-shot prefix that gives the four other objects' labels and asks object `ask`.
    ask=5: identical to moh's cumulative index-5 prompt suffix ' obj1: c1, ..., obj4: c4, obj5:'.
    ask=1 (BAAAA variant): ' obj2: c2, obj3: c3, obj4: c4, obj5: c5, obj1:' (same user-turn
    placement; the asked object comes last so the model continues from it)."""
    others = [k for k in range(1, 6) if k != ask]
    return "".join(f" obj{k}: {c}," for k, c in zip(others, given)) + f" obj{ask}:"


def cumulative_prompts(prompt, given_classes):
    """MOH: evaluation.py TeacherForcingEvaluation.process_entry cumulative-prompt logic.
    Returns the prompt for every index 1..len(given_classes)+1. In moh, the class appended
    after the call for index k is entry["objects"][k-1]["name"].lower() (teacher forcing);
    here the caller passes those classes (gold for teacher forcing, C for counterfactual).
    Because the prefix does not depend on the model's output, all calls are independent."""
    out = []
    for index in range(1, len(given_classes) + 2):
        if index == 1:
            cumulative_prompt = prompt + f" obj{index}:"
        else:
            cumulative_prompt = cumulative_prompt + f", obj{index}:"
        out.append(cumulative_prompt)
        if index <= len(given_classes):
            cumulative_prompt += " " + given_classes[index - 1]
    return out


def counterfactual_class(entry, split, image_key, seed=0):
    """NEW. Draw the wrong class C with a fixed seed from the split's candidate list minus
    every class in the image's object_set. Seeded per image, so the draw is order-independent."""
    present = {c.lower() for c in entry["object_set"]} | set(gold_labels(entry))
    pool = [c for c in candidates(split, entry["data_source"]) if c.lower() not in present]
    h = int(hashlib.sha256(f"{seed}|{split}|{image_key}".encode()).hexdigest(), 16)
    return random.Random(h).choice(pool).lower()


PLACES = ["user", "assistant"]


def build_calls(probe, entry, split, tf_mode="oneshot", no_think=False, image_key="", seed=0,
                subset=None, n_given=None, place="user"):
    """Return (calls, meta). calls = list of dicts {text, prefix, obj_index, prefill}; obj_index
    is the 1-based object each call asks about (None = all five). For one-shot teacher_forcing
    and counterfactual the asked object is B: object 5 on AAAAB (and non-adversarial subsets),
    object 1 on BAAAA (the other four given).

    NEW (one-shot teacher_forcing and counterfactual only):
      n_given  0-4: give only the first n_given of the four other objects (box order), then ask B.
               None = all four (the default one-shot prompt).
      place    "user" = prefix appended to the user turn (moh placement, default);
               "assistant" = the user turn is the plain multi-object prompt and the prefix
               (without its leading space) is the start of the model's own answer (`prefill`)."""
    src = entry["data_source"]
    gold = gold_labels(entry)
    meta = {}
    one_shot = probe == "counterfactual" or (probe == "teacher_forcing" and tf_mode == "oneshot")
    if (n_given is not None or place != "user") and not one_shot:
        raise ValueError("n_given and place apply to one-shot teacher_forcing and counterfactual only")
    if n_given is not None and not 0 <= n_given <= 4:
        raise ValueError(f"n_given must be 0-4, got {n_given}")
    if place not in PLACES:
        raise ValueError(place)
    if probe == "default":
        calls = [{"text": multi_object_prompt(split, src), "prefix": "", "obj_index": None}]
    elif probe in SINGLE_PROBES:
        calls = [{"text": single_object_prompt(k, split, src), "prefix": "", "obj_index": k}
                 for k in range(1, 6)]
    elif probe in ("teacher_forcing", "counterfactual"):
        base = multi_object_prompt(split, src)
        if probe == "teacher_forcing":
            given = gold[:4]
        else:
            c = counterfactual_class(entry, split, image_key, seed)
            meta["counterfactual_class"] = c
            given = [c] * 4
        if probe == "teacher_forcing" and tf_mode not in TF_MODES:
            raise ValueError(tf_mode)
        if probe == "teacher_forcing" and tf_mode == "incremental":
            cps = cumulative_prompts(base, given)  # moh's 5 calls, unchanged
            calls = [{"text": cps[k - 1], "prefix": cps[k - 1][len(base):], "obj_index": k}
                     for k in range(1, 6)]
        else:
            ask = b_index(subset)
            if probe == "teacher_forcing":
                given = [g for k, g in enumerate(gold, 1) if k != ask]
            m = 4 if n_given is None else n_given
            pre = given_prefix(ask, given[:m])  # ask=5, m=4: == moh's cumulative index-5 prompt
            if n_given is not None:
                meta["n_given"] = n_given
            if place == "assistant":
                calls = [{"text": base, "prefix": pre, "obj_index": ask, "prefill": pre.lstrip()}]
            else:
                calls = [{"text": base + pre, "prefix": pre, "obj_index": ask}]
    else:
        raise ValueError(f"unknown probe {probe}")
    if no_think:
        for c in calls:
            c["text"] += NO_THINK_SUFFIX
    return calls, meta


def chat_messages(text, family):
    """NEW. One user turn, image first then text (MiMo card: image before text; Qwen3-VL
    examples use the same order). No system message: MiMo's template then injects its default
    system prompt, Qwen3-VL's injects none. `family` is kept for future per-family changes."""
    if family not in ("qwen3vl", "mimo"):
        raise ValueError(family)
    return [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": text}]}]
