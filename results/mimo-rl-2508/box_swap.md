# Box swaps inside B=A

Calls that label all five boxes in one answer, not cut. "B on an A box": the gold class of B is written on one of the four A boxes.

| model | split | order | condition | n | B=A | of which B on an A box | B on an A box (all answers) |
|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | AAAAB | CF | 159 | 40 (25.2%) | 1 (2% of B=A) | 11 (6.9%) |
| mimo-rl-2508 | Seen | AAAAB | CF far | 163 | 42 (25.8%) | 1 (2% of B=A) | 15 (9.2%) |
| mimo-rl-2508 | Seen | AAAAB | CF near | 162 | 33 (20.4%) | 0 (0% of B=A) | 12 (7.4%) |
| mimo-rl-2508 | Seen | AAAAB | TF one-shot | 163 | 48 (29.4%) | 0 (0% of B=A) | 7 (4.3%) |
| mimo-rl-2508 | Seen | AAAAB | default | 159 | 35 (22.0%) | 3 (9% of B=A) | 19 (11.9%) |
| mimo-rl-2508 | Seen | BAAAA | CF | 159 | 38 (23.9%) | 1 (3% of B=A) | 17 (10.7%) |
| mimo-rl-2508 | Seen | BAAAA | CF far | 158 | 36 (22.8%) | 1 (3% of B=A) | 16 (10.1%) |
| mimo-rl-2508 | Seen | BAAAA | CF near | 163 | 36 (22.1%) | 1 (3% of B=A) | 17 (10.4%) |
| mimo-rl-2508 | Seen | BAAAA | TF one-shot | 165 | 36 (21.8%) | 1 (3% of B=A) | 12 (7.3%) |
| mimo-rl-2508 | Seen | BAAAA | default | 156 | 30 (19.2%) | 2 (7% of B=A) | 18 (11.5%) |
| mimo-rl-2508 | Unseen | AAAAB | CF | 304 | 118 (38.8%) | 18 (15% of B=A) | 35 (11.5%) |
| mimo-rl-2508 | Unseen | AAAAB | CF far | 315 | 130 (41.3%) | 21 (16% of B=A) | 39 (12.4%) |
| mimo-rl-2508 | Unseen | AAAAB | CF near | 315 | 126 (40.0%) | 18 (14% of B=A) | 36 (11.4%) |
| mimo-rl-2508 | Unseen | AAAAB | TF one-shot | 318 | 142 (44.7%) | 13 (9% of B=A) | 27 (8.5%) |
| mimo-rl-2508 | Unseen | AAAAB | default | 297 | 98 (33.0%) | 12 (12% of B=A) | 32 (10.8%) |
| mimo-rl-2508 | Unseen | BAAAA | CF | 313 | 118 (37.7%) | 19 (16% of B=A) | 45 (14.4%) |
| mimo-rl-2508 | Unseen | BAAAA | CF far | 311 | 117 (37.6%) | 19 (16% of B=A) | 50 (16.1%) |
| mimo-rl-2508 | Unseen | BAAAA | CF near | 311 | 118 (37.9%) | 19 (16% of B=A) | 42 (13.5%) |
| mimo-rl-2508 | Unseen | BAAAA | TF one-shot | 320 | 118 (36.9%) | 13 (11% of B=A) | 29 (9.1%) |
| mimo-rl-2508 | Unseen | BAAAA | default | 311 | 108 (34.7%) | 19 (18% of B=A) | 46 (14.8%) |

## Default against Single-object: how much of the B=A gain is box swaps

Same images, tolerant, a cut call is wrong and not A. "Without swaps": a Default B=A answer that writes B's class on an A box is not counted as A.

| model | split | order | n img | Default up / Single up | of the Default up: B on an A box | B=A gain (points) | gain without swaps |
|---|---|---|---|---|---|---|---|
| mimo-rl-2508 | Seen | AAAAB | 168 | 17 / 3 | 2 | +8.3 | +7.1 |
| mimo-rl-2508 | Seen | BAAAA | 168 | 9 / 6 | 1 | +1.8 | +1.2 |
| mimo-rl-2508 | Unseen | AAAAB | 334 | 49 / 14 | 9 | +10.5 | +7.8 |
| mimo-rl-2508 | Unseen | BAAAA | 334 | 43 / 14 | 12 | +8.7 | +5.1 |
