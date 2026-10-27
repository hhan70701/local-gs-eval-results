"""Run round16a render sequentially, then evaluate shots in three workers."""
import concurrent.futures
import csv
import json
import os
import subprocess
import time
from pathlib import Path

import yaml

ROOT = Path('/home/han/linux-han/local-gs-eval')
os.chdir(ROOT)
PYTHON = '/home/han/anaconda3/envs/gspl/bin/python'
CONFIG = 'configs/dataset6_lean.yaml'
SHOTS = yaml.safe_load((ROOT / CONFIG).read_text())['dataset6']['hosts']['linux-3090']
WORK = ROOT / 'work/dataset6'
BASE = [PYTHON, 'scripts/run_scenes.py', '--config', CONFIG]
ENV = os.environ.copy()
ENV.update(HF_HUB_OFFLINE='1', PYTHONUNBUFFERED='1', OMP_NUM_THREADS='4', OPENBLAS_NUM_THREADS='4')
ENV.pop('LGS_WORK_DIR', None)
RUNS = ('p3h_fsl', 'p3h_fsl_g', 'p3h_fss', 'p3h_fss_g', 'p3h_flw',
        'pix2_fsl', 'pix2_fsl_g', 'pix2_fss', 'pix2_fss_g', 'pix2_flw')


def folder(shot):
    return WORK / shot.replace('/', '_')


def generated(shot):
    root = folder(shot) / 'gs/in035'
    return all((root / f'gs_tokcnw_cnn_{run}448_{run.split("_")[0]}_al_local/meta.json').exists()
               for run in RUNS)


def complete(shot):
    root = folder(shot) / 'eval'
    try:
        val = json.loads((root / 'validation.json').read_text())
        with (root / 'metrics.csv').open(newline='') as stream:
            methods = {row['method'] for row in csv.DictReader(stream)}
        return val['status'] == 'PASS' and val['methods'] >= 109 and any('pix2_fsl' in m for m in methods)
    except (OSError, ValueError, KeyError):
        return False


def run(shot, steps, log):
    path = folder(shot) / 'logs' / log
    path.parent.mkdir(parents=True, exist_ok=True)
    start = time.time()
    with path.open('w') as out:
        rc = subprocess.run(BASE + ['--shots', shot, '--steps'] + steps,
                            cwd=ROOT, env=ENV, stdout=out, stderr=subprocess.STDOUT).returncode
    if rc:
        raise RuntimeError(f'{shot} {steps}: exit {rc}; inspect {path}')
    print(json.dumps({'shot': shot, 'steps': steps, 'seconds': round(time.time()-start, 2)}), flush=True)


def evaluate(shot):
    path = folder(shot) / 'timing.json'
    earlier = json.loads(path.read_text()) if path.exists() else {}
    run(shot, ['evaluate', 'validate'], 'round16a_evaluate.log')
    current = json.loads(path.read_text())
    earlier.update(current)
    path.write_text(json.dumps(earlier, indent=1) + '\n')
    if not complete(shot):
        raise RuntimeError(f'{shot}: round16a validation missing or failed')


def main():
    pending = [shot for shot in SHOTS if not complete(shot)]
    print(json.dumps({'stage': 'start', 'all': len(SHOTS), 'complete': len(SHOTS)-len(pending),
                      'pending': len(pending)}), flush=True)
    for i, shot in enumerate(pending, 1):
        if not generated(shot):
            run(shot, ['pixgs'], 'round16a_generate.log')
        print(json.dumps({'stage': 'generate', 'done': i, 'total': len(pending)}), flush=True)
    print(json.dumps({'stage': 'evaluate', 'workers': 3, 'shots': len(pending)}), flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(evaluate, shot): shot for shot in pending}
        for future in concurrent.futures.as_completed(futures):
            future.result()
    with (WORK / 'round16a_summary.log').open('w') as out:
        rc = subprocess.run(BASE + ['--host', 'linux-3090', '--summary-only'],
                            cwd=ROOT, env=ENV, stdout=out, stderr=subprocess.STDOUT).returncode
    if rc:
        raise RuntimeError('final summary failed')
    assert all(complete(shot) for shot in SHOTS)
    print(json.dumps({'stage': 'complete', 'validated': len(SHOTS)}), flush=True)


if __name__ == '__main__':
    main()
