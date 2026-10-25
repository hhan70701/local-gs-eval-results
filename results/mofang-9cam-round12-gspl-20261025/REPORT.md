# 第十二轮：3090 上精简流程与逐视图裁剪 TTO 实测

源代码标签 [`linux-3090-round12`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round12)，提交 `aed2679360ff1c73ccf5dfcdc115be11e2dbab6d`。使用 `gspl`、RTX 3090、`configs/mofang_9cam_lean.yaml`。准备数据、光流、位姿、token 与兼容包的 1271 个文件逐个 SHA256 与第七轮一致；GS/TTO 和评估本轮重新执行。

## 结论

逐视图裁剪与只训练 rife 区域使 200 步累计优化时间从第十一轮的 cam3 14.108 秒、cam5 24.536 秒降到本轮 9.667 秒、12.111 秒。两项改动同时存在，因此这个差不能归因于裁剪框单一因素。cam3 的质量维持；cam5 在 200 步的质量下降，主要体现在目标 3，前景 PSNR 相对第十一轮同检查点下降约 3.07 dB。

按既定判据（两组前景均值 PSNR≥纯光流、LPIPS≤纯光流，且不差视点数至少达到第十轮 6/6 与 3/4），本轮 **50/100/200 步均未达标**：cam5 各为 2/4。当前固定预设中，cam5 的 50 步前景平均 PSNR 最高，不能据此宣称其 4 个视点都获益。

## 主质量与时间

固定 `rife`、`_al`、直接贴回。PSNR 单位 dB，LPIPS 越小越好；每组各留出视点等权平均。累计 TTO 时间经过 CUDA 同步，排除编码、目标渲染及评估；第十一轮同检查点数据来自已归档原始 CSV/日志。

| 设置 | 步数 | 本轮 TTO 秒 | 本轮前景 PSNR / LPIPS | 第十一轮前景 PSNR / LPIPS | 本轮物体 PSNR / LPIPS | 本轮不差目标 |
|---|---:|---:|---:|---:|---:|---:|
| cam3 | FF | 0.000 | 26.399 / 0.05362 | 26.373 / 0.05356 | 17.455 / 0.16342 | 4/6 |
| cam3 | 50 | 2.405 | 27.086 / 0.04894 | 27.101 / 0.04870 | 18.777 / 0.11876 | 6/6 |
| cam3 | 100 | 4.811 | 27.288 / 0.04655 | 27.295 / 0.04648 | 19.748 / 0.09589 | 6/6 |
| cam3 | 200 | 9.667 | 27.350 / 0.04583 | 27.334 / 0.04602 | 20.123 / 0.08985 | 6/6 |
| cam5 | FF | 0.000 | 27.759 / 0.04193 | 27.690 / 0.04194 | 20.158 / 0.09216 | 0/4 |
| cam5 | 50 | 3.024 | 29.042 / 0.03882 | 28.962 / 0.03893 | 22.235 / 0.07076 | 2/4 |
| cam5 | 100 | 6.041 | 28.985 / 0.03817 | 29.097 / 0.03784 | 22.206 / 0.06217 | 2/4 |
| cam5 | 200 | 12.111 | 28.349 / 0.03865 | 29.149 / 0.03817 | 21.094 / 0.05978 | 2/4 |

纯光流基线：cam3 前景 22.604 / 0.062884，cam5 前景 28.000 / 0.039572。FF 行的 0 秒仅表示没有 TTO，编码与渲染仍耗时。cam3 在 50 步达 6/6；cam5 的 50 步、100 步与 200 步均只有 2/4。

## 监督范围与速度

| 设置 | 训练高斯数 | 监督图边长 | 本轮视图平均面积 | 上轮共框面积 | 本轮 50 / 100 / 200 步秒 | 上轮 50 / 100 / 200 步秒 |
|---|---:|---:|---:|---:|---|---|
| cam3 | 53588（上轮 143439） | 911 | 60.90% | 96.38% | 2.405 / 4.811 / 9.667 | 3.479 / 6.999 / 14.108 |
| cam5 | 47283（上轮 207208） | 917 | 35.16% | 91.49% | 3.024 / 6.041 / 12.111 | 6.036 / 12.133 / 24.536 |

逐视图 `(x,y,w,h)`、每步时间及输入视点拟合度见 `eval/tto_supervision_boxes.csv`、`eval/tto_checkpoint_timing.csv` 和 `eval/tto_training.csv`。各视图分别光栅化；监督面积为各视图占原裁剪面积比例的均值。不同监督范围与训练高斯集合会改变优化轨迹。输入 PSNR 在各自监督框内测得，不能跨轮直接当成同一像素集的质量比较。

## cam5 目标 3 的退化

| 步数 | 本轮前景 PSNR | 第十一轮前景 PSNR | 差值 | 本轮 LPIPS | 第十一轮 LPIPS |
|---:|---:|---:|---:|---:|---:|
| 50 | 34.036 | 33.837 | +0.198 | 0.02243 | 0.02324 |
| 100 | 33.699 | 34.320 | -0.621 | 0.02160 | 0.02152 |
| 200 | 31.417 | 34.488 | -3.071 | 0.02250 | 0.02145 |

[cam5 目标 3 固定检查点对比图](figures/cam5/cam3_rife_checkpoints.png) 同时展示真值、光流、FF、50/100/200 步；图是视觉辅助，数值以原始逐视点 CSV 为准。各目标对比图在 `figures/`。上游 `eval/summary.md` 的“TTO 第十一轮”标题是标签中沿用的旧文案，这里的数据由本轮结果生成。上游拼图会按真值挑局部变体，仅作诊断；固定方法比较以本报告及固定检查点图为准。

## 执行与验证

- 上游 17 项单元测试通过。`validate_results.py`：`PASS`，13 种方法、780 行指标、50 行 AUC，警告 []。
- cam3、cam5 在 GS/TTO 全部完成后分别运行原版 `evaluate.main()`，输入只读共享，原始七份 CSV 逐行等于两组工作输出按固定顺序拼接；见 `eval/parallel_merge_validation.json`。
- 第七轮的 1271 个复用文件以 SHA256 逐个核对；清单见 `reused_files_manifest.json`。
- 本轮 TTO 在标签原代码上运行，没有修改优化或指标算法。两个独立评估进程只影响评估完成的墙钟时间，不影响事先记录的 TTO 时间。
- 仓库没有保存优化后的高斯参数或优化器状态；`work/round12/gs` 留有渲染 RGB/alpha，上传仅包含评估、图、元数据、日志和复现脚本。原始数据与权重需在本机自行提供。
- 未记录 GS 开始到评估结束的精确墙钟时间，因此不能验证 README 所说的“十几分钟”端到端目标。

## 复现

```bash
cd /home/han/linux-han/local-gs-eval
git fetch --tags -f origin
git switch -c experiment/mofang-9cam-round12-gspl-20261025 linux-3090-round12
export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH
export LGS_WORK_DIR=work/round12 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1
mkdir -p "$LGS_WORK_DIR"
cp -a --reflink=auto work/round7/{prepare,flow,poses,tokens,compat_packages} "$LGS_WORK_DIR"/
python -m unittest discover -s tests -v
python scripts/run_anysplat.py --config configs/mofang_9cam_lean.yaml
python scripts/evaluate.py --config configs/mofang_9cam_lean.yaml
python scripts/validate_results.py configs/mofang_9cam_lean.yaml
```

本次评估实际用 `evaluate_parallel.py` 与 `evaluate_worker.py` 按 cam3/cam5 并行；标准顺序命令也会调用同一个评估程序。完整结果、逐视点 CSV、监督框、日志与第十一轮归档随新分支保存。
