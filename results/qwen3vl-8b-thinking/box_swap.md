# Box swaps inside B=A

Calls that label all five boxes in one answer, not cut. "B on an A box": the gold class of B is written on one of the four A boxes.

| model | split | order | condition | n | B=A | of which B on an A box | B on an A box (all answers) |
|---|---|---|---|---|---|---|---|
| qwen3vl-8b-thinking | Seen | AAAAB | CF | 160 | 48 (30.0%) | 1 (2% of B=A) | 14 (8.8%) |
| qwen3vl-8b-thinking | Seen | AAAAB | CF far | 158 | 50 (31.6%) | 0 (0% of B=A) | 14 (8.9%) |
| qwen3vl-8b-thinking | Seen | AAAAB | CF near | 161 | 40 (24.8%) | 0 (0% of B=A) | 9 (5.6%) |
| qwen3vl-8b-thinking | Seen | AAAAB | TF one-shot | 163 | 55 (33.7%) | 0 (0% of B=A) | 7 (4.3%) |
| qwen3vl-8b-thinking | Seen | BAAAA | CF | 159 | 41 (25.8%) | 1 (2% of B=A) | 15 (9.4%) |
| qwen3vl-8b-thinking | Seen | BAAAA | CF far | 160 | 41 (25.6%) | 1 (2% of B=A) | 22 (13.8%) |
| qwen3vl-8b-thinking | Seen | BAAAA | CF near | 157 | 40 (25.5%) | 1 (2% of B=A) | 11 (7.0%) |
| qwen3vl-8b-thinking | Seen | BAAAA | TF one-shot | 165 | 50 (30.3%) | 0 (0% of B=A) | 8 (4.8%) |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF | 314 | 113 (36.0%) | 2 (2% of B=A) | 30 (9.6%) |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF far | 308 | 116 (37.7%) | 3 (3% of B=A) | 33 (10.7%) |
| qwen3vl-8b-thinking | Unseen | AAAAB | CF near | 308 | 117 (38.0%) | 3 (3% of B=A) | 22 (7.1%) |
| qwen3vl-8b-thinking | Unseen | AAAAB | TF one-shot | 314 | 139 (44.3%) | 2 (1% of B=A) | 10 (3.2%) |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF | 300 | 115 (38.3%) | 0 (0% of B=A) | 26 (8.7%) |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF far | 301 | 114 (37.9%) | 3 (3% of B=A) | 31 (10.3%) |
| qwen3vl-8b-thinking | Unseen | BAAAA | CF near | 312 | 113 (36.2%) | 1 (1% of B=A) | 24 (7.7%) |
| qwen3vl-8b-thinking | Unseen | BAAAA | TF one-shot | 312 | 121 (38.8%) | 0 (0% of B=A) | 20 (6.4%) |
