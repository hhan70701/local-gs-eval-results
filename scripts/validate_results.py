"""Check experiment completeness, finite metrics, registration and image artifacts."""
import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lgs.common import load_cfg, load_json, imread_rgb, setup_cams


def main():
    cfg = load_cfg(sys.argv[1] if len(sys.argv) > 1 else 'configs/mofang_9cam.yaml')
    work = Path(cfg['work_dir'])
    metrics = list(csv.DictReader((work / 'eval/metrics.csv').open()))
    auc = list(csv.DictReader((work / 'eval/auc.csv').open()))
    targets_count = sum(len(setup_cams(cfg, s)[1]) for s in cfg['setups'])
    assert len(metrics) == targets_count * 22 * 5, len(metrics)
    assert len(auc) == targets_count * 5, len(auc)
    keys = {(r['setup'], r['target'], r['method'], r['region']) for r in metrics}
    assert len(keys) == len(metrics), 'Duplicate metric rows'
    for row in metrics:
        assert int(row['area_px']) > 0, row
        for col in ('psnr', 'ssim', 'lpips', 'area_frac_fg'):
            assert math.isfinite(float(row[col])), row
    for row in auc:
        assert 0 <= float(row['auc']) <= 1, row
    prepare = load_json(work / 'prepare/prepare.json')
    assert len(prepare) == cfg['num_cams']
    assert all(r['warp_psnr_db'] > 30 for r in prepare.values())
    counts = {'gs_renders': 0, 'flow_renders': 0, 'montages': 0}
    for setup in cfg['setups']:
        _, targets = setup_cams(cfg, setup)
        for variant in ('gs_center448', 'gs_center518', 'gs_fg448', 'gs_fg518'):
            folder = work / 'gs' / setup / variant
            meta = load_json(folder / 'meta.json')
            assert max(meta['ctx_rot_err_deg']) < 1, folder
            assert max(meta['ctx_center_err_rel_baseline']) < .05, folder
            for k in targets:
                rgb = imread_rgb(folder / f'cam{k}.png')
                assert rgb.shape == (1080, 1920, 3)
                counts['gs_renders'] += 1
        for scale in (1.0, 0.5):
            for mode in ('uniform', 'pose', 'oracle'):
                folder = work / 'flow' / setup / f'flow_s{scale}_{mode}'
                meta = load_json(folder / 'meta.json')
                assert set(meta) == {str(k) for k in targets}
                for k in targets:
                    assert imread_rgb(folder / f'cam{k}.png').shape == (1080, 1920, 3)
                    with np.load(folder / f'cam{k}_signals.npz') as sig:
                        for name in ('r_warp', 'r_col', 'g_disp', 'mask_ent', 'mask_grad', 'flow'):
                            assert np.isfinite(sig[name]).all(), (folder, k, name)
                    counts['flow_renders'] += 1
        for k in targets:
            imread_rgb(work / 'eval' / setup / f'cam{k}_montage.png')
            counts['montages'] += 1
    result = dict(status='PASS', metric_rows=len(metrics), auc_rows=len(auc), **counts)
    (work / 'eval/validation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
