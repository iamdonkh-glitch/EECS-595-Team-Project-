# RQ2 forcing probes

Files (12): forcing_dose_qwen3vl-8b-thinking_train.jsonl, forcing_dose_qwen3vl-8b-thinking_validation.jsonl, forcing_homog_qwen3vl-8b-thinking_train.jsonl, forcing_homog_qwen3vl-8b-thinking_validation.jsonl, forcing_place_qwen3vl-8b-thinking_train.jsonl, forcing_place_qwen3vl-8b-thinking_validation.jsonl, forcing_qwen3vl-8b-thinking_cf_train.jsonl, forcing_qwen3vl-8b-thinking_cf_validation.jsonl, forcing_qwen3vl-8b-thinking_tf-incremental_train.jsonl, forcing_qwen3vl-8b-thinking_tf-incremental_validation.jsonl, forcing_qwen3vl-8b-thinking_tf-oneshot_train.jsonl, forcing_qwen3vl-8b-thinking_tf-oneshot_validation.jsonl

## Table 4: the odd object B under each condition (%)

B acc = B named correctly; B=A = B given the class of the other four (inertia); B=C = B given the counterfactual class. Tolerant parse, strict in parentheses. cut = calls for B at the token limit (scored wrong). vs default = paired on the same images, y - x in points; p = exact McNemar, Holm over the model's comparisons in the same probe family (core = single, TF incremental, TF one-shot, CF; dose = given=0-3; placement = assistant; C near/far; Homogeneous control).

| model | split | order | condition | n img | cut | B acc [95% CI] | B=A [95% CI] | B=C | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | Adversarial | TF incremental | 336 | 14 | 48.5 (46.4) [43.2, 53.9] | 27.7 (26.2) [22.9, 32.4] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot | 336 | 8 | 47.9 (47.9) [42.6, 53.3] | 31.2 (31.2) [26.5, 36.3] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | CF | 336 | 17 | 51.2 (51.2) [45.8, 56.8] | 26.5 (26.5) [22.0, 31.0] | 1.5 (1.5) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | CF, assistant | 336 | 21 | 30.1 (30.1) [25.0, 34.8] | 0.3 (0.3) [0.0, 0.9] | 51.8 (51.8) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, assistant | 336 | 31 | 46.7 (46.7) [41.1, 52.1] | 27.4 (27.4) [22.6, 32.4] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=0 | 336 | 19 | 52.7 (52.7) [47.3, 58.0] | 20.2 (20.2) [16.1, 24.7] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=1 | 336 | 22 | 50.6 (50.6) [45.2, 55.7] | 23.8 (23.8) [19.3, 28.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=2 | 336 | 24 | 48.8 (48.8) [43.5, 54.2] | 27.4 (27.4) [22.6, 32.1] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=3 | 336 | 19 | 50.3 (50.3) [44.9, 55.4] | 28.9 (28.9) [24.1, 33.9] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF incremental | 168 | 3 | 45.8 (41.7) [38.1, 53.6] | 33.3 (30.4) [26.2, 40.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot | 168 | 5 | 46.4 (46.4) [38.7, 53.6] | 32.7 (32.7) [25.6, 39.9] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | CF | 168 | 8 | 50.0 (50.0) [42.3, 57.1] | 28.6 (28.6) [22.0, 35.7] | 1.8 (1.8) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | CF, assistant | 168 | 10 | 25.0 (25.0) [18.5, 31.5] | 0.0 (0.0) [0.0, 0.0] | 58.9 (58.9) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, assistant | 168 | 14 | 44.0 (44.0) [36.9, 51.8] | 30.4 (30.4) [23.8, 37.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=0 | 168 | 5 | 54.2 (54.2) [46.4, 61.9] | 20.8 (20.8) [14.9, 27.4] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=1 | 168 | 11 | 50.0 (50.0) [42.9, 57.1] | 22.6 (22.6) [16.7, 29.2] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=2 | 168 | 15 | 49.4 (49.4) [42.3, 57.1] | 28.0 (28.0) [21.4, 34.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=3 | 168 | 10 | 48.8 (48.8) [41.1, 56.0] | 29.8 (29.8) [23.2, 36.9] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF incremental | 168 | 11 | 51.2 (51.2) [43.5, 58.3] | 22.0 (22.0) [16.1, 28.0] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot | 168 | 3 | 49.4 (49.4) [41.7, 57.1] | 29.8 (29.8) [22.6, 36.9] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | CF | 168 | 9 | 52.4 (52.4) [44.6, 59.5] | 24.4 (24.4) [17.9, 31.0] | 1.2 (1.2) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | CF, assistant | 168 | 11 | 35.1 (35.1) [28.0, 42.3] | 0.6 (0.6) [0.0, 1.8] | 44.6 (44.6) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, assistant | 168 | 17 | 49.4 (49.4) [41.7, 57.1] | 24.4 (24.4) [18.5, 31.0] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=0 | 168 | 14 | 51.2 (51.2) [44.0, 58.3] | 19.6 (19.6) [13.7, 25.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=1 | 168 | 11 | 51.2 (51.2) [44.0, 58.9] | 25.0 (25.0) [18.5, 31.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=2 | 168 | 9 | 48.2 (48.2) [40.5, 56.0] | 26.8 (26.8) [20.8, 33.3] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=3 | 168 | 9 | 51.8 (51.8) [44.0, 58.9] | 28.0 (28.0) [20.8, 35.1] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Homogeneous control | TF one-shot | 400 | 4 | 95.2 (95.2) [93.2, 97.2] | - | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF incremental | 668 | 63 | 40.9 (38.2) [37.3, 44.8] | 37.1 (34.3) [33.5, 40.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot | 668 | 42 | 40.9 (40.9) [37.3, 44.8] | 38.9 (38.9) [35.2, 42.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | CF | 668 | 54 | 39.7 (39.7) [35.9, 43.4] | 34.1 (34.1) [30.7, 37.7] | 1.3 (1.3) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | CF, assistant | 668 | 76 | 23.7 (23.7) [20.4, 26.9] | 0.1 (0.1) [0.0, 0.4] | 58.7 (58.7) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, assistant | 668 | 70 | 38.9 (38.9) [35.3, 42.7] | 39.5 (39.5) [35.9, 43.1] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=0 | 668 | 65 | 43.9 (43.9) [40.3, 47.6] | 30.2 (30.2) [26.8, 33.7] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=1 | 668 | 69 | 42.8 (42.8) [39.1, 46.7] | 34.0 (34.0) [30.5, 37.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=2 | 668 | 62 | 40.7 (40.7) [37.0, 44.5] | 36.2 (36.2) [32.8, 40.0] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=3 | 668 | 52 | 39.5 (39.5) [35.6, 43.3] | 39.4 (39.4) [35.6, 43.3] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF incremental | 334 | 26 | 38.3 (32.9) [32.9, 43.7] | 42.2 (36.5) [36.8, 47.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot | 334 | 20 | 38.9 (38.9) [33.8, 44.3] | 41.6 (41.6) [36.5, 46.7] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF | 334 | 20 | 41.9 (41.9) [36.5, 47.3] | 33.8 (33.8) [29.0, 38.9] | 0.9 (0.9) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF, assistant | 334 | 43 | 17.7 (17.7) [13.8, 21.6] | 0.0 (0.0) [0.0, 0.0] | 64.4 (64.4) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, assistant | 334 | 34 | 35.9 (35.9) [30.8, 41.3] | 44.9 (44.9) [39.5, 50.3] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=0 | 334 | 32 | 44.3 (44.3) [39.2, 49.4] | 29.9 (29.9) [25.1, 35.0] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=1 | 334 | 28 | 45.8 (45.8) [40.4, 51.2] | 33.5 (33.5) [28.7, 38.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=2 | 334 | 24 | 40.1 (40.1) [35.0, 45.2] | 38.0 (38.0) [32.9, 42.8] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=3 | 334 | 25 | 37.4 (37.4) [32.3, 42.8] | 40.4 (40.4) [35.0, 45.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF incremental | 334 | 37 | 43.4 (43.4) [38.0, 48.8] | 32.0 (32.0) [26.9, 36.8] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot | 334 | 22 | 42.8 (42.8) [37.7, 48.2] | 36.2 (36.2) [31.1, 41.3] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF | 334 | 34 | 37.4 (37.4) [32.3, 42.5] | 34.4 (34.4) [29.6, 39.5] | 1.8 (1.8) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF, assistant | 334 | 33 | 29.6 (29.6) [24.9, 34.7] | 0.3 (0.3) [0.0, 0.9] | 53.0 (53.0) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, assistant | 334 | 36 | 41.9 (41.9) [37.1, 47.3] | 34.1 (34.1) [29.0, 39.2] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=0 | 334 | 33 | 43.4 (43.4) [38.0, 48.8] | 30.5 (30.5) [25.7, 35.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=1 | 334 | 41 | 39.8 (39.8) [34.7, 45.2] | 34.4 (34.4) [29.6, 39.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=2 | 334 | 38 | 41.3 (41.3) [36.2, 46.1] | 34.4 (34.4) [29.6, 39.8] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=3 | 334 | 27 | 41.6 (41.6) [36.5, 47.0] | 38.3 (38.3) [33.2, 43.4] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Homogeneous control | TF one-shot | 490 | 18 | 87.8 (87.8) [84.7, 90.4] | - | - | - | - | - | - |

## Assistant-turn prefill: the forced line, then the model's own re-check (%)

first = the label written right after the prefill (the one Table 4 uses); kept writing = the model went on after it (typically "Wait, no, that's wrong" and a re-check); restarted = wrote no label after the forced "objK:" and began its own five-label list on a new line (counted in kept writing; first counts as wrong and not A); final = obj K's last "objK: <class>" in the answer (= first when it stopped); unresolved = kept writing but gave no final label for B, or hit the token limit. cut = thinking never closed. All over n img, tolerant.

| model | split | order | condition | n img | cut | first: B acc | first: B=A | first: B=C | kept writing | restarted | final: B acc | final: B=A | final: B=C | unresolved |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | Adversarial | CF, assistant | 336 | 21 | 30.1 | 0.3 | 51.8 | 0.0 | 0.0 | 30.1 | 0.3 | 51.8 | 0.0 |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, assistant | 336 | 31 | 46.7 | 27.4 | - | 0.0 | 0.0 | 46.7 | 27.4 | - | 0.0 |
| qwen3vl-8b-thinking | Seen | AAAAB | CF, assistant | 168 | 10 | 25.0 | 0.0 | 58.9 | 0.0 | 0.0 | 25.0 | 0.0 | 58.9 | 0.0 |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, assistant | 168 | 14 | 44.0 | 30.4 | - | 0.0 | 0.0 | 44.0 | 30.4 | - | 0.0 |
| qwen3vl-8b-thinking | Seen | BAAAA | CF, assistant | 168 | 11 | 35.1 | 0.6 | 44.6 | 0.0 | 0.0 | 35.1 | 0.6 | 44.6 | 0.0 |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, assistant | 168 | 17 | 49.4 | 24.4 | - | 0.0 | 0.0 | 49.4 | 24.4 | - | 0.0 |
| qwen3vl-8b-thinking | Unseen | Adversarial | CF, assistant | 668 | 76 | 23.7 | 0.1 | 58.7 | 0.0 | 0.0 | 23.7 | 0.1 | 58.7 | 0.0 |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, assistant | 668 | 70 | 38.9 | 39.5 | - | 0.1 | 0.0 | 38.8 | 39.5 | - | 0.1 |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF, assistant | 334 | 43 | 17.7 | 0.0 | 64.4 | 0.0 | 0.0 | 17.7 | 0.0 | 64.4 | 0.0 |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, assistant | 334 | 34 | 35.9 | 44.9 | - | 0.0 | 0.0 | 35.9 | 44.9 | - | 0.0 |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF, assistant | 334 | 33 | 29.6 | 0.3 | 53.0 | 0.0 | 0.0 | 29.6 | 0.3 | 53.0 | 0.0 |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, assistant | 334 | 36 | 41.9 | 34.1 | - | 0.3 | 0.0 | 41.6 | 34.1 | - | 0.3 |

## What the answer does with the given boxes (one-shot, labels in the user turn; %)

Over answered rows (calls for B not cut), tolerant parse, last objK: mention per box. B read before objK: = the answer has no objK: for B but writes B's label first and then other boxes (it continues the prompt's last "objK:"), and B's label was read from that first segment (see asked_label); writes all 5 = a label for every box, i.e. the model rewrites the list instead of answering only B; keeps given = every given box keeps its given label; given boxes = A = every given box is labelled A; C kept = C stays on at least one given box (CF only). '-' = no label given (n = 0).

| model | split | order | condition | n answered | B read before objK: | writes all 5 | keeps given | given boxes = A | C kept |
|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot | 328 | 0.0 | 100.0 | 92.7 | 92.7 | - |
| qwen3vl-8b-thinking | Seen | Adversarial | CF | 319 | 0.0 | 100.0 | 1.3 | 76.2 | 1.9 |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=0 | 317 | 0.0 | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=1 | 314 | 0.0 | 100.0 | 92.4 | 92.4 | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=2 | 312 | 0.0 | 100.0 | 92.0 | 92.0 | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot, given=3 | 317 | 0.0 | 100.0 | 93.7 | 93.7 | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot | 163 | 0.0 | 100.0 | 94.5 | 94.5 | - |
| qwen3vl-8b-thinking | Seen | AAAAB | CF | 160 | 0.0 | 100.0 | 2.5 | 76.9 | 2.5 |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=0 | 163 | 0.0 | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=1 | 157 | 0.0 | 100.0 | 93.6 | 93.6 | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=2 | 153 | 0.0 | 100.0 | 94.1 | 94.1 | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot, given=3 | 158 | 0.0 | 100.0 | 94.9 | 94.9 | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot | 165 | 0.0 | 100.0 | 90.9 | 90.9 | - |
| qwen3vl-8b-thinking | Seen | BAAAA | CF | 159 | 0.0 | 100.0 | 0.0 | 75.5 | 1.3 |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=0 | 154 | 0.0 | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=1 | 157 | 0.0 | 100.0 | 91.1 | 91.1 | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=2 | 159 | 0.0 | 100.0 | 89.9 | 89.9 | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot, given=3 | 159 | 0.0 | 100.0 | 92.5 | 92.5 | - |
| qwen3vl-8b-thinking | Seen | Homogeneous control | TF one-shot | 396 | 0.0 | 100.0 | 96.7 | 96.7 | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot | 626 | 0.0 | 100.0 | 85.6 | 85.6 | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | CF | 614 | 0.0 | 100.0 | 1.3 | 71.0 | 2.4 |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=0 | 603 | 0.0 | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=1 | 599 | 0.0 | 100.0 | 86.6 | 86.6 | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=2 | 606 | 0.0 | 100.0 | 85.5 | 85.5 | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot, given=3 | 616 | 0.0 | 100.0 | 86.4 | 86.4 | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot | 314 | 0.0 | 100.0 | 87.3 | 87.3 | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF | 314 | 0.0 | 100.0 | 1.3 | 69.7 | 2.5 |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=0 | 302 | 0.0 | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=1 | 306 | 0.0 | 100.0 | 86.9 | 86.9 | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=2 | 310 | 0.0 | 100.0 | 85.5 | 85.5 | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot, given=3 | 309 | 0.0 | 100.0 | 87.4 | 87.4 | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot | 312 | 0.0 | 100.0 | 84.0 | 84.0 | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF | 300 | 0.0 | 100.0 | 1.3 | 72.3 | 2.3 |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=0 | 301 | 0.0 | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=1 | 293 | 0.0 | 100.0 | 86.3 | 86.3 | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=2 | 296 | 0.0 | 100.0 | 85.5 | 85.5 | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot, given=3 | 307 | 0.0 | 100.0 | 85.3 | 85.3 | - |
| qwen3vl-8b-thinking | Unseen | Homogeneous control | TF one-shot | 472 | 0.0 | 100.0 | 90.9 | 90.9 | - |

## Figure 4 data: dose-response (tolerant, %)

| model | split | probe | order | labels given | n img | B acc [95% CI] | B=A [95% CI] | B=C [95% CI] |
|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | TF one-shot | Adversarial | 0 | 336 | 52.7 [47.3, 58.0] | 20.2 [16.1, 24.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | Adversarial | 1 | 336 | 50.6 [45.2, 55.7] | 23.8 [19.3, 28.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | Adversarial | 2 | 336 | 48.8 [43.5, 54.2] | 27.4 [22.6, 32.1] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | Adversarial | 3 | 336 | 50.3 [44.9, 55.4] | 28.9 [24.1, 33.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | Adversarial | 4 | 336 | 47.9 [42.6, 53.3] | 31.2 [26.5, 36.3] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | AAAAB | 0 | 168 | 54.2 [46.4, 61.9] | 20.8 [14.9, 27.4] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | AAAAB | 1 | 168 | 50.0 [42.9, 57.1] | 22.6 [16.7, 29.2] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | AAAAB | 2 | 168 | 49.4 [42.3, 57.1] | 28.0 [21.4, 34.5] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | AAAAB | 3 | 168 | 48.8 [41.1, 56.0] | 29.8 [23.2, 36.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | AAAAB | 4 | 168 | 46.4 [38.7, 53.6] | 32.7 [25.6, 39.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | BAAAA | 0 | 168 | 51.2 [44.0, 58.3] | 19.6 [13.7, 25.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | BAAAA | 1 | 168 | 51.2 [44.0, 58.9] | 25.0 [18.5, 31.5] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | BAAAA | 2 | 168 | 48.2 [40.5, 56.0] | 26.8 [20.8, 33.3] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | BAAAA | 3 | 168 | 51.8 [44.0, 58.9] | 28.0 [20.8, 35.1] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Seen | TF one-shot | BAAAA | 4 | 168 | 49.4 [41.7, 57.1] | 29.8 [22.6, 36.9] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | Adversarial | 0 | 668 | 43.9 [40.3, 47.6] | 30.2 [26.8, 33.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | Adversarial | 1 | 668 | 42.8 [39.1, 46.7] | 34.0 [30.5, 37.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | Adversarial | 2 | 668 | 40.7 [37.0, 44.5] | 36.2 [32.8, 40.0] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | Adversarial | 3 | 668 | 39.5 [35.6, 43.3] | 39.4 [35.6, 43.3] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | Adversarial | 4 | 668 | 40.9 [37.3, 44.8] | 38.9 [35.2, 42.5] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | AAAAB | 0 | 334 | 44.3 [39.2, 49.4] | 29.9 [25.1, 35.0] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | AAAAB | 1 | 334 | 45.8 [40.4, 51.2] | 33.5 [28.7, 38.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | AAAAB | 2 | 334 | 40.1 [35.0, 45.2] | 38.0 [32.9, 42.8] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | AAAAB | 3 | 334 | 37.4 [32.3, 42.8] | 40.4 [35.0, 45.5] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | AAAAB | 4 | 334 | 38.9 [33.8, 44.3] | 41.6 [36.5, 46.7] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | BAAAA | 0 | 334 | 43.4 [38.0, 48.8] | 30.5 [25.7, 35.6] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | BAAAA | 1 | 334 | 39.8 [34.7, 45.2] | 34.4 [29.6, 39.5] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | BAAAA | 2 | 334 | 41.3 [36.2, 46.1] | 34.4 [29.6, 39.8] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | BAAAA | 3 | 334 | 41.6 [36.5, 47.0] | 38.3 [33.2, 43.4] | 0.0 [0.0, 0.0] |
| qwen3vl-8b-thinking | Unseen | TF one-shot | BAAAA | 4 | 334 | 42.8 [37.7, 48.2] | 36.2 [31.1, 41.3] | 0.0 [0.0, 0.0] |

## Figure 4 tests: labels given against none

Images with every dose point (tolerant). slope = per-image least-squares change per label given (0-4), in points, permutation p (doses shuffled within image). 4 vs 0 = all four labels against none, paired, exact McNemar. Holm per model and outcome.

| model | split | probe | order | n img | B=A slope / label [CI] | p (Holm) | B=A 4 vs 0 [CI] | p (Holm) | acc slope / label [CI] | p (Holm) | acc 4 vs 0 [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | TF one-shot | Adversarial | 336 | +2.7 [+1.8, +3.6] | 1.0e-04 (6.0e-04) | +11.0 [+7.1, +15.2] | 1.2e-07 (2.5e-06) | -1.0 [-1.9, -0.1] | 0.0152 (0.0456) | -4.8 [-8.0, -1.5] | 0.00904 (0.19) |
| qwen3vl-8b-thinking | Seen | TF one-shot | AAAAB | 168 | +3.1 [+1.7, +4.5] | 1.0e-04 (6.0e-04) | +11.9 [+6.5, +17.9] | 8.8e-05 (0.00132) | -1.7 [-3.0, -0.5] | 0.0046 (0.0184) | -7.7 [-12.5, -3.0] | 0.00235 (0.054) |
| qwen3vl-8b-thinking | Seen | TF one-shot | BAAAA | 168 | +2.3 [+1.1, +3.6] | 1.0e-04 (6.0e-04) | +10.1 [+4.8, +16.1] | 9.1e-04 (0.0118) | -0.3 [-1.4, +1.0] | 0.613 (1) | -1.8 [-6.5, +3.0] | 0.629 (1) |
| qwen3vl-8b-thinking | Unseen | TF one-shot | Adversarial | 668 | +2.3 [+1.7, +2.9] | 1.0e-04 (6.0e-04) | +8.7 [+6.1, +11.4] | 7.9e-11 (1.8e-09) | -0.9 [-1.6, -0.3] | 0.0018 (0.009) | -3.0 [-5.7, -0.1] | 0.047 (0.799) |
| qwen3vl-8b-thinking | Unseen | TF one-shot | AAAAB | 334 | +3.0 [+2.0, +4.0] | 1.0e-04 (6.0e-04) | +11.7 [+8.1, +15.9] | 7.6e-09 (1.7e-07) | -1.9 [-2.9, -1.0] | 2.0e-04 (0.0012) | -5.4 [-9.3, -1.5] | 0.0133 (0.266) |
| qwen3vl-8b-thinking | Unseen | TF one-shot | BAAAA | 334 | +1.5 [+0.7, +2.3] | 1.0e-04 (6.0e-04) | +5.7 [+2.4, +9.3] | 0.00188 (0.0187) | +0.1 [-0.9, +1.0] | 0.913 (1) | -0.6 [-4.5, +3.3] | 0.88 (1) |

