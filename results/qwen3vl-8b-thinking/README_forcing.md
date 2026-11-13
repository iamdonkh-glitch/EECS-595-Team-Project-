# RQ2 forcing runs of qwen3vl-8b-thinking (Qwen3-VL-8B-Thinking)

Xingjian Liu's RQ2 forcing runs of Qwen3-VL-8B-Thinking on Adversarial ROPE (`AAAAB`, `BAAAA`; Seen = `train`, Unseen = `validation`). The probes, scoring and statistics are the same as for MiMo-VL-7B-RL-2508; `results/mimo-rl-2508/README.md` (section "RQ2 forcing probes" and after) describes them in full.

**This folder has the core probes only, for now** (TF one-shot, TF incremental, CF). The finer runs (dose, placement, Homogeneous, C near / far) are still running on Great Lakes and will be added here with their tables and the 50-output hand check.

**The RQ1 baseline of this model is not in yet** (Zhongqi's run). Until its `rq1_qwen3vl-8b-thinking_*` files are in this folder, the tables give the rate under each probe and say nothing about `default` or `single`. Once they arrive, the same command rebuilds every table with those comparisons.

## Files

| file | contents | rows | calls | at the limit | size |
|---|---|---|---|---|---|
| `forcing_qwen3vl-8b-thinking_tf-oneshot_{train,validation}.jsonl` | one-shot teacher forcing: the four true A labels given, then B | 336 / 668 | 336 / 668 | 8 / 42 | 2.1 / 6.2 MB |
| `forcing_qwen3vl-8b-thinking_tf-incremental_{train,validation}.jsonl` | moh's incremental teacher forcing (5 calls per image) | 336 / 668 | 1,680 / 3,340 | 95 / 305 | 13.6 / 36.1 MB |
| `forcing_qwen3vl-8b-thinking_cf_{train,validation}.jsonl` | counterfactual prefix: a wrong class C (seeded) on the four other boxes | 336 / 668 | 336 / 668 | 17 / 54 | 3.0 / 7.7 MB |
| `forcing_tables.md` | full output of `analysis/forcing_table.py` on the forcing files here | | | | |
| `forcing_table4.csv` | Table 4 rates with CIs, one line per split x order x condition (no comparison with `default` yet) | | | | |
| `box_swap.md` | B=A answers that write B's class on an A box (`analysis/box_swap.py`, commit `d9225d5`; see the MiMo-VL-7B-RL README, section "Box swaps inside B=A") | | | | |

**Integrity.** Every condition has exactly one row per ROPE entry in each subset (168 + 168 Seen and 334 + 334 Unseen), with no duplicate keys and no broken lines (`publish_forcing.py`).

**Calls at the token limit.** 6.3% of the Unseen one-shot calls, 8.1% of the CF calls and 9.1% of the incremental calls reach 8,192 tokens (Seen: 2.4%, 5.1%, 5.7%). Every one of them is still inside its reasoning: none closed `</think>`, and the answer is empty. In the incremental runs they are spread over all five calls (25–38 calls per box and order on Unseen). The harness never closed the reasoning by force. As for the other models, a cut call is scored wrong and never A.

## How the runs were made

Great Lakes, account `cse595f26_class`, one NVIDIA A40 per job (`-p spgpu`), vLLM 0.11.0, model revision `92f3c4b4feadd3a016ef468d103bb5f58b2a2c6b`, `max_tokens` 8192 (the model's setting in `harness/configs/models.yaml`; the model card allows 40,960), `max_model_len` 12288, greedy, `--chunk 128`, `--resume`. The core runs use the team harness on `main` at `52429fe`, as the other models' core runs.

| job | run | split | elapsed |
|---|---|---|---|
| 65950450 | TF one-shot + CF | Unseen | 1:20:04 |
| 65950459 | TF incremental | Unseen | 2:33:56 |
| 65950461 | TF one-shot + CF | Seen | 35:51 |
| 65950463 | TF incremental | Seen | 54:53 |

Every piece finished within its first job; the standby jobs 65950452, 65950460, 65950462 and 65950464 found nothing left and exited within 8 s. Smoke test 65950440 (placement, 16 images) ran first. The commands are those of `results/mimo-rl-2508/README.md` with `MODEL=qwen3vl-8b-thinking`.

## Scoring

The tables come from `analysis/forcing_table.py` on branch `rq2/forcing-probes` (commit `aca3073`):

```bash
python analysis/forcing_table.py --out-dir results/qwen3vl-8b-thinking \
  results/qwen3vl-8b-thinking/forcing_*qwen3vl-8b-thinking_*.jsonl > results/qwen3vl-8b-thinking/forcing_tables.md
# once Zhongqi's RQ1 files are here, add: results/qwen3vl-8b-thinking/rq1_qwen3vl-8b-thinking_*.jsonl
```

Like the MiMo models, Qwen-Thinking reasons and then writes the plain `obj1: …, obj5: …` list, so strict and tolerant agree for the one-shot probes (e.g. 41.6% and 41.6% B=A under TF one-shot on Unseen `AAAAB`). They differ only under TF incremental. There the model answers every call with all five labels, which both parsers read, but strict follows moh's rule: after the first call of an image it cannot parse (here, a cut call), every later box of that image counts wrong.

## Results (core probes)

### B under each probe (%, tolerant)

| split | order | TF one-shot: B acc / B=A | TF incremental: B acc / B=A | CF: B acc / B=A / B=C |
|---|---|---|---|---|
| Unseen | AAAAB | 38.9 / 41.6 | 38.3 / 42.2 | 41.9 / 33.8 / 0.9 |
| Unseen | BAAAA | 42.8 / 36.2 | 43.4 / 32.0 (B asked first) | 37.4 / 34.4 / 1.8 |
| Seen | AAAAB | 46.4 / 32.7 | 45.8 / 33.3 | 50.0 / 28.6 / 1.8 |
| Seen | BAAAA | 49.4 / 29.8 | 51.2 / 22.0 (B asked first) | 52.4 / 24.4 / 1.2 |

### What the answer does with the given boxes (one-shot, labels in the user turn)

Over answered rows, Qwen-Thinking writes all five labels in 100% of answers and never continues from the given labels (the "B read before objK:" column is 0%). Under TF one-shot it keeps the four given A labels in 87.3 / 84.0% of answers (Unseen `AAAAB` / `BAAAA`; Seen 94.5 / 90.9%). Under CF it keeps C on at least one given box in 1.3–2.5% of answers and relabels all four given boxes A in 70–77%.

### Box swaps

Rare under the forcing probes: 0–2% of B=A answers write B's class on an A box (`box_swap.md`). The `default` share needs the RQ1 files.

## Notes for the team

1. **Qwen-Thinking answers like the MiMo models, not like Qwen-Instruct.** It reasons over the boxes and rewrites the whole list in box order, so in `BAAAA` it writes B first. Qwen-Instruct, without reasoning, continues from the given labels. Whether this removes the pull in `BAAAA`, as for MiMo-VL-7B-RL, needs the dose runs (n = 0 against n = 4) or the RQ1 `default` run.
2. **It rejects a wrong class.** Under CF, B is labelled C in 0.9–1.8% of items (Qwen-Instruct: 15.5–41.0%), and C survives on a given box in at most 2.5% of answers. As with MiMo, the given boxes are mostly relabelled A.
3. **True labels pull more than wrong ones.** On Unseen `AAAAB`, B=A is 41.6% with four true A labels and 33.8% with four C labels that the model then relabels A itself (paired, 38 images A only under TF and 12 only under CF; exact McNemar p = 3.1e-04, not adjusted). On Seen the gap is smaller and not significant (32.7 against 28.6%, p = 0.23). Neither is tested against `default` yet.
4. **Cut calls are 6–9% on Unseen**, all inside the reasoning. They lower B accuracy and B=A alike, so compare conditions on the uncut images too once `default` is in.
