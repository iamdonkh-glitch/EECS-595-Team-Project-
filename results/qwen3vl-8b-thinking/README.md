# Runs of qwen3vl-8b-thinking (Qwen3-VL-8B-Thinking)

Zhongqi Huang's RQ1 run of Qwen3-VL-8B-Thinking (`qwen3vl-8b-thinking`) on all 5,163 ROPE items, with both probes: `default` (all five boxes in one answer) and `single` (one box per call). Decoding is greedy. Split `train` is Seen and `validation` is Unseen. The code is the team harness on `main` at `52429fe`, unchanged. Every number below comes from the files in this folder.

**Hardware differs from the other RQ1 runs.** These jobs ran on NVIDIA H100 80GB GPUs on the ARC Lighthouse cluster (a research-group partition), not on Great Lakes A40s under the class account. Model, revision, prompts, greedy decoding, `max_tokens` and scoring are the same as in the other runs. Greedy decoding on different GPUs is not guaranteed to give identical text, so compare this model with the others knowing that the GPU differs. The RQ2 budget-sweep runs of this model will use the same GPU type, so they compare cleanly with this folder.

## Files

| file | contents | rows | size |
|---|---|---|---|
| `rq1_qwen3vl-8b-thinking_default_train.jsonl` | default, Seen, subsets `heterogenous` `homogenous` `mixed` | 2,251 | 29.9 MB |
| `rq1_qwen3vl-8b-thinking_default_validation.jsonl` | default, Unseen, the same three subsets | 1,908 | 30.2 MB |
| `rq1_qwen3vl-8b-thinking_single_train.jsonl` | single, Seen, the same three subsets | 2,251 | 23.4 MB |
| `rq1_qwen3vl-8b-thinking_single_validation.jsonl` | single, Unseen, the same three subsets | 1,908 | 20.0 MB |
| `rq1_qwen3vl-8b-thinking_adversarial_default_train.jsonl` | default, Seen, `AAAAB` `BAAAA` | 336 | 3.1 MB |
| `rq1_qwen3vl-8b-thinking_adversarial_default_validation.jsonl` | default, Unseen, `AAAAB` `BAAAA` | 668 | 8.4 MB |
| `rq1_qwen3vl-8b-thinking_adversarial_single_train.jsonl` | single, Seen, `AAAAB` `BAAAA` | 336 | 2.8 MB |
| `rq1_qwen3vl-8b-thinking_adversarial_single_validation.jsonl` | single, Unseen, `AAAAB` `BAAAA` | 668 | 6.5 MB |
| `rq1_table1.csv` | Table 1, one line per subset x probe x split | 24 | |
| `rq1_fig1_position.png` | accuracy by box position (Figure 1) | | |
| `rq1_tables.md` | full output of `analysis/rq1_table.py` on these files: Table 1, paired tests, box positions, Seen vs Unseen | | |

The file layout, subset names and row schema are the same as in `results/mimo-rl-2508/` and `results/qwen3vl-8b-instruct/`:

- Subset names follow moh's folder names: `mixed` is In-the-Wild, `homogenous` is Homogeneous and `heterogenous` is Heterogeneous. Adversarial is `AAAAB` plus `BAAAA` (502 images, each in both orders).
- Rows follow the JSONL schema in `harness/README.md`. `raw_output` and `trace_text` keep the full thinking trace.
- `image_path` and `model_path` are relative to `$CSE595_ROOT`. The runner wrote absolute paths; after the run they were rewritten as `$CSE595_ROOT/...`. That is the only change to the rows. Each job wrote one file per probe and split, which was then split into the three main subsets and Adversarial.

The tables, CSV and figure come from:

```bash
source harness/env.sh
python analysis/rq1_table.py --out-dir results/qwen3vl-8b-thinking results/qwen3vl-8b-thinking/rq1_*.jsonl > results/qwen3vl-8b-thinking/rq1_tables.md
```

The figure needs matplotlib, which the team venv lacks; on Lighthouse `/usr/bin/python3` has none either. The script was therefore run with a separate venv holding numpy 2.2.6 (the team venv's version) and matplotlib 3.11.2. Run with the team venv, the script gives the same tables and CSV byte for byte (it fails only at the figure).

## How the runs were made

| setting | value |
|---|---|
| GPU | NVIDIA H100 80GB HBM3, one per job (Lighthouse) |
| vLLM / transformers / torch | 0.11.0 / 4.57.6 / 2.8.0 (Python 3.11.5, `harness/requirements.txt`) |
| model revision | `92f3c4b4feadd3a016ef468d103bb5f58b2a2c6b` |
| ROPE revision | `b4939b83aae74c650794eb48853cc383c2b666e1` |
| `max_tokens` | 8,192 (`configs/models.yaml`; the model card allows 40,960) |
| `max_model_len`, GPU memory utilization | 32,768 and 0.90 (`run.sbatch`'s setting for cards of 80 GB or more; A40 runs use 12,288). Prompts are 277–594 tokens, so a call needs at most 8,786 and the setting does not change any call. |
| decoding | greedy, `--chunk 128`; prefix caching `auto` for default and `off` for single, as in the other RQ1 runs |

Each job ran `harness/scripts/run.sbatch` on all five subsets of one probe and split:

```bash
sbatch -J rq1-qwen3vl-8b-thinking-<probe>-<split> -p <H100 partition> -A <account> --gres=gpu:h100:1 \
    -c 4 --mem=48G -t 08:00:00 -o "$CSE595_LOGS/%x-%j.out" -e "$CSE595_LOGS/%x-%j.err" \
    --export=ALL,MODEL=qwen3vl-8b-thinking,SPLIT=<split>,PROBES=<probe>,EXTRA="--chunk 128 --prefix-caching <auto|off>",OUT=$CSE595_RUNS/rq1_qwen3vl-8b-thinking_<probe>_<split>.jsonl \
    harness/scripts/run.sbatch
```

which calls

```bash
python -m rope_runner.run --model qwen3vl-8b-thinking --probe <probe> --split <split> --greedy --chunk 128 --prefix-caching <auto|off> --out <file> --resume
```

| job | probe | split | start (2026-11-15) | elapsed |
|---|---|---|---|---|
| 28173228 | default | Unseen | 14:19 | 0:43:01 |
| 28173229 | default | Seen | 14:19 | 0:40:36 |
| 28173230 | single | Unseen | 14:19 | 0:36:26 |
| 28173231 | single | Seen | 14:56 | 0:31:56 |

Each file finished within its first job (about 3 minutes of each is model loading).

## Integrity

Every file has exactly one row per entry of the ROPE JSON for its subset and split (Seen: 312 / 400 / 1,539 for heterogenous / homogenous / mixed, 168 + 168 Adversarial; Unseen: 246 / 490 / 1,172, 334 + 334). There are no duplicate keys among the 10,326 rows and no broken lines.

**Calls at the token limit.** Every call that reached 8,192 tokens is still inside its reasoning: `</think>` never came and the answer is empty. Following the team rule, every object such a call answers is scored wrong and stays in the denominator (Table 1, "cut calls"), and a cut call is never counted as B = A.

| probe | Seen | Unseen |
|---|---|---|
| default (1 call per image) | 313 of 2,587 calls (12.1%) | 359 of 2,576 (13.9%) |
| single (5 calls per image) | 178 of 12,935 (1.4%) | 173 of 12,880 (1.3%) |

Strict (moh) and tolerant parsing give the same accuracy on every row of Table 1: the model reasons and then writes the plain `obj1: …, obj5: …` list, or a bare class name under `single`. Nearly all parse failures are the empty answers of cut calls.

## Table 1: per-object accuracy (%)

Tolerant parse is the main number and strict is shown beside it. Accuracy is correct boxes over scored boxes, with cut calls scored wrong. CIs are 95% percentile bootstraps over images. "tol, trunc dropped" leaves out the images with a cut call.

| subset | probe | split | n images | n objects | cut calls / rows | tolerant [95% CI] | strict [95% CI] | tol, trunc dropped |
|---|---|---|---|---|---|---|---|---|
| In-the-Wild | default | Seen | 1,539 | 7,695 | 206 / 206 | 62.6 [61.0, 64.2] | 62.6 [61.0, 64.4] | 72.3 |
| In-the-Wild | default | Unseen | 1,172 | 5,860 | 209 / 209 | 53.3 [51.3, 55.2] | 53.3 [51.3, 55.2] | 64.9 |
| In-the-Wild | single | Seen | 1,539 | 7,695 | 105 / 96 | 70.6 [69.3, 71.7] | 70.6 [69.4, 71.7] | 71.8 |
| In-the-Wild | single | Unseen | 1,172 | 5,860 | 92 / 86 | 65.1 [63.7, 66.5] | 65.1 [63.7, 66.5] | 66.1 |
| Homogeneous | default | Seen | 400 | 2,000 | 9 / 9 | 89.9 [87.0, 92.5] | 89.9 [87.1, 92.4] | 92.0 |
| Homogeneous | default | Unseen | 490 | 2,450 | 30 / 30 | 79.4 [76.0, 82.8] | 79.4 [75.9, 82.8] | 84.6 |
| Homogeneous | single | Seen | 400 | 2,000 | 11 / 10 | 88.2 [85.9, 90.5] | 88.2 [85.7, 90.5] | 88.9 |
| Homogeneous | single | Unseen | 490 | 2,450 | 21 / 19 | 80.4 [77.6, 83.4] | 80.4 [77.5, 83.2] | 82.0 |
| Heterogeneous | default | Seen | 312 | 1,560 | 75 / 75 | 51.3 [47.6, 55.1] | 51.3 [47.4, 55.3] | 67.6 |
| Heterogeneous | default | Unseen | 246 | 1,230 | 50 / 50 | 42.9 [39.3, 46.6] | 42.9 [39.2, 46.9] | 53.9 |
| Heterogeneous | single | Seen | 312 | 1,560 | 49 / 44 | 65.1 [62.9, 67.4] | 65.1 [62.8, 67.3] | 66.8 |
| Heterogeneous | single | Unseen | 246 | 1,230 | 22 / 21 | 53.7 [50.8, 56.3] | 53.7 [50.9, 56.4] | 55.3 |
| Adversarial | default | Seen | 336 | 1,680 | 23 / 23 | 70.7 [66.8, 74.5] | 70.7 [67.0, 74.3] | 75.9 |
| Adversarial | default | Unseen | 668 | 3,340 | 70 / 70 | 64.6 [61.7, 67.4] | 64.6 [61.7, 67.2] | 72.2 |
| Adversarial | single | Seen | 336 | 1,680 | 13 / 12 | 73.7 [70.5, 76.7] | 73.7 [70.6, 76.7] | 74.1 |
| Adversarial | single | Unseen | 668 | 3,340 | 38 / 34 | 68.9 [66.5, 71.3] | 68.9 [66.5, 71.3] | 70.8 |

`rq1_tables.md` also splits Adversarial into `AAAAB` and `BAAAA`, and holds the paired single-vs-default tests, accuracy by box position and the Seen vs Unseen gaps.

## Notes for the report

1. **Most of the default–single gap is the token limit.** With cut calls scored wrong, default is 3.0–13.7 points below single on In-the-Wild, Heterogeneous and Adversarial (paired McNemar, Holm p < 0.005; `rq1_tables.md` section b). On the images where no call was cut, the difference is −1.4 to +2.8 points on every subset. Default cuts 12–14% of its calls at 8,192 tokens, single about 1.4%. The 8,192 cap is the team setting; the model card allows 40,960. A rerun of the cut calls with a larger limit is planned under RQ2 (budget sweep, finer direction 2) and will be reported beside these numbers, not in place of them.
2. **The odd object B is harder even alone, and default adds a little inertia.** B accuracy (tolerant, cut calls wrong) and the share of B answered with the A class:

| order | split | n | single: B acc / B = A | default: B acc / B = A |
|---|---|---|---|---|
| `AAAAB` (B = box 5) | Seen | 168 | 56.5% / 17.9% | 50.0% / 25.6% |
| `AAAAB` | Unseen | 334 | 50.3% / 26.6% | 41.3% / 32.0% |
| `BAAAA` (B = box 1) | Seen | 168 | 56.0% / 19.6% | 54.2% / 22.0% |
| `BAAAA` | Unseen | 334 | 50.3% / 27.8% | 41.6% / 33.2% |

The A boxes of the same images score about 68–79% under default (`rq1_tables.md`, section c). Part of the B = A rate is already there with one box per call; default adds 2.4–7.7 points. These counts are descriptive; the paired decomposition (B alone, B first, B last, with A controls) is part of the RQ1 analysis.

## Not done yet

- A hand check of parsed rows (as in `results/mimo-rl-2508/rq1_parser_audit.jsonl`). Strict and tolerant agree everywhere here, so its main use would be to confirm the empty answers of cut calls.
- The rerun of cut calls with a larger token limit (Note 1).
