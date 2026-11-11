# CSE 595 ROPE environment. Usage: source <code folder>/env.sh
# Every user-specific setting is one of the variables below. Export any of them before sourcing
# to change them; the ones left unset get the defaults shown.
#   CSE595_CODE     this code folder                    (default: the folder of this file)
#   CSE595_ROOT     folder holding venv, models, data, hf  (default: $HOME/cse595)
#   CSE595_VENV     Python venv                         (default: $CSE595_ROOT/venv)
#   MODELS_DIR      model folders                       (default: $CSE595_ROOT/models)
#   ROPE_DIR        ROPE data, with train/ validation/  (default: $CSE595_ROOT/data/ROPE)
#   HF_HOME         Hugging Face cache                  (default: $CSE595_ROOT/hf)
#   CSE595_RUNS     run outputs (JSONL)                 (default: <parent of CSE595_CODE>/runs)
#   CSE595_LOGS     Slurm logs                          (default: $CSE595_RUNS/logs)
#   CSE595_ACCOUNT  Slurm account for sbatch -A         (default: cse595f26_class)
export CSE595_CODE=${CSE595_CODE:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}
export CSE595_ROOT=${CSE595_ROOT:-$HOME/cse595}
export CSE595_VENV=${CSE595_VENV:-$CSE595_ROOT/venv}
export MODELS_DIR=${MODELS_DIR:-$CSE595_ROOT/models}
export ROPE_DIR=${ROPE_DIR:-$CSE595_ROOT/data/ROPE}
export HF_HOME=${HF_HOME:-$CSE595_ROOT/hf}
export CSE595_RUNS=${CSE595_RUNS:-$(dirname "$CSE595_CODE")/runs}
export CSE595_LOGS=${CSE595_LOGS:-$CSE595_RUNS/logs}
export CSE595_ACCOUNT=${CSE595_ACCOUNT:-cse595f26_class}
export HF_HUB_ENABLE_HF_TRANSFER=0

# Outbound proxy (compute nodes need it)
export http_proxy=http://proxy1.arc-ts.umich.edu:3128/
export https_proxy=http://proxy1.arc-ts.umich.edu:3128/
export HTTP_PROXY=$http_proxy
export HTTPS_PROXY=$https_proxy
export no_proxy=localhost,127.0.0.1,.localdomain,.umich.edu
export NO_PROXY=$no_proxy

if ! command -v module >/dev/null 2>&1 && [ -f /etc/profile.d/lmod.sh ]; then
  source /etc/profile.d/lmod.sh
fi
module load python/3.11.5
source "$CSE595_VENV/bin/activate"
