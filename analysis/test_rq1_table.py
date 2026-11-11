"""CPU test for analysis/rq1_table.py on a tiny hand-made fixture: Table 1 accuracy, truncation and
parse-failure counts, box-level paired McNemar counts, positions, and the note for a missing pair."""
import importlib.util
import json
import os

spec = importlib.util.spec_from_file_location("rq1_table", os.path.join(os.path.dirname(os.path.abspath(__file__)), "rq1_table.py"))
rq1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rq1)

GOLD = ["chair", "chair", "table", "vase", "door"]  # all in the ADE validation list


def row(model, probe, idx, correct, trunc=False, unparsed=()):
    labels = [g if c else "dog" for g, c in zip(GOLD, correct)]  # "dog" is not an ADE validation class
    labels = [None if i in unparsed else x for i, x in enumerate(labels)]
    return {"key": f"{model}|{probe}|g|validation|mixed|{idx}|img{idx}", "model": model, "probe": probe,
            "split": "validation", "subset": "mixed", "entry_idx": idx, "image_id": f"img{idx}",
            "data_source": "ADE", "obj_indices": [1, 2, 3, 4, 5], "correct_flags": list(correct),
            "tolerant_correct_flags": list(correct), "parsed_labels": labels, "tolerant_labels": labels,
            "finish_reason": ["length" if trunc else "stop"] * (1 if probe == "default" else 5)}


def test_rq1_tables(tmp_path, capsys):
    rows = [row("m", "default", 0, [1, 1, 1, 1, 0]), row("m", "default", 1, [0, 0, 0, 0, 0], trunc=True, unparsed=range(5)),
            row("m", "single", 0, [1, 1, 1, 1, 1]), row("m", "single", 1, [1, 0, 0, 0, 0])]
    p = tmp_path / "x.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    data = rq1.load([str(p)])

    t1 = {(r["subset"], r["probe"]): r for r in rq1.table1(data)}
    d = t1[("In-the-Wild", "default")]
    assert (d["n_images"], d["n_objects"], d["n_truncated"]) == (2, 10, 1)
    assert abs(d["acc_tolerant"] - 0.4) < 1e-9 and abs(d["acc_strict"] - 0.4) < 1e-9
    assert abs(d["acc_tolerant_trunc_dropped"] - 0.8) < 1e-9
    assert abs(d["parse_fail_tolerant"] - 0.5) < 1e-9
    assert abs(d["parse_fail_strict"] - 0.6) < 1e-9  # 5 None + 1 off-list "dog"
    assert abs(t1[("In-the-Wild", "single")]["acc_tolerant"] - 0.6) < 1e-9

    res = rq1.paired_test(rq1.group(data, "m", "single", "validation", ("mixed",)),
                          rq1.group(data, "m", "default", "validation", ("mixed",)))
    # boxes right under single only: img0 box5, img1 box1 -> b = 2; right under default only: none -> c = 0
    assert (res["n_img"], res["t"]["b"], res["t"]["c"]) == (2, 2, 0)
    assert abs(res["t"]["diff"] - (-0.2)) < 1e-9 and abs(res["t"]["p"] - 0.5) < 1e-9
    assert res["t_kept"][1] == 1

    pos = rq1.positions(data)[("m", "default", "validation", "mixed")]
    assert pos["t"] == [0.5, 0.5, 0.5, 0.5, 0.0]

    rq1.paired_section(data)
    out = capsys.readouterr().out
    assert "skipped" in out and "single (x) vs default (y)" in out


def test_token_limit_rule(tmp_path):
    """A call at finish_reason 'length' makes its objects wrong even when the cut answer parsed right."""
    dflt = row("m", "default", 0, [1, 1, 1, 1, 1], trunc=True)  # all five stored correct, call cut
    sing = row("m", "single", 0, [1, 1, 1, 1, 1])
    sing["finish_reason"] = ["stop", "stop", "length", "stop", "stop"]  # only call 3 (box 3) cut
    sing["asked_objects"] = [1, 2, 3, 4, 5]
    p = tmp_path / "x.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in [dflt, sing]) + "\n")
    data = rq1.load([str(p)])
    d = data[("m", "default", "validation", "mixed")][(0, "img0")]
    s = data[("m", "single", "validation", "mixed")][(0, "img0")]
    assert d["t"] == d["s"] == [0, 0, 0, 0, 0] and d["flipped"] == {"t": 5, "s": 5} and d["n_cut_calls"] == 1
    assert s["t"] == s["s"] == [1, 1, 0, 1, 1] and s["flipped"] == {"t": 1, "s": 1} and s["n_cut_calls"] == 1
    t1 = {r["probe"]: r for r in rq1.table1(data) if r["subset"] == "In-the-Wild"}
    assert t1["single"]["n_objects"] == 5 and abs(t1["single"]["acc_strict"] - 0.8) < 1e-9
    assert t1["default"]["n_token_limit_calls"] == 1 and t1["default"]["acc_tolerant"] == 0
