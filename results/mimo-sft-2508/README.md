# Runs of mimo-sft-2508 (MiMo-VL-7B-SFT-2508)

The RQ1 run of MiMo-VL-7B-SFT-2508 (`mimo-sft-2508`) on all 5,163 ROPE items, with both probes: `default` (all five boxes in one answer) and `single` (one box per call). Decoding is greedy. Split `train` is Seen and `validation` is Unseen. The run uses the team harness on `main` at `52429fe`, unchanged. This folder holds result data only.

This folder has two runs:

- The finished RQ1 run (all sections up to "Notes for the team").
- A smoke run on part of Unseen, made before the full run (last section).

The RQ2 forcing runs of this model are on branch `rq2/forcing-results` (`results/mimo-sft-2508/README_forcing.md` there). That README waits for the `rq1_mimo-sft-2508_*` files in this folder.

## Files of the RQ1 run

| file | contents | rows | size |
|---|---|---|---|
| `rq1_mimo-sft-2508_default_train.jsonl` | default, Seen, subsets `heterogenous` `homogenous` `mixed` | 2,251 | 16.5 MB |
| `rq1_mimo-sft-2508_default_validation.jsonl` | default, Unseen, the same three subsets | 1,908 | 15.3 MB |
| `rq1_mimo-sft-2508_single_train.jsonl` | single, Seen, the same three subsets | 2,251 | 17.7 MB |
| `rq1_mimo-sft-2508_single_validation.jsonl` | single, Unseen, the same three subsets | 1,908 | 14.2 MB |
| `rq1_mimo-sft-2508_adversarial_default_train.jsonl` | default, Seen, `AAAAB` `BAAAA` | 336 | 1.6 MB |
| `rq1_mimo-sft-2508_adversarial_default_validation.jsonl` | default, Unseen, `AAAAB` `BAAAA` | 668 | 3.9 MB |
| `rq1_mimo-sft-2508_adversarial_single_train.jsonl` | single, Seen, `AAAAB` `BAAAA` | 336 | 2.2 MB |
| `rq1_mimo-sft-2508_adversarial_single_validation.jsonl` | single, Unseen, `AAAAB` `BAAAA` | 668 | 5.1 MB |
| `rq1_table1.csv` | Table 1, one line per subset x probe x split | 24 | |
| `rq1_fig1_position.png` | accuracy by box position (Figure 1) | | |
| `rq1_tables.md` | full output of `analysis/rq1_table.py` on these files: Table 1, paired tests, box positions, Seen vs Unseen | | |

The file layout, subset names, row schema and paths are the same as in `results/qwen3vl-8b-instruct/`:

- Subset names follow moh's folder names: `mixed` is In-the-Wild, `homogenous` is Homogeneous and `heterogenous` is Heterogeneous. Adversarial is `AAAAB` plus `BAAAA` (502 images, each in both orders).
- Rows follow the JSONL schema in `harness/README.md`. `raw_output` keeps the full thinking trace.
- `image_path` and `model_path` are relative to `$CSE595_ROOT`. The runner wrote absolute paths; after the run they were rewritten as `$CSE595_ROOT/...`. That is the only change to the rows. The runner wrote one file per probe and split; each was then split into the three main subsets and Adversarial.

The tables, CSV and figure come from:

```bash
source harness/env.sh
python analysis/rq1_table.py --out-dir results/mimo-sft-2508 results/mimo-sft-2508/rq1_*.jsonl \
    > results/mimo-sft-2508/rq1_tables.md
```

The team venv has no matplotlib, and the system `/usr/bin/python3` on the node used had none either, so with the team venv the script stops at the figure, before section (d). The files here come from the same command run with a separate Python 3.11.5 venv that holds numpy 2.2.6 (the team venv's version), matplotlib 3.11.2 and PyYAML 6.0.3. Sections (a) to (c) of `rq1_tables.md` and `rq1_table1.csv` are byte-identical to the output of the team venv.

## How the RQ1 runs were made

All jobs ran on Great Lakes under account `cse595f26_class`, on one NVIDIA A40 each (partition `spgpu`, `max_model_len` 12288, GPU memory utilization 0.85: the setting of `run.sbatch` for cards under 46,000 MiB).

| setting | value |
|---|---|
| harness | `main` at `52429fe` |
| Python | 3.11.5 |
| vLLM | 0.11.0 |
| transformers | 4.57.6 |
| torch | 2.8.0 (+cu128) |
| model revision | `11e8fdc278f5e1e6a72f9561772a6d7cd6921d33` |
| ROPE revision | `b4939b83aae74c650794eb48853cc383c2b666e1` |
| `max_tokens` | 8192 (`configs/models.yaml`) |
| decoding | greedy (temperature 0, seed 0), `--chunk 128`; prefix caching `auto` for default and `off` for single, as in the other RQ1 runs |

Each job ran `harness/scripts/run.sbatch` on all five subsets of one probe and split. That script calls the following, with `--prefix-caching off` added for `single`:

```bash
python -m rope_runner.run --model mimo-sft-2508 --probe <probe> --split <split> --greedy --chunk 128 --out <file> --resume
```

| job | probe | split | start (2026-11-17) | elapsed |
|---|---|---|---|---|
| 66262399 | default | Unseen | 00:28 | 2:02:14 |
| 66262401 | single | Unseen | 02:31 | 2:12:13 |
| 66262403 | default | Seen | 04:43 | 2:02:49 |
| 66262405 | single | Seen | 06:46 | 2:14:49 |

Each file finished within its first job. Each run also had a standby job under the same job name (`--dependency=singleton`) to continue it with `--resume` after the 4-hour limit. Since every run had already finished, those jobs (66262400, 66262402, 66262404, 66262406) found nothing left to do and exited within 12 s. All eight jobs were also held until the smoke job had succeeded (`--dependency=afterok:66261809`).

This command reproduces a run (here single on Seen; for default use `PROBES=default` and `EXTRA="--chunk 128"`, and change `SPLIT` for Unseen). It is submitted from `harness/`:

```bash
source env.sh
sbatch -J rq1-mimo-sft-2508-single-train --dependency=singleton -A "$CSE595_ACCOUNT" \
  -o "$CSE595_LOGS/%x-%j.out" -e "$CSE595_LOGS/%x-%j.err" \
  --export=ALL,MODEL=mimo-sft-2508,SPLIT=train,PROBES=single,EXTRA="--chunk 128 --prefix-caching off",OUT=$CSE595_RUNS/rq1_mimo-sft-2508_single_train.jsonl \
  scripts/run.sbatch
```

## Integrity

Every file has exactly one row per entry of the ROPE JSON for its subset and split. There are no duplicate keys and no broken lines. This was checked on the four runner files and again on the eight files here, which hold the same 10,326 rows.

| split | heterogenous | homogenous | mixed | AAAAB | BAAAA |
|---|---|---|---|---|---|
| Seen | 312 | 400 | 1,539 | 168 | 168 |
| Unseen | 246 | 490 | 1,172 | 334 | 334 |

### Calls that hit the 8,192-token limit

| probe | split | calls | at the limit | median thinking tokens | 90th percentile |
|---|---|---|---|---|---|
| default | Seen | 2,587 | 146 (5.6%) | 176 | 1,034 |
| default | Unseen | 2,576 | 160 (6.2%) | 184 | 1,135 |
| single | Seen | 12,935 | 146 (1.1%) | 54 | 79 |
| single | Unseen | 12,880 | 134 (1.0%) | 54 | 82 |

Heterogeneous has the most cut calls under default (43 of 312 Seen, 30 of 246 Unseen). Table 1 gives the count for each cell.

Every cut call stopped inside the thinking block (no `</think>`), so its answer is empty and already scored wrong. The token-limit rule therefore changes no object in this run. Almost all cut traces end in a loop: in 144 of 146 (default, Seen), 157 of 160 (default, Unseen) and all 280 cut single calls, some sentence of at least 20 characters occurs three or more times in the last 4,000 characters.

## Scoring

Scoring follows the Qwen3-VL-8B-Instruct README:

- **Parsers.** The tolerant parse gives the main number, and strict (moh's official parser) is shown beside it.
- **Token limit.** A call that hits the token limit makes every object it answers wrong. Those objects stay in the denominator.
- **Accuracy and CIs.** Accuracy is correct boxes over scored boxes. CIs are 95% percentile bootstraps over images (2,000 reps).
- **"Cut rows dropped".** This column drops every row with a call at the limit. It is shown as a check on the token-limit rule.

## Table 1: per-object accuracy (%)

| subset | probe | split | n images | n objects | calls at limit | tolerant [95% CI] | strict [95% CI] | tolerant, cut rows dropped |
|---|---|---|---|---|---|---|---|---|
| In-the-Wild | default | Seen | 1,539 | 7,695 | 90 | 61.0 [59.6, 62.4] | 61.0 [59.4, 62.4] | 64.8 |
| In-the-Wild | default | Unseen | 1,172 | 5,860 | 95 | 55.2 [53.4, 56.9] | 55.2 [53.4, 56.9] | 60.1 |
| In-the-Wild | single | Seen | 1,539 | 7,695 | 90 | 68.3 [67.0, 69.5] | 68.2 [67.0, 69.4] | 69.3 |
| In-the-Wild | single | Unseen | 1,172 | 5,860 | 68 | 62.7 [61.3, 64.2] | 62.7 [61.3, 64.2] | 63.7 |
| Homogeneous | default | Seen | 400 | 2,000 | 5 | 85.2 [82.1, 88.2] | 85.2 [82.1, 88.2] | 86.3 |
| Homogeneous | default | Unseen | 490 | 2,450 | 12 | 80.9 [77.8, 84.0] | 80.9 [77.9, 83.8] | 83.0 |
| Homogeneous | single | Seen | 400 | 2,000 | 10 | 85.1 [82.8, 87.5] | 85.1 [82.7, 87.5] | 85.4 |
| Homogeneous | single | Unseen | 490 | 2,450 | 10 | 75.8 [73.1, 78.7] | 75.8 [72.8, 78.7] | 76.4 |
| Heterogeneous | default | Seen | 312 | 1,560 | 43 | 49.4 [46.1, 52.8] | 49.4 [46.1, 52.9] | 57.3 |
| Heterogeneous | default | Unseen | 246 | 1,230 | 30 | 42.1 [38.8, 45.4] | 42.1 [38.8, 45.4] | 48.0 |
| Heterogeneous | single | Seen | 312 | 1,560 | 33 | 59.2 [56.9, 61.7] | 59.2 [56.9, 61.5] | 60.9 |
| Heterogeneous | single | Unseen | 246 | 1,230 | 21 | 49.6 [47.0, 52.0] | 49.6 [47.0, 52.2] | 50.3 |
| Adversarial | default | Seen | 336 | 1,680 | 8 | 70.8 [67.4, 74.0] | 70.7 [67.4, 73.8] | 72.5 |
| Adversarial | default | Unseen | 668 | 3,340 | 23 | 64.4 [61.8, 66.7] | 64.4 [61.9, 66.8] | 66.7 |
| Adversarial | single | Seen | 336 | 1,680 | 13 | 73.8 [70.9, 76.7] | 73.8 [71.0, 76.5] | 74.4 |
| Adversarial | single | Unseen | 668 | 3,340 | 35 | 64.6 [62.3, 66.9] | 64.6 [62.2, 66.8] | 66.3 |

`rq1_tables.md` also has the AAAAB and BAAAA rows separately and the share of boxes each parser fails to read.

## Single vs default on the same images

The comparison is paired by image and box: diff = default - single, in points. The method (exact McNemar on discordant boxes, paired bootstrap over images, Holm over the eight rows) is the same as in the Qwen3-VL-8B-Instruct README. The last column comes without a CI or test.

| subset | split | tolerant single -> default | diff [95% CI] | Holm p | strict diff | tolerant diff, cut rows dropped |
|---|---|---|---|---|---|---|
| In-the-Wild | Seen | 68.3 -> 61.0 | -7.2 [-8.5, -6.0] | 3.6e-43 | -7.2 | -4.5 |
| In-the-Wild | Unseen | 62.7 -> 55.2 | -7.5 [-9.1, -6.1] | 2.5e-31 | -7.6 | -3.4 |
| Homogeneous | Seen | 85.1 -> 85.2 | +0.1 [-2.2, +2.4] | 1 | +0.1 | +0.7 |
| Homogeneous | Unseen | 75.8 -> 80.9 | +5.1 [+2.8, +7.3] | 1.1e-10 | +5.1 | +6.4 |
| Heterogeneous | Seen | 59.2 -> 49.4 | -9.8 [-12.8, -7.0] | 1.5e-15 | -9.7 | -3.0 |
| Heterogeneous | Unseen | 49.6 -> 42.1 | -7.5 [-10.3, -4.4] | 9.3e-09 | -7.5 | -2.8 |
| Adversarial | Seen | 73.8 -> 70.8 | -3.0 [-5.4, -0.7] | 0.0093 | -3.1 | -1.9 |
| Adversarial | Unseen | 64.6 -> 64.4 | -0.2 [-2.2, +1.5] | 1 | -0.2 | +1.0 |

## Seen vs Unseen

Every cell is lower on Unseen, by 4.3 to 9.6 points under the tolerant parse. Seven of the eight rows have Holm p <= 0.0063. The exception is Homogeneous default: -4.3 [-8.5, +0.2], Holm p = 0.055. See section (d) of `rq1_tables.md`.

## Accuracy by box position

Section (c) of `rq1_tables.md` and `rq1_fig1_position.png` give every subset. On Adversarial, the odd box B is the hard one (tolerant, %):

| split | order | B under default | B under single | other four boxes, default | other four boxes, single |
|---|---|---|---|---|---|
| Seen | AAAAB (B = box 5) | 50.0 | 58.3 | 75.6 to 82.7 | 74.4 to 84.5 |
| Seen | BAAAA (B = box 1) | 53.0 | 58.3 | 70.2 to 76.8 | 74.4 to 82.7 |
| Unseen | AAAAB (B = box 5) | 40.7 | 56.0 | 68.6 to 73.4 | 66.2 to 68.6 |
| Unseen | BAAAA (B = box 1) | 43.4 | 54.5 | 65.6 to 71.9 | 65.0 to 68.9 |

## Notes for the team

1. **Strict and tolerant agree for this model.**
   - MiMo-SFT answers in the plain `obj1: ..., obj5: ...` format under default and with a bare class name under single.
   - The two parsers differ by at most 0.1 points in every cell of Table 1.
   - Under default, almost all parse failures are calls cut at the token limit.
   - So unlike MiMo-RL (whose `single` answers are often `\boxed{class}`), strict `single` is not pulled down by a format habit here.
2. **Default loses to single on In-the-Wild and Heterogeneous, and only part of that is the token limit.**
   - Under the tolerant parse, default is 7.2 to 9.8 points below single on these two subsets.
   - When rows with a cut call are dropped, the gap shrinks to 2.8 to 4.5 points but does not close.
   - On Homogeneous Unseen it goes the other way: default is 5.1 points above single (Holm p = 1.1e-10).
   - On Adversarial the two probes are close (-3.0 Seen, -0.2 Unseen).
3. **Fewer cut calls than MiMo-RL.** Default calls hit the 8,192-token limit 5.6 to 6.2% of the time and single calls about 1%; the MiMo-RL README reports 11.2 to 13.5% for default. Almost every cut trace ends in a loop.
4. **The odd box B is harder under both probes, and more so under default** (table above). The drop under default also appears in BAAAA, where B is the first box the model labels. These position numbers are descriptive and not tested here.
5. **No parser audit yet.** There is no `rq1_parser_audit.jsonl` for this model. Since strict and tolerant agree to 0.1 points, the audit matters less here than for MiMo-RL.

## Smoke run (before the full run)

A smoke run is a test on a small sample of items. It checked the setup before the full run. The file name starts with `smoke_`, so `analysis/rq1_table.py` (which reads `rq1_*.jsonl`) does not pick it up. Do not use these numbers for Table 1.

| file | contents | rows | size |
|---|---|---|---|
| `smoke_mimo-sft-2508_validation.jsonl` | `default` and `single`, Unseen, first 100 entries of each subset | 1,000 | 7.9 MB |

Unlike the RQ1 run, the smoke run used the command of `harness/README.md` (section "Smoke test on the GPU") without `EXTRA`: chunk 64 and prefix caching `auto` for both probes. Its `single` rows therefore have variant `greedy,seed=0`, not `greedy,seed=0,pc=off`, and their keys differ from the RQ1 run's. Its paths were rewritten the same way.

| job | PROBES | SUBSETS | LIMIT | EXTRA | elapsed |
|---|---|---|---|---|---|
| 66261809 | default single | all five | 100 | none | 1:16:53 (default 40:12, single 36:25, each with model loading) |

```bash
sbatch -J smoke-mimo-sft-2508 -A "$CSE595_ACCOUNT" -o "$CSE595_LOGS/%x-%j.out" -e "$CSE595_LOGS/%x-%j.err" \
  --export=ALL,MODEL=mimo-sft-2508,SPLIT=validation,LIMIT=100,OUT=$CSE595_RUNS/smoke_mimo-sft-2508_validation.jsonl \
  scripts/run.sbatch
```
