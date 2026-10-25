# 第十三轮本机实验：TTO 位移和协方差约束

来源：`luckyhan-mike/local-gs-eval` 的 `linux-3090-round13` 标签，提交 `a5d5cbc0ddd2b0a8143bfdccab456ae417f8cb78`。在 RTX 3090 的 `gspl` 环境，按 `configs/mofang_9cam_lean.yaml` 执行。结果归档到 `hhan70701/local-gs-eval-results` 的 `experiment/mofang-9cam-round13-gspl-20261026` 分支；完整渲染中间产物保存在本机 `work/round13`。

## 主要发现

cam3 在 50 步达到 6/6 留出视点不差；cam5 到 100 步仍只有 2/4。cam5 目标 3 的 100 步前景 PSNR 从第十二轮 33.699 dB 变为本轮 33.895 dB，LPIPS 从 0.02160 变为 0.02243（变差）；PSNR 仍低于第十二轮 50 步的 34.036 dB。第十三轮没有 200 步检查点，因此无法直接检验之前在 200 步出现的 -3.07 dB 退化是否消失。

此轮同时改了位置学习率、位移约束、协方差参数化和缩放约束，且 AnySplat 前馈重新编码略有差异；任何质量变化都不能单独归因于某一个约束。参考光流沿用第七轮，指标与第十二轮逐项完全相同。

## 质量与耗时

固定 `rife`、`_al`、直接贴回，目标等权平均。PSNR 越高、LPIPS 越低越好。TTO 时间是 GPU 同步后的累计优化时间，排除编码、目标渲染与评估。FF 的 0 秒仅表示不做 TTO。

| 设置 | 步数 | TTO 秒 | 前景 PSNR / LPIPS | 物体 PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---:|---:|---:|
| cam3 | FF | 0.000 | 26.334 / 0.05382 | 17.331 / 0.16624 | 3/6 |
| cam3 | 25 | 1.808 | 26.677 / 0.05088 | 17.792 / 0.14498 | 5/6 |
| cam3 | 50 | 3.681 | 26.873 / 0.04913 | 18.222 / 0.13111 | 6/6 |
| cam3 | 100 | 7.459 | 27.044 / 0.04782 | 18.936 / 0.11492 | 6/6 |
| cam5 | FF | 0.000 | 27.724 / 0.04215 | 20.232 / 0.09189 | 0/4 |
| cam5 | 25 | 2.101 | 28.387 / 0.04038 | 21.020 / 0.08232 | 1/4 |
| cam5 | 50 | 4.249 | 28.726 / 0.03941 | 21.721 / 0.07747 | 2/4 |
| cam5 | 100 | 8.572 | 28.968 / 0.03871 | 22.322 / 0.06815 | 2/4 |

参考光流：cam3 前景 22.604 dB / 0.062884，cam5 前景 28.000 dB / 0.039572。与第十二轮相同检查点的逐目标对比见 `eval/tto_quality_per_view.csv`。

## 重点目标：cam5 / 3

| 步数 | 本轮前景 PSNR | 第十二轮同检查点 | 本轮 LPIPS | 第十二轮同检查点 |
|---:|---:|---:|---:|---:|
| FF | 30.813 | 30.980 | 0.02931 | 0.02882 |
| 50 | 33.227 | 34.036 | 0.02390 | 0.02243 |
| 100 | 33.895 | 33.699 | 0.02243 | 0.02160 |

[固定检查点对比图](figures/cam5/cam3_rife_checkpoints.png) 展示 GT、光流、FF、25/50/100 步；其余目标也保存在 `figures/`。图是视觉诊断，数字以原始 `eval/metrics.csv` 为准。第十二轮 200 步仅作为历史失败点，不在本轮配置的测量范围内。

## 训练范围与执行验证

| 设置 | 训练高斯 | 监督视图平均面积 | 25 / 50 / 100 步累计秒 |
|---|---:|---:|---|
| cam3 | 53872 | 60.80% | 1.808 / 3.681 / 7.459 |
| cam5 | 47474 | 35.13% | 2.101 / 4.249 / 8.572 |

监督框逐相机坐标在 `eval/tto_supervision_boxes.csv`；输入视点 PSNR 在每个框内计算，不能直接跨轮比较。

18 项上游测试通过；仓库验证 `PASS`，13 种方法、780 行指标、50 行 AUC、10 张拼图，无警告。

GS/TTO 进程墙钟 39.91 秒；cam3/cam5 并行评估墙钟 61.63 秒；验证 2.70 秒。评估在 GS/TTO 完成后才开始，两进程各自调用原始 `evaluate.main()`；7 份合并 CSV 已逐行对照两组独立输出。

第七轮复用输入 1271 个文件已逐个 SHA256 核对；参考光流的 PSNR、LPIPS、区域像素数相对第十二轮最大差都是 0。

归档包含配置、环境、原始评估 CSV、元数据、日志、固定检查点图和复现脚本。全部渲染 RGB/alpha 留在 `work/round13/gs`，原始数据和权重仍在主机原位置；源脚本没有保存优化后高斯或优化器状态。

## 复现

```bash
cd /home/han/linux-han/local-gs-eval
git fetch --tags -f origin
git switch -c experiment/mofang-9cam-round13-gspl-20261026-local linux-3090-round13
export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH
export LGS_WORK_DIR=work/round13 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1
mkdir -p "$LGS_WORK_DIR"
cp -a --reflink=auto work/round7/{prepare,flow,poses,tokens,compat_packages} "$LGS_WORK_DIR"/
python -m unittest discover -s tests -v
python scripts/run_anysplat.py --config configs/mofang_9cam_lean.yaml
python scripts/evaluate.py --config configs/mofang_9cam_lean.yaml
python scripts/validate_results.py configs/mofang_9cam_lean.yaml
```

本次评估实际使用本目录的 `evaluate_parallel.py` 与 `evaluate_worker.py` 按相机组合并行；标准顺序命令调用同一原始评估程序。
