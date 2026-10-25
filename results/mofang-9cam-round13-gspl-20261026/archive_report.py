"""Archive the local-only RTX 3090 round 13 run and its measured comparisons."""
import csv
import hashlib
import json
import platform
import shutil
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work/round13"
OUT = ROOT / "results/mofang-9cam-round13-gspl-20261026"
OLD = ROOT / "results/mofang-9cam-round12-gspl-20261025"
STEPS = (0, 25, 50, 100)
REF = "flow_s1.0_pose"


def cp(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def rows(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_rows(path, data):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0]))
        writer.writeheader()
        writer.writerows(data)


def hash_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def method(step):
    return "hyb_token[gs_tokrife448_nat_dil_al" + (f"_tto{step}" if step else "") + "_local]"


def mean(data, key):
    return statistics.mean(float(r[key]) for r in data)


OUT.mkdir(exist_ok=True)
cp(ROOT / "configs/mofang_9cam_lean.yaml", OUT / "config.yaml")
for path in (WORK / "eval").rglob("*"):
    if path.is_file():
        cp(path, OUT / "eval" / path.relative_to(WORK / "eval"))
for name in ("prepare", "flow", "poses", "tokens", "gs"):
    for path in (WORK / name).rglob("*.json"):
        cp(path, OUT / name / path.relative_to(WORK / name))
for path in (WORK / "logs").glob("*"):
    if path.is_file():
        cp(path, OUT / "logs" / path.name)

manifest = json.loads((OLD / "reused_files_manifest.json").read_text())
for r in manifest:
    path = WORK / r["path"]
    assert path.stat().st_size == r["size"] and hash_file(path) == r["sha256"], r["path"]
cp(OLD / "reused_files_manifest.json", OUT / "reused_files_manifest.json")

import torch
import gsplat

environment = dict(source_tag="linux-3090-round13",
                   source_commit="a5d5cbc0ddd2b0a8143bfdccab456ae417f8cb78",
                   python=sys.version, executable=sys.executable,
                   torch=torch.__version__, torch_cuda=torch.version.cuda,
                   gsplat=gsplat.__version__, gpu=torch.cuda.get_device_name(0),
                   platform=platform.platform(), reused_round7_files_verified=len(manifest),
                   publication="hhan70701/local-gs-eval-results:experiment/mofang-9cam-round13-gspl-20261026")
(OUT / "environment.json").write_text(json.dumps(environment, ensure_ascii=False, indent=2) + "\n")

timing, boxes, train = [], [], []
for setup, cams in (("cam3", [0, 4, 8]), ("cam5", [0, 2, 4, 6, 8])):
    meta = json.loads((WORK / "gs" / setup / "gs_tokrife448_nat_dil_al_local/meta.json").read_text())
    tto = meta["tto"]
    box = tto["log"][0]["box"]
    assert len(box["per_view"]) == len(cams)
    for cam, (x, y, w, h) in zip(cams, box["per_view"]):
        boxes.append(dict(setup=setup, camera=cam, x=x, y=y, w=w, h=h,
                          supervision_res=tto["res"], area_frac=w*h/tto["res"]**2))
    for entry in tto["log"]:
        for cam, psnr in zip(cams, entry["ctx_psnr"]):
            train.append(dict(setup=setup, camera=cam, iteration=entry["iter"],
                              input_crop_psnr=psnr, loss=entry["loss"]))
        if "time_s" in entry:
            timing.append(dict(setup=setup, iteration=entry["iter"],
                               cumulative_tto_s=entry["time_s"],
                               step_ms=entry["time_s"]*1000/entry["iter"],
                               mean_input_psnr=statistics.mean(entry["ctx_psnr"]),
                               mean_area_frac=box["area_frac"], train_gaussians=tto["train_gaussians"],
                               encode_s=meta["time_encode_s"]))
save_rows(OUT / "eval/tto_checkpoint_timing.csv", timing)
save_rows(OUT / "eval/tto_supervision_boxes.csv", boxes)
save_rows(OUT / "eval/tto_training.csv", train)

merge_counts = {}
for name in ("metrics.csv", "auc.csv", "registration.csv", "risk_sweep.csv",
             "paste.csv", "tokchk.csv", "token_ringreg.csv"):
    combined = list(csv.reader((WORK / "eval" / name).open(newline="")))
    parts = [list(csv.reader((WORK / "eval_jobs" / s / "eval" / name).open(newline="")))
             for s in ("cam3", "cam5")]
    assert all(part[0] == combined[0] for part in parts), name
    assert combined[1:] == parts[0][1:] + parts[1][1:], name
    merge_counts[name] = len(combined)-1
(OUT / "eval/parallel_merge_validation.json").write_text(json.dumps(merge_counts, indent=2)+"\n")

new = rows(OUT / "eval/metrics.csv")
old = rows(OLD / "eval/metrics.csv")
ni = {(r["setup"], r["target"], r["method"], r["region"]): r for r in new}
oi = {(r["setup"], r["target"], r["method"], r["region"]): r for r in old}
quality, per_view = [], []
for setup in ("cam3", "cam5"):
    targets = sorted({r["target"] for r in new if r["setup"] == setup}, key=int)
    for step in STEPS:
        method_name = method(step)
        q = dict(setup=setup, step=step, cumulative_tto_s=next((r["cumulative_tto_s"] for r in timing if r["setup"]==setup and r["iteration"]==step), 0), targets=len(targets))
        count=0
        for target in targets:
            fg=ni[setup,target,method_name,"fg"]
            flow=ni[setup,target,REF,"fg"]
            nonworse=float(fg["psnr"])>=float(flow["psnr"])-1e-6 and float(fg["lpips"])<=float(flow["lpips"])+1e-6
            count+=nonworse
            old_fg=oi.get((setup,target,method_name,"fg"))
            per_view.append(dict(setup=setup,target=target,step=step,
                                 fg_psnr=fg["psnr"],fg_lpips=fg["lpips"],
                                 delta_flow_psnr=float(fg["psnr"])-float(flow["psnr"]),
                                 delta_flow_lpips=float(fg["lpips"])-float(flow["lpips"]),
                                 old_fg_psnr=old_fg["psnr"] if old_fg else "",
                                 old_fg_lpips=old_fg["lpips"] if old_fg else "",
                                 nonworse_flow=nonworse))
        q["nonworse_targets"]=count
        for region in ("fg","object","rest"):
            for key in ("psnr","lpips"):
                rr=[ni[setup,t,method_name,region] for t in targets]
                q[f"{region}_{key}"]=mean(rr,key)
                if all((setup,t,method_name,region) in oi for t in targets):
                    oo=[oi[setup,t,method_name,region] for t in targets]
                    q[f"{region}_{key}_old"]=mean(oo,key)
        quality.append(q)
save_rows(OUT / "eval/tto_quality_comparison.csv", quality)
save_rows(OUT / "eval/tto_quality_per_view.csv", per_view)

validation=json.loads((OUT / "eval/validation.json").read_text())
assert validation["status"]=="PASS" and not validation["warnings"]
reference_delta={key:max(abs(float(r[key])-float(ni[r["setup"],r["target"],r["method"],r["region"]][key]))
                         for r in old if r["method"]==REF) for key in ("psnr","lpips","area_px")}
assert all(v==0 for v in reference_delta.values())
(OUT / "eval/reference_baseline_check.json").write_text(json.dumps(reference_delta,indent=2)+"\n")

def q(setup, step):
    return next(r for r in quality if r["setup"]==setup and r["step"]==step)

def val(setup, target, step):
    return next(r for r in per_view if r["setup"]==setup and r["target"]==str(target) and r["step"]==step)

def elapsed(name):
    return float(next(x.split()[1] for x in (WORK/"logs"/f"{name}.time").read_text().splitlines() if x.startswith("real ")))

lines=["# 第十三轮本机实验：TTO 位移和协方差约束", "",
       "来源：`luckyhan-mike/local-gs-eval` 的 `linux-3090-round13` 标签，提交 `a5d5cbc0ddd2b0a8143bfdccab456ae417f8cb78`。在 RTX 3090 的 `gspl` 环境，按 `configs/mofang_9cam_lean.yaml` 执行。结果归档到 `hhan70701/local-gs-eval-results` 的 `experiment/mofang-9cam-round13-gspl-20261026` 分支；完整渲染中间产物保存在本机 `work/round13`。", "",
       "## 主要发现", "",
       "cam3 在 50 步达到 6/6 留出视点不差；cam5 到 100 步仍只有 2/4。cam5 目标 3 的 100 步前景 PSNR 从第十二轮 33.699 dB 变为本轮 33.895 dB，LPIPS 从 0.02160 变为 0.02243（变差）；PSNR 仍低于第十二轮 50 步的 34.036 dB。第十三轮没有 200 步检查点，因此无法直接检验之前在 200 步出现的 -3.07 dB 退化是否消失。", "",
       "此轮同时改了位置学习率、位移约束、协方差参数化和缩放约束，且 AnySplat 前馈重新编码略有差异；任何质量变化都不能单独归因于某一个约束。参考光流沿用第七轮，指标与第十二轮逐项完全相同。", "",
       "## 质量与耗时", "",
       "固定 `rife`、`_al`、直接贴回，目标等权平均。PSNR 越高、LPIPS 越低越好。TTO 时间是 GPU 同步后的累计优化时间，排除编码、目标渲染与评估。FF 的 0 秒仅表示不做 TTO。", "",
       "| 设置 | 步数 | TTO 秒 | 前景 PSNR / LPIPS | 物体 PSNR / LPIPS | 不差目标数 |", "|---|---:|---:|---:|---:|---:|"]
for setup in ("cam3","cam5"):
    for step in STEPS:
        r=q(setup,step)
        lines.append(f"| {setup} | {'FF' if step==0 else step} | {float(r['cumulative_tto_s']):.3f} | {r['fg_psnr']:.3f} / {r['fg_lpips']:.5f} | {r['object_psnr']:.3f} / {r['object_lpips']:.5f} | {r['nonworse_targets']}/{r['targets']} |")
lines += ["", "参考光流：cam3 前景 22.604 dB / 0.062884，cam5 前景 28.000 dB / 0.039572。与第十二轮相同检查点的逐目标对比见 `eval/tto_quality_per_view.csv`。", "",
          "## 重点目标：cam5 / 3", "", "| 步数 | 本轮前景 PSNR | 第十二轮同检查点 | 本轮 LPIPS | 第十二轮同检查点 |", "|---:|---:|---:|---:|---:|"]
for step in (0,50,100):
    r=val("cam5",3,step)
    lines.append(f"| {'FF' if step==0 else step} | {float(r['fg_psnr']):.3f} | {float(r['old_fg_psnr']):.3f} | {float(r['fg_lpips']):.5f} | {float(r['old_fg_lpips']):.5f} |")
lines += ["", "[固定检查点对比图](figures/cam5/cam3_rife_checkpoints.png) 展示 GT、光流、FF、25/50/100 步；其余目标也保存在 `figures/`。图是视觉诊断，数字以原始 `eval/metrics.csv` 为准。第十二轮 200 步仅作为历史失败点，不在本轮配置的测量范围内。", "",
          "## 训练范围与执行验证", "", "| 设置 | 训练高斯 | 监督视图平均面积 | 25 / 50 / 100 步累计秒 |", "|---|---:|---:|---|"]
for setup in ("cam3","cam5"):
    rr=[r for r in timing if r["setup"]==setup]
    times = " / ".join("%.3f" % r["cumulative_tto_s"] for r in rr)
    lines.append(f"| {setup} | {rr[0]['train_gaussians']} | {rr[0]['mean_area_frac']:.2%} | {times} |")
lines += ["", "监督框逐相机坐标在 `eval/tto_supervision_boxes.csv`；输入视点 PSNR 在每个框内计算，不能直接跨轮比较。", "",
          f"18 项上游测试通过；仓库验证 `{validation['status']}`，{validation['methods']} 种方法、{validation['metric_rows']} 行指标、{validation['auc_rows']} 行 AUC、{validation['montages']} 张拼图，无警告。", "",
          f"GS/TTO 进程墙钟 {elapsed('1_anysplat'):.2f} 秒；cam3/cam5 并行评估墙钟 {elapsed('3_evaluate'):.2f} 秒；验证 {elapsed('4_validation'):.2f} 秒。评估在 GS/TTO 完成后才开始，两进程各自调用原始 `evaluate.main()`；7 份合并 CSV 已逐行对照两组独立输出。", "",
          f"第七轮复用输入 {len(manifest)} 个文件已逐个 SHA256 核对；参考光流的 PSNR、LPIPS、区域像素数相对第十二轮最大差都是 0。", "",
          "归档包含配置、环境、原始评估 CSV、元数据、日志、固定检查点图和复现脚本。全部渲染 RGB/alpha 留在 `work/round13/gs`，原始数据和权重仍在主机原位置；源脚本没有保存优化后高斯或优化器状态。", "",
          "## 复现", "", "```bash", "cd /home/han/linux-han/local-gs-eval", "git fetch --tags -f origin", "git switch -c experiment/mofang-9cam-round13-gspl-20261026-local linux-3090-round13", "export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH", "export LGS_WORK_DIR=work/round13 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1", 'mkdir -p "$LGS_WORK_DIR"', 'cp -a --reflink=auto work/round7/{prepare,flow,poses,tokens,compat_packages} "$LGS_WORK_DIR"/', "python -m unittest discover -s tests -v", "python scripts/run_anysplat.py --config configs/mofang_9cam_lean.yaml", "python scripts/evaluate.py --config configs/mofang_9cam_lean.yaml", "python scripts/validate_results.py configs/mofang_9cam_lean.yaml", "```", "", "本次评估实际使用本目录的 `evaluate_parallel.py` 与 `evaluate_worker.py` 按相机组合并行；标准顺序命令调用同一原始评估程序。", ""]
(OUT/"REPORT.md").write_text("\n".join(lines),encoding="utf-8")
print(json.dumps(dict(validation=validation,quality=quality,reused=len(manifest)),ensure_ascii=False))
