# Box swaps inside B=A

Calls that label all five boxes in one answer, not cut. "B on an A box": the gold class of B is written on one of the four A boxes.

| model | split | order | condition | n | B=A | of which B on an A box | B on an A box (all answers) |
|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | AAAAB | CF | 160 | 48 (30.0%) | 1 (2% of B=A) | 14 (8.8%) |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot | 163 | 55 (33.7%) | 0 (0% of B=A) | 7 (4.3%) |
| qwen3vl-8b-thinking | Seen | BAAAA | CF | 159 | 41 (25.8%) | 1 (2% of B=A) | 15 (9.4%) |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot | 165 | 50 (30.3%) | 0 (0% of B=A) | 8 (4.8%) |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF | 314 | 113 (36.0%) | 2 (2% of B=A) | 30 (9.6%) |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot | 314 | 139 (44.3%) | 2 (1% of B=A) | 10 (3.2%) |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF | 300 | 115 (38.3%) | 0 (0% of B=A) | 26 (8.7%) |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot | 312 | 121 (38.8%) | 0 (0% of B=A) | 20 (6.4%) |
