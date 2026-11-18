# RQ1 tables

Files (8): rq1_mimo-sft-2508_adversarial_default_train.jsonl, rq1_mimo-sft-2508_adversarial_default_validation.jsonl, rq1_mimo-sft-2508_adversarial_single_train.jsonl, rq1_mimo-sft-2508_adversarial_single_validation.jsonl, rq1_mimo-sft-2508_default_train.jsonl, rq1_mimo-sft-2508_default_validation.jsonl, rq1_mimo-sft-2508_single_train.jsonl, rq1_mimo-sft-2508_single_validation.jsonl

## (a) Table 1: per-object accuracy (%)

Tolerant parse is primary, strict (moh) beside it. Accuracy = correct boxes / scored boxes; 95% CI = bootstrap over images. Token-limit rule: every object answered by a call that hit max_tokens is wrong (kept in the denominator). Cut calls = calls at max_tokens; cut rows = rows with at least one; 'tol, trunc dropped' drops those rows. Parse fail = share of boxes with no tolerant label / with a strict label that is not a candidate name (single: raw answer is not exactly a candidate).

| model | subset | probe | split | n img | n obj | cut calls / rows | tolerant [95% CI] | strict [95% CI] | tol, trunc dropped | parse fail tol / strict |
|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | In-the-Wild | default | Seen | 1539 | 7695 | 90 / 90 | 61.0 [59.6, 62.4] | 61.0 [59.4, 62.4] | 64.8 | 5.9 / 6.1 |
| mimo-sft-2508 | In-the-Wild | default | Unseen | 1172 | 5860 | 95 / 95 | 55.2 [53.4, 56.9] | 55.2 [53.4, 56.9] | 60.1 | 8.1 / 8.3 |
| mimo-sft-2508 | In-the-Wild | single | Seen | 1539 | 7695 | 90 / 79 | 68.3 [67.0, 69.5] | 68.2 [67.0, 69.4] | 69.3 | 1.2 / 1.7 |
| mimo-sft-2508 | In-the-Wild | single | Unseen | 1172 | 5860 | 68 / 66 | 62.7 [61.3, 64.2] | 62.7 [61.3, 64.2] | 63.7 | 1.2 / 1.6 |
| mimo-sft-2508 | Homogeneous | default | Seen | 400 | 2000 | 5 / 5 | 85.2 [82.1, 88.2] | 85.2 [82.1, 88.2] | 86.3 | 1.2 / 1.5 |
| mimo-sft-2508 | Homogeneous | default | Unseen | 490 | 2450 | 12 / 12 | 80.9 [77.8, 84.0] | 80.9 [77.9, 83.8] | 83.0 | 2.4 / 2.6 |
| mimo-sft-2508 | Homogeneous | single | Seen | 400 | 2000 | 10 / 10 | 85.1 [82.8, 87.5] | 85.1 [82.7, 87.5] | 85.4 | 0.5 / 0.9 |
| mimo-sft-2508 | Homogeneous | single | Unseen | 490 | 2450 | 10 / 10 | 75.8 [73.1, 78.7] | 75.8 [72.8, 78.7] | 76.4 | 0.4 / 0.7 |
| mimo-sft-2508 | Heterogeneous | default | Seen | 312 | 1560 | 43 / 43 | 49.4 [46.1, 52.8] | 49.4 [46.1, 52.9] | 57.3 | 13.8 / 14.1 |
| mimo-sft-2508 | Heterogeneous | default | Unseen | 246 | 1230 | 30 / 30 | 42.1 [38.8, 45.4] | 42.1 [38.8, 45.4] | 48.0 | 12.2 / 12.4 |
| mimo-sft-2508 | Heterogeneous | single | Seen | 312 | 1560 | 33 / 31 | 59.2 [56.9, 61.7] | 59.2 [56.9, 61.5] | 60.9 | 2.1 / 2.8 |
| mimo-sft-2508 | Heterogeneous | single | Unseen | 246 | 1230 | 21 / 21 | 49.6 [47.0, 52.0] | 49.6 [47.0, 52.2] | 50.3 | 1.7 / 2.4 |
| mimo-sft-2508 | Adversarial | default | Seen | 336 | 1680 | 8 / 8 | 70.8 [67.4, 74.0] | 70.7 [67.4, 73.8] | 72.5 | 2.4 / 2.7 |
| mimo-sft-2508 | Adversarial | default | Unseen | 668 | 3340 | 23 / 23 | 64.4 [61.8, 66.7] | 64.4 [61.9, 66.8] | 66.7 | 3.4 / 3.5 |
| mimo-sft-2508 | Adversarial | single | Seen | 336 | 1680 | 13 / 13 | 73.8 [70.9, 76.7] | 73.8 [71.0, 76.5] | 74.4 | 0.8 / 1.2 |
| mimo-sft-2508 | Adversarial | single | Unseen | 668 | 3340 | 35 / 31 | 64.6 [62.3, 66.9] | 64.6 [62.2, 66.8] | 66.3 | 1.0 / 1.5 |
| mimo-sft-2508 | Adversarial AAAAB | default | Seen | 168 | 840 | 3 / 3 | 72.5 [68.0, 76.8] | 72.4 [68.0, 76.6] | 73.8 | 1.8 / 2.0 |
| mimo-sft-2508 | Adversarial AAAAB | default | Unseen | 334 | 1670 | 13 / 13 | 64.7 [61.3, 68.1] | 64.7 [61.0, 68.3] | 67.4 | 3.9 / 3.9 |
| mimo-sft-2508 | Adversarial AAAAB | single | Seen | 168 | 840 | 8 / 8 | 74.4 [70.2, 78.3] | 74.4 [70.4, 78.1] | 75.4 | 1.0 / 1.4 |
| mimo-sft-2508 | Adversarial AAAAB | single | Unseen | 334 | 1670 | 19 / 17 | 64.9 [61.7, 67.9] | 64.9 [61.6, 68.0] | 66.8 | 1.1 / 1.7 |
| mimo-sft-2508 | Adversarial BAAAA | default | Seen | 168 | 840 | 5 / 5 | 69.0 [64.0, 73.7] | 69.0 [63.9, 73.7] | 71.2 | 3.0 / 3.3 |
| mimo-sft-2508 | Adversarial BAAAA | default | Unseen | 334 | 1670 | 10 / 10 | 64.0 [60.8, 67.4] | 64.0 [60.6, 67.5] | 66.0 | 3.0 / 3.1 |
| mimo-sft-2508 | Adversarial BAAAA | single | Seen | 168 | 840 | 5 / 5 | 73.2 [68.9, 77.1] | 73.2 [69.2, 77.0] | 73.4 | 0.6 / 1.1 |
| mimo-sft-2508 | Adversarial BAAAA | single | Unseen | 334 | 1670 | 16 / 14 | 64.4 [61.0, 67.7] | 64.3 [61.1, 67.5] | 65.8 | 1.0 / 1.3 |

## (b) Paired tests on the same images

### single (x) vs default (y), each model

Paired unit: the box (image x box position) on the same image, images matched on (split, subset, entry_idx, image_id). McNemar = exact two-sided test on discordant boxes (b = right only under x, c = right only under y; it treats the 5 boxes of an image as independent). CI = paired bootstrap over images of the per-image accuracy difference. diff = y - x in points. Holm family = all rows of this table, separately per parser.

| comparison | subset | probe | split | n img | tolerant x -> y | diff [95% CI] | b / c | p | Holm p | strict diff [95% CI] | strict p (Holm) | tol diff, trunc dropped (n img) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508: single -> default | In-the-Wild | - | Seen | 1539 | 68.3 -> 61.0 | -7.2 [-8.5, -6.0] | 1092 / 535 | 4.6e-44 | 3.6e-43 | -7.2 [-8.4, -6.0] | 2.1e-43 (1.7e-42) | -4.5 (1402) |
| mimo-sft-2508: single -> default | In-the-Wild | - | Unseen | 1172 | 62.7 -> 55.2 | -7.5 [-9.1, -6.1] | 930 / 488 | 3.5e-32 | 2.5e-31 | -7.6 [-9.2, -6.0] | 2.7e-32 (1.9e-31) | -3.4 (1035) |
| mimo-sft-2508: single -> default | Homogeneous | - | Seen | 400 | 85.1 -> 85.2 | +0.1 [-2.2, +2.4] | 129 / 132 | 0.902 | 1 | +0.1 [-2.3, +2.5] | 0.902 (1) | +0.7 (385) |
| mimo-sft-2508: single -> default | Homogeneous | - | Unseen | 490 | 75.8 -> 80.9 | +5.1 [+2.8, +7.3] | 113 / 238 | 2.2e-11 | 1.1e-10 | +5.1 [+3.0, +7.2] | 2.2e-11 (1.1e-10) | +6.4 (471) |
| mimo-sft-2508: single -> default | Heterogeneous | - | Seen | 312 | 59.2 -> 49.4 | -9.8 [-12.8, -7.0] | 254 / 101 | 2.5e-16 | 1.5e-15 | -9.7 [-12.8, -6.7] | 3.5e-16 (2.1e-15) | -3.0 (250) |
| mimo-sft-2508: single -> default | Heterogeneous | - | Unseen | 246 | 49.6 -> 42.1 | -7.5 [-10.3, -4.4] | 165 / 73 | 2.3e-09 | 9.3e-09 | -7.5 [-10.7, -4.4] | 2.3e-09 (9.3e-09) | -2.8 (200) |
| mimo-sft-2508: single -> default | Adversarial | - | Seen | 336 | 73.8 -> 70.8 | -3.0 [-5.4, -0.7] | 169 / 118 | 0.0031 | 0.00929 | -3.1 [-5.4, -0.8] | 0.00259 (0.00778) | -1.9 (315) |
| mimo-sft-2508: single -> default | Adversarial | - | Unseen | 668 | 64.6 -> 64.4 | -0.2 [-2.2, +1.5] | 334 / 326 | 0.785 | 1 | -0.2 [-1.9, +1.6] | 0.816 (1) | +1.0 (623) |

Note: pair mimo-sft-2508 vs mimo-rl-2508 skipped: no file for mimo-rl-2508.

Note: pair qwen3vl-8b-instruct vs qwen3vl-8b-thinking skipped: no file for qwen3vl-8b-instruct.

## (c) Accuracy by box position (%), tolerant (strict)

| model | subset | probe | split | n img | box 1 | box 2 | box 3 | box 4 | box 5 |
|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | Adversarial AAAAB | default | Seen | 168 | 75.6 (75.0) | 76.2 (76.2) | 78.0 (78.0) | 82.7 (82.7) | 50.0 (50.0) |
| mimo-sft-2508 | Adversarial BAAAA | default | Seen | 168 | 53.0 (53.0) | 76.8 (76.8) | 70.2 (70.2) | 72.0 (72.0) | 73.2 (73.2) |
| mimo-sft-2508 | Heterogeneous | default | Seen | 312 | 48.1 (48.1) | 50.0 (50.0) | 46.2 (46.2) | 52.6 (52.6) | 50.3 (50.3) |
| mimo-sft-2508 | Homogeneous | default | Seen | 400 | 85.2 (85.0) | 84.8 (84.8) | 85.5 (85.5) | 85.8 (86.0) | 85.0 (85.0) |
| mimo-sft-2508 | In-the-Wild | default | Seen | 1539 | 60.2 (60.2) | 59.5 (59.5) | 61.1 (61.1) | 63.9 (63.9) | 60.5 (60.4) |
| mimo-sft-2508 | Adversarial AAAAB | default | Unseen | 334 | 68.6 (68.6) | 71.0 (70.7) | 70.1 (70.1) | 73.4 (73.7) | 40.7 (40.7) |
| mimo-sft-2508 | Adversarial BAAAA | default | Unseen | 334 | 43.4 (43.4) | 69.8 (69.8) | 69.5 (69.5) | 71.9 (71.9) | 65.6 (65.6) |
| mimo-sft-2508 | Heterogeneous | default | Unseen | 246 | 45.1 (45.1) | 41.1 (41.1) | 39.0 (39.0) | 45.9 (45.9) | 39.4 (39.4) |
| mimo-sft-2508 | Homogeneous | default | Unseen | 490 | 81.8 (81.8) | 79.6 (79.6) | 80.6 (80.6) | 81.6 (81.6) | 81.0 (81.0) |
| mimo-sft-2508 | In-the-Wild | default | Unseen | 1172 | 54.8 (54.8) | 55.6 (55.5) | 53.8 (53.8) | 57.7 (57.6) | 54.2 (54.2) |
| mimo-sft-2508 | Adversarial AAAAB | single | Seen | 168 | 77.4 (77.4) | 74.4 (74.4) | 77.4 (77.4) | 84.5 (84.5) | 58.3 (58.3) |
| mimo-sft-2508 | Adversarial BAAAA | single | Seen | 168 | 58.3 (58.3) | 74.4 (74.4) | 76.2 (76.2) | 74.4 (74.4) | 82.7 (82.7) |
| mimo-sft-2508 | Heterogeneous | single | Seen | 312 | 60.6 (60.6) | 59.6 (59.6) | 55.8 (55.8) | 60.9 (60.9) | 59.3 (59.0) |
| mimo-sft-2508 | Homogeneous | single | Seen | 400 | 84.5 (84.5) | 85.8 (85.8) | 85.8 (85.8) | 85.2 (85.2) | 84.2 (84.2) |
| mimo-sft-2508 | In-the-Wild | single | Seen | 1539 | 67.4 (67.3) | 68.2 (68.2) | 68.9 (68.9) | 69.0 (69.0) | 67.8 (67.6) |
| mimo-sft-2508 | Adversarial AAAAB | single | Unseen | 334 | 66.2 (66.2) | 68.6 (68.6) | 67.4 (67.4) | 66.2 (66.2) | 56.0 (56.0) |
| mimo-sft-2508 | Adversarial BAAAA | single | Unseen | 334 | 54.5 (54.5) | 67.4 (67.1) | 68.9 (68.9) | 66.2 (66.2) | 65.0 (65.0) |
| mimo-sft-2508 | Heterogeneous | single | Unseen | 246 | 52.8 (52.8) | 52.0 (52.0) | 48.4 (48.4) | 51.2 (51.2) | 43.5 (43.5) |
| mimo-sft-2508 | Homogeneous | single | Unseen | 490 | 77.1 (77.1) | 78.6 (78.6) | 75.7 (75.7) | 74.3 (74.3) | 73.5 (73.5) |
| mimo-sft-2508 | In-the-Wild | single | Unseen | 1172 | 63.3 (63.3) | 62.7 (62.7) | 62.2 (62.1) | 62.5 (62.5) | 63.1 (63.1) |

## (d) Seen vs Unseen gap (unpaired: different images and candidate lists)

gap = Unseen - Seen, points, per-object accuracy. CI = bootstrap resampling each split's images separately; p = two-sided permutation test on per-image accuracy (10,000 reps). Holm family = the rows of one model.

| model | subset | probe | n Seen / Unseen | tolerant Seen -> Unseen | gap [95% CI] | p | Holm p | strict gap [95% CI] |
|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | In-the-Wild | default | 1539 / 1172 | 61.0 -> 55.2 | -5.8 [-8.1, -3.5] | 1.0e-04 | 8.0e-04 | -5.8 [-8.1, -3.4] |
| mimo-sft-2508 | In-the-Wild | single | 1539 / 1172 | 68.3 -> 62.7 | -5.5 [-7.5, -3.6] | 1.0e-04 | 8.0e-04 | -5.5 [-7.3, -3.6] |
| mimo-sft-2508 | Homogeneous | default | 400 / 490 | 85.2 -> 80.9 | -4.3 [-8.5, +0.2] | 0.0549 | 0.0549 | -4.3 [-8.5, -0.2] |
| mimo-sft-2508 | Homogeneous | single | 400 / 490 | 85.1 -> 75.8 | -9.3 [-13.0, -5.5] | 1.0e-04 | 8.0e-04 | -9.3 [-13.0, -5.4] |
| mimo-sft-2508 | Heterogeneous | default | 312 / 246 | 49.4 -> 42.1 | -7.3 [-12.0, -2.3] | 0.0031 | 0.0063 | -7.3 [-11.8, -2.6] |
| mimo-sft-2508 | Heterogeneous | single | 312 / 246 | 59.2 -> 49.6 | -9.6 [-13.1, -6.2] | 1.0e-04 | 8.0e-04 | -9.6 [-13.2, -6.1] |
| mimo-sft-2508 | Adversarial | default | 336 / 668 | 70.8 -> 64.4 | -6.4 [-10.4, -2.4] | 0.0021 | 0.0063 | -6.3 [-10.5, -2.3] |
| mimo-sft-2508 | Adversarial | single | 336 / 668 | 73.8 -> 64.6 | -9.2 [-12.7, -5.5] | 1.0e-04 | 8.0e-04 | -9.2 [-12.8, -5.7] |

