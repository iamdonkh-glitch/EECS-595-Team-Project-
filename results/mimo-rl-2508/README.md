# Runs of mimo-rl-2508 (MiMo-VL-7B-RL-2508)

Xingjian Liu's runs of MiMo-VL-7B-RL-2508 (`mimo-rl-2508`). This folder holds result data only. The code is the team harness on `main` at `52429fe`.

This folder has two runs:

- The finished RQ1 run on all 5,163 ROPE items, with both probes: `default` (all five boxes in one answer) and `single` (one box per call). Decoding is greedy. Split `train` is Seen and `validation` is Unseen.
- A smoke run on part of Unseen, made before the full run (last section).

The forcing-probe runs will be added here when they finish.

## Files of the RQ1 run

| file | contents | rows | size |
|---|---|---|---|
| `rq1_mimo-rl-2508_default_train.jsonl` | default, Seen, subsets `heterogenous` `homogenous` `mixed` | 2,251 | 34.2 MB |
| `rq1_mimo-rl-2508_default_validation.jsonl` | default, Unseen, the same three subsets | 1,908 | 35.1 MB |
| `rq1_mimo-rl-2508_single_train.jsonl` | single, Seen, the same three subsets | 2,251 | 19.0 MB |
| `rq1_mimo-rl-2508_single_validation.jsonl` | single, Unseen, the same three subsets | 1,908 | 18.2 MB |
| `rq1_mimo-rl-2508_adversarial_default_train.jsonl` | default, Seen, `AAAAB` `BAAAA` | 336 | 3.6 MB |
| `rq1_mimo-rl-2508_adversarial_default_validation.jsonl` | default, Unseen, `AAAAB` `BAAAA` | 668 | 9.5 MB |
| `rq1_mimo-rl-2508_adversarial_single_train.jsonl` | single, Seen, `AAAAB` `BAAAA` | 336 | 2.4 MB |
| `rq1_mimo-rl-2508_adversarial_single_validation.jsonl` | single, Unseen, `AAAAB` `BAAAA` | 668 | 6.3 MB |
| `rq1_table1.csv` | Table 1, one line per subset x probe x split | 24 | |
| `rq1_fig1_position.png` | accuracy by box position (Figure 1) | | |
| `rq1_parser_audit.jsonl` | hand check of 100 rows: key, verdict, note | 100 | |
| `rq1_tables.md` | full output of `analysis/rq1_table.py` on these files: Table 1, paired tests, box positions, Seen vs Unseen | | |

The file layout, subset names, row schema and paths are the same as in `results/qwen3vl-8b-instruct/`:

- Subset names follow moh's folder names: `mixed` is In-the-Wild, `homogenous` is Homogeneous and `heterogenous` is Heterogeneous. Adversarial is `AAAAB` plus `BAAAA` (502 images, each in both orders).
- Rows follow the JSONL schema in `harness/README.md`. `raw_output` keeps the full thinking trace.
- `image_path` and `model_path` are relative to `$CSE595_ROOT`.

The tables, CSV and figure come from:

```bash
source harness/env.sh
python analysis/rq1_table.py --out-dir results/mimo-rl-2508 results/mimo-rl-2508/rq1_*.jsonl
```

## How the RQ1 runs were made

All jobs ran on Great Lakes under account `cse595f26_class`, on one A40 each (partition `spgpu`, `max_model_len` 12288, GPU memory utilization 0.85).

| setting | value |
|---|---|
| vLLM | 0.11.0 |
| transformers | 4.57.6 |
| torch | 2.8.0 |
| model revision | `ec4ebdc29b83b94aa7f62670c78376250dad8dbc` |
| `max_tokens` | 8192 (`configs/models.yaml`) |

Each job ran `harness/scripts/run.sbatch` on all five subsets of one split. That script calls the following, with `--prefix-caching off` added for `single`:

```bash
python -m rope_runner.run --model mimo-rl-2508 --probe <probe> --split <split> --greedy --chunk 128 --out <file> --resume
```

The runner wrote one file per probe and split. The eight files here are those four files split into the three main subsets and Adversarial.

| job | probe | split | elapsed |
|---|---|---|---|
| 65890397 | default | Unseen | 3:25:43 |
| 65890399 | single | Unseen | 2:20:05 |
| 65890403 | default | Seen | 2:58:24 |
| 65890405 | single | Seen | 2:15:29 |

Each file finished within its first job. The class account stops every job after 4 hours, so each run also had standby jobs queued to continue it with `--resume`. Since every run had already finished, those jobs (65890398, 65890400–65890402, 65890404, 65890406–65890408) found nothing left to do and exited within 12 s.

This command reproduces a run (here single on Seen; change `SPLIT`, `PROBES` and the flags for the others):

```bash
sbatch -A "$CSE595_ACCOUNT" -o "$CSE595_LOGS/%x-%j.out" -e "$CSE595_LOGS/%x-%j.err" \
  --export=ALL,MODEL=mimo-rl-2508,SPLIT=train,PROBES=single,EXTRA="--chunk 128 --prefix-caching off",OUT=$CSE595_RUNS/rq1_mimo-rl-2508_single_train.jsonl \
  harness/scripts/run.sbatch
```

## Integrity

Every file has exactly one row per entry of the ROPE JSON for its subset and split. There are no duplicate keys and no broken lines.

| split | heterogenous | homogenous | mixed | AAAAB | BAAAA |
|---|---|---|---|---|---|
| Seen | 312 | 400 | 1,539 | 168 | 168 |
| Unseen | 246 | 490 | 1,172 | 334 | 334 |

### Calls that hit the 8,192-token limit

| probe | split | calls | at the limit | median thinking tokens | 90th percentile |
|---|---|---|---|---|---|
| default | Seen | 2,587 | 291 (11.2%) | 660 | 8,192 |
| default | Unseen | 2,576 | 347 (13.5%) | 949 | 8,192 |
| single | Seen | 12,935 | 129 (1.0%) | 50 | 152 |
| single | Unseen | 12,880 | 158 (1.2%) | 55 | 232 |

Most cut `default` traces end in a loop. In 248 of 291 (Seen) and 250 of 347 (Unseen), the same sentences repeat over and over in the last 4,000 characters. The rest keep going back and forth ("Wait, no, ...") until they hit the limit.

## Scoring

Scoring follows the Qwen3-VL-8B-Instruct README:

- **Parsers.** The tolerant parse gives the main number, and strict (moh's official parser) is shown beside it.
- **Token limit.** A call that hits the token limit makes every object it answers wrong. Those objects stay in the denominator.
- **Accuracy and CIs.** Accuracy is correct boxes over scored boxes. CIs are 95% percentile bootstraps over images (2,000 reps).
- **"Cut rows dropped".** This column drops every row with a call at the limit. It is shown as a check on the token-limit rule.

## Table 1: per-object accuracy (%)

| subset | probe | split | n images | n objects | calls at limit | tolerant [95% CI] | strict [95% CI] | tolerant, cut rows dropped |
|---|---|---|---|---|---|---|---|---|
| In-the-Wild | default | Seen | 1,539 | 7,695 | 195 | 60.6 [59.0, 62.3] | 55.7 [53.9, 57.4] | 69.4 |
| In-the-Wild | default | Unseen | 1,172 | 5,860 | 211 | 53.3 [51.5, 55.3] | 46.3 [44.2, 48.4] | 65.1 |
| In-the-Wild | single | Seen | 1,539 | 7,695 | 79 | 69.8 [68.6, 71.0] | 52.9 [51.5, 54.3] | 70.7 |
| In-the-Wild | single | Unseen | 1,172 | 5,860 | 80 | 64.9 [63.5, 66.3] | 47.0 [45.5, 48.7] | 65.7 |
| Homogeneous | default | Seen | 400 | 2,000 | 7 | 87.0 [84.0, 90.0] | 85.2 [81.6, 88.3] | 88.5 |
| Homogeneous | default | Unseen | 490 | 2,450 | 22 | 79.8 [76.6, 82.8] | 78.0 [74.6, 81.3] | 83.5 |
| Homogeneous | single | Seen | 400 | 2,000 | 5 | 88.2 [85.8, 90.5] | 73.7 [70.5, 76.8] | 88.4 |
| Homogeneous | single | Unseen | 490 | 2,450 | 16 | 79.7 [77.0, 82.5] | 64.4 [61.3, 67.5] | 81.6 |
| Heterogeneous | default | Seen | 312 | 1,560 | 68 | 48.1 [44.5, 51.8] | 45.4 [41.6, 49.5] | 61.6 |
| Heterogeneous | default | Unseen | 246 | 1,230 | 57 | 41.5 [37.7, 45.3] | 35.4 [31.4, 39.4] | 54.0 |
| Heterogeneous | single | Seen | 312 | 1,560 | 33 | 61.8 [59.5, 64.2] | 41.7 [39.2, 44.4] | 63.3 |
| Heterogeneous | single | Unseen | 246 | 1,230 | 23 | 53.0 [50.5, 55.4] | 32.8 [30.2, 35.5] | 53.8 |
| Adversarial | default | Seen | 336 | 1,680 | 21 | 70.2 [66.4, 73.9] | 67.9 [64.2, 71.8] | 74.9 |
| Adversarial | default | Unseen | 668 | 3,340 | 57 | 65.1 [62.3, 67.8] | 60.6 [57.8, 63.4] | 71.2 |
| Adversarial | single | Seen | 336 | 1,680 | 12 | 77.5 [74.6, 80.3] | 63.9 [60.7, 67.0] | 78.2 |
| Adversarial | single | Unseen | 668 | 3,340 | 39 | 68.1 [65.9, 70.2] | 52.2 [49.8, 54.6] | 70.2 |

`rq1_tables.md` also has the AAAAB and BAAAA rows separately.

## Single vs default on the same images

The comparison is paired by image and box: diff = default − single, in points. The method (McNemar and the paired bootstrap) is the same as in the Qwen3-VL-8B-Instruct README. The last column comes without a CI or test.

| subset | split | tolerant single -> default | diff [95% CI] | Holm p | strict diff | tolerant diff, cut rows dropped |
|---|---|---|---|---|---|---|
| In-the-Wild | Seen | 69.8 -> 60.6 | -9.1 [-10.5, -7.8] | 8.0e-76 | +2.8 | -2.3 |
| In-the-Wild | Unseen | 64.9 -> 53.3 | -11.6 [-13.2, -9.9] | 1.9e-76 | -0.7 | -1.9 |
| Homogeneous | Seen | 88.2 -> 87.0 | -1.2 [-3.2, +0.6] | 0.127 | +11.4 | +0.1 |
| Homogeneous | Unseen | 79.7 -> 79.8 | +0.1 [-1.8, +2.0] | 0.951 | +13.6 | +2.2 |
| Heterogeneous | Seen | 61.8 -> 48.1 | -13.7 [-17.0, -10.4] | 3.1e-29 | +3.7 | -2.1 |
| Heterogeneous | Unseen | 53.0 -> 41.5 | -11.5 [-14.6, -8.4] | 2.6e-18 | +2.5 | -0.9 |
| Adversarial | Seen | 77.5 -> 70.2 | -7.3 [-9.9, -4.5] | 8.1e-14 | +3.9 | -3.5 |
| Adversarial | Unseen | 68.1 -> 65.1 | -2.9 [-4.9, -1.0] | 2.0e-04 | +8.4 | +2.0 |

## Seen vs Unseen

Every cell is lower on Unseen, by 4.8 to 9.4 points under the tolerant parse (Holm p ≤ 0.03 for all eight rows; see section (d) of `rq1_tables.md`).

## Parser audit

We drew 100 rows of the eight RQ1 files and read every answer. The draw used seed 0 and took 5 rows from each probe x split x subset cell, so it covers 500 objects. `rq1_parser_audit.jsonl` has the verdict for each row.

| check | rows | Wilson 95% |
|---|---|---|
| tolerant label differs from what the answer says | 0 / 100 (0 / 500 objects) | 0.0 to 3.7% (objects: 0.0 to 0.8%) |
| the answer names a class outside the candidate list | 0 / 100 | 0.0 to 3.7% |
| default: strict fails only because of the answer's format | 6 / 50 | 5.6 to 23.8% |
| single: strict fails only because of the answer's format (calls answered `\boxed{class}`) | 33 / 50 (78 / 250 calls) | 52.2 to 77.6% (calls: 25.8 to 37.2%) |
| default: the call hit the token limit (no answer) | 5 / 50 | |

The six default format failures have two causes:

- **`\boxed{...}` wrapper (4 rows).** The answer is wrapped in `\boxed{obj1: ..., obj5: ...}`. Strict keeps the closing brace on box 5 (`person}`), so only that box is lost.
- **Explanation before the answer (2 rows).** The answer is a markdown explanation that ends in a boxed list. Strict reads nothing there.

## Notes for the team

1. **Under tolerant scoring, default loses to single mostly through the token limit.**
   - Default calls hit the 8,192-token limit 11–14% of the time; single calls about 1%.
   - Under the tolerant parse, default is 9–14 points below single on In-the-Wild and Heterogeneous.
   - When rows with a cut call are dropped, that gap shrinks to about 1–2 points.
   - So for MiMo-RL, most of default's loss is thinking that runs away on the five-box prompt, not wrong labels. The RQ1 write-up should show both columns.
2. **Strict on `single` mostly measures a format habit.**
   - In `single`, MiMo-RL often answers `\boxed{class}`. The strict parser reads that as an off-list label.
   - This happens on 3,528 of 12,935 Seen and 4,082 of 12,880 Unseen single answers.
   - So strict `single` is 14–20 points below tolerant. This is why strict says default beats single (strict diff column) while tolerant says the opposite.
3. **The odd box B is harder under both probes, and more so under default.**
   - On Unseen AAAAB, box 5 (B) gets 42.2% under default and 57.2% under single. Boxes 1–4 get 68–73% under both probes.
   - On Unseen BAAAA, box 1 (B) gets 44.6% under default and 54.2% under single.
   - Seen shows the same pattern with smaller gaps: AAAAB 56.5 vs 63.7, BAAAA 51.8 vs 58.9.
   - The drop under default also appears in BAAAA, where B is the first box the model labels.
   - These position numbers are descriptive and not tested here. The forcing probes (Table 4) pair them.

## Smoke run (before the full run)

A smoke run is a test on a small sample of items. It checked the setup before the full run and showed what MiMo-RL's outputs look like. The file names start with `smoke_`, so `analysis/rq1_table.py` (which reads `rq1_*.jsonl`) does not pick them up. Do not use these numbers for Table 1.

| file | contents | rows | size |
|---|---|---|---|
| `smoke_mimo-rl-2508_validation.jsonl` | `default` and `single`, Unseen, first 100 entries of each subset | 1,000 | 13.5 MB |
| `smoke_forcing_mimo-rl-2508_validation.jsonl` | One-shot `teacher_forcing`, `counterfactual` and incremental `teacher_forcing`, Unseen, first 50 entries of `AAAAB` and of `BAAAA` | 300 | 10.0 MB |

The smoke run used the same setup as the RQ1 run, with `--limit` added.

| job | PROBES | SUBSETS | LIMIT | EXTRA | elapsed |
|---|---|---|---|---|---|
| 65889054 | default | all five | 100 | `--chunk 128` | 36:09 |
| 65889055 | single | all five | 100 | `--chunk 128 --prefix-caching off` | 28:46 |
| 65889056 | teacher_forcing counterfactual | AAAAB BAAAA | 50 | `--chunk 128` | 15:03 |
| 65889057 | teacher_forcing | AAAAB BAAAA | 50 | `--chunk 128 --tf-mode incremental` | 28:39 |

On the forcing probes, MiMo-RL usually re-labels all five boxes (`obj1: ..., obj5: ...`) instead of answering only the box it was asked about. It also often ignores the labels given in the user turn. Under `counterfactual`, the wrong class C lands on box B in only 0–2% of items. The forcing-probe scripts therefore read box B by its key, not by position.
