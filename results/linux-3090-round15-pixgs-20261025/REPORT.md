# linux-3090 第十五轮：逐像素高斯 pixgs，23 组场景

源代码为 [`linux-3090-round15-pixgs`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round15-pixgs)，提交 `cae8a7b2a4245f20c966fc1cc15137f52a5e083c`。按 `configs/dataset6_lean.yaml --host linux-3090` 执行，23 组场景、每组 3 个留出视点，共 69 个目标。所有 23 组已通过仓库验证。

pixgs 使用随源码提交的 FoundationStereo 位移、原分辨率 token 重建区及 gsplat 渲染；不调用 AnySplat 编码或 TTO。下表比较的是同一批目标、同一个固定 token 变体、直接贴回或真值 oracle 上限。

## 主对比：全部 69 个留出视点

纯光流前景均值：27.294 dB / 0.06349 LPIPS。PSNR 越高、LPIPS 越低越好；“不差”要求同一目标两项都不低于纯光流。

| token / 方法 | 直接贴回 fg PSNR / LPIPS | 直接不差目标 | oracle fg PSNR / LPIPS | oracle 不差目标 |
|---|---:|---:|---:|---:|
| cnw_cnn | 26.751 / 0.08443 | 0/69 | 27.299 / 0.06840 | 5/69 |
| cnw_cnn_mw | 26.948 / 0.08192 | 0/69 | 27.439 / 0.06700 | 8/69 |
| cnw_cnn_pix | 27.044 / 0.07877 | 0/69 | 27.499 / 0.06810 | 2/69 |
| cnw_f5 | 26.276 / 0.09170 | 0/69 | 27.146 / 0.07027 | 5/69 |
| cnw_f5_mw | 26.472 / 0.08853 | 0/69 | 27.247 / 0.06891 | 5/69 |
| cnw_f5_pix | 26.691 / 0.08292 | 0/69 | 27.354 / 0.06941 | 0/69 |

这里的单窗口/多窗口均为 AnySplat 前馈；TTO 25/50/100 步的完整对照见原始 `summary_all.md` 和每组 `eval/metrics.csv`。oracle 使用目标真值定义失败区域，只是上限诊断。

## 第七轮试点场景（9 个留出视点）

检测 CNN 没有用这 3 组训练；`cnw_cnn` 的泛化判断应以这里为主。

| token / 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 |
|---|---:|---:|---:|---:|
| cnw_cnn | 24.559 / 0.08293 | 0/9 | 24.998 / 0.07130 | 0/9 |
| cnw_cnn_mw | 24.727 / 0.08020 | 0/9 | 25.168 / 0.06966 | 0/9 |
| cnw_cnn_pix | 25.071 / 0.07536 | 0/9 | 25.440 / 0.06624 | 1/9 |

## pixgs 渲染、视差覆盖与范围

| 变体 | 每视点渲染中位数 | 最大视差缺失率 a / b | 中位高斯数 / 目标 |
|---|---:|---:|---:|
| cnw_cnn | 472.0 ms | 0.000% / 5.335% | 435593 |
| cnw_f5 | 112.8 ms | 0.000% / 5.612% | 590107 |

`time_render_per_view_s` 包含生成高斯、完整与 core 两次 gsplat 渲染及 CPU/GPU 转换；首组可能包含 CUDA 首次调用开销，不含离线 FoundationStereo。`time_encode_s` 是 Windows RTX 3090 导出视差时记录的时间，不能算进本机运行时间。逐目标统计见 `pixgs_per_target.csv`。

## 验证与复现

上游 22 项单元测试通过。23/23 组验证 PASS，合计 32469 行指标、345 行 AUC，警告数 0。

前两组按 README 完整顺序运行；其余 21 组顺序生成 prepare、token、AnySplat、pixgs、光流，再以 3 个独立进程按场景并行执行原版评估与验证，最后用 `--summary-only` 生成 23 组汇总。评估没有与 GS/TTO 计时重叠；各组 `timing.json` 保留了两个阶段的耗时。兼容包通过工作目录链接接入，没有改系统 conda 包。

归档上传 `summary_all.md`、逐组配置/位姿/日志/评估/验证、GS `meta.json`、视差导出元数据、环境与复现脚本；大型原图、对齐图、光流数组及 GS 渲染 RGB/alpha 保留在本机 `work/dataset6`。所有 23 组原始图与位移数据在运行前做过文件存在性及 NPZ 字段检查。

本机 `gspl` 的 PyTorch 2.0.1 与全局 e3nn 不兼容；这次复用已有的 `work/round7/compat_packages`，为每组工作目录建立链接后运行。下面的复现命令要求该兼容包和 README 所列原始图像、标定、预导出 token/视差均已就绪；`work/dataset6` 原始中间结果保留在本机。

```bash
cd /home/han/linux-han/local-gs-eval
git fetch --tags -f origin
git switch -c experiment/linux-3090-round15-pixgs-20261025 linux-3090-round15-pixgs
export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH
export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1
python -m unittest discover -s tests -v
python - <<'PY'
import pathlib, yaml
root = pathlib.Path.cwd()
shots = yaml.safe_load((root / 'configs/dataset6_lean.yaml').read_text())['dataset6']['hosts']['linux-3090']
source = root / 'work/round7/compat_packages'
assert source.is_dir()
for shot in shots:
    folder = root / 'work/dataset6' / shot.replace('/', '_')
    folder.mkdir(parents=True, exist_ok=True)
    link = folder / 'compat_packages'
    if not link.exists(): link.symlink_to(source, target_is_directory=True)
PY
python scripts/run_scenes.py --config configs/dataset6_lean.yaml --host linux-3090
```
