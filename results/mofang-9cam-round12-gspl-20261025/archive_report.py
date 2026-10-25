"""Archive and summarize the measured round 12 run without changing its metrics."""
import csv
import hashlib
import json
import platform
import shutil
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lgs.common import load_cfg

WORK = ROOT / "work/round12"
OUT = ROOT / "results/mofang-9cam-round12-gspl-20261025"
OLD = ROOT / "results/mofang-9cam-round11-gspl-20261025"
CFG = load_cfg(str(ROOT / "configs/mofang_9cam_lean.yaml"))
REF = CFG["eval"]["ref_flow"]
STEPS = [0] + CFG["gs"]["tto"]["checkpoints"]
METHOD = lambda n: "hyb_token[gs_tokrife448_nat_dil_al" + (f"_tto{n}" if n else "") + "_local]"


def copy(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def avg(rows, key):
    return statistics.mean(float(r[key]) for r in rows)


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


OUT.mkdir(parents=True, exist_ok=True)
copy(ROOT / "configs/mofang_9cam_lean.yaml", OUT / "config.yaml")
for p in (WORK / "eval").rglob("*"):
    if p.is_file():
        copy(p, OUT / "eval" / p.relative_to(WORK / "eval"))
for folder in ("gs", "flow", "poses", "prepare", "tokens"):
    for p in (WORK / folder).rglob("*.json"):
        copy(p, OUT / folder / p.relative_to(WORK / folder))
for p in (WORK / "logs").glob("*"):
    if p.is_file():
        copy(p, OUT / "logs" / p.name)
copy(WORK / "1_anysplat.log", OUT / "logs/1_anysplat.log")

old_manifest = json.loads((OLD / "reused_files_manifest.json").read_text())
for r in old_manifest:
    p = WORK / r["path"]
    assert p.stat().st_size == r["size"] and sha256(p) == r["sha256"], r["path"]
copy(OLD / "reused_files_manifest.json", OUT / "reused_files_manifest.json")

import torch, gsplat
env = {
    "source_tag": "linux-3090-round12",
    "source_commit": "aed2679360ff1c73ccf5dfcdc115be11e2dbab6d",
    "work_dir": "work/round12",
    "python": sys.version,
    "executable": sys.executable,
    "torch": torch.__version__,
    "torch_cuda": torch.version.cuda,
    "gsplat": gsplat.__version__,
    "gpu": torch.cuda.get_device_name(0),
    "platform": platform.platform(),
    "reused_round7_file_count": len(old_manifest),
    "eval_parallel_by_setup": True,
}
(OUT / "environment.json").write_text(json.dumps(env, indent=2, ensure_ascii=False) + "\n")

timing, boxes, train = [], [], []
for setup in CFG["setups"]:
    m = json.loads((WORK / "gs" / setup / "gs_tokrife448_nat_dil_al_local/meta.json").read_text())
    t = m["tto"]
    cams = CFG["setups"][setup]["context"]
    b = t["log"][0]["box"]
    for cam, (x, y, w, h) in zip(cams, b["per_view"]):
        boxes.append(dict(setup=setup, camera=cam, x=x, y=y, w=w, h=h,
                          supervision_res=t["res"], area_frac=w*h/t["res"]**2))
    for e in t["log"]:
        for cam, psnr in zip(cams, e["ctx_psnr"]):
            train.append(dict(setup=setup, camera=cam, iteration=e["iter"],
                              input_crop_psnr=psnr, loss=e["loss"]))
        if "time_s" in e:
            timing.append(dict(setup=setup, iteration=e["iter"], cumulative_tto_s=e["time_s"],
                               step_ms=e["time_s"]*1000/e["iter"],
                               mean_input_psnr=statistics.mean(e["ctx_psnr"]),
                               mean_area_frac=b["area_frac"], max_box_w=b["w"],
                               max_box_h=b["h"], train_gaussians=t["train_gaussians"],
                               encode_s=m["time_encode_s"]))
write_csv(OUT / "eval/tto_checkpoint_timing.csv", timing)
write_csv(OUT / "eval/tto_supervision_boxes.csv", boxes)
write_csv(OUT / "eval/tto_training.csv", train)

merge_counts = {}
for name in ("metrics.csv", "auc.csv", "registration.csv", "risk_sweep.csv",
             "paste.csv", "tokchk.csv", "token_ringreg.csv"):
    combined = list(csv.reader((WORK / "eval" / name).open(newline="")))
    parts = [list(csv.reader((WORK / "eval_jobs" / setup / "eval" / name).open(newline="")))
             for setup in CFG["setups"]]
    assert all(p[0] == combined[0] for p in parts), name
    assert combined[1:] == sum((p[1:] for p in parts), []), name
    merge_counts[name] = len(combined)-1
(OUT / "eval/parallel_merge_validation.json").write_text(json.dumps(merge_counts, indent=2)+"\n")

new = read_csv(OUT / "eval/metrics.csv")
old = read_csv(OLD / "eval/metrics.csv")
validation = json.loads((OUT / "eval/validation.json").read_text())
assert validation["status"] == "PASS"
new_by = {(r["setup"], r["target"], r["method"], r["region"]): r for r in new}
old_by = {(r["setup"], r["target"], r["method"], r["region"]): r for r in old}
quality, per_view = [], []
for setup in CFG["setups"]:
    targets = sorted({r["target"] for r in new if r["setup"] == setup}, key=int)
    for step in STEPS:
        method = METHOD(step)
        count = 0
        for target in targets:
            f = new_by[setup, target, REF, "fg"]
            n = new_by[setup, target, method, "fg"]
            o = old_by[setup, target, method, "fg"]
            nonworse = float(n["psnr"]) >= float(f["psnr"])-1e-6 and float(n["lpips"]) <= float(f["lpips"])+1e-6
            count += nonworse
            per_view.append(dict(setup=setup, target=target, step=step,
                                 fg_psnr=n["psnr"], fg_lpips=n["lpips"],
                                 delta_flow_psnr=float(n["psnr"])-float(f["psnr"]),
                                 delta_flow_lpips=float(n["lpips"])-float(f["lpips"]),
                                 delta_round11_psnr=float(n["psnr"])-float(o["psnr"]),
                                 delta_round11_lpips=float(n["lpips"])-float(o["lpips"]),
                                 nonworse_flow=nonworse))
        row = dict(setup=setup, step=step, cumulative_tto_s=next((r["cumulative_tto_s"] for r in timing if r["setup"]==setup and r["iteration"]==step), 0),
                   fg_nonworse_count=count, targets=len(targets))
        for region in ("fg", "object", "rest"):
            for key in ("psnr", "lpips"):
                nn=[new_by[setup,t,method,region] for t in targets]
                oo=[old_by[setup,t,method,region] for t in targets]
                row[f"{region}_{key}"]=avg(nn,key)
                row[f"{region}_{key}_round11"]=avg(oo,key)
                row[f"{region}_{key}_delta_round11"]=avg(nn,key)-avg(oo,key)
        quality.append(row)
write_csv(OUT / "eval/tto_quality_comparison.csv", quality)
write_csv(OUT / "eval/tto_quality_per_view.csv", per_view)

def q(setup, step):
    return next(r for r in quality if r["setup"]==setup and r["step"]==step)

lines = [
    "# 第十二轮：3090 上精简流程与逐视图裁剪 TTO 实测", "",
    "源代码标签 [`linux-3090-round12`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round12)，提交 `aed2679360ff1c73ccf5dfcdc115be11e2dbab6d`。使用 `gspl`、RTX 3090、`configs/mofang_9cam_lean.yaml`。准备数据、光流、位姿、token 与兼容包的 1271 个文件逐个 SHA256 与第七轮一致；GS/TTO 和评估本轮重新执行。", "",
    "## 结论", "",
    "逐视图裁剪与只训练 rife 区域使 200 步累计优化时间从第十一轮的 cam3 14.108 秒、cam5 24.536 秒降到本轮 9.667 秒、12.111 秒。两项改动同时存在，因此这个差不能归因于裁剪框单一因素。cam3 的质量维持；cam5 在 200 步的质量下降，主要体现在目标 3，前景 PSNR 相对第十一轮同检查点下降约 3.07 dB。", "",
    "按既定判据（两组前景均值 PSNR≥纯光流、LPIPS≤纯光流，且不差视点数至少达到第十轮 6/6 与 3/4），本轮 **50/100/200 步均未达标**：cam5 各为 2/4。当前固定预设中，cam5 的 50 步前景平均 PSNR 最高，不能据此宣称其 4 个视点都获益。", "",
    "## 主质量与时间", "",
    "固定 `rife`、`_al`、直接贴回。PSNR 单位 dB，LPIPS 越小越好；每组各留出视点等权平均。累计 TTO 时间经过 CUDA 同步，排除编码、目标渲染及评估；第十一轮同检查点数据来自已归档原始 CSV/日志。", "",
    "| 设置 | 步数 | 本轮 TTO 秒 | 本轮前景 PSNR / LPIPS | 第十一轮前景 PSNR / LPIPS | 本轮物体 PSNR / LPIPS | 本轮不差目标 |", "|---|---:|---:|---:|---:|---:|---:|",
]
for setup in CFG["setups"]:
    for step in STEPS:
        v=q(setup,step)
        lines.append(f"| {setup} | {'FF' if step==0 else step} | {float(v['cumulative_tto_s']):.3f} | {v['fg_psnr']:.3f} / {v['fg_lpips']:.5f} | {v['fg_psnr_round11']:.3f} / {v['fg_lpips_round11']:.5f} | {v['object_psnr']:.3f} / {v['object_lpips']:.5f} | {v['fg_nonworse_count']}/{v['targets']} |")
lines += ["", "纯光流基线：cam3 前景 22.604 / 0.062884，cam5 前景 28.000 / 0.039572。FF 行的 0 秒仅表示没有 TTO，编码与渲染仍耗时。cam3 在 50 步达 6/6；cam5 的 50 步、100 步与 200 步均只有 2/4。", "",
          "## 监督范围与速度", "", "| 设置 | 训练高斯数 | 监督图边长 | 本轮视图平均面积 | 上轮共框面积 | 本轮 50 / 100 / 200 步秒 | 上轮 50 / 100 / 200 步秒 |", "|---|---:|---:|---:|---:|---|---|"]
old_meta = {s: json.loads((OLD / "gs" / s / "gs_tok448_nat_dil_al/meta.json").read_text())["tto"] for s in CFG["setups"]}
new_meta = {s: json.loads((WORK / "gs" / s / "gs_tokrife448_nat_dil_al_local/meta.json").read_text()) for s in CFG["setups"]}
for setup in CFG["setups"]:
    t=new_meta[setup]["tto"]
    n=[next(r for r in timing if r["setup"]==setup and r["iteration"]==step)["cumulative_tto_s"] for step in STEPS[1:]]
    o=[next(r["time_s"] for r in old_meta[setup]["log"] if r["iter"]==step) for step in STEPS[1:]]
    lines.append(f"| {setup} | {t['train_gaussians']}（上轮 {old_meta[setup]['train_gaussians']}） | {t['res']} | {t['log'][0]['box']['area_frac']:.2%} | {old_meta[setup]['log'][0]['box']['area_frac']:.2%} | {' / '.join(f'{x:.3f}' for x in n)} | {' / '.join(f'{x:.3f}' for x in o)} |")
lines += ["", "逐视图 `(x,y,w,h)`、每步时间及输入视点拟合度见 `eval/tto_supervision_boxes.csv`、`eval/tto_checkpoint_timing.csv` 和 `eval/tto_training.csv`。各视图分别光栅化；监督面积为各视图占原裁剪面积比例的均值。不同监督范围与训练高斯集合会改变优化轨迹。输入 PSNR 在各自监督框内测得，不能跨轮直接当成同一像素集的质量比较。", "",
          "## cam5 目标 3 的退化", "", "| 步数 | 本轮前景 PSNR | 第十一轮前景 PSNR | 差值 | 本轮 LPIPS | 第十一轮 LPIPS |", "|---:|---:|---:|---:|---:|---:|"]
for step in STEPS[1:]:
    r=next(r for r in per_view if r["setup"]=="cam5" and r["target"]=="3" and r["step"]==step)
    lines.append(f"| {step} | {float(r['fg_psnr']):.3f} | {float(r['fg_psnr'])-float(r['delta_round11_psnr']):.3f} | {float(r['delta_round11_psnr']):+.3f} | {float(r['fg_lpips']):.5f} | {float(r['fg_lpips'])-float(r['delta_round11_lpips']):.5f} |")
lines += ["", "[cam5 目标 3 固定检查点对比图](figures/cam5/cam3_rife_checkpoints.png) 同时展示真值、光流、FF、50/100/200 步；图是视觉辅助，数值以原始逐视点 CSV 为准。各目标对比图在 `figures/`。上游 `eval/summary.md` 的“TTO 第十一轮”标题是标签中沿用的旧文案，这里的数据由本轮结果生成。上游拼图会按真值挑局部变体，仅作诊断；固定方法比较以本报告及固定检查点图为准。", "",
          "## 执行与验证", "", f"- 上游 17 项单元测试通过。`validate_results.py`：`{validation['status']}`，{validation['methods']} 种方法、{validation['metric_rows']} 行指标、{validation['auc_rows']} 行 AUC，警告 {validation['warnings']}。", "- cam3、cam5 在 GS/TTO 全部完成后分别运行原版 `evaluate.main()`，输入只读共享，原始七份 CSV 逐行等于两组工作输出按固定顺序拼接；见 `eval/parallel_merge_validation.json`。", "- 第七轮的 1271 个复用文件以 SHA256 逐个核对；清单见 `reused_files_manifest.json`。", "- 本轮 TTO 在标签原代码上运行，没有修改优化或指标算法。两个独立评估进程只影响评估完成的墙钟时间，不影响事先记录的 TTO 时间。", "- 仓库没有保存优化后的高斯参数或优化器状态；`work/round12/gs` 留有渲染 RGB/alpha，上传仅包含评估、图、元数据、日志和复现脚本。原始数据与权重需在本机自行提供。", "- 未记录 GS 开始到评估结束的精确墙钟时间，因此不能验证 README 所说的“十几分钟”端到端目标。", "",
          "## 复现", "", "```bash", "cd /home/han/linux-han/local-gs-eval", "git fetch --tags -f origin", "git switch -c experiment/mofang-9cam-round12-gspl-20261025 linux-3090-round12", "export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH", "export LGS_WORK_DIR=work/round12 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1", 'mkdir -p "$LGS_WORK_DIR"', 'cp -a --reflink=auto work/round7/{prepare,flow,poses,tokens,compat_packages} "$LGS_WORK_DIR"/', "python -m unittest discover -s tests -v", "python scripts/run_anysplat.py --config configs/mofang_9cam_lean.yaml", "python scripts/evaluate.py --config configs/mofang_9cam_lean.yaml", "python scripts/validate_results.py configs/mofang_9cam_lean.yaml", "```", "", "本次评估实际用 `evaluate_parallel.py` 与 `evaluate_worker.py` 按 cam3/cam5 并行；标准顺序命令也会调用同一个评估程序。完整结果、逐视点 CSV、监督框、日志与第十一轮归档随新分支保存。", ""]
(OUT / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps({"quality": quality, "merge_counts": merge_counts, "files_verified": len(old_manifest)}, ensure_ascii=False))
