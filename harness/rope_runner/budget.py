"""NEW. Generation with optional truncate-and-close thinking budget.

Budget N:
  1. generate with max_tokens = N;
  2. if thinking is open (a <think> was emitted or prefilled by the template) and no </think>
     came, append Qwen3's official early-stop phrase + "</think>\\n\\n" and continue for
     `answer_max_tokens`;
  3. if </think> came but the answer was cut by the cap, continue plainly for
     `answer_max_tokens` (no phrase).
Without a budget this is a single generate call with the model's max_tokens.
Works for any model that emits <think> (MiMo-VL) or has it prefilled (Qwen3-VL-Thinking).
The forced close is a distribution shift; rows carry forced_close=True so it can be reported.
"""
from .models import THINK_CLOSE, THINK_OPEN, strip_think

EARLY_STOP = ("\n\nConsidering the limited time by the user, I have to give the solution "
              "based on the thinking directly now.\n" + THINK_CLOSE + "\n\n")


def run_calls(model, prompts, images, max_tokens, budget=None, answer_max_tokens=128):
    """prompts: rendered chat strings. Returns one dict per prompt with raw_output, trace_text,
    stripped_answer, think_closed, forced_close, thinking_tokens, answer_tokens, finish_reason,
    prompt_tokens, cached_tokens (summed over the call and its continuation, if any)."""
    first = model.generate(prompts, images, budget if budget else max_tokens)
    prefilled = [p.rstrip().endswith(THINK_OPEN) for p in prompts]
    cont_idx, cont_prompts, cont_images, forced = [], [], [], {}
    if budget:
        for i, (text, _, fin, *_rest) in enumerate(first):
            if fin != "length":
                continue
            opened = prefilled[i] or THINK_OPEN in text
            if opened and THINK_CLOSE not in text:
                forced[i] = True
                cont_prompts.append(prompts[i] + text + EARLY_STOP)
            else:
                cont_prompts.append(prompts[i] + text)
            cont_idx.append(i)
            cont_images.append(images[i])
    second = dict(zip(cont_idx, model.generate(cont_prompts, cont_images, answer_max_tokens))) if cont_idx else {}

    rows = []
    for i, g1 in enumerate(first):
        t1, n1, f1 = g1[:3]
        g2 = second.get(i, ("", 0, None))
        t2, n2, f2 = g2[:3]
        pt = [x[3] for x in (g1, g2) if len(x) > 3 and x[3] is not None]
        ct = [x[4] for x in (g1, g2) if len(x) > 4 and x[4] is not None]
        if forced.get(i):
            raw = t1 + EARLY_STOP + t2
            trace = t1.split(THINK_OPEN, 1)[-1].strip()
            answer = strip_think(t2)[1]
            closed, think_n, ans_n = True, n1, n2
        else:
            raw = t1 + t2
            trace, answer, closed = strip_think(raw, prefilled[i])
            tail = raw.rsplit(THINK_CLOSE, 1)[1] if closed else ("" if closed is False else raw)
            ans_n = model.count_tokens(tail.strip())
            think_n = max(n1 + n2 - ans_n, 0) if closed is not None else 0
            if closed is None:
                ans_n = n1 + n2
        rows.append({
            "raw_output": raw, "trace_text": trace, "stripped_answer": answer,
            "think_closed": closed, "forced_close": bool(forced.get(i)),
            "thinking_tokens": think_n, "answer_tokens": ans_n,
            "finish_reason": f2 or f1,
            "prompt_tokens": sum(pt) if pt else None,
            "cached_tokens": sum(ct) if ct else None,
        })
    return rows


def _drop_specials(text):
    for s in ("<|im_end|>", "<|endoftext|>"):
        text = text.replace(s, "")
    return text


def run_prefilled(model, prompts, images, prefills, thinking, max_tokens, answer_max_tokens=128):
    """NEW. Assistant-turn prefill: the given labels are the start of the model's own answer.

    Non-thinking model: one call on prompt + prefill.
    Thinking model: (1) generate on the plain prompt, stopping at </think> (the same thinking as
    the default probe); (2) if thinking closed, continue on prompt + thinking + "\\n\\n" + prefill
    for `answer_max_tokens`. If thinking never closed within max_tokens there is no step 2: the
    answer is "" and finish_reason is "length" (wrong under the token-limit rule).

    stripped_answer = prefill + the generated continuation, so the answer is scored in the same
    `obj1: c1, ...` format as the user-turn probes; raw_output holds only generated text."""
    if not thinking:
        rows = []
        gens = model.generate([p + f for p, f in zip(prompts, prefills)], images, max_tokens)
        for f, g in zip(prefills, gens):
            t, n, fin = g[:3]
            rows.append({
                "raw_output": t, "trace_text": "", "stripped_answer": (f + _drop_specials(t)).strip(),
                "think_closed": None, "forced_close": False, "thinking_tokens": 0, "answer_tokens": n,
                "finish_reason": fin,
                "prompt_tokens": g[3] if len(g) > 3 else None, "cached_tokens": g[4] if len(g) > 4 else None,
            })
        return rows

    first = model.generate(prompts, images, max_tokens, stop=[THINK_CLOSE])
    idx = [i for i, g in enumerate(first) if THINK_CLOSE in g[0]]
    cont = [prompts[i] + first[i][0] + "\n\n" + prefills[i] for i in idx]
    second = dict(zip(idx, model.generate(cont, [images[i] for i in idx], answer_max_tokens))) if idx else {}
    rows = []
    for i, g1 in enumerate(first):
        t1, n1, f1 = g1[:3]
        g2 = second.get(i)
        pt = [x[3] for x in (g1, g2) if x and len(x) > 3 and x[3] is not None]
        ct = [x[4] for x in (g1, g2) if x and len(x) > 4 and x[4] is not None]
        if g2 is None:  # thinking never closed
            trace = t1.split(THINK_OPEN, 1)[-1].replace(THINK_CLOSE, "").strip()
            rows.append({"raw_output": t1, "trace_text": trace, "stripped_answer": "",
                         "think_closed": False, "forced_close": False, "thinking_tokens": n1,
                         "answer_tokens": 0, "finish_reason": f1,
                         "prompt_tokens": sum(pt) if pt else None, "cached_tokens": sum(ct) if ct else None})
            continue
        t2, n2, f2 = g2[:3]
        trace = t1.rsplit(THINK_CLOSE, 1)[0].split(THINK_OPEN, 1)[-1].strip()
        # keep the continuation's leading space: "obj5:" + " dog" must stay "obj5: dog"
        cont_text = _drop_specials(t2.rsplit(THINK_CLOSE, 1)[-1] if THINK_CLOSE in t2 else t2)
        rows.append({
            "raw_output": t1 + "\n\n" + prefills[i] + t2, "trace_text": trace,
            "stripped_answer": (prefills[i] + cont_text).strip(),
            "think_closed": True, "forced_close": False, "thinking_tokens": n1, "answer_tokens": n2,
            "finish_reason": f2,
            "prompt_tokens": sum(pt) if pt else None, "cached_tokens": sum(ct) if ct else None,
        })
    return rows
