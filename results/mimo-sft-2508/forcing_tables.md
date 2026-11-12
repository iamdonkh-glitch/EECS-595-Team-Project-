# RQ2 forcing probes

Files (16): forcing_cffar_mimo-sft-2508_train.jsonl, forcing_cffar_mimo-sft-2508_validation.jsonl, forcing_cfnear_mimo-sft-2508_train.jsonl, forcing_cfnear_mimo-sft-2508_validation.jsonl, forcing_dose_mimo-sft-2508_train.jsonl, forcing_dose_mimo-sft-2508_validation.jsonl, forcing_homog_mimo-sft-2508_train.jsonl, forcing_homog_mimo-sft-2508_validation.jsonl, forcing_mimo-sft-2508_cf_train.jsonl, forcing_mimo-sft-2508_cf_validation.jsonl, forcing_mimo-sft-2508_tf-incremental_train.jsonl, forcing_mimo-sft-2508_tf-incremental_validation.jsonl, forcing_mimo-sft-2508_tf-oneshot_train.jsonl, forcing_mimo-sft-2508_tf-oneshot_validation.jsonl, forcing_place_mimo-sft-2508_train.jsonl, forcing_place_mimo-sft-2508_validation.jsonl

## Table 4: the odd object B under each condition (%)

B acc = B named correctly; B=A = B given the class of the other four (inertia); B=C = B given the counterfactual class. Tolerant parse, strict in parentheses. cut = calls for B at the token limit (scored wrong). vs default = paired on the same images, y - x in points; p = exact McNemar, Holm over the model's comparisons in the same probe family (core = single, TF incremental, TF one-shot, CF; dose = given=0-3; placement = assistant; C near/far; Homogeneous control).

| model | split | order | condition | n img | cut | B acc [95% CI] | B=A [95% CI] | B=C | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | Seen | Adversarial | TF incremental | 336 | 7 | 44.9 (44.0) [39.6, 50.3] | 33.3 (31.8) [28.6, 38.7] | - | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot | 336 | 5 | 47.0 (47.0) [41.7, 52.4] | 33.3 (33.3) [28.3, 38.1] | - | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | CF | 336 | 7 | 46.4 (46.4) [41.1, 51.8] | 28.0 (28.0) [23.2, 32.7] | 1.2 (1.2) | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | CF near | 336 | 4 | 48.8 (48.8) [43.5, 53.9] | 25.3 (25.3) [20.8, 30.1] | 5.4 (5.4) | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | CF far | 336 | 3 | 48.8 (48.8) [43.5, 54.2] | 28.6 (28.6) [23.8, 33.6] | 0.9 (0.9) | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | CF, assistant | 336 | 5 | 15.5 (15.5) [11.6, 19.3] | 0.0 (0.0) [0.0, 0.0] | 79.8 (79.8) | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, assistant | 336 | 10 | 46.1 (46.1) [41.1, 51.8] | 31.5 (31.5) [26.5, 36.3] | - | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=0 | 336 | 9 | 53.0 (53.0) [47.9, 58.3] | 21.4 (21.4) [17.3, 25.9] | - | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=1 | 336 | 3 | 53.9 (53.9) [48.5, 59.2] | 22.0 (22.0) [17.9, 26.5] | - | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=2 | 336 | 5 | 53.9 (53.9) [48.8, 58.9] | 22.9 (22.9) [18.5, 27.4] | - | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=3 | 336 | 5 | 50.0 (50.0) [44.9, 55.1] | 27.1 (27.1) [22.3, 31.8] | - | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF incremental | 168 | 1 | 36.9 (35.1) [29.8, 44.0] | 45.2 (42.3) [38.1, 52.4] | - | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot | 168 | 2 | 39.9 (39.9) [32.7, 47.0] | 42.9 (42.9) [35.1, 50.6] | - | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | CF | 168 | 2 | 41.7 (41.7) [34.5, 49.4] | 34.5 (34.5) [27.4, 41.7] | 2.4 (2.4) | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | CF near | 168 | 2 | 42.9 (42.9) [35.7, 50.6] | 29.2 (29.2) [22.0, 35.7] | 8.9 (8.9) | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | CF far | 168 | 1 | 47.0 (47.0) [39.3, 54.2] | 34.5 (34.5) [27.4, 41.7] | 0.6 (0.6) | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | CF, assistant | 168 | 2 | 20.2 (20.2) [14.3, 26.2] | 0.0 (0.0) [0.0, 0.0] | 75.0 (75.0) | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, assistant | 168 | 2 | 43.5 (43.5) [35.7, 51.2] | 35.7 (35.7) [28.6, 43.5] | - | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=0 | 168 | 5 | 52.4 (52.4) [44.6, 60.1] | 21.4 (21.4) [15.5, 28.0] | - | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=1 | 168 | 2 | 53.6 (53.6) [46.4, 60.7] | 23.8 (23.8) [17.9, 30.4] | - | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=2 | 168 | 1 | 54.8 (54.8) [47.0, 62.5] | 24.4 (24.4) [18.5, 31.0] | - | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=3 | 168 | 1 | 46.4 (46.4) [39.3, 54.2] | 32.1 (32.1) [25.0, 39.3] | - | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF incremental | 168 | 6 | 53.0 (53.0) [45.2, 60.1] | 21.4 (21.4) [15.5, 27.4] | - | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot | 168 | 3 | 54.2 (54.2) [46.4, 61.9] | 23.8 (23.8) [17.9, 30.4] | - | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | CF | 168 | 5 | 51.2 (51.2) [44.0, 58.3] | 21.4 (21.4) [15.5, 27.4] | 0.0 (0.0) | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | CF near | 168 | 2 | 54.8 (54.8) [47.0, 61.9] | 21.4 (21.4) [15.5, 28.6] | 1.8 (1.8) | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | CF far | 168 | 2 | 50.6 (50.6) [42.9, 57.7] | 22.6 (22.6) [16.7, 28.6] | 1.2 (1.2) | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | CF, assistant | 168 | 3 | 10.7 (10.7) [6.0, 15.5] | 0.0 (0.0) [0.0, 0.0] | 84.5 (84.5) | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, assistant | 168 | 8 | 48.8 (48.8) [41.7, 56.5] | 27.4 (27.4) [20.8, 34.5] | - | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=0 | 168 | 4 | 53.6 (53.6) [46.4, 61.3] | 21.4 (21.4) [15.5, 28.0] | - | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=1 | 168 | 1 | 54.2 (54.2) [46.4, 61.3] | 20.2 (20.2) [14.3, 26.8] | - | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=2 | 168 | 4 | 53.0 (53.0) [45.2, 60.7] | 21.4 (21.4) [15.5, 28.0] | - | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=3 | 168 | 4 | 53.6 (53.6) [45.8, 61.3] | 22.0 (22.0) [16.1, 28.6] | - | - | - | - | - |
| mimo-sft-2508 | Seen | Homogeneous control | TF one-shot | 400 | 1 | 95.2 (95.2) [93.0, 97.2] | - | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF incremental | 668 | 22 | 36.5 (35.5) [32.8, 40.1] | 42.1 (40.7) [38.2, 45.8] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot | 668 | 9 | 37.4 (37.4) [33.7, 41.0] | 43.0 (43.0) [39.1, 46.6] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | CF | 668 | 19 | 38.2 (38.2) [34.6, 41.8] | 39.2 (39.2) [35.6, 43.0] | 1.2 (1.2) | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | CF near | 668 | 14 | 36.2 (36.2) [32.8, 40.0] | 38.3 (38.3) [34.6, 42.1] | 4.9 (4.9) | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | CF far | 668 | 18 | 37.9 (37.9) [34.3, 41.6] | 40.3 (40.3) [36.2, 43.9] | 1.0 (1.0) | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | CF, assistant | 668 | 34 | 9.1 (9.1) [7.2, 11.2] | 0.4 (0.4) [0.0, 1.0] | 82.8 (82.8) | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, assistant | 668 | 26 | 37.7 (37.7) [34.0, 41.3] | 44.6 (44.6) [40.7, 48.2] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=0 | 668 | 27 | 43.1 (43.1) [39.5, 46.9] | 32.6 (32.6) [29.0, 36.1] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=1 | 668 | 27 | 42.4 (42.4) [38.6, 45.8] | 35.2 (35.2) [31.6, 38.8] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=2 | 668 | 28 | 40.3 (40.3) [36.4, 44.2] | 37.1 (37.1) [33.5, 40.6] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=3 | 668 | 16 | 39.2 (39.2) [35.5, 43.0] | 41.0 (41.0) [37.1, 44.9] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF incremental | 334 | 4 | 30.5 (28.4) [25.7, 35.9] | 51.2 (48.5) [46.1, 56.6] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot | 334 | 1 | 30.8 (30.8) [25.7, 35.9] | 51.5 (51.5) [46.1, 56.6] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | CF | 334 | 6 | 35.0 (35.0) [30.2, 40.1] | 43.1 (43.1) [38.0, 48.2] | 1.8 (1.8) | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | CF near | 334 | 5 | 29.9 (29.9) [25.1, 35.0] | 43.4 (43.4) [38.3, 48.5] | 6.9 (6.9) | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | CF far | 334 | 8 | 33.8 (33.8) [29.0, 39.2] | 43.4 (43.4) [38.3, 48.8] | 1.8 (1.8) | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | CF, assistant | 334 | 21 | 11.1 (11.1) [7.8, 14.7] | 0.0 (0.0) [0.0, 0.0] | 79.0 (79.0) | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, assistant | 334 | 15 | 32.3 (32.3) [27.5, 37.4] | 49.1 (49.1) [43.7, 54.8] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=0 | 334 | 15 | 42.2 (42.2) [37.1, 47.6] | 32.0 (32.0) [27.2, 37.1] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=1 | 334 | 13 | 39.8 (39.8) [34.4, 44.9] | 37.7 (37.7) [32.6, 42.8] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=2 | 334 | 13 | 38.0 (38.0) [32.6, 42.8] | 40.4 (40.4) [35.0, 45.8] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=3 | 334 | 6 | 33.2 (33.2) [28.4, 38.3] | 48.5 (48.5) [43.1, 53.9] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF incremental | 334 | 18 | 42.5 (42.5) [37.4, 47.9] | 32.9 (32.9) [27.8, 37.7] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot | 334 | 8 | 44.0 (44.0) [38.6, 49.1] | 34.4 (34.4) [29.3, 39.5] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | CF | 334 | 13 | 41.3 (41.3) [35.9, 46.4] | 35.3 (35.3) [30.2, 40.4] | 0.6 (0.6) | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | CF near | 334 | 9 | 42.5 (42.5) [37.1, 47.9] | 33.2 (33.2) [28.1, 38.3] | 3.0 (3.0) | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | CF far | 334 | 10 | 41.9 (41.9) [36.5, 47.3] | 37.1 (37.1) [31.7, 42.2] | 0.3 (0.3) | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | CF, assistant | 334 | 13 | 7.2 (7.2) [4.5, 9.9] | 0.9 (0.9) [0.0, 1.8] | 86.5 (86.5) | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, assistant | 334 | 11 | 43.1 (43.1) [37.7, 48.2] | 40.1 (40.1) [34.7, 45.2] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=0 | 334 | 12 | 44.0 (44.0) [38.6, 49.1] | 33.2 (33.2) [28.4, 38.6] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=1 | 334 | 14 | 44.9 (44.9) [39.5, 50.6] | 32.6 (32.6) [27.8, 37.4] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=2 | 334 | 15 | 42.5 (42.5) [37.1, 47.9] | 33.8 (33.8) [28.4, 39.2] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=3 | 334 | 10 | 45.2 (45.2) [39.8, 50.6] | 33.5 (33.5) [28.1, 38.6] | - | - | - | - | - |
| mimo-sft-2508 | Unseen | Homogeneous control | TF one-shot | 490 | 1 | 88.2 (88.2) [85.3, 91.0] | - | - | - | - | - | - |

## Assistant-turn prefill: the forced line, then the model's own re-check (%)

first = the label written right after the prefill (the one Table 4 uses); kept writing = the model went on after it (typically "Wait, no, that's wrong" and a re-check); restarted = wrote no label after the forced "objK:" and began its own five-label list on a new line (counted in kept writing; first counts as wrong and not A); final = obj K's last "objK: <class>" in the answer (= first when it stopped); unresolved = kept writing but gave no final label for B, or hit the token limit. cut = thinking never closed. All over n img, tolerant.

| model | split | order | condition | n img | cut | first: B acc | first: B=A | first: B=C | kept writing | restarted | final: B acc | final: B=A | final: B=C | unresolved |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | Seen | Adversarial | CF, assistant | 336 | 5 | 15.5 | 0.0 | 79.8 | 0.0 | 0.0 | 15.5 | 0.0 | 79.8 | 0.0 |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, assistant | 336 | 10 | 46.1 | 31.5 | - | 0.3 | 0.0 | 46.4 | 31.5 | - | 0.0 |
| mimo-sft-2508 | Seen | AAAAB | CF, assistant | 168 | 2 | 20.2 | 0.0 | 75.0 | 0.0 | 0.0 | 20.2 | 0.0 | 75.0 | 0.0 |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, assistant | 168 | 2 | 43.5 | 35.7 | - | 0.6 | 0.0 | 44.0 | 35.7 | - | 0.0 |
| mimo-sft-2508 | Seen | BAAAA | CF, assistant | 168 | 3 | 10.7 | 0.0 | 84.5 | 0.0 | 0.0 | 10.7 | 0.0 | 84.5 | 0.0 |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, assistant | 168 | 8 | 48.8 | 27.4 | - | 0.0 | 0.0 | 48.8 | 27.4 | - | 0.0 |
| mimo-sft-2508 | Unseen | Adversarial | CF, assistant | 668 | 34 | 9.1 | 0.4 | 82.8 | 0.0 | 0.0 | 9.1 | 0.4 | 82.8 | 0.0 |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, assistant | 668 | 26 | 37.7 | 44.6 | - | 0.1 | 0.0 | 37.6 | 44.6 | - | 0.0 |
| mimo-sft-2508 | Unseen | AAAAB | CF, assistant | 334 | 21 | 11.1 | 0.0 | 79.0 | 0.0 | 0.0 | 11.1 | 0.0 | 79.0 | 0.0 |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, assistant | 334 | 15 | 32.3 | 49.1 | - | 0.3 | 0.0 | 32.0 | 49.1 | - | 0.0 |
| mimo-sft-2508 | Unseen | BAAAA | CF, assistant | 334 | 13 | 7.2 | 0.9 | 86.5 | 0.0 | 0.0 | 7.2 | 0.9 | 86.5 | 0.0 |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, assistant | 334 | 11 | 43.1 | 40.1 | - | 0.0 | 0.0 | 43.1 | 40.1 | - | 0.0 |

## What the answer does with the given boxes (one-shot, labels in the user turn; %)

Over answered rows (calls for B not cut), tolerant parse, last objK: mention per box. B read before objK: = the answer has no objK: for B but writes B's label first and then other boxes (it continues the prompt's last "objK:"), and B's label was read from that first segment (see asked_label); writes all 5 = a label for every box, i.e. the model rewrites the list instead of answering only B; keeps given = every given box keeps its given label; given boxes = A = every given box is labelled A; C kept = C stays on at least one given box (CF only). '-' = no label given (n = 0).

| model | split | order | condition | n answered | B read before objK: | writes all 5 | keeps given | given boxes = A | C kept |
|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | Seen | Adversarial | TF one-shot | 331 | 0.0 | 100.0 | 89.7 | 89.7 | - |
| mimo-sft-2508 | Seen | Adversarial | CF | 329 | 0.0 | 100.0 | 2.4 | 69.6 | 3.6 |
| mimo-sft-2508 | Seen | Adversarial | CF near | 332 | 0.0 | 100.0 | 21.7 | 52.1 | 29.8 |
| mimo-sft-2508 | Seen | Adversarial | CF far | 333 | 0.0 | 100.0 | 0.9 | 65.5 | 2.4 |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=0 | 327 | 0.0 | - | - | - | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=1 | 333 | 0.0 | 100.0 | 92.5 | 92.5 | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=2 | 331 | 0.0 | 100.0 | 90.9 | 90.9 | - |
| mimo-sft-2508 | Seen | Adversarial | TF one-shot, given=3 | 331 | 0.0 | 100.0 | 89.1 | 89.1 | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot | 166 | 0.0 | 100.0 | 92.2 | 92.2 | - |
| mimo-sft-2508 | Seen | AAAAB | CF | 166 | 0.0 | 100.0 | 4.2 | 70.5 | 4.8 |
| mimo-sft-2508 | Seen | AAAAB | CF near | 166 | 0.0 | 100.0 | 22.3 | 53.0 | 28.9 |
| mimo-sft-2508 | Seen | AAAAB | CF far | 167 | 0.0 | 100.0 | 0.6 | 66.5 | 1.8 |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=0 | 163 | 0.0 | - | - | - | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=1 | 166 | 0.0 | 100.0 | 92.2 | 92.2 | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=2 | 167 | 0.0 | 100.0 | 91.0 | 91.0 | - |
| mimo-sft-2508 | Seen | AAAAB | TF one-shot, given=3 | 167 | 0.0 | 100.0 | 91.6 | 91.6 | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot | 165 | 0.0 | 100.0 | 87.3 | 87.3 | - |
| mimo-sft-2508 | Seen | BAAAA | CF | 163 | 0.0 | 100.0 | 0.6 | 68.7 | 2.5 |
| mimo-sft-2508 | Seen | BAAAA | CF near | 166 | 0.0 | 100.0 | 21.1 | 51.2 | 30.7 |
| mimo-sft-2508 | Seen | BAAAA | CF far | 166 | 0.0 | 100.0 | 1.2 | 64.5 | 3.0 |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=0 | 164 | 0.0 | - | - | - | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=1 | 167 | 0.0 | 100.0 | 92.8 | 92.8 | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=2 | 164 | 0.0 | 100.0 | 90.9 | 90.9 | - |
| mimo-sft-2508 | Seen | BAAAA | TF one-shot, given=3 | 164 | 0.0 | 100.0 | 86.6 | 86.6 | - |
| mimo-sft-2508 | Seen | Homogeneous control | TF one-shot | 399 | 0.0 | 100.0 | 97.0 | 97.0 | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot | 659 | 0.0 | 100.0 | 82.1 | 82.1 | - |
| mimo-sft-2508 | Unseen | Adversarial | CF | 649 | 0.0 | 100.0 | 2.0 | 63.8 | 3.4 |
| mimo-sft-2508 | Unseen | Adversarial | CF near | 654 | 0.0 | 100.0 | 9.2 | 60.9 | 12.8 |
| mimo-sft-2508 | Unseen | Adversarial | CF far | 650 | 0.0 | 100.0 | 1.1 | 62.9 | 1.8 |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=0 | 641 | 0.0 | - | - | - | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=1 | 641 | 0.0 | 100.0 | 85.3 | 85.3 | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=2 | 640 | 0.0 | 99.7 | 84.4 | 84.4 | - |
| mimo-sft-2508 | Unseen | Adversarial | TF one-shot, given=3 | 652 | 0.0 | 100.0 | 82.8 | 82.8 | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot | 333 | 0.0 | 100.0 | 83.5 | 83.5 | - |
| mimo-sft-2508 | Unseen | AAAAB | CF | 328 | 0.0 | 100.0 | 2.1 | 63.7 | 4.0 |
| mimo-sft-2508 | Unseen | AAAAB | CF near | 329 | 0.0 | 100.0 | 12.2 | 58.7 | 14.3 |
| mimo-sft-2508 | Unseen | AAAAB | CF far | 326 | 0.0 | 100.0 | 1.5 | 62.0 | 2.5 |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=0 | 319 | 0.0 | - | - | - | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=1 | 321 | 0.0 | 100.0 | 85.0 | 85.0 | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=2 | 321 | 0.0 | 99.4 | 83.2 | 83.2 | - |
| mimo-sft-2508 | Unseen | AAAAB | TF one-shot, given=3 | 328 | 0.0 | 100.0 | 82.6 | 82.6 | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot | 326 | 0.0 | 100.0 | 80.7 | 80.7 | - |
| mimo-sft-2508 | Unseen | BAAAA | CF | 321 | 0.0 | 100.0 | 1.9 | 63.9 | 2.8 |
| mimo-sft-2508 | Unseen | BAAAA | CF near | 325 | 0.0 | 100.0 | 6.2 | 63.1 | 11.4 |
| mimo-sft-2508 | Unseen | BAAAA | CF far | 324 | 0.0 | 100.0 | 0.6 | 63.9 | 1.2 |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=0 | 322 | 0.0 | - | - | - | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=1 | 320 | 0.0 | 100.0 | 85.6 | 85.6 | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=2 | 319 | 0.0 | 100.0 | 85.6 | 85.6 | - |
| mimo-sft-2508 | Unseen | BAAAA | TF one-shot, given=3 | 324 | 0.0 | 100.0 | 83.0 | 83.0 | - |
| mimo-sft-2508 | Unseen | Homogeneous control | TF one-shot | 489 | 0.0 | 100.0 | 89.8 | 89.8 | - |

## C near / far: does a C closer to A get copied more?

Paired on the same images, y - x in points, tolerant; B=C = B given the injected class of that condition. Exact McNemar, Holm per model and outcome over these comparisons.

| model | split | order | x | y | n img | B=C y - x [CI] | p (Holm) | B=A y - x [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | Seen | Adversarial | CF | CF near | 336 | +4.2 [+1.5, +6.8] | 0.00434 (0.0521) | -2.7 [-6.2, +1.2] | 0.2 (1) |
| mimo-sft-2508 | Seen | Adversarial | CF | CF far | 336 | -0.3 [-1.8, +1.2] | 1 (1) | +0.6 [-2.7, +3.9] | 0.86 (1) |
| mimo-sft-2508 | Seen | Adversarial | CF near | CF far | 336 | -4.5 [-7.4, -2.1] | 0.00149 (0.0209) | +3.3 [-0.6, +7.1] | 0.108 (1) |
| mimo-sft-2508 | Seen | AAAAB | CF | CF near | 168 | +6.5 [+1.8, +11.9] | 0.0192 (0.192) | -5.4 [-11.3, +0.0] | 0.108 (1) |
| mimo-sft-2508 | Seen | AAAAB | CF | CF far | 168 | -1.8 [-4.8, +0.6] | 0.375 (1) | +0.0 [-4.2, +4.8] | 1 (1) |
| mimo-sft-2508 | Seen | AAAAB | CF near | CF far | 168 | -8.3 [-13.1, -4.2] | 5.2e-04 (0.00778) | +5.4 [+0.0, +11.3] | 0.108 (1) |
| mimo-sft-2508 | Seen | BAAAA | CF | CF near | 168 | +1.8 [+0.0, +4.2] | 0.25 (1) | +0.0 [-4.2, +4.2] | 1 (1) |
| mimo-sft-2508 | Seen | BAAAA | CF | CF far | 168 | +1.2 [+0.0, +3.0] | 0.5 (1) | +1.2 [-3.6, +6.0] | 0.804 (1) |
| mimo-sft-2508 | Seen | BAAAA | CF near | CF far | 168 | -0.6 [-3.0, +1.8] | 1 (1) | +1.2 [-3.0, +5.4] | 0.791 (1) |
| mimo-sft-2508 | Unseen | Adversarial | CF | CF near | 668 | +3.7 [+2.2, +5.2] | 4.6e-06 (8.4e-05) | -0.9 [-3.4, +1.6] | 0.581 (1) |
| mimo-sft-2508 | Unseen | Adversarial | CF | CF far | 668 | -0.1 [-1.2, +0.9] | 1 (1) | +1.0 [-1.3, +3.3] | 0.45 (1) |
| mimo-sft-2508 | Unseen | Adversarial | CF near | CF far | 668 | -3.9 [-5.7, -2.2] | 2.4e-05 (4.1e-04) | +1.9 [-0.9, +4.8] | 0.203 (1) |
| mimo-sft-2508 | Unseen | AAAAB | CF | CF near | 334 | +5.1 [+2.7, +7.8] | 2.2e-04 (0.00354) | +0.3 [-3.9, +4.5] | 1 (1) |
| mimo-sft-2508 | Unseen | AAAAB | CF | CF far | 334 | +0.0 [-1.8, +1.8] | 1 (1) | +0.3 [-3.6, +3.9] | 1 (1) |
| mimo-sft-2508 | Unseen | AAAAB | CF near | CF far | 334 | -5.1 [-8.1, -2.1] | 0.00151 (0.0209) | +0.0 [-4.5, +4.2] | 1 (1) |
| mimo-sft-2508 | Unseen | BAAAA | CF | CF near | 334 | +2.4 [+0.6, +4.2] | 0.0215 (0.193) | -2.1 [-5.4, +1.2] | 0.296 (1) |
| mimo-sft-2508 | Unseen | BAAAA | CF | CF far | 334 | -0.3 [-1.2, +0.6] | 1 (1) | +1.8 [-0.9, +4.8] | 0.307 (1) |
| mimo-sft-2508 | Unseen | BAAAA | CF near | CF far | 334 | -2.7 [-4.8, -0.9] | 0.0117 (0.129) | +3.9 [+0.6, +7.2] | 0.0351 (0.631) |

## Figure 4 data: dose-response (tolerant, %)

| model | split | probe | order | labels given | n img | B acc [95% CI] | B=A [95% CI] | B=C [95% CI] |
|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | Seen | TF one-shot | Adversarial | 0 | 336 | 53.0 [47.9, 58.3] | 21.4 [17.3, 25.9] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | Adversarial | 1 | 336 | 53.9 [48.5, 59.2] | 22.0 [17.9, 26.5] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | Adversarial | 2 | 336 | 53.9 [48.8, 58.9] | 22.9 [18.5, 27.4] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | Adversarial | 3 | 336 | 50.0 [44.9, 55.1] | 27.1 [22.3, 31.8] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | Adversarial | 4 | 336 | 47.0 [41.7, 52.4] | 33.3 [28.3, 38.1] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | AAAAB | 0 | 168 | 52.4 [44.6, 60.1] | 21.4 [15.5, 28.0] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | AAAAB | 1 | 168 | 53.6 [46.4, 60.7] | 23.8 [17.9, 30.4] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | AAAAB | 2 | 168 | 54.8 [47.0, 62.5] | 24.4 [18.5, 31.0] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | AAAAB | 3 | 168 | 46.4 [39.3, 54.2] | 32.1 [25.0, 39.3] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | AAAAB | 4 | 168 | 39.9 [32.7, 47.0] | 42.9 [35.1, 50.6] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | BAAAA | 0 | 168 | 53.6 [46.4, 61.3] | 21.4 [15.5, 28.0] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | BAAAA | 1 | 168 | 54.2 [46.4, 61.3] | 20.2 [14.3, 26.8] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | BAAAA | 2 | 168 | 53.0 [45.2, 60.7] | 21.4 [15.5, 28.0] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | BAAAA | 3 | 168 | 53.6 [45.8, 61.3] | 22.0 [16.1, 28.6] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Seen | TF one-shot | BAAAA | 4 | 168 | 54.2 [46.4, 61.9] | 23.8 [17.9, 30.4] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | Adversarial | 0 | 668 | 43.1 [39.5, 46.9] | 32.6 [29.0, 36.1] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | Adversarial | 1 | 668 | 42.4 [38.6, 45.8] | 35.2 [31.6, 38.8] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | Adversarial | 2 | 668 | 40.3 [36.4, 44.2] | 37.1 [33.5, 40.6] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | Adversarial | 3 | 668 | 39.2 [35.5, 43.0] | 41.0 [37.1, 44.9] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | Adversarial | 4 | 668 | 37.4 [33.7, 41.0] | 43.0 [39.1, 46.6] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | AAAAB | 0 | 334 | 42.2 [37.1, 47.6] | 32.0 [27.2, 37.1] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | AAAAB | 1 | 334 | 39.8 [34.4, 44.9] | 37.7 [32.6, 42.8] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | AAAAB | 2 | 334 | 38.0 [32.6, 42.8] | 40.4 [35.0, 45.8] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | AAAAB | 3 | 334 | 33.2 [28.4, 38.3] | 48.5 [43.1, 53.9] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | AAAAB | 4 | 334 | 30.8 [25.7, 35.9] | 51.5 [46.1, 56.6] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | BAAAA | 0 | 334 | 44.0 [38.6, 49.1] | 33.2 [28.4, 38.6] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | BAAAA | 1 | 334 | 44.9 [39.5, 50.6] | 32.6 [27.8, 37.4] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | BAAAA | 2 | 334 | 42.5 [37.1, 47.9] | 33.8 [28.4, 39.2] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | BAAAA | 3 | 334 | 45.2 [39.8, 50.6] | 33.5 [28.1, 38.6] | 0.0 [0.0, 0.0] |
| mimo-sft-2508 | Unseen | TF one-shot | BAAAA | 4 | 334 | 44.0 [38.6, 49.1] | 34.4 [29.3, 39.5] | 0.0 [0.0, 0.0] |

## Figure 4 tests: labels given against none

Images with every dose point (tolerant). slope = per-image least-squares change per label given (0-4), in points, permutation p (doses shuffled within image). 4 vs 0 = all four labels against none, paired, exact McNemar. Holm per model and outcome.

| model | split | probe | order | n img | B=A slope / label [CI] | p (Holm) | B=A 4 vs 0 [CI] | p (Holm) | acc slope / label [CI] | p (Holm) | acc 4 vs 0 [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | Seen | TF one-shot | Adversarial | 336 | +2.9 [+1.9, +3.9] | 1.0e-04 (6.0e-04) | +11.9 [+7.7, +16.4] | 1.6e-07 (3.1e-06) | -1.6 [-2.6, -0.6] | 2.0e-04 (6.0e-04) | -6.0 [-10.4, -1.5] | 0.0105 (0.209) |
| mimo-sft-2508 | Seen | TF one-shot | AAAAB | 168 | +5.1 [+3.5, +6.7] | 1.0e-04 (6.0e-04) | +21.4 [+14.9, +28.0] | 5.6e-09 (1.2e-07) | -3.2 [-4.8, -1.7] | 1.0e-04 (6.0e-04) | -12.5 [-19.1, -5.9] | 7.5e-04 (0.0158) |
| mimo-sft-2508 | Seen | TF one-shot | BAAAA | 168 | +0.7 [-0.5, +1.7] | 0.184 (0.368) | +2.4 [-2.4, +7.1] | 0.481 (1) | +0.1 [-1.0, +1.2] | 0.948 (1) | +0.6 [-4.8, +5.4] | 1 (1) |
| mimo-sft-2508 | Unseen | TF one-shot | Adversarial | 668 | +2.6 [+1.9, +3.3] | 1.0e-04 (6.0e-04) | +10.3 [+7.3, +13.5] | 8.9e-11 (2.0e-09) | -1.5 [-2.1, -0.8] | 1.0e-04 (6.0e-04) | -5.7 [-9.0, -2.5] | 6.7e-04 (0.0147) |
| mimo-sft-2508 | Unseen | TF one-shot | AAAAB | 334 | +5.0 [+3.9, +6.1] | 1.0e-04 (6.0e-04) | +19.5 [+14.4, +24.6] | 3.0e-14 (7.1e-13) | -2.9 [-4.0, -1.9] | 1.0e-04 (6.0e-04) | -11.4 [-15.9, -6.9] | 8.1e-06 (2.0e-04) |
| mimo-sft-2508 | Unseen | TF one-shot | BAAAA | 334 | +0.3 [-0.5, +1.1] | 0.383 (0.383) | +1.2 [-2.4, +4.8] | 0.618 (1) | +0.0 [-0.8, +0.9] | 0.97 (1) | +0.0 [-3.9, +3.9] | 1 (1) |

