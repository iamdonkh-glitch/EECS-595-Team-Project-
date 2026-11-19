# RQ3 Table 3: error taxonomy

Files (32): rq1_mimo-rl-2508_adversarial_default_train.jsonl, rq1_mimo-rl-2508_adversarial_default_validation.jsonl, rq1_mimo-rl-2508_adversarial_single_train.jsonl, rq1_mimo-rl-2508_adversarial_single_validation.jsonl, rq1_mimo-rl-2508_default_train.jsonl, rq1_mimo-rl-2508_default_validation.jsonl, rq1_mimo-rl-2508_single_train.jsonl, rq1_mimo-rl-2508_single_validation.jsonl, rq1_mimo-sft-2508_adversarial_default_train.jsonl, rq1_mimo-sft-2508_adversarial_default_validation.jsonl, rq1_mimo-sft-2508_adversarial_single_train.jsonl, rq1_mimo-sft-2508_adversarial_single_validation.jsonl, rq1_mimo-sft-2508_default_train.jsonl, rq1_mimo-sft-2508_default_validation.jsonl, rq1_mimo-sft-2508_single_train.jsonl, rq1_mimo-sft-2508_single_validation.jsonl, rq1_qwen3vl-8b-instruct_adversarial_default_train.jsonl, rq1_qwen3vl-8b-instruct_adversarial_default_validation.jsonl, rq1_qwen3vl-8b-instruct_adversarial_single_train.jsonl, rq1_qwen3vl-8b-instruct_adversarial_single_validation.jsonl, rq1_qwen3vl-8b-instruct_default_train.jsonl, rq1_qwen3vl-8b-instruct_default_validation.jsonl, rq1_qwen3vl-8b-instruct_single_train.jsonl, rq1_qwen3vl-8b-instruct_single_validation.jsonl, rq1_qwen3vl-8b-thinking_adversarial_default_train.jsonl, rq1_qwen3vl-8b-thinking_adversarial_default_validation.jsonl, rq1_qwen3vl-8b-thinking_adversarial_single_train.jsonl, rq1_qwen3vl-8b-thinking_adversarial_single_validation.jsonl, rq1_qwen3vl-8b-thinking_default_train.jsonl, rq1_qwen3vl-8b-thinking_default_validation.jsonl, rq1_qwen3vl-8b-thinking_single_train.jsonl, rq1_qwen3vl-8b-thinking_single_validation.jsonl

## (a) Table 3, tolerant parse: category of each scored object (% of scored objects)

Each row sums to 100 (up to rounding). Categories and their order are defined in the script docstring and the README. correct equals Table 1's accuracy (token-limit rule applied).

| model | subset | probe | split | n img | n obj | correct | truncated | unparsed | B=A | borrowed | off-list | in-image | invented |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | In-the-Wild | default | Seen | 1539 | 7695 | 61.0 | 5.8 | 0.0 | 0.0 | 14.3 | 0.2 | 9.5 | 9.1 |
| mimo-sft-2508 | In-the-Wild | default | Unseen | 1172 | 5860 | 55.2 | 8.1 | 0.0 | 0.0 | 17.7 | 0.2 | 10.4 | 8.4 |
| mimo-sft-2508 | In-the-Wild | single | Seen | 1539 | 7695 | 68.3 | 1.2 | 0.0 | 0.0 | 11.2 | 0.4 | 9.2 | 9.8 |
| mimo-sft-2508 | In-the-Wild | single | Unseen | 1172 | 5860 | 62.7 | 1.2 | 0.0 | 0.0 | 14.8 | 0.4 | 11.3 | 9.6 |
| mimo-sft-2508 | Homogeneous | default | Seen | 400 | 2000 | 85.2 | 1.2 | 0.0 | 0.0 | 0.0 | 0.2 | 6.3 | 6.9 |
| mimo-sft-2508 | Homogeneous | default | Unseen | 490 | 2450 | 80.9 | 2.4 | 0.0 | 0.0 | 0.0 | 0.1 | 12.0 | 4.5 |
| mimo-sft-2508 | Homogeneous | single | Seen | 400 | 2000 | 85.1 | 0.5 | 0.0 | 0.0 | 0.0 | 0.4 | 7.5 | 6.5 |
| mimo-sft-2508 | Homogeneous | single | Unseen | 490 | 2450 | 75.8 | 0.4 | 0.0 | 0.0 | 0.0 | 0.2 | 16.7 | 6.9 |
| mimo-sft-2508 | Heterogeneous | default | Seen | 312 | 1560 | 49.4 | 13.8 | 0.0 | 0.0 | 17.2 | 0.3 | 8.5 | 10.9 |
| mimo-sft-2508 | Heterogeneous | default | Unseen | 246 | 1230 | 42.1 | 12.2 | 0.0 | 0.0 | 21.9 | 0.2 | 12.2 | 11.4 |
| mimo-sft-2508 | Heterogeneous | single | Seen | 312 | 1560 | 59.2 | 2.1 | 0.0 | 0.0 | 17.7 | 0.6 | 9.3 | 11.1 |
| mimo-sft-2508 | Heterogeneous | single | Unseen | 246 | 1230 | 49.6 | 1.7 | 0.0 | 0.0 | 23.3 | 0.6 | 12.4 | 12.4 |
| mimo-sft-2508 | Adversarial AAAAB | default | Seen | 168 | 840 | 72.5 | 1.8 | 0.0 | 5.2 | 5.2 | 0.2 | 10.2 | 4.8 |
| mimo-sft-2508 | Adversarial AAAAB | default | Unseen | 334 | 1670 | 64.7 | 3.9 | 0.0 | 6.8 | 5.5 | 0.0 | 13.1 | 6.0 |
| mimo-sft-2508 | Adversarial AAAAB | single | Seen | 168 | 840 | 74.4 | 1.0 | 0.0 | 2.4 | 4.9 | 0.5 | 11.3 | 5.6 |
| mimo-sft-2508 | Adversarial AAAAB | single | Unseen | 334 | 1670 | 64.9 | 1.1 | 0.0 | 3.2 | 7.1 | 0.4 | 15.0 | 8.4 |
| mimo-sft-2508 | Adversarial BAAAA | default | Seen | 168 | 840 | 69.0 | 3.0 | 0.0 | 4.3 | 5.7 | 0.4 | 8.9 | 8.7 |
| mimo-sft-2508 | Adversarial BAAAA | default | Unseen | 334 | 1670 | 64.0 | 3.0 | 0.0 | 6.8 | 6.2 | 0.1 | 12.8 | 7.0 |
| mimo-sft-2508 | Adversarial BAAAA | single | Seen | 168 | 840 | 73.2 | 0.6 | 0.0 | 2.4 | 5.5 | 0.5 | 11.0 | 6.9 |
| mimo-sft-2508 | Adversarial BAAAA | single | Unseen | 334 | 1670 | 64.4 | 1.0 | 0.0 | 4.2 | 6.9 | 0.1 | 14.4 | 9.0 |
| mimo-rl-2508 | In-the-Wild | default | Seen | 1539 | 7695 | 60.6 | 12.7 | 0.1 | 0.0 | 11.4 | 0.0 | 7.1 | 8.1 |
| mimo-rl-2508 | In-the-Wild | default | Unseen | 1172 | 5860 | 53.3 | 18.0 | 0.0 | 0.0 | 14.1 | 0.1 | 7.7 | 6.7 |
| mimo-rl-2508 | In-the-Wild | single | Seen | 1539 | 7695 | 69.8 | 1.0 | 0.0 | 0.0 | 11.4 | 0.0 | 8.0 | 9.8 |
| mimo-rl-2508 | In-the-Wild | single | Unseen | 1172 | 5860 | 64.9 | 1.4 | 0.0 | 0.0 | 14.8 | 0.0 | 10.2 | 8.6 |
| mimo-rl-2508 | Homogeneous | default | Seen | 400 | 2000 | 87.0 | 1.8 | 0.1 | 0.0 | 0.0 | 0.0 | 6.0 | 5.2 |
| mimo-rl-2508 | Homogeneous | default | Unseen | 490 | 2450 | 79.8 | 4.5 | 0.5 | 0.0 | 0.0 | 0.0 | 11.6 | 3.6 |
| mimo-rl-2508 | Homogeneous | single | Seen | 400 | 2000 | 88.2 | 0.2 | 0.0 | 0.0 | 0.0 | 0.0 | 6.2 | 5.4 |
| mimo-rl-2508 | Homogeneous | single | Unseen | 490 | 2450 | 79.7 | 0.7 | 0.0 | 0.0 | 0.0 | 0.0 | 14.0 | 5.6 |
| mimo-rl-2508 | Heterogeneous | default | Seen | 312 | 1560 | 48.1 | 21.8 | 0.3 | 0.0 | 13.5 | 0.1 | 6.7 | 9.6 |
| mimo-rl-2508 | Heterogeneous | default | Unseen | 246 | 1230 | 41.5 | 23.2 | 0.0 | 0.0 | 16.5 | 0.0 | 10.2 | 8.6 |
| mimo-rl-2508 | Heterogeneous | single | Seen | 312 | 1560 | 61.8 | 2.1 | 0.0 | 0.0 | 17.6 | 0.0 | 7.5 | 11.0 |
| mimo-rl-2508 | Heterogeneous | single | Unseen | 246 | 1230 | 53.0 | 1.9 | 0.0 | 0.0 | 22.0 | 0.1 | 11.5 | 11.5 |
| mimo-rl-2508 | Adversarial AAAAB | default | Seen | 168 | 840 | 71.7 | 5.4 | 0.0 | 4.2 | 5.0 | 0.0 | 7.0 | 6.8 |
| mimo-rl-2508 | Adversarial AAAAB | default | Unseen | 334 | 1670 | 64.0 | 10.5 | 0.1 | 5.9 | 3.4 | 0.0 | 10.7 | 5.4 |
| mimo-rl-2508 | Adversarial AAAAB | single | Seen | 168 | 840 | 78.3 | 0.6 | 0.0 | 2.5 | 4.9 | 0.0 | 8.7 | 5.0 |
| mimo-rl-2508 | Adversarial AAAAB | single | Unseen | 334 | 1670 | 68.7 | 1.2 | 0.0 | 3.8 | 5.8 | 0.1 | 13.5 | 6.9 |
| mimo-rl-2508 | Adversarial BAAAA | default | Seen | 168 | 840 | 68.8 | 7.1 | 0.0 | 3.6 | 4.5 | 0.0 | 7.9 | 8.1 |
| mimo-rl-2508 | Adversarial BAAAA | default | Unseen | 334 | 1670 | 66.3 | 6.6 | 0.1 | 6.5 | 4.9 | 0.0 | 10.1 | 5.5 |
| mimo-rl-2508 | Adversarial BAAAA | single | Seen | 168 | 840 | 76.7 | 0.8 | 0.0 | 3.2 | 4.9 | 0.0 | 8.7 | 5.7 |
| mimo-rl-2508 | Adversarial BAAAA | single | Unseen | 334 | 1670 | 67.4 | 1.1 | 0.0 | 4.8 | 6.8 | 0.1 | 12.9 | 6.9 |
| qwen3vl-8b-instruct | In-the-Wild | default | Seen | 1539 | 7695 | 75.5 | 0.0 | 0.0 | 0.0 | 10.7 | 0.9 | 7.4 | 5.5 |
| qwen3vl-8b-instruct | In-the-Wild | default | Unseen | 1172 | 5860 | 69.3 | 0.3 | 0.0 | 0.0 | 15.1 | 0.8 | 9.3 | 5.3 |
| qwen3vl-8b-instruct | In-the-Wild | single | Seen | 1539 | 7695 | 75.5 | 0.0 | 0.0 | 0.0 | 10.0 | 0.3 | 7.9 | 6.3 |
| qwen3vl-8b-instruct | In-the-Wild | single | Unseen | 1172 | 5860 | 69.9 | 0.0 | 0.0 | 0.0 | 14.3 | 0.3 | 9.7 | 5.7 |
| qwen3vl-8b-instruct | Homogeneous | default | Seen | 400 | 2000 | 93.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 4.5 | 1.9 |
| qwen3vl-8b-instruct | Homogeneous | default | Unseen | 490 | 2450 | 85.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 12.9 | 1.7 |
| qwen3vl-8b-instruct | Homogeneous | single | Seen | 400 | 2000 | 90.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 6.5 | 2.8 |
| qwen3vl-8b-instruct | Homogeneous | single | Unseen | 490 | 2450 | 83.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 14.0 | 2.4 |
| qwen3vl-8b-instruct | Heterogeneous | default | Seen | 312 | 1560 | 69.3 | 0.0 | 0.0 | 0.0 | 14.0 | 1.7 | 6.9 | 8.1 |
| qwen3vl-8b-instruct | Heterogeneous | default | Unseen | 246 | 1230 | 59.7 | 0.4 | 0.0 | 0.0 | 20.2 | 1.1 | 9.1 | 9.5 |
| qwen3vl-8b-instruct | Heterogeneous | single | Seen | 312 | 1560 | 69.1 | 0.0 | 0.0 | 0.0 | 13.6 | 0.6 | 7.9 | 8.8 |
| qwen3vl-8b-instruct | Heterogeneous | single | Unseen | 246 | 1230 | 61.0 | 0.0 | 0.0 | 0.0 | 20.9 | 0.2 | 9.6 | 8.3 |
| qwen3vl-8b-instruct | Adversarial AAAAB | default | Seen | 168 | 840 | 80.7 | 0.0 | 0.0 | 5.4 | 4.9 | 0.1 | 5.7 | 3.2 |
| qwen3vl-8b-instruct | Adversarial AAAAB | default | Unseen | 334 | 1670 | 73.0 | 0.0 | 0.0 | 7.2 | 5.3 | 0.7 | 11.1 | 2.8 |
| qwen3vl-8b-instruct | Adversarial AAAAB | single | Seen | 168 | 840 | 78.6 | 0.0 | 0.0 | 3.0 | 5.1 | 0.0 | 8.9 | 4.4 |
| qwen3vl-8b-instruct | Adversarial AAAAB | single | Unseen | 334 | 1670 | 73.9 | 0.0 | 0.0 | 4.0 | 5.2 | 0.3 | 12.5 | 4.1 |
| qwen3vl-8b-instruct | Adversarial BAAAA | default | Seen | 168 | 840 | 79.6 | 0.0 | 0.0 | 3.7 | 6.0 | 0.6 | 7.0 | 3.1 |
| qwen3vl-8b-instruct | Adversarial BAAAA | default | Unseen | 334 | 1670 | 73.4 | 0.0 | 0.0 | 5.0 | 6.1 | 0.4 | 11.6 | 3.5 |
| qwen3vl-8b-instruct | Adversarial BAAAA | single | Seen | 168 | 840 | 78.1 | 0.0 | 0.0 | 3.7 | 5.0 | 0.0 | 8.3 | 4.9 |
| qwen3vl-8b-instruct | Adversarial BAAAA | single | Unseen | 334 | 1670 | 72.9 | 0.0 | 0.0 | 4.6 | 5.8 | 0.2 | 12.5 | 4.1 |
| qwen3vl-8b-thinking | In-the-Wild | default | Seen | 1539 | 7695 | 62.6 | 13.4 | 0.0 | 0.0 | 11.0 | 0.1 | 7.3 | 5.6 |
| qwen3vl-8b-thinking | In-the-Wild | default | Unseen | 1172 | 5860 | 53.3 | 17.8 | 0.0 | 0.0 | 14.3 | 0.0 | 8.6 | 6.0 |
| qwen3vl-8b-thinking | In-the-Wild | single | Seen | 1539 | 7695 | 70.6 | 1.4 | 0.0 | 0.0 | 11.6 | 0.0 | 9.5 | 7.0 |
| qwen3vl-8b-thinking | In-the-Wild | single | Unseen | 1172 | 5860 | 65.1 | 1.6 | 0.0 | 0.0 | 16.2 | 0.0 | 10.7 | 6.3 |
| qwen3vl-8b-thinking | Homogeneous | default | Seen | 400 | 2000 | 89.9 | 2.2 | 0.0 | 0.0 | 0.0 | 0.0 | 5.2 | 2.7 |
| qwen3vl-8b-thinking | Homogeneous | default | Unseen | 490 | 2450 | 79.4 | 6.1 | 0.0 | 0.0 | 0.0 | 0.0 | 12.2 | 2.2 |
| qwen3vl-8b-thinking | Homogeneous | single | Seen | 400 | 2000 | 88.2 | 0.6 | 0.0 | 0.0 | 0.0 | 0.0 | 7.7 | 3.5 |
| qwen3vl-8b-thinking | Homogeneous | single | Unseen | 490 | 2450 | 80.4 | 0.9 | 0.0 | 0.0 | 0.0 | 0.0 | 15.7 | 3.0 |
| qwen3vl-8b-thinking | Heterogeneous | default | Seen | 312 | 1560 | 51.3 | 24.0 | 0.0 | 0.0 | 10.8 | 0.2 | 6.9 | 6.7 |
| qwen3vl-8b-thinking | Heterogeneous | default | Unseen | 246 | 1230 | 42.9 | 20.3 | 0.0 | 0.0 | 18.6 | 0.3 | 9.7 | 8.1 |
| qwen3vl-8b-thinking | Heterogeneous | single | Seen | 312 | 1560 | 65.1 | 3.1 | 0.0 | 0.0 | 15.3 | 0.0 | 8.5 | 8.0 |
| qwen3vl-8b-thinking | Heterogeneous | single | Unseen | 246 | 1230 | 53.7 | 1.8 | 0.0 | 0.0 | 23.1 | 0.2 | 11.1 | 10.2 |
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Seen | 168 | 840 | 72.0 | 6.0 | 0.0 | 5.1 | 4.4 | 0.1 | 6.8 | 5.6 |
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Unseen | 334 | 1670 | 63.6 | 11.4 | 0.0 | 6.4 | 4.6 | 0.0 | 10.9 | 3.1 |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Seen | 168 | 840 | 73.5 | 0.6 | 0.0 | 3.6 | 5.0 | 0.1 | 11.4 | 5.8 |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Unseen | 334 | 1670 | 69.0 | 1.0 | 0.0 | 5.3 | 6.5 | 0.0 | 14.1 | 4.0 |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Seen | 168 | 840 | 69.4 | 7.7 | 0.0 | 4.4 | 5.1 | 0.0 | 8.3 | 5.0 |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Unseen | 334 | 1670 | 65.6 | 9.6 | 0.0 | 6.6 | 5.0 | 0.0 | 10.5 | 2.6 |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Seen | 168 | 840 | 73.9 | 1.0 | 0.0 | 3.9 | 5.1 | 0.0 | 10.6 | 5.5 |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Unseen | 334 | 1670 | 68.7 | 1.3 | 0.0 | 5.6 | 6.6 | 0.0 | 14.1 | 3.8 |

## (b) Table 3, strict parse: category of each scored object (% of scored objects)

| model | subset | probe | split | n img | n obj | correct | truncated | unparsed | B=A | borrowed | off-list | in-image | invented |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | In-the-Wild | default | Seen | 1539 | 7695 | 61.0 | 5.8 | 0.0 | 0.0 | 14.3 | 0.2 | 9.5 | 9.1 |
| mimo-sft-2508 | In-the-Wild | default | Unseen | 1172 | 5860 | 55.2 | 8.1 | 0.0 | 0.0 | 17.7 | 0.2 | 10.4 | 8.4 |
| mimo-sft-2508 | In-the-Wild | single | Seen | 1539 | 7695 | 68.2 | 1.2 | 0.0 | 0.0 | 11.1 | 0.5 | 9.2 | 9.7 |
| mimo-sft-2508 | In-the-Wild | single | Unseen | 1172 | 5860 | 62.7 | 1.2 | 0.0 | 0.0 | 14.8 | 0.4 | 11.3 | 9.6 |
| mimo-sft-2508 | Homogeneous | default | Seen | 400 | 2000 | 85.2 | 1.2 | 0.0 | 0.0 | 0.0 | 0.2 | 6.3 | 6.9 |
| mimo-sft-2508 | Homogeneous | default | Unseen | 490 | 2450 | 80.9 | 2.4 | 0.0 | 0.0 | 0.0 | 0.1 | 12.0 | 4.5 |
| mimo-sft-2508 | Homogeneous | single | Seen | 400 | 2000 | 85.1 | 0.5 | 0.0 | 0.0 | 0.0 | 0.4 | 7.5 | 6.5 |
| mimo-sft-2508 | Homogeneous | single | Unseen | 490 | 2450 | 75.8 | 0.4 | 0.0 | 0.0 | 0.0 | 0.3 | 16.7 | 6.8 |
| mimo-sft-2508 | Heterogeneous | default | Seen | 312 | 1560 | 49.4 | 13.8 | 0.0 | 0.0 | 17.2 | 0.3 | 8.5 | 10.8 |
| mimo-sft-2508 | Heterogeneous | default | Unseen | 246 | 1230 | 42.1 | 12.2 | 0.0 | 0.0 | 21.9 | 0.2 | 12.2 | 11.4 |
| mimo-sft-2508 | Heterogeneous | single | Seen | 312 | 1560 | 59.2 | 2.1 | 0.0 | 0.0 | 17.7 | 0.7 | 9.3 | 11.0 |
| mimo-sft-2508 | Heterogeneous | single | Unseen | 246 | 1230 | 49.6 | 1.7 | 0.0 | 0.0 | 23.2 | 0.7 | 12.4 | 12.4 |
| mimo-sft-2508 | Adversarial AAAAB | default | Seen | 168 | 840 | 72.4 | 1.8 | 0.0 | 5.4 | 5.2 | 0.2 | 10.2 | 4.8 |
| mimo-sft-2508 | Adversarial AAAAB | default | Unseen | 334 | 1670 | 64.7 | 3.9 | 0.0 | 6.8 | 5.5 | 0.0 | 13.1 | 6.0 |
| mimo-sft-2508 | Adversarial AAAAB | single | Seen | 168 | 840 | 74.4 | 1.0 | 0.0 | 2.4 | 4.9 | 0.5 | 11.3 | 5.6 |
| mimo-sft-2508 | Adversarial AAAAB | single | Unseen | 334 | 1670 | 64.9 | 1.1 | 0.0 | 3.2 | 7.1 | 0.5 | 15.0 | 8.3 |
| mimo-sft-2508 | Adversarial BAAAA | default | Seen | 168 | 840 | 69.0 | 3.0 | 0.0 | 4.3 | 5.7 | 0.4 | 8.9 | 8.7 |
| mimo-sft-2508 | Adversarial BAAAA | default | Unseen | 334 | 1670 | 64.0 | 3.0 | 0.0 | 6.8 | 6.2 | 0.1 | 12.8 | 7.0 |
| mimo-sft-2508 | Adversarial BAAAA | single | Seen | 168 | 840 | 73.2 | 0.6 | 0.0 | 2.4 | 5.5 | 0.5 | 11.0 | 6.9 |
| mimo-sft-2508 | Adversarial BAAAA | single | Unseen | 334 | 1670 | 64.3 | 1.0 | 0.0 | 4.1 | 6.9 | 0.3 | 14.4 | 9.0 |
| mimo-rl-2508 | In-the-Wild | default | Seen | 1539 | 7695 | 55.7 | 12.7 | 5.8 | 0.0 | 10.9 | 1.2 | 6.6 | 7.1 |
| mimo-rl-2508 | In-the-Wild | default | Unseen | 1172 | 5860 | 46.3 | 18.0 | 10.2 | 0.0 | 12.3 | 1.6 | 6.3 | 5.3 |
| mimo-rl-2508 | In-the-Wild | single | Seen | 1539 | 7695 | 52.9 | 1.0 | 0.0 | 0.0 | 7.5 | 28.6 | 4.7 | 5.2 |
| mimo-rl-2508 | In-the-Wild | single | Unseen | 1172 | 5860 | 47.0 | 1.4 | 0.0 | 0.0 | 8.5 | 33.3 | 5.9 | 3.9 |
| mimo-rl-2508 | Homogeneous | default | Seen | 400 | 2000 | 85.2 | 1.8 | 2.3 | 0.0 | 0.0 | 0.3 | 5.7 | 4.8 |
| mimo-rl-2508 | Homogeneous | default | Unseen | 490 | 2450 | 78.0 | 4.5 | 2.0 | 0.0 | 0.0 | 0.8 | 11.4 | 3.2 |
| mimo-rl-2508 | Homogeneous | single | Seen | 400 | 2000 | 73.7 | 0.2 | 0.0 | 0.0 | 0.0 | 20.4 | 3.6 | 2.0 |
| mimo-rl-2508 | Homogeneous | single | Unseen | 490 | 2450 | 64.4 | 0.7 | 0.0 | 0.0 | 0.0 | 25.3 | 6.8 | 2.9 |
| mimo-rl-2508 | Heterogeneous | default | Seen | 312 | 1560 | 45.4 | 21.8 | 4.5 | 0.0 | 12.3 | 1.0 | 6.2 | 8.8 |
| mimo-rl-2508 | Heterogeneous | default | Unseen | 246 | 1230 | 35.4 | 23.2 | 11.0 | 0.0 | 14.4 | 0.7 | 8.1 | 7.2 |
| mimo-rl-2508 | Heterogeneous | single | Seen | 312 | 1560 | 41.7 | 2.1 | 0.0 | 0.0 | 11.2 | 34.0 | 4.9 | 6.1 |
| mimo-rl-2508 | Heterogeneous | single | Unseen | 246 | 1230 | 32.8 | 1.9 | 0.0 | 0.0 | 11.8 | 41.5 | 5.9 | 6.0 |
| mimo-rl-2508 | Adversarial AAAAB | default | Seen | 168 | 840 | 68.8 | 5.4 | 3.6 | 4.0 | 4.2 | 0.5 | 6.9 | 6.7 |
| mimo-rl-2508 | Adversarial AAAAB | default | Unseen | 334 | 1670 | 59.0 | 10.5 | 6.0 | 5.3 | 2.9 | 1.7 | 10.0 | 4.6 |
| mimo-rl-2508 | Adversarial AAAAB | single | Seen | 168 | 840 | 64.5 | 0.6 | 0.0 | 1.8 | 2.5 | 22.9 | 5.0 | 2.7 |
| mimo-rl-2508 | Adversarial AAAAB | single | Unseen | 334 | 1670 | 52.2 | 1.2 | 0.0 | 1.9 | 3.5 | 30.0 | 7.7 | 3.5 |
| mimo-rl-2508 | Adversarial BAAAA | default | Seen | 168 | 840 | 66.9 | 7.1 | 3.0 | 3.5 | 4.4 | 0.5 | 7.6 | 7.0 |
| mimo-rl-2508 | Adversarial BAAAA | default | Unseen | 334 | 1670 | 62.2 | 6.6 | 5.4 | 6.4 | 4.0 | 1.1 | 9.3 | 5.0 |
| mimo-rl-2508 | Adversarial BAAAA | single | Seen | 168 | 840 | 63.3 | 0.8 | 0.0 | 2.4 | 2.6 | 23.3 | 4.9 | 2.6 |
| mimo-rl-2508 | Adversarial BAAAA | single | Unseen | 334 | 1670 | 52.2 | 1.1 | 0.0 | 3.3 | 3.4 | 29.9 | 6.5 | 3.5 |
| qwen3vl-8b-instruct | In-the-Wild | default | Seen | 1539 | 7695 | 75.4 | 0.0 | 0.0 | 0.0 | 10.7 | 0.9 | 7.4 | 5.5 |
| qwen3vl-8b-instruct | In-the-Wild | default | Unseen | 1172 | 5860 | 68.5 | 0.3 | 1.2 | 0.0 | 15.1 | 0.8 | 9.0 | 5.2 |
| qwen3vl-8b-instruct | In-the-Wild | single | Seen | 1539 | 7695 | 75.5 | 0.0 | 0.0 | 0.0 | 10.0 | 0.3 | 7.9 | 6.3 |
| qwen3vl-8b-instruct | In-the-Wild | single | Unseen | 1172 | 5860 | 69.9 | 0.0 | 0.0 | 0.0 | 14.3 | 0.3 | 9.7 | 5.7 |
| qwen3vl-8b-instruct | Homogeneous | default | Seen | 400 | 2000 | 93.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 4.5 | 1.9 |
| qwen3vl-8b-instruct | Homogeneous | default | Unseen | 490 | 2450 | 85.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 12.9 | 1.7 |
| qwen3vl-8b-instruct | Homogeneous | single | Seen | 400 | 2000 | 90.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 6.5 | 2.8 |
| qwen3vl-8b-instruct | Homogeneous | single | Unseen | 490 | 2450 | 83.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 14.0 | 2.4 |
| qwen3vl-8b-instruct | Heterogeneous | default | Seen | 312 | 1560 | 68.8 | 0.0 | 0.4 | 0.0 | 14.0 | 1.8 | 6.9 | 8.1 |
| qwen3vl-8b-instruct | Heterogeneous | default | Unseen | 246 | 1230 | 59.1 | 0.4 | 0.8 | 0.0 | 20.2 | 1.1 | 8.9 | 9.4 |
| qwen3vl-8b-instruct | Heterogeneous | single | Seen | 312 | 1560 | 69.1 | 0.0 | 0.0 | 0.0 | 13.6 | 0.6 | 7.9 | 8.8 |
| qwen3vl-8b-instruct | Heterogeneous | single | Unseen | 246 | 1230 | 61.0 | 0.0 | 0.0 | 0.0 | 20.9 | 0.2 | 9.6 | 8.3 |
| qwen3vl-8b-instruct | Adversarial AAAAB | default | Seen | 168 | 840 | 80.7 | 0.0 | 0.0 | 5.4 | 4.9 | 0.1 | 5.7 | 3.2 |
| qwen3vl-8b-instruct | Adversarial AAAAB | default | Unseen | 334 | 1670 | 73.0 | 0.0 | 0.0 | 7.2 | 5.3 | 0.7 | 11.1 | 2.8 |
| qwen3vl-8b-instruct | Adversarial AAAAB | single | Seen | 168 | 840 | 78.6 | 0.0 | 0.0 | 3.0 | 5.1 | 0.0 | 8.9 | 4.4 |
| qwen3vl-8b-instruct | Adversarial AAAAB | single | Unseen | 334 | 1670 | 73.9 | 0.0 | 0.0 | 4.0 | 5.2 | 0.3 | 12.5 | 4.1 |
| qwen3vl-8b-instruct | Adversarial BAAAA | default | Seen | 168 | 840 | 79.2 | 0.0 | 0.5 | 3.7 | 6.0 | 0.7 | 7.0 | 3.0 |
| qwen3vl-8b-instruct | Adversarial BAAAA | default | Unseen | 334 | 1670 | 72.8 | 0.0 | 0.5 | 5.0 | 6.1 | 0.5 | 11.5 | 3.5 |
| qwen3vl-8b-instruct | Adversarial BAAAA | single | Seen | 168 | 840 | 78.1 | 0.0 | 0.0 | 3.7 | 5.0 | 0.0 | 8.3 | 4.9 |
| qwen3vl-8b-instruct | Adversarial BAAAA | single | Unseen | 334 | 1670 | 72.9 | 0.0 | 0.0 | 4.6 | 5.8 | 0.2 | 12.5 | 4.1 |
| qwen3vl-8b-thinking | In-the-Wild | default | Seen | 1539 | 7695 | 62.6 | 13.4 | 0.0 | 0.0 | 11.0 | 0.1 | 7.3 | 5.6 |
| qwen3vl-8b-thinking | In-the-Wild | default | Unseen | 1172 | 5860 | 53.3 | 17.8 | 0.0 | 0.0 | 14.3 | 0.0 | 8.6 | 6.0 |
| qwen3vl-8b-thinking | In-the-Wild | single | Seen | 1539 | 7695 | 70.6 | 1.4 | 0.0 | 0.0 | 11.6 | 0.0 | 9.5 | 7.0 |
| qwen3vl-8b-thinking | In-the-Wild | single | Unseen | 1172 | 5860 | 65.1 | 1.6 | 0.0 | 0.0 | 16.2 | 0.0 | 10.7 | 6.3 |
| qwen3vl-8b-thinking | Homogeneous | default | Seen | 400 | 2000 | 89.9 | 2.2 | 0.0 | 0.0 | 0.0 | 0.0 | 5.2 | 2.7 |
| qwen3vl-8b-thinking | Homogeneous | default | Unseen | 490 | 2450 | 79.4 | 6.1 | 0.0 | 0.0 | 0.0 | 0.0 | 12.2 | 2.2 |
| qwen3vl-8b-thinking | Homogeneous | single | Seen | 400 | 2000 | 88.2 | 0.6 | 0.0 | 0.0 | 0.0 | 0.0 | 7.7 | 3.5 |
| qwen3vl-8b-thinking | Homogeneous | single | Unseen | 490 | 2450 | 80.4 | 0.9 | 0.0 | 0.0 | 0.0 | 0.0 | 15.7 | 3.0 |
| qwen3vl-8b-thinking | Heterogeneous | default | Seen | 312 | 1560 | 51.3 | 24.0 | 0.0 | 0.0 | 10.8 | 0.2 | 6.9 | 6.7 |
| qwen3vl-8b-thinking | Heterogeneous | default | Unseen | 246 | 1230 | 42.9 | 20.3 | 0.0 | 0.0 | 18.6 | 0.3 | 9.7 | 8.1 |
| qwen3vl-8b-thinking | Heterogeneous | single | Seen | 312 | 1560 | 65.1 | 3.1 | 0.0 | 0.0 | 15.3 | 0.0 | 8.5 | 8.0 |
| qwen3vl-8b-thinking | Heterogeneous | single | Unseen | 246 | 1230 | 53.7 | 1.8 | 0.0 | 0.0 | 23.1 | 0.2 | 11.1 | 10.2 |
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Seen | 168 | 840 | 72.0 | 6.0 | 0.0 | 5.1 | 4.4 | 0.1 | 6.8 | 5.6 |
| qwen3vl-8b-thinking | Adversarial AAAAB | default | Unseen | 334 | 1670 | 63.6 | 11.4 | 0.0 | 6.4 | 4.6 | 0.0 | 10.9 | 3.1 |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Seen | 168 | 840 | 73.5 | 0.6 | 0.0 | 3.6 | 5.0 | 0.1 | 11.4 | 5.8 |
| qwen3vl-8b-thinking | Adversarial AAAAB | single | Unseen | 334 | 1670 | 69.0 | 1.0 | 0.0 | 5.3 | 6.5 | 0.0 | 14.1 | 4.0 |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Seen | 168 | 840 | 69.4 | 7.7 | 0.0 | 4.4 | 5.1 | 0.0 | 8.3 | 5.0 |
| qwen3vl-8b-thinking | Adversarial BAAAA | default | Unseen | 334 | 1670 | 65.6 | 9.6 | 0.0 | 6.6 | 5.0 | 0.0 | 10.5 | 2.6 |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Seen | 168 | 840 | 73.9 | 1.0 | 0.0 | 3.9 | 5.1 | 0.0 | 10.6 | 5.5 |
| qwen3vl-8b-thinking | Adversarial BAAAA | single | Unseen | 334 | 1670 | 68.7 | 1.3 | 0.0 | 5.6 | 6.6 | 0.0 | 14.1 | 3.8 |

## (c) The odd box B on Adversarial (tolerant)

One B box per image: box 5 in AAAAB, box 1 in BAAAA. B=A = B labelled with A, the class of the other four boxes. A truncated B box counts as truncated, not as B=A. CI = bootstrap over images.

| model | order | probe | split | n img | B correct | B=A [95% CI] | B truncated | B other error |
|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | AAAAB | default | Seen | 168 | 50.0 | 26.2 [19.6, 33.3] | 1.8 | 22.0 |
| mimo-sft-2508 | AAAAB | default | Unseen | 334 | 40.7 | 34.1 [29.0, 39.5] | 3.9 | 21.3 |
| mimo-sft-2508 | AAAAB | single | Seen | 168 | 58.3 | 11.9 [7.1, 17.3] | 1.8 | 28.0 |
| mimo-sft-2508 | AAAAB | single | Unseen | 334 | 56.0 | 15.9 [12.3, 19.8] | 2.1 | 26.0 |
| mimo-sft-2508 | BAAAA | default | Seen | 168 | 53.0 | 21.4 [15.5, 28.0] | 3.0 | 22.6 |
| mimo-sft-2508 | BAAAA | default | Unseen | 334 | 43.4 | 34.1 [29.0, 39.2] | 3.0 | 19.5 |
| mimo-sft-2508 | BAAAA | single | Seen | 168 | 58.3 | 11.9 [7.1, 17.3] | 1.2 | 28.6 |
| mimo-sft-2508 | BAAAA | single | Unseen | 334 | 54.5 | 21.0 [16.5, 25.4] | 1.5 | 23.1 |
| mimo-rl-2508 | AAAAB | default | Seen | 168 | 56.5 | 20.8 [14.9, 27.4] | 5.4 | 17.3 |
| mimo-rl-2508 | AAAAB | default | Unseen | 334 | 42.2 | 29.3 [24.6, 34.4] | 10.5 | 18.0 |
| mimo-rl-2508 | AAAAB | single | Seen | 168 | 63.7 | 12.5 [7.7, 17.3] | 0.6 | 23.2 |
| mimo-rl-2508 | AAAAB | single | Unseen | 334 | 57.2 | 18.9 [15.0, 23.1] | 2.7 | 21.3 |
| mimo-rl-2508 | BAAAA | default | Seen | 168 | 51.8 | 17.9 [12.5, 23.8] | 7.1 | 23.2 |
| mimo-rl-2508 | BAAAA | default | Unseen | 334 | 44.6 | 32.6 [27.8, 37.7] | 6.6 | 16.2 |
| mimo-rl-2508 | BAAAA | single | Seen | 168 | 58.9 | 16.1 [10.7, 22.0] | 1.2 | 23.8 |
| mimo-rl-2508 | BAAAA | single | Unseen | 334 | 54.2 | 24.0 [19.5, 28.7] | 1.5 | 20.4 |
| qwen3vl-8b-instruct | AAAAB | default | Seen | 168 | 57.7 | 26.8 [20.2, 33.3] | 0.0 | 15.5 |
| qwen3vl-8b-instruct | AAAAB | default | Unseen | 334 | 49.7 | 35.9 [30.8, 41.0] | 0.0 | 14.4 |
| qwen3vl-8b-instruct | AAAAB | single | Seen | 168 | 63.1 | 14.9 [9.5, 20.2] | 0.0 | 22.0 |
| qwen3vl-8b-instruct | AAAAB | single | Unseen | 334 | 59.6 | 20.1 [15.6, 24.6] | 0.0 | 20.4 |
| qwen3vl-8b-instruct | BAAAA | default | Seen | 168 | 61.3 | 18.5 [12.5, 24.4] | 0.0 | 20.2 |
| qwen3vl-8b-instruct | BAAAA | default | Unseen | 334 | 56.0 | 25.1 [20.4, 29.9] | 0.0 | 18.9 |
| qwen3vl-8b-instruct | BAAAA | single | Seen | 168 | 61.9 | 18.5 [13.1, 24.4] | 0.0 | 19.6 |
| qwen3vl-8b-instruct | BAAAA | single | Unseen | 334 | 57.2 | 22.8 [18.0, 27.5] | 0.0 | 20.1 |
| qwen3vl-8b-thinking | AAAAB | default | Seen | 168 | 50.0 | 25.6 [19.6, 32.1] | 6.0 | 18.5 |
| qwen3vl-8b-thinking | AAAAB | default | Unseen | 334 | 41.3 | 32.0 [27.2, 36.8] | 11.4 | 15.3 |
| qwen3vl-8b-thinking | AAAAB | single | Seen | 168 | 56.5 | 17.9 [12.5, 23.8] | 1.2 | 24.4 |
| qwen3vl-8b-thinking | AAAAB | single | Unseen | 334 | 50.3 | 26.6 [21.6, 31.4] | 2.1 | 21.0 |
| qwen3vl-8b-thinking | BAAAA | default | Seen | 168 | 54.2 | 22.0 [16.1, 28.6] | 7.7 | 16.1 |
| qwen3vl-8b-thinking | BAAAA | default | Unseen | 334 | 41.6 | 33.2 [28.4, 38.0] | 9.6 | 15.6 |
| qwen3vl-8b-thinking | BAAAA | single | Seen | 168 | 56.0 | 19.6 [13.7, 25.6] | 1.2 | 23.2 |
| qwen3vl-8b-thinking | BAAAA | single | Unseen | 334 | 50.3 | 27.8 [23.1, 32.9] | 1.8 | 20.1 |

## (d) Composition of the errors, all five subsets pooled (tolerant, % of wrong objects)

Same items for every model, so rows of one split are comparable across models. B=A only exists on Adversarial, which is 1,680 of 12,935 Seen and 3,340 of 12,880 Unseen objects.

| model | probe | split | n wrong / n obj | truncated | unparsed | B=A | borrowed | off-list | in-image | invented |
|---|---|---|---|---|---|---|---|---|---|---|
| mimo-sft-2508 | default | Seen | 4574 / 12935 | 16.0 | 0.0 | 1.7 | 31.9 | 0.7 | 25.1 | 24.5 |
| mimo-sft-2508 | default | Unseen | 4994 / 12880 | 16.0 | 0.0 | 4.6 | 30.1 | 0.3 | 29.7 | 19.3 |
| mimo-sft-2508 | single | Seen | 3816 / 12935 | 3.8 | 0.0 | 1.0 | 32.0 | 1.5 | 31.2 | 30.4 |
| mimo-sft-2508 | single | Unseen | 4577 / 12880 | 2.9 | 0.0 | 2.7 | 30.3 | 0.9 | 37.5 | 25.7 |
| mimo-rl-2508 | default | Seen | 4598 / 12935 | 31.6 | 0.2 | 1.4 | 25.4 | 0.0 | 19.5 | 21.8 |
| mimo-rl-2508 | default | Unseen | 5114 / 12880 | 33.9 | 0.4 | 4.0 | 22.9 | 0.1 | 23.7 | 15.1 |
| mimo-rl-2508 | single | Seen | 3536 / 12935 | 3.6 | 0.0 | 1.4 | 34.9 | 0.1 | 28.4 | 31.7 |
| mimo-rl-2508 | single | Unseen | 4198 / 12880 | 3.8 | 0.0 | 3.4 | 32.2 | 0.1 | 36.4 | 24.2 |
| qwen3vl-8b-instruct | default | Seen | 2834 / 12935 | 0.0 | 0.0 | 2.7 | 40.1 | 3.7 | 30.8 | 22.6 |
| qwen3vl-8b-instruct | default | Unseen | 3553 / 12880 | 0.6 | 0.0 | 5.7 | 37.3 | 2.3 | 37.9 | 16.1 |
| qwen3vl-8b-instruct | single | Seen | 2916 / 12935 | 0.0 | 0.0 | 1.9 | 36.6 | 1.1 | 34.6 | 25.8 |
| qwen3vl-8b-instruct | single | Unseen | 3533 / 12880 | 0.0 | 0.0 | 4.0 | 36.2 | 0.9 | 40.9 | 17.9 |
| qwen3vl-8b-thinking | default | Seen | 4329 / 12935 | 36.2 | 0.0 | 1.8 | 25.3 | 0.2 | 20.9 | 15.7 |
| qwen3vl-8b-thinking | default | Unseen | 5125 / 12880 | 35.0 | 0.0 | 4.3 | 23.9 | 0.1 | 24.9 | 11.8 |
| qwen3vl-8b-thinking | single | Seen | 3488 / 12935 | 5.1 | 0.0 | 1.8 | 34.9 | 0.1 | 34.5 | 23.7 |
| qwen3vl-8b-thinking | single | Unseen | 4133 / 12880 | 4.2 | 0.0 | 4.4 | 35.2 | 0.1 | 39.2 | 17.0 |

## (e) Checks

- Rows read (after deduplication): 41304. Image ids that do not match the ROPE entry: 0. Adversarial rows whose four non-B boxes do not share one class: 0.
- tolerant: the harness's error_type, rerun on the stored labels, differs from the stored type for 0 objects. Outside cut calls, the category here maps back to a different stored type for 0 of 197502 objects.
- strict: the harness's error_type, rerun on the stored labels, differs from the stored type for 0 objects. Outside cut calls, the category here maps back to a different stored type for 0 of 197502 objects.

| model | probe | split | rows | objects |
|---|---|---|---|---|
| mimo-sft-2508 | default | Seen | 2587 | 12935 |
| mimo-sft-2508 | default | Unseen | 2576 | 12880 |
| mimo-sft-2508 | single | Seen | 2587 | 12935 |
| mimo-sft-2508 | single | Unseen | 2576 | 12880 |
| mimo-rl-2508 | default | Seen | 2587 | 12935 |
| mimo-rl-2508 | default | Unseen | 2576 | 12880 |
| mimo-rl-2508 | single | Seen | 2587 | 12935 |
| mimo-rl-2508 | single | Unseen | 2576 | 12880 |
| qwen3vl-8b-instruct | default | Seen | 2587 | 12935 |
| qwen3vl-8b-instruct | default | Unseen | 2576 | 12880 |
| qwen3vl-8b-instruct | single | Seen | 2587 | 12935 |
| qwen3vl-8b-instruct | single | Unseen | 2576 | 12880 |
| qwen3vl-8b-thinking | default | Seen | 2587 | 12935 |
| qwen3vl-8b-thinking | default | Unseen | 2576 | 12880 |
| qwen3vl-8b-thinking | single | Seen | 2587 | 12935 |
| qwen3vl-8b-thinking | single | Unseen | 2576 | 12880 |

