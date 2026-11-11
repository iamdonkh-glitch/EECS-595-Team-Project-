# RQ1 tables

Files (8): rq1_mimo-rl-2508_adversarial_default_train.jsonl, rq1_mimo-rl-2508_adversarial_default_validation.jsonl, rq1_mimo-rl-2508_adversarial_single_train.jsonl, rq1_mimo-rl-2508_adversarial_single_validation.jsonl, rq1_mimo-rl-2508_default_train.jsonl, rq1_mimo-rl-2508_default_validation.jsonl, rq1_mimo-rl-2508_single_train.jsonl, rq1_mimo-rl-2508_single_validation.jsonl

## (a) Table 1: per-object accuracy (%)

Tolerant parse is primary, strict (moh) beside it. Accuracy = correct boxes / scored boxes; 95% CI = bootstrap over images. Token-limit rule: every object answered by a call that hit max_tokens is wrong (kept in the denominator). Cut calls = calls at max_tokens; cut rows = rows with at least one; 'tol, trunc dropped' drops those rows. Parse fail = share of boxes with no tolerant label / with a strict label that is not a candidate name (single: raw answer is not exactly a candidate).

| model | subset | probe | split | n img | n obj | cut calls / rows | tolerant [95% CI] | strict [95% CI] | tol, trunc dropped | parse fail tol / strict |
|---|---|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | In-the-Wild | default | Seen | 1539 | 7695 | 195 / 195 | 60.6 [59.0, 62.3] | 55.7 [53.9, 57.4] | 69.4 | 12.6 / 19.8 |
| mimo-rl-2508 | In-the-Wild | default | Unseen | 1172 | 5860 | 211 / 211 | 53.3 [51.5, 55.3] | 46.3 [44.2, 48.4] | 65.1 | 17.9 / 29.8 |
| mimo-rl-2508 | In-the-Wild | single | Seen | 1539 | 7695 | 79 / 72 | 69.8 [68.6, 71.0] | 52.9 [51.5, 54.3] | 70.7 | 1.0 / 29.6 |
| mimo-rl-2508 | In-the-Wild | single | Unseen | 1172 | 5860 | 80 / 77 | 64.9 [63.5, 66.3] | 47.0 [45.5, 48.7] | 65.7 | 1.4 / 34.7 |
| mimo-rl-2508 | Homogeneous | default | Seen | 400 | 2000 | 7 / 7 | 87.0 [84.0, 90.0] | 85.2 [81.6, 88.3] | 88.5 | 1.8 / 4.4 |
| mimo-rl-2508 | Homogeneous | default | Unseen | 490 | 2450 | 22 / 22 | 79.8 [76.6, 82.8] | 78.0 [74.6, 81.3] | 83.5 | 5.0 / 7.3 |
| mimo-rl-2508 | Homogeneous | single | Seen | 400 | 2000 | 5 / 3 | 88.2 [85.8, 90.5] | 73.7 [70.5, 76.8] | 88.4 | 0.2 / 20.6 |
| mimo-rl-2508 | Homogeneous | single | Unseen | 490 | 2450 | 16 / 16 | 79.7 [77.0, 82.5] | 64.4 [61.3, 67.5] | 81.6 | 0.7 / 25.9 |
| mimo-rl-2508 | Heterogeneous | default | Seen | 312 | 1560 | 68 / 68 | 48.1 [44.5, 51.8] | 45.4 [41.6, 49.5] | 61.6 | 22.1 / 27.3 |
| mimo-rl-2508 | Heterogeneous | default | Unseen | 246 | 1230 | 57 / 57 | 41.5 [37.7, 45.3] | 35.4 [31.4, 39.4] | 54.0 | 22.8 / 34.9 |
| mimo-rl-2508 | Heterogeneous | single | Seen | 312 | 1560 | 33 / 30 | 61.8 [59.5, 64.2] | 41.7 [39.2, 44.4] | 63.3 | 2.1 / 36.2 |
| mimo-rl-2508 | Heterogeneous | single | Unseen | 246 | 1230 | 23 / 21 | 53.0 [50.5, 55.4] | 32.8 [30.2, 35.5] | 53.8 | 1.9 / 43.4 |
| mimo-rl-2508 | Adversarial | default | Seen | 336 | 1680 | 21 / 21 | 70.2 [66.4, 73.9] | 67.9 [64.2, 71.8] | 74.9 | 6.2 / 10.0 |
| mimo-rl-2508 | Adversarial | default | Unseen | 668 | 3340 | 57 / 57 | 65.1 [62.3, 67.8] | 60.6 [57.8, 63.4] | 71.2 | 8.6 / 15.7 |
| mimo-rl-2508 | Adversarial | single | Seen | 336 | 1680 | 12 / 10 | 77.5 [74.6, 80.3] | 63.9 [60.7, 67.0] | 78.2 | 0.7 / 23.8 |
| mimo-rl-2508 | Adversarial | single | Unseen | 668 | 3340 | 39 / 35 | 68.1 [65.9, 70.2] | 52.2 [49.8, 54.6] | 70.2 | 1.2 / 31.1 |
| mimo-rl-2508 | Adversarial AAAAB | default | Seen | 168 | 840 | 9 / 9 | 71.7 [66.7, 76.7] | 68.8 [63.5, 73.8] | 75.7 | 5.4 / 9.4 |
| mimo-rl-2508 | Adversarial AAAAB | default | Unseen | 334 | 1670 | 35 / 35 | 64.0 [60.3, 68.0] | 59.0 [54.9, 63.1] | 71.4 | 10.6 / 18.3 |
| mimo-rl-2508 | Adversarial AAAAB | single | Seen | 168 | 840 | 5 / 4 | 78.3 [74.2, 82.1] | 64.5 [59.6, 69.2] | 78.9 | 0.6 / 23.5 |
| mimo-rl-2508 | Adversarial AAAAB | single | Unseen | 334 | 1670 | 20 / 18 | 68.7 [65.6, 72.0] | 52.2 [48.6, 55.7] | 70.8 | 1.2 / 31.2 |
| mimo-rl-2508 | Adversarial BAAAA | default | Seen | 168 | 840 | 12 / 12 | 68.8 [63.5, 73.9] | 66.9 [61.2, 72.1] | 74.1 | 7.1 / 10.6 |
| mimo-rl-2508 | Adversarial BAAAA | default | Unseen | 334 | 1670 | 22 / 22 | 66.3 [62.8, 70.0] | 62.2 [58.2, 66.1] | 71.0 | 6.6 / 13.1 |
| mimo-rl-2508 | Adversarial BAAAA | single | Seen | 168 | 840 | 7 / 6 | 76.7 [72.4, 80.5] | 63.3 [58.8, 67.7] | 77.4 | 0.8 / 24.2 |
| mimo-rl-2508 | Adversarial BAAAA | single | Unseen | 334 | 1670 | 19 / 17 | 67.4 [64.0, 70.5] | 52.2 [49.0, 55.6] | 69.7 | 1.1 / 31.1 |

## (b) Paired tests on the same images

### single (x) vs default (y), each model

Paired unit: the box (image x box position) on the same image, images matched on (split, subset, entry_idx, image_id). McNemar = exact two-sided test on discordant boxes (b = right only under x, c = right only under y; it treats the 5 boxes of an image as independent). CI = paired bootstrap over images of the per-image accuracy difference. diff = y - x in points. Holm family = all rows of this table, separately per parser.

| comparison | subset | probe | split | n img | tolerant x -> y | diff [95% CI] | b / c | p | Holm p | strict diff [95% CI] | strict p (Holm) | tol diff, trunc dropped (n img) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508: single -> default | In-the-Wild | - | Seen | 1539 | 69.8 -> 60.6 | -9.1 [-10.5, -7.8] | 1098 / 395 | 1.1e-76 | 8.0e-76 | +2.8 [+1.1, +4.6] | 5.2e-06 (2.6e-05) | -2.3 (1308) |
| mimo-rl-2508: single -> default | In-the-Wild | - | Unseen | 1172 | 64.9 -> 53.3 | -11.6 [-13.2, -9.9] | 1032 / 353 | 2.4e-77 | 1.9e-76 | -0.7 [-2.7, +1.3] | 0.363 (0.363) | -1.9 (920) |
| mimo-rl-2508: single -> default | Homogeneous | - | Seen | 400 | 88.2 -> 87.0 | -1.2 [-3.2, +0.6] | 89 / 65 | 0.0635 | 0.127 | +11.4 [+8.3, +14.5] | 1.3e-31 (8.9e-31) | +0.1 (391) |
| mimo-rl-2508: single -> default | Homogeneous | - | Unseen | 490 | 79.7 -> 79.8 | +0.1 [-1.8, +2.0] | 133 / 135 | 0.951 | 0.951 | +13.6 [+10.9, +16.1] | 3.6e-47 (2.9e-46) | +2.2 (459) |
| mimo-rl-2508: single -> default | Heterogeneous | - | Seen | 312 | 61.8 -> 48.1 | -13.7 [-17.0, -10.4] | 291 / 78 | 5.2e-30 | 3.1e-29 | +3.7 [-0.0, +7.5] | 0.0104 (0.0313) | -2.1 (234) |
| mimo-rl-2508: single -> default | Heterogeneous | - | Unseen | 246 | 53.0 -> 41.5 | -11.5 [-14.6, -8.4] | 203 / 61 | 5.3e-19 | 2.6e-18 | +2.5 [-1.5, +6.6] | 0.105 (0.21) | -0.9 (181) |
| mimo-rl-2508: single -> default | Adversarial | - | Seen | 336 | 77.5 -> 70.2 | -7.3 [-9.9, -4.5] | 191 / 69 | 2.0e-14 | 8.1e-14 | +3.9 [+0.3, +7.7] | 0.00141 (0.00564) | -3.5 (310) |
| mimo-rl-2508: single -> default | Adversarial | - | Unseen | 668 | 68.1 -> 65.1 | -2.9 [-4.9, -1.0] | 340 / 243 | 6.8e-05 | 2.0e-04 | +8.4 [+5.9, +10.7] | 1.1e-20 (6.6e-20) | +2.0 (588) |

Note: pair mimo-sft-2508 vs mimo-rl-2508 skipped: no file for mimo-sft-2508.

Note: pair qwen3vl-8b-instruct vs qwen3vl-8b-thinking skipped: no file for qwen3vl-8b-instruct.

## (c) Accuracy by box position (%), tolerant (strict)

| model | subset | probe | split | n img | box 1 | box 2 | box 3 | box 4 | box 5 |
|---|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Adversarial AAAAB | default | Seen | 168 | 76.2 (72.6) | 73.2 (70.8) | 75.6 (73.2) | 76.8 (75.0) | 56.5 (52.4) |
| mimo-rl-2508 | Adversarial BAAAA | default | Seen | 168 | 51.8 (51.2) | 73.8 (72.0) | 72.0 (70.2) | 72.6 (71.4) | 73.8 (69.6) |
| mimo-rl-2508 | Heterogeneous | default | Seen | 312 | 50.6 (47.8) | 47.1 (45.8) | 43.6 (42.0) | 50.6 (47.8) | 48.7 (43.6) |
| mimo-rl-2508 | Homogeneous | default | Seen | 400 | 87.0 (86.2) | 85.2 (83.8) | 87.5 (86.0) | 88.2 (86.0) | 87.0 (83.8) |
| mimo-rl-2508 | In-the-Wild | default | Seen | 1539 | 59.7 (55.6) | 60.1 (56.3) | 60.9 (56.7) | 62.0 (57.9) | 60.5 (51.9) |
| mimo-rl-2508 | Adversarial AAAAB | default | Unseen | 334 | 68.3 (62.6) | 68.9 (65.9) | 71.6 (67.7) | 68.9 (65.6) | 42.2 (33.2) |
| mimo-rl-2508 | Adversarial BAAAA | default | Unseen | 334 | 44.6 (41.3) | 70.1 (67.7) | 73.1 (70.1) | 73.1 (69.8) | 71.0 (62.0) |
| mimo-rl-2508 | Heterogeneous | default | Unseen | 246 | 44.7 (37.8) | 42.3 (36.6) | 39.0 (35.0) | 44.7 (37.0) | 36.6 (30.5) |
| mimo-rl-2508 | Homogeneous | default | Unseen | 490 | 79.2 (77.8) | 79.6 (79.2) | 80.0 (79.0) | 79.6 (79.2) | 80.4 (74.9) |
| mimo-rl-2508 | In-the-Wild | default | Unseen | 1172 | 54.2 (48.4) | 54.2 (48.1) | 51.5 (45.6) | 53.3 (47.5) | 53.6 (42.1) |
| mimo-rl-2508 | Adversarial AAAAB | single | Seen | 168 | 82.1 (66.7) | 79.2 (66.1) | 81.0 (73.2) | 85.7 (72.6) | 63.7 (44.0) |
| mimo-rl-2508 | Adversarial BAAAA | single | Seen | 168 | 58.9 (46.4) | 82.1 (70.2) | 78.6 (61.9) | 79.8 (69.6) | 83.9 (68.5) |
| mimo-rl-2508 | Heterogeneous | single | Seen | 312 | 63.8 (44.2) | 60.3 (41.7) | 56.1 (40.4) | 62.5 (38.5) | 66.3 (43.9) |
| mimo-rl-2508 | Homogeneous | single | Seen | 400 | 89.0 (73.0) | 87.2 (73.8) | 90.2 (76.8) | 89.5 (73.2) | 85.0 (71.8) |
| mimo-rl-2508 | In-the-Wild | single | Seen | 1539 | 68.1 (50.9) | 70.7 (53.9) | 69.4 (53.9) | 70.9 (52.4) | 69.8 (53.2) |
| mimo-rl-2508 | Adversarial AAAAB | single | Unseen | 334 | 72.8 (56.9) | 71.3 (57.2) | 71.9 (54.2) | 70.7 (55.4) | 57.2 (37.4) |
| mimo-rl-2508 | Adversarial BAAAA | single | Unseen | 334 | 54.2 (36.5) | 71.9 (56.0) | 73.1 (58.4) | 68.9 (54.8) | 68.9 (55.4) |
| mimo-rl-2508 | Heterogeneous | single | Unseen | 246 | 56.5 (36.2) | 54.9 (35.4) | 49.6 (30.5) | 54.5 (30.9) | 49.6 (31.3) |
| mimo-rl-2508 | Homogeneous | single | Unseen | 490 | 80.6 (66.7) | 81.4 (65.5) | 79.6 (63.1) | 78.6 (64.5) | 78.2 (62.4) |
| mimo-rl-2508 | In-the-Wild | single | Unseen | 1172 | 65.8 (47.4) | 66.3 (48.4) | 63.6 (45.2) | 63.0 (46.2) | 66.0 (48.0) |

## (d) Seen vs Unseen gap (unpaired: different images and candidate lists)

gap = Unseen - Seen, points, per-object accuracy. CI = bootstrap resampling each split's images separately; p = two-sided permutation test on per-image accuracy (10,000 reps). Holm family = the rows of one model.

| model | subset | probe | n Seen / Unseen | tolerant Seen -> Unseen | gap [95% CI] | p | Holm p | strict gap [95% CI] |
|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | In-the-Wild | default | 1539 / 1172 | 60.6 -> 53.3 | -7.3 [-9.8, -4.7] | 1.0e-04 | 8.0e-04 | -9.3 [-12.1, -6.7] |
| mimo-rl-2508 | In-the-Wild | single | 1539 / 1172 | 69.8 -> 64.9 | -4.8 [-6.8, -3.0] | 1.0e-04 | 8.0e-04 | -5.8 [-7.9, -3.8] |
| mimo-rl-2508 | Homogeneous | default | 400 / 490 | 87.0 -> 79.8 | -7.2 [-11.5, -3.0] | 0.0012 | 0.0036 | -7.2 [-11.5, -2.7] |
| mimo-rl-2508 | Homogeneous | single | 400 / 490 | 88.2 -> 79.7 | -8.5 [-12.1, -4.7] | 1.0e-04 | 8.0e-04 | -9.3 [-13.9, -4.8] |
| mimo-rl-2508 | Heterogeneous | default | 312 / 246 | 48.1 -> 41.5 | -6.7 [-12.0, -1.1] | 0.0148 | 0.0296 | -10.0 [-15.7, -4.2] |
| mimo-rl-2508 | Heterogeneous | single | 312 / 246 | 61.8 -> 53.0 | -8.8 [-12.3, -5.4] | 1.0e-04 | 8.0e-04 | -8.9 [-12.5, -5.2] |
| mimo-rl-2508 | Adversarial | default | 336 / 668 | 70.2 -> 65.1 | -5.1 [-9.6, -0.7] | 0.028 | 0.0296 | -7.3 [-12.0, -2.5] |
| mimo-rl-2508 | Adversarial | single | 336 / 668 | 77.5 -> 68.1 | -9.4 [-13.1, -5.8] | 1.0e-04 | 8.0e-04 | -11.7 [-15.8, -7.6] |

