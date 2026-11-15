# RQ1 tables

Files (8): rq1_qwen3vl-8b-thinking_adversarial_default_train.jsonl, rq1_qwen3vl-8b-thinking_adversarial_default_validation.jsonl, rq1_qwen3vl-8b-thinking_adversarial_single_train.jsonl, rq1_qwen3vl-8b-thinking_adversarial_single_validation.jsonl, rq1_qwen3vl-8b-thinking_default_train.jsonl, rq1_qwen3vl-8b-thinking_default_validation.jsonl, rq1_qwen3vl-8b-thinking_single_train.jsonl, rq1_qwen3vl-8b-thinking_single_validation.jsonl

## (a) Table 1: per-object accuracy (%)

Tolerant parse is primary, strict (moh) beside it. Accuracy = correct boxes / scored boxes; 95% CI = bootstrap over images. Token-limit rule: every object answered by a call that hit max_tokens is wrong (kept in the denominator). Cut calls = calls at max_tokens; cut rows = rows with at least one; 'tol, trunc dropped' drops those rows. Parse fail = share of boxes with no tolerant label / with a strict label that is not a candidate name (single: raw answer is not exactly a candidate).

| model | subset | probe | split | n img | n obj | cut calls / rows | tolerant [95% CI] | strict [95% CI] | tol, trunc dropped | parse fail tol / strict |
|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | In-the-Wild | default | Seen | 1539 | 7695 | 206 / 206 | 62.6 [61.0, 64.2] | 62.6 [61.0, 64.4] | 72.3 | 13.4 / 13.4 |
| qwen3vl-8b-thinking | In-the-Wild | default | Unseen | 1172 | 5860 | 209 / 209 | 53.3 [51.3, 55.2] | 53.3 [51.3, 55.2] | 64.9 | 17.8 / 17.9 |
| qwen3vl-8b-thinking | In-the-Wild | single | Seen | 1539 | 7695 | 105 / 96 | 70.6 [69.3, 71.7] | 70.6 [69.4, 71.7] | 71.8 | 1.4 / 1.4 |
| qwen3vl-8b-thinking | In-the-Wild | single | Unseen | 1172 | 5860 | 92 / 86 | 65.1 [63.7, 66.5] | 65.1 [63.7, 66.5] | 66.1 | 1.6 / 1.6 |
| qwen3vl-8b-thinking | Homogeneous | default | Seen | 400 | 2000 | 9 / 9 | 89.9 [87.0, 92.5] | 89.9 [87.1, 92.4] | 92.0 | 2.2 / 2.2 |
| qwen3vl-8b-thinking | Homogeneous | default | Unseen | 490 | 2450 | 30 / 30 | 79.4 [76.0, 82.8] | 79.4 [75.9, 82.8] | 84.6 | 6.1 / 6.1 |
| qwen3vl-8b-thinking | Homogeneous | single | Seen | 400 | 2000 | 11 / 10 | 88.2 [85.9, 90.5] | 88.2 [85.7, 90.5] | 88.9 | 0.5 / 0.5 |
| qwen3vl-8b-thinking | Homogeneous | single | Unseen | 490 | 2450 | 21 / 19 | 80.4 [77.6, 83.4] | 80.4 [77.5, 83.2] | 82.0 | 0.9 / 0.9 |
| qwen3vl-8b-thinking | Heterogeneous | default | Seen | 312 | 1560 | 75 / 75 | 51.3 [47.6, 55.1] | 51.3 [47.4, 55.3] | 67.6 | 24.0 / 24.2 |
| qwen3vl-8b-thinking | Heterogeneous | default | Unseen | 246 | 1230 | 50 / 50 | 42.9 [39.3, 46.6] | 42.9 [39.2, 46.9] | 53.9 | 20.3 / 20.7 |
| qwen3vl-8b-thinking | Heterogeneous | single | Seen | 312 | 1560 | 49 / 44 | 65.1 [62.9, 67.4] | 65.1 [62.8, 67.3] | 66.8 | 3.1 / 3.1 |
| qwen3vl-8b-thinking | Heterogeneous | single | Unseen | 246 | 1230 | 22 / 21 | 53.7 [50.8, 56.3] | 53.7 [50.9, 56.4] | 55.3 | 1.8 / 2.0 |
| qwen3vl-8b-thinking | Adversarial | default | Seen | 336 | 1680 | 23 / 23 | 70.7 [66.8, 74.5] | 70.7 [67.0, 74.3] | 75.9 | 6.8 / 6.9 |
| qwen3vl-8b-thinking | Adversarial | default | Unseen | 668 | 3340 | 70 / 70 | 64.6 [61.7, 67.4] | 64.6 [61.7, 67.2] | 72.2 | 10.5 / 10.5 |
| qwen3vl-8b-thinking | Adversarial | single | Seen | 336 | 1680 | 13 / 12 | 73.7 [70.5, 76.7] | 73.7 [70.6, 76.7] | 74.1 | 0.8 / 0.8 |
| qwen3vl-8b-thinking | Adversarial | single | Unseen | 668 | 3340 | 38 / 34 | 68.9 [66.5, 71.3] | 68.9 [66.5, 71.3] | 70.8 | 1.1 / 1.1 |
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Seen | 168 | 840 | 10 / 10 | 72.0 [67.0, 77.3] | 72.0 [67.1, 76.9] | 76.6 | 6.0 / 6.1 |
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Unseen | 334 | 1670 | 38 / 38 | 63.6 [59.6, 67.5] | 63.6 [59.5, 67.5] | 71.8 | 11.4 / 11.4 |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Seen | 168 | 840 | 5 / 4 | 73.5 [68.7, 77.6] | 73.5 [68.9, 77.5] | 73.9 | 0.6 / 0.7 |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Unseen | 334 | 1670 | 17 / 15 | 69.0 [65.6, 72.5] | 69.0 [65.4, 72.3] | 70.6 | 1.0 / 1.0 |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Seen | 168 | 840 | 13 / 13 | 69.4 [64.2, 74.4] | 69.4 [63.9, 74.6] | 75.2 | 7.7 / 7.7 |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Unseen | 334 | 1670 | 32 / 32 | 65.6 [61.8, 69.6] | 65.6 [61.7, 69.5] | 72.6 | 9.6 / 9.6 |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Seen | 168 | 840 | 8 / 8 | 73.9 [69.6, 77.7] | 73.9 [69.8, 77.9] | 74.4 | 1.0 / 1.0 |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Unseen | 334 | 1670 | 21 / 19 | 68.7 [65.1, 72.0] | 68.7 [65.5, 72.0] | 70.9 | 1.3 / 1.3 |

## (b) Paired tests on the same images

### single (x) vs default (y), each model

Paired unit: the box (image x box position) on the same image, images matched on (split, subset, entry_idx, image_id). McNemar = exact two-sided test on discordant boxes (b = right only under x, c = right only under y; it treats the 5 boxes of an image as independent). CI = paired bootstrap over images of the per-image accuracy difference. diff = y - x in points. Holm family = all rows of this table, separately per parser.

| comparison | subset | probe | split | n img | tolerant x -> y | diff [95% CI] | b / c | p | Holm p | strict diff [95% CI] | strict p (Holm) | tol diff, trunc dropped (n img) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking: single -> default | In-the-Wild | - | Seen | 1539 | 70.6 -> 62.6 | -7.9 [-9.3, -6.6] | 990 / 380 | 6.2e-63 | 4.3e-62 | -7.9 [-9.3, -6.6] | 6.2e-63 (4.3e-62) | -0.5 (1290) |
| qwen3vl-8b-thinking: single -> default | In-the-Wild | - | Unseen | 1172 | 65.1 -> 53.3 | -11.8 [-13.5, -10.3] | 970 / 277 | 2.0e-90 | 1.6e-89 | -11.8 [-13.6, -10.1] | 1.3e-90 (1.0e-89) | -1.4 (925) |
| qwen3vl-8b-thinking: single -> default | Homogeneous | - | Seen | 400 | 88.2 -> 89.9 | +1.6 [-0.4, +3.6] | 61 / 94 | 0.00993 | 0.0199 | +1.6 [-0.3, +3.6] | 0.00993 (0.0199) | +2.8 (384) |
| qwen3vl-8b-thinking: single -> default | Homogeneous | - | Unseen | 490 | 80.4 -> 79.4 | -1.0 [-2.9, +0.8] | 118 / 93 | 0.0983 | 0.0983 | -1.0 [-2.9, +0.8] | 0.0999 (0.0999) | +1.7 (447) |
| qwen3vl-8b-thinking: single -> default | Heterogeneous | - | Seen | 312 | 65.1 -> 51.3 | -13.7 [-17.1, -10.3] | 276 / 62 | 2.3e-33 | 1.4e-32 | -13.7 [-17.2, -10.3] | 2.3e-33 (1.4e-32) | +0.5 (221) |
| qwen3vl-8b-thinking: single -> default | Heterogeneous | - | Unseen | 246 | 53.7 -> 42.9 | -10.7 [-14.1, -7.6] | 186 / 54 | 3.6e-18 | 1.8e-17 | -10.7 [-14.1, -7.5] | 3.6e-18 (1.8e-17) | -0.8 (185) |
| qwen3vl-8b-thinking: single -> default | Adversarial | - | Seen | 336 | 73.7 -> 70.7 | -3.0 [-5.5, -0.5] | 144 / 94 | 0.00144 | 0.00432 | -3.0 [-5.4, -0.5] | 0.00144 (0.00432) | +0.8 (308) |
| qwen3vl-8b-thinking: single -> default | Adversarial | - | Unseen | 668 | 68.9 -> 64.6 | -4.3 [-6.1, -2.5] | 298 / 156 | 2.5e-11 | 1.0e-10 | -4.3 [-6.1, -2.5] | 2.5e-11 (1.0e-10) | +1.2 (584) |

Note: pair mimo-sft-2508 vs mimo-rl-2508 skipped: no file for mimo-sft-2508.

Note: pair qwen3vl-8b-instruct vs qwen3vl-8b-thinking skipped: no file for qwen3vl-8b-instruct.

## (c) Accuracy by box position (%), tolerant (strict)

| model | subset | probe | split | n img | box 1 | box 2 | box 3 | box 4 | box 5 |
|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Seen | 168 | 77.4 (77.4) | 77.4 (77.4) | 76.2 (76.2) | 79.2 (79.2) | 50.0 (50.0) |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Seen | 168 | 54.2 (54.2) | 73.8 (73.8) | 72.6 (72.6) | 72.6 (72.6) | 73.8 (73.8) |
| qwen3vl-8b-thinking | Heterogeneous | default | Seen | 312 | 54.5 (54.5) | 49.0 (49.0) | 49.4 (49.4) | 51.9 (51.9) | 51.9 (51.9) |
| qwen3vl-8b-thinking | Homogeneous | default | Seen | 400 | 90.0 (90.0) | 89.2 (89.2) | 90.0 (90.0) | 90.2 (90.2) | 90.0 (90.0) |
| qwen3vl-8b-thinking | In-the-Wild | default | Seen | 1539 | 61.9 (61.9) | 61.5 (61.5) | 63.2 (63.2) | 64.5 (64.5) | 62.1 (62.1) |
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Unseen | 334 | 67.7 (67.7) | 69.8 (69.8) | 70.4 (70.4) | 68.9 (68.9) | 41.3 (41.3) |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Unseen | 334 | 41.6 (41.6) | 70.4 (70.4) | 72.5 (72.5) | 72.5 (72.5) | 71.3 (71.3) |
| qwen3vl-8b-thinking | Heterogeneous | default | Unseen | 246 | 46.3 (46.3) | 44.3 (44.3) | 39.0 (39.0) | 43.9 (43.9) | 41.1 (41.1) |
| qwen3vl-8b-thinking | Homogeneous | default | Unseen | 490 | 79.8 (79.8) | 78.8 (79.0) | 79.6 (79.6) | 79.4 (79.4) | 79.6 (79.4) |
| qwen3vl-8b-thinking | In-the-Wild | default | Unseen | 1172 | 55.4 (55.4) | 53.3 (53.3) | 50.9 (50.8) | 53.1 (53.1) | 53.8 (53.8) |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Seen | 168 | 79.2 (79.2) | 76.2 (76.2) | 76.2 (76.2) | 79.2 (79.2) | 56.5 (56.5) |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Seen | 168 | 56.0 (56.0) | 78.6 (78.6) | 77.4 (77.4) | 76.8 (76.8) | 81.0 (81.0) |
| qwen3vl-8b-thinking | Heterogeneous | single | Seen | 312 | 67.0 (67.0) | 68.3 (68.3) | 64.1 (64.1) | 62.5 (62.5) | 63.5 (63.5) |
| qwen3vl-8b-thinking | Homogeneous | single | Seen | 400 | 89.0 (89.0) | 87.0 (87.0) | 89.0 (89.0) | 87.8 (87.8) | 88.5 (88.5) |
| qwen3vl-8b-thinking | In-the-Wild | single | Seen | 1539 | 67.4 (67.4) | 69.9 (69.9) | 71.2 (71.2) | 73.6 (73.6) | 70.7 (70.7) |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Unseen | 334 | 72.5 (72.5) | 72.8 (72.8) | 77.2 (77.2) | 72.5 (72.5) | 50.3 (50.3) |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Unseen | 334 | 50.3 (50.3) | 70.7 (70.7) | 75.4 (75.4) | 73.7 (73.7) | 73.4 (73.4) |
| qwen3vl-8b-thinking | Heterogeneous | single | Unseen | 246 | 55.7 (55.7) | 52.8 (52.8) | 51.6 (51.6) | 54.9 (54.9) | 53.3 (53.3) |
| qwen3vl-8b-thinking | Homogeneous | single | Unseen | 490 | 79.8 (79.8) | 79.6 (79.6) | 82.0 (82.0) | 79.4 (79.4) | 81.4 (81.4) |
| qwen3vl-8b-thinking | In-the-Wild | single | Unseen | 1172 | 66.6 (66.6) | 65.6 (65.6) | 61.9 (61.9) | 67.0 (67.0) | 64.5 (64.5) |

## (d) Seen vs Unseen gap (unpaired: different images and candidate lists)

gap = Unseen - Seen, points, per-object accuracy. CI = bootstrap resampling each split's images separately; p = two-sided permutation test on per-image accuracy (10,000 reps). Holm family = the rows of one model.

| model | subset | probe | n Seen / Unseen | tolerant Seen -> Unseen | gap [95% CI] | p | Holm p | strict gap [95% CI] |
|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | In-the-Wild | default | 1539 / 1172 | 62.6 -> 53.3 | -9.3 [-11.9, -6.7] | 1.0e-04 | 8.0e-04 | -9.3 [-11.9, -6.8] |
| qwen3vl-8b-thinking | In-the-Wild | single | 1539 / 1172 | 70.6 -> 65.1 | -5.4 [-7.3, -3.6] | 1.0e-04 | 8.0e-04 | -5.4 [-7.4, -3.7] |
| qwen3vl-8b-thinking | Homogeneous | default | 400 / 490 | 89.9 -> 79.4 | -10.5 [-14.8, -6.2] | 1.0e-04 | 8.0e-04 | -10.5 [-14.8, -6.2] |
| qwen3vl-8b-thinking | Homogeneous | single | 400 / 490 | 88.2 -> 80.4 | -7.8 [-11.5, -4.1] | 3.0e-04 | 0.0012 | -7.8 [-11.7, -4.0] |
| qwen3vl-8b-thinking | Heterogeneous | default | 312 / 246 | 51.3 -> 42.9 | -8.4 [-13.8, -2.7] | 0.0032 | 0.0096 | -8.4 [-13.8, -3.1] |
| qwen3vl-8b-thinking | Heterogeneous | single | 312 / 246 | 65.1 -> 53.7 | -11.4 [-15.1, -7.9] | 1.0e-04 | 8.0e-04 | -11.4 [-15.0, -7.9] |
| qwen3vl-8b-thinking | Adversarial | default | 336 / 668 | 70.7 -> 64.6 | -6.1 [-10.6, -1.7] | 0.0099 | 0.0198 | -6.1 [-10.8, -1.6] |
| qwen3vl-8b-thinking | Adversarial | single | 336 / 668 | 73.7 -> 68.9 | -4.8 [-8.6, -1.0] | 0.0199 | 0.0199 | -4.8 [-8.7, -1.1] |

