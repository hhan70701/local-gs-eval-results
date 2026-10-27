"""Archive and summarize a completed round-17 linux-3090 experiment."""
import csv
import gzip
import json
import platform
import shutil
import statistics
import sys
from pathlib import Path

import gsplat
import torch
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
CFG = yaml.safe_load((ROOT / 'configs/dataset6_lean.yaml').read_text())
WORK = ROOT / CFG['dataset6']['work_root']
SHOTS = CFG['dataset6']['hosts']['linux-3090']
PILOT = set(SHOTS) & set(CFG['dataset6']['pilot_shots'])
RUNS = ('pix2_fsl', 'pix2_fsl_g', 'pix3n_fsl', 'pix3n_fsl_g', 'pix3_fsl')
METHODS = ('cnw_cnn_mw_tto100',) + tuple('cnw_cnn_' + x for x in RUNS)
REGIONS = ('fg', 'oracle_fail', 'fail_vis2', 'fail_vis1')
SOURCE_COMMIT = '3585842a50d8e26ffa87033dda9f0cfb28d21626'


def cp(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def read_csv(path):
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def save_csv(path, records):
    assert records, path
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def stem(label):
    if label == 'cnw_cnn_mw_tto100':
        return 'gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local'
    run = label.removeprefix('cnw_cnn_')
    return f'gs_tok{label}448_{run.split("_")[0].removesuffix("n") if run.startswith("pix3n") else run.split("_")[0]}_al_local'


def method(label, kind):
    prefix = 'hyb_token' if kind == 'direct' else 'hyb_tokchk_oracle'
    return f'{prefix}[{stem(label)}]'


def avg(records, key):
    return statistics.mean(float(r[key]) for r in records)


assert len(SHOTS) == 23 and len(set(SHOTS)) == 23
for src, rel in ((ROOT / 'configs/dataset6_lean.yaml', 'config.yaml'),
                 (Path('/tmp/round17_3090_tests.log'), 'logs/numerics_tests.log'),
                 (ROOT / 'work/dataset6_r17.log', 'logs/dataset6_r17.log'),
                 (ROOT / 'work/bench_dense_r17.log', 'logs/bench_dense_r17.log'),
                 (WORK / 'summary_all.md', 'summary_all.md'),
                 (WORK / 'bench_dense_linux-3090.md', 'bench_dense_linux-3090.md'),
                 (WORK / 'bench_dense_linux-3090.json', 'bench_dense_linux-3090.json')):
    cp(src, OUT / rel)

metrics, validations, timings, render = [], {}, [], []
for shot in SHOTS:
    tag = shot.replace('/', '_')
    src, dst = WORK / tag, OUT / 'shots' / tag
    for rel in ('config.yaml', 'timing.json', 'poses/in035.json'):
        cp(src / rel, dst / rel)
    for folder in ('logs', 'eval'):
        for p in (src / folder).rglob('*'):
            if p.is_file():
                cp(p, dst / p.relative_to(src))
    v = json.loads((src / 'eval/validation.json').read_text())
    assert v['status'] == 'PASS' and not v['warnings'], (shot, v)
    validations[shot] = v
    data = read_csv(src / 'eval/metrics.csv')
    assert len(data) == v['metric_rows'], shot
    metrics += [dict(shot=shot, **row) for row in data]
    timings.append(dict(shot=shot, **json.loads((src / 'timing.json').read_text())))
    for run in RUNS:
        label = 'cnw_cnn_' + run
        rel = Path('in035') / stem(label) / 'meta.json'
        p = src / 'gs' / rel
        cp(p, dst / 'gs' / rel)
        m = json.loads(p.read_text())
        assert m['render']['mode'] == 'gsplat', (shot, run, m['render']['mode'])
        pairs = m['round16'].get('pairs', {})
        for target, item in m['pixgs'].items():
            pair = pairs.get(item['pair'], {})
            render.append(dict(shot=shot, run=run, target=target, backend=m['render']['mode'],
                               render_s=m['time_render_per_view_s'],
                               prep_pair_s=m['round16']['time_prep_per_pair_s'],
                               pair_build_s=pair.get('build_s', ''),
                               pair_opt_s=pair.get('opt', {}).get('time_s', ''),
                               gaussians=item['gaussians'], core_px=item['core_px'],
                               hole_in_core=item.get('hole_in_core', ''),
                               vis_both_share_in_core=item.get('vis_both_share_in_core', ''),
                               gate_keep=item.get('gate_keep', '')))

with gzip.open(OUT / 'metrics_all.csv.gz', 'wt', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(metrics[0]))
    writer.writeheader()
    writer.writerows(metrics)
save_csv(OUT / 'timing_all.csv', timings)
save_csv(OUT / 'render_all.csv', render)
(OUT / 'validation_all.json').write_text(json.dumps(validations, ensure_ascii=False, indent=2) + '\n')

index = {(r['shot'], int(r['target']), r['method'], r['region']): r for r in metrics}
targets = [(s, t) for s in SHOTS for t in (1, 2, 4)]
assert len(targets) == 69 and len([x for x in targets if x[0] in PILOT]) == 9
comparison = []
for subset, pairs in (('all', targets), ('pilot', [x for x in targets if x[0] in PILOT])):
    for region in REGIONS:
        for label in METHODS:
            for kind in ('direct', 'oracle'):
                selected, flow = [], []
                for shot, target in pairs:
                    a = index.get((shot, target, method(label, kind), region))
                    b = index.get((shot, target, CFG['eval']['ref_flow'], region))
                    if a is not None and b is not None:
                        selected.append(a)
                        flow.append(b)
                assert selected or region in ('fail_vis2', 'fail_vis1'), (subset, region, label, kind)
                comparison.append(dict(subset=subset, region=region, variant=label, kind=kind,
                                       targets=len(selected), psnr=avg(selected, 'psnr') if selected else '',
                                       lpips=avg(selected, 'lpips') if selected else '',
                                       flow_psnr=avg(flow, 'psnr') if flow else '',
                                       flow_lpips=avg(flow, 'lpips') if flow else '',
                                       nonworse=sum(float(a['psnr']) >= float(b['psnr']) - 1e-6 and
                                                   float(a['lpips']) <= float(b['lpips']) + 1e-6
                                                   for a, b in zip(selected, flow))))
save_csv(OUT / 'quality_comparison.csv', comparison)

bench = json.loads((OUT / 'bench_dense_linux-3090.json').read_text())
assert bench['host'] == 'linux-3090' and bench['shots']
assert bench['backend_pix2'] == 'gsplat'
environment = dict(source_repo='luckyhan-mike/local-gs-eval', source_tag='linux-3090-round17-pix3',
                   source_commit=SOURCE_COMMIT, host='linux-3090', shots=SHOTS,
                   python=sys.version, executable=sys.executable, torch=torch.__version__,
                   torch_cuda=torch.version.cuda, gsplat=gsplat.__version__,
                   gpu=torch.cuda.get_device_name(0), platform=platform.platform(),
                   reused_work='round16 work/dataset6 (token, flow, AnySplat, disparity)')
(OUT / 'environment.json').write_text(json.dumps(environment, ensure_ascii=False, indent=2) + '\n')


def find(subset, region, label, kind):
    return next(r for r in comparison if (r['subset'], r['region'], r['variant'], r['kind']) ==
                (subset, region, label, kind))


lines = ['# linux-3090 第十七轮 pix3 结果', '',
         f'源码标签 [`linux-3090-round17-pix3`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round17-pix3)，提交 `{SOURCE_COMMIT}`。',
         '复用本机第十六轮的 token、光流、AnySplat 和 FoundationStereo-L 位移；23 组场景、69 个留出视点。',
         'direct 是不使用目标真值的贴回；oracle 用真值圈定光流失败区，仅作上限诊断。所有均值按目标视点等权，区域为空的视点不计入该区域均值。', '']
for subset, pairs in (('all', targets), ('pilot', [x for x in targets if x[0] in PILOT])):
    lines += [f'## {"全部" if subset == "all" else "未参与 CNN 训练的试点"} {len(pairs)} 个留出视点', '']
    for region in REGIONS:
        lines += [f'### {region}', '', '| 变体 | direct PSNR / LPIPS | direct 不差 | oracle PSNR / LPIPS | oracle 不差 |',
                  '|---|---:|---:|---:|---:|']
        for label in METHODS:
            a, b = find(subset, region, label, 'direct'), find(subset, region, label, 'oracle')
            fmt = lambda x: f"{x['psnr']:.3f} / {x['lpips']:.5f}" if x['targets'] else '无有效区域'
            lines.append(f"| {label} | {fmt(a)} (n={a['targets']}) | {a['nonworse']}/{a['targets']} | "
                         f"{fmt(b)} (n={b['targets']}) | {b['nonworse']}/{b['targets']} |")
        lines.append('')
lines += ['## 耗时与验证', '',
          '逐场景 `render_all.csv` 的渲染耗时含每个进程初次调用；密集视点计时先预热，详见 [`bench_dense_linux-3090.md`](bench_dense_linux-3090.md)。两者时间范围不同。',
          '', '| 变体 | 每视点渲染中位数 | 每输入对准备中位数 |', '|---|---:|---:|']
for run in RUNS:
    rr = [r for r in render if r['run'] == run]
    assert len(rr) == 69
    lines.append(f"| {run} | {statistics.median(float(r['render_s']) for r in rr)*1000:.1f} ms | "
                 f"{statistics.median(float(r['prep_pair_s']) for r in rr)*1000:.1f} ms |")
lines += ['', f"23/23 组验证 PASS；{sum(v['metric_rows'] for v in validations.values())} 行指标，"
          f"{sum(v['auc_rows'] for v in validations.values())} 行 AUC，0 条警告；25 项单元测试通过。", '',
          '复现：在 `gspl` 环境与第十六轮同一工作目录中运行：', '', '```bash',
          'python -m unittest discover -s tests -v',
          'python scripts/run_scenes.py --config configs/dataset6_lean.yaml --host linux-3090 --steps pixgs evaluate validate',
          'python scripts/bench_dense.py --config configs/dataset6_lean.yaml --host linux-3090 --views 41 60',
          '```', '',
          '归档包含逐组评估（含拼图）、日志、位姿、五个 pixgs 变体 meta、批次日志和密集视点计时。原始图像、渲染图和大体积中间数组保留在本机工作目录。', '']
(OUT / 'REPORT.md').write_text('\n'.join(lines), encoding='utf-8')
print(json.dumps(dict(shots=len(SHOTS), metric_rows=len(metrics), render_rows=len(render),
                      bench_shots=len(bench['shots']), archive=str(OUT))))
