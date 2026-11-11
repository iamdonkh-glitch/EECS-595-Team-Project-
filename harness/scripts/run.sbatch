#!/bin/bash
#SBATCH -J rope-run
#SBATCH -p spgpu,gpu-rtx6000
#SBATCH --gres=gpu:1
#SBATCH -c 4
#SBATCH --mem=48G
#SBATCH -t 04:00:00
# One model, one split, one or more probes, greedy, --resume. Re-submitting the same command
# continues the same OUT file where the last job stopped.
# Give the account and log files on the command line; -p and -t above can be overridden there too:
#   sbatch -A "$CSE595_ACCOUNT" -o "$CSE595_LOGS/%x-%j.out" -e "$CSE595_LOGS/%x-%j.err" \
#     --export=ALL,MODEL=mimo-sft-2508,SPLIT=validation,OUT=$CSE595_RUNS/x.jsonl scripts/run.sbatch
# Env: MODEL, SPLIT (train|validation), OUT (JSONL) are required.
#      PROBES   runner probe names, space-separated (default "default single")
#      SUBSETS  space-separated subset names (default: the probe's subsets in configs/probes.yaml)
#      LIMIT    first N images per subset (default: all)
#      EXTRA    more rope_runner.run flags, e.g. "--tf-mode incremental", "--budget 512", "--no-think"
# The code folder is $CSE595_CODE, or the folder sbatch was called from.
set -euo pipefail
CODE=${CSE595_CODE:-${SLURM_SUBMIT_DIR:-$PWD}}
if [ ! -f "$CODE/env.sh" ]; then
  echo "[run] no env.sh in $CODE: export CSE595_CODE or call sbatch from the code folder" >&2; exit 1
fi
source "$CODE/env.sh"
MODEL=${MODEL:?set MODEL}
SPLIT=${SPLIT:?set SPLIT}
OUT=${OUT:?set OUT}
PROBES=${PROBES:-default single}
SUBSETS=${SUBSETS:-}
LIMIT=${LIMIT:-}
EXTRA=${EXTRA:-}
ARGS=()
if [ -n "$SUBSETS" ]; then ARGS+=(--subset $SUBSETS); fi
if [ -n "$LIMIT" ]; then ARGS+=(--limit "$LIMIT"); fi
# temp files on node-local /tmp
export TMPDIR=/tmp/${USER}/rope_${SLURM_JOB_ID:-local}
mkdir -p "$TMPDIR"
trap 'rm -rf "$TMPDIR"' EXIT
echo "[run] MODEL=$MODEL SPLIT=$SPLIT PROBES=$PROBES SUBSETS=${SUBSETS:-probes.yaml} LIMIT=${LIMIT:-all} EXTRA=$EXTRA OUT=$OUT"
echo "[run] code=$CODE host=$(hostname) account=${SLURM_JOB_ACCOUNT:-?} partition=${SLURM_JOB_PARTITION:-?} start=$(date -Is)"
mkdir -p "$(dirname "$OUT")"
cd "$CODE"
nvidia-smi || true
# vLLM 0.11 parses CUDA_VISIBLE_DEVICES as integers; a MIG slice comes as a UUID and is index 0.
if [[ "${CUDA_VISIBLE_DEVICES:-}" == MIG-* ]]; then export CUDA_VISIBLE_DEVICES=0; fi
# Size vLLM to the card: <46000 MiB (A40 reports 45490) 0.85 / 12288;
# 46000-80000 MiB 0.90 / 16384; >=80000 MiB (RTX PRO 6000) 0.90 / 32768.
GPU_MIB=$(python -c "import torch; print(torch.cuda.get_device_properties(0).total_memory >> 20)")
if [ "${GPU_MIB:-0}" -lt 46000 ]; then
  export ROPE_GPU_MEM_UTIL=${ROPE_GPU_MEM_UTIL:-0.85}; export ROPE_MAX_MODEL_LEN=${ROPE_MAX_MODEL_LEN:-12288}
elif [ "${GPU_MIB:-0}" -lt 80000 ]; then
  export ROPE_GPU_MEM_UTIL=${ROPE_GPU_MEM_UTIL:-0.90}; export ROPE_MAX_MODEL_LEN=${ROPE_MAX_MODEL_LEN:-16384}
else
  export ROPE_GPU_MEM_UTIL=${ROPE_GPU_MEM_UTIL:-0.90}; export ROPE_MAX_MODEL_LEN=${ROPE_MAX_MODEL_LEN:-32768}
fi
echo "[run] gpu=$(python -c "import torch; print(torch.cuda.get_device_name(0))") mem_mib=$GPU_MIB util=$ROPE_GPU_MEM_UTIL max_model_len=$ROPE_MAX_MODEL_LEN"
for PROBE in $PROBES; do
  echo "[run] probe=$PROBE start=$(date -Is)"
  # shellcheck disable=SC2086
  python -m rope_runner.run --model "$MODEL" --probe "$PROBE" --split "$SPLIT" "${ARGS[@]}" \
    --greedy $EXTRA --out "$OUT" --resume
  echo "[run] probe=$PROBE end=$(date -Is)"
done
python -m rope_runner.analyze "$OUT" || true
