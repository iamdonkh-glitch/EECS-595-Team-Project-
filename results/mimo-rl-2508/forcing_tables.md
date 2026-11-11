# RQ2 forcing probes

Files (10): rq1_mimo-rl-2508_adversarial_default_train.jsonl, rq1_mimo-rl-2508_adversarial_default_validation.jsonl, rq1_mimo-rl-2508_adversarial_single_train.jsonl, rq1_mimo-rl-2508_adversarial_single_validation.jsonl, forcing_mimo-rl-2508_cf_train.jsonl, forcing_mimo-rl-2508_cf_validation.jsonl, forcing_mimo-rl-2508_tf-incremental_train.jsonl, forcing_mimo-rl-2508_tf-incremental_validation.jsonl, forcing_mimo-rl-2508_tf-oneshot_train.jsonl, forcing_mimo-rl-2508_tf-oneshot_validation.jsonl

## Table 4: the odd object B under each condition (%)

B acc = B named correctly; B=A = B given the class of the other four (inertia); B=C = B given the counterfactual class. Tolerant parse, strict in parentheses. cut = calls for B at the token limit (scored wrong). vs default = paired on the same images, y - x in points; p = exact McNemar, Holm over the model's comparisons.

| model | split | order | condition | n img | cut | B acc [95% CI] | B=A [95% CI] | B=C | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | Adversarial | single | 336 | 3 | 61.3 (45.2) [56.2, 66.7] | 14.3 (10.4) [10.7, 18.5] | - | +7.1 [+2.7, +11.9] | 0.00369 (0.0775) | -5.1 [-8.3, -1.8] | 0.00599 (0.0778) |
| mimo-rl-2508 | Seen | Adversarial | default | 336 | 21 | 54.2 (51.8) [49.1, 59.5] | 19.3 (18.8) [15.2, 23.5] | - | - | - | - | - |
| mimo-rl-2508 | Seen | Adversarial | TF incremental | 336 | 13 | 52.1 (38.7) [46.7, 57.4] | 24.7 (18.8) [20.2, 29.5] | - | -2.1 [-6.2, +1.8] | 0.401 (1) | +5.4 [+1.8, +8.9] | 0.00643 (0.0778) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot | 336 | 8 | 52.7 (42.6) [47.3, 58.0] | 25.0 (21.7) [20.5, 29.5] | - | -1.5 [-6.0, +3.0] | 0.603 (1) | +5.7 [+2.1, +9.2] | 0.00432 (0.0605) |
| mimo-rl-2508 | Seen | Adversarial | CF | 336 | 18 | 50.6 (38.4) [44.9, 55.7] | 23.2 (18.2) [18.8, 27.7] | 0.9 (0.6) | -3.6 [-7.7, +0.3] | 0.111 (1) | +3.9 [+0.3, +7.1] | 0.0351 (0.316) |
| mimo-rl-2508 | Seen | AAAAB | single | 168 | 1 | 63.7 (44.0) [56.5, 70.8] | 12.5 (8.9) [7.7, 18.5] | - | +7.1 [+0.6, +14.3] | 0.0652 (1) | -8.3 [-13.7, -3.6] | 0.00258 (0.0393) |
| mimo-rl-2508 | Seen | AAAAB | default | 168 | 9 | 56.5 (52.4) [48.8, 63.7] | 20.8 (20.2) [14.9, 27.4] | - | - | - | - | - |
| mimo-rl-2508 | Seen | AAAAB | TF incremental | 168 | 4 | 51.2 (25.0) [43.5, 58.9] | 28.6 (16.7) [22.0, 35.1] | - | -5.4 [-11.9, +1.2] | 0.163 (1) | +7.7 [+1.8, +13.7] | 0.0192 (0.211) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot | 168 | 5 | 50.6 (41.1) [43.5, 58.3] | 28.6 (25.0) [21.4, 35.1] | - | -6.0 [-13.1, +0.6] | 0.143 (1) | +7.7 [+1.8, +13.7] | 0.0241 (0.241) |
| mimo-rl-2508 | Seen | AAAAB | CF | 168 | 9 | 50.0 (39.3) [42.3, 57.1] | 23.8 (17.3) [17.9, 30.4] | 1.2 (0.6) | -6.5 [-13.1, +0.0] | 0.0708 (1) | +3.0 [-1.8, +7.7] | 0.359 (1) |
| mimo-rl-2508 | Seen | BAAAA | single | 168 | 2 | 58.9 (46.4) [51.2, 66.7] | 16.1 (11.9) [10.7, 21.4] | - | +7.1 [+1.2, +13.1] | 0.0357 (0.714) | -1.8 [-6.0, +3.0] | 0.607 (1) |
| mimo-rl-2508 | Seen | BAAAA | default | 168 | 12 | 51.8 (51.2) [44.6, 59.5] | 17.9 (17.3) [12.5, 23.8] | - | - | - | - | - |
| mimo-rl-2508 | Seen | BAAAA | TF incremental | 168 | 9 | 53.0 (52.4) [45.8, 60.7] | 20.8 (20.8) [14.9, 27.4] | - | +1.2 [-3.6, +6.5] | 0.815 (1) | +3.0 [-1.2, +7.1] | 0.267 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot | 168 | 3 | 54.8 (44.0) [47.6, 62.5] | 21.4 (18.5) [15.5, 28.0] | - | +3.0 [-2.4, +8.3] | 0.383 (1) | +3.6 [+0.0, +7.7] | 0.146 (1) |
| mimo-rl-2508 | Seen | BAAAA | CF | 168 | 9 | 51.2 (37.5) [43.5, 58.9] | 22.6 (19.0) [16.7, 29.2] | 0.6 (0.6) | -0.6 [-5.4, +4.2] | 1 (1) | +4.8 [+0.6, +9.5] | 0.0574 (0.459) |
| mimo-rl-2508 | Unseen | Adversarial | single | 668 | 14 | 55.7 (37.0) [51.8, 59.3] | 21.4 (12.9) [18.4, 24.6] | - | +12.3 [+8.8, +15.7] | 5.4e-12 (1.3e-10) | -9.6 [-12.6, -6.4] | 3.8e-09 (9.0e-08) |
| mimo-rl-2508 | Unseen | Adversarial | default | 668 | 57 | 43.4 (37.3) [39.7, 47.2] | 31.0 (29.2) [27.4, 34.4] | - | - | - | - | - |
| mimo-rl-2508 | Unseen | Adversarial | TF incremental | 668 | 51 | 40.3 (28.7) [36.7, 43.9] | 37.0 (28.0) [33.2, 40.6] | - | -3.1 [-6.3, -0.3] | 0.046 (0.793) | +6.0 [+3.0, +8.8] | 1.1e-04 (0.00208) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot | 668 | 30 | 40.1 (32.3) [36.2, 43.9] | 38.9 (29.9) [35.3, 42.8] | - | -3.3 [-6.1, -0.4] | 0.0371 (0.714) | +7.9 [+4.9, +11.1] | 3.8e-07 (8.3e-06) |
| mimo-rl-2508 | Unseen | Adversarial | CF | 668 | 50 | 40.9 (26.8) [37.3, 44.6] | 35.5 (24.7) [31.7, 39.1] | 0.4 (0.0) | -2.5 [-5.2, +0.1] | 0.0966 (1) | +4.5 [+1.8, +7.3] | 0.00161 (0.0273) |
| mimo-rl-2508 | Unseen | AAAAB | single | 334 | 9 | 57.2 (37.4) [52.4, 62.6] | 18.9 (9.3) [15.0, 23.4] | - | +15.0 [+9.9, +20.1] | 1.4e-08 (3.2e-07) | -10.5 [-15.0, -6.0] | 1.1e-05 (2.2e-04) |
| mimo-rl-2508 | Unseen | AAAAB | default | 334 | 35 | 42.2 (33.2) [36.8, 47.6] | 29.3 (26.3) [24.6, 34.4] | - | - | - | - | - |
| mimo-rl-2508 | Unseen | AAAAB | TF incremental | 334 | 16 | 38.6 (17.1) [33.5, 43.7] | 40.7 (23.4) [35.3, 46.1] | - | -3.6 [-8.1, +1.2] | 0.169 (1) | +11.4 [+6.9, +16.2] | 2.8e-06 (5.9e-05) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot | 334 | 16 | 37.4 (31.4) [32.3, 42.8] | 42.5 (32.9) [37.1, 47.6] | - | -4.8 [-9.0, -0.3] | 0.044 (0.793) | +13.2 [+8.7, +18.0] | 6.2e-08 (1.4e-06) |
| mimo-rl-2508 | Unseen | AAAAB | CF | 334 | 29 | 39.2 (21.9) [33.8, 44.6] | 35.6 (22.8) [30.5, 40.7] | 0.3 (0.0) | -3.0 [-6.9, +1.2] | 0.203 (1) | +6.3 [+2.4, +10.2] | 0.00246 (0.0393) |
| mimo-rl-2508 | Unseen | BAAAA | single | 334 | 5 | 54.2 (36.5) [48.8, 59.6] | 24.0 (16.5) [19.5, 28.4] | - | +9.6 [+4.8, +14.1] | 1.0e-04 (0.00223) | -8.7 [-13.2, -4.8] | 1.5e-04 (0.00277) |
| mimo-rl-2508 | Unseen | BAAAA | default | 334 | 22 | 44.6 (41.3) [39.2, 50.0] | 32.6 (32.0) [27.5, 37.7] | - | - | - | - | - |
| mimo-rl-2508 | Unseen | BAAAA | TF incremental | 334 | 35 | 41.9 (40.4) [36.8, 47.0] | 33.2 (32.6) [28.4, 38.3] | - | -2.7 [-6.3, +0.9] | 0.188 (1) | +0.6 [-3.0, +4.2] | 0.871 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot | 334 | 14 | 42.8 (33.2) [37.7, 47.9] | 35.3 (26.9) [30.2, 41.0] | - | -1.8 [-5.7, +2.1] | 0.461 (1) | +2.7 [-0.9, +6.3] | 0.211 (1) |
| mimo-rl-2508 | Unseen | BAAAA | CF | 334 | 21 | 42.5 (31.7) [37.4, 47.9] | 35.3 (26.6) [30.2, 40.4] | 0.6 (0.0) | -2.1 [-5.7, +1.8] | 0.36 (1) | +2.7 [-0.9, +6.3] | 0.211 (1) |

## Table 4, sensitivity: images where neither call for B hit the token limit

Same comparisons with default as Table 4 (tolerant, y - x in points, exact McNemar, Holm over the model's comparisons), on the images where neither the condition's nor default's call for B was cut.

| model | split | order | condition | n img | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | Adversarial | single | 314 | +4.5 [+0.0, +8.6] | 0.0759 (0.987) | -6.4 [-9.6, -3.2] | 3.2e-04 (0.00552) |
| mimo-rl-2508 | Seen | Adversarial | TF incremental | 309 | -3.6 [-7.8, +0.3] | 0.117 (1) | +4.5 [+1.0, +8.1] | 0.0243 (0.267) |
| mimo-rl-2508 | Seen | Adversarial | TF one-shot | 310 | -5.2 [-9.4, -1.0] | 0.0293 (0.44) | +5.5 [+1.6, +9.0] | 0.00763 (0.0992) |
| mimo-rl-2508 | Seen | Adversarial | CF | 305 | -3.3 [-7.2, +0.7] | 0.143 (1) | +3.6 [+0.7, +6.9] | 0.0433 (0.39) |
| mimo-rl-2508 | Seen | AAAAB | single | 158 | +4.4 [-2.5, +11.4] | 0.281 (1) | -8.9 [-13.9, -3.8] | 0.00131 (0.021) |
| mimo-rl-2508 | Seen | AAAAB | TF incremental | 158 | -7.6 [-13.9, -1.3] | 0.0357 (0.5) | +7.6 [+1.3, +13.9] | 0.029 (0.29) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot | 155 | -9.7 [-16.8, -2.6] | 0.0135 (0.23) | +8.4 [+1.3, +14.8] | 0.0192 (0.23) |
| mimo-rl-2508 | Seen | AAAAB | CF | 154 | -5.8 [-12.3, +0.6] | 0.108 (1) | +3.2 [-1.9, +8.4] | 0.332 (1) |
| mimo-rl-2508 | Seen | BAAAA | single | 156 | +4.5 [-1.3, +10.9] | 0.21 (1) | -3.8 [-8.3, +0.0] | 0.146 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF incremental | 151 | +0.7 [-4.0, +5.3] | 1 (1) | +1.3 [-2.0, +5.3] | 0.727 (1) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot | 155 | -0.6 [-5.8, +3.9] | 1 (1) | +2.6 [-1.3, +6.5] | 0.344 (1) |
| mimo-rl-2508 | Seen | BAAAA | CF | 151 | -0.7 [-5.3, +4.0] | 1 (1) | +4.0 [+0.7, +7.9] | 0.0703 (0.562) |
| mimo-rl-2508 | Unseen | Adversarial | single | 600 | +8.3 [+5.0, +11.8] | 2.5e-06 (6.1e-05) | -10.7 [-14.0, -7.5] | 6.0e-10 (1.4e-08) |
| mimo-rl-2508 | Unseen | Adversarial | TF incremental | 580 | -4.1 [-7.1, -1.4] | 0.00631 (0.12) | +6.0 [+2.9, +9.0] | 1.5e-04 (0.00278) |
| mimo-rl-2508 | Unseen | Adversarial | TF one-shot | 592 | -4.9 [-7.8, -2.0] | 0.00108 (0.0237) | +6.6 [+3.4, +9.8] | 4.3e-05 (8.6e-04) |
| mimo-rl-2508 | Unseen | Adversarial | CF | 582 | -3.3 [-6.0, -0.5] | 0.0271 (0.434) | +4.5 [+1.7, +7.4] | 0.00255 (0.0382) |
| mimo-rl-2508 | Unseen | AAAAB | single | 293 | +10.2 [+5.1, +15.4] | 1.3e-04 (0.00309) | -11.9 [-16.7, -7.5] | 3.3e-06 (7.6e-05) |
| mimo-rl-2508 | Unseen | AAAAB | TF incremental | 289 | -7.6 [-12.1, -3.1] | 0.00209 (0.0439) | +10.7 [+6.2, +15.9] | 3.3e-05 (6.9e-04) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot | 290 | -6.9 [-11.4, -2.4] | 0.00366 (0.0732) | +11.4 [+6.9, +16.2] | 8.7e-06 (1.9e-04) |
| mimo-rl-2508 | Unseen | AAAAB | CF | 282 | -3.9 [-7.8, +0.0] | 0.0801 (0.987) | +6.0 [+2.1, +10.3] | 0.00599 (0.0838) |
| mimo-rl-2508 | Unseen | BAAAA | single | 307 | +6.5 [+2.0, +11.1] | 0.00779 (0.14) | -9.4 [-14.0, -4.9] | 8.2e-05 (0.00155) |
| mimo-rl-2508 | Unseen | BAAAA | TF incremental | 291 | -0.7 [-3.8, +2.7] | 0.839 (1) | +1.4 [-2.1, +4.8] | 0.572 (1) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot | 302 | -3.0 [-6.3, +0.7] | 0.15 (1) | +2.0 [-1.7, +5.6] | 0.392 (1) |
| mimo-rl-2508 | Unseen | BAAAA | CF | 300 | -2.7 [-6.7, +1.3] | 0.229 (1) | +3.0 [-0.7, +6.7] | 0.175 (1) |

