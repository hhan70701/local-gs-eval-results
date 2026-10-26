"""Archive and summarize the complete linux-3090 round15-pixgs run."""
import csv
import json
import platform
import shutil
import statistics
import sys
from collections import defaultdict
from pathlib import Path

import torch
import gsplat
import yaml

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work/dataset6"
OUT = ROOT / "results/linux-3090-round15-pixgs-20261025"
CONFIG = yaml.safe_load((ROOT / "configs/dataset6_lean.yaml").read_text())
SHOTS = CONFIG["dataset6"]["hosts"]["linux-3090"]
REF = CONFIG["eval"]["ref_flow"]
PILOT = set(CONFIG["dataset6"]["pilot_shots"]) & set(SHOTS)
VARIANTS = ("cnw_cnn", "cnw_cnn_mw", "cnw_cnn_pix", "cnw_f5", "cnw_f5_mw", "cnw_f5_pix")


def cp(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(data[0]))
        w.writeheader()
        w.writerows(data)


def method(variant, how="direct"):
    if variant.endswith("_pix"):
        base = f"gs_tok{variant}448_pix_al_local"
    else:
        base = f"gs_tok{variant}448_nat_dil_al_local"
    return ("hyb_token" if how == "direct" else "hyb_tokchk_oracle") + f"[{base}]"


def avg(data, name):
    return statistics.mean(float(r[name]) for r in data)


assert len(SHOTS) == 23 and len(set(SHOTS)) == 23
OUT.mkdir(parents=True, exist_ok=True)
cp(ROOT / "configs/dataset6_lean.yaml", OUT / "config.yaml")
for name in ("dataset6_run.log", "dataset6_run.start_utc", "dataset6_run.end_utc", "dataset6_run.time",
             "dataset6_batch.log", "dataset6_batch.start_utc", "dataset6_batch.end_utc", "dataset6_batch.time"):
    p = ROOT / "work" / name
    if p.exists():
        cp(p, OUT / "logs" / name)
cp(Path("/tmp/round15_3090_tests.log"), OUT / "logs/numerics_tests.log")
cp(Path("/tmp/round15_3090_batched.py"), OUT / "run_batched.py")
cp(WORK / "summary_all.md", OUT / "summary_all.md")

all_metrics = []
validations = {}
pix_meta = []
timings = []
for shot in SHOTS:
    tag = shot.replace("/", "_")
    src = WORK / tag
    dst = OUT / "shots" / tag
    for rel in ("config.yaml", "timing.json", "prepare/prepare.json", "tokens/tokens.json"):
        cp(src / rel, dst / rel)
    for folder in ("poses", "logs", "eval"):
        for p in (src / folder).rglob("*"):
            if p.is_file():
                cp(p, dst / folder / p.relative_to(src / folder))
    for p in (src / "gs").rglob("meta.json"):
        cp(p, dst / "gs" / p.relative_to(src / "gs"))
    disp_meta = ROOT / "data/disp_fs" / tag / "meta.json"
    cp(disp_meta, dst / "disp_fs/meta.json")
    val = json.loads((src / "eval/validation.json").read_text())
    assert val["status"] == "PASS" and not val["warnings"], (shot, val)
    validations[shot] = val
    data = read_csv(src / "eval/metrics.csv")
    assert len(data) == val["metric_rows"]
    all_metrics.extend(dict(shot=shot, **r) for r in data)
    timings.append(dict(shot=shot, **json.loads((src / "timing.json").read_text())))
    for v in ("cnw_cnn", "cnw_f5"):
        m = json.loads((src / "gs/in035" / f"gs_tok{v}_pix448_pix_al_local/meta.json").read_text())
        assert m["render"]["mode"] == "gsplat", (shot, v, m["render"])
        for target, item in m["pixgs"].items():
            pix_meta.append(dict(shot=shot, variant=v, target=int(target),
                                 render_per_view_s=m["time_render_per_view_s"],
                                 windows_stereo_encode_s=m["time_encode_s"],
                                 missing_a=item["missing_a"], missing_b=item["missing_b"],
                                 gaussians=item["gaussians"]))
write_csv(OUT / "metrics_all.csv", all_metrics)
write_csv(OUT / "timing_all.csv", timings)
write_csv(OUT / "pixgs_per_target.csv", pix_meta)
(OUT / "validation_all.json").write_text(json.dumps(validations, ensure_ascii=False, indent=2) + "\n")

idx = {(r["shot"], int(r["target"]), r["method"], r["region"]): r for r in all_metrics}
targets = [(shot, k) for shot in SHOTS for k in (1, 2, 4)]
assert len(targets) == 69
comparisons = []
for subset, pairs in (("all", targets), ("pilot", [p for p in targets if p[0] in PILOT])):
    for variant in VARIANTS:
        for how in ("direct", "oracle"):
            meth = method(variant, how)
            fg = [idx[s,k,meth,"fg"] for s,k in pairs]
            flow = [idx[s,k,REF,"fg"] for s,k in pairs]
            rest = [idx[s,k,meth,"rest"] for s,k in pairs]
            nonworse = sum(float(a["psnr"]) >= float(b["psnr"])-1e-6 and
                           float(a["lpips"]) <= float(b["lpips"])+1e-6 for a,b in zip(fg,flow))
            comparisons.append(dict(subset=subset, variant=variant, how=how, targets=len(pairs),
                                    fg_psnr=avg(fg,"psnr"), fg_lpips=avg(fg,"lpips"),
                                    rest_psnr=avg(rest,"psnr"), nonworse=nonworse))
write_csv(OUT / "quality_comparison.csv", comparisons)

environment = dict(source_repo="luckyhan-mike/local-gs-eval",
                   source_tag="linux-3090-round15-pixgs",
                   source_commit="cae8a7b2a4245f20c966fc1cc15137f52a5e083c",
                   host="linux-3090", shots=SHOTS,
                   python=sys.version, executable=sys.executable,
                   torch=torch.__version__, torch_cuda=torch.version.cuda,
                   gsplat=gsplat.__version__, gpu=torch.cuda.get_device_name(0),
                   platform=platform.platform(),
                   compatibility_package="work/round7/compat_packages linked into each shot work directory")
(OUT / "environment.json").write_text(json.dumps(environment, ensure_ascii=False, indent=2) + "\n")

def comp(subset, v, how):
    return next(x for x in comparisons if x["subset"]==subset and x["variant"]==v and x["how"]==how)

def score(x):
    return f"{x['fg_psnr']:.3f} / {x['fg_lpips']:.5f}"

flow_fg = [idx[s,k,REF,"fg"] for s,k in targets]
lines = ["# linux-3090 第十五轮：逐像素高斯 pixgs，23 组场景", "",
         "源代码为 [`linux-3090-round15-pixgs`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round15-pixgs)，提交 `cae8a7b2a4245f20c966fc1cc15137f52a5e083c`。按 `configs/dataset6_lean.yaml --host linux-3090` 执行，23 组场景、每组 3 个留出视点，共 69 个目标。所有 23 组已通过仓库验证。", "",
         "pixgs 使用随源码提交的 FoundationStereo 位移、原分辨率 token 重建区及 gsplat 渲染；不调用 AnySplat 编码或 TTO。下表比较的是同一批目标、同一个固定 token 变体、直接贴回或真值 oracle 上限。", "",
         "## 主对比：全部 69 个留出视点", "",
         f"纯光流前景均值：{avg(flow_fg,'psnr'):.3f} dB / {avg(flow_fg,'lpips'):.5f} LPIPS。PSNR 越高、LPIPS 越低越好；“不差”要求同一目标两项都不低于纯光流。", "",
         "| token / 方法 | 直接贴回 fg PSNR / LPIPS | 直接不差目标 | oracle fg PSNR / LPIPS | oracle 不差目标 |", "|---|---:|---:|---:|---:|"]
for v in VARIANTS:
    a,b=comp("all",v,"direct"),comp("all",v,"oracle")
    lines.append(f"| {v} | {score(a)} | {a['nonworse']}/69 | {score(b)} | {b['nonworse']}/69 |")
lines += ["", "这里的单窗口/多窗口均为 AnySplat 前馈；TTO 25/50/100 步的完整对照见原始 `summary_all.md` 和每组 `eval/metrics.csv`。oracle 使用目标真值定义失败区域，只是上限诊断。", "",
          "## 第七轮试点场景（9 个留出视点）", "",
          "检测 CNN 没有用这 3 组训练；`cnw_cnn` 的泛化判断应以这里为主。", "",
          "| token / 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 |", "|---|---:|---:|---:|---:|"]
for v in ("cnw_cnn","cnw_cnn_mw","cnw_cnn_pix"):
    a,b=comp("pilot",v,"direct"),comp("pilot",v,"oracle")
    lines.append(f"| {v} | {score(a)} | {a['nonworse']}/9 | {score(b)} | {b['nonworse']}/9 |")
lines += ["", "## pixgs 渲染、视差覆盖与范围", "",
          "| 变体 | 每视点渲染中位数 | 最大视差缺失率 a / b | 中位高斯数 / 目标 |", "|---|---:|---:|---:|"]
for v in ("cnw_cnn","cnw_f5"):
    rr=[x for x in pix_meta if x["variant"]==v]
    lines.append(f"| {v} | {statistics.median(x['render_per_view_s'] for x in rr)*1000:.1f} ms | {max(x['missing_a'] for x in rr):.3%} / {max(x['missing_b'] for x in rr):.3%} | {statistics.median(x['gaussians'] for x in rr):.0f} |")
lines += ["", "`time_render_per_view_s` 包含生成高斯、完整与 core 两次 gsplat 渲染及 CPU/GPU 转换；首组可能包含 CUDA 首次调用开销，不含离线 FoundationStereo。`time_encode_s` 是 Windows RTX 3090 导出视差时记录的时间，不能算进本机运行时间。逐目标统计见 `pixgs_per_target.csv`。", "",
          "## 验证与复现", "",
          f"上游 22 项单元测试通过。23/23 组验证 PASS，合计 {sum(v['metric_rows'] for v in validations.values())} 行指标、{sum(v['auc_rows'] for v in validations.values())} 行 AUC，警告数 {sum(len(v['warnings']) for v in validations.values())}。", "",
          "前两组按 README 完整顺序运行；其余 21 组顺序生成 prepare、token、AnySplat、pixgs、光流，再以 3 个独立进程按场景并行执行原版评估与验证，最后用 `--summary-only` 生成 23 组汇总。评估没有与 GS/TTO 计时重叠；各组 `timing.json` 保留了两个阶段的耗时。兼容包通过工作目录链接接入，没有改系统 conda 包。", "",
          "归档上传 `summary_all.md`、逐组配置/位姿/日志/评估/验证、GS `meta.json`、视差导出元数据、环境与复现脚本；大型原图、对齐图、光流数组及 GS 渲染 RGB/alpha 保留在本机 `work/dataset6`。所有 23 组原始图与位移数据在运行前做过文件存在性及 NPZ 字段检查。", "",
          "本机 `gspl` 的 PyTorch 2.0.1 与全局 e3nn 不兼容；这次复用已有的 `work/round7/compat_packages`，为每组工作目录建立链接后运行。下面的复现命令要求该兼容包和 README 所列原始图像、标定、预导出 token/视差均已就绪；`work/dataset6` 原始中间结果保留在本机。", "",
          "```bash", "cd /home/han/linux-han/local-gs-eval", "git fetch --tags -f origin", "git switch -c experiment/linux-3090-round15-pixgs-20261025 linux-3090-round15-pixgs", "export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH", "export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1", "python -m unittest discover -s tests -v", "python - <<'PY'", "import pathlib, yaml", "root = pathlib.Path.cwd()", "shots = yaml.safe_load((root / 'configs/dataset6_lean.yaml').read_text())['dataset6']['hosts']['linux-3090']", "source = root / 'work/round7/compat_packages'", "assert source.is_dir()", "for shot in shots:", "    folder = root / 'work/dataset6' / shot.replace('/', '_')", "    folder.mkdir(parents=True, exist_ok=True)", "    link = folder / 'compat_packages'", "    if not link.exists(): link.symlink_to(source, target_is_directory=True)", "PY", "python scripts/run_scenes.py --config configs/dataset6_lean.yaml --host linux-3090", "```", ""]
(OUT / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps(dict(shots=len(SHOTS), metrics=len(all_metrics), pixgs_rows=len(pix_meta), archive=str(OUT)), ensure_ascii=False))
