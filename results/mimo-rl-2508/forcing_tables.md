# RQ2 forcing probes

Files (20): rq1_mimo-rl-2508_adversarial_default_train.jsonl, rq1_mimo-rl-2508_adversarial_default_validation.jsonl, rq1_mimo-rl-2508_adversarial_single_train.jsonl, rq1_mimo-rl-2508_adversarial_single_validation.jsonl, rq1_mimo-rl-2508_default_train.jsonl, rq1_mimo-rl-2508_default_validation.jsonl, rq1_mimo-rl-2508_single_train.jsonl, rq1_mimo-rl-2508_single_validation.jsonl, forcing_mimo-rl-2508_cf_train.jsonl, forcing_mimo-rl-2508_cf_validation.jsonl, forcing_mimo-rl-2508_tf-incremental_train.jsonl, forcing_mimo-rl-2508_tf-incremental_validation.jsonl, forcing_mimo-rl-2508_tf-oneshot_train.jsonl, forcing_mimo-rl-2508_tf-oneshot_validation.jsonl, forcing_dose_mimo-rl-2508_train.jsonl, forcing_dose_mimo-rl-2508_validation.jsonl, forcing_place_mimo-rl-2508_train.jsonl, forcing_place_mimo-rl-2508_validation.jsonl, forcing_homog_mimo-rl-2508_train.jsonl, forcing_homog_mimo-rl-2508_validation.jsonl

## Table 4: the odd object B under each condition (%)

B acc = B named correctly; B=A = B given the class of the other four (inertia); B=C = B given the counterfactual class. Tolerant parse, strict in parentheses. cut = calls for B at the token limit (scored wrong). vs default = paired on the same images, y - x in points; p = exact McNemar, Holm over the model's comparisons in the same probe family (core = single, TF incremental, TF one-shot, CF; dose = given=0-3; placement = assistant; C near/far; Homogeneous control).

| model | split | order | condition | n img | cut | B acc [95% CI] | B=A [95% CI] | B=C | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | Adversarial | single | 336 | 3 | 61.3 (45.2) [56.2, 66.7] | 14.3 (10.4) [10.7, 18.5] | - | +7.1 [+2.7, +11.9] | 0.00369 (0.0775) | -5.1 [-8.3, -1.8] | 0.00599 (0.0778) |
| mimo-rl-2508 | Seen | Adversarial | default | 336 | 21 | 54.2 (51.8) [49.1, 59.5] | 19.3 (18.8) [15.2, 23.5] | - | - | - | - | - |
| mimo-rl-2508 | Seen | Adversarial | TF incremental | 336 | 13 | 52.1 (38.7) [46.7, 57.4] | 24.7 (18.8) [19.9, 29.5] | - | -2.1 [-6.2, +2.1] | 0.401 (1) | +5.4 [+1.8, +8.9] | 0.00643 (0.0778) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot | 336 | 8 | 52.7 (42.6) [47.0, 58.3] | 25.0 (21.7) [20.5, 29.5] | - | -1.5 [-6.0, +3.0] | 0.603 (1) | +5.7 [+2.1, +9.2] | 0.00432 (0.0605) |
| mimo-rl-2508 | Seen | Adversarial | CF | 336 | 18 | 50.6 (38.4) [45.5, 56.0] | 23.2 (18.2) [18.8, 28.0] | 0.9 (0.6) | -3.6 [-7.4, +0.3] | 0.111 (1) | +3.9 [+0.6, +7.1] | 0.0351 (0.316) |
| mimo-rl-2508 | Seen | Adversarial | CF, assistant | 336 | 22 | 11.0 (9.2) [7.7, 14.6] | 0.0 (0.0) [0.0, 0.0] | 40.2 (28.9) | -43.2 [-48.8, -37.5] | 1.7e-42 (1.8e-41) | -19.3 [-23.8, -15.2] | 5.4e-20 (4.9e-19) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, assistant | 336 | 18 | 47.9 (45.2) [42.6, 53.6] | 20.8 (20.8) [16.7, 25.0] | - | -6.2 [-10.1, -2.4] | 0.00309 (0.0154) | +1.5 [-1.5, +4.5] | 0.458 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=0 | 336 | 17 | 56.2 (49.4) [50.9, 61.6] | 19.0 (15.2) [14.9, 23.2] | - | +2.1 [-1.8, +6.2] | 0.371 (1) | -0.3 [-3.3, +2.7] | 1 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=1 | 336 | 15 | 56.8 (42.0) [51.5, 62.2] | 20.5 (14.9) [16.4, 25.0] | - | +2.7 [-0.9, +6.2] | 0.2 (1) | +1.2 [-2.1, +4.5] | 0.608 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=2 | 336 | 15 | 53.0 (39.0) [47.3, 58.0] | 21.7 (16.4) [17.3, 26.2] | - | -1.2 [-4.8, +2.4] | 0.627 (1) | +2.4 [-0.9, +5.7] | 0.215 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=3 | 336 | 5 | 54.2 (42.0) [48.8, 59.5] | 22.3 (17.3) [17.9, 27.1] | - | +0.0 [-3.9, +3.9] | 1 (1) | +3.0 [+0.3, +6.0] | 0.0639 (1) |
| mimo-rl-2508 | Seen | AAAAB | single | 168 | 1 | 63.7 (44.0) [56.5, 70.8] | 12.5 (8.9) [7.7, 17.9] | - | +7.1 [+0.6, +13.7] | 0.0652 (1) | -8.3 [-13.7, -3.6] | 0.00258 (0.0393) |
| mimo-rl-2508 | Seen | AAAAB | default | 168 | 9 | 56.5 (52.4) [49.4, 64.3] | 20.8 (20.2) [14.9, 27.4] | - | - | - | - | - |
| mimo-rl-2508 | Seen | AAAAB | TF incremental | 168 | 4 | 51.2 (25.0) [44.0, 58.9] | 28.6 (16.7) [22.0, 35.1] | - | -5.4 [-11.9, +1.2] | 0.163 (1) | +7.7 [+1.8, +14.3] | 0.0192 (0.211) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot | 168 | 5 | 50.6 (41.1) [42.9, 57.7] | 28.6 (25.0) [22.0, 35.7] | - | -6.0 [-13.7, +0.6] | 0.143 (1) | +7.7 [+1.8, +14.3] | 0.0241 (0.241) |
| mimo-rl-2508 | Seen | AAAAB | CF | 168 | 9 | 50.0 (39.3) [42.3, 57.1] | 23.8 (17.3) [17.9, 30.4] | 1.2 (0.6) | -6.5 [-13.1, +0.0] | 0.0708 (1) | +3.0 [-2.4, +8.3] | 0.359 (1) |
| mimo-rl-2508 | Seen | AAAAB | CF, assistant | 168 | 8 | 12.5 (9.5) [7.7, 17.3] | 0.0 (0.0) [0.0, 0.0] | 31.5 (21.4) | -44.0 [-51.8, -36.3] | 1.1e-22 (8.5e-22) | -20.8 [-27.4, -14.9] | 5.8e-11 (4.7e-10) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, assistant | 168 | 7 | 45.2 (43.5) [37.5, 53.0] | 22.0 (22.0) [16.7, 28.0] | - | -11.3 [-16.7, -5.4] | 3.1e-04 (0.00186) | +1.2 [-3.6, +6.0] | 0.791 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=0 | 168 | 5 | 59.5 (52.4) [52.4, 66.7] | 19.6 (14.3) [13.7, 25.6] | - | +3.0 [-2.4, +8.9] | 0.424 (1) | -1.2 [-6.0, +3.6] | 0.815 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=1 | 168 | 8 | 57.7 (39.3) [49.4, 65.5] | 20.2 (14.9) [14.3, 26.2] | - | +1.2 [-4.8, +6.5] | 0.845 (1) | -0.6 [-6.0, +4.8] | 1 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=2 | 168 | 5 | 54.8 (35.7) [47.6, 61.9] | 22.6 (14.9) [16.7, 29.2] | - | -1.8 [-7.7, +4.2] | 0.678 (1) | +1.8 [-3.6, +7.1] | 0.648 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=3 | 168 | 2 | 53.0 (39.3) [45.2, 60.1] | 23.8 (17.9) [17.3, 30.4] | - | -3.6 [-9.5, +2.4] | 0.327 (1) | +3.0 [-1.8, +7.7] | 0.302 (1) |
| mimo-rl-2508 | Seen | BAAAA | single | 168 | 2 | 58.9 (46.4) [51.8, 66.1] | 16.1 (11.9) [10.7, 22.0] | - | +7.1 [+1.8, +13.7] | 0.0357 (0.714) | -1.8 [-6.0, +2.4] | 0.607 (1) |
| mimo-rl-2508 | Seen | BAAAA | default | 168 | 12 | 51.8 (51.2) [43.5, 59.5] | 17.9 (17.3) [12.5, 23.8] | - | - | - | - | - |
| mimo-rl-2508 | Seen | BAAAA | TF incremental | 168 | 9 | 53.0 (52.4) [45.8, 60.7] | 20.8 (20.8) [14.9, 26.8] | - | +1.2 [-3.6, +6.0] | 0.815 (1) | +3.0 [-1.2, +7.1] | 0.267 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot | 168 | 3 | 54.8 (44.0) [47.6, 61.9] | 21.4 (18.5) [15.5, 27.4] | - | +3.0 [-2.4, +8.3] | 0.383 (1) | +3.6 [-0.6, +7.7] | 0.146 (1) |
| mimo-rl-2508 | Seen | BAAAA | CF | 168 | 9 | 51.2 (37.5) [44.0, 58.9] | 22.6 (19.0) [16.7, 29.2] | 0.6 (0.6) | -0.6 [-5.4, +4.2] | 1 (1) | +4.8 [+0.6, +9.5] | 0.0574 (0.459) |
| mimo-rl-2508 | Seen | BAAAA | CF, assistant | 168 | 14 | 9.5 (8.9) [5.4, 14.3] | 0.0 (0.0) [0.0, 0.0] | 48.8 (36.3) | -42.3 [-50.0, -34.5] | 1.6e-20 (1.1e-19) | -17.9 [-23.8, -12.5] | 1.9e-09 (1.3e-08) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, assistant | 168 | 11 | 50.6 (47.0) [43.5, 57.7] | 19.6 (19.6) [13.7, 26.2] | - | -1.2 [-6.5, +3.6] | 0.824 (0.824) | +1.8 [-3.0, +6.5] | 0.607 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=0 | 168 | 12 | 53.0 (46.4) [44.6, 60.7] | 18.5 (16.1) [12.5, 24.4] | - | +1.2 [-4.2, +6.5] | 0.824 (1) | +0.6 [-2.4, +4.2] | 1 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=1 | 168 | 7 | 56.0 (44.6) [48.2, 63.7] | 20.8 (14.9) [14.9, 26.8] | - | +4.2 [+0.0, +8.3] | 0.0923 (1) | +3.0 [-1.2, +7.1] | 0.267 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=2 | 168 | 10 | 51.2 (42.3) [44.0, 58.3] | 20.8 (17.9) [15.5, 26.8] | - | -0.6 [-4.8, +4.2] | 1 (1) | +3.0 [-1.2, +7.1] | 0.267 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=3 | 168 | 3 | 55.4 (44.6) [47.6, 62.5] | 20.8 (16.7) [14.9, 26.8] | - | +3.6 [-1.2, +8.3] | 0.21 (1) | +3.0 [-0.6, +6.5] | 0.18 (1) |
| mimo-rl-2508 | Seen | Homogeneous control | single | 400 | 0 | 85.0 (71.8) [81.5, 88.5] | - | - | -2.0 [-5.0, +1.0] | 0.256 (0.4) | - | - |
| mimo-rl-2508 | Seen | Homogeneous control | default | 400 | 7 | 87.0 (83.8) [83.7, 90.2] | - | - | - | - | - | - |
| mimo-rl-2508 | Seen | Homogeneous control | TF one-shot | 400 | 0 | 96.0 (90.2) [94.0, 97.8] | - | - | +9.0 [+6.2, +12.0] | 1.5e-09 (6.0e-09) | - | - |
| mimo-rl-2508 | Unseen | Adversarial | single | 668 | 14 | 55.7 (37.0) [51.8, 59.3] | 21.4 (12.9) [18.1, 24.4] | - | +12.3 [+8.8, +15.7] | 5.4e-12 (1.3e-10) | -9.6 [-12.7, -6.6] | 3.8e-09 (9.0e-08) |
| mimo-rl-2508 | Unseen | Adversarial | default | 668 | 57 | 43.4 (37.3) [39.7, 47.2] | 31.0 (29.2) [27.5, 34.4] | - | - | - | - | - |
| mimo-rl-2508 | Unseen | Adversarial | TF incremental | 668 | 51 | 40.3 (28.7) [36.7, 43.9] | 37.0 (28.0) [33.4, 40.7] | - | -3.1 [-6.0, -0.3] | 0.046 (0.793) | +6.0 [+3.1, +8.8] | 1.1e-04 (0.00208) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot | 668 | 30 | 40.1 (32.3) [36.2, 43.9] | 38.9 (29.9) [35.3, 42.8] | - | -3.3 [-6.3, -0.3] | 0.0371 (0.714) | +7.9 [+4.9, +10.9] | 3.8e-07 (8.3e-06) |
| mimo-rl-2508 | Unseen | Adversarial | CF | 668 | 50 | 40.9 (26.8) [37.3, 44.6] | 35.5 (24.7) [32.0, 39.1] | 0.4 (0.0) | -2.5 [-5.5, +0.2] | 0.0966 (1) | +4.5 [+1.8, +7.3] | 0.00161 (0.0273) |
| mimo-rl-2508 | Unseen | Adversarial | CF, assistant | 668 | 73 | 6.4 (4.5) [4.6, 8.4] | 0.0 (0.0) [0.0, 0.0] | 46.6 (34.3) | -37.0 [-40.7, -33.4] | 6.0e-69 (7.2e-68) | -31.0 [-34.7, -27.4] | 9.7e-63 (1.2e-61) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, assistant | 668 | 59 | 39.5 (37.4) [35.8, 43.3] | 34.7 (30.4) [31.1, 38.3] | - | -3.9 [-6.7, -0.7] | 0.0188 (0.0752) | +3.7 [+0.7, +6.9] | 0.0211 (0.127) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=0 | 668 | 46 | 43.0 (34.6) [39.1, 46.6] | 32.6 (27.8) [28.9, 36.2] | - | -0.4 [-3.1, +2.4] | 0.834 (1) | +1.6 [-0.9, +4.2] | 0.26 (1) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=1 | 668 | 54 | 42.2 (26.5) [38.5, 46.3] | 33.7 (25.6) [30.1, 37.3] | - | -1.2 [-3.9, +1.5] | 0.445 (1) | +2.7 [+0.0, +5.4] | 0.0662 (1) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=2 | 668 | 44 | 40.9 (26.5) [37.1, 44.8] | 36.7 (25.4) [32.9, 40.1] | - | -2.5 [-5.4, +0.4] | 0.104 (1) | +5.7 [+2.7, +8.5] | 1.1e-04 (0.00244) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=3 | 668 | 51 | 38.3 (25.1) [34.7, 42.1] | 38.2 (27.7) [34.4, 41.8] | - | -5.1 [-8.1, -2.1] | 7.7e-04 (0.0185) | +7.2 [+4.5, +10.0] | 2.8e-07 (6.4e-06) |
| mimo-rl-2508 | Unseen | AAAAB | single | 334 | 9 | 57.2 (37.4) [51.8, 62.3] | 18.9 (9.3) [14.7, 23.1] | - | +15.0 [+10.2, +20.1] | 1.4e-08 (3.2e-07) | -10.5 [-15.0, -6.0] | 1.1e-05 (2.2e-04) |
| mimo-rl-2508 | Unseen | AAAAB | default | 334 | 35 | 42.2 (33.2) [36.8, 47.3] | 29.3 (26.3) [24.9, 34.4] | - | - | - | - | - |
| mimo-rl-2508 | Unseen | AAAAB | TF incremental | 334 | 16 | 38.6 (17.1) [33.2, 44.0] | 40.7 (23.4) [35.6, 46.1] | - | -3.6 [-8.1, +0.9] | 0.169 (1) | +11.4 [+6.9, +15.9] | 2.8e-06 (5.9e-05) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot | 334 | 16 | 37.4 (31.4) [32.6, 42.8] | 42.5 (32.9) [37.1, 47.9] | - | -4.8 [-9.3, -0.3] | 0.044 (0.793) | +13.2 [+8.1, +17.7] | 6.2e-08 (1.4e-06) |
| mimo-rl-2508 | Unseen | AAAAB | CF | 334 | 29 | 39.2 (21.9) [34.1, 44.6] | 35.6 (22.8) [30.5, 40.7] | 0.3 (0.0) | -3.0 [-7.2, +1.2] | 0.203 (1) | +6.3 [+2.7, +10.2] | 0.00246 (0.0393) |
| mimo-rl-2508 | Unseen | AAAAB | CF, assistant | 334 | 44 | 7.2 (4.5) [4.5, 9.9] | 0.0 (0.0) [0.0, 0.0] | 36.8 (29.0) | -35.0 [-40.4, -29.6] | 5.8e-32 (5.3e-31) | -29.3 [-34.4, -24.9] | 6.3e-30 (6.3e-29) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, assistant | 334 | 31 | 38.0 (37.7) [32.9, 43.1] | 32.6 (29.0) [27.8, 38.0] | - | -4.2 [-8.7, +0.3] | 0.098 (0.294) | +3.3 [-1.2, +7.5] | 0.177 (0.708) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=0 | 334 | 21 | 42.8 (33.5) [37.4, 48.2] | 32.9 (28.1) [28.1, 37.7] | - | +0.6 [-3.3, +4.8] | 0.89 (1) | +3.6 [-0.3, +7.5] | 0.111 (1) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=1 | 334 | 29 | 41.3 (23.1) [35.9, 46.4] | 33.2 (23.1) [27.8, 38.6] | - | -0.9 [-4.8, +3.0] | 0.761 (1) | +3.9 [+0.0, +7.8] | 0.0725 (1) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=2 | 334 | 24 | 39.8 (22.5) [34.4, 44.9] | 36.8 (22.5) [32.0, 42.2] | - | -2.4 [-6.9, +2.1] | 0.366 (1) | +7.5 [+3.3, +12.0] | 0.00102 (0.0213) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=3 | 334 | 30 | 35.3 (19.5) [30.2, 40.7] | 40.4 (27.2) [35.0, 45.5] | - | -6.9 [-11.4, -2.7] | 0.0032 (0.0736) | +11.1 [+6.9, +15.0] | 2.4e-07 (5.7e-06) |
| mimo-rl-2508 | Unseen | BAAAA | single | 334 | 5 | 54.2 (36.5) [48.8, 59.6] | 24.0 (16.5) [19.5, 28.4] | - | +9.6 [+4.8, +14.4] | 1.0e-04 (0.00223) | -8.7 [-12.9, -4.2] | 1.5e-04 (0.00277) |
| mimo-rl-2508 | Unseen | BAAAA | default | 334 | 22 | 44.6 (41.3) [39.2, 50.0] | 32.6 (32.0) [27.8, 37.7] | - | - | - | - | - |
| mimo-rl-2508 | Unseen | BAAAA | TF incremental | 334 | 35 | 41.9 (40.4) [36.8, 47.6] | 33.2 (32.6) [28.1, 38.3] | - | -2.7 [-6.3, +0.9] | 0.188 (1) | +0.6 [-3.0, +4.2] | 0.871 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot | 334 | 14 | 42.8 (33.2) [37.7, 48.2] | 35.3 (26.9) [30.2, 40.7] | - | -1.8 [-5.4, +2.1] | 0.461 (1) | +2.7 [-0.9, +6.6] | 0.211 (1) |
| mimo-rl-2508 | Unseen | BAAAA | CF | 334 | 21 | 42.5 (31.7) [37.4, 47.9] | 35.3 (26.6) [30.2, 40.1] | 0.6 (0.0) | -2.1 [-6.0, +1.5] | 0.36 (1) | +2.7 [-1.2, +6.3] | 0.211 (1) |
| mimo-rl-2508 | Unseen | BAAAA | CF, assistant | 334 | 29 | 5.7 (4.5) [3.3, 8.1] | 0.0 (0.0) [0.0, 0.0] | 56.3 (39.5) | -38.9 [-44.3, -33.8] | 4.9e-38 (4.9e-37) | -32.6 [-37.7, -27.5] | 3.1e-33 (3.4e-32) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, assistant | 334 | 28 | 41.0 (37.1) [35.6, 46.1] | 36.8 (31.7) [31.4, 41.9] | - | -3.6 [-7.8, +0.6] | 0.126 (0.294) | +4.2 [+0.0, +8.7] | 0.0759 (0.38) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=0 | 334 | 25 | 43.1 (35.6) [38.0, 48.5] | 32.3 (27.5) [27.2, 37.1] | - | -1.5 [-5.4, +2.4] | 0.522 (1) | -0.3 [-3.6, +3.0] | 1 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=1 | 334 | 25 | 43.1 (29.9) [38.0, 48.5] | 34.1 (28.1) [29.3, 39.5] | - | -1.5 [-5.4, +2.1] | 0.533 (1) | +1.5 [-2.4, +5.4] | 0.533 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=2 | 334 | 20 | 41.9 (30.5) [36.8, 47.3] | 36.5 (28.4) [31.1, 41.6] | - | -2.7 [-6.3, +0.9] | 0.188 (1) | +3.9 [+0.3, +7.5] | 0.0533 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=3 | 334 | 21 | 41.3 (30.8) [36.2, 47.0] | 35.9 (28.1) [30.8, 41.0] | - | -3.3 [-7.2, +0.6] | 0.117 (1) | +3.3 [-0.3, +6.9] | 0.0895 (1) |
| mimo-rl-2508 | Unseen | Homogeneous control | single | 490 | 5 | 78.2 (62.4) [74.7, 81.8] | - | - | -2.2 [-5.5, +0.8] | 0.2 (0.4) | - | - |
| mimo-rl-2508 | Unseen | Homogeneous control | default | 490 | 22 | 80.4 (74.9) [76.9, 83.9] | - | - | - | - | - | - |
| mimo-rl-2508 | Unseen | Homogeneous control | TF one-shot | 490 | 8 | 86.9 (79.2) [84.1, 90.0] | - | - | +6.5 [+3.9, +9.4] | 5.6e-06 (1.7e-05) | - | - |

## Table 4, sensitivity: images where neither call for B hit the token limit

Same comparisons with default as Table 4 (tolerant, y - x in points, exact McNemar, Holm within the probe family), on the images where neither the condition's nor default's call for B was cut.

| model | split | order | condition | n img | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | Adversarial | single | 314 | +4.5 [+0.0, +8.6] | 0.0759 (0.987) | -6.4 [-9.6, -3.2] | 3.2e-04 (0.00552) |
| mimo-rl-2508 | Seen | Adversarial | TF incremental | 309 | -3.6 [-7.8, +0.6] | 0.117 (1) | +4.5 [+1.0, +8.4] | 0.0243 (0.267) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot | 310 | -5.2 [-9.4, -1.0] | 0.0293 (0.44) | +5.5 [+1.9, +9.7] | 0.00763 (0.0992) |
| mimo-rl-2508 | Seen | Adversarial | CF | 305 | -3.3 [-7.2, +0.7] | 0.143 (1) | +3.6 [+0.6, +6.9] | 0.0433 (0.39) |
| mimo-rl-2508 | Seen | Adversarial | CF, assistant | 305 | -45.2 [-50.8, -39.3] | 2.0e-40 (2.2e-39) | -21.3 [-26.2, -16.4] | 5.4e-20 (4.9e-19) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, assistant | 309 | -7.1 [-11.0, -3.2] | 6.8e-04 (0.0034) | +1.9 [-1.3, +5.5] | 0.327 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=0 | 307 | +1.3 [-2.3, +5.2] | 0.608 (1) | -1.0 [-3.9, +2.0] | 0.664 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=1 | 306 | +2.6 [-0.7, +5.9] | 0.185 (1) | +0.3 [-2.9, +3.6] | 1 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=2 | 306 | -1.3 [-4.6, +2.3] | 0.585 (1) | +2.3 [-0.7, +5.2] | 0.21 (1) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=3 | 313 | -2.9 [-6.4, +1.0] | 0.163 (1) | +2.2 [-0.6, +4.8] | 0.189 (1) |
| mimo-rl-2508 | Seen | AAAAB | single | 158 | +4.4 [-2.5, +11.4] | 0.281 (1) | -8.9 [-14.6, -3.8] | 0.00131 (0.021) |
| mimo-rl-2508 | Seen | AAAAB | TF incremental | 158 | -7.6 [-14.6, -1.3] | 0.0357 (0.5) | +7.6 [+1.9, +13.9] | 0.029 (0.29) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot | 155 | -9.7 [-16.8, -2.6] | 0.0135 (0.23) | +8.4 [+1.9, +14.8] | 0.0192 (0.23) |
| mimo-rl-2508 | Seen | AAAAB | CF | 154 | -5.8 [-12.3, +0.6] | 0.108 (1) | +3.2 [-1.9, +8.4] | 0.332 (1) |
| mimo-rl-2508 | Seen | AAAAB | CF, assistant | 157 | -45.9 [-53.5, -38.2] | 4.2e-22 (3.4e-21) | -22.3 [-29.3, -15.9] | 5.8e-11 (4.7e-10) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, assistant | 156 | -12.8 [-18.6, -7.1] | 3.6e-05 (2.2e-04) | +2.6 [-1.9, +7.1] | 0.388 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=0 | 157 | +2.5 [-3.2, +8.3] | 0.503 (1) | -2.5 [-7.6, +1.9] | 0.454 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=1 | 154 | +0.6 [-4.5, +6.5] | 1 (1) | +0.6 [-4.5, +5.8] | 1 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=2 | 155 | -3.2 [-9.0, +1.9] | 0.359 (1) | +1.9 [-3.2, +7.1] | 0.607 (1) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=3 | 158 | -6.3 [-12.0, -0.6] | 0.0525 (0.997) | +2.5 [-1.9, +7.0] | 0.424 (1) |
| mimo-rl-2508 | Seen | BAAAA | single | 156 | +4.5 [-1.9, +10.3] | 0.21 (1) | -3.8 [-8.3, +0.0] | 0.146 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF incremental | 151 | +0.7 [-4.0, +5.3] | 1 (1) | +1.3 [-2.6, +5.3] | 0.727 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot | 155 | -0.6 [-5.8, +4.5] | 1 (1) | +2.6 [-1.3, +6.5] | 0.344 (1) |
| mimo-rl-2508 | Seen | BAAAA | CF | 151 | -0.7 [-5.3, +4.6] | 1 (1) | +4.0 [+0.7, +7.9] | 0.0703 (0.562) |
| mimo-rl-2508 | Seen | BAAAA | CF, assistant | 148 | -44.6 [-52.7, -36.5] | 4.7e-19 (3.3e-18) | -20.3 [-27.0, -14.2] | 1.9e-09 (1.3e-08) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, assistant | 153 | -1.3 [-6.5, +3.9] | 0.804 (0.804) | +1.3 [-3.3, +5.9] | 0.791 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=0 | 150 | +0.0 [-5.3, +4.7] | 1 (1) | +0.7 [-2.0, +4.0] | 1 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=1 | 152 | +4.6 [+1.3, +8.6] | 0.0391 (0.781) | +0.0 [-3.3, +3.9] | 1 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=2 | 151 | +0.7 [-3.3, +4.6] | 1 (1) | +2.6 [-0.7, +6.0] | 0.289 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=3 | 155 | +0.6 [-3.2, +5.2] | 1 (1) | +1.9 [-1.3, +5.8] | 0.453 (1) |
| mimo-rl-2508 | Seen | Homogeneous control | single | 393 | -3.3 [-6.4, -0.5] | 0.0351 (0.0351) | - | - |
| mimo-rl-2508 | Seen | Homogeneous control | TF one-shot | 393 | +7.4 [+4.6, +10.4] | 1.3e-07 (5.2e-07) | - | - |
| mimo-rl-2508 | Unseen | Adversarial | single | 600 | +8.3 [+5.0, +11.7] | 2.5e-06 (6.1e-05) | -10.7 [-14.0, -7.3] | 6.0e-10 (1.4e-08) |
| mimo-rl-2508 | Unseen | Adversarial | TF incremental | 580 | -4.1 [-7.1, -1.4] | 0.00631 (0.12) | +6.0 [+2.9, +8.8] | 1.5e-04 (0.00278) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot | 592 | -4.9 [-7.8, -2.0] | 0.00108 (0.0237) | +6.6 [+3.7, +9.6] | 4.3e-05 (8.6e-04) |
| mimo-rl-2508 | Unseen | Adversarial | CF | 582 | -3.3 [-6.0, -0.5] | 0.0271 (0.434) | +4.5 [+1.7, +7.4] | 0.00255 (0.0382) |
| mimo-rl-2508 | Unseen | Adversarial | CF, assistant | 566 | -41.2 [-45.4, -37.1] | 8.5e-69 (1.0e-67) | -34.8 [-38.7, -30.7] | 1.0e-59 (1.2e-58) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, assistant | 581 | -4.3 [-7.2, -1.2] | 0.00884 (0.0353) | +3.6 [+0.3, +6.9] | 0.0396 (0.238) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=0 | 582 | -0.9 [-3.4, +1.7] | 0.59 (1) | +0.9 [-1.5, +3.4] | 0.603 (1) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=1 | 578 | -1.9 [-4.3, +0.9] | 0.193 (1) | +2.6 [-0.2, +5.4] | 0.0864 (1) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=2 | 586 | -3.8 [-6.5, -1.0] | 0.00921 (0.193) | +5.5 [+2.6, +8.4] | 3.8e-04 (0.00831) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=3 | 578 | -5.4 [-8.1, -2.6] | 1.2e-04 (0.00281) | +6.9 [+4.2, +9.7] | 1.7e-06 (4.0e-05) |
| mimo-rl-2508 | Unseen | AAAAB | single | 293 | +10.2 [+5.5, +15.4] | 1.3e-04 (0.00309) | -11.9 [-16.7, -7.2] | 3.3e-06 (7.6e-05) |
| mimo-rl-2508 | Unseen | AAAAB | TF incremental | 289 | -7.6 [-12.5, -3.1] | 0.00209 (0.0439) | +10.7 [+5.9, +15.6] | 3.3e-05 (6.9e-04) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot | 290 | -6.9 [-11.7, -2.8] | 0.00366 (0.0732) | +11.4 [+6.9, +16.2] | 8.7e-06 (1.9e-04) |
| mimo-rl-2508 | Unseen | AAAAB | CF | 282 | -3.9 [-8.2, +0.0] | 0.0801 (0.987) | +6.0 [+2.1, +10.3] | 0.00599 (0.0838) |
| mimo-rl-2508 | Unseen | AAAAB | CF, assistant | 272 | -40.4 [-46.3, -34.6] | 1.5e-33 (1.4e-32) | -33.8 [-39.7, -28.3] | 4.0e-28 (4.0e-27) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, assistant | 285 | -5.3 [-9.8, -0.4] | 0.04 (0.12) | +2.1 [-2.5, +6.7] | 0.461 (1) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=0 | 287 | -2.1 [-6.3, +1.7] | 0.392 (1) | +2.4 [-1.7, +6.6] | 0.324 (1) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=1 | 283 | -3.2 [-7.1, +0.7] | 0.15 (1) | +3.9 [+0.0, +8.1] | 0.0895 (1) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=2 | 286 | -6.3 [-10.8, -2.1] | 0.00792 (0.174) | +7.7 [+3.5, +12.2] | 0.00164 (0.0345) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=3 | 281 | -7.5 [-11.7, -3.2] | 7.5e-04 (0.0173) | +10.7 [+6.4, +15.3] | 2.8e-06 (6.5e-05) |
| mimo-rl-2508 | Unseen | BAAAA | single | 307 | +6.5 [+2.3, +10.7] | 0.00779 (0.14) | -9.4 [-14.0, -4.9] | 8.2e-05 (0.00155) |
| mimo-rl-2508 | Unseen | BAAAA | TF incremental | 291 | -0.7 [-4.1, +2.7] | 0.839 (1) | +1.4 [-2.1, +4.8] | 0.572 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot | 302 | -3.0 [-6.6, +0.7] | 0.15 (1) | +2.0 [-1.7, +6.0] | 0.392 (1) |
| mimo-rl-2508 | Unseen | BAAAA | CF | 300 | -2.7 [-6.3, +1.0] | 0.229 (1) | +3.0 [-1.0, +6.7] | 0.175 (1) |
| mimo-rl-2508 | Unseen | BAAAA | CF, assistant | 294 | -41.8 [-47.6, -36.1] | 5.9e-36 (5.9e-35) | -35.7 [-41.2, -30.3] | 4.9e-32 (5.4e-31) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, assistant | 296 | -3.4 [-7.4, +0.7] | 0.143 (0.287) | +5.1 [+0.7, +9.5] | 0.0444 (0.238) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=0 | 295 | +0.3 [-2.4, +3.4] | 1 (1) | -0.7 [-3.7, +2.4] | 0.832 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=1 | 295 | -0.7 [-4.1, +3.1] | 0.851 (1) | +1.4 [-2.4, +5.1] | 0.597 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=2 | 300 | -1.3 [-4.7, +1.7] | 0.541 (1) | +3.3 [-0.3, +7.0] | 0.11 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=3 | 297 | -3.4 [-6.7, +0.0] | 0.0755 (1) | +3.4 [+0.0, +6.7] | 0.0872 (1) |
| mimo-rl-2508 | Unseen | Homogeneous control | single | 465 | -4.3 [-7.3, -1.5] | 0.0066 (0.0132) | - | - |
| mimo-rl-2508 | Unseen | Homogeneous control | TF one-shot | 463 | +4.8 [+2.4, +7.1] | 2.0e-04 (5.9e-04) | - | - |

## Table 4, against Single-object (B asked alone)

Same images, tolerant, y - x in points, exact McNemar, Holm over the model's comparisons with Single-object in the same probe family (default counts as core). Single-object asks one box per turn with the official single-object prompt, so this gap holds both the multi-object format (default) and the given labels.

| model | split | order | condition | n img | acc vs single [CI] | p (Holm) | B=A vs single [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | Adversarial | default | 336 | -7.1 [-11.6, -2.7] | 0.00369 (0.0221) | +5.1 [+1.8, +8.3] | 0.00599 (0.0299) |
| mimo-rl-2508 | Seen | Adversarial | TF incremental | 336 | -9.2 [-13.7, -4.5] | 1.9e-04 (0.0021) | +10.4 [+6.5, +14.6] | 1.2e-06 (1.8e-05) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot | 336 | -8.6 [-13.1, -4.2] | 2.6e-04 (0.00238) | +10.7 [+6.8, +14.6] | 4.0e-07 (6.9e-06) |
| mimo-rl-2508 | Seen | Adversarial | CF | 336 | -10.7 [-15.2, -6.5] | 4.8e-06 (6.3e-05) | +8.9 [+5.4, +13.1] | 1.5e-05 (1.5e-04) |
| mimo-rl-2508 | Seen | Adversarial | CF, assistant | 336 | -50.3 [-56.0, -44.9] | 1.1e-49 (1.3e-48) | -14.3 [-18.2, -10.7] | 7.1e-15 (6.4e-14) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, assistant | 336 | -13.4 [-18.8, -8.6] | 3.6e-07 (1.1e-06) | +6.5 [+2.7, +10.4] | 0.00126 (0.00378) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=0 | 336 | -5.1 [-9.5, -0.9] | 0.03 (0.21) | +4.8 [+0.9, +8.6] | 0.0195 (0.101) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=1 | 336 | -4.5 [-8.6, -0.3] | 0.0534 (0.321) | +6.2 [+3.0, +9.5] | 5.1e-04 (0.00439) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=2 | 336 | -8.3 [-12.8, -4.2] | 2.3e-04 (0.00281) | +7.4 [+3.9, +11.0] | 1.1e-04 (0.00135) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, given=3 | 336 | -7.1 [-11.3, -3.3] | 7.2e-04 (0.00789) | +8.0 [+4.5, +11.6] | 1.4e-05 (1.9e-04) |
| mimo-rl-2508 | Seen | AAAAB | default | 168 | -7.1 [-13.7, -0.6] | 0.0652 (0.196) | +8.3 [+3.6, +13.7] | 0.00258 (0.0155) |
| mimo-rl-2508 | Seen | AAAAB | TF incremental | 168 | -12.5 [-19.6, -4.8] | 0.00145 (0.0102) | +16.1 [+10.1, +22.6] | 1.4e-06 (1.8e-05) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot | 168 | -13.1 [-20.2, -6.0] | 6.8e-04 (0.00544) | +16.1 [+9.5, +22.0] | 3.5e-06 (4.2e-05) |
| mimo-rl-2508 | Seen | AAAAB | CF | 168 | -13.7 [-20.8, -7.1] | 1.9e-04 (0.0021) | +11.3 [+5.4, +17.9] | 5.5e-04 (0.00382) |
| mimo-rl-2508 | Seen | AAAAB | CF, assistant | 168 | -51.2 [-58.9, -44.0] | 2.6e-26 (2.1e-25) | -12.5 [-17.9, -7.7] | 9.5e-07 (4.8e-06) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, assistant | 168 | -18.5 [-25.6, -11.3] | 1.6e-06 (3.3e-06) | +9.5 [+3.6, +15.5] | 0.00249 (0.00499) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=0 | 168 | -4.2 [-10.7, +1.8] | 0.265 (0.714) | +7.1 [+1.8, +12.5] | 0.0169 (0.101) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=1 | 168 | -6.0 [-12.5, +0.6] | 0.11 (0.441) | +7.7 [+2.4, +13.1] | 0.0106 (0.0744) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=2 | 168 | -8.9 [-14.9, -3.0] | 0.0107 (0.0961) | +10.1 [+4.8, +15.5] | 4.9e-04 (0.00439) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, given=3 | 168 | -10.7 [-17.3, -4.8] | 0.00143 (0.0143) | +11.3 [+6.0, +16.7] | 1.6e-04 (0.00172) |
| mimo-rl-2508 | Seen | BAAAA | default | 168 | -7.1 [-13.1, -1.2] | 0.0357 (0.143) | +1.8 [-2.4, +6.5] | 0.607 (0.607) |
| mimo-rl-2508 | Seen | BAAAA | TF incremental | 168 | -6.0 [-11.9, +0.0] | 0.0755 (0.196) | +4.8 [+0.0, +10.1] | 0.115 (0.231) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot | 168 | -4.2 [-9.5, +1.2] | 0.189 (0.196) | +5.4 [+0.6, +10.1] | 0.049 (0.147) |
| mimo-rl-2508 | Seen | BAAAA | CF | 168 | -7.7 [-13.7, -2.4] | 0.0146 (0.0732) | +6.5 [+1.8, +11.3] | 0.0192 (0.0768) |
| mimo-rl-2508 | Seen | BAAAA | CF, assistant | 168 | -49.4 [-56.5, -41.7] | 4.4e-24 (3.1e-23) | -16.1 [-21.4, -10.7] | 1.5e-08 (1.0e-07) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, assistant | 168 | -8.3 [-15.5, -1.2] | 0.0288 (0.0288) | +3.6 [-1.2, +8.3] | 0.238 (0.238) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=0 | 168 | -6.0 [-11.9, +0.0] | 0.0755 (0.378) | +2.4 [-3.0, +7.1] | 0.503 (0.503) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=1 | 168 | -3.0 [-8.3, +2.4] | 0.383 (0.714) | +4.8 [+1.2, +8.9] | 0.0386 (0.154) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=2 | 168 | -7.7 [-13.7, -2.4] | 0.0146 (0.117) | +4.8 [+0.0, +9.5] | 0.0963 (0.193) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, given=3 | 168 | -3.6 [-8.3, +1.2] | 0.238 (0.714) | +4.8 [+0.6, +8.9] | 0.0574 (0.172) |
| mimo-rl-2508 | Seen | Homogeneous control | default | 400 | +2.0 [-1.0, +5.2] | 0.256 (0.4) | - | - |
| mimo-rl-2508 | Seen | Homogeneous control | TF one-shot | 400 | +11.0 [+8.0, +14.2] | 1.1e-13 (4.5e-13) | - | - |
| mimo-rl-2508 | Unseen | Adversarial | default | 668 | -12.3 [-15.6, -9.0] | 5.4e-12 (1.1e-10) | +9.6 [+6.6, +12.6] | 3.8e-09 (6.8e-08) |
| mimo-rl-2508 | Unseen | Adversarial | TF incremental | 668 | -15.4 [-19.2, -11.8] | 1.3e-17 (3.0e-16) | +15.6 [+12.3, +18.9] | 3.6e-20 (8.2e-19) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot | 668 | -15.6 [-19.0, -12.3] | 6.5e-19 (1.6e-17) | +17.5 [+14.2, +20.7] | 1.5e-24 (3.6e-23) |
| mimo-rl-2508 | Unseen | Adversarial | CF | 668 | -14.8 [-18.3, -11.4] | 1.0e-16 (2.2e-15) | +14.1 [+10.9, +17.4] | 1.3e-16 (2.6e-15) |
| mimo-rl-2508 | Unseen | Adversarial | CF, assistant | 668 | -49.3 [-53.1, -45.5] | 6.4e-96 (7.6e-95) | -21.4 [-24.7, -18.4] | 1.8e-43 (2.2e-42) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, assistant | 668 | -16.2 [-19.8, -12.4] | 1.6e-17 (9.4e-17) | +13.3 [+9.6, +17.1] | 4.9e-13 (3.9e-12) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=0 | 668 | -12.7 [-16.0, -9.4] | 4.1e-13 (8.6e-12) | +11.2 [+8.1, +14.2] | 3.2e-12 (6.3e-11) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=1 | 668 | -13.5 [-17.4, -9.9] | 1.3e-12 (2.7e-11) | +12.3 [+9.1, +15.4] | 7.0e-13 (1.5e-11) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=2 | 668 | -14.8 [-18.6, -11.2] | 7.9e-16 (1.7e-14) | +15.3 [+11.8, +18.6] | 9.6e-19 (2.2e-17) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, given=3 | 668 | -17.4 [-20.7, -13.9] | 2.1e-22 (5.2e-21) | +16.8 [+13.6, +20.1] | 1.0e-23 (2.5e-22) |
| mimo-rl-2508 | Unseen | AAAAB | default | 334 | -15.0 [-20.1, -9.9] | 1.4e-08 (2.4e-07) | +10.5 [+5.7, +15.0] | 1.1e-05 (1.2e-04) |
| mimo-rl-2508 | Unseen | AAAAB | TF incremental | 334 | -18.6 [-23.7, -13.5] | 1.8e-11 (3.4e-10) | +21.9 [+17.1, +26.7] | 2.4e-17 (5.1e-16) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot | 334 | -19.8 [-25.1, -15.0] | 2.4e-13 (5.0e-12) | +23.7 [+18.6, +28.4] | 1.4e-19 (3.1e-18) |
| mimo-rl-2508 | Unseen | AAAAB | CF | 334 | -18.0 [-23.1, -12.9] | 2.7e-11 (4.9e-10) | +16.8 [+12.0, +21.9] | 3.0e-11 (5.6e-10) |
| mimo-rl-2508 | Unseen | AAAAB | CF, assistant | 334 | -50.0 [-55.4, -44.9] | 9.8e-48 (8.8e-47) | -18.9 [-23.1, -14.7] | 2.2e-19 (2.2e-18) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, assistant | 334 | -19.2 [-24.3, -13.5] | 6.1e-11 (3.1e-10) | +13.8 [+9.0, +18.9] | 1.5e-07 (9.1e-07) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=0 | 334 | -14.4 [-19.2, -9.9] | 2.3e-08 (4.0e-07) | +14.1 [+9.6, +18.6] | 9.8e-10 (1.8e-08) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=1 | 334 | -15.9 [-21.3, -10.5] | 2.0e-08 (3.5e-07) | +14.4 [+9.3, +19.5] | 2.3e-08 (4.0e-07) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=2 | 334 | -17.4 [-22.5, -12.0] | 1.4e-10 (2.7e-09) | +18.0 [+13.5, +23.1] | 3.2e-12 (6.3e-11) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, given=3 | 334 | -21.9 [-26.9, -17.1] | 7.1e-16 (1.6e-14) | +21.6 [+16.8, +26.3] | 2.8e-18 (6.1e-17) |
| mimo-rl-2508 | Unseen | BAAAA | default | 334 | -9.6 [-14.4, -5.1] | 1.0e-04 (0.00122) | +8.7 [+4.5, +13.2] | 1.5e-04 (0.00123) |
| mimo-rl-2508 | Unseen | BAAAA | TF incremental | 334 | -12.3 [-17.1, -7.5] | 2.8e-07 (4.5e-06) | +9.3 [+5.4, +13.5] | 3.3e-05 (3.0e-04) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot | 334 | -11.4 [-15.9, -6.9] | 7.6e-07 (1.1e-05) | +11.4 [+7.2, +15.9] | 4.5e-07 (7.2e-06) |
| mimo-rl-2508 | Unseen | BAAAA | CF | 334 | -11.7 [-16.2, -6.9] | 1.2e-06 (1.6e-05) | +11.4 [+7.2, +15.9] | 1.2e-06 (1.8e-05) |
| mimo-rl-2508 | Unseen | BAAAA | CF, assistant | 334 | -48.5 [-53.9, -43.1] | 3.4e-49 (3.4e-48) | -24.0 [-28.7, -19.5] | 1.7e-24 (1.8e-23) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, assistant | 334 | -13.2 [-17.7, -8.4] | 1.0e-07 (4.1e-07) | +12.9 [+8.1, +18.0] | 1.3e-06 (5.1e-06) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=0 | 334 | -11.1 [-15.6, -6.6] | 6.5e-06 (9.0e-05) | +8.4 [+3.9, +12.9] | 3.1e-04 (0.00307) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=1 | 334 | -11.1 [-16.2, -6.3] | 2.2e-05 (2.9e-04) | +10.2 [+6.0, +14.4] | 1.2e-05 (1.7e-04) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=2 | 334 | -12.3 [-17.1, -7.5] | 1.5e-06 (2.3e-05) | +12.6 [+8.1, +16.8] | 1.0e-07 (1.6e-06) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, given=3 | 334 | -12.9 [-17.4, -8.4] | 6.0e-08 (9.6e-07) | +12.0 [+7.8, +16.2] | 1.6e-07 (2.4e-06) |
| mimo-rl-2508 | Unseen | Homogeneous control | default | 490 | +2.2 [-0.8, +5.3] | 0.2 (0.4) | - | - |
| mimo-rl-2508 | Unseen | Homogeneous control | TF one-shot | 490 | +8.8 [+5.7, +11.8] | 6.0e-08 (1.8e-07) | - | - |

## Assistant-turn prefill: the forced line, then the model's own re-check (%)

first = the label written right after the prefill (the one Table 4 uses); kept writing = the model went on after it (typically "Wait, no, that's wrong" and a re-check); restarted = wrote no label after the forced "objK:" and began its own five-label list on a new line (counted in kept writing; first counts as wrong and not A); final = obj K's last "objK: <class>" in the answer (= first when it stopped); unresolved = kept writing but gave no final label for B, or hit the token limit. cut = thinking never closed. All over n img, tolerant.

| model | split | order | condition | n img | cut | first: B acc | first: B=A | first: B=C | kept writing | restarted | final: B acc | final: B=A | final: B=C | unresolved |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | Adversarial | CF, assistant | 336 | 22 | 11.0 | 0.0 | 40.2 | 66.4 | 40.8 | 44.0 | 13.4 | 18.2 | 2.1 |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot, assistant | 336 | 18 | 47.9 | 20.8 | - | 21.7 | 11.0 | 53.3 | 20.2 | - | 0.9 |
| mimo-rl-2508 | Seen | AAAAB | CF, assistant | 168 | 8 | 12.5 | 0.0 | 31.5 | 78.0 | 50.0 | 51.2 | 16.7 | 7.7 | 2.4 |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot, assistant | 168 | 7 | 45.2 | 22.0 | - | 17.9 | 13.1 | 53.6 | 20.8 | - | 0.6 |
| mimo-rl-2508 | Seen | BAAAA | CF, assistant | 168 | 14 | 9.5 | 0.0 | 48.8 | 54.8 | 31.5 | 36.9 | 10.1 | 28.6 | 1.8 |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot, assistant | 168 | 11 | 50.6 | 19.6 | - | 25.6 | 8.9 | 53.0 | 19.6 | - | 1.2 |
| mimo-rl-2508 | Unseen | Adversarial | CF, assistant | 668 | 73 | 6.4 | 0.0 | 46.6 | 69.0 | 33.7 | 35.9 | 20.7 | 17.2 | 1.6 |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot, assistant | 668 | 59 | 39.5 | 34.7 | - | 26.5 | 7.2 | 43.3 | 30.8 | - | 1.3 |
| mimo-rl-2508 | Unseen | AAAAB | CF, assistant | 334 | 44 | 7.2 | 0.0 | 36.8 | 75.7 | 39.5 | 38.0 | 23.1 | 8.4 | 1.5 |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot, assistant | 334 | 31 | 38.0 | 32.6 | - | 21.9 | 9.9 | 44.0 | 28.7 | - | 1.2 |
| mimo-rl-2508 | Unseen | BAAAA | CF, assistant | 334 | 29 | 5.7 | 0.0 | 56.3 | 62.3 | 27.8 | 33.8 | 18.3 | 26.0 | 1.8 |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot, assistant | 334 | 28 | 41.0 | 36.8 | - | 31.1 | 4.5 | 42.5 | 32.9 | - | 1.5 |

## Figure 4 data: dose-response (tolerant, %)

| model | split | probe | order | labels given | n img | B acc [95% CI] | B=A [95% CI] | B=C [95% CI] |
|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | TF one-shot | Adversarial | 0 | 336 | 56.2 [50.9, 61.3] | 19.0 [14.9, 23.2] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | Adversarial | 1 | 336 | 56.8 [51.8, 62.2] | 20.5 [16.4, 24.7] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | Adversarial | 2 | 336 | 53.0 [47.9, 58.0] | 21.7 [17.3, 26.2] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | Adversarial | 3 | 336 | 54.2 [48.8, 59.5] | 22.3 [17.9, 27.1] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | Adversarial | 4 | 336 | 52.7 [47.3, 58.0] | 25.0 [20.5, 29.8] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | AAAAB | 0 | 168 | 59.5 [51.8, 66.7] | 19.6 [13.7, 25.6] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | AAAAB | 1 | 168 | 57.7 [50.0, 64.9] | 20.2 [14.3, 26.2] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | AAAAB | 2 | 168 | 54.8 [47.6, 62.5] | 22.6 [16.7, 29.2] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | AAAAB | 3 | 168 | 53.0 [45.8, 60.1] | 23.8 [17.3, 30.4] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | AAAAB | 4 | 168 | 50.6 [42.9, 58.3] | 28.6 [21.4, 35.7] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | BAAAA | 0 | 168 | 53.0 [45.8, 60.1] | 18.5 [12.5, 24.4] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | BAAAA | 1 | 168 | 56.0 [48.2, 63.1] | 20.8 [14.9, 27.4] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | BAAAA | 2 | 168 | 51.2 [43.5, 58.3] | 20.8 [14.9, 26.8] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | BAAAA | 3 | 168 | 55.4 [47.6, 63.1] | 20.8 [14.9, 27.4] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Seen | TF one-shot | BAAAA | 4 | 168 | 54.8 [47.0, 61.9] | 21.4 [15.5, 27.4] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | Adversarial | 0 | 668 | 43.0 [39.1, 46.9] | 32.6 [29.2, 36.1] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | Adversarial | 1 | 668 | 42.2 [38.6, 46.0] | 33.7 [30.2, 37.4] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | Adversarial | 2 | 668 | 40.9 [37.1, 44.6] | 36.7 [33.1, 40.4] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | Adversarial | 3 | 668 | 38.3 [34.7, 42.1] | 38.2 [34.7, 41.9] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | Adversarial | 4 | 668 | 40.1 [36.5, 43.7] | 38.9 [35.3, 42.7] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | AAAAB | 0 | 334 | 42.8 [37.4, 48.2] | 32.9 [28.1, 38.0] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | AAAAB | 1 | 334 | 41.3 [35.9, 46.7] | 33.2 [28.1, 38.3] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | AAAAB | 2 | 334 | 39.8 [34.4, 45.2] | 36.8 [31.4, 41.9] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | AAAAB | 3 | 334 | 35.3 [29.9, 40.4] | 40.4 [35.3, 45.8] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | AAAAB | 4 | 334 | 37.4 [32.3, 42.5] | 42.5 [37.1, 47.9] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | BAAAA | 0 | 334 | 43.1 [37.7, 48.5] | 32.3 [26.9, 37.1] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | BAAAA | 1 | 334 | 43.1 [37.7, 48.5] | 34.1 [29.3, 39.2] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | BAAAA | 2 | 334 | 41.9 [36.5, 47.3] | 36.5 [31.4, 41.9] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | BAAAA | 3 | 334 | 41.3 [36.2, 47.0] | 35.9 [30.8, 41.0] | 0.0 [0.0, 0.0] |
| mimo-rl-2508 | Unseen | TF one-shot | BAAAA | 4 | 334 | 42.8 [37.7, 48.5] | 35.3 [30.2, 40.4] | 0.0 [0.0, 0.0] |

## Figure 4 tests: labels given against none

Images with every dose point (tolerant). slope = per-image least-squares change per label given (0-4), in points, permutation p (doses shuffled within image). 4 vs 0 = all four labels against none, paired, exact McNemar. Holm per model and outcome.

| model | split | probe | order | n img | B=A slope / label [CI] | p (Holm) | B=A 4 vs 0 [CI] | p (Holm) | acc slope / label [CI] | p (Holm) | acc 4 vs 0 [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | TF one-shot | Adversarial | 336 | +1.4 [+0.6, +2.1] | 3.0e-04 (0.0012) | +6.0 [+2.4, +9.5] | 0.00222 (0.0444) | -1.0 [-1.9, -0.1] | 0.0188 (0.0564) | -3.6 [-7.4, +0.6] | 0.104 (1) |
| mimo-rl-2508 | Seen | TF one-shot | AAAAB | 168 | +2.1 [+0.9, +3.4] | 4.0e-04 (0.0012) | +8.9 [+3.6, +14.9] | 0.00408 (0.0775) | -2.3 [-3.6, -1.0] | 3.0e-04 (0.0015) | -8.9 [-14.9, -3.6] | 0.00408 (0.0897) |
| mimo-rl-2508 | Seen | TF one-shot | BAAAA | 168 | +0.6 [-0.3, +1.5] | 0.208 (0.208) | +3.0 [-1.2, +7.1] | 0.302 (1) | +0.3 [-0.9, +1.5] | 0.622 (1) | +1.8 [-3.6, +7.1] | 0.664 (1) |
| mimo-rl-2508 | Unseen | TF one-shot | Adversarial | 668 | +1.7 [+1.1, +2.3] | 1.0e-04 (6.0e-04) | +6.3 [+3.6, +9.1] | 1.1e-05 (2.5e-04) | -1.0 [-1.6, -0.3] | 0.0023 (0.0092) | -2.8 [-5.7, +0.1] | 0.0614 (1) |
| mimo-rl-2508 | Unseen | TF one-shot | AAAAB | 334 | +2.6 [+1.7, +3.6] | 1.0e-04 (6.0e-04) | +9.6 [+5.7, +13.8] | 5.6e-06 (1.3e-04) | -1.7 [-2.6, -0.9] | 2.0e-04 (0.0012) | -5.4 [-9.6, -1.5] | 0.0133 (0.279) |
| mimo-rl-2508 | Unseen | TF one-shot | BAAAA | 334 | +0.8 [-0.0, +1.6] | 0.0505 (0.101) | +3.0 [-0.6, +6.6] | 0.154 (1) | -0.2 [-1.1, +0.7] | 0.591 (1) | -0.3 [-4.2, +3.6] | 1 (1) |

