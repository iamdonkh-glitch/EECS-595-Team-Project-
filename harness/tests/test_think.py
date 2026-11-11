from rope_runner.budget import EARLY_STOP, run_calls
from rope_runner.models import FakeModel, strip_think


def test_strip_closed():
    assert strip_think("<think>\nreason\n</think>\n\nobj1: dog") == ("reason", "obj1: dog", True)


def test_strip_prefilled_qwen_thinking():
    # Qwen3-VL-Thinking: <think> is in the prompt, output only has </think>
    assert strip_think("reason </think>\n\ndog<|im_end|>", think_prefilled=True) == ("reason", "dog", True)


def test_strip_missing_close():
    assert strip_think("<think> still going") == ("still going", "", False)
    assert strip_think("still going", think_prefilled=True) == ("still going", "", False)


def test_strip_no_think():
    assert strip_think("  obj1: dog\n") == ("", "obj1: dog", None)
    assert strip_think("<think>\n\n</think>\n\ndog") == ("", "dog", True)  # MiMo /no_think


def test_strip_last_close_wins():
    assert strip_think("<think>a</think>b</think> dog")[1] == "dog"


def _fake(ans, think_tokens):
    m = FakeModel(think_tokens=think_tokens)
    p = m.render("q")
    m.answer_for[(p, None)] = ans
    return m, p


def test_no_budget_counts():
    m, p = _fake("obj1: dog", 10)
    r = run_calls(m, [p], [None], max_tokens=1000)[0]
    assert r["stripped_answer"] == "obj1: dog" and not r["forced_close"]
    assert r["answer_tokens"] == 2 and r["thinking_tokens"] == 12  # <think> + 10 + </think>


def test_budget_forces_close():
    m, p = _fake("obj1: dog", 50)
    r = run_calls(m, [p], [None], max_tokens=1000, budget=8)[0]
    assert r["forced_close"] and r["think_closed"]
    assert EARLY_STOP in r["raw_output"]
    assert r["stripped_answer"] == "obj1: dog"
    assert r["thinking_tokens"] == 8 and "Considering" not in r["trace_text"]


def test_budget_not_needed():
    m, p = _fake("dog", 3)
    r = run_calls(m, [p], [None], max_tokens=1000, budget=100)[0]
    assert not r["forced_close"] and r["stripped_answer"] == "dog"
