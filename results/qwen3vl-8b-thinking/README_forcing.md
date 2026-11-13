# RQ2 forcing runs of qwen3vl-8b-thinking (Qwen3-VL-8B-Thinking)

Xingjian Liu's RQ2 forcing runs of Qwen3-VL-8B-Thinking on Adversarial ROPE (`AAAAB`, `BAAAA`; Seen = `train`, Unseen = `validation`) and the Homogeneous control. The probes, scoring and statistics are the same as for MiMo-VL-7B-RL-2508; `results/mimo-rl-2508/README.md` (section "RQ2 forcing probes" and after) describes them in full.

**What this folder has.** The core probes (TF one-shot, TF incremental, CF), the dose series, placement, the Homogeneous control, and the 50-output hand check. **C near / far are still running** on Great Lakes. They will be added here with the final tables.

**The RQ1 baseline of this model is not in yet** (Zhongqi's run). Until its `rq1_qwen3vl-8b-thinking_*` files are in this folder, the tables here give:
- the rates under each probe;
- the dose tests (each n against n = 0);
- placement, tested by `forcing_place_tests.md` against the same labels in the user turn and against n = 0;
- the given-box table.

They give no comparison with `default` or `single`. Once the RQ1 files arrive, the same command rebuilds every table with those comparisons.

## Files

| file | contents | rows | calls | at the limit | size |
|---|---|---|---|---|---|
| `forcing_qwen3vl-8b-thinking_tf-oneshot_{train,validation}.jsonl` | one-shot teacher forcing: the four true A labels given, then B | 336 / 668 | 336 / 668 | 8 / 42 | 2.1 / 6.2 MB |
| `forcing_qwen3vl-8b-thinking_tf-incremental_{train,validation}.jsonl` | moh's incremental teacher forcing (5 calls per image) | 336 / 668 | 1,680 / 3,340 | 95 / 305 | 13.6 / 36.1 MB |
| `forcing_qwen3vl-8b-thinking_cf_{train,validation}.jsonl` | counterfactual prefix: a wrong class C (seeded) on the four other boxes | 336 / 668 | 336 / 668 | 17 / 54 | 3.0 / 7.7 MB |
| `forcing_dose_qwen3vl-8b-thinking_{train,validation}.jsonl` | one-shot TF with only the first n of the four labels (n = 0–3) | 1,344 / 2,672 | same | 84 / 248 | 12.9 / 32.7 MB |
| `forcing_place_qwen3vl-8b-thinking_{train,validation}.jsonl` | TF one-shot and CF with the labels written as the start of the model's answer, after its reasoning | 672 / 1,336 | same | 52 / 146 | 6.9 / 17.0 MB |
| `forcing_homog_qwen3vl-8b-thinking_{train,validation}.jsonl` | one-shot TF on Homogeneous (`homogenous`) | 400 / 490 | same | 4 / 18 | 1.5 / 3.0 MB |
| `forcing_tables.md` | full output of `analysis/forcing_table.py` on every forcing file here | | | | |
| `forcing_table4.csv` | Table 4 rates with CIs, one line per split x order x condition (no comparison with `default` yet) | | | | |
| `forcing_fig4_tests.csv`, `forcing_fig4_dose.png` | dose tests and Figure 4 for this model | | | | |
| `forcing_place_tests.md` | placement against labels in the user turn and against n = 0, paired (`analysis/place_tests.py`) | | | | |
| `forcing_output_check.jsonl` | hand check of 50 raw outputs: key, condition, automatic reading, verdict, note | 50 | | | |
| `box_swap.md` | B=A answers that write B's class on an A box (`analysis/box_swap.py`, commit `d9225d5`; see the MiMo-VL-7B-RL README, section "Box swaps inside B=A") | | | | |

**Integrity.** `publish_forcing.py` checked every file:
- Every condition has exactly one row per ROPE entry in each subset: 168 + 168 Seen and 334 + 334 Unseen Adversarial, 400 Seen and 490 Unseen Homogeneous.
- There are no duplicate keys and no broken lines.

On 2026-11-13 the home quota on Great Lakes filled during the C near run. That run is not in this folder yet. It is being redone from its last good row, and none of the files here was written in that window.

**Calls at the token limit.** On Unseen items these calls reach 8,192 tokens (Seen in parentheses):
- one-shot: 6.3% (2.4%)
- CF: 8.1% (5.1%)
- incremental: 9.1% (5.7%)
- dose: 7.2–12.3% per n and order (3.0–8.9%)
- placement: 9.9–12.9% (6.0–10.1%)
- Homogeneous: 3.7% (1.0%)

Every one of them is still inside its reasoning: none closed `</think>`, and the answer is empty. In the incremental runs they are spread over all five calls (25–38 calls per box and order on Unseen). In placement a cut call never reached the forced labels. The harness never closed the reasoning by force. As for the other models, a cut call is scored wrong and never A.

## How the runs were made

**Setup:**
- Great Lakes, account `cse595f26_class`, one NVIDIA A40 per job (`-p spgpu`).
- vLLM 0.11.0, model revision `92f3c4b4feadd3a016ef468d103bb5f58b2a2c6b`.
- `max_tokens` 8192 (the model's setting in `harness/configs/models.yaml`; the model card allows 40,960) and `max_model_len` 12288.
- Greedy decoding, `--chunk 128`, `--resume`.

**Code:**
- The core runs use the team harness on `main` at `52429fe`, as the other models' core runs.
- The finer runs use commit `df9d74d` on branch `rq2/forcing-probes` (dose, Homogeneous, placement, C near / far).

| job | run | split | elapsed |
|---|---|---|---|
| 65950450 | TF one-shot + CF | Unseen | 1:20:04 |
| 65950459 | TF incremental | Unseen | 2:33:56 |
| 65950461 | TF one-shot + CF | Seen | 35:51 |
| 65950463 | TF incremental | Seen | 54:53 |
| 65950468–65950471 | dose n = 0, 1, 2, 3 | Unseen | 44:30, 49:05, 45:29, 40:52 |
| 65950472 | placement (TF one-shot + CF) | Unseen | 1:39:34 |
| 65950474 | Homogeneous | Unseen | 20:20 |
| 65950475–65950477, 65950481 | dose n = 0, 1, 2, 3 | Seen | 18:43, 19:59, 19:47, 19:08 |
| 65950482 | placement (TF one-shot + CF) | Seen | 42:08 |
| 65950484 | Homogeneous | Seen | 14:12 |

**Notes on the jobs:**
- Every piece finished within its first job.
- The standby jobs (65950452, 65950460, 65950462, 65950464, 65950473, 65950483) found nothing left and exited within 8 s.
- Smoke test 65950440 (placement, 16 images) ran first.
- The commands are those of `results/mimo-rl-2508/README.md` with `MODEL=qwen3vl-8b-thinking`.

## Scoring

The tables come from `analysis/forcing_table.py` on branch `rq2/forcing-probes` (commit `aca3073`):

```bash
python analysis/forcing_table.py --out-dir results/qwen3vl-8b-thinking \
  results/qwen3vl-8b-thinking/forcing_*qwen3vl-8b-thinking_*.jsonl > results/qwen3vl-8b-thinking/forcing_tables.md
# once Zhongqi's RQ1 files are here, add: results/qwen3vl-8b-thinking/rq1_qwen3vl-8b-thinking_*.jsonl
python analysis/place_tests.py qwen3vl-8b-thinking results/qwen3vl-8b-thinking/forcing_*qwen3vl-8b-thinking_*.jsonl \
  > results/qwen3vl-8b-thinking/forcing_place_tests.md
```

**Strict and tolerant parsing.** Like the MiMo models, Qwen-Thinking reasons and then writes the plain `obj1: …, obj5: …` list. Strict and tolerant parsing therefore agree for every one-shot probe (e.g. 41.6% and 41.6% B=A under TF one-shot on Unseen `AAAAB`). They differ only under TF incremental. There the model answers every call with all five labels, which both parsers read, but strict follows moh's rule: after the first call of an image it cannot parse (here, a cut call), every later box of that image counts wrong.

## Results

### B under each core probe (%, tolerant)

| split | order | TF one-shot: B acc / B=A | TF incremental: B acc / B=A | CF: B acc / B=A / B=C |
|---|---|---|---|---|
| Unseen | AAAAB | 38.9 / 41.6 | 38.3 / 42.2 | 41.9 / 33.8 / 0.9 |
| Unseen | BAAAA | 42.8 / 36.2 | 43.4 / 32.0 (B asked first) | 37.4 / 34.4 / 1.8 |
| Seen | AAAAB | 46.4 / 32.7 | 45.8 / 33.3 | 50.0 / 28.6 / 1.8 |
| Seen | BAAAA | 49.4 / 29.8 | 51.2 / 22.0 (B asked first) | 52.4 / 24.4 / 1.2 |

### Dose: how many true labels are given (TF one-shot, n = 0–4)

B=A rises with every label in both orders (`forcing_fig4_tests.csv`). Slopes are per label, with permutation tests at 10,000 shuffles, so the smallest p is 1e-4. The 4 vs 0 comparisons use exact McNemar. Holm adjusts per model and outcome.

| split | order | B=A, n = 0 → 4 | slope [95% CI] | p (Holm) | 4 vs 0 [95% CI] | p (Holm) |
|---|---|---|---|---|---|---|
| Unseen | `AAAAB` | 29.9 → 41.6 | +3.0 [+2.0, +4.0] | 6.0e-04 | +11.7 [+8.1, +15.9] | 1.7e-07 |
| Unseen | `BAAAA` | 30.5 → 36.2 | +1.5 [+0.7, +2.3] | 6.0e-04 | +5.7 [+2.4, +9.3] | 0.019 |
| Seen | `AAAAB` | 20.8 → 32.7 | +3.1 [+1.7, +4.5] | 6.0e-04 | +11.9 [+6.5, +17.9] | 0.0013 |
| Seen | `BAAAA` | 19.6 → 29.8 | +2.3 [+1.1, +3.6] | 6.0e-04 | +10.1 [+4.8, +16.1] | 0.012 |

On images where neither call was cut, 4 vs 0 on Unseen is +10.7 (`AAAAB`) and +5.5 (`BAAAA`). B accuracy falls with the labels on `AAAAB`: −1.9 points per label on Unseen (Holm 0.001) and −1.7 on Seen (Holm 0.018). It does not change on `BAAAA`.

**The labels pull B in `BAAAA` too, although the model writes B first there.** The model rewrites all five labels in box order (next section). So in `BAAAA` no label comes before B in its answer, yet four given labels still raise B=A by 5.7 points on Unseen. That is half the `AAAAB` effect, and about the size of Qwen-Instruct's `BAAAA` pull. MiMo-VL-7B-RL and MiMo-VL-7B-SFT, which also rewrite the list, are flat on `BAAAA`.

**The reasoning goes back to the given labels.** We counted, by keyword, which reasoning traces refer to the given labels. The keywords were "given", "example", "problem statement", "provided" and the like, and the script is `analysis/think_cite.py` on the code branch. On Unseen `BAAAA`, the reasoning of the n = 4 call refers to them in 81% of the 21 images where four labels turn B into A (B not A with no labels, A with four). It does so in 52% of the images where B is correct with and without the labels. On `AAAAB` the shares are 65% against 24%. Only images where neither call was cut are counted. A typical trace calls the labels "the example in the problem statement" and concludes that all five boxes share one class.

### Placement: the same labels written as the start of the answer (`forcing_place_tests.md`)

The labels are written at the start of the answer, after the reasoning. The table gives the first label written for B. The comparisons are paired, with exact McNemar and Holm per split.

| split | order | in answer | in user turn | n = 0 (no labels) | answer − user turn | answer − n = 0 |
|---|---|---|---|---|---|---|
| Unseen | `AAAAB`, B=A | 44.9 | 41.6 | 29.9 | +3.3 (Holm 0.41) | +15.0 (Holm 3.2e-09) |
| Unseen | `BAAAA`, B=A | 34.1 | 36.2 | 30.5 | −2.1 (0.43) | +3.6 (0.29) |
| Seen | `AAAAB`, B=A | 30.4 | 32.7 | 20.8 | −2.4 (0.52) | +9.5 (0.0016) |
| Seen | `BAAAA`, B=A | 24.4 | 29.8 | 19.6 | −5.4 (0.37) | +4.8 (0.37) |
| Unseen | CF, B=C (`AAAAB` / `BAAAA`) | 64.4 / 53.0 | 0.9 / 1.8 | | | |
| Seen | CF, B=C (`AAAAB` / `BAAAA`) | 58.9 / 44.6 | 1.8 / 1.2 | | | |

The differences keep their size on uncut images, e.g. +15.1 instead of +15.0 for answer − n = 0 on Unseen `AAAAB`.

**The model never re-checks the forced line.** It keeps writing after the label in 0.0–0.3% of items (`forcing_tables.md`, assistant-prefill table). So the first label is also the final one.

**This differs from MiMo-VL-7B-RL.** For that model, true labels in its answer leave B=A at the `default` level. For Qwen-Thinking, they pull as much as labels in the user turn.

### Homogeneous control

Accuracy on box 5 under TF one-shot is 87.8% on Unseen and 95.2% on Seen. The `default` baseline comes with the RQ1 files.

### What the answer does with the given boxes (one-shot, labels in the user turn)

Over answered rows:
- **Rewrites the list.** Qwen-Thinking writes all five labels in 100% of answers and never continues from the given labels (the "B read before objK:" column is 0%).
- **TF one-shot.** It keeps the four given A labels in 87.3 / 84.0% of answers (Unseen `AAAAB` / `BAAAA`) and in 94.5 / 90.9% on Seen.
- **CF.** It keeps C on at least one given box in 1.3–2.5% of answers and relabels all four given boxes A in 70–77%.

### Box swaps

These are rare under the forcing probes. 0–2% of B=A answers write B's class on an A box (`box_swap.md`). The `default` share needs the RQ1 files.

### Hand check of 50 outputs

The sample design is the same as for MiMo-VL-7B-RL: 25 rows per split, `random.Random(0)`, finished one-shot calls. Every row was read by hand, and `forcing_output_check.jsonl` has the verdicts.

- **Labels in the user turn (34 rows).** The model never continues from the given labels.
  - Every answer writes all five labels in box order, so in `BAAAA` its answer starts with B.
  - With fewer than four labels given, it labels the other boxes itself.
  - It changes a given label in 3 of the 26 rows with true labels.
  - In 7 of the 8 CF rows it replaces C with its own classes. In 1 it keeps C on the four given boxes, though not on B.
- **Labels written as its answer (16 rows).** It writes one label after the forced line and stops in all 16. The label is A in 4 of the 8 TF rows and C in 6 of the 8 CF rows.

## Notes for the team

1. **Qwen-Thinking answers like the MiMo models, but is pulled like Qwen-Instruct.** It reasons over the boxes and rewrites the whole list in box order, so in `BAAAA` it writes B first. Even so, given labels raise its B=A in `BAAAA` on both splits (dose slope +1.5 / +2.3 points per label, Holm 6e-4). Its reasoning refers to the given labels far more often when they flip B to A. Answer order alone does not explain its pull.
2. **Its answer line carries inertia; MiMo-VL-7B-RL's does not.**
   - True labels written at the start of its answer pull B to A as much as labels in the user turn: on `AAAAB`, +15.0 (Unseen) and +9.5 (Seen) points over no labels.
   - It never re-checks a forced line.
   - After four forced C labels, B is C in 45–64% of items.
3. **It rejects a wrong class in the user turn.** Under CF, B is labelled C in 0.9–1.8% of items (Qwen-Instruct: 15.5–41.0%), and C survives on a given box in at most 2.5% of answers. As with MiMo, the given boxes are mostly relabelled A.
4. **True labels pull more than wrong ones.** On Unseen `AAAAB`, B=A is 41.6% with four true A labels. With four C labels that the model then relabels A itself, it is 33.8%. This comparison is paired: 38 images are A only under TF and 12 only under CF, exact McNemar p = 3.1e-04, not adjusted. On Seen the gap is smaller and not significant (32.7 against 28.6%, p = 0.23).
5. **Cut calls are 6–13% on Unseen**, all inside the reasoning. They lower B accuracy and B=A alike. The dose and placement effects above hold on the images where neither call was cut. Compare conditions on the uncut images too once `default` is in.
