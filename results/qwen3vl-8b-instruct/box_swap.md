# Box swaps inside B=A

Calls that label all five boxes in one answer, not cut. "B on an A box": the gold class of B is written on one of the four A boxes.

| model | split | order | condition | n | B=A | of which B on an A box | B on an A box (all answers) |
|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | AAAAB | CF | 53 | 11 (20.8%) | 0 (0% of B=A) | 7 (13.2%) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF far | 45 | 9 (20.0%) | 0 (0% of B=A) | 5 (11.1%) |
| qwen3vl-8b-instruct | Seen | AAAAB | CF near | 33 | 11 (33.3%) | 0 (0% of B=A) | 4 (12.1%) |
| qwen3vl-8b-instruct | Seen | AAAAB | default | 168 | 45 (26.8%) | 1 (2% of B=A) | 19 (11.3%) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF | 125 | 20 (16.0%) | 0 (0% of B=A) | 12 (9.6%) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF far | 112 | 21 (18.8%) | 1 (5% of B=A) | 12 (10.7%) |
| qwen3vl-8b-instruct | Seen | BAAAA | CF near | 70 | 12 (17.1%) | 0 (0% of B=A) | 7 (10.0%) |
| qwen3vl-8b-instruct | Seen | BAAAA | TF one-shot | 4 | 0 (0.0%) | 0 (0% of B=A) | 1 (25.0%) |
| qwen3vl-8b-instruct | Seen | BAAAA | default | 168 | 31 (18.5%) | 0 (0% of B=A) | 23 (13.7%) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF | 80 | 25 (31.2%) | 1 (4% of B=A) | 7 (8.8%) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF far | 141 | 35 (24.8%) | 1 (3% of B=A) | 18 (12.8%) |
| qwen3vl-8b-instruct | Unseen | AAAAB | CF near | 68 | 19 (27.9%) | 0 (0% of B=A) | 4 (5.9%) |
| qwen3vl-8b-instruct | Unseen | AAAAB | TF one-shot | 2 | 0 (0.0%) | 0 (0% of B=A) | 0 (0.0%) |
| qwen3vl-8b-instruct | Unseen | AAAAB | default | 334 | 120 (35.9%) | 7 (6% of B=A) | 42 (12.6%) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF | 199 | 43 (21.6%) | 2 (5% of B=A) | 15 (7.5%) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF far | 241 | 47 (19.5%) | 1 (2% of B=A) | 29 (12.0%) |
| qwen3vl-8b-instruct | Unseen | BAAAA | CF near | 135 | 34 (25.2%) | 0 (0% of B=A) | 12 (8.9%) |
| qwen3vl-8b-instruct | Unseen | BAAAA | TF one-shot | 17 | 3 (17.6%) | 1 (33% of B=A) | 3 (17.6%) |
| qwen3vl-8b-instruct | Unseen | BAAAA | default | 334 | 84 (25.1%) | 3 (4% of B=A) | 45 (13.5%) |

## Default against Single-object: how much of the B=A gain is box swaps

Same images, tolerant, a cut call is wrong and not A. "Without swaps": a Default B=A answer that writes B's class on an A box is not counted as A.

| model | split | order | n img | Default up / Single up | of the Default up: B on an A box | B=A gain (points) | gain without swaps |
|---|---|---|---|---|---|---|---|
| qwen3vl-8b-instruct | Seen | AAAAB | 168 | 23 / 3 | 1 | +11.9 | +11.3 |
| qwen3vl-8b-instruct | Seen | BAAAA | 168 | 5 / 5 | 0 | +0.0 | +0.0 |
| qwen3vl-8b-instruct | Unseen | AAAAB | 334 | 56 / 3 | 5 | +15.9 | +14.4 |
| qwen3vl-8b-instruct | Unseen | BAAAA | 334 | 20 / 12 | 0 | +2.4 | +2.4 |
