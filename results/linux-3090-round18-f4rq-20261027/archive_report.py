"""Archive the completed round-18 linux-3090 experiment and its measured comparisons."""
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

REPO = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
CFG = yaml.safe_load((REPO / 'configs/dataset6_lean.yaml').read_text())
WORK = REPO / CFG['dataset6']['work_root']
SHOTS = CFG['dataset6']['hosts']['linux-3090']
PILOT = set(SHOTS) & set(CFG['dataset6']['pilot_shots'])
LABELS = ('cnw_cnn_mw', 'cnw_cnn_pix3_fsl', 'f4rq_pix3_fsl',
          'f4rq_pix3bg_fsl', 'f4rq_pix3bg_fsl_g',
          'f4rq_pix3bg_fsl_s25', 'f4rq_pix3bg_fsl_s50')
NEW = tuple(x for x in LABELS if x.startswith('f4rq_'))
REGIONS = ('fg', 'oracle_fail', 'fail_vis2', 'fail_vis1')
SOURCE_COMMIT = '80a09871a3d7a6bd815e24ddffa0421e8ef7970b'


def cp(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def rows(path):
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def csvout(path, records):
    assert records, path
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)


def stem(label):
    if label == 'cnw_cnn_mw':
        return 'gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local'
    return f'gs_tok{label}448_pix3_al_local'


def method(label, how):
    prefix = 'hyb_token' if how == 'direct' else 'hyb_tokchk_oracle'
    return f'{prefix}[{stem(label)}]'


def avg(items, key):
    return statistics.mean(float(x[key]) for x in items)


assert len(SHOTS) == 6 and len(PILOT) == 3
for src, rel in ((REPO / 'configs/dataset6_lean.yaml', 'config.yaml'),
                 (Path('/tmp/round18_3090_tests.log'), 'logs/numerics_tests.log'),
                 (REPO / 'work/dataset6_r18.log', 'logs/dataset6_r18.log'),
                 (REPO / 'work/bench_dense_r18.log', 'logs/bench_dense_r18.log'),
                 (WORK / 'summary_all.md', 'summary_all.md'),
                 (WORK / 'bench_dense_linux-3090.md', 'bench_dense_linux-3090.md'),
                 (WORK / 'bench_dense_linux-3090.json', 'bench_dense_linux-3090.json')):
    cp(src, OUT / rel)

metrics, validations, timings, render = [], {}, [], []
for shot in SHOTS:
    tag = shot.replace('/', '_')
    src, dst = WORK / tag, OUT / 'shots' / tag
    for rel in ('config.yaml', 'timing.json', 'poses/in035.json',
                'prepare/prepare.json', 'tokens/tokens.json'):
        cp(src / rel, dst / rel)
    for folder in ('logs', 'eval'):
        for p in (src / folder).rglob('*'):
            if p.is_file():
                cp(p, dst / p.relative_to(src))
    val = json.loads((src / 'eval/validation.json').read_text())
    assert val['status'] == 'PASS' and not val['warnings'], (shot, val)
    validations[shot] = val
    data = rows(src / 'eval/metrics.csv')
    assert len(data) == val['metric_rows'], shot
    metrics.extend(dict(shot=shot, **r) for r in data)
    timings.append(dict(shot=shot, **json.loads((src / 'timing.json').read_text())))
    for label in LABELS:
        rel = Path('in035') / stem(label) / 'meta.json'
        p = src / 'gs' / rel
        cp(p, dst / 'gs' / rel)
        if label not in NEW:
            continue
        meta = json.loads(p.read_text())
        assert meta['render']['mode'] == 'gsplat', (shot, label)
        pairs = meta['round16']['pairs']
        for target, item in meta['pixgs'].items():
            pair = pairs[item['pair']]
            render.append(dict(shot=shot, label=label, target=target,
                               backend=meta['render']['mode'],
                               render_s=meta['time_render_per_view_s'],
                               prep_pair_s=meta['round16']['time_prep_per_pair_s'],
                               build_pair_s=pair['build_s'],
                               opt_full100_pair_s=pair['opt']['time_s'],
                               snapshot_steps=(25 if label.endswith('_s25') else
                                               50 if label.endswith('_s50') else 100),
                               gaussians=item['gaussians'],
                               core_px=item['core_px'],
                               gate_keep=item.get('gate_keep', ''),
                               bg_used=pair.get('bg_used', ''),
                               bg_replaced=pair.get('bg_replaced', '')))

with gzip.open(OUT / 'metrics_all.csv.gz', 'wt', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(metrics[0]))
    w.writeheader()
    w.writerows(metrics)
csvout(OUT / 'timing_all.csv', timings)
csvout(OUT / 'render_all.csv', render)
(OUT / 'validation_all.json').write_text(json.dumps(validations, ensure_ascii=False, indent=2) + '\n')

index = {(r['shot'], int(r['target']), r['method'], r['region']): r for r in metrics}
targets = [(s, t) for s in SHOTS for t in (1, 2, 4)]
assert len(targets) == 18
comparison = []
for subset, pairs in (('all', targets), ('pilot', [x for x in targets if x[0] in PILOT])):
    for region in REGIONS:
        for label in LABELS:
            for how in ('direct', 'oracle'):
                selected, flow = [], []
                for shot, target in pairs:
                    a = index.get((shot, target, method(label, how), region))
                    b = index.get((shot, target, CFG['eval']['ref_flow'], region))
                    if a is not None and b is not None:
                        selected.append(a)
                        flow.append(b)
                assert selected, (subset, region, label, how)
                comparison.append(dict(subset=subset, region=region, variant=label, how=how,
                                       targets=len(selected), psnr=avg(selected, 'psnr'),
                                       lpips=avg(selected, 'lpips'),
                                       flow_psnr=avg(flow, 'psnr'),
                                       flow_lpips=avg(flow, 'lpips'),
                                       nonworse=sum(float(a['psnr']) >= float(b['psnr']) - 1e-6 and
                                                   float(a['lpips']) <= float(b['lpips']) + 1e-6
                                                   for a, b in zip(selected, flow))))
csvout(OUT / 'quality_comparison.csv', comparison)

bench = json.loads((OUT / 'bench_dense_linux-3090.json').read_text())
assert bench['host'] == 'linux-3090' and bench['shots']
environment = dict(source_repo='luckyhan-mike/local-gs-eval', source_tag='linux-3090-round18-f4rq',
                   source_commit=SOURCE_COMMIT, host='linux-3090', shots=SHOTS,
                   python=sys.version, executable=sys.executable, torch=torch.__version__,
                   torch_cuda=torch.version.cuda, gsplat=gsplat.__version__,
                   gpu=torch.cuda.get_device_name(0), platform=platform.platform(),
                   reused_work='round17 work/dataset6 (aligned inputs, flow, baseline GS, disparity)')
(OUT / 'environment.json').write_text(json.dumps(environment, ensure_ascii=False, indent=2) + '\n')


def get(subset, region, label, how):
    return next(r for r in comparison if (r['subset'], r['region'], r['variant'], r['how']) ==
                (subset, region, label, how))


lines = ['# linux-3090 第十八轮：F4R-q、背景平面与 GPU 加速', '',
         f'源码标签 [`linux-3090-round18-f4rq`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round18-f4rq)，提交 `{SOURCE_COMMIT}`。',
         '本机 6 组场景、18 个留出视点；其中 3 组 / 9 个视点为未参与检测 CNN 训练的试点。',
         'direct 为不用目标真值的贴回；oracle 用真值圈定光流失败区，只作上限诊断。',
         '下表按视点等权平均，"不差"要求同一个视点的前景 PSNR 不低于且 LPIPS 不高于纯光流。', '']
lines += ['本机 6 组上，F4R-q 的 100 步 pix3 直接贴回前景为 26.34 dB / 0.0768 LPIPS，'
          '旧 Cn_wide token 的同方法为 26.66 dB / 0.0708；换 token 后两个平均指标都下降。'
          '加入背景平面后为 26.32 dB / 0.0775，单侧可见失败区均值几乎不变。'
          '门控把该变体 LPIPS 降至 0.0739，但 PSNR 同时降至 26.18 dB。'
          '这些只是本机 18 个目标视点的实测结果，不能外推为全部 46 组结论。', '',
          '`summary_all.md` 由上游复用的汇总函数生成，开头误写“第十七轮”；该文件中的 6 组和 18 个视点数据属于本轮。', '']
for subset, pairs in (('all', targets), ('pilot', [x for x in targets if x[0] in PILOT])):
    lines += [f'## {"全部" if subset == "all" else "未参与 CNN 训练的试点"} {len(pairs)} 个留出视点', '']
    for region in REGIONS:
        lines += [f'### {region}', '',
                  '| 变体 | direct PSNR / LPIPS | direct 不差 | oracle PSNR / LPIPS | oracle 不差 |',
                  '|---|---:|---:|---:|---:|']
        for label in LABELS:
            a, b = get(subset, region, label, 'direct'), get(subset, region, label, 'oracle')
            lines.append(f"| {label} | {a['psnr']:.3f} / {a['lpips']:.5f} (n={a['targets']}) | "
                         f"{a['nonworse']}/{a['targets']} | {b['psnr']:.3f} / {b['lpips']:.5f} "
                         f"(n={b['targets']}) | {b['nonworse']}/{b['targets']} |")
        lines.append('')
lines += ['## 速度与验证', '',
          '密集视点的 fp32 单视点与 fp16 四视点批量计时见 [`bench_dense_linux-3090.md`](bench_dense_linux-3090.md)；逐场景与逐目标构建、优化、渲染时间见 `render_all.csv`。',
          f"6/6 组验证 PASS，{sum(v['metric_rows'] for v in validations.values())} 行指标，"
          f"{sum(v['auc_rows'] for v in validations.values())} 行 AUC，0 条警告；26 项单元测试通过。", '',
          '复现（gspl 环境，沿用第十七轮工作目录）：', '', '```bash',
          'python -m unittest discover -s tests -v',
          'python scripts/run_scenes.py --config configs/dataset6_lean.yaml --host linux-3090 --steps tokens pixgs evaluate validate',
          'python scripts/bench_dense.py --config configs/dataset6_lean.yaml --host linux-3090 --views 30',
          '```', '',
          '归档含本轮 6 组的逐组评估、拼图、日志和新 GS 变体元数据。原始图像、渲染图、大体积中间数据留在本机工作目录。', '']
(OUT / 'REPORT.md').write_text('\n'.join(lines), encoding='utf-8')
print(json.dumps(dict(shots=len(SHOTS), metrics=len(metrics), render=len(render),
                      bench_shots=len(bench['shots']), archive=str(OUT))))
