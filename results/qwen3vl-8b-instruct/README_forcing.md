# RQ2 forcing runs of qwen3vl-8b-instruct (Qwen3-VL-8B-Instruct)

Xingjian Liu's RQ2 forcing runs of Qwen3-VL-8B-Instruct on Adversarial ROPE (`AAAAB`, `BAAAA`; Seen = `train`, Unseen = `validation`) and the Homogeneous control. The RQ1 baseline in this folder (`rq1_*`, `README.md`) is Xiangchen Song's run; every comparison with `default` and `single` below uses those files. The probes, scoring and statistics are the same as for MiMo-VL-7B-RL-2508; `results/mimo-rl-2508/README.md` (section "RQ2 forcing probes" and after) describes them in full.

## Files

| file | contents | rows | calls | at the limit | size |
|---|---|---|---|---|---|
| `forcing_qwen3vl-8b-instruct_tf-oneshot_{train,validation}.jsonl` | one-shot teacher forcing: the four true A labels given, then B | 336 / 668 | 336 / 668 | 0 / 0 | 0.5 / 1.0 MB |
| `forcing_qwen3vl-8b-instruct_tf-incremental_{train,validation}.jsonl` | moh's incremental teacher forcing (5 calls per image) | 336 / 668 | 1,680 / 3,340 | 0 / 5 | 0.8 / 1.6 MB |
| `forcing_qwen3vl-8b-instruct_cf_{train,validation}.jsonl` | counterfactual prefix: a wrong class C (seeded) on the four other boxes | 336 / 668 | 336 / 668 | 0 / 0 | 0.5 / 1.0 MB |
| `forcing_dose_qwen3vl-8b-instruct_{train,validation}.jsonl` | one-shot TF with only the first n of the four labels (n = 0–3) | 1,344 / 2,672 | same | 0 / 0 | 2.1 / 4.2 MB |
| `forcing_place_qwen3vl-8b-instruct_{train,validation}.jsonl` | TF one-shot and CF with the labels written as the start of the model's answer | 672 / 1,336 | same | 0 / 0 | 1.1 / 2.1 MB |
| `forcing_homog_qwen3vl-8b-instruct_{train,validation}.jsonl` | one-shot TF on Homogeneous (`homogenous`) | 400 / 490 | same | 0 / 0 | 0.6 / 0.7 MB |
| `forcing_cfnear_qwen3vl-8b-instruct_{train,validation}.jsonl` | CF with C = the remaining class most similar to A | 336 / 668 | same | 0 / 0 | 0.5 / 1.0 MB |
| `forcing_cffar_qwen3vl-8b-instruct_{train,validation}.jsonl` | CF with C = the remaining class least similar to A | 336 / 668 | same | 0 / 0 | 0.5 / 1.1 MB |
| `forcing_tables.md` | full output of `analysis/forcing_table.py` on the RQ1 files and every forcing file here | | | | |
| `forcing_table4.csv` | Table 4 with CIs and p-values, one line per split x order x condition | | | | |
| `forcing_fig4_tests.csv`, `forcing_fig4_dose.png` | dose tests and Figure 4 for this model | | | | |
| `forcing_output_check.jsonl` | hand check of 50 raw outputs: key, condition, automatic reading, verdict, note | 50 | | | |

**Integrity.** Every condition has exactly one row per ROPE entry in each subset (168 + 168 Seen and 334 + 334 Unseen Adversarial; 400 Seen and 490 Unseen Homogeneous), with no duplicate keys and no broken lines (`publish_forcing.py`). Five of the 3,340 Unseen incremental calls hit the 1,024-token limit, all of them call 1 (box 1: four in `AAAAB`, and one in `BAAAA`, where box 1 is B); no other call did.

## How the runs were made

Great Lakes, account `cse595f26_class`, one NVIDIA A40 per job (`-p spgpu`), vLLM 0.11.0, model revision `0c351dd01ed87e9c1b53cbc748cba10e6187ff3b`, `max_tokens` 1024 (the model's setting in `harness/configs/models.yaml`), `max_model_len` 12288, greedy, `--chunk 128`, `--resume`. The core runs (TF one-shot, TF incremental, CF) use the team harness on `main` at `52429fe`, as the RQ1 run. The finer runs (dose, placement, Homogeneous, C near / far) use commit `df9d74d` on branch `rq2/forcing-probes`.

| job | run | split | elapsed |
|---|---|---|---|
| 65950295 | TF one-shot + CF | Unseen | 4:58 |
| 65950297 | TF incremental | Unseen | 5:11 |
| 65950299 | TF one-shot + CF | Seen | 3:25 |
| 65950301 | TF incremental | Seen | 2:02 |
| 65950372–65950375 | dose n = 0, 1, 2, 3 | Unseen | 2:30, 2:27, 2:26, 2:25 |
| 65950376 | placement (TF + CF) | Unseen | 5:08 |
| 65950378 | Homogeneous | Unseen | 2:18 |
| 65950379–65950382 | dose n = 0, 1, 2, 3 | Seen | 1:48, 1:47, 1:46, 1:46 |
| 65950383 | placement (TF + CF) | Seen | 3:20 |
| 65950385 | Homogeneous | Seen | 1:52 |
| 65950386 / 65950387 | C near / C far | Unseen | 5:13 / 2:39 |
| 65950388 / 65950389 | C near / C far | Seen | 1:57 / 1:55 |

Standby jobs 65950296, 65950298, 65950300, 65950302, 65950377 and 65950384 found nothing left and exited within 12 s. The commands are those of `results/mimo-rl-2508/README.md` with `MODEL=qwen3vl-8b-instruct`.

## Scoring

The tables come from `analysis/forcing_table.py` on branch `rq2/forcing-probes` (commit `aca3073`):

```bash
python analysis/forcing_table.py --out-dir results/qwen3vl-8b-instruct \
  results/qwen3vl-8b-instruct/rq1_qwen3vl-8b-instruct_*.jsonl results/qwen3vl-8b-instruct/forcing_*qwen3vl-8b-instruct_*.jsonl \
  > results/qwen3vl-8b-instruct/forcing_tables.md
```

Two points matter for this model:

- **Continued answers.** The one-shot prompt ends in `objK:`, and Qwen-Instruct often answers by continuing it. It writes only a bare class name (`drawer`), or, when fewer than four labels are given, B's label first and then the boxes that were not given (`cabinet, obj4: cabinet, obj5: door`). The harness's tolerant parser reads the bare form correctly, but it returns nothing for the second form, because other boxes are named and B is not. From commit `aca3073`, Table 4 reads B from the first segment before the first `objK:` when that segment names a candidate. An explicit `objK:` still wins. Column "B read before objK:" of the given-box table shows how often this was used: up to 84% of the `BAAAA` rows with three labels given, and never for MiMo-VL-7B-RL. Without it, accuracy on B under dose n = 2 and 3 looked 42–49 points lower than `default`.
- **Strict.** For the same reason, strict (moh's format, which needs `objK:`) reads almost nothing in the one-shot probes (e.g. 0.0–0.3% B=A on `AAAAB`). Read strict as a format measure here.

## Results

### Table 4 core (B labelled A, %, tolerant; vs `default` in points, Holm p within the core family)

| split | order | single | default | TF one-shot | TF incremental | CF: B=A | CF: B=C |
|---|---|---|---|---|---|---|---|
| Unseen | AAAAB | 20.1 | 35.9 | 41.3 (+5.4, 0.056) | 41.0 (+5.1, 0.076) | 10.8 (−25.1, 2.7e-20) | 41.0 |
| Unseen | BAAAA | 22.8 | 25.1 | **32.6 (+7.5, 7.0e-04)** | 25.4 (+0.3, 1; B asked first) | 18.9 (−6.3, 0.0071) | 21.0 |
| Seen | AAAAB | 14.9 | 26.8 | 32.7 (+6.0, 0.32) | 32.7 (+6.0, 0.32) | 9.5 (−17.3, 5.7e-07) | 31.5 |
| Seen | BAAAA | 18.5 | 18.5 | 26.2 (+7.7, 0.028) | 20.8 (+2.4, 0.5) | 12.5 (−6.0, 0.17) | 15.5 |

On `AAAAB` the incremental call for B is the same prompt as the one-shot call, and greedy decoding gives the same answers. Against `single`, B=A under TF one-shot is higher on Unseen `AAAAB` (+21.3, Holm 3.5e-18) and `BAAAA` (+9.9, 1.1e-04).

### Dose-response (B=A by labels given, %)

| split | order | n = 0 | 1 | 2 | 3 | 4 | slope / label (Holm p) | 4 vs 0 (Holm p) |
|---|---|---|---|---|---|---|---|---|
| Unseen | AAAAB | 29.6 | 33.2 | 35.0 | 36.5 | 41.3 | +2.7 (6.0e-04) | +11.7 (6.4e-08) |
| Unseen | BAAAA | 27.2 | 29.6 | 32.9 | 34.4 | 32.6 | +1.6 (6.0e-04) | +5.4 (0.033) |
| Seen | AAAAB | 20.2 | 27.4 | 30.4 | 29.2 | 32.7 | +2.7 (6.0e-04) | +12.5 (1.0e-04) |
| Seen | BAAAA | 20.8 | 26.2 | 25.6 | 27.4 | 26.2 | +1.2 (0.0056) | +5.4 (0.086) |

With no labels (n = 0), B=A on Unseen `AAAAB` is 6.3 points below `default` (Holm 4.3e-04, dose family): in `default` the model writes the four A labels itself before B.

### Labels written as the model's answer (placement)

Qwen-Instruct has no reasoning. It continues the forced line and stops in every row: "kept writing" and "restarted" are 0%.

| split | order | TF: B=A first label | CF: B=C first label | CF: B=A |
|---|---|---|---|---|
| Unseen | AAAAB | 47.6 (+11.7 vs default, 8.6e-10) | 83.5 | 0.0 |
| Unseen | BAAAA | 44.9 (+19.8, 3.3e-18) | 83.2 | 0.0 |
| Seen | AAAAB | 36.3 (+9.5, 4.0e-04) | 79.2 | 0.0 |
| Seen | BAAAA | 33.3 (+14.9, 1.2e-07) | 81.5 | 0.0 |

### Homogeneous control (accuracy on box 5, %)

| split | single | default | TF one-shot | TF vs default |
|---|---|---|---|---|
| Unseen | 83.1 | 85.3 | 95.9 | +10.6 (Holm 1.8e-15) |
| Seen | 91.5 | 93.8 | 98.8 | +5.0 (Holm 5.7e-06) |

### C near / far

B labelled C (%): Unseen `AAAAB` random 41.0, near 32.3, far 29.3; `BAAAA` 21.0, 20.1, 14.7. Seen `AAAAB` 31.5, 28.6, 36.9; `BAAAA` 15.5, 20.2, 10.1. Pooled over both orders on Unseen (paired, Holm over the model's 18 near/far comparisons), far C is copied 9.0 points less than random C (Holm 1.9e-05). Near does not differ from random after correction (−4.8, Holm 0.11). On Seen nothing differs. Unlike MiMo-VL-7B-RL, a C close to A is not accepted more.

### Hand check of 50 outputs

Same sample design as for MiMo-VL-7B-RL (25 rows per split, `random.Random(0)`, finished one-shot calls). Every row was read by hand; `forcing_output_check.jsonl` has the verdicts.

- **Labels in the user turn (34 rows).** Qwen-Instruct mostly continues from the given labels. In 20 rows it answers only B (19 bare class names, one `obj1: door`). In 7 dose rows it writes B's label first and then labels the boxes that were not given. In 7 rows it rewrites the whole list. Two of the three CF rows that rewrite keep C on all four given boxes. The four TF rewrites keep the given labels.
- **Labels written as its answer (16 rows).** It continues on the same line and stops in all 16. The label is A in 3 of the 8 TF rows and C in 3 of the 8 CF rows.

## Notes for the team

1. **The pull toward A shows in both orders.** True labels raise B=A by 5–8 points against `default`, and the dose slope is positive on `AAAAB` (+2.7 per label) and on `BAAAA` (+1.6 on Unseen). MiMo-VL-7B-RL showed no pull on `BAAAA`. The difference fits how the two models answer. Qwen-Instruct writes B right after the given labels; MiMo rewrites all five in box order, so in `BAAAA` it writes B first.
2. **Qwen-Instruct copies a wrong class.** Under CF in the user turn, B is labelled C in 41% of Unseen `AAAAB` items (MiMo-VL-7B-RL: 0.3%). Written as its own answer, C is copied onto B in 79–84% of items, and B is never labelled A.
3. **Labels in its own answer pull hardest.** Without reasoning to override them, true labels written as the start of the answer raise B=A by 9–20 points, more than the same labels in the user turn. MiMo-VL-7B-RL, which reasons first, showed almost no effect.
4. **Labels help when they are right.** On Homogeneous items, accuracy on box 5 rises by 10.6 (Unseen) and 5.0 (Seen) points.
5. **Read the tolerant parser.** Strict reads almost nothing for the one-shot probes, because the model answers with bare class names.
