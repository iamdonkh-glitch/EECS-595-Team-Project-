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
