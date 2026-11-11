"""End-to-end CPU run with the fake model: write, resume skips done rows, torn line ignored."""
import json

import pytest

from rope_runner import run
from conftest import FIXTURE


def _run(out, *extra):
    run.main(["--model", "fake", "--probe", "default", "--split", "validation", "--subset", "AAAAB", "mixed",
              "--data-dir", FIXTURE, "--out", str(out), "--dry-run", "--greedy", *extra])


def rows(p):
    return [json.loads(l) for l in open(p) if l.strip().startswith("{") and l.strip().endswith("}")]


def test_resume(tmp_path):
    out = tmp_path / "r.jsonl"
    _run(out, "--limit", "2")
    assert len(rows(out)) == 4
    with pytest.raises(SystemExit):
        _run(out)  # refuses to overwrite without --resume
    with open(out, "a") as f:
        f.write('{"key": "torn')  # killed mid-write
    _run(out, "--resume")
    rs = rows(out)
    assert len(rs) == 6 and len({r["key"] for r in rs}) == 6
    _run(out, "--resume")
    assert len(rows(out)) == 6


def test_row_schema_and_scores(tmp_path):
    out = tmp_path / "r.jsonl"
    for probe, extra in [("default", []), ("single", []), ("teacher_forcing", ["--tf-mode", "incremental"]),
                         ("teacher_forcing", []), ("counterfactual", [])]:
        run.main(["--model", "fake", "--probe", probe, "--split", "validation", "--subset", "AAAAB",
                  "--data-dir", FIXTURE, "--out", str(out), "--dry-run", "--resume", *extra])
    rs = rows(out)
    need = ["image_id", "subset", "split", "probe", "prefix_used", "raw_output", "stripped_answer",
            "parsed_labels", "gold_labels", "correct_flags", "error_types", "trace_text", "thinking_tokens",
            "answer_tokens", "model", "sampling", "run_timestamp"]
    for r in rs:
        assert all(k in r for k in need)
        n = 1 if (r["probe"] == "counterfactual" or r["tf_mode"] == "oneshot") else 5
        assert len(r["parsed_labels"]) == n == len(r["gold_labels"]) == len(r["correct_flags"])
        if r["probe"] != "counterfactual":
            assert all(r["correct_flags"]), r  # fake model answers gold
        assert all(t > 0 for t in r["thinking_tokens"])
    assert len(rs) == 5 * 3
    from rope_runner.analyze import load, summarize
    s = summarize(load([str(out)]))
    assert len(s) == 5


def test_budget_dry_run(tmp_path):
    out = tmp_path / "b.jsonl"
    _run(out, "--limit", "1", "--budget", "5")
    for r in rows(out):
        assert r["forced_close"] == [True] and all(r["correct_flags"]) and r["budget"] == 5
