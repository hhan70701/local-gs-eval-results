#!/usr/bin/env bash
set -euo pipefail
cd /home/han/linux-han/local-gs-eval
export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH
export LGS_WORK_DIR=work/round7 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1 OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
trap 'run_exit=$?; printf "%s\n" "$run_exit" > work/round7/logs/runner_exit_code.txt' EXIT
echo tests > work/round7/logs/current_stage.txt
python -m unittest discover -s tests -v > work/round7/logs/numerics_tests.log 2>&1
echo detect_tokens > work/round7/logs/current_stage.txt
python scripts/detect_tokens.py --config configs/mofang_9cam.yaml > work/round7/logs/0_tokens.log 2>&1
echo run_anysplat > work/round7/logs/current_stage.txt
python scripts/run_anysplat.py --config configs/mofang_9cam.yaml > work/round7/logs/1_anysplat.log 2>&1
echo evaluate > work/round7/logs/current_stage.txt
python scripts/evaluate.py --config configs/mofang_9cam.yaml > work/round7/logs/3_evaluate.log 2>&1
echo validate > work/round7/logs/current_stage.txt
python scripts/validate_results.py configs/mofang_9cam.yaml > work/round7/logs/4_validation.log 2>&1
echo complete > work/round7/logs/current_stage.txt
