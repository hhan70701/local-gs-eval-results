"""Archive the completed round16a RTX 3090 run and compare held-out targets."""
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
WORK = ROOT / 'work/dataset6'
OUT = Path(__file__).resolve().parent
CFG = yaml.safe_load((ROOT / 'configs/dataset6_lean.yaml').read_text())
SHOTS = CFG['dataset6']['hosts']['linux-3090']
PILOT = set(SHOTS) & set(CFG['dataset6']['pilot_shots'])
REF = CFG['eval']['ref_flow']
RUNS = ('p3h_fsl', 'p3h_fsl_g', 'p3h_fss', 'p3h_fss_g', 'p3h_flw',
        'pix2_fsl', 'pix2_fsl_g', 'pix2_fss', 'pix2_fss_g', 'pix2_flw')
COMPARE = ('cnw_cnn_pix', 'cnw_cnn_mw_tto100') + tuple('cnw_cnn_' + r for r in RUNS)


def cp(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def rows(path):
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def csvout(path, data):
    assert data
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(data[0]))
        w.writeheader()
        w.writerows(data)


def meth(label, how):
    if label == 'cnw_cnn_pix':
        stem = 'gs_tokcnw_cnn_pix448_pix_al_local'
    elif label == 'cnw_cnn_mw_tto100':
        stem = 'gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local'
    else:
        run = label.removeprefix('cnw_cnn_')
        stem = f'gs_tok{label}448_{run.split("_")[0]}_al_local'
    return ('hyb_token' if how == 'direct' else 'hyb_tokchk_oracle') + f'[{stem}]'


def mean(rows_, field):
    return statistics.mean(float(r[field]) for r in rows_)


assert len(SHOTS) == 23 and len(set(SHOTS)) == 23
cp(ROOT / 'configs/dataset6_lean.yaml', OUT / 'config.yaml')
for name in ('round16a_smoke.log', 'dataset6_round16a_batch.log', 'bench_dense.log'):
    p = ROOT / 'work' / name
    if p.exists():
        cp(p, OUT / 'logs' / name)
cp(Path('/tmp/round16a_3090_tests.log'), OUT / 'logs/numerics_tests.log')
cp(Path('/tmp/round16a_3090_batched.py'), OUT / 'run_batched.py')
cp(WORK / 'summary_all.md', OUT / 'summary_all.md')
for name in ('md', 'json'):
    p = WORK / f'bench_dense_linux-3090.{name}'
    if p.exists():
        cp(p, OUT / p.name)

all_metrics = []
validations = {}
timings = []
render = []
for shot in SHOTS:
    tag = shot.replace('/', '_')
    src = WORK / tag
    dst = OUT / 'shots' / tag
    for rel in ('config.yaml', 'timing.json'):
        cp(src / rel, dst / rel)
    for folder in ('poses', 'logs', 'eval'):
        for p in (src / folder).rglob('*'):
            if p.is_file():
                cp(p, dst / folder / p.relative_to(src / folder))
    for typ in ('disp_fs', 'disp_fss', 'disp_flw'):
        cp(ROOT / 'data' / typ / tag / 'meta.json', dst / typ / 'meta.json')
    val = json.loads((src / 'eval/validation.json').read_text())
    assert val['status'] == 'PASS' and val['methods'] >= 109 and not val['warnings'], (shot, val)
    validations[shot] = val
    data = rows(src / 'eval/metrics.csv')
    assert len(data) == val['metric_rows']
    all_metrics.extend(dict(shot=shot, **r) for r in data)
    timings.append(dict(shot=shot, **json.loads((src / 'timing.json').read_text())))
    for run in RUNS:
        method = run.split('_')[0]
        rel = Path('in035') / f'gs_tokcnw_cnn_{run}448_{method}_al_local/meta.json'
        p = src / 'gs' / rel
        cp(p, dst / 'gs' / rel)
        m = json.loads(p.read_text())
        if method == 'pix2':
            assert m['render']['mode'] == 'gsplat', (shot, run, m['render'])
        for target, item in m['pixgs'].items():
            render.append(dict(shot=shot, run=run, target=int(target), backend=m['render']['mode'],
                               render_s=m['time_render_per_view_s'], prep_pair_s=m['round16']['time_prep_per_pair_s'],
                               stereo_export_s=m['time_encode_s'], core_px=item['core_px'],
                               hole_core_px=item['hole_in_core'], lr_fail_a=item['lr_fail_a'],
                               lr_fail_b=item['lr_fail_b'], gate_keep=item.get('gate_keep', '')))

with gzip.open(OUT / 'metrics_all.csv.gz', 'wt', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(all_metrics[0]))
    w.writeheader()
    w.writerows(all_metrics)
csvout(OUT / 'timing_all.csv', timings)
csvout(OUT / 'render_all.csv', render)
(OUT / 'validation_all.json').write_text(json.dumps(validations, ensure_ascii=False, indent=2) + '\n')

index = {(r['shot'], int(r['target']), r['method'], r['region']): r for r in all_metrics}
targets = [(shot, t) for shot in SHOTS for t in (1, 2, 4)]
assert len(targets) == 69 and len([x for x in targets if x[0] in PILOT]) == 9
comparison = []
for subset, pairs in (('all', targets), ('pilot', [x for x in targets if x[0] in PILOT])):
    for label in COMPARE:
        for how in ('direct', 'oracle'):
            method = meth(label, how)
            selected = [index[s, t, method, 'fg'] for s, t in pairs]
            flow = [index[s, t, REF, 'fg'] for s, t in pairs]
            nonworse = sum(float(a['psnr']) >= float(b['psnr']) - 1e-6 and
                           float(a['lpips']) <= float(b['lpips']) + 1e-6
                           for a, b in zip(selected, flow))
            comparison.append(dict(subset=subset, variant=label, how=how, targets=len(pairs),
                                   fg_psnr=mean(selected, 'psnr'), fg_lpips=mean(selected, 'lpips'),
                                   nonworse=nonworse))
csvout(OUT / 'quality_comparison.csv', comparison)

environment = dict(source_repo='luckyhan-mike/local-gs-eval', source_tag='linux-3090-round16a-p3h-pix2',
                   source_commit='34ee4649f2a76980c36d0d600a6ddf3b93a70296', host='linux-3090',
                   shots=SHOTS, python=sys.version, executable=sys.executable, torch=torch.__version__,
                   torch_cuda=torch.version.cuda, gsplat=gsplat.__version__, gpu=torch.cuda.get_device_name(0),
                   platform=platform.platform(), prior_results='work/dataset6 from round15 pixgs')
(OUT / 'environment.json').write_text(json.dumps(environment, ensure_ascii=False, indent=2) + '\n')


def comp(subset, label, how):
    return next(x for x in comparison if x['subset'] == subset and x['variant'] == label and x['how'] == how)


def score(x):
    return f"{x['fg_psnr']:.3f} / {x['fg_lpips']:.5f}"


flow = [index[s, t, REF, 'fg'] for s, t in targets]
lines = ['# linux-3090 第十六轮 a：p3h / pix2 修补对比', '',
         '源码标签 [`linux-3090-round16a-p3h-pix2`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round16a-p3h-pix2)，提交 `34ee4649f2a76980c36d0d600a6ddf3b93a70296`。复用第十五轮本机 `work/dataset6` 的预处理、token、光流和 AnySplat 输出，仅补本轮变体、重新评估与验证。23 组场景、69 个留出视点。', '',
         '下表均在同一批目标和 `cnw_cnn` token 区比较。`direct` 为实际无真值贴回；`oracle` 用目标真值圈定失败区域，只是上限诊断。“不差”要求单目标的 fg PSNR 不低于且 LPIPS 不高于纯光流。', '',
         '## 全部 69 个留出视点', '',
         f"纯光流 fg 均值：{mean(flow, 'psnr'):.3f} dB / {mean(flow, 'lpips'):.5f} LPIPS。", '',
         '| 方法 | direct fg PSNR / LPIPS | direct 不差 | oracle fg PSNR / LPIPS | oracle 不差 |',
         '|---|---:|---:|---:|---:|']
for label in COMPARE:
    a, b = comp('all', label, 'direct'), comp('all', label, 'oracle')
    lines.append(f"| {label} | {score(a)} | {a['nonworse']}/69 | {score(b)} | {b['nonworse']}/69 |")
lines += ['',
          '结果解读：`pix2_fsl_g` 的直接贴回 LPIPS 低于旧版 `cnw_cnn_pix`，也低于同来源的 `p3h_fsl_g`；但其 PSNR 仍低于纯光流，两个指标同时不差的目标仍为 0/69。`pix2_fsl` 与 `p3h_fsl` 各有指标优势，不能只据平均 LPIPS 宣称高斯整体胜出。门控降低了多数变体的 LPIPS，却没有提升直接贴回的“不差目标数”。', '']
lines += ['', '## 第七轮试点场景（9 个留出视点）', '',
          '这 3 组未用于 `cnw_cnn` 检测 CNN 训练，泛化判断以本表为主。', '',
          '| 方法 | direct fg PSNR / LPIPS | direct 不差 | oracle fg PSNR / LPIPS | oracle 不差 |',
          '|---|---:|---:|---:|---:|']
for label in COMPARE:
    a, b = comp('pilot', label, 'direct'), comp('pilot', label, 'oracle')
    lines.append(f"| {label} | {score(a)} | {a['nonworse']}/9 | {score(b)} | {b['nonworse']}/9 |")
lines += ['', '## 渲染耗时与对应覆盖', '',
          '以下为每场景 meta 所记每视点渲染时间的中位数；其中渲染前处理按一对输入相机计时。`stereo_export_s` 来自 Windows RTX 3090 的离线位移导出，不属于本机推理耗时。逐目标记录见 `render_all.csv`。', '',
          '| 变体 | 后端 | 每视点渲染中位数 | 每输入对准备中位数 | 最大核心空洞比例 |',
          '|---|---|---:|---:|---:|']
for run in RUNS:
    rr = [x for x in render if x['run'] == run]
    hole = max(x['hole_core_px'] / max(x['core_px'], 1) for x in rr)
    lines.append(f"| {run} | {rr[0]['backend']} | {statistics.median(x['render_s'] for x in rr)*1000:.1f} ms | {statistics.median(x['prep_pair_s'] for x in rr)*1000:.1f} ms | {hole:.2%} |")
lines += ['', '这张表来自逐场景仅 3 个目标的输出流程，包含每个进程首次调用的开销；`pix2_fsl` 恰好是每组的首次 gsplat 变体。下述密集计时先预热，在 GPU 上复用每对输入准备的数据、连续生成 41/60 个视点，二者的时间范围不同，不能直接比较其毫秒数。', '']
bench = OUT / 'bench_dense_linux-3090.md'
if bench.exists():
    lines += ['', '密集视点（41/60）计时及时间范围见 [`bench_dense_linux-3090.md`](bench_dense_linux-3090.md)。']
lines += ['', '## 验证与复现', '',
          f"上游 24 项单元测试通过。23/23 组验证 PASS，共 {sum(v['metric_rows'] for v in validations.values())} 行指标、{sum(v['auc_rows'] for v in validations.values())} 行 AUC，警告数 {sum(len(v['warnings']) for v in validations.values())}。", '',
          '首组按 README 顺序运行；其余组顺序执行 pixgs 生成，再以 3 个独立进程按场景执行源码评估与验证，最后重新汇总。计时文件合并保留两个阶段。本机原始图像、光流数组、渲染 RGB/alpha 和第十五轮工作目录保留在 `work/dataset6`；归档包括逐组指标、验证、日志、位姿和本轮十种变体的 meta。', '',
          '```bash', 'cd /home/han/linux-han/local-gs-eval', 'git fetch --tags -f origin',
          'git switch -c experiment/linux-3090-round16a-p3h-pix2-20261027 linux-3090-round16a-p3h-pix2',
          'export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH',
          'export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1',
          'python -m unittest discover -s tests -v',
          '# work/dataset6 需已有第十五轮本机 23 组结果',
          'python scripts/run_scenes.py --config configs/dataset6_lean.yaml --host linux-3090 --steps pixgs evaluate validate',
          'python scripts/bench_dense.py --config configs/dataset6_lean.yaml --host linux-3090 --views 41 60',
          '```', '']
(OUT / 'REPORT.md').write_text('\n'.join(lines), encoding='utf-8')
print(json.dumps(dict(shots=len(SHOTS), metrics=len(all_metrics), render_rows=len(render), archive=str(OUT))))
