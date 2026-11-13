# RQ2 forcing runs of mimo-sft-2508 (MiMo-VL-7B-SFT-2508)

Xingjian Liu's RQ2 forcing runs of MiMo-VL-7B-SFT-2508 on Adversarial ROPE (`AAAAB`, `BAAAA`; Seen = `train`, Unseen = `validation`) and the Homogeneous control. The probes, scoring and statistics are the same as for MiMo-VL-7B-RL-2508; `results/mimo-rl-2508/README.md` (section "RQ2 forcing probes" and after) describes them in full.

**The RQ1 baseline of this model is not in yet.** Until its `rq1_mimo-sft-2508_*` files are in this folder, the tables here give the rates under each probe, the dose tests (each n against n = 0), placement, the given-box table and C near / far against random C. They do not give any comparison with `default` or `single`. Once the RQ1 files arrive, the same command rebuilds every table with those comparisons.

## Files

| file | contents | rows | calls | at the limit | size |
|---|---|---|---|---|---|
| `forcing_mimo-sft-2508_tf-oneshot_{train,validation}.jsonl` | one-shot teacher forcing | 336 / 668 | 336 / 668 | 5 / 9 | 1.2 / 2.5 MB |
| `forcing_mimo-sft-2508_tf-incremental_{train,validation}.jsonl` | moh's incremental teacher forcing (5 calls per image) | 336 / 668 | 1,680 / 3,340 | 30 / 109 | 5.3 / 14.9 MB |
| `forcing_mimo-sft-2508_cf_{train,validation}.jsonl` | counterfactual prefix (random C, seeded) | 336 / 668 | 336 / 668 | 7 / 19 | 1.4 / 3.4 MB |
| `forcing_dose_mimo-sft-2508_{train,validation}.jsonl` | one-shot TF with only the first n of the four labels (n = 0–3) | 1,344 / 2,672 | same | 22 / 98 | 5.7 / 15.5 MB |
| `forcing_place_mimo-sft-2508_{train,validation}.jsonl` | TF one-shot and CF with the labels written as the start of the model's answer | 672 / 1,336 | same | 15 / 60 | 3.2 / 8.4 MB |
| `forcing_homog_mimo-sft-2508_{train,validation}.jsonl` | one-shot TF on Homogeneous (`homogenous`) | 400 / 490 | same | 1 / 1 | 1.0 / 1.3 MB |
| `forcing_cfnear_mimo-sft-2508_{train,validation}.jsonl` | CF with C = the remaining class most similar to A | 336 / 668 | same | 4 / 14 | 1.3 / 3.2 MB |
| `forcing_cffar_mimo-sft-2508_{train,validation}.jsonl` | CF with C = the remaining class least similar to A | 336 / 668 | same | 3 / 18 | 1.3 / 3.4 MB |
| `forcing_tables.md` | full output of `analysis/forcing_table.py` on every forcing file here | | | | |
| `forcing_table4.csv` | Table 4 rates with CIs, one line per split x order x condition (no comparison with `default` yet) | 68 | | | |
| `forcing_fig4_tests.csv`, `forcing_fig4_dose.png` | dose tests and Figure 4 for this model | | | | |
| `forcing_output_check.jsonl` | hand check of 50 raw outputs: key, condition, automatic reading, verdict, note | 50 | | | |
| `box_swap.md` | B=A answers that write B's class on an A box (`analysis/box_swap.py`, commit `d9225d5`; see the MiMo-VL-7B-RL README, section "Box swaps inside B=A") | | | | |

**Integrity.** Every condition has exactly one row per ROPE entry in each subset (168 + 168 Seen and 334 + 334 Unseen Adversarial; 400 Seen and 490 Unseen Homogeneous), with no duplicate keys and no broken lines (`publish_forcing.py`).

## How the runs were made

Great Lakes, account `cse595f26_class`, one NVIDIA A40 per job, vLLM 0.11.0, model revision `11e8fdc278f5e1e6a72f9561772a6d7cd6921d33`, `max_tokens` 8192, `max_model_len` 12288, greedy, `--chunk 128`, `--resume`. The core runs use the team harness on `main` at `52429fe`. The finer runs use commits on branch `rq2/forcing-probes`: `d1b7996` for dose and Homogeneous, `25a0244` for placement, and `df9d74d` for C near / far.

| job | run | split | elapsed |
|---|---|---|---|
| 65894400 | TF one-shot + CF | Unseen | 52:50 |
| 65894402 | TF incremental | Unseen | 58:26 |
| 65894404 | TF one-shot + CF | Seen | 29:52 |
| 65894406 | TF incremental | Seen | 22:25 |
| 65894408–65894411 | dose n = 0, 1, 2, 3 | Unseen | 32:02, 31:55, 32:04, 29:55 |
| 65894414 | Homogeneous | Unseen | 8:43 |
| 65894415–65894418 | dose n = 0, 1, 2, 3 | Seen | 15:26, 11:06, 11:57, 14:17 |
| 65894421 | Homogeneous | Seen | 6:26 |
| 65920351 | placement (TF + CF) | Unseen | 58:54 |
| 65920353 | placement (TF + CF) | Seen | 24:54 |
| 65937213 / 65937214 | C near / C far | Unseen | 29:23 / 26:29 |
| 65937215 / 65937216 | C near / C far | Seen | 14:36 / 11:19 |

Every piece finished within its first job. The standby jobs (65894401, 65894403, 65894405, 65894407, 65920352, 65920354, and 65951506–65951525 from `rope-pin-df9d74d`) found nothing left and exited within 12 s. The commands are those of `results/mimo-rl-2508/README.md` with `MODEL=mimo-sft-2508`.

## Scoring

The tables come from `analysis/forcing_table.py` on branch `rq2/forcing-probes` (commit `aca3073`):

```bash
python analysis/forcing_table.py --out-dir results/mimo-sft-2508 \
  results/mimo-sft-2508/forcing_*mimo-sft-2508_*.jsonl > results/mimo-sft-2508/forcing_tables.md
# once this model's RQ1 files are here, add: results/mimo-sft-2508/rq1_mimo-sft-2508_*.jsonl
```

Unlike MiMo-VL-7B-RL, the SFT model answers in the plain `obj1: …, obj5: …` format, so strict and tolerant agree here (for example 51.5% and 51.5% B=A under TF one-shot on Unseen `AAAAB`).

## Results

### B under each probe (%, tolerant)

| split | order | TF one-shot: B acc / B=A | TF incremental: B acc / B=A | CF: B acc / B=A / B=C |
|---|---|---|---|---|
| Unseen | AAAAB | 30.8 / 51.5 | 30.5 / 51.2 | 35.0 / 43.1 / 1.8 |
| Unseen | BAAAA | 44.0 / 34.4 | 42.5 / 32.9 (B asked first) | 41.3 / 35.3 / 0.6 |
| Seen | AAAAB | 39.9 / 42.9 | 36.9 / 45.2 | 41.7 / 34.5 / 2.4 |
| Seen | BAAAA | 54.2 / 23.8 | 53.0 / 21.4 (B asked first) | 51.2 / 21.4 / 0.0 |

### Dose-response (B=A by labels given, %)

| split | order | n = 0 | 1 | 2 | 3 | 4 | slope / label (Holm p) | 4 vs 0 (Holm p) |
|---|---|---|---|---|---|---|---|---|
| Unseen | AAAAB | 32.0 | 37.7 | 40.4 | 48.5 | 51.5 | **+5.0 (6.0e-04)** | **+19.5 (7.1e-13)** |
| Unseen | BAAAA | 33.2 | 32.6 | 33.8 | 33.5 | 34.4 | +0.3 (0.38) | +1.2 (1) |
| Seen | AAAAB | 21.4 | 23.8 | 24.4 | 32.1 | 42.9 | **+5.1 (6.0e-04)** | **+21.4 (1.2e-07)** |
| Seen | BAAAA | 21.4 | 20.2 | 21.4 | 22.0 | 23.8 | +0.7 (0.37) | +2.4 (1) |

B accuracy falls by 2.9 (Unseen) and 3.2 (Seen) points per label on `AAAAB` (Holm 6.0e-04 for both) and does not change on `BAAAA`.

### Labels written as the model's answer (placement)

The SFT model never re-checks. It writes one label after the forced line and stops: "kept writing" is 0–0.6% and "restarted" is 0%.

| split | order | TF: B acc / B=A (first label) | CF: B acc / B=C (first label) | CF: B=A |
|---|---|---|---|---|
| Unseen | AAAAB | 32.3 / 49.1 | 11.1 / 79.0 | 0.0 |
| Unseen | BAAAA | 43.1 / 40.1 | 7.2 / 86.5 | 0.9 |
| Seen | AAAAB | 43.5 / 35.7 | 20.2 / 75.0 | 0.0 |
| Seen | BAAAA | 48.8 / 27.4 | 10.7 / 84.5 | 0.0 |

### Homogeneous control

Accuracy on box 5 under TF one-shot: 88.2% (Unseen) and 95.2% (Seen). The `default` baseline comes with the RQ1 files.

### What the answer does with the given boxes (one-shot, labels in the user turn)

The model writes all five labels in 100% of answered rows. Under TF one-shot it keeps the four given A labels in 83.5 / 80.7% (Unseen `AAAAB` / `BAAAA`) and 92.2 / 87.3% (Seen). Under CF it keeps C on at least one given box in 0.6–4.2% of answers and relabels the given boxes A in 64–71%. With C near those rates become 6.2–22.3% and 51–63%.

### C near / far

Pooled over both orders and paired with the random C: near C is copied onto B 3.7 points more often on Unseen (Holm 8.4e-05) and 4.2 on Seen (Holm 0.052), and 3.9 / 4.5 points more often than far C (Holm 4.1e-04 / 0.021). Far does not differ from random. B=A does not differ between the three. This is the same pattern as MiMo-VL-7B-RL.

### Hand check of 50 outputs

Same sample design as for MiMo-VL-7B-RL (25 rows per split, `random.Random(0)`, finished one-shot calls). Every row was read by hand; `forcing_output_check.jsonl` has the verdicts.

- **Labels in the user turn (34 rows).** The model never continues from the given labels. Every answer writes all five labels in box order. In 1 of the 26 rows with true labels it changes a given label; in all 8 CF rows it replaces C with its own classes.
- **Labels written as its answer (16 rows).** It writes one label after the forced line and stops in all 16. The label is A in 3 of the 8 TF rows and C in 6 of the 8 CF rows.

## Notes for the team

1. **The dose effect is about twice as strong as in the RL model.** On `AAAAB`, B=A rises by 5.0 points per true label (Unseen; 5.1 Seen), from 32.0% with none to 51.5% with all four. MiMo-VL-7B-RL gives 2.6 and 2.1 points per label. On `BAAAA` both models are flat. Whether this means RL training weakens the pull, or only that the SFT model starts from a different baseline, needs the SFT RQ1 `default` run.
2. **The SFT model does not re-check its own answer line.** After four forced C labels it copies C onto B in 75–87% of items and never corrects it. MiMo-VL-7B-RL copies C in 31–56% of first labels, then often writes "Wait, no" and re-checks.
3. **Like the RL model, it rewrites the whole list and rejects C in the user turn** (B=C 0–2.4%). A C close to A is accepted somewhat more often.
