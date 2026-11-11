# rope_runner: vLLM runner for ROPE (CSE 595)

Runs the ROPE multi-object probes on MiMo-VL-7B (SFT-2508, RL-2508) and Qwen3-VL-8B (Instruct, Thinking) with offline vLLM, scores them with the official `sled-group/moh` scorer, and writes one JSONL row per (model, probe settings, image).

The moh code in `third_party/moh` and the pieces copied from it have no licence file; they are copied with attribution to their authors (sled-group/moh).

## Setup and first run

### 1. Code and variables

The code comes from one of two places. Either clone this repository on Great Lakes and use its folder `harness/`, or download `rope_harness.zip` from the team's Google Drive folder, copy it to Great Lakes and unzip it:

```bash
scp rope_harness.zip <uniqname>@greatlakes.arc-ts.umich.edu:~/      # from your own computer
mkdir -p ~/cse595 && cd ~/cse595 && unzip ~/rope_harness.zip          # on Great Lakes: ~/cse595/rope_harness
```

If you use the clone, put the path of its `harness/` folder wherever the commands below say `~/cse595/rope_harness`.

Everything that depends on the user is an environment variable read by `env.sh`. Export the ones you want to change before you source it, for example in `~/.bashrc`:

| variable | what | default |
|---|---|---|
| `CSE595_CODE` | this code folder | the folder `env.sh` is in |
| `CSE595_ROOT` | folder that holds `venv/`, `models/`, `data/ROPE/`, `hf/` | `$HOME/cse595` |
| `CSE595_VENV` | Python venv | `$CSE595_ROOT/venv` |
| `MODELS_DIR` | model folders | `$CSE595_ROOT/models` |
| `ROPE_DIR` | ROPE data (`train/`, `validation/`) | `$CSE595_ROOT/data/ROPE` |
| `HF_HOME` | Hugging Face cache | `$CSE595_ROOT/hf` |
| `CSE595_RUNS` | run outputs | `runs/` beside the code folder |
| `CSE595_LOGS` | Slurm logs | `$CSE595_RUNS/logs` |
| `CSE595_ACCOUNT` | Slurm account | `cse595f26_class` |

Keep `CSE595_ROOT` under `$HOME`. The environment needs about 30 GB and 70,000 files, and the class scratch folder `/scratch/cse595f26_class_root/cse595f26_class/` cannot take new files at the moment because its file count is at the limit. The home quota is 80 GB; `home-quota` shows how much of it you use.

Then, in every new shell:

```bash
source ~/cse595/rope_harness/env.sh    # module python/3.11.5, the venv, the proxy, the variables above
```

### 2. Environment

The venv takes 9.8 GB and 59,000 files; one model 16.6 to 17.5 GB; ROPE 3.3 GB and 10,335 files once unpacked (the zips add 3.3 GB until you delete them). Build the venv first; `env.sh` activates it, so source `env.sh` only after this step.

```bash
module load python/3.11.5
mkdir -p ~/cse595
python -m venv ~/cse595/venv
source ~/cse595/venv/bin/activate
pip install --no-cache-dir -r ~/cse595/rope_harness/requirements.txt   # vllm 0.11.0, transformers 4.57.6, torch 2.8.0
```

Download the model you were assigned (repo id, revision, folder name):

| key | Hugging Face repo | revision | folder under `$MODELS_DIR` |
|---|---|---|---|
| `mimo-sft-2508` | `XiaomiMiMo/MiMo-VL-7B-SFT-2508` | `11e8fdc278f5e1e6a72f9561772a6d7cd6921d33` | `MiMo-VL-7B-SFT-2508` |
| `mimo-rl-2508` | `XiaomiMiMo/MiMo-VL-7B-RL-2508` | `ec4ebdc29b83b94aa7f62670c78376250dad8dbc` | `MiMo-VL-7B-RL-2508` |
| `qwen3vl-8b-instruct` | `Qwen/Qwen3-VL-8B-Instruct` | `0c351dd01ed87e9c1b53cbc748cba10e6187ff3b` | `Qwen3-VL-8B-Instruct` |
| `qwen3vl-8b-thinking` | `Qwen/Qwen3-VL-8B-Thinking` | `92f3c4b4feadd3a016ef468d103bb5f58b2a2c6b` | `Qwen3-VL-8B-Thinking` |

```bash
source ~/cse595/rope_harness/env.sh
hf download XiaomiMiMo/MiMo-VL-7B-SFT-2508 --revision 11e8fdc278f5e1e6a72f9561772a6d7cd6921d33 \
    --local-dir $MODELS_DIR/MiMo-VL-7B-SFT-2508
```

ROPE comes from the dataset repo `sled-umich/ROPE` at revision `b4939b83aae74c650794eb48853cc383c2b666e1`. Each zip holds its split's five JSON files and images:

```bash
hf download sled-umich/ROPE --repo-type dataset --revision b4939b83aae74c650794eb48853cc383c2b666e1 \
    --include train.zip validation.zip --local-dir $ROPE_DIR
cd $ROPE_DIR && unzip -q train.zip -x '__MACOSX/*' && unzip -q validation.zip -x '__MACOSX/*' \
    && rm train.zip validation.zip
```

`train.zip` unpacks its images to `train/images/` while its JSON files say `train/image/`. `rope_runner/data.py` falls back to the plural folder, so leave the folders as they unpack.

### 3. CPU tests and a dry run

```bash
cd $CSE595_CODE
python -m pytest -q tests
python -m rope_runner.run --model mimo-sft-2508 --probe default --split validation --limit 5 \
    --greedy --dry-run --out /tmp/$USER/dry.jsonl
```

The tests use a fake model and the small fixture in `tests/fixtures`. The dry run reads your real `$ROPE_DIR` with the fake model and ends with `dry run: 0 image files missing` when the data is in place. Delete `/tmp/$USER/dry.jsonl` before running it again.

### 4. Smoke test on the GPU

`scripts/run.sbatch` runs one model on one split, for each probe in `PROBES` (default `default single`), greedy, with `--resume`. Required: `MODEL`, `SPLIT` (`train` = Seen, `validation` = Unseen), `OUT`. Optional: `SUBSETS` (default: the probe's subsets in `configs/probes.yaml`, all five for default and single), `LIMIT` (first N items per subset), `EXTRA` (more `rope_runner.run` flags). Account and log files go on the sbatch line. It asks for one GPU on `spgpu` (A40) or `gpu-rtx6000` (RTX PRO 6000) for 4 hours. Submit from the code folder:

```bash
cd $CSE595_CODE && source env.sh && mkdir -p $CSE595_LOGS
M=mimo-sft-2508
sbatch -A $CSE595_ACCOUNT -o "$CSE595_LOGS/%x-%j.out" -e "$CSE595_LOGS/%x-%j.err" \
    --export=ALL,MODEL=$M,SPLIT=validation,LIMIT=100,OUT=$CSE595_RUNS/smoke_${M}_validation.jsonl \
    scripts/run.sbatch
```

That is the first 100 items of each of the five subsets, default and single, so 1,000 rows. The log prints the settings, the GPU, `[run] wrote ...` per chunk and the summary table from `rope_runner.analyze` at the end.

### 5. Full run with resume

The full set is 5,163 items: 2,587 in `train` and 2,576 in `validation`. One split of one model takes more than one 4-hour job. Submit the same command several times under one job name with `--dependency=singleton`. The jobs then run one after another, and each continues the JSONL where the last one stopped (`--resume` skips keys already written; a line torn by the time limit is dropped). A job that finds nothing left to do prints `0 images to do` and ends.

```bash
cd $CSE595_CODE && source env.sh
M=mimo-sft-2508
for SPLIT in validation train; do
  for i in 1 2 3 4; do
    sbatch -J rope-$M --dependency=singleton -A $CSE595_ACCOUNT \
        -o "$CSE595_LOGS/%x-%j.out" -e "$CSE595_LOGS/%x-%j.err" \
        --export=ALL,MODEL=$M,SPLIT=$SPLIT,OUT=$CSE595_RUNS/full_${M}_${SPLIT}.jsonl scripts/run.sbatch
  done
done
```

A split is done when its file has one row per item and probe: `wc -l` gives 5,152 for validation and 5,174 for train with default and single. If it has fewer, submit the same line again.

The other probes use the same script:

```bash
--export=ALL,MODEL=$M,SPLIT=validation,PROBES=teacher_forcing,EXTRA="--tf-mode oneshot",OUT=...
--export=ALL,MODEL=$M,SPLIT=validation,PROBES=teacher_forcing,EXTRA="--tf-mode incremental",OUT=...
--export=ALL,MODEL=$M,SPLIT=validation,PROBES=counterfactual,OUT=...      # AAAAB and BAAAA only
--export=ALL,MODEL=$M,SPLIT=validation,EXTRA="--budget 512",OUT=...       # truncate-and-close at 512 thinking tokens
--export=ALL,MODEL=$M,SPLIT=validation,EXTRA="--no-think",OUT=...         # MiMo 2508 only
```

The probe settings are part of each row's key, so several settings can share one OUT file. By hand, inside a GPU job after `source env.sh`, the same run is `python -m rope_runner.run --model ... --probe ... --split ... --greedy --out ... --resume`, and `python -m rope_runner.analyze <file.jsonl>` prints the table.

### 6. Output

Each run appends one JSON line per (model, probe settings, item) to `OUT`. A row has the raw model output of every call, the thinking trace and the stripped answer, the strict (official moh) and tolerant parses with their correctness flags and error types, the gold labels, `finish_reason` and token counts, and the model path and decoding settings. The full list is in the JSONL schema section below.

### 7. Team rules

- The official ROPE prompts go to the model unchanged; `prompts.py` copies them from moh and `tests/test_prompts.py` checks them against moh's own code.
- Decoding is greedy (`--greedy`; `run.sbatch` always passes it).
- Every row carries both the strict score (moh's parser) and the tolerant score. Report both.
- The token limit is applied per model call. A call with `finish_reason == "length"` counts as wrong for every object it answers: all five objects of the image for default, the one object of that call for single (and for each teacher-forcing or counterfactual call, the object it asks). The stored `correct_flags` do not apply this rule, because a cut answer can still parse; apply it when you compute accuracy, keep those objects in the denominator, and report how many calls hit the limit.
- Keep the raw JSONL files and the exact sbatch command for every run. The first lines of the job log repeat the settings.
- Model keys: `mimo-sft-2508`, `mimo-rl-2508`, `qwen3vl-8b-instruct`, `qwen3vl-8b-thinking`. Subsets use moh's folder names: `AAAAB BAAAA heterogenous homogenous mixed`. Without `--greedy`, each model uses its card's recommended sampling from `configs/models.yaml`.

## What the probes send

All prompt text goes in the single user turn, image first, through the model's own HF chat template. The rendered string is sent to vLLM as a raw prompt.

| probe | calls / image | user text | scored objects |
|---|---|---|---|
| default | 1 | moh multi-object prompt | 1-5 |
| single | 5 | moh single-object prompt for Obj.k | 1-5 |
| teacher_forcing, incremental | 5 | moh prompt + ` obj1: g1, ..., objk:` (moh's cumulative prompt) | k-th segment of call k |
| teacher_forcing, oneshot | 1 | moh prompt + ` obj1: g1, obj2: g2, obj3: g3, obj4: g4, obj5:` (= moh's k=5 call); on BAAAA: ` obj2: g2, obj3: g3, obj4: g4, obj5: g5, obj1:` | 5 (BAAAA: 1) |
| counterfactual | 1 | the same, with the four given labels replaced by C | 5 (BAAAA: 1) |
| `--no-think` (MiMo 2508) | as the probe | the probe's text + ` /no_think` | as the probe |

C is drawn per image from the split's 50-class list minus the image's `object_set`. The seed is `sha256(seed|split|subset/entry_idx/image_id)`, so the draw does not depend on run order (seed in `configs/probes.yaml`). The prefix goes in the user turn, as in moh. moh does not cover where a thinking model should get it.

In AAAAB and BAAAA, B is the odd object (position 5 in AAAAB, position 1 in BAAAA) and A is the class of the other four. One-shot teacher forcing and counterfactual ask B.

Dry run of any probe on CPU (fake model, real data, 5 images):

```bash
python -m rope_runner.run --model mimo-sft-2508 --probe counterfactual --split validation --subset BAAAA \
    --limit 5 --greedy --dry-run --out /tmp/$USER/dry_cf.jsonl
```

## JSONL schema (one row per model × probe settings × image)

Per-call fields are lists, one element per model call (1 or 5). Per-object fields are lists over the scored objects (5, or 1 for oneshot and counterfactual).

| field | meaning |
|---|---|
| `key` | `model\|probe\|variant\|split\|subset\|entry_idx\|image_id`, used by `--resume` |
| `image_id`, `entry_idx`, `image_path` | PNG stem, position in the JSON file, the bbox PNG the model saw |
| `subset`, `split`, `probe`, `tf_mode`, `no_think`, `budget`, `variant` | run settings (`variant` = greedy/recommended, seed, tf mode, no_think, budget, prefix caching when set) |
| `counterfactual_class` | C (counterfactual only) |
| `prefix_used` | per call: text appended to the official prompt (`""` for default/single) |
| `asked_objects` | per call: the object the call asks about (`null` = all five) |
| `raw_output` | per call: full generated text (including the injected early-stop phrase when forced) |
| `trace_text`, `stripped_answer` | per call: thinking part / text after the last `</think>` |
| `think_closed` | per call: True = `</think>` seen, False = thinking never closed (answer = ""), None = no thinking |
| `forced_close` | per call: truncate-and-close fired |
| `thinking_tokens`, `answer_tokens` | per call: generated tokens before / after `</think>` |
| `finish_reason` | per call: vLLM finish reason of the last generation step (`length` = hit the token limit) |
| `prompt_tokens`, `cached_tokens` | per call: prompt tokens and those served from vLLM's prefix cache |
| `parsed_labels`, `gold_labels`, `obj_indices` | strict (moh) parse, gold, and 1-based object positions |
| `correct_flags`, `error_types` | strict correctness and error type per scored object |
| `tolerant_labels`, `tolerant_correct_flags`, `tolerant_error_types` | the same for the tolerant parser |
| `moh_total` | this row's contribution to moh's `total_predictions` (see quirks) |
| `all_gold_labels`, `data_source` | all 5 gold names, COCO/ADE |
| `prefix_caching` | the `--prefix-caching` setting |
| `chunk_id`, `chunk_images`, `chunk_wall_s` | the checkpoint chunk the row was written in, its size and its generation wall time |
| `model`, `model_path`, `sampling`, `run_timestamp` | provenance |

Error types: `inertia` = AAAAB object 5 labelled A; `borrowed` = another target object's class; `invented` = in the candidate list but not a target class; `copied_prefix` = counterfactual C; `off_list` = not in the 50-class list (a formatting failure, not a hallucination); `unparsed` = no label recovered. `null` = correct.

## Copied from moh vs written new

moh: https://github.com/sled-group/moh @ `9483f2e4a69a90aee339b2305c1f5866daeba1a0` (2024-11-13). `third_party/moh` holds the four files the tests import (`evaluation.py`, `image_processor.py`, `utils.py`, `constant.py`). moh has no licence file, so we copy it with attribution and do not redistribute it. Every copied piece has a header comment naming its source.

Copied verbatim:
- `rope_runner/constant.py` = `constant.py` (class lists), whole file.
- `data.py`: `JSON_FILES` and `file2folder_dict` (`data_handler.py`); the image path expression and RGBA conversion (`evaluation.py`, `image_processor.py`); the split/source class-list branch of `_generate_prompt` (`self.data_type` became an argument).
- `prompts.py`: the multi-object prompt string and the single-object f-string; the teacher-forcing cumulative-prompt loop (`TeacherForcingEvaluation.process_entry`), moved into a function.
- `scoring.py`: `segment_classes` verbatim. The accounting of `MultiObjectEvaluation`, `SingleObjectEvaluation` and `TeacherForcingEvaluation.process_entry` is re-expressed per row. `tests/test_scoring.py` runs moh's own classes on the same responses and checks that `correct_predictions`, `total_predictions` and `acc_list` match exactly.

Written new: the vLLM loader (`models.py`), think-tag stripping, the one-shot and counterfactual prefixes, the `/no_think` suffix, truncate-and-close (`budget.py`), the tolerant parser, error typing, JSONL output, checkpoint/resume (`run.py`), `analyze.py`, and the CPU fake model.

## moh scoring quirks we keep (strict = official)

- Default: a response that `segment_classes` cannot parse (no `", "`/`": "` structure, e.g. newline-separated or markdown) counts all five objects wrong. moh also adds 5 to `total_predictions` twice, so `moh_total = 10`. `analyze.py` reports both `strict` (correct / 5 per image) and `moh` (correct / moh's total).
- Single: `response.lower() == gold`, with no stripping or parsing, so `dog.` or `Obj.1: dog` is wrong.
- Teacher forcing (incremental): call k must return the full `obj1: ..., objk: ...` list; moh takes the k-th segment. A bare class answer fails to parse. At the first failure moh stops, objects k..5 count wrong, and `5-k+1` more is added to the total.
- Oneshot / counterfactual: these have no moh counterpart. We apply moh's index-k rule (`segment_classes`, take segment k, where k is the asked object: 5, or 1 on BAAAA) and `moh_total = 1`.
- One deviation: we `.strip()` the answer after removing the think block. moh's HF handlers (Yi-VL, LLaVA-NeXT) also strip.

The tolerant parser (`objK:` anywhere, markdown and case removed, mapped to the longest matching candidate; a bare class for single-object questions) is reported next to the strict one and never replaces it.

## Truncate-and-close (`--budget N`)

1. Generate with `max_tokens=N`.
2. If thinking is open (`<think>` was emitted, as MiMo does, or prefilled by the template, as Qwen3-VL-Thinking does) and no `</think>` came, append Qwen3's early-stop phrase `"\n\nConsidering the limited time by the user, I have to give the solution based on the thinking directly now.\n</think>\n\n"` and continue for `answer_max_tokens` (128).
3. If `</think>` came but the cap cut the answer, continue plainly.

`thinking_tokens` = N for forced rows. The forced close is a distribution shift; the `forced_close` flag lets the report say so. `configs/probes.yaml` lists suggested budgets (256, 512, 1024, 2048).

## Known gaps

- `thinking_tokens`/`answer_tokens` split the generated count by re-tokenizing the answer text, so they can be off by a token or two. They are exact only for forced rows.
- Images go in at native resolution (no `max_pixels`). MiMo (28 px/token) and Qwen3-VL (32 px/token) therefore get different visual-token counts. `mm_processor_kwargs` can be set per model in `models.yaml`.
- Data quirks: `validation/mixed` has two PNGs listed twice with different object lists (entries 184/1170 and 256/1171), and the drawn boxes can match only one of each pair. The key includes `entry_idx`, so both are run. The HF `train.zip` unpacks to `train/images/` while the JSONs say `train/image/`; `data.image_path` falls back to the plural folder.
- No prefix placement after `</think>` (assistant turn), and no student forcing.
- `--limit` only takes the first N items per subset; there is no random or stratified subset.
