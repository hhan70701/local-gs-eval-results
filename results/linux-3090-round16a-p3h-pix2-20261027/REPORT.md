# linux-3090 第十六轮 a：p3h / pix2 修补对比

源码标签 [`linux-3090-round16a-p3h-pix2`](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-3090-round16a-p3h-pix2)，提交 `34ee4649f2a76980c36d0d600a6ddf3b93a70296`。复用第十五轮本机 `work/dataset6` 的预处理、token、光流和 AnySplat 输出，仅补本轮变体、重新评估与验证。23 组场景、69 个留出视点。

下表均在同一批目标和 `cnw_cnn` token 区比较。`direct` 为实际无真值贴回；`oracle` 用目标真值圈定失败区域，只是上限诊断。“不差”要求单目标的 fg PSNR 不低于且 LPIPS 不高于纯光流。

## 全部 69 个留出视点

纯光流 fg 均值：27.294 dB / 0.06349 LPIPS。

| 方法 | direct fg PSNR / LPIPS | direct 不差 | oracle fg PSNR / LPIPS | oracle 不差 |
|---|---:|---:|---:|---:|
| cnw_cnn_pix | 27.044 / 0.07877 | 0/69 | 27.499 / 0.06810 | 2/69 |
| cnw_cnn_mw_tto100 | 27.294 / 0.07396 | 0/69 | 27.706 / 0.06349 | 26/69 |
| cnw_cnn_p3h_fsl | 27.263 / 0.07841 | 0/69 | 27.643 / 0.07004 | 3/69 |
| cnw_cnn_p3h_fsl_g | 27.233 / 0.07368 | 0/69 | 27.569 / 0.06898 | 2/69 |
| cnw_cnn_p3h_fss | 27.018 / 0.08024 | 0/69 | 27.490 / 0.07092 | 1/69 |
| cnw_cnn_p3h_fss_g | 27.016 / 0.07512 | 0/69 | 27.433 / 0.06967 | 5/69 |
| cnw_cnn_p3h_flw | 26.949 / 0.08235 | 0/69 | 27.234 / 0.07574 | 0/69 |
| cnw_cnn_pix2_fsl | 27.113 / 0.07659 | 0/69 | 27.556 / 0.06789 | 4/69 |
| cnw_cnn_pix2_fsl_g | 27.105 / 0.07221 | 0/69 | 27.502 / 0.06724 | 4/69 |
| cnw_cnn_pix2_fss | 26.879 / 0.07831 | 0/69 | 27.417 / 0.06904 | 2/69 |
| cnw_cnn_pix2_fss_g | 26.878 / 0.07390 | 0/69 | 27.371 / 0.06828 | 4/69 |
| cnw_cnn_pix2_flw | 26.985 / 0.07379 | 1/69 | 27.272 / 0.06816 | 8/69 |

结果解读：`pix2_fsl_g` 的直接贴回 LPIPS 低于旧版 `cnw_cnn_pix`，也低于同来源的 `p3h_fsl_g`；但其 PSNR 仍低于纯光流，两个指标同时不差的目标仍为 0/69。`pix2_fsl` 与 `p3h_fsl` 各有指标优势，不能只据平均 LPIPS 宣称高斯整体胜出。门控降低了多数变体的 LPIPS，却没有提升直接贴回的“不差目标数”。


## 第七轮试点场景（9 个留出视点）

这 3 组未用于 `cnw_cnn` 检测 CNN 训练，泛化判断以本表为主。

| 方法 | direct fg PSNR / LPIPS | direct 不差 | oracle fg PSNR / LPIPS | oracle 不差 |
|---|---:|---:|---:|---:|
| cnw_cnn_pix | 25.071 / 0.07536 | 0/9 | 25.440 / 0.06624 | 1/9 |
| cnw_cnn_mw_tto100 | 25.221 / 0.07116 | 0/9 | 25.533 / 0.06384 | 1/9 |
| cnw_cnn_p3h_fsl | 25.334 / 0.07507 | 0/9 | 25.703 / 0.06728 | 0/9 |
| cnw_cnn_p3h_fsl_g | 25.338 / 0.07037 | 0/9 | 25.626 / 0.06662 | 0/9 |
| cnw_cnn_p3h_fss | 25.159 / 0.07769 | 0/9 | 25.577 / 0.06870 | 0/9 |
| cnw_cnn_p3h_fss_g | 25.194 / 0.07263 | 0/9 | 25.527 / 0.06767 | 0/9 |
| cnw_cnn_p3h_flw | 24.916 / 0.08457 | 0/9 | 25.130 / 0.07734 | 0/9 |
| cnw_cnn_pix2_fsl | 25.116 / 0.07332 | 0/9 | 25.549 / 0.06618 | 0/9 |
| cnw_cnn_pix2_fsl_g | 25.142 / 0.06991 | 0/9 | 25.515 / 0.06557 | 0/9 |
| cnw_cnn_pix2_fss | 24.928 / 0.07532 | 0/9 | 25.434 / 0.06761 | 0/9 |
| cnw_cnn_pix2_fss_g | 24.970 / 0.07211 | 0/9 | 25.415 / 0.06694 | 0/9 |
| cnw_cnn_pix2_flw | 24.890 / 0.07486 | 0/9 | 25.122 / 0.06916 | 0/9 |

## 渲染耗时与对应覆盖

以下为每场景 meta 所记每视点渲染时间的中位数；其中渲染前处理按一对输入相机计时。`stereo_export_s` 来自 Windows RTX 3090 的离线位移导出，不属于本机推理耗时。逐目标记录见 `render_all.csv`。

| 变体 | 后端 | 每视点渲染中位数 | 每输入对准备中位数 | 最大核心空洞比例 |
|---|---|---:|---:|---:|
| p3h_fsl | splat | 49.3 ms | 304.3 ms | 0.00% |
| p3h_fsl_g | splat | 49.3 ms | 304.3 ms | 0.00% |
| p3h_fss | splat | 44.0 ms | 287.8 ms | 0.00% |
| p3h_fss_g | splat | 44.0 ms | 287.8 ms | 0.00% |
| p3h_flw | splat | 44.8 ms | 289.7 ms | 0.00% |
| pix2_fsl | gsplat | 195.5 ms | 290.7 ms | 1.91% |
| pix2_fsl_g | gsplat | 195.5 ms | 290.7 ms | 1.91% |
| pix2_fss | gsplat | 52.7 ms | 287.9 ms | 2.15% |
| pix2_fss_g | gsplat | 52.7 ms | 287.9 ms | 2.15% |
| pix2_flw | gsplat | 52.9 ms | 289.3 ms | 0.38% |

这张表来自逐场景仅 3 个目标的输出流程，包含每个进程首次调用的开销；`pix2_fsl` 恰好是每组的首次 gsplat 变体。下述密集计时先预热，在 GPU 上复用每对输入准备的数据、连续生成 41/60 个视点，二者的时间范围不同，不能直接比较其毫秒数。


密集视点（41/60）计时及时间范围见 [`bench_dense_linux-3090.md`](bench_dense_linux-3090.md)。

## 验证与复现

上游 24 项单元测试通过。23/23 组验证 PASS，共 44799 行指标、345 行 AUC，警告数 0。

首组按 README 顺序运行；其余组顺序执行 pixgs 生成，再以 3 个独立进程按场景执行源码评估与验证，最后重新汇总。计时文件合并保留两个阶段。本机原始图像、光流数组、渲染 RGB/alpha 和第十五轮工作目录保留在 `work/dataset6`；归档包括逐组指标、验证、日志、位姿和本轮十种变体的 meta。

```bash
cd /home/han/linux-han/local-gs-eval
git fetch --tags -f origin
git switch -c experiment/linux-3090-round16a-p3h-pix2-20261027 linux-3090-round16a-p3h-pix2
export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH
export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1
python -m unittest discover -s tests -v
# work/dataset6 需已有第十五轮本机 23 组结果
python scripts/run_scenes.py --config configs/dataset6_lean.yaml --host linux-3090 --steps pixgs evaluate validate
python scripts/bench_dense.py --config configs/dataset6_lean.yaml --host linux-3090 --views 41 60
```
