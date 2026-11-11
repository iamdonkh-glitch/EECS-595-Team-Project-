"""Scoring.

STRICT = sled-group/moh @ 9483f2e4a69a90aee339b2305c1f5866daeba1a0 evaluation.py, copied
(segment_classes verbatim; the per-entry accounting of MultiObjectEvaluation,
SingleObjectEvaluation and TeacherForcingEvaluation re-expressed per row so that summing
rows reproduces moh's correct_predictions / total_predictions / acc_list exactly; see
tests/test_scoring.py, which runs moh's own classes on the same responses).
moh has no license file: attribution only.

TOLERANT = new, reported separately, never replaces the strict number.
Error typing = new.
"""
import re


# ---------------------------------------------------------------- strict (moh)
def segment_classes(response):
    # MOH: evaluation.py MultiObjectEvaluation.segment_classes (verbatim body).
    segments = response.split(", ")
    classes = [segment.split(": ")[1] for segment in segments]
    return classes


def strict_score(probe, answers, gold, tf_mode="oneshot", ask_index=5):
    """answers: list of stripped answers, one per call. gold: 5 lowercase gold names.
    Returns parsed (list), correct (list of bool), moh_total (moh's denominator contribution).

    moh quirks kept on purpose:
      * default: a parse failure adds 5 to total_predictions twice (moh_total=10), and every
        object counts wrong;
      * single: raw `response.lower() == true_class` (no strip, no parsing);
      * teacher forcing (incremental): the k-th call is parsed with segment_classes and its
        k-th segment is taken; at the first failure moh breaks, so objects k..5 count wrong
        and 5-k+1 extra is added to total_predictions.
    One-shot teacher forcing and counterfactual have no moh counterpart: we split with moh's
    segment_classes (any segment without ": " fails the parse) and take the segment whose key
    is obj{k}, k = the asked object (5, or 1 on BAAAA); moh_total = 1. Taking the segment by
    its key rather than its position matters when the answer follows the prefix's order
    (BAAAA lists obj2..obj5 before obj1; an assistant-turn prefill always does)."""
    if probe == "default":
        try:
            seg = segment_classes(answers[0])
        except Exception:
            return [None] * 5, [False] * 5, 10
        parsed = [seg[i].lower() if len(seg) >= i + 1 else None for i in range(5)]
        return parsed, [p == g for p, g in zip(parsed, gold)], 5
    if probe == "single":
        parsed = [a.lower() for a in answers]
        return parsed, [p == g for p, g in zip(parsed, gold)], 5
    if probe == "teacher_forcing" and tf_mode == "incremental":
        parsed, total = [None] * 5, 5
        for index in range(1, 6):
            try:
                seg = segment_classes(answers[index - 1])
            except Exception:
                total += 5 - index + 1
                break
            if len(seg) >= index:
                parsed[index - 1] = seg[index - 1].lower()
            else:
                total += 5 - index + 1
                break
        return parsed, [p == g for p, g in zip(parsed, gold)], total
    # one-shot teacher forcing / counterfactual: the asked object only, found by its key
    k = ask_index
    p = keyed_segment(answers[0], k)
    return [p], [p == gold[k - 1]], 1


def keyed_segment(response, k):
    """NEW. moh's split (segments on ", ", key and class on ": "; a segment without ": " fails
    the whole parse, as in segment_classes), then the class of the first segment keyed obj{k}.
    None when the parse fails or no segment is keyed obj{k}."""
    try:
        segment_classes(response)  # same failure condition as moh
    except Exception:
        return None
    for segment in response.split(", "):
        key, cls = segment.split(": ")[0], segment.split(": ")[1]
        if key.strip().lower() == f"obj{k}":
            return cls.lower()
    return None


# ---------------------------------------------------------------- tolerant (new)
_OBJ = re.compile(r"obj\s*\.?\s*([1-5])\s*[:：]", re.IGNORECASE)


def normalize(s):
    s = s.lower().replace("*", "").replace("`", "").replace("_", " ")
    s = s.strip().strip("'\"<>[](){}").strip()
    s = re.sub(r"[\s]+", " ", s)
    return s.strip(" .,;:!'\"")


def to_candidate(s, cands):
    """Exact candidate after normalization; else the longest candidate that occurs as a whole
    phrase in s; else the normalized string itself (scored wrong, typed off_list)."""
    s = normalize(s)
    low = [c.lower() for c in cands]
    if s in low:
        return s
    hits = [c for c in low if re.search(r"(?<![a-z])" + re.escape(c) + r"(?![a-z])", s)]
    return max(hits, key=len) if hits else (s or None)


def tolerant_multi(text, cands):
    """objK: <label> anywhere in the text (markdown, newlines, extra words ok). Last mention of
    each index wins (models sometimes restate). Returns {index: label}."""
    found = {}
    ms = list(_OBJ.finditer(text))
    for m, nxt in zip(ms, ms[1:] + [None]):
        chunk = text[m.end(): nxt.start() if nxt else len(text)]
        chunk = re.split(r"[\n,;]", chunk.strip(), maxsplit=1)[0]
        found[int(m.group(1))] = to_candidate(chunk, cands)
    return found


def tolerant_one(text, k, cands):
    """Label for object k: an explicit objK: if present, else the whole answer."""
    found = tolerant_multi(text, cands)
    if k in found:
        return found[k]
    if found:  # other objects named but not k
        return None
    return to_candidate(text, cands) if text.strip() else None


def prefill_labels(answer, prefill, k, cands, finish):
    """NEW. Object k after an assistant-turn prefill that ends in "obj{k}:" (the asked object).
    answer = the row's stripped answer (prefill + the model's continuation); finish = the answer
    stage's finish_reason. Returns None when the answer does not start with the prefill (thinking
    never closed, so there was no answer stage), else a dict:
      first_s  the first segment of the continuation (up to the first ",", ";" or line break),
               lowercased and trimmed: the strict reading (any extra text makes it off-list)
      first_t  to_candidate(first segment): the tolerant reading
      more     the model kept writing after that label (e.g. "Wait, no, that's wrong. ...")
      final_t  obj{k}'s label at the end of the answer: first_t when more is False; else the last
               "obj{k}: <class>" in the later text whose label is exactly a candidate after
               normalize() (descriptions such as "obj5: the box on the right is a drawer" are
               skipped); None when there is no such mention or the answer hit the token limit."""
    p = prefill.strip()
    if not answer.startswith(p):
        return None
    head = answer[len(p):].lstrip(" ")
    seg = re.split(r"[,;\n]", head, maxsplit=1)[0]
    later = head[len(seg):]
    more = bool(later.strip(" .,;\n"))
    first_s = seg.strip().lower() or None
    first_t = to_candidate(seg, cands) if seg.strip() else None
    if not more:
        return dict(first_s=first_s, first_t=first_t, more=False, final_t=first_t)
    low = {c.lower() for c in cands}
    final = None
    ms = list(_OBJ.finditer(later))
    for m, nxt in zip(ms, ms[1:] + [None]):
        if int(m.group(1)) != k:
            continue
        chunk = re.split(r"[\n,;]", later[m.end(): nxt.start() if nxt else len(later)].strip(), maxsplit=1)[0]
        if normalize(chunk) in low:
            final = normalize(chunk)
    return dict(first_s=first_s, first_t=first_t, more=True, final_t=None if finish == "length" else final)


def tolerant_score(probe, answers, gold, cands, tf_mode="oneshot", ask_index=5):
    if probe == "default":
        found = tolerant_multi(answers[0], cands)
        parsed = [found.get(i) for i in range(1, 6)]
    elif probe == "single" or (probe == "teacher_forcing" and tf_mode == "incremental"):
        parsed = [tolerant_one(a, k, cands) for k, a in zip(range(1, 6), answers)]
    else:
        parsed = [tolerant_one(answers[0], ask_index, cands)]
        return parsed, [parsed[0] == gold[ask_index - 1]]
    return parsed, [p == g for p, g in zip(parsed, gold)]


# ---------------------------------------------------------------- error typing (new)
def error_type(pred, obj_index, gold, subset, cands, counterfactual_class=None):
    """Error type of one prediction. obj_index is 1-based. Returns None when correct.
    unparsed      no label recovered
    copied_prefix counterfactual probe: predicted the injected wrong class C
    inertia       AAAAB, object 5 (the odd one, B) labelled A
    borrowed      equals another target object's class in this image
    off_list      not in the 50-class candidate list (formatting, not a hallucination claim)
    invented      in the candidate list but not among the 5 target classes"""
    g = gold[obj_index - 1]
    if pred is None:
        return "unparsed"
    if pred == g:
        return None
    if counterfactual_class is not None and pred == counterfactual_class:
        return "copied_prefix"
    if subset == "AAAAB" and obj_index == 5 and pred == gold[0]:
        return "inertia"
    if pred in [x for j, x in enumerate(gold) if j != obj_index - 1]:
        return "borrowed"
    if pred not in [c.lower() for c in cands]:
        return "off_list"
    return "invented"


def error_types(parsed, obj_indices, gold, subset, cands, counterfactual_class=None):
    return [error_type(p, k, gold, subset, cands, counterfactual_class) for p, k in zip(parsed, obj_indices)]
