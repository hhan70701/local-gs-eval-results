"""Finish source pipeline with independent per-shot evaluation in three workers."""
import concurrent.futures
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path('/home/han/linux-han/local-gs-eval')
os.chdir(ROOT)
PYTHON = '/home/han/anaconda3/envs/gspl/bin/python'
CONFIG = 'configs/dataset6_lean.yaml'
cfg = yaml.safe_load((ROOT / CONFIG).read_text())
SHOTS = cfg['dataset6']['hosts']['linux-3090']
WORK = ROOT / 'work/dataset6'
BASE = [PYTHON, 'scripts/run_scenes.py', '--config', CONFIG]
ENV = os.environ.copy()
ENV.update(HF_HUB_OFFLINE='1', PYTHONUNBUFFERED='1', OMP_NUM_THREADS='4', OPENBLAS_NUM_THREADS='4')
ENV.pop('LGS_WORK_DIR', None)


def folder(shot):
    return WORK / shot.replace('/', '_')


def complete(shot):
    p = folder(shot) / 'eval/validation.json'
    if not p.exists():
        return False
    return json.loads(p.read_text())['status'] == 'PASS'


def run(shot, steps, log):
    cmd = BASE + ['--shots', shot, '--steps'] + steps
    path = folder(shot) / 'logs' / log
    path.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    with path.open('w') as out:
        rc = subprocess.run(cmd, cwd=ROOT, env=ENV, stdout=out, stderr=subprocess.STDOUT).returncode
    if rc:
        raise RuntimeError(f'{shot} {steps}: exit {rc}, see {path}')
    print(json.dumps(dict(shot=shot, steps=steps, seconds=round(time.time()-t0, 2)), ensure_ascii=False), flush=True)


def evaluate(shot):
    p = folder(shot) / 'timing.json'
    previous = json.loads(p.read_text()) if p.exists() else {}
    run(shot, ['evaluate', 'validate'], 'batch_evaluate.log')
    current = json.loads(p.read_text())
    previous.update(current)
    p.write_text(json.dumps(previous, indent=1) + '\n')
    if not complete(shot):
        raise RuntimeError(f'{shot}: validation missing or failed')


def main():
    completed = [s for s in SHOTS if complete(s)]
    pending = [s for s in SHOTS if not complete(s)]
    print(json.dumps(dict(stage='start', all=len(SHOTS), completed=completed, pending=len(pending)), ensure_ascii=False), flush=True)
    for i, shot in enumerate(pending, 1):
        run(shot, ['prepare', 'tokens', 'anysplat', 'pixgs', 'flow'], 'batch_generate.log')
        print(json.dumps(dict(stage='generate', done=i, total=len(pending))), flush=True)
    print(json.dumps(dict(stage='evaluation', workers=3, shots=len(pending))), flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(evaluate, shot): shot for shot in pending}
        for future in concurrent.futures.as_completed(futures):
            future.result()
    with (WORK / 'batch_summary.log').open('w') as out:
        rc = subprocess.run(BASE + ['--host', 'linux-3090', '--summary-only'],
                            cwd=ROOT, env=ENV, stdout=out, stderr=subprocess.STDOUT).returncode
    if rc:
        raise RuntimeError('final summary failed')
    assert all(complete(s) for s in SHOTS)
    print(json.dumps(dict(stage='complete', validated=len(SHOTS))), flush=True)


if __name__ == '__main__':
    main()
