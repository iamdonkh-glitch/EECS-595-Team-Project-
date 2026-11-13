# RQ2 forcing probes

Files (6): forcing_qwen3vl-8b-thinking_cf_train.jsonl, forcing_qwen3vl-8b-thinking_cf_validation.jsonl, forcing_qwen3vl-8b-thinking_tf-incremental_train.jsonl, forcing_qwen3vl-8b-thinking_tf-incremental_validation.jsonl, forcing_qwen3vl-8b-thinking_tf-oneshot_train.jsonl, forcing_qwen3vl-8b-thinking_tf-oneshot_validation.jsonl

## Table 4: the odd object B under each condition (%)

B acc = B named correctly; B=A = B given the class of the other four (inertia); B=C = B given the counterfactual class. Tolerant parse, strict in parentheses. cut = calls for B at the token limit (scored wrong). vs default = paired on the same images, y - x in points; p = exact McNemar, Holm over the model's comparisons in the same probe family (core = single, TF incremental, TF one-shot, CF; dose = given=0-3; placement = assistant; C near/far; Homogeneous control).

| model | split | order | condition | n img | cut | B acc [95% CI] | B=A [95% CI] | B=C | acc vs default [CI] | p (Holm) | B=A vs default [CI] | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | Adversarial | TF incremental | 336 | 14 | 48.5 (46.4) [43.2, 53.9] | 27.7 (26.2) [22.9, 32.4] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot | 336 | 8 | 47.9 (47.9) [42.6, 53.3] | 31.2 (31.2) [26.5, 36.3] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | Adversarial | CF | 336 | 17 | 51.2 (51.2) [45.8, 56.8] | 26.5 (26.5) [22.0, 31.0] | 1.5 (1.5) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF incremental | 168 | 3 | 45.8 (41.7) [38.1, 53.6] | 33.3 (30.4) [26.2, 40.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot | 168 | 5 | 46.4 (46.4) [38.7, 53.6] | 32.7 (32.7) [25.6, 39.9] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | AAAAB | CF | 168 | 8 | 50.0 (50.0) [42.3, 57.1] | 28.6 (28.6) [22.0, 35.7] | 1.8 (1.8) | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF incremental | 168 | 11 | 51.2 (51.2) [43.5, 58.3] | 22.0 (22.0) [16.1, 28.0] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot | 168 | 3 | 49.4 (49.4) [41.7, 57.1] | 29.8 (29.8) [22.6, 36.9] | - | - | - | - | - |
| qwen3vl-8b-thinking | Seen | BAAAA | CF | 168 | 9 | 52.4 (52.4) [44.6, 59.5] | 24.4 (24.4) [17.9, 31.0] | 1.2 (1.2) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF incremental | 668 | 63 | 40.9 (38.2) [37.3, 44.8] | 37.1 (34.3) [33.5, 40.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot | 668 | 42 | 40.9 (40.9) [37.3, 44.8] | 38.9 (38.9) [35.2, 42.5] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | CF | 668 | 54 | 39.7 (39.7) [35.9, 43.4] | 34.1 (34.1) [30.7, 37.7] | 1.3 (1.3) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF incremental | 334 | 26 | 38.3 (32.9) [32.9, 43.7] | 42.2 (36.5) [36.8, 47.6] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot | 334 | 20 | 38.9 (38.9) [33.8, 44.3] | 41.6 (41.6) [36.5, 46.7] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF | 334 | 20 | 41.9 (41.9) [36.5, 47.3] | 33.8 (33.8) [29.0, 38.9] | 0.9 (0.9) | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF incremental | 334 | 37 | 43.4 (43.4) [38.0, 48.8] | 32.0 (32.0) [26.9, 36.8] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot | 334 | 22 | 42.8 (42.8) [37.7, 48.2] | 36.2 (36.2) [31.1, 41.3] | - | - | - | - | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF | 334 | 34 | 37.4 (37.4) [32.3, 42.5] | 34.4 (34.4) [29.6, 39.5] | 1.8 (1.8) | - | - | - | - |

## What the answer does with the given boxes (one-shot, labels in the user turn; %)

Over answered rows (calls for B not cut), tolerant parse, last objK: mention per box. B read before objK: = the answer has no objK: for B but writes B's label first and then other boxes (it continues the prompt's last "objK:"), and B's label was read from that first segment (see asked_label); writes all 5 = a label for every box, i.e. the model rewrites the list instead of answering only B; keeps given = every given box keeps its given label; given boxes = A = every given box is labelled A; C kept = C stays on at least one given box (CF only). '-' = no label given (n = 0).

| model | split | order | condition | n answered | B read before objK: | writes all 5 | keeps given | given boxes = A | C kept |
|---|---|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | Adversarial | TF one-shot | 328 | 0.0 | 100.0 | 92.7 | 92.7 | - |
| qwen3vl-8b-thinking | Seen | Adversarial | CF | 319 | 0.0 | 100.0 | 1.3 | 76.2 | 1.9 |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot | 163 | 0.0 | 100.0 | 94.5 | 94.5 | - |
| qwen3vl-8b-thinking | Seen | AAAAB | CF | 160 | 0.0 | 100.0 | 2.5 | 76.9 | 2.5 |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot | 165 | 0.0 | 100.0 | 90.9 | 90.9 | - |
| qwen3vl-8b-thinking | Seen | BAAAA | CF | 159 | 0.0 | 100.0 | 0.0 | 75.5 | 1.3 |
| qwen3vl-8b-thinking | Unseen | Adversarial | TF one-shot | 626 | 0.0 | 100.0 | 85.6 | 85.6 | - |
| qwen3vl-8b-thinking | Unseen | Adversarial | CF | 614 | 0.0 | 100.0 | 1.3 | 71.0 | 2.4 |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot | 314 | 0.0 | 100.0 | 87.3 | 87.3 | - |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF | 314 | 0.0 | 100.0 | 1.3 | 69.7 | 2.5 |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot | 312 | 0.0 | 100.0 | 84.0 | 84.0 | - |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF | 300 | 0.0 | 100.0 | 1.3 | 72.3 | 2.3 |

