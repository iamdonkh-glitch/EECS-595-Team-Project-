# RQ3 Table 3: error taxonomy of the RQ1 runs

Every scored object of the four RQ1 runs (MiMo-VL-7B SFT-2508 and RL-2508, Qwen3-VL-8B Instruct and Thinking; `default` and `single`; all 5,163 ROPE items) gets one category: correct, or one of seven error types. Table 3 gives the share of each category per model x subset x probe x split, for the tolerant parse (primary) and the strict (moh) parse.

This folder holds analysis output only. No model was run for it.

| file | contents |
|---|---|
| `rq3_tables.md` | full output of `analysis/rq3_table3.py`: (a) Table 3, tolerant; (b) Table 3, strict; (c) the odd box B on Adversarial; (d) composition of the errors; (e) checks |
| `rq3_table3.csv` | category counts, one line per model x subset x probe x split x parser (160 lines) |

## Definitions decided for RQ3 (2026-11-18)

The harness stores an error type for every object (`rope_runner/scoring.py`). Three of its rules differ from the task description, so RQ3 re-classifies the stored labels in `analysis/rq3_table3.py`; the harness is unchanged. The fourth point is the salience definition for Figure 3.

1. **Invented vs borrowed.** The harness calls a wrong label "invented" when it is not one of the five target classes. Most of those labels (54 to 65%, depending on model and probe) name an object that ROPE annotates elsewhere in the same image (the entry's `object_set`). RQ3 splits them: **borrowed** (the class of another of the five boxes), **in-image** (annotated in the image, but not one of the five boxes) and **invented** (not annotated in the image). Both earlier definitions can be rebuilt from these three.
2. **B labelled A.** The harness counts "inertia" only on AAAAB (box 5 labelled A); on BAAAA the same error is "borrowed". RQ3 counts **B=A in both orders** and keeps AAAAB and BAAAA as separate rows. Under `default`, B is the first box written in BAAAA, and `single` has no earlier answers at all, so B=A by itself is not proof of self-induced inertia; the contrast between probes and orders is.
3. **Calls cut at the token limit.** Team rule: every object answered by a call with `finish_reason == "length"` is wrong. RQ3 gives these objects their own category, **truncated**, instead of leaving them in "unparsed" or scoring a cut answer that happens to parse. With this rule, `correct` equals Table 1's accuracy.
4. **Salience (Figure 3).** The working definition stays: the box's area rank among the five boxes, plus its distance from the image centre. Both come from ROPE's box coordinates and image size.

## Categories

Each scored object gets exactly one category, checked in this order:

| category | rule |
|---|---|
| truncated | the call that answers the object hit `max_tokens` (wrong even if the cut answer parses) |
| unparsed | no label recovered from an answer that was not cut |
| correct | label = gold |
| B=A | Adversarial only: the odd box B (AAAAB box 5, BAAAA box 1) labelled A, the class of the other four boxes |
| borrowed | label = the class of another of the five target boxes |
| off-list | label not in the split's 50-class candidate list (a formatting failure, not a hallucination) |
| in-image | in the candidate list, not a target class, but in the image's `object_set` |
| invented | in the candidate list and not in the image's `object_set` |

`object_set` lists every class annotated in the image, with ADE's alternative names (for example `person`, `individual`, `someone`) and background classes such as `wall` or `sky`. Matching is on the exact lower-case class name. In-image means the class is annotated somewhere in the image, not that the model looked at that object. Invented can still name an object that is in the image but not annotated; the hand reading of 100 errors (finer direction 4) will estimate how often.

## Inputs and how the tables were made

The RQ1 files of the four models are on four branches. They were read unchanged (8 files per model, 10,326 rows each):

| model | branch | commit |
|---|---|---|
| `mimo-sft-2508` | `rq1/mimo-sft-2508` | `0112cf1` |
| `mimo-rl-2508` | `rq2/forcing-results` | `298832d` |
| `qwen3vl-8b-instruct` | `main` | `52429fe` |
| `qwen3vl-8b-thinking` | `rq1/qwen3vl-8b-thinking` | `6830a80` |

```bash
source harness/env.sh
IN=$HOME/cse595/rq1_inputs
for pair in "mimo-sft-2508 origin/rq1/mimo-sft-2508" "mimo-rl-2508 origin/rq2/forcing-results" \
            "qwen3vl-8b-instruct origin/main" "qwen3vl-8b-thinking origin/rq1/qwen3vl-8b-thinking"; do
  set -- $pair; mkdir -p $IN/$1
  for p in $(git ls-tree --name-only $2 results/$1/ | grep -E "/rq1_$1_.*\.jsonl$"); do
    git show $2:$p > $IN/$1/$(basename $p)
  done
done
python analysis/rq3_table3.py --out-dir results/rq3 $IN/*/rq1_*.jsonl > results/rq3/rq3_tables.md
```

Once the four models' RQ1 files are merged into one branch, `python analysis/rq3_table3.py --out-dir results/rq3 > results/rq3/rq3_tables.md` reads `results/*/rq1_*.jsonl` by itself. The script needs only the team venv (numpy) and `$ROPE_DIR` for `object_set`. `analysis/test_rq3_table3.py` tests every category on hand-made labels (`python -m pytest analysis`).

## Checks

- **Rows.** 41,304 rows (4 models x 10,326), every one matched to its ROPE entry by split, subset, entry index and image id. Every Adversarial image has four non-B boxes of one class.
- **Stored labels.** For both parsers, the harness's own `error_type`, rerun on the stored labels, gives the stored error type for every object.
- **Mapping.** Outside cut calls (197,502 objects per parser), every category maps back to the stored harness type: inertia = B=A on AAAAB; borrowed = borrowed + B=A on BAAAA; invented = in-image + invented. The other 9,018 objects are truncated.
- **Accuracy.** `correct` equals the tolerant and strict accuracy in each model's `rq1_table1.csv` in all 160 cells (5 subsets x 2 probes x 2 splits x 2 parsers x 4 models; largest difference 5e-07, the CSVs' rounding).

## Composition of the errors (tolerant, % of wrong objects, all five subsets pooled)

The items are the same for every model, so rows of one split can be compared across models. B=A exists only on Adversarial (1,680 of 12,935 Seen and 3,340 of 12,880 Unseen objects). Table 3 itself (per subset, as % of all objects) is in `rq3_tables.md`.

| model | probe | split | n wrong / n obj | truncated | unparsed | B=A | borrowed | off-list | in-image | invented |
|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | default | Seen | 4574 / 12935 | 16.0 | 0.0 | 1.7 | 31.9 | 0.7 | 25.1 | 24.5 |
| mimo-sft-2508 | default | Unseen | 4994 / 12880 | 16.0 | 0.0 | 4.6 | 30.1 | 0.3 | 29.7 | 19.3 |
| mimo-sft-2508 | single | Seen | 3816 / 12935 | 3.8 | 0.0 | 1.0 | 32.0 | 1.5 | 31.2 | 30.4 |
| mimo-sft-2508 | single | Unseen | 4577 / 12880 | 2.9 | 0.0 | 2.7 | 30.3 | 0.9 | 37.5 | 25.7 |
| mimo-rl-2508 | default | Seen | 4598 / 12935 | 31.6 | 0.2 | 1.4 | 25.4 | 0.0 | 19.5 | 21.8 |
| mimo-rl-2508 | default | Unseen | 5114 / 12880 | 33.9 | 0.4 | 4.0 | 22.9 | 0.1 | 23.7 | 15.1 |
| mimo-rl-2508 | single | Seen | 3536 / 12935 | 3.6 | 0.0 | 1.4 | 34.9 | 0.1 | 28.4 | 31.7 |
| mimo-rl-2508 | single | Unseen | 4198 / 12880 | 3.8 | 0.0 | 3.4 | 32.2 | 0.1 | 36.4 | 24.2 |
| qwen3vl-8b-instruct | default | Seen | 2834 / 12935 | 0.0 | 0.0 | 2.7 | 40.1 | 3.7 | 30.8 | 22.6 |
| qwen3vl-8b-instruct | default | Unseen | 3553 / 12880 | 0.6 | 0.0 | 5.7 | 37.3 | 2.3 | 37.9 | 16.1 |
| qwen3vl-8b-instruct | single | Seen | 2916 / 12935 | 0.0 | 0.0 | 1.9 | 36.6 | 1.1 | 34.6 | 25.8 |
| qwen3vl-8b-instruct | single | Unseen | 3533 / 12880 | 0.0 | 0.0 | 4.0 | 36.2 | 0.9 | 40.9 | 17.9 |
| qwen3vl-8b-thinking | default | Seen | 4329 / 12935 | 36.2 | 0.0 | 1.8 | 25.3 | 0.2 | 20.9 | 15.7 |
| qwen3vl-8b-thinking | default | Unseen | 5125 / 12880 | 35.0 | 0.0 | 4.3 | 23.9 | 0.1 | 24.9 | 11.8 |
| qwen3vl-8b-thinking | single | Seen | 3488 / 12935 | 5.1 | 0.0 | 1.8 | 34.9 | 0.1 | 34.5 | 23.7 |
| qwen3vl-8b-thinking | single | Unseen | 4133 / 12880 | 4.2 | 0.0 | 4.4 | 35.2 | 0.1 | 39.2 | 17.0 |

## The odd box B: share labelled A (tolerant, % of B boxes)

168 Seen and 334 Unseen images per order. A truncated B box counts as truncated, not as B=A. Section (c) of `rq3_tables.md` adds B accuracy, 95% CIs and the other errors.

| model | AAAAB default | AAAAB single | BAAAA default | BAAAA single |
|---|---|---|---|---|
| mimo-sft-2508, Seen | 26.2 | 11.9 | 21.4 | 11.9 |
| mimo-sft-2508, Unseen | 34.1 | 15.9 | 34.1 | 21.0 |
| mimo-rl-2508, Seen | 20.8 | 12.5 | 17.9 | 16.1 |
| mimo-rl-2508, Unseen | 29.3 | 18.9 | 32.6 | 24.0 |
| qwen3vl-8b-instruct, Seen | 26.8 | 14.9 | 18.5 | 18.5 |
| qwen3vl-8b-instruct, Unseen | 35.9 | 20.1 | 25.1 | 22.8 |
| qwen3vl-8b-thinking, Seen | 25.6 | 17.9 | 22.0 | 19.6 |
| qwen3vl-8b-thinking, Unseen | 32.0 | 26.6 | 33.2 | 27.8 |

## Notes for the team

These are descriptive. No paired test between probes or models has been run on the error types yet.

1. **Under `default`, truncation is the largest error type of both reasoning models.**
   - Truncated objects are 31.6 to 33.9% of MiMo-RL's errors and 35.0 to 36.2% of Qwen-Thinking's, against 16.0% for MiMo-SFT and at most 0.6% for Qwen-Instruct.
   - Under `single` it is 2.9 to 5.1% for the three thinking models.
   - A truncated object has no label, so it is neither a hallucination nor a correct answer. Error-type shares under `default` should be read with this in mind.
2. **Most labels the harness calls "invented" name an object annotated in the image.**
   - In-image exceeds invented in every Unseen row and in six of eight Seen rows; the exceptions are MiMo-RL on Seen.
   - Pooled over splits, in-image is 54 to 65% of in-image + invented.
3. **Borrowed and in-image are the two largest error types that carry a label.**
   - Borrowed is the largest in all eight Seen rows, and in-image in seven of eight Unseen rows (MiMo-SFT `default` is the exception).
   - Borrowed is 22.9 to 40.1% of errors, highest for Qwen-Instruct under `default`; in-image is 19.5 to 40.9%.
4. **B=A is common under both probes.**
   - On Unseen under `default`, 29.3 to 35.9% of B boxes in AAAAB and 25.1 to 34.1% in BAAAA are labelled A.
   - Under `single`, where the model has given no earlier answer, it is still 15.9 to 26.6% (AAAAB) and 21.0 to 27.8% (BAAAA).
   - For three models, B=A under `default` is as high in BAAAA, where B is written first, as in AAAAB. Qwen-Instruct is the exception (25.1 vs 35.9 on Unseen).
   - So a large part of B=A comes from the image itself (four boxes of one class), not from the model's own earlier answers. The self-induced part is the contrast between AAAAB `default` and `single` (and the forcing probes in Table 4).
5. **Strict and tolerant give the same picture for three models.** For MiMo-RL `single`, the strict parse moves 29.5% of all objects to off-list (its `\boxed{class}` habit), which hides 8.4 points of in-image + invented. The tolerant table is the one to read for MiMo-RL.
