# 本机环境安装记录

## 使用方式

```bash
source /home/sang-usb/miniconda3/etc/profile.d/conda.sh
conda activate gspl
cd /home/sang-usb/linux-han/local-gs-eval
```

环境激活后自动设置 `LGS_DATA_ROOT=/home/sang-usb/linux-han`，覆盖仓库配置中的旧主机路径。

## 版本

- Python 3.10.22
- torch 2.2.0+cu121 / torchvision 0.17.0+cu121
- CUDA runtime 12.1 / NVIDIA RTX 4090 / 驱动 580.178.04
- gsplat 1.4.0+pt22cu121
- xformers 0.0.24
- torch_scatter 2.1.2+pt22cu121
- NumPy 1.25.0 / e3nn 0.5.6

按照主仓库 README 的新主机环境要求安装 AnySplat 依赖，使用预编译 CUDA 扩展。
PyTorch3D 未安装：README 说明本实验不调用它，可跳过；不适用于需要该库的 AnySplat 其他功能。
e3nn 固定为 README 中说明与旧版 torch 兼容的 0.5.6，所有安装都使用 constraints.txt 保护 torch 版本。
Conda 环境使用 conda-forge 创建；大文件使用国内镜像下载，未修改全局 pip/conda 源配置。

## 已验证

- 项目自带 17 项单元测试全部通过（unit-tests.log）。
- torch 在 RTX 4090 上可用。
- gsplat GPU 渲染及梯度计算通过（gpu-check.log）。
- xformers GPU 注意力及梯度计算通过（gpu-check.log）。
- torch_scatter GPU 计算及梯度计算通过（scatter-check.log）。
- pip 依赖一致性检查通过（pip-check.log）。
- AnySplat 模型类及位姿解码器导入通过（anysplat-import.log）。

AnySplat 源码位于 `/home/sang-usb/linux-han/AnySplat`。可选的 RoPE2D CUDA 扩展未编译，
导入时提示自动使用 PyTorch 实现；运行速度尚未做完整模型实测。

完整版本清单见 requirements-lock.txt 和 environment.yml，安装过程见本目录各 log 文件。

## 实验状态

用户已授权运行六路数据集实验。主仓库更新至标签 `linux-4090-dataset6` 对应的
`af66f0f2d861dcec902100027213030d5b86a451`，使用 `configs/dataset6_lean.yaml`。
AnySplat、VGGT-1B 和 LPIPS/AlexNet 权重已下载并通过 SHA-256 校验。
用户拷入的 `train_log/` 和 `model/` 通过 `Practical-RIFE/` 内的软链接提供给实验，未替换网络或权重版本。

拷入的数据缺少 `homographies_cam3_raw2304_to_crop1920x1088_halfpx.npy`，用户明确授权从现有矩阵生成。
新矩阵采用 `T(-0.5, -0.5) @ H_existing[i]`，即裁剪起点 `(192.5, 104.5)`，
六路统一，原文件保留；cam3 双线性重采样验证通过。详细记录见 `halfpx-generation.json`。

输出目录为 `work/dataset6/`，总日志为 `work/dataset6_run.log`，启动器状态为 `work/dataset6_run_status.json`。
各场景按 prepare → tokens → anysplat → flow → evaluate → validate 运行。

本次五组场景已全部完成，启动器退出码为 0，五份 validation.json 均为 PASS 且无警告，
15 张目标视点对比图齐全。正式计算耗时约 289 秒（不含权重下载）。
总汇总为 `work/dataset6/summary_all.md`，完整性记录为 `work/dataset6/completion_check.json`。
