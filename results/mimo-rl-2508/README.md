# Runs of mimo-rl-2508 (MiMo-VL-7B-RL-2508)

Xingjian Liu's runs of MiMo-VL-7B-RL-2508 (`mimo-rl-2508`). This folder holds result data only. The code is the team harness on `main`.

So far it holds one smoke run on part of Unseen (`validation`). The full RQ1 run (`rq1_*.jsonl`) and the forcing-probe runs will be added here when they finish.

## Smoke run

A smoke run is a test on a small sample of items. Its purpose was to check the setup before the full run and to show what MiMo-RL's outputs look like. The file names start with `smoke_`, so `analysis/rq1_table.py`, which reads `rq1_*.jsonl`, does not pick them up. Do not use these numbers for Table 1.

| file | contents | rows | size |
|---|---|---|---|
| `smoke_mimo-rl-2508_validation.jsonl` | `default` and `single` probes, Unseen, first 100 entries of each subset (`mixed` `homogenous` `heterogenous` `AAAAB` `BAAAA`) | 1,000 | 13.5 MB |
| `smoke_forcing_mimo-rl-2508_validation.jsonl` | One-shot `teacher_forcing`, `counterfactual` and incremental `teacher_forcing`, Unseen, first 50 entries of `AAAAB` and of `BAAAA` | 300 | 10.0 MB |

The rows follow the JSONL schema in `harness/README.md`. `image_path` and `model_path` are written relative to `$CSE595_ROOT`, as in `results/qwen3vl-8b-instruct/`. `raw_output` keeps the full thinking trace.

### How the runs were made

All four jobs ran on Great Lakes under account `cse595f26_class` on one A40 each (partition `spgpu`, `max_model_len` 12288, GPU memory utilization 0.85). The code was `main` at `52429fe`.

| Component | Value |
|---|---|
| vLLM | 0.11.0 |
| transformers | 4.57.6 |
| torch | 2.8.0 |
| model revision | `ec4ebdc29b83b94aa7f62670c78376250dad8dbc` |
| decoding | greedy (`--greedy`) |
| `max_tokens` | 8192 (`configs/models.yaml`) |

Each job ran `harness/scripts/run.sbatch`, which calls `python -m rope_runner.run --model mimo-rl-2508 --probe <probe> --split validation [--subset ...] --limit <N> --greedy <EXTRA> --out <file> --resume` for each probe.

| job | PROBES | SUBSETS | LIMIT | EXTRA | elapsed |
|---|---|---|---|---|---|
| 65889054 | default | all five | 100 | `--chunk 128` | 36:09 |
| 65889055 | single | all five | 100 | `--chunk 128 --prefix-caching off` | 28:46 |
| 65889056 | teacher_forcing counterfactual | AAAAB BAAAA | 50 | `--chunk 128` | 15:03 |
| 65889057 | teacher_forcing | AAAAB BAAAA | 50 | `--chunk 128 --tf-mode incremental` | 28:39 |

Each file has one row per (probe, subset, entry) and no duplicate keys.

### Calls that hit the 8,192-token limit

A call that hits the limit has `finish_reason` `length` and is scored wrong.

| probe | AAAAB | BAAAA | heterogenous | homogenous | mixed | total |
|---|---|---|---|---|---|---|
| default (1 call per image) | 10 / 100 | 9 / 100 | 20 / 100 | 7 / 100 | 16 / 100 | 62 / 500 (12.4%) |
| single (5 calls per image) | 11 / 500 | 7 / 500 | 13 / 500 | 4 / 500 | 1 / 500 | 36 / 2,500 (1.4%) |
| TF one-shot (1 call) | 3 / 50 | 8 / 50 | | | | 11 / 100 |
| counterfactual (1 call) | 3 / 50 | 4 / 50 | | | | 7 / 100 |
| TF incremental (5 calls) | 24 / 250 | 27 / 250 | | | | 51 / 500 |

The median `default` trace is about 900 thinking tokens. About half of the cut traces loop on "Wait, no, ..." until the limit.

### First look (`python -m rope_runner.analyze`)

These are the per-object accuracy (%) on 100 images per cell, from `rope_runner.analyze`.

| subset | default tolerant | default strict | single tolerant | single strict |
|---|---|---|---|---|
| AAAAB | 52.8 | 47.2 | 56.2 | 41.2 |
| BAAAA | 56.2 | 53.4 | 55.0 | 43.4 |
| heterogenous | 42.4 | 34.4 | 52.4 | 30.6 |
| homogenous | 86.0 | 83.4 | 88.8 | 73.2 |
| mixed | 57.4 | 47.2 | 65.8 | 44.6 |

### Notes for the team

1. **`\boxed{}` breaks strict on `single`.** In `single`, MiMo-RL often wraps its answer as `\boxed{cabinet}`. The strict parser (moh's) then reads the class as `\boxed{cabinet}`, an off-list label. 824 of 2,500 single calls (33%) fail strict this way, while the tolerant parser reads them correctly. So for this model, strict is much lower than tolerant on `single`. Tolerant is the main number, as in the Qwen3-VL-8B-Instruct README.
2. **Markdown before the answer breaks strict on `default`.** On `default`, the gap between strict and tolerant comes mostly from answers that explain in markdown before giving the list.
3. **The forcing probes re-label every box.** On the forcing probes, MiMo-RL usually re-labels all five boxes (`obj1: ..., obj5: ...`) instead of answering only the box it was asked about. It also often ignores the labels given in the user turn. Under `counterfactual`, the wrong class C ends up on box B in 0–2% of items. The forcing-probe scripts read box B by its key, not by position.
