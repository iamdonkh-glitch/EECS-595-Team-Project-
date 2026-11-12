# RQ2 forcing probes

Files (24): rq1_qwen3vl-8b-instruct_adversarial_default_train.jsonl, rq1_qwen3vl-8b-instruct_adversarial_default_validation.jsonl, rq1_qwen3vl-8b-instruct_adversarial_single_train.jsonl, rq1_qwen3vl-8b-instruct_adversarial_single_validation.jsonl, rq1_qwen3vl-8b-instruct_default_train.jsonl, rq1_qwen3vl-8b-instruct_default_validation.jsonl, rq1_qwen3vl-8b-instruct_single_train.jsonl, rq1_qwen3vl-8b-instruct_single_validation.jsonl, forcing_cffar_qwen3vl-8b-instruct_train.jsonl, forcing_cffar_qwen3vl-8b-instruct_validation.jsonl, forcing_cfnear_qwen3vl-8b-instruct_train.jsonl, forcing_cfnear_qwen3vl-8b-instruct_validation.jsonl, forcing_dose_qwen3vl-8b-instruct_train.jsonl, forcing_dose_qwen3vl-8b-instruct_validation.jsonl, forcing_homog_qwen3vl-8b-instruct_train.jsonl, forcing_homog_qwen3vl-8b-instruct_validation.jsonl, forcing_place_qwen3vl-8b-instruct_train.jsonl, forcing_place_qwen3vl-8b-instruct_validation.jsonl, forcing_qwen3vl-8b-instruct_cf_train.jsonl, forcing_qwen3vl-8b-instruct_cf_validation.jsonl, forcing_qwen3vl-8b-instruct_tf-incremental_train.jsonl, forcing_qwen3vl-8b-instruct_tf-incremental_validation.jsonl, forcing_qwen3vl-8b-instruct_tf-oneshot_train.jsonl, forcing_qwen3vl-8b-instruct_tf-oneshot_validation.jsonl

## Table 4: the odd object B under each condition (%)

B acc = B named correctly; B=A = B given the class of the other four (inertia); B=C = B given the counterfactual class. Tolerant parse, strict in parentheses. cut = calls for B at the token limit (scored wrong). vs default = paired on the same images, y - x in points; p = exact McNemar, Holm over the model's comparisons in the same probe family (core = single, TF incremental, TF one-shot, CF; dose = given=0-3; placement = assistant; C near/far; Homogeneous control).

| model | split | order | condition | n img | cut | B acc [95% CI] | B=A [95% CI] | B=C | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | Adversarial | single | 336 | 0 | 62.5 (62.5) [57.1, 67.6] | 16.7 (16.7) [12.8, 20.8] | - | +3.0 [-0.6, +6.5] | 0.143 (1) | -6.0 [-9.5, -2.4] | 0.00119 (0.0155) |
| qwen3vl-8b-instruct | Seen | Adversarial | default | 336 | 0 | 59.5 (59.5) [53.6, 64.6] | 22.6 (22.6) [18.5, 27.1] | - | - | - | - | - |
| qwen3vl-8b-instruct | Seen | Adversarial | TF incremental | 336 | 0 | 56.5 (29.8) [50.9, 61.9] | 26.8 (10.4) [22.0, 31.5] | - | -3.0 [-6.0, +0.0] | 0.0755 (0.831) | +4.2 [+1.2, +7.1] | 0.00936 (0.0842) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot | 336 | 0 | 56.0 (3.6) [50.9, 61.0] | 29.5 (3.6) [24.7, 34.2] | - | -3.6 [-6.8, -0.3] | 0.0576 (0.691) | +6.8 [+3.3, +10.4] | 2.9e-04 (0.00441) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF | 336 | 0 | 50.9 (33.0) [45.5, 56.2] | 11.0 (9.2) [8.0, 14.6] | 23.5 (8.0) | -8.6 [-12.5, -4.8] | 2.5e-05 (4.5e-04) | -11.6 [-15.8, -8.0] | 2.8e-09 (5.6e-08) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF near | 336 | 0 | 52.7 (20.2) [47.0, 58.0] | 8.6 (8.0) [5.7, 11.9] | 24.4 (8.3) | -6.8 [-10.4, -3.3] | 1.9e-04 (0.00115) | -14.0 [-18.2, -9.8] | 6.4e-11 (5.1e-10) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF far | 336 | 0 | 50.6 (29.8) [45.5, 56.0] | 10.4 (8.9) [7.4, 13.7] | 23.5 (7.1) | -8.9 [-12.8, -5.1] | 2.4e-05 (1.9e-04) | -12.2 [-16.1, -8.3] | 8.2e-10 (5.8e-09) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF, assistant | 336 | 0 | 16.1 (16.1) [11.9, 20.2] | 0.0 (0.0) [0.0, 0.0] | 80.4 (80.4) | -43.5 [-49.1, -38.1] | 1.6e-41 (1.6e-40) | -22.6 [-27.1, -18.2] | 2.6e-23 (2.1e-22) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, assistant | 336 | 0 | 52.4 (52.4) [47.3, 57.7] | 34.8 (34.8) [30.1, 39.9] | - | -7.1 [-10.4, -4.2] | 3.9e-05 (1.5e-04) | +12.2 [+8.6, +15.8] | 5.9e-11 (2.9e-10) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=0 | 336 | 0 | 60.7 (59.2) [55.4, 66.1] | 20.5 (20.2) [16.1, 25.0] | - | +1.2 [-1.2, +3.6] | 0.481 (1) | -2.1 [-4.5, +0.0] | 0.118 (1) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=1 | 336 | 0 | 57.4 (47.0) [52.1, 62.5] | 26.8 (21.7) [22.3, 31.5] | - | -2.1 [-5.1, +1.2] | 0.265 (1) | +4.2 [+1.2, +7.1] | 0.0125 (0.15) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=2 | 336 | 0 | 57.7 (19.3) [52.4, 62.8] | 28.0 (10.1) [23.2, 32.7] | - | -1.8 [-5.1, +1.5] | 0.392 (1) | +5.4 [+2.1, +8.3] | 0.0021 (0.0315) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=3 | 336 | 0 | 57.1 (8.9) [52.1, 62.2] | 28.3 (6.0) [23.5, 33.0] | - | -2.4 [-6.0, +1.2] | 0.256 (1) | +5.7 [+2.4, +9.2] | 0.00256 (0.0359) |
| qwen3vl-8b-instruct | Seen | AAAAB | single | 168 | 0 | 63.1 (63.1) [55.4, 70.2] | 14.9 (14.9) [9.5, 20.2] | - | +5.4 [+0.6, +10.7] | 0.0784 (0.831) | -11.9 [-17.3, -6.5] | 8.8e-05 (0.00141) |
| qwen3vl-8b-instruct | Seen | AAAAB | default | 168 | 0 | 57.7 (57.7) [50.0, 65.5] | 26.8 (26.8) [20.2, 33.9] | - | - | - | - | - |
| qwen3vl-8b-instruct | Seen | AAAAB | TF incremental | 168 | 0 | 53.6 (0.0) [45.8, 60.7] | 32.7 (0.0) [25.6, 39.9] | - | -4.2 [-9.5, +0.6] | 0.167 (1) | +6.0 [+0.6, +11.3] | 0.0525 (0.315) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot | 168 | 0 | 53.6 (0.0) [45.8, 60.7] | 32.7 (0.0) [25.6, 39.9] | - | -4.2 [-9.5, +0.6] | 0.167 (1) | +6.0 [+0.6, +11.3] | 0.0525 (0.315) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF | 168 | 0 | 46.4 (17.9) [39.3, 53.6] | 9.5 (6.5) [5.4, 14.3] | 31.5 (1.2) | -11.3 [-17.9, -5.4] | 8.8e-04 (0.014) | -17.3 [-23.8, -11.3] | 3.0e-08 (5.7e-07) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF near | 168 | 0 | 50.6 (8.9) [42.8, 57.7] | 7.1 (6.5) [3.6, 11.3] | 28.6 (0.6) | -7.1 [-12.5, -1.8] | 0.0227 (0.0453) | -19.6 [-26.2, -13.7] | 2.1e-09 (1.3e-08) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF far | 168 | 0 | 44.6 (15.5) [36.9, 52.4] | 7.1 (5.4) [3.6, 11.3] | 36.9 (4.2) | -13.1 [-19.6, -6.5] | 2.0e-04 (0.00115) | -19.6 [-26.2, -13.1] | 2.1e-09 (1.3e-08) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF, assistant | 168 | 0 | 17.3 (17.3) [11.9, 23.2] | 0.0 (0.0) [0.0, 0.0] | 79.2 (79.2) | -40.5 [-48.2, -32.1] | 1.1e-18 (7.8e-18) | -26.8 [-33.3, -20.2] | 5.7e-14 (3.4e-13) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, assistant | 168 | 0 | 50.6 (50.6) [43.5, 58.3] | 36.3 (36.3) [28.6, 43.5] | - | -7.1 [-11.9, -2.4] | 0.00754 (0.00836) | +9.5 [+4.8, +14.9] | 4.0e-04 (4.0e-04) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=0 | 168 | 0 | 61.3 (58.9) [54.2, 68.5] | 20.2 (19.6) [14.3, 26.8] | - | +3.6 [-0.0, +7.7] | 0.146 (1) | -6.5 [-10.7, -3.0] | 9.8e-04 (0.0166) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=1 | 168 | 0 | 57.7 (42.9) [50.0, 64.9] | 27.4 (18.5) [20.8, 33.9] | - | +0.0 [-5.4, +4.8] | 1 (1) | +0.6 [-4.2, +4.8] | 1 (1) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=2 | 168 | 0 | 55.4 (16.7) [47.6, 62.5] | 30.4 (6.5) [23.8, 36.9] | - | -2.4 [-7.7, +3.0] | 0.503 (1) | +3.6 [-1.2, +8.3] | 0.238 (1) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=3 | 168 | 0 | 56.0 (9.5) [48.8, 63.7] | 29.2 (6.0) [22.6, 36.3] | - | -1.8 [-7.2, +3.6] | 0.678 (1) | +2.4 [-3.0, +7.2] | 0.503 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | single | 168 | 0 | 61.9 (61.9) [54.8, 69.6] | 18.5 (18.5) [13.1, 24.4] | - | +0.6 [-4.2, +5.4] | 1 (1) | +0.0 [-3.6, +3.6] | 1 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | default | 168 | 0 | 61.3 (61.3) [53.6, 68.5] | 18.5 (18.5) [13.1, 23.8] | - | - | - | - | - |
| qwen3vl-8b-instruct | Seen | BAAAA | TF incremental | 168 | 0 | 59.5 (59.5) [52.4, 66.7] | 20.8 (20.8) [14.9, 27.4] | - | -1.8 [-4.8, +1.2] | 0.453 (1) | +2.4 [+0.6, +4.8] | 0.125 (0.5) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot | 168 | 0 | 58.3 (7.1) [51.2, 65.5] | 26.2 (7.1) [19.0, 33.3] | - | -3.0 [-7.1, +1.2] | 0.302 (1) | +7.7 [+3.6, +13.1] | 0.00235 (0.0282) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF | 168 | 0 | 55.4 (48.2) [48.2, 62.5] | 12.5 (11.9) [7.7, 17.3] | 15.5 (14.9) | -6.0 [-10.7, -1.8] | 0.0213 (0.298) | -6.0 [-10.7, -1.2] | 0.0213 (0.17) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF near | 168 | 0 | 54.8 (31.5) [47.6, 61.9] | 10.1 (9.5) [6.0, 14.9] | 20.2 (16.1) | -6.5 [-10.7, -3.0] | 0.00342 (0.0103) | -8.3 [-13.7, -3.6] | 0.00434 (0.013) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF far | 168 | 0 | 56.5 (44.0) [48.8, 64.3] | 13.7 (12.5) [8.3, 19.0] | 10.1 (10.1) | -4.8 [-9.5, +0.0] | 0.0768 (0.0768) | -4.8 [-9.5, -0.6] | 0.0574 (0.0574) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF, assistant | 168 | 0 | 14.9 (14.9) [10.1, 20.2] | 0.0 (0.0) [0.0, 0.0] | 81.5 (81.5) | -46.4 [-54.2, -39.3] | 6.6e-24 (5.3e-23) | -18.5 [-25.0, -12.5] | 9.3e-10 (2.8e-09) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, assistant | 168 | 0 | 54.2 (54.2) [47.0, 61.9] | 33.3 (33.3) [26.2, 40.5] | - | -7.1 [-11.9, -3.0] | 0.00418 (0.00836) | +14.9 [+9.5, +20.2] | 6.0e-08 (1.2e-07) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=0 | 168 | 0 | 60.1 (59.5) [52.4, 67.3] | 20.8 (20.8) [14.9, 27.4] | - | -1.2 [-4.2, +1.2] | 0.688 (1) | +2.4 [+0.6, +4.8] | 0.125 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=1 | 168 | 0 | 57.1 (51.2) [49.4, 64.9] | 26.2 (25.0) [19.6, 32.7] | - | -4.2 [-8.3, -0.6] | 0.0654 (1) | +7.7 [+4.2, +11.9] | 2.4e-04 (0.00464) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=2 | 168 | 0 | 60.1 (22.0) [52.4, 67.3] | 25.6 (13.7) [19.0, 32.1] | - | -1.2 [-5.4, +3.0] | 0.791 (1) | +7.1 [+3.0, +11.3] | 0.00183 (0.0293) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=3 | 168 | 0 | 58.3 (8.3) [50.6, 65.5] | 27.4 (6.0) [20.8, 35.1] | - | -3.0 [-7.7, +1.2] | 0.302 (1) | +8.9 [+4.8, +13.7] | 2.7e-04 (0.00494) |
| qwen3vl-8b-instruct | Seen | Homogeneous control | single | 400 | 0 | 91.5 (91.5) [88.8, 94.0] | - | - | -2.2 [-4.2, -0.5] | 0.0352 (0.0532) | - | - |
| qwen3vl-8b-instruct | Seen | Homogeneous control | default | 400 | 0 | 93.8 (93.8) [91.5, 96.0] | - | - | - | - | - | - |
| qwen3vl-8b-instruct | Seen | Homogeneous control | TF one-shot | 400 | 0 | 98.8 (0.0) [97.5, 99.8] | - | - | +5.0 [+3.0, +7.2] | 1.9e-06 (5.7e-06) | - | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | single | 668 | 0 | 58.4 (58.4) [54.8, 62.3] | 21.4 (21.4) [18.3, 24.6] | - | +5.5 [+2.8, +8.2] | 1.1e-04 (0.00187) | -9.1 [-12.0, -6.4] | 5.5e-11 (1.2e-09) |
| qwen3vl-8b-instruct | Unseen | Adversarial | default | 668 | 0 | 52.8 (52.7) [49.1, 56.7] | 30.5 (30.5) [27.2, 34.0] | - | - | - | - | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF incremental | 668 | 1 | 47.3 (23.8) [43.4, 51.2] | 33.2 (12.9) [29.8, 36.8] | - | -5.5 [-8.1, -3.1] | 1.3e-05 (2.4e-04) | +2.7 [+0.3, +4.9] | 0.0247 (0.173) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot | 668 | 0 | 49.3 (2.4) [45.4, 53.1] | 37.0 (4.3) [33.1, 40.6] | - | -3.6 [-6.0, -1.2] | 0.00558 (0.0837) | +6.4 [+4.0, +9.0] | 6.1e-07 (1.1e-05) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF | 668 | 0 | 42.7 (21.3) [38.9, 46.4] | 14.8 (10.9) [12.1, 17.7] | 31.0 (8.7) | -10.2 [-12.9, -7.5] | 7.2e-13 (1.7e-11) | -15.7 [-18.9, -12.7] | 2.9e-23 (6.9e-22) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF near | 668 | 0 | 46.4 (15.4) [42.7, 50.1] | 13.0 (8.7) [10.5, 15.6] | 26.2 (10.3) | -6.4 [-8.8, -4.2] | 1.0e-07 (1.1e-06) | -17.5 [-21.0, -14.4] | 1.5e-27 (1.9e-26) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF far | 668 | 0 | 44.6 (31.0) [41.0, 48.5] | 18.7 (13.0) [15.7, 21.6] | 22.0 (6.9) | -8.2 [-10.8, -5.7] | 6.8e-10 (8.2e-09) | -11.8 [-14.7, -9.1] | 5.5e-17 (5.1e-16) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF, assistant | 668 | 0 | 13.5 (13.5) [10.9, 16.2] | 0.0 (0.0) [0.0, 0.0] | 83.4 (83.4) | -39.4 [-43.1, -35.5] | 3.0e-76 (3.6e-75) | -30.5 [-34.0, -27.1] | 7.8e-62 (9.3e-61) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, assistant | 668 | 0 | 44.3 (44.3) [40.6, 48.1] | 46.3 (46.3) [42.5, 50.0] | - | -8.5 [-10.9, -6.3] | 1.3e-12 (7.6e-12) | +15.7 [+12.9, +18.7] | 1.8e-28 (1.8e-27) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=0 | 668 | 0 | 53.9 (47.8) [50.1, 57.6] | 28.4 (27.1) [25.1, 31.9] | - | +1.0 [-0.7, +2.8] | 0.349 (1) | -2.1 [-4.0, -0.3] | 0.0385 (0.423) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=1 | 668 | 0 | 51.5 (40.3) [47.6, 55.2] | 31.4 (25.3) [28.0, 34.9] | - | -1.3 [-3.1, +0.4] | 0.2 (1) | +0.9 [-0.9, +2.7] | 0.441 (1) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=2 | 668 | 0 | 51.2 (15.4) [47.5, 54.9] | 34.0 (12.7) [30.4, 37.6] | - | -1.6 [-4.2, +0.7] | 0.228 (1) | +3.4 [+1.2, +5.7] | 0.00674 (0.0876) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=3 | 668 | 0 | 50.9 (9.3) [47.2, 54.8] | 35.5 (9.7) [31.9, 39.2] | - | -1.9 [-4.5, +0.4] | 0.148 (1) | +4.9 [+2.5, +7.5] | 2.2e-04 (0.00434) |
| qwen3vl-8b-instruct | Unseen | AAAAB | single | 334 | 0 | 59.6 (59.6) [54.2, 65.0] | 20.1 (20.1) [15.9, 24.3] | - | +9.9 [+5.7, +14.1] | 8.7e-06 (1.7e-04) | -15.9 [-20.4, -12.0] | 1.2e-13 (2.6e-12) |
| qwen3vl-8b-instruct | Unseen | AAAAB | default | 334 | 0 | 49.7 (49.7) [44.6, 55.1] | 35.9 (35.9) [30.8, 41.0] | - | - | - | - | - |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF incremental | 334 | 0 | 47.0 (0.3) [41.6, 52.4] | 41.0 (0.3) [35.6, 46.4] | - | -2.7 [-6.0, +0.6] | 0.163 (1) | +5.1 [+1.5, +8.7] | 0.00763 (0.0763) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot | 334 | 0 | 46.7 (0.3) [41.3, 52.1] | 41.3 (0.0) [35.9, 46.7] | - | -3.0 [-6.3, +0.3] | 0.121 (1) | +5.4 [+1.8, +9.0] | 0.0051 (0.0561) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF | 334 | 0 | 38.3 (10.8) [33.2, 43.7] | 10.8 (7.5) [7.8, 14.1] | 41.0 (0.3) | -11.4 [-15.6, -7.5] | 2.6e-07 (5.9e-06) | -25.1 [-29.9, -20.1] | 1.2e-21 (2.7e-20) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF near | 334 | 0 | 44.0 (6.6) [38.9, 49.7] | 10.2 (5.7) [7.2, 13.5] | 32.3 (4.5) | -5.7 [-9.3, -2.4] | 0.00256 (0.0103) | -25.7 [-30.5, -20.7] | 5.8e-25 (6.3e-24) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF far | 334 | 0 | 41.0 (21.6) [35.6, 45.8] | 16.5 (10.5) [12.6, 20.7] | 29.3 (0.9) | -8.7 [-12.3, -5.1] | 1.5e-05 (1.4e-04) | -19.5 [-24.3, -15.0] | 5.1e-17 (5.1e-16) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF, assistant | 334 | 0 | 13.5 (13.5) [9.9, 17.4] | 0.0 (0.0) [0.0, 0.0] | 83.5 (83.5) | -36.2 [-41.6, -31.4] | 3.7e-34 (3.3e-33) | -35.9 [-41.0, -31.1] | 1.5e-36 (1.7e-35) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, assistant | 334 | 0 | 43.7 (43.7) [38.3, 49.1] | 47.6 (47.6) [42.5, 53.0] | - | -6.0 [-9.3, -3.0] | 3.2e-04 (9.7e-04) | +11.7 [+8.1, +15.3] | 2.2e-10 (8.6e-10) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=0 | 334 | 0 | 52.7 (47.9) [47.3, 57.8] | 29.6 (29.0) [24.9, 34.7] | - | +3.0 [+0.3, +5.7] | 0.0525 (1) | -6.3 [-9.3, -3.6] | 1.9e-05 (4.3e-04) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=1 | 334 | 0 | 50.3 (40.4) [44.9, 55.7] | 33.2 (25.7) [28.1, 38.3] | - | +0.6 [-2.1, +3.3] | 0.832 (1) | -2.7 [-6.0, +0.3] | 0.122 (1) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=2 | 334 | 0 | 51.2 (17.1) [46.1, 56.6] | 35.0 (10.5) [29.9, 40.1] | - | +1.5 [-2.1, +5.1] | 0.511 (1) | -0.9 [-4.5, +2.7] | 0.743 (1) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=3 | 334 | 0 | 50.6 (11.7) [45.2, 56.0] | 36.5 (8.7) [31.4, 41.6] | - | +0.9 [-3.0, +4.5] | 0.743 (1) | +0.6 [-3.0, +3.9] | 0.875 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | single | 334 | 0 | 57.2 (57.2) [52.1, 62.9] | 22.8 (22.8) [18.3, 27.3] | - | +1.2 [-2.1, +4.8] | 0.608 (1) | -2.4 [-5.7, +0.9] | 0.215 (0.646) |
| qwen3vl-8b-instruct | Unseen | BAAAA | default | 334 | 0 | 56.0 (55.7) [50.6, 61.1] | 25.1 (25.1) [20.4, 29.9] | - | - | - | - | - |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF incremental | 334 | 1 | 47.6 (47.3) [42.2, 53.0] | 25.4 (25.4) [20.7, 30.2] | - | -8.4 [-12.0, -5.1] | 4.3e-06 (8.9e-05) | +0.3 [-2.4, +3.0] | 1 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot | 334 | 0 | 51.8 (4.5) [46.7, 57.5] | 32.6 (8.7) [27.2, 37.4] | - | -4.2 [-7.8, -0.9] | 0.0288 (0.375) | +7.5 [+4.2, +11.1] | 4.1e-05 (7.0e-04) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF | 334 | 0 | 47.0 (31.7) [41.3, 52.4] | 18.9 (14.4) [14.7, 23.4] | 21.0 (17.1) | -9.0 [-12.9, -5.7] | 1.4e-06 (3.0e-05) | -6.3 [-9.9, -3.0] | 5.1e-04 (0.00712) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF near | 334 | 0 | 48.8 (24.3) [43.4, 54.5] | 15.9 (11.7) [12.0, 19.8] | 20.1 (16.2) | -7.2 [-10.5, -4.2] | 8.4e-06 (8.4e-05) | -9.3 [-13.2, -5.7] | 5.5e-06 (2.2e-05) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF far | 334 | 0 | 48.2 (40.4) [42.8, 53.6] | 21.0 (15.6) [17.1, 25.1] | 14.7 (12.9) | -7.8 [-11.1, -4.2] | 2.4e-05 (1.9e-04) | -4.2 [-7.2, -1.2] | 0.0125 (0.0251) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF, assistant | 334 | 0 | 13.5 (13.5) [10.2, 17.4] | 0.0 (0.0) [0.0, 0.0] | 83.2 (83.2) | -42.5 [-47.6, -37.4] | 3.6e-43 (3.9e-42) | -25.1 [-29.6, -20.7] | 1.0e-25 (9.3e-25) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, assistant | 334 | 0 | 44.9 (44.9) [39.5, 50.3] | 44.9 (44.9) [39.5, 50.3] | - | -11.1 [-15.0, -7.5] | 7.8e-10 (3.9e-09) | +19.8 [+15.6, +24.3] | 4.7e-19 (3.3e-18) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=0 | 334 | 0 | 55.1 (47.6) [49.7, 60.5] | 27.2 (25.1) [22.5, 32.0] | - | -0.9 [-3.3, +1.8] | 0.648 (1) | +2.1 [+0.0, +4.5] | 0.118 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=1 | 334 | 0 | 52.7 (40.1) [47.3, 58.1] | 29.6 (24.9) [24.9, 34.7] | - | -3.3 [-5.7, -0.9] | 0.0127 (0.28) | +4.5 [+2.4, +6.9] | 6.1e-05 (0.00128) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=2 | 334 | 0 | 51.2 (13.8) [46.1, 56.6] | 32.9 (15.0) [27.8, 38.0] | - | -4.8 [-8.4, -1.5] | 0.007 (0.168) | +7.8 [+4.8, +10.8] | 8.7e-07 (2.0e-05) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=3 | 334 | 0 | 51.2 (6.9) [45.8, 56.6] | 34.4 (10.8) [29.3, 39.2] | - | -4.8 [-8.1, -1.5] | 0.007 (0.168) | +9.3 [+6.0, +12.9] | 1.2e-07 (3.0e-06) |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | single | 490 | 0 | 83.1 (83.1) [79.8, 86.1] | - | - | -2.2 [-4.1, -0.6] | 0.0266 (0.0532) | - | - |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | default | 490 | 0 | 85.3 (85.3) [82.0, 88.4] | - | - | - | - | - | - |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | TF one-shot | 490 | 0 | 95.9 (0.4) [94.1, 97.6] | - | - | +10.6 [+8.0, +13.5] | 4.4e-16 (1.8e-15) | - | - |

## Table 4, sensitivity: images where neither call for B hit the token limit

Same comparisons with default as Table 4 (tolerant, y - x in points, exact McNemar, Holm within the probe family), on the images where neither the condition's nor default's call for B was cut.

| model | split | order | condition | n img | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | Adversarial | single | 336 | +3.0 [-0.6, +6.5] | 0.143 (1) | -6.0 [-9.5, -2.4] | 0.00119 (0.0155) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF incremental | 336 | -3.0 [-6.0, +0.0] | 0.0755 (0.831) | +4.2 [+1.2, +7.1] | 0.00936 (0.0842) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot | 336 | -3.6 [-6.8, -0.3] | 0.0576 (0.691) | +6.8 [+3.3, +10.4] | 2.9e-04 (0.00441) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF | 336 | -8.6 [-12.5, -4.8] | 2.5e-05 (4.5e-04) | -11.6 [-15.8, -8.0] | 2.8e-09 (5.6e-08) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF near | 336 | -6.8 [-10.4, -3.3] | 1.9e-04 (0.00115) | -14.0 [-18.2, -9.8] | 6.4e-11 (5.1e-10) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF far | 336 | -8.9 [-12.8, -5.1] | 2.4e-05 (1.9e-04) | -12.2 [-16.1, -8.3] | 8.2e-10 (5.8e-09) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF, assistant | 336 | -43.5 [-49.1, -38.1] | 1.6e-41 (1.6e-40) | -22.6 [-27.1, -18.2] | 2.6e-23 (2.1e-22) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, assistant | 336 | -7.1 [-10.4, -4.2] | 3.9e-05 (1.5e-04) | +12.2 [+8.6, +15.8] | 5.9e-11 (2.9e-10) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=0 | 336 | +1.2 [-1.2, +3.6] | 0.481 (1) | -2.1 [-4.5, +0.0] | 0.118 (1) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=1 | 336 | -2.1 [-5.1, +1.2] | 0.265 (1) | +4.2 [+1.2, +7.1] | 0.0125 (0.15) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=2 | 336 | -1.8 [-5.1, +1.5] | 0.392 (1) | +5.4 [+2.1, +8.3] | 0.0021 (0.0315) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=3 | 336 | -2.4 [-6.0, +1.2] | 0.256 (1) | +5.7 [+2.4, +9.2] | 0.00256 (0.0359) |
| qwen3vl-8b-instruct | Seen | AAAAB | single | 168 | +5.4 [+0.6, +10.7] | 0.0784 (0.831) | -11.9 [-17.3, -6.5] | 8.8e-05 (0.00141) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF incremental | 168 | -4.2 [-9.5, +0.6] | 0.167 (1) | +6.0 [+0.6, +11.3] | 0.0525 (0.315) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot | 168 | -4.2 [-9.5, +0.6] | 0.167 (1) | +6.0 [+0.6, +11.3] | 0.0525 (0.315) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF | 168 | -11.3 [-17.9, -5.4] | 8.8e-04 (0.014) | -17.3 [-23.8, -11.3] | 3.0e-08 (5.7e-07) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF near | 168 | -7.1 [-12.5, -1.8] | 0.0227 (0.0453) | -19.6 [-26.2, -13.7] | 2.1e-09 (1.3e-08) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF far | 168 | -13.1 [-19.6, -6.5] | 2.0e-04 (0.00115) | -19.6 [-26.2, -13.1] | 2.1e-09 (1.3e-08) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF, assistant | 168 | -40.5 [-48.2, -32.1] | 1.1e-18 (7.8e-18) | -26.8 [-33.3, -20.2] | 5.7e-14 (3.4e-13) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, assistant | 168 | -7.1 [-11.9, -2.4] | 0.00754 (0.00836) | +9.5 [+4.8, +14.9] | 4.0e-04 (4.0e-04) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=0 | 168 | +3.6 [-0.0, +7.7] | 0.146 (1) | -6.5 [-10.7, -3.0] | 9.8e-04 (0.0166) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=1 | 168 | +0.0 [-5.4, +4.8] | 1 (1) | +0.6 [-4.2, +4.8] | 1 (1) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=2 | 168 | -2.4 [-7.7, +3.0] | 0.503 (1) | +3.6 [-1.2, +8.3] | 0.238 (1) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=3 | 168 | -1.8 [-7.2, +3.6] | 0.678 (1) | +2.4 [-3.0, +7.2] | 0.503 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | single | 168 | +0.6 [-4.2, +5.4] | 1 (1) | +0.0 [-3.6, +3.6] | 1 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF incremental | 168 | -1.8 [-4.8, +1.2] | 0.453 (1) | +2.4 [+0.6, +4.8] | 0.125 (0.5) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot | 168 | -3.0 [-7.1, +1.2] | 0.302 (1) | +7.7 [+3.6, +13.1] | 0.00235 (0.0282) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF | 168 | -6.0 [-10.7, -1.8] | 0.0213 (0.298) | -6.0 [-10.7, -1.2] | 0.0213 (0.17) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF near | 168 | -6.5 [-10.7, -3.0] | 0.00342 (0.0103) | -8.3 [-13.7, -3.6] | 0.00434 (0.013) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF far | 168 | -4.8 [-9.5, +0.0] | 0.0768 (0.0768) | -4.8 [-9.5, -0.6] | 0.0574 (0.0574) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF, assistant | 168 | -46.4 [-54.2, -39.3] | 6.6e-24 (5.3e-23) | -18.5 [-25.0, -12.5] | 9.3e-10 (2.8e-09) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, assistant | 168 | -7.1 [-11.9, -3.0] | 0.00418 (0.00836) | +14.9 [+9.5, +20.2] | 6.0e-08 (1.2e-07) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=0 | 168 | -1.2 [-4.2, +1.2] | 0.688 (1) | +2.4 [+0.6, +4.8] | 0.125 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=1 | 168 | -4.2 [-8.3, -0.6] | 0.0654 (1) | +7.7 [+4.2, +11.9] | 2.4e-04 (0.00464) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=2 | 168 | -1.2 [-5.4, +3.0] | 0.791 (1) | +7.1 [+3.0, +11.3] | 0.00183 (0.0293) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=3 | 168 | -3.0 [-7.7, +1.2] | 0.302 (1) | +8.9 [+4.8, +13.7] | 2.7e-04 (0.00494) |
| qwen3vl-8b-instruct | Seen | Homogeneous control | single | 400 | -2.2 [-4.2, -0.5] | 0.0352 (0.0532) | - | - |
| qwen3vl-8b-instruct | Seen | Homogeneous control | TF one-shot | 400 | +5.0 [+3.0, +7.2] | 1.9e-06 (5.7e-06) | - | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | single | 668 | +5.5 [+2.8, +8.2] | 1.1e-04 (0.00187) | -9.1 [-12.0, -6.4] | 5.5e-11 (1.2e-09) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF incremental | 667 | -5.4 [-7.9, -2.8] | 1.9e-05 (3.6e-04) | +2.7 [+0.4, +4.8] | 0.0247 (0.173) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot | 668 | -3.6 [-6.0, -1.2] | 0.00558 (0.0837) | +6.4 [+4.0, +9.0] | 6.1e-07 (1.1e-05) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF | 668 | -10.2 [-12.9, -7.5] | 7.2e-13 (1.7e-11) | -15.7 [-18.9, -12.7] | 2.9e-23 (6.9e-22) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF near | 668 | -6.4 [-8.8, -4.2] | 1.0e-07 (1.1e-06) | -17.5 [-21.0, -14.4] | 1.5e-27 (1.9e-26) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF far | 668 | -8.2 [-10.8, -5.7] | 6.8e-10 (8.2e-09) | -11.8 [-14.7, -9.1] | 5.5e-17 (5.1e-16) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF, assistant | 668 | -39.4 [-43.1, -35.5] | 3.0e-76 (3.6e-75) | -30.5 [-34.0, -27.1] | 7.8e-62 (9.3e-61) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, assistant | 668 | -8.5 [-10.9, -6.3] | 1.3e-12 (7.6e-12) | +15.7 [+12.9, +18.7] | 1.8e-28 (1.8e-27) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=0 | 668 | +1.0 [-0.7, +2.8] | 0.349 (1) | -2.1 [-4.0, -0.3] | 0.0385 (0.423) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=1 | 668 | -1.3 [-3.1, +0.4] | 0.2 (1) | +0.9 [-0.9, +2.7] | 0.441 (1) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=2 | 668 | -1.6 [-4.2, +0.7] | 0.228 (1) | +3.4 [+1.2, +5.7] | 0.00674 (0.0876) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=3 | 668 | -1.9 [-4.5, +0.4] | 0.148 (1) | +4.9 [+2.5, +7.5] | 2.2e-04 (0.00434) |
| qwen3vl-8b-instruct | Unseen | AAAAB | single | 334 | +9.9 [+5.7, +14.1] | 8.7e-06 (1.7e-04) | -15.9 [-20.4, -12.0] | 1.2e-13 (2.6e-12) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF incremental | 334 | -2.7 [-6.0, +0.6] | 0.163 (1) | +5.1 [+1.5, +8.7] | 0.00763 (0.0763) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot | 334 | -3.0 [-6.3, +0.3] | 0.121 (1) | +5.4 [+1.8, +9.0] | 0.0051 (0.0561) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF | 334 | -11.4 [-15.6, -7.5] | 2.6e-07 (5.9e-06) | -25.1 [-29.9, -20.1] | 1.2e-21 (2.7e-20) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF near | 334 | -5.7 [-9.3, -2.4] | 0.00256 (0.0103) | -25.7 [-30.5, -20.7] | 5.8e-25 (6.3e-24) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF far | 334 | -8.7 [-12.3, -5.1] | 1.5e-05 (1.4e-04) | -19.5 [-24.3, -15.0] | 5.1e-17 (5.1e-16) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF, assistant | 334 | -36.2 [-41.6, -31.4] | 3.7e-34 (3.3e-33) | -35.9 [-41.0, -31.1] | 1.5e-36 (1.7e-35) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, assistant | 334 | -6.0 [-9.3, -3.0] | 3.2e-04 (9.7e-04) | +11.7 [+8.1, +15.3] | 2.2e-10 (8.6e-10) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=0 | 334 | +3.0 [+0.3, +5.7] | 0.0525 (1) | -6.3 [-9.3, -3.6] | 1.9e-05 (4.3e-04) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=1 | 334 | +0.6 [-2.1, +3.3] | 0.832 (1) | -2.7 [-6.0, +0.3] | 0.122 (1) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=2 | 334 | +1.5 [-2.1, +5.1] | 0.511 (1) | -0.9 [-4.5, +2.7] | 0.743 (1) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=3 | 334 | +0.9 [-3.0, +4.5] | 0.743 (1) | +0.6 [-3.0, +3.9] | 0.875 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | single | 334 | +1.2 [-2.1, +4.8] | 0.608 (1) | -2.4 [-5.7, +0.9] | 0.215 (0.646) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF incremental | 333 | -8.1 [-11.7, -4.8] | 7.4e-06 (1.6e-04) | +0.3 [-2.4, +3.0] | 1 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot | 334 | -4.2 [-7.8, -0.9] | 0.0288 (0.375) | +7.5 [+4.2, +11.1] | 4.1e-05 (7.0e-04) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF | 334 | -9.0 [-12.9, -5.7] | 1.4e-06 (3.0e-05) | -6.3 [-9.9, -3.0] | 5.1e-04 (0.00712) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF near | 334 | -7.2 [-10.5, -4.2] | 8.4e-06 (8.4e-05) | -9.3 [-13.2, -5.7] | 5.5e-06 (2.2e-05) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF far | 334 | -7.8 [-11.1, -4.2] | 2.4e-05 (1.9e-04) | -4.2 [-7.2, -1.2] | 0.0125 (0.0251) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF, assistant | 334 | -42.5 [-47.6, -37.4] | 3.6e-43 (3.9e-42) | -25.1 [-29.6, -20.7] | 1.0e-25 (9.3e-25) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, assistant | 334 | -11.1 [-15.0, -7.5] | 7.8e-10 (3.9e-09) | +19.8 [+15.6, +24.3] | 4.7e-19 (3.3e-18) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=0 | 334 | -0.9 [-3.3, +1.8] | 0.648 (1) | +2.1 [+0.0, +4.5] | 0.118 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=1 | 334 | -3.3 [-5.7, -0.9] | 0.0127 (0.28) | +4.5 [+2.4, +6.9] | 6.1e-05 (0.00128) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=2 | 334 | -4.8 [-8.4, -1.5] | 0.007 (0.168) | +7.8 [+4.8, +10.8] | 8.7e-07 (2.0e-05) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=3 | 334 | -4.8 [-8.1, -1.5] | 0.007 (0.168) | +9.3 [+6.0, +12.9] | 1.2e-07 (3.0e-06) |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | single | 490 | -2.2 [-4.1, -0.6] | 0.0266 (0.0532) | - | - |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | TF one-shot | 490 | +10.6 [+8.0, +13.5] | 4.4e-16 (1.8e-15) | - | - |

## Table 4, against Single-object (B asked alone)

Same images, tolerant, y - x in points, exact McNemar, Holm over the model's comparisons with Single-object in the same probe family (default counts as core). Single-object asks one box per turn with the official single-object prompt, so this gap holds both the multi-object format (default) and the given labels.

| model | split | order | condition | n img | acc vs single [CI] | p (Holm) | B=A vs single [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | Adversarial | default | 336 | -3.0 [-6.5, +0.6] | 0.143 (0.717) | +6.0 [+2.4, +9.5] | 0.00119 (0.0119) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF incremental | 336 | -6.0 [-9.8, -2.4] | 0.00222 (0.02) | +10.1 [+6.5, +14.0] | 1.4e-07 (2.1e-06) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot | 336 | -6.5 [-10.1, -3.3] | 3.1e-04 (0.00375) | +12.8 [+8.9, +16.7] | 7.0e-11 (1.3e-09) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF | 336 | -11.6 [-15.8, -7.4] | 8.1e-08 (1.5e-06) | -5.7 [-9.5, -2.1] | 0.00432 (0.0346) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF near | 336 | -9.8 [-14.0, -5.6] | 1.9e-05 (7.7e-05) | -8.0 [-12.2, -4.5] | 9.8e-05 (9.8e-04) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF far | 336 | -11.9 [-16.4, -7.4] | 1.6e-07 (1.3e-06) | -6.2 [-9.8, -3.0] | 7.5e-04 (0.00678) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF, assistant | 336 | -46.4 [-51.5, -40.8] | 2.2e-41 (2.0e-40) | -16.7 [-20.8, -12.5] | 2.8e-17 (1.7e-16) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, assistant | 336 | -10.1 [-14.3, -6.0] | 2.0e-06 (6.1e-06) | +18.2 [+14.3, +22.6] | 6.8e-16 (3.4e-15) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=0 | 336 | -1.8 [-5.1, +1.5] | 0.377 (1) | +3.9 [+0.9, +6.8] | 0.0192 (0.0575) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=1 | 336 | -5.1 [-8.6, -1.5] | 0.00763 (0.0916) | +10.1 [+6.5, +13.7] | 1.9e-08 (2.7e-07) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=2 | 336 | -4.8 [-8.0, -1.5] | 0.0113 (0.125) | +11.3 [+7.7, +15.2] | 5.1e-09 (8.2e-08) |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=3 | 336 | -5.4 [-9.2, -1.8] | 0.00643 (0.0835) | +11.6 [+7.7, +15.2] | 8.7e-10 (1.6e-08) |
| qwen3vl-8b-instruct | Seen | AAAAB | default | 168 | -5.4 [-10.7, -0.6] | 0.0784 (0.47) | +11.9 [+6.5, +17.9] | 8.8e-05 (9.7e-04) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF incremental | 168 | -9.5 [-14.9, -4.8] | 4.0e-04 (0.00443) | +17.9 [+11.9, +23.8] | 1.5e-08 (2.6e-07) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot | 168 | -9.5 [-14.9, -4.8] | 4.0e-04 (0.00443) | +17.9 [+11.9, +23.8] | 1.5e-08 (2.6e-07) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF | 168 | -16.7 [-22.6, -10.1] | 7.7e-07 (1.2e-05) | -5.4 [-11.3, +0.6] | 0.108 (0.539) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF near | 168 | -12.5 [-19.0, -6.0] | 5.1e-04 (0.00152) | -7.7 [-13.7, -2.4] | 0.0106 (0.0637) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF far | 168 | -18.5 [-25.6, -11.9] | 3.4e-07 (2.3e-06) | -7.7 [-13.1, -2.4] | 0.0106 (0.0637) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF, assistant | 168 | -45.8 [-54.2, -37.5] | 2.0e-20 (1.4e-19) | -14.9 [-20.2, -9.5] | 6.0e-08 (1.2e-07) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, assistant | 168 | -12.5 [-18.5, -7.1] | 4.9e-05 (9.8e-05) | +21.4 [+15.5, +28.6] | 2.8e-10 (1.1e-09) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=0 | 168 | -1.8 [-6.0, +2.4] | 0.581 (1) | +5.4 [+1.2, +9.5] | 0.0352 (0.0703) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=1 | 168 | -5.4 [-10.1, -0.6] | 0.049 (0.392) | +12.5 [+7.1, +17.9] | 5.7e-06 (5.1e-05) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=2 | 168 | -7.7 [-12.5, -3.0] | 0.00443 (0.0664) | +15.5 [+9.5, +22.0] | 2.2e-07 (2.6e-06) |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=3 | 168 | -7.1 [-12.5, -1.8] | 0.0118 (0.125) | +14.3 [+8.9, +19.6] | 8.0e-07 (8.9e-06) |
| qwen3vl-8b-instruct | Seen | BAAAA | default | 168 | -0.6 [-5.4, +4.2] | 1 (1) | +0.0 [-3.6, +3.6] | 1 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF incremental | 168 | -2.4 [-7.7, +3.0] | 0.503 (1) | +2.4 [-1.8, +6.5] | 0.388 (0.775) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot | 168 | -3.6 [-8.3, +1.2] | 0.21 (0.84) | +7.7 [+3.0, +12.5] | 0.00235 (0.0211) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF | 168 | -6.5 [-11.9, -1.2] | 0.0266 (0.186) | -6.0 [-10.7, -1.2] | 0.0213 (0.149) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF near | 168 | -7.1 [-12.5, -1.2] | 0.0227 (0.0453) | -8.3 [-14.3, -3.0] | 0.00661 (0.0463) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF far | 168 | -5.4 [-10.7, +0.0] | 0.0784 (0.0784) | -4.8 [-9.5, -0.6] | 0.0574 (0.229) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF, assistant | 168 | -47.0 [-54.2, -39.3] | 7.2e-22 (5.8e-21) | -18.5 [-24.4, -13.1] | 9.3e-10 (2.8e-09) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, assistant | 168 | -7.7 [-13.1, -1.8] | 0.0146 (0.0146) | +14.9 [+9.5, +20.8] | 1.6e-06 (1.6e-06) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=0 | 168 | -1.8 [-6.6, +3.0] | 0.648 (1) | +2.4 [-1.8, +6.5] | 0.388 (0.388) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=1 | 168 | -4.8 [-10.1, +0.6] | 0.115 (0.807) | +7.7 [+3.0, +12.5] | 0.00235 (0.0141) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=2 | 168 | -1.8 [-6.5, +3.0] | 0.629 (1) | +7.1 [+2.4, +11.9] | 0.00754 (0.0302) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=3 | 168 | -3.6 [-8.9, +1.2] | 0.263 (1) | +8.9 [+4.2, +14.3] | 7.3e-04 (0.0051) |
| qwen3vl-8b-instruct | Seen | Homogeneous control | default | 400 | +2.2 [+0.5, +4.0] | 0.0352 (0.0532) | - | - |
| qwen3vl-8b-instruct | Seen | Homogeneous control | TF one-shot | 400 | +7.2 [+4.8, +9.8] | 3.7e-09 (1.1e-08) | - | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | default | 668 | -5.5 [-8.1, -2.8] | 1.1e-04 (0.00143) | +9.1 [+6.4, +11.8] | 5.5e-11 (1.0e-09) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF incremental | 668 | -11.1 [-14.1, -8.2] | 1.2e-12 (2.6e-11) | +11.8 [+9.1, +14.8] | 3.5e-16 (7.3e-15) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot | 668 | -9.1 [-12.0, -6.1] | 7.1e-09 (1.5e-07) | +15.6 [+12.7, +18.7] | 4.3e-22 (1.0e-20) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF | 668 | -15.7 [-18.9, -12.4] | 6.4e-22 (1.5e-20) | -6.6 [-9.3, -3.9] | 6.3e-06 (8.9e-05) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF near | 668 | -12.0 [-14.8, -9.3] | 2.0e-16 (2.1e-15) | -8.4 [-11.2, -5.5] | 1.1e-08 (1.3e-07) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF far | 668 | -13.8 [-17.1, -10.8] | 1.9e-19 (2.2e-18) | -2.7 [-5.5, +0.1] | 0.0854 (0.256) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF, assistant | 668 | -44.9 [-48.7, -41.2] | 7.4e-89 (8.9e-88) | -21.4 [-24.6, -18.3] | 1.8e-43 (2.0e-42) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, assistant | 668 | -14.1 [-17.1, -10.9] | 4.3e-18 (2.6e-17) | +24.9 [+21.7, +28.3] | 2.9e-44 (3.4e-43) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=0 | 668 | -4.5 [-7.0, -1.9] | 5.3e-04 (0.00963) | +7.0 [+4.8, +9.3] | 2.0e-09 (3.5e-08) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=1 | 668 | -6.9 [-9.6, -4.2] | 2.2e-06 (4.9e-05) | +10.0 [+7.5, +12.7] | 5.9e-14 (1.2e-12) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=2 | 668 | -7.2 [-10.2, -4.2] | 2.1e-06 (4.9e-05) | +12.6 [+9.6, +15.6] | 2.0e-17 (4.5e-16) |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=3 | 668 | -7.5 [-10.5, -4.9] | 2.3e-07 (5.4e-06) | +14.1 [+11.1, +16.9] | 2.3e-21 (5.6e-20) |
| qwen3vl-8b-instruct | Unseen | AAAAB | default | 334 | -9.9 [-14.4, -5.7] | 8.7e-06 (1.3e-04) | +15.9 [+12.0, +20.4] | 1.2e-13 (2.4e-12) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF incremental | 334 | -12.6 [-17.1, -8.1] | 5.7e-08 (1.1e-06) | +21.0 [+16.5, +25.7] | 2.9e-19 (6.5e-18) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot | 334 | -12.9 [-17.1, -8.7] | 3.4e-08 (6.8e-07) | +21.3 [+17.1, +25.4] | 1.5e-19 (3.5e-18) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF | 334 | -21.3 [-26.0, -16.5] | 8.4e-16 (1.9e-14) | -9.3 [-13.8, -5.1] | 4.7e-05 (5.7e-04) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF near | 334 | -15.6 [-20.1, -11.1] | 9.0e-12 (8.1e-11) | -9.9 [-14.1, -6.0] | 3.4e-06 (3.7e-05) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF far | 334 | -18.6 [-23.1, -14.1] | 2.1e-14 (2.1e-13) | -3.6 [-8.1, +0.6] | 0.141 (0.282) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF, assistant | 334 | -46.1 [-51.2, -40.7] | 3.4e-45 (3.8e-44) | -20.1 [-24.6, -15.9] | 1.4e-20 (1.1e-19) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, assistant | 334 | -15.9 [-20.4, -11.1] | 7.3e-11 (3.7e-10) | +27.5 [+22.8, +32.6] | 1.2e-25 (1.2e-24) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=0 | 334 | -6.9 [-10.8, -3.3] | 6.1e-04 (0.0103) | +9.6 [+6.0, +13.2] | 6.7e-08 (8.7e-07) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=1 | 334 | -9.3 [-13.5, -5.1] | 2.2e-05 (4.7e-04) | +13.2 [+9.3, +17.1] | 3.7e-11 (7.0e-10) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=2 | 334 | -8.4 [-12.9, -4.2] | 2.3e-04 (0.00445) | +15.0 [+11.1, +19.2] | 3.2e-12 (6.3e-11) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=3 | 334 | -9.0 [-13.2, -4.8] | 5.2e-05 (0.00104) | +16.5 [+12.3, +21.0] | 3.3e-14 (7.2e-13) |
| qwen3vl-8b-instruct | Unseen | BAAAA | default | 334 | -1.2 [-4.8, +2.4] | 0.608 (1) | +2.4 [-0.9, +6.0] | 0.215 (0.646) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF incremental | 334 | -9.6 [-13.8, -5.7] | 9.1e-06 (1.3e-04) | +2.7 [-0.6, +5.7] | 0.136 (0.544) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot | 334 | -5.4 [-9.3, -1.5] | 0.0153 (0.123) | +9.9 [+5.7, +13.8] | 8.7e-06 (1.1e-04) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF | 334 | -10.2 [-14.1, -6.3] | 3.1e-07 (5.3e-06) | -3.9 [-7.5, -0.6] | 0.047 (0.282) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF near | 334 | -8.4 [-12.0, -5.1] | 8.4e-06 (4.2e-05) | -6.9 [-10.8, -3.0] | 0.00109 (0.00871) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF far | 334 | -9.0 [-12.9, -5.4] | 2.8e-06 (1.7e-05) | -1.8 [-5.7, +2.1] | 0.441 (0.441) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF, assistant | 334 | -43.7 [-49.1, -38.3] | 2.2e-44 (2.2e-43) | -22.8 [-27.2, -18.0] | 2.6e-23 (2.4e-22) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, assistant | 334 | -12.3 [-16.8, -8.1] | 2.7e-08 (1.1e-07) | +22.2 [+17.7, +26.9] | 1.4e-19 (9.9e-19) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=0 | 334 | -2.1 [-5.1, +0.9] | 0.265 (1) | +4.5 [+1.5, +7.2] | 0.00592 (0.0296) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=1 | 334 | -4.5 [-8.1, -0.9] | 0.0275 (0.248) | +6.9 [+3.6, +10.5] | 1.9e-04 (0.00153) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=2 | 334 | -6.0 [-9.9, -2.1] | 0.00453 (0.0664) | +10.2 [+6.3, +14.1] | 1.2e-06 (1.2e-05) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=3 | 334 | -6.0 [-9.6, -2.7] | 0.00222 (0.0355) | +11.7 [+7.5, +15.9] | 1.8e-08 (2.7e-07) |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | default | 490 | +2.2 [+0.4, +4.3] | 0.0266 (0.0532) | - | - |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | TF one-shot | 490 | +12.9 [+10.2, +15.9] | 2.2e-19 (8.7e-19) | - | - |

## Assistant-turn prefill: the forced line, then the model's own re-check (%)

first = the label written right after the prefill (the one Table 4 uses); kept writing = the model went on after it (typically "Wait, no, that's wrong" and a re-check); restarted = wrote no label after the forced "objK:" and began its own five-label list on a new line (counted in kept writing; first counts as wrong and not A); final = obj K's last "objK: <class>" in the answer (= first when it stopped); unresolved = kept writing but gave no final label for B, or hit the token limit. cut = thinking never closed. All over n img, tolerant.

| model | split | order | condition | n img | cut | first: B acc | first: B=A | first: B=C | kept writing | restarted | final: B acc | final: B=A | final: B=C | unresolved |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | Adversarial | CF, assistant | 336 | 0 | 16.1 | 0.0 | 80.4 | 0.0 | 0.0 | 16.1 | 0.0 | 80.4 | 0.0 |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, assistant | 336 | 0 | 52.4 | 34.8 | - | 0.0 | 0.0 | 52.4 | 34.8 | - | 0.0 |
| qwen3vl-8b-instruct | Seen | AAAAB | CF, assistant | 168 | 0 | 17.3 | 0.0 | 79.2 | 0.0 | 0.0 | 17.3 | 0.0 | 79.2 | 0.0 |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, assistant | 168 | 0 | 50.6 | 36.3 | - | 0.0 | 0.0 | 50.6 | 36.3 | - | 0.0 |
| qwen3vl-8b-instruct | Seen | BAAAA | CF, assistant | 168 | 0 | 14.9 | 0.0 | 81.5 | 0.0 | 0.0 | 14.9 | 0.0 | 81.5 | 0.0 |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, assistant | 168 | 0 | 54.2 | 33.3 | - | 0.0 | 0.0 | 54.2 | 33.3 | - | 0.0 |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF, assistant | 668 | 0 | 13.5 | 0.0 | 83.4 | 0.0 | 0.0 | 13.5 | 0.0 | 83.4 | 0.0 |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, assistant | 668 | 0 | 44.3 | 46.3 | - | 0.0 | 0.0 | 44.3 | 46.3 | - | 0.0 |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF, assistant | 334 | 0 | 13.5 | 0.0 | 83.5 | 0.0 | 0.0 | 13.5 | 0.0 | 83.5 | 0.0 |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, assistant | 334 | 0 | 43.7 | 47.6 | - | 0.0 | 0.0 | 43.7 | 47.6 | - | 0.0 |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF, assistant | 334 | 0 | 13.5 | 0.0 | 83.2 | 0.0 | 0.0 | 13.5 | 0.0 | 83.2 | 0.0 |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, assistant | 334 | 0 | 44.9 | 44.9 | - | 0.0 | 0.0 | 44.9 | 44.9 | - | 0.0 |

## What the answer does with the given boxes (one-shot, labels in the user turn; %)

Over answered rows (calls for B not cut), tolerant parse, last objK: mention per box. B read before objK: = the answer has no objK: for B but writes B's label first and then other boxes (it continues the prompt's last "objK:"), and B's label was read from that first segment (see asked_label); writes all 5 = a label for every box, i.e. the model rewrites the list instead of answering only B; keeps given = every given box keeps its given label; given boxes = A = every given box is labelled A; C kept = C stays on at least one given box (CF only). '-' = no label given (n = 0).

| model | split | order | condition | n answered | B read before objK: | writes all 5 | keeps given | given boxes = A | C kept |
|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot | 336 | 0.0 | 1.2 | 0.9 | 0.9 | - |
| qwen3vl-8b-instruct | Seen | Adversarial | CF | 336 | 0.0 | 53.0 | 8.3 | 35.1 | 8.9 |
| qwen3vl-8b-instruct | Seen | Adversarial | CF near | 336 | 0.0 | 30.7 | 5.1 | 20.2 | 5.4 |
| qwen3vl-8b-instruct | Seen | Adversarial | CF far | 336 | 0.0 | 46.7 | 9.5 | 28.6 | 9.8 |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=0 | 336 | 0.3 | - | - | - | - |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=1 | 336 | 6.8 | 80.7 | 80.7 | 80.7 | - |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=2 | 336 | 33.9 | 35.4 | 33.3 | 33.3 | - |
| qwen3vl-8b-instruct | Seen | Adversarial | TF one-shot, given=3 | 336 | 51.5 | 18.2 | 17.0 | 17.0 | - |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot | 168 | 0.0 | 0.0 | 0.0 | 0.0 | - |
| qwen3vl-8b-instruct | Seen | AAAAB | CF | 168 | 0.0 | 31.5 | 1.2 | 22.0 | 1.8 |
| qwen3vl-8b-instruct | Seen | AAAAB | CF near | 168 | 0.0 | 19.6 | 0.6 | 15.5 | 0.6 |
| qwen3vl-8b-instruct | Seen | AAAAB | CF far | 168 | 0.0 | 26.8 | 4.2 | 18.5 | 4.8 |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=0 | 168 | 0.0 | - | - | - | - |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=1 | 168 | 4.2 | 70.8 | 73.2 | 73.2 | - |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=2 | 168 | 11.9 | 28.0 | 26.2 | 26.2 | - |
| qwen3vl-8b-instruct | Seen | AAAAB | TF one-shot, given=3 | 168 | 19.0 | 20.2 | 19.0 | 19.0 | - |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot | 168 | 0.0 | 2.4 | 1.8 | 1.8 | - |
| qwen3vl-8b-instruct | Seen | BAAAA | CF | 168 | 0.0 | 74.4 | 15.5 | 48.2 | 16.1 |
| qwen3vl-8b-instruct | Seen | BAAAA | CF near | 168 | 0.0 | 41.7 | 9.5 | 25.0 | 10.1 |
| qwen3vl-8b-instruct | Seen | BAAAA | CF far | 168 | 0.0 | 66.7 | 14.9 | 38.7 | 14.9 |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=0 | 168 | 0.6 | - | - | - | - |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=1 | 168 | 9.5 | 90.5 | 88.1 | 88.1 | - |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=2 | 168 | 56.0 | 42.9 | 40.5 | 40.5 | - |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot, given=3 | 168 | 83.9 | 16.1 | 14.9 | 14.9 | - |
| qwen3vl-8b-instruct | Seen | Homogeneous control | TF one-shot | 400 | 0.0 | 0.0 | 0.0 | 0.0 | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot | 668 | 0.0 | 2.8 | 0.9 | 0.9 | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF | 668 | 0.0 | 41.8 | 9.3 | 22.6 | 9.3 |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF near | 668 | 0.0 | 30.4 | 6.0 | 15.3 | 6.3 |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF far | 668 | 0.0 | 57.2 | 6.4 | 32.9 | 6.7 |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=0 | 668 | 5.2 | - | - | - | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=1 | 668 | 11.4 | 76.2 | 75.6 | 75.6 | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=2 | 668 | 40.3 | 34.0 | 30.8 | 30.8 | - |
| qwen3vl-8b-instruct | Unseen | Adversarial | TF one-shot, given=3 | 668 | 49.6 | 23.5 | 19.2 | 19.2 | - |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot | 334 | 0.0 | 0.6 | 0.0 | 0.0 | - |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF | 334 | 0.0 | 24.0 | 0.3 | 16.2 | 0.3 |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF near | 334 | 0.0 | 20.4 | 3.0 | 10.2 | 3.0 |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF far | 334 | 0.0 | 42.2 | 1.5 | 25.7 | 1.8 |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=0 | 334 | 0.6 | - | - | - | - |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=1 | 334 | 4.2 | 72.8 | 75.7 | 75.7 | - |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=2 | 334 | 20.7 | 29.3 | 29.0 | 29.0 | - |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot, given=3 | 334 | 23.1 | 23.7 | 19.2 | 19.2 | - |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot | 334 | 0.0 | 5.1 | 1.8 | 1.8 | - |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF | 334 | 0.0 | 59.6 | 18.3 | 29.0 | 18.3 |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF near | 334 | 0.0 | 40.4 | 9.0 | 20.4 | 9.6 |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF far | 334 | 0.0 | 72.2 | 11.4 | 40.1 | 11.7 |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=0 | 334 | 9.9 | - | - | - | - |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=1 | 334 | 18.6 | 79.6 | 75.4 | 75.4 | - |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=2 | 334 | 59.9 | 38.6 | 32.6 | 32.6 | - |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot, given=3 | 334 | 76.0 | 23.4 | 19.2 | 19.2 | - |
| qwen3vl-8b-instruct | Unseen | Homogeneous control | TF one-shot | 490 | 0.0 | 1.2 | 0.4 | 0.4 | - |

## C near / far: does a C closer to A get copied more?

Paired on the same images, y - x in points, tolerant; B=C = B given the injected class of that condition. Exact McNemar, Holm per model and outcome over these comparisons.

| model | split | order | x | y | n img | B=C y - x [CI] | p (Holm) | B=A y - x [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | Adversarial | CF | CF near | 336 | +0.9 [-3.9, +6.0] | 0.818 (1) | -2.4 [-6.0, +1.2] | 0.256 (1) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF | CF far | 336 | +0.0 [-5.1, +4.8] | 1 (1) | -0.6 [-3.6, +2.4] | 0.851 (1) |
| qwen3vl-8b-instruct | Seen | Adversarial | CF near | CF far | 336 | -0.9 [-6.0, +4.2] | 0.813 (1) | +1.8 [-1.5, +5.1] | 0.377 (1) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF | CF near | 168 | -3.0 [-10.7, +4.8] | 0.56 (1) | -2.4 [-7.7, +2.4] | 0.481 (1) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF | CF far | 168 | +5.4 [-2.4, +13.1] | 0.233 (1) | -2.4 [-6.5, +1.8] | 0.388 (1) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF near | CF far | 168 | +8.3 [+1.2, +14.9] | 0.0336 (0.336) | +0.0 [-4.2, +4.2] | 1 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF | CF near | 168 | +4.8 [-0.6, +11.3] | 0.185 (1) | -2.4 [-7.8, +3.0] | 0.503 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF | CF far | 168 | -5.4 [-11.3, +0.0] | 0.108 (0.97) | +1.2 [-3.6, +6.0] | 0.804 (1) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF near | CF far | 168 | -10.1 [-16.7, -3.6] | 0.00455 (0.0683) | +3.6 [-1.8, +8.3] | 0.263 (1) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF | CF near | 668 | -4.8 [-8.2, -1.3] | 0.00808 (0.105) | -1.8 [-4.2, +0.6] | 0.182 (1) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF | CF far | 668 | -9.0 [-12.4, -5.4] | 1.1e-06 (1.9e-05) | +3.9 [+1.5, +6.4] | 0.00294 (0.0471) |
| qwen3vl-8b-instruct | Unseen | Adversarial | CF near | CF far | 668 | -4.2 [-7.5, -0.7] | 0.0203 (0.243) | +5.7 [+3.1, +7.9] | 1.1e-05 (2.0e-04) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF | CF near | 334 | -8.7 [-13.8, -3.3] | 0.00147 (0.0235) | -0.6 [-4.2, +2.7] | 0.86 (1) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF | CF far | 334 | -11.7 [-17.1, -6.0] | 7.8e-05 (0.00133) | +5.7 [+1.8, +9.3] | 0.00661 (0.0925) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF near | CF far | 334 | -3.0 [-8.1, +2.1] | 0.314 (1) | +6.3 [+2.7, +10.2] | 0.00145 (0.0247) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF | CF near | 334 | -0.9 [-5.4, +3.6] | 0.795 (1) | -3.0 [-6.6, +0.6] | 0.132 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF | CF far | 334 | -6.3 [-10.8, -2.1] | 0.00646 (0.0904) | +2.1 [-0.9, +5.1] | 0.248 (1) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF near | CF far | 334 | -5.4 [-9.9, -1.2] | 0.0222 (0.245) | +5.1 [+1.8, +8.7] | 0.00455 (0.0683) |

## Figure 4 data: dose-response (tolerant, %)

| model | split | probe | order | labels given | n img | B acc [95% CI] | B=A [95% CI] | B=C [95% CI] |
|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | TF one-shot | Adversarial | 0 | 336 | 60.7 [55.4, 66.1] | 20.5 [16.1, 25.0] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | Adversarial | 1 | 336 | 57.4 [52.1, 62.5] | 26.8 [22.3, 31.5] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | Adversarial | 2 | 336 | 57.7 [52.4, 62.8] | 28.0 [23.2, 32.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | Adversarial | 3 | 336 | 57.1 [52.1, 62.2] | 28.3 [23.5, 33.0] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | Adversarial | 4 | 336 | 56.0 [50.9, 61.0] | 29.5 [24.7, 34.2] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | AAAAB | 0 | 168 | 61.3 [54.2, 68.5] | 20.2 [14.3, 26.8] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | AAAAB | 1 | 168 | 57.7 [50.0, 64.9] | 27.4 [20.8, 33.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | AAAAB | 2 | 168 | 55.4 [47.6, 62.5] | 30.4 [23.8, 36.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | AAAAB | 3 | 168 | 56.0 [48.8, 63.7] | 29.2 [22.6, 36.3] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | AAAAB | 4 | 168 | 53.6 [45.8, 60.7] | 32.7 [25.6, 39.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | BAAAA | 0 | 168 | 60.1 [52.4, 67.3] | 20.8 [14.9, 27.4] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | BAAAA | 1 | 168 | 57.1 [49.4, 64.9] | 26.2 [19.6, 32.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | BAAAA | 2 | 168 | 60.1 [52.4, 67.3] | 25.6 [19.0, 32.1] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | BAAAA | 3 | 168 | 58.3 [50.6, 65.5] | 27.4 [20.8, 35.1] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Seen | TF one-shot | BAAAA | 4 | 168 | 58.3 [51.2, 65.5] | 26.2 [19.0, 33.3] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | Adversarial | 0 | 668 | 53.9 [50.1, 57.6] | 28.4 [25.1, 31.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | Adversarial | 1 | 668 | 51.5 [47.6, 55.2] | 31.4 [28.0, 34.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | Adversarial | 2 | 668 | 51.2 [47.5, 54.9] | 34.0 [30.4, 37.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | Adversarial | 3 | 668 | 50.9 [47.2, 54.8] | 35.5 [31.9, 39.2] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | Adversarial | 4 | 668 | 49.3 [45.4, 53.1] | 37.0 [33.1, 40.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | AAAAB | 0 | 334 | 52.7 [47.3, 57.8] | 29.6 [24.9, 34.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | AAAAB | 1 | 334 | 50.3 [44.9, 55.7] | 33.2 [28.1, 38.3] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | AAAAB | 2 | 334 | 51.2 [46.1, 56.6] | 35.0 [29.9, 40.1] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | AAAAB | 3 | 334 | 50.6 [45.2, 56.0] | 36.5 [31.4, 41.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | AAAAB | 4 | 334 | 46.7 [41.3, 52.1] | 41.3 [35.9, 46.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | BAAAA | 0 | 334 | 55.1 [49.7, 60.5] | 27.2 [22.5, 32.0] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | BAAAA | 1 | 334 | 52.7 [47.3, 58.1] | 29.6 [24.9, 34.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | BAAAA | 2 | 334 | 51.2 [46.1, 56.6] | 32.9 [27.8, 38.0] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | BAAAA | 3 | 334 | 51.2 [45.8, 56.6] | 34.4 [29.3, 39.2] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-instruct | Unseen | TF one-shot | BAAAA | 4 | 334 | 51.8 [46.7, 57.5] | 32.6 [27.2, 37.4] | 0.0 [0.0, 0.0] |

## Figure 4 tests: labels given against none

Images with every dose point (tolerant). slope = per-image least-squares change per label given (0-4), in points, permutation p (doses shuffled within image). 4 vs 0 = all four labels against none, paired, exact McNemar. Holm per model and outcome.

| model | split | probe | order | n img | B=A slope / label [CI] | p (Holm) | B=A 4 vs 0 [CI] | p (Holm) | acc slope / label [CI] | p (Holm) | acc 4 vs 0 [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | TF one-shot | Adversarial | 336 | +1.9 [+1.1, +2.8] | 1.0e-04 (6.0e-04) | +8.9 [+5.4, +12.5] | 6.0e-07 (1.2e-05) | -1.0 [-1.8, -0.1] | 0.0053 (0.0159) | -4.8 [-8.3, -1.5] | 0.0113 (0.238) |
| qwen3vl-8b-instruct | Seen | TF one-shot | AAAAB | 168 | +2.7 [+1.4, +3.9] | 1.0e-04 (6.0e-04) | +12.5 [+7.7, +17.9] | 5.7e-06 (1.0e-04) | -1.7 [-3.0, -0.5] | 8.0e-04 (0.004) | -7.7 [-13.1, -3.0] | 0.00443 (0.0974) |
| qwen3vl-8b-instruct | Seen | TF one-shot | BAAAA | 168 | +1.2 [+0.1, +2.4] | 0.0056 (0.0056) | +5.4 [+1.2, +9.5] | 0.0352 (0.0859) | -0.2 [-1.4, +0.9] | 0.648 (0.648) | -1.8 [-6.5, +3.0] | 0.629 (1) |
| qwen3vl-8b-instruct | Unseen | TF one-shot | Adversarial | 668 | +2.1 [+1.5, +2.7] | 1.0e-04 (6.0e-04) | +8.5 [+5.8, +11.1] | 1.3e-10 (3.2e-09) | -1.0 [-1.5, -0.4] | 1.0e-04 (6.0e-04) | -4.6 [-6.9, -2.4] | 1.9e-04 (0.00466) |
| qwen3vl-8b-instruct | Unseen | TF one-shot | AAAAB | 334 | +2.7 [+1.8, +3.5] | 1.0e-04 (6.0e-04) | +11.7 [+7.8, +15.6] | 2.8e-09 (6.4e-08) | -1.2 [-2.0, -0.4] | 0.0018 (0.0072) | -6.0 [-9.3, -2.7] | 8.2e-04 (0.0189) |
| qwen3vl-8b-instruct | Unseen | TF one-shot | BAAAA | 334 | +1.6 [+0.7, +2.5] | 1.0e-04 (6.0e-04) | +5.4 [+1.8, +8.7] | 0.00393 (0.0329) | -0.8 [-1.6, +0.0] | 0.0138 (0.0276) | -3.3 [-6.6, +0.0] | 0.0801 (0.882) |

