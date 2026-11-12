"""CPU test for analysis/forcing_table.py on hand-made rows: B outcomes per condition, strict re-read
by key, the token-limit rule, paired counts against default, and the dose-response series."""
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("forcing_table", os.path.join(HERE, "forcing_table.py"))
ft = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ft)

A, B, C = "door", "drawer", "zebra"


def row(probe, subset, idx, b_label, tf_mode=None, n_given=None, place="user", cf=None, cut=False, answer=None):
    gold = [A] * 4 + [B] if subset == "AAAAB" else [B] + [A] * 4
    b = 5 if subset == "AAAAB" else 1
    one = probe == "counterfactual" or (probe == "teacher_forcing" and tf_mode == "oneshot")
    if one:
        objs, calls = [b], 1
        labels = [b_label]
    else:
        objs, calls = [1, 2, 3, 4, 5], (1 if probe == "default" else 5)
        labels = [b_label if k == b else A for k in objs]
    if answer is None:
        answer = f"obj{b}: {b_label}"
    variant = "greedy,seed=0" + (f",given={n_given}" if n_given is not None else "") + (",place=assistant" if place == "assistant" else "")
    return {"key": f"m|{probe}|{tf_mode}|{variant}|validation|{subset}|{idx}", "model": "m", "probe": probe,
            "tf_mode": tf_mode, "variant": variant, "n_given": n_given, "prefix_place": place, "budget": None,
            "no_think": False, "split": "validation", "subset": subset, "entry_idx": idx, "image_id": f"img{idx}",
            "data_source": "ADE", "obj_indices": objs, "asked_objects": [None] if calls == 1 and not one else objs,
            "all_gold_labels": gold, "parsed_labels": labels, "tolerant_labels": labels,
            "counterfactual_class": cf, "stripped_answer": [answer] * calls,
            "finish_reason": ["length" if cut else "stop"] * calls}


def test_forcing_table(tmp_path, capsys):
    rows = [
        row("default", "AAAAB", 0, A), row("default", "AAAAB", 1, B), row("default", "BAAAA", 0, B),
        row("single", "AAAAB", 0, B), row("single", "AAAAB", 1, B), row("single", "BAAAA", 0, B),
        row("teacher_forcing", "AAAAB", 0, A, tf_mode="oneshot"), row("teacher_forcing", "AAAAB", 1, A, tf_mode="oneshot"),
        # BAAAA answer in prefix order: segment 1 is obj2 (A); strict must read obj1 by its key
        row("teacher_forcing", "BAAAA", 0, B, tf_mode="oneshot", answer=f"obj2: {A}, obj3: {A}, obj4: {A}, obj5: {A}, obj1: {B}"),
        row("teacher_forcing", "AAAAB", 0, B, tf_mode="oneshot", n_given=0),
        row("teacher_forcing", "AAAAB", 1, B, tf_mode="oneshot", n_given=0, cut=True),
        row("counterfactual", "AAAAB", 0, C, cf=C), row("counterfactual", "AAAAB", 1, B, cf=C),
        row("teacher_forcing", "AAAAB", 0, A, tf_mode="incremental"),
    ]
    rows[8]["parsed_labels"] = [A]  # what a position-based strict scorer wrote
    p = tmp_path / "x.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    data = ft.load([str(p)])

    assert ft.b_record(rows[8])["s"] == {"ok": 1, "A": 0, "C": 0}  # re-read by key
    cut = data[("m", "TF one-shot, given=0", "validation", "AAAAB")][(1, "img1")]
    assert cut["cut"] and cut["t"] == {"ok": 0, "A": 0, "C": 0}

    t4 = {(r["order"], r["condition"]): r for r in ft.table4(data) if r["split"] == "Unseen"}
    assert t4[("AAAAB", "default")]["ok_t"] == 0.5 and t4[("AAAAB", "default")]["A_t"] == 0.5
    tf = t4[("AAAAB", "TF one-shot")]
    assert tf["ok_t"] == 0 and tf["A_t"] == 1
    # paired vs default on AAAAB: img1 right under default only -> b = 1, c = 0
    assert (tf["vs_ok"]["n"], tf["vs_ok"]["b"], tf["vs_ok"]["c"]) == (2, 1, 0)
    assert tf["vs_A"]["b"] == 0 and tf["vs_A"]["c"] == 1  # img1 becomes B=A
    assert t4[("AAAAB", "CF")]["C_t"] == 0.5
    assert t4[("Adversarial", "TF one-shot")]["n_images"] == 3
    assert t4[("Adversarial", "TF one-shot")]["ok_s"] == 1 / 3
    assert t4[("AAAAB", "TF incremental")]["A_t"] == 1
    # against single: B right alone on img0 and img1, labelled A under TF one-shot on both
    v1 = tf["vs1_A"]
    assert (v1["n"], v1["b"], v1["c"], tf["vs1_ok"]["b"]) == (2, 0, 2, 2)
    assert "vs1_ok" not in t4[("AAAAB", "single")] and t4[("AAAAB", "default")]["vs1_ok"]["n"] == 2

    series = {(s["probe"], s["order"]): s for s in ft.dose(data) if s["split"] == "validation"}
    pts = {q["n"]: q for q in series[("TF one-shot", "Adversarial")]["pts"]}
    assert set(pts) == {0, 4} and pts[0]["ok"][0] == 0.5 and pts[4]["A"][0] == 2 / 3
    assert {q["n"] for q in series[("TF one-shot", "AAAAB")]["pts"]} == {0, 4}
    assert ("TF one-shot", "BAAAA") not in series  # one dose point there
    assert not [k for k in series if k[0] == "CF"]  # only one dose point
    ft.plot(ft.dose(data), str(tmp_path / "fig.png"))
    assert (tmp_path / "fig.png").stat().st_size > 0

    # dose tests: AAAAB has given=0 and given=4 on img0 and img1; BAAAA has no given=0 run
    dt = {r["order"]: r for r in ft.dose_tests(data) if r["split"] == "Unseen" and r["probe"] == "TF one-shot"}
    assert set(dt) == {"Adversarial", "AAAAB"}
    d = dt["AAAAB"]
    # B=A: 0 -> 1 on both images (4 labels apart); acc: img0 1 -> 0, img1 0 (cut) -> 0
    assert d["n_images"] == 2 and d["slope_A"]["diff"] == 0.25 and d["slope_ok"]["diff"] == -0.125
    assert (d["vs0_A_4"]["b"], d["vs0_A_4"]["c"]) == (0, 2) and 0.4 < d["slope_A"]["p"] <= 1
    assert dt["Adversarial"]["n_images"] == 2  # pooled keeps only images with every dose point
    ft.print_dose_tests(ft.dose_tests(data))
    assert "| m | Unseen | TF one-shot | AAAAB | 2 | +25.0 " in capsys.readouterr().out
    ft.write_dose_csv(ft.dose_tests(data), str(tmp_path / "d.csv"))
    assert (tmp_path / "d.csv").read_text().splitlines()[0].startswith("model,split,probe,order,n_images,slope_A,")

    ft.print_table4(ft.table4(data))
    out = capsys.readouterr().out
    assert "| m | Unseen | BAAAA | TF one-shot | 1 | 0 |" in out

    # sensitivity: img1 of "TF one-shot, given=0" is cut, so only img0 is compared there
    g0 = t4[("AAAAB", "TF one-shot, given=0")]
    assert g0["vs_ok"]["n"] == 2 and g0["vs_ok_uncut"]["n"] == 1 and g0["vs_A_uncut"]["n"] == 1
    ft.print_uncut(ft.table4(data))
    assert "| m | Unseen | AAAAB | TF one-shot, given=0 | 1 |" in capsys.readouterr().out
    ft.print_vs_single(ft.table4(data))
    assert "| m | Unseen | AAAAB | TF one-shot | 2 | -100.0 " in capsys.readouterr().out
    ft.write_csv(ft.table4(data), str(tmp_path / "t4.csv"))
    head = (tmp_path / "t4.csv").read_text().splitlines()[0]
    assert "A_vs_default_uncut_holm" in head and head.endswith("A_vs_single_p,A_vs_single_holm")


def test_slope_test():
    import numpy as np
    y = np.tile([0.0, 0.0, 0.0, 1.0, 1.0], (40, 1))  # every image flips to 1 at three labels given
    t = ft.slope_test(np.arange(5.0), y, reps=2000)
    assert abs(t["diff"] - 0.3) < 1e-9 and t["p"] < 0.001
    flat = ft.slope_test(np.arange(5.0), np.ones((40, 5)), reps=2000)
    assert flat["diff"] == 0 and flat["p"] == 1


def test_homogeneous_control(tmp_path):
    def homog(probe, idx, label, tf_mode=None):
        r = row(probe, "AAAAB", idx, label, tf_mode=tf_mode)
        r.update(subset="homogenous", all_gold_labels=[A] * 5, key=r["key"].replace("AAAAB", "homogenous"))
        return r
    rows = [homog("default", 0, B), homog("default", 1, A), homog("teacher_forcing", 0, A, "oneshot"),
            homog("teacher_forcing", 1, A, "oneshot"), row("default", "AAAAB", 0, A)]
    p = tmp_path / "h.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    t4 = {(r["order"], r["condition"]): r for r in ft.table4(ft.load([str(p)]))}
    assert t4[(ft.CONTROL, "default")]["ok_t"] == 0.5 and t4[(ft.CONTROL, "TF one-shot")]["ok_t"] == 1
    assert t4[(ft.CONTROL, "TF one-shot")]["vs_ok"]["c"] == 1 and "vs_A" not in t4[(ft.CONTROL, "TF one-shot")]
    # no forcing run on homogenous -> no control rows
    p.write_text("\n".join(json.dumps(r) for r in rows[:2] + rows[4:]) + "\n")
    assert not [r for r in ft.table4(ft.load([str(p)])) if r["order"] == ft.CONTROL]


def test_assistant_prefill(tmp_path, capsys):
    pre = f"obj1: {A}, obj2: {A}, obj3: {A}, obj4: {A}, obj5:"

    def asst(idx, cont, fin="stop"):
        r = row("teacher_forcing", "AAAAB", idx, None, tf_mode="oneshot", place="assistant")
        r.update(prefix_used=[" " + pre], stripped_answer=["" if cont is None else pre + cont], finish_reason=[fin])
        return r
    redo = f" {A}\n\nWait, no, that's wrong.\nobj1: {A}, obj2: {A}, obj3: {A}, obj4: {A}, obj5: {B}"
    rows = [asst(0, f" {A}"),                       # copies A and stops
            asst(1, redo),                          # copies A, then re-checks and fixes B
            asst(2, f" {A}\n\nWait, no. " + "look " * 50, "length"),  # copies A, re-check cut
            asst(3, None, "length"),                # thinking never closed
            asst(4, f"\n\nobj1: {A}, obj2: {A}, obj3: {A}, obj4: {A}, obj5: {B}")]  # restarts its own list
    rows += [row("default", "AAAAB", i, B) for i in range(5)]
    assert ft.b_record(rows[2])["cut"] is False and ft.b_record(rows[2])["t"]["A"] == 1
    assert ft.b_record(rows[3])["cut"] is True
    rs = ft.b_record(rows[4])
    assert rs["restart"] == 1 and rs["t"] == {"ok": 0, "A": 0, "C": 0} and rs["f"]["ok"] == 1
    assert ft.b_record(rows[1])["restart"] == 0
    p = tmp_path / "a.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    data = ft.load([str(p)])
    t4 = {(r["order"], r["condition"]): r for r in ft.table4(data)}
    a = t4[("AAAAB", "TF one-shot, assistant")]
    assert (a["n_images"], a["n_cut"], a["A_t"], a["A_s"]) == (5, 1, 0.6, 0.6)
    ap = {r["order"]: r for r in ft.after_prefill(data)}["AAAAB"]
    assert ap["more"][0] == 0.6 and ap["restart"][0] == 0.2 and ap["unresolved"][0] == 0.2
    assert ap["final_ok"][0] == 0.4 and ap["final_A"][0] == 0.2
    ft.print_after_prefill(ft.after_prefill(data))
    assert "| m | Unseen | AAAAB | TF one-shot, assistant | 5 | 1 |" in capsys.readouterr().out


def test_holm_families(tmp_path):
    assert [ft.family(c, "AAAAB") for c in ("TF one-shot", "CF", "single", "TF one-shot, given=2",
                                            "CF, assistant", "CF near", "CF far, given=1")] == \
        ["core", "core", "core", "dose", "placement", "C near/far", "dose"]
    assert ft.family("TF one-shot", ft.CONTROL) == "control"

    def holms(rows):
        p = tmp_path / "h.jsonl"
        p.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
        return {(r["order"], r["condition"]): r["vs_A"]["holm"] for r in ft.table4(ft.load([str(p)])) if r.get("vs_A")}
    core = [row("default", "AAAAB", i, B) for i in range(8)]
    core += [row("teacher_forcing", "AAAAB", i, A if i < 6 else B, tf_mode="oneshot") for i in range(8)]
    core += [row("counterfactual", "AAAAB", i, A if i < 2 else B, cf=C) for i in range(8)]
    before = holms(core)
    after = holms(core + [row("teacher_forcing", "AAAAB", i, A, tf_mode="oneshot", n_given=2) for i in range(8)])
    assert all(after[k] == v for k, v in before.items())  # the dose rows do not touch the core family
    assert after[("AAAAB", "TF one-shot, given=2")] < 1


def test_out_of_scope_rows_are_dropped():
    r = row("default", "AAAAB", 0, A)
    assert ft.condition(dict(r, budget=512)) is None
    assert ft.condition(dict(r, no_think=True)) is None
    assert ft.condition(dict(r, variant="recommended,seed=0")) is None
    assert ft.b_record(dict(r, subset="mixed")) is None and ft.b_record(dict(r, subset="heterogenous")) is None
    assert ft.condition(row("counterfactual", "BAAAA", 0, B, cf=C, n_given=2, place="assistant")) == "CF, given=2, assistant"
    cf = row("counterfactual", "AAAAB", 0, C, cf=C)
    assert ft.condition(dict(cf, cf_mode="near")) == "CF near" and ft.condition(dict(cf, cf_mode="far")) == "CF far"
    assert ft.condition(dict(cf, cf_mode="random")) == "CF" == ft.condition(cf)
    assert ft.b_record(dict(cf, cf_mode="far"))["t"]["C"] == 1
