"""NEW options for the forcing probes: --n-given (dose-response) and --prefix-place assistant."""
import json

import pytest

from rope_runner import run
from rope_runner.budget import run_prefilled
from rope_runner.data import gold_labels
from rope_runner.models import FakeModel
from rope_runner.prompts import build_calls, multi_object_prompt
from rope_runner.scoring import tolerant_score
from conftest import FIXTURE


def test_n_given_prefixes(entries):
    e = entries["AAAAB"][0]
    g = gold_labels(e)
    full = build_calls("teacher_forcing", e, "validation", subset="AAAAB")[0][0]
    for m in range(5):
        c = build_calls("teacher_forcing", e, "validation", subset="AAAAB", n_given=m)[0][0]
        assert c["prefix"] == "".join(f" obj{k}: {g[k - 1]}," for k in range(1, m + 1)) + " obj5:"
        assert c["obj_index"] == 5
    assert build_calls("teacher_forcing", e, "validation", subset="AAAAB", n_given=4)[0][0]["text"] == full["text"]

    b = entries["BAAAA"][0]
    gb = gold_labels(b)
    c = build_calls("teacher_forcing", b, "validation", subset="BAAAA", n_given=2)[0][0]
    assert c["prefix"] == f" obj2: {gb[1]}, obj3: {gb[2]}, obj1:" and c["obj_index"] == 1

    calls, meta = build_calls("counterfactual", e, "validation", image_key="k", subset="AAAAB", n_given=2)
    cf = meta["counterfactual_class"]
    assert calls[0]["prefix"] == f" obj1: {cf}, obj2: {cf}, obj5:" and meta["n_given"] == 2


def test_options_rejected_outside_one_shot(entries):
    e = entries["AAAAB"][0]
    with pytest.raises(ValueError):
        build_calls("teacher_forcing", e, "validation", "incremental", n_given=2)
    with pytest.raises(ValueError):
        build_calls("default", e, "validation", place="assistant")
    with pytest.raises(ValueError):
        build_calls("counterfactual", e, "validation", n_given=5)


def test_assistant_place_moves_prefix_out_of_user_turn(entries):
    e = entries["AAAAB"][0]
    user = build_calls("teacher_forcing", e, "validation", subset="AAAAB")[0][0]
    asst = build_calls("teacher_forcing", e, "validation", subset="AAAAB", place="assistant")[0][0]
    assert asst["text"] == multi_object_prompt("validation", e["data_source"])
    assert asst["prefill"] == user["prefix"].lstrip() and asst["prefix"] == user["prefix"]
    nt = build_calls("counterfactual", e, "validation", subset="AAAAB", place="assistant", no_think=True)[0][0]
    assert nt["text"].endswith(" /no_think") and "obj5:" not in nt["text"][-20:]


def _prefilled_case(think_tokens=10, thinking=True, max_tokens=1000):
    m = FakeModel(think_tokens=think_tokens)
    m.thinking = thinking
    p = m.render("q")
    prefill = "obj1: door, obj2: door, obj3: door, obj4: door, obj5:"
    m.answer_for[(p, None)] = prefill + " drawer"
    return run_prefilled(m, [p], [None], [prefill], thinking, max_tokens)[0]


def test_run_prefilled_thinking():
    r = _prefilled_case()
    assert r["stripped_answer"] == "obj1: door, obj2: door, obj3: door, obj4: door, obj5: drawer"
    assert r["think_closed"] is True and r["thinking_tokens"] > 0 and r["answer_tokens"] == 1
    assert r["finish_reason"] == "stop" and "hmm" in r["trace_text"] and "</think>" not in r["trace_text"]
    gold = ["door"] * 4 + ["drawer"]
    assert tolerant_score("teacher_forcing", [r["stripped_answer"]], gold, gold)[1] == [True]


def test_run_prefilled_no_thinking():
    r = _prefilled_case(thinking=False)
    assert r["stripped_answer"].endswith("obj5: drawer") and r["think_closed"] is None
    assert r["thinking_tokens"] == 0


def test_run_prefilled_thinking_never_closed():
    r = _prefilled_case(think_tokens=50, max_tokens=8)
    assert r["stripped_answer"] == "" and r["think_closed"] is False and r["finish_reason"] == "length"


def _rows(p):
    return [json.loads(l) for l in open(p)]


def test_dry_run_options(tmp_path):
    out = tmp_path / "f.jsonl"
    base = ["--model", "fake", "--split", "validation", "--subset", "AAAAB", "BAAAA", "--limit", "2",
            "--data-dir", FIXTURE, "--out", str(out), "--dry-run", "--resume", "--greedy"]
    for probe, extra in [("teacher_forcing", []), ("teacher_forcing", ["--n-given", "2"]),
                         ("teacher_forcing", ["--prefix-place", "assistant"]),
                         ("counterfactual", ["--n-given", "0", "--prefix-place", "assistant"])]:
        run.main(base + ["--probe", probe] + extra)
    rs = _rows(out)
    assert len(rs) == 4 * 4 and len({r["key"] for r in rs}) == 16
    for r in rs:
        assert r["prefix_place"] in ("user", "assistant")
        if "given=2" in r["variant"]:
            assert r["n_given"] == 2 and r["prefix_used"][0].count("obj") == 3
        if r["prefix_place"] == "assistant":
            assert "place=assistant" in r["variant"]
            assert r["stripped_answer"][0].startswith(r["prefix_used"][0].lstrip())
        if r["probe"] == "teacher_forcing":
            assert r["tolerant_correct_flags"] == [True], r  # fake model answers gold


def test_cli_rejects_bad_combinations(tmp_path):
    base = ["--model", "fake", "--split", "validation", "--subset", "AAAAB", "--limit", "1",
            "--data-dir", FIXTURE, "--dry-run", "--greedy"]
    with pytest.raises(SystemExit):
        run.main(base + ["--probe", "teacher_forcing", "--tf-mode", "incremental", "--n-given", "1",
                         "--out", str(tmp_path / "a.jsonl")])
    with pytest.raises(SystemExit):
        run.main(base + ["--probe", "counterfactual", "--prefix-place", "assistant", "--budget", "64",
                         "--out", str(tmp_path / "b.jsonl")])
