# linux-4090：六路数据集实验结果（2026-10-25）

代码：[luckyhan-mike/local-gs-eval](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-4090-dataset6)，标签 `linux-4090-dataset6`，提交 `af66f0f2d861dcec902100027213030d5b86a451`。

使用 `configs/dataset6_lean.yaml`：输入相机 0/3/5，目标相机 1/2/4；5 组场景，共 15 个目标视点。使用仓库默认参数完成 prepare → tokens → AnySplat（含 TTO 50/100/200 步）→ flow → evaluate → validate。

## 结果与验证

完整结果见 [summary_all.md](summary_all.md)，运行日志见 [dataset6_run.log](dataset6_run.log)。
五组验证均为 PASS、无验证警告；15 张目标视点主对比图齐全。正式流程耗时 288.56 秒，不含环境安装和模型权重下载。

| 方法 | 前景 PSNR ↑ | 前景 LPIPS ↓ | 两项指标均不差于纯光流的目标数 |
|---|---:|---:|---:|
| 纯光流 | 25.30 | 0.0974 | — |
| 前馈直接贴回 | 25.18 | 0.1412 | 0/15 |
| TTO 50 步直接贴回 | 25.69 | 0.1270 | 0/15 |
| TTO 100 步直接贴回 | 25.62 | 0.1248 | 1/15 |
| TTO 200 步直接贴回 | 25.31 | 0.1239 | 1/15 |
| TTO 200 步 oracle | 26.13 | 0.0911 | 8/15 |

本次直接贴回方案未稳定优于纯光流。Oracle 使用真值失败区，仅为诊断上限。TTO 200 步耗时约 4.43–6.27 秒/场景；前馈编码约 0.32 秒/场景。

## 环境和数据说明

- RTX 4090，驱动 580.178.04，Python 3.10.22，torch 2.2.0+cu121，gsplat 1.4.0+pt22cu121，xformers 0.0.24。
- AnySplat 提交 `5f5e208a7dd57d52e43ea0d553a95eab526e8775`；使用用户提供的同版本 RIFE 网络和权重。
- PyTorch3D 按实验 README 跳过；可选 RoPE2D CUDA 扩展未编译，使用 AnySplat 的 PyTorch 实现。
- 用户拷入的数据缺少新版 halfpx 矩阵，经用户明确授权从已有矩阵生成：`H_halfpx[i] = T(-0.5,-0.5) @ H_existing[i]`。即六路统一使用裁剪起点 `(192.5,104.5)`；原矩阵保留，cam3 双线性重采样检查通过。
- 两份矩阵位于 `calibration/`，生成记录见 [environment/halfpx-generation.json](environment/halfpx-generation.json)。源码版本、模型权重和输入文件哈希见 [environment_and_inputs.json](environment_and_inputs.json)。

## 文件内容

每个场景包含配置、耗时、poses、logs、完整 eval（指标和对比图）、prepare/prepare.json、tokens/tokens.json，以及 GS 各阶段 meta.json。环境依赖、测试日志和 GPU 检查记录位于 `environment/`。

不包含原始数据、模型权重、aligned/flow/gs 大图。本目录仅包含本次 linux-4090 六路实验结果。
