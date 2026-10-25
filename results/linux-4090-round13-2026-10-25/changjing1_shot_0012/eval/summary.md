# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 20.5% | 25.67 / 0.0215 | 22.19 / 0.0556 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 22.4% | 25.85 / 0.0227 | 23.55 / 0.0489 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 21.3% | 25.75 / 0.0220 | 23.34 / 0.0495 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 21.7% | 25.80 / 0.0220 | 23.55 / 0.0487 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_local | 12.6% | 25.96 / 0.0210 | 21.21 / 0.0564 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | 13.5% | 25.98 / 0.0226 | 22.83 / 0.0489 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | 13.0% | 25.96 / 0.0213 | 22.28 / 0.0488 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | 13.2% | 25.96 / 0.0218 | 22.57 / 0.0482 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_local | 10.3% | 23.63 / 0.0141 | 19.74 / 0.0281 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | 11.1% | 23.87 / 0.0150 | 20.18 / 0.0300 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | 10.7% | 23.78 / 0.0142 | 20.10 / 0.0279 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | 10.9% | 23.86 / 0.0142 | 20.27 / 0.0277 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.76 / 0.0513 | 26.59 / 0.0712 | 19.75 / 0.0167 | 29.67 / 0.0267 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.46 / 0.0790 | 23.97 / 0.1358 | 18.89 / 0.0210 | 29.01 / 0.0321 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.09 / 0.0695 | 24.94 / 0.1108 | 19.97 / 0.0176 | 29.05 / 0.0314 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.02 / 0.0744 | 24.85 / 0.1230 | 19.62 / 0.0191 | 29.12 / 0.0317 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.07 / 0.0720 | 24.89 / 0.1191 | 19.80 / 0.0182 | 29.09 / 0.0316 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 26.80 / 0.0694 | 23.79 / 0.1435 | 19.21 / 0.0201 | 29.05 / 0.0305 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.18 / 0.0638 | 24.66 / 0.1153 | 19.90 / 0.0175 | 29.08 / 0.0305 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.17 / 0.0666 | 24.44 / 0.1314 | 19.75 / 0.0186 | 29.13 / 0.0301 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.20 / 0.0651 | 24.55 / 0.1270 | 19.86 / 0.0178 | 29.12 / 0.0301 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 27.36 / 0.0609 | 25.76 / 0.1012 | 19.58 / 0.0187 | 29.32 / 0.0289 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 27.36 / 0.0596 | 25.83 / 0.0876 | 19.73 / 0.0179 | 29.25 / 0.0292 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 27.38 / 0.0605 | 25.93 / 0.0930 | 19.68 / 0.0183 | 29.30 / 0.0290 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 27.39 / 0.0602 | 25.89 / 0.0913 | 19.72 / 0.0181 | 29.28 / 0.0291 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.3%） | — | — | 27.76 / 0.0513 | 26.59 / 0.0712 | 29.67 |
| in035 | rife | 11.8% | 20.5% | 26.46 / 0.0790 | 23.97 / 0.1358 | 29.01 |
| in035 | rife_w30 | 6.9% | 12.6% | 26.80 / 0.0694 | 23.79 / 0.1435 | 29.05 |
| in035 | rife_w40 | 3.2% | 6.9% | 27.36 / 0.0609 | 25.76 / 0.1012 | 29.32 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | rife_w30 | rife_w40 | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.51 / 0.0569 | — | -1.15 / +0.0298 (core 12.6%) | -0.78 / +0.0186 (core 8.7%) | +0.03 / +0.0108 (core 4.9%) | — | — | — |
| in035 | 2 | 0-3 | 27.39 / 0.0519 | — | -1.87 / +0.0361 (core 12.6%) | -1.43 / +0.0271 (core 8.7%) | -1.20 / +0.0180 (core 4.9%) | — | — | — |
| in035 | 4 | 3-5 | 29.38 / 0.0452 | — | -0.88 / +0.0172 (core 6.3%) | -0.67 / +0.0086 (core 1.8%) | +0.00 / +0.0000 (core 0.0%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.76 / 0.0513 | 26.59 | 29.67 | — |
| in035 | rife | 不复核 | —% | 26.46 / 0.0790 | 23.97 | 29.01 | 0/3 |
| in035 | rife | oracle | 3.5% | 27.28 / 0.0583 | 25.10 | 29.61 | 0/3 |
| in035 | rife | 不复核 | —% | 27.09 / 0.0695 | 24.94 | 29.05 | 0/3 |
| in035 | rife | oracle | 3.7% | 27.75 / 0.0536 | 26.16 | 29.61 | 0/3 |
| in035 | rife | 不复核 | —% | 27.02 / 0.0744 | 24.85 | 29.12 | 0/3 |
| in035 | rife | oracle | 3.6% | 27.64 / 0.0560 | 25.95 | 29.61 | 0/3 |
| in035 | rife | 不复核 | —% | 27.07 / 0.0720 | 24.89 | 29.09 | 0/3 |
| in035 | rife | oracle | 3.6% | 27.70 / 0.0548 | 26.08 | 29.61 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 26.80 / 0.0694 | 23.79 | 29.05 | 0/3 |
| in035 | rife_w30 | oracle | 2.5% | 27.48 / 0.0561 | 25.43 | 29.61 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 27.18 / 0.0638 | 24.66 | 29.08 | 0/3 |
| in035 | rife_w30 | oracle | 2.6% | 27.76 / 0.0527 | 26.32 | 29.61 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 27.17 / 0.0666 | 24.44 | 29.13 | 0/3 |
| in035 | rife_w30 | oracle | 2.5% | 27.72 / 0.0544 | 26.10 | 29.61 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 27.20 / 0.0651 | 24.55 | 29.12 | 0/3 |
| in035 | rife_w30 | oracle | 2.5% | 27.76 / 0.0533 | 26.25 | 29.61 | 0/3 |
| in035 | rife_w40 | 不复核 | —% | 27.36 / 0.0609 | 25.76 | 29.32 | 1/3 |
| in035 | rife_w40 | oracle | 1.5% | 27.61 / 0.0540 | 26.39 | 29.61 | 1/3 |
| in035 | rife_w40 | 不复核 | —% | 27.36 / 0.0596 | 25.83 | 29.25 | 1/3 |
| in035 | rife_w40 | oracle | 1.5% | 27.68 / 0.0528 | 26.47 | 29.61 | 1/3 |
| in035 | rife_w40 | 不复核 | —% | 27.38 / 0.0605 | 25.93 | 29.30 | 1/3 |
| in035 | rife_w40 | oracle | 1.5% | 27.67 / 0.0532 | 26.53 | 29.61 | 1/3 |
| in035 | rife_w40 | 不复核 | —% | 27.39 / 0.0602 | 25.89 | 29.28 | 1/3 |
| in035 | rife_w40 | oracle | 1.5% | 27.68 / 0.0530 | 26.51 | 29.61 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.76 / 0.0513 | 26.59 / 0.0712 | — |
| in035 | FF | 0（前馈） | 1285×861（62%） | 26.81 | 26.46 / 0.0790 | 23.97 / 0.1358 | 0/3 |
| in035 | 25 | 1.20 s | 1285×861（62%） | 27.78 | 27.02 / 0.0744 | 24.85 / 0.1230 | 0/3 |
| in035 | 50 | 2.36 s | 1285×861（62%） | 28.20 | 27.07 / 0.0720 | 24.89 / 0.1191 | 0/3 |
| in035 | 100 | 4.69 s | 1285×861（62%） | 28.60 | 27.09 / 0.0695 | 24.94 / 0.1108 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.76 / 0.0513 | 26.59 / 0.0712 | 29.67 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 26.46 / 0.0790 | 23.97 / 0.1358 | 29.01 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.28 / 0.0583 | 25.10 / 0.0884 | 29.61 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.02 / 0.0744 | 24.85 / 0.1230 | 29.12 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.64 / 0.0560 | 25.95 / 0.0782 | 29.61 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.07 / 0.0720 | 24.89 / 0.1191 | 29.09 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.70 / 0.0548 | 26.08 / 0.0753 | 29.61 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.09 / 0.0695 | 24.94 / 0.1108 | 29.05 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.75 / 0.0536 | 26.16 / 0.0717 | 29.61 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | 直接 | 26.80 / 0.0694 | 23.79 / 0.1435 | 29.05 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | oracle | 27.48 / 0.0561 | 25.43 / 0.0853 | 29.61 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | 直接 | 27.17 / 0.0666 | 24.44 / 0.1314 | 29.13 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | oracle | 27.72 / 0.0544 | 26.10 / 0.0754 | 29.61 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | 直接 | 27.20 / 0.0651 | 24.55 / 0.1270 | 29.12 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | oracle | 27.76 / 0.0533 | 26.25 / 0.0723 | 29.61 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | 直接 | 27.18 / 0.0638 | 24.66 / 0.1153 | 29.08 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | oracle | 27.76 / 0.0527 | 26.32 / 0.0695 | 29.61 | 0/3 |
| in035 | rife_w40 | GS 前馈颜色 | 直接 | 27.36 / 0.0609 | 25.76 / 0.1012 | 29.32 | 1/3 |
| in035 | rife_w40 | GS 前馈颜色 | oracle | 27.61 / 0.0540 | 26.39 / 0.0774 | 29.61 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | 直接 | 27.38 / 0.0605 | 25.93 / 0.0930 | 29.30 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | oracle | 27.67 / 0.0532 | 26.53 / 0.0704 | 29.61 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | 直接 | 27.39 / 0.0602 | 25.89 / 0.0913 | 29.28 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | oracle | 27.68 / 0.0530 | 26.51 / 0.0691 | 29.61 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | 直接 | 27.36 / 0.0596 | 25.83 / 0.0876 | 29.25 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | oracle | 27.68 / 0.0528 | 26.47 / 0.0676 | 29.61 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 / 0.0712 | 19.75 / 0.0167 | 29.67 / 0.0267 | 27.76 / 0.0513 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 6.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.7493 | 0.0712 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 19.06 | 0.7091 | 0.2082 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 21.23 | 0.7364 | 0.1577 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 19.93 | 0.7341 | 0.1865 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.52 | 0.7367 | 0.1739 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 18.09 | 0.6772 | 0.2467 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 19.32 | 0.7076 | 0.1927 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 18.54 | 0.7011 | 0.2277 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 18.73 | 0.7031 | 0.2150 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 15.08 | 0.4575 | 0.3304 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 15.50 | 0.4685 | 0.2918 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 15.27 | 0.4694 | 0.3156 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 15.34 | 0.4699 | 0.3059 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.10 | 0.7587 | 0.0884 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.16 | 0.7727 | 0.0717 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.95 | 0.7699 | 0.0782 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.08 | 0.7723 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 25.43 | 0.7596 | 0.0853 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 26.32 | 0.7724 | 0.0695 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 26.10 | 0.7695 | 0.0754 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.25 | 0.7718 | 0.0723 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 26.39 | 0.7605 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.47 | 0.7661 | 0.0676 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.53 | 0.7649 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.51 | 0.7659 | 0.0691 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.97 | 0.7425 | 0.1358 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.94 | 0.7599 | 0.1108 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.85 | 0.7616 | 0.1230 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.89 | 0.7621 | 0.1191 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 23.79 | 0.7266 | 0.1435 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 24.66 | 0.7454 | 0.1153 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.44 | 0.7417 | 0.1314 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 24.55 | 0.7436 | 0.1270 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 25.76 | 0.7520 | 0.1012 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.83 | 0.7590 | 0.0876 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.93 | 0.7596 | 0.0930 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.89 | 0.7600 | 0.0913 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.75 | 0.6007 | 0.0167 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.07 | 0.4418 | 0.0702 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.36 | 0.4931 | 0.0641 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.21 | 0.4796 | 0.0672 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.26 | 0.4861 | 0.0658 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 7.14 | 0.3517 | 0.0952 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 7.32 | 0.3960 | 0.0900 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 7.23 | 0.3847 | 0.0927 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 7.27 | 0.3905 | 0.0914 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 7.93 | 0.2555 | 0.0969 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 8.06 | 0.2800 | 0.0935 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 7.99 | 0.2741 | 0.0958 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 8.02 | 0.2770 | 0.0948 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.91 | 0.6088 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.98 | 0.6516 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.64 | 0.6388 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.81 | 0.6458 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 19.23 | 0.6079 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 19.93 | 0.6404 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 19.77 | 0.6311 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 19.88 | 0.6359 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 19.60 | 0.6103 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 19.74 | 0.6197 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 19.70 | 0.6171 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 19.73 | 0.6180 | 0.0179 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.89 | 0.6065 | 0.0210 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.97 | 0.6496 | 0.0176 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.62 | 0.6373 | 0.0191 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.80 | 0.6443 | 0.0182 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 19.21 | 0.6062 | 0.0201 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 19.90 | 0.6391 | 0.0175 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 19.75 | 0.6300 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 19.86 | 0.6350 | 0.0178 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 19.58 | 0.6085 | 0.0187 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 19.73 | 0.6188 | 0.0179 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 19.68 | 0.6158 | 0.0183 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 19.72 | 0.6172 | 0.0181 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 45.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.7718 | 0.0287 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.58 | 0.5312 | 0.2289 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.86 | 0.5551 | 0.2081 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.66 | 0.5549 | 0.2203 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.73 | 0.5563 | 0.2150 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 5.93 | 0.4685 | 0.2710 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 6.09 | 0.4855 | 0.2579 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 5.98 | 0.4866 | 0.2650 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 6.02 | 0.4873 | 0.2618 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 7.12 | 0.3096 | 0.2783 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 7.24 | 0.3184 | 0.2704 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 7.16 | 0.3203 | 0.2751 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 7.19 | 0.3204 | 0.2729 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.74 | 0.7678 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.56 | 0.7775 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.32 | 0.7755 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.45 | 0.7769 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 26.10 | 0.7698 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 26.58 | 0.7763 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 26.51 | 0.7754 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.58 | 0.7763 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 26.38 | 0.7716 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.49 | 0.7734 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.46 | 0.7735 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.49 | 0.7736 | 0.0308 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.41 | 0.7482 | 0.0562 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.20 | 0.7597 | 0.0508 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.20 | 0.7638 | 0.0523 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.28 | 0.7636 | 0.0509 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 24.97 | 0.7574 | 0.0466 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.50 | 0.7648 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.51 | 0.7669 | 0.0438 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.57 | 0.7670 | 0.0423 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 25.86 | 0.7686 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.89 | 0.7695 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.91 | 0.7716 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.94 | 0.7714 | 0.0371 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 53.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.98 | 0.7281 | 0.0352 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.32 | 0.4734 | 0.2819 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.49 | 0.4957 | 0.2633 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.37 | 0.4962 | 0.2736 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.41 | 0.4975 | 0.2689 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 4.90 | 0.4082 | 0.3242 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 4.99 | 0.4261 | 0.3104 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 4.94 | 0.4267 | 0.3184 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 4.96 | 0.4275 | 0.3147 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 6.93 | 0.2769 | 0.3128 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 7.00 | 0.2878 | 0.3045 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 6.96 | 0.2880 | 0.3098 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 6.98 | 0.2886 | 0.3074 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.51 | 0.7261 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.24 | 0.7344 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.06 | 0.7326 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.16 | 0.7339 | 0.0385 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 26.81 | 0.7275 | 0.0399 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.25 | 0.7335 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.19 | 0.7323 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.25 | 0.7331 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 27.02 | 0.7295 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 27.12 | 0.7317 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 27.10 | 0.7313 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 27.12 | 0.7316 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.45 | 0.7132 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.40 | 0.7263 | 0.0511 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.24 | 0.7270 | 0.0557 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.35 | 0.7279 | 0.0533 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 25.90 | 0.7183 | 0.0521 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 26.49 | 0.7268 | 0.0466 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 26.44 | 0.7268 | 0.0494 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.50 | 0.7274 | 0.0479 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 26.75 | 0.7272 | 0.0435 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.75 | 0.7294 | 0.0424 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.76 | 0.7298 | 0.0434 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.78 | 0.7299 | 0.0431 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.67 | 0.7076 | 0.0267 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.91 | 0.3691 | 0.2665 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.02 | 0.3765 | 0.2560 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.95 | 0.3801 | 0.2622 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.98 | 0.3794 | 0.2593 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 3.14 | 0.3192 | 0.3023 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 3.21 | 0.3237 | 0.2958 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 3.18 | 0.3271 | 0.2994 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 3.19 | 0.3263 | 0.2975 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 5.58 | 0.2081 | 0.2961 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 5.61 | 0.2100 | 0.2919 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 5.60 | 0.2120 | 0.2944 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 5.61 | 0.2115 | 0.2932 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.61 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.61 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.61 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 29.61 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 29.61 | 0.7072 | 0.0270 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.01 | 0.7047 | 0.0321 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.05 | 0.7052 | 0.0314 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.12 | 0.7062 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.09 | 0.7059 | 0.0316 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 29.05 | 0.7046 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.08 | 0.7047 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.13 | 0.7054 | 0.0301 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.12 | 0.7053 | 0.0301 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 29.32 | 0.7063 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 29.25 | 0.7058 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.30 | 0.7063 | 0.0290 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 29.28 | 0.7062 | 0.0291 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.76 | 0.7224 | 0.0513 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.03 | 0.4266 | 0.3477 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.15 | 0.4414 | 0.3229 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.07 | 0.4435 | 0.3364 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.10 | 0.4438 | 0.3299 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 4.08 | 0.3735 | 0.3915 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 4.15 | 0.3846 | 0.3727 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 4.12 | 0.3867 | 0.3833 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 4.13 | 0.3866 | 0.3781 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 6.22 | 0.2515 | 0.4037 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 6.27 | 0.2580 | 0.3911 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 6.25 | 0.2593 | 0.3990 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 6.26 | 0.2593 | 0.3953 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.28 | 0.7204 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.75 | 0.7249 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.64 | 0.7241 | 0.0560 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.70 | 0.7247 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 27.48 | 0.7213 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.76 | 0.7245 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.72 | 0.7239 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.76 | 0.7243 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 27.61 | 0.7224 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 27.68 | 0.7235 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 27.67 | 0.7234 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 27.68 | 0.7235 | 0.0530 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.46 | 0.7127 | 0.0790 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.09 | 0.7198 | 0.0695 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.02 | 0.7208 | 0.0744 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.07 | 0.7210 | 0.0720 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 26.80 | 0.7157 | 0.0694 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.18 | 0.7202 | 0.0638 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.17 | 0.7207 | 0.0666 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.20 | 0.7209 | 0.0651 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 27.36 | 0.7208 | 0.0609 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 27.36 | 0.7218 | 0.0596 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 27.38 | 0.7224 | 0.0605 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 27.39 | 0.7224 | 0.0602 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|

## 风险阈值扫描（风险区 vs oracle_fail，按 IoU 排序，前 8 名与配置默认值）

| 设置 | warp 阈值 | col 阈值 | 精确率 | 召回率 | IoU | 面积比 |
|---|---:|---:|---:|---:|---:|---:|

## t 估计对比（scale=1.0）

| 设置 | 目标相机 | t_uniform | t_pose (VGGT) | t_posecal (标定) | t_oracle |
|---|---:|---:|---:|---:|---:|
| in035 | 1 | — | 0.357 | — | — |
| in035 | 2 | — | 0.688 | — | — |
| in035 | 4 | — | 0.481 | — | — |

## AnySplat 运行统计

旋转/光心误差：vggt 行是联合估计与输入视点估计的一致性；calib/calibK 行是标定位姿经 Sim(3) 对齐到AnySplat 输入视点位姿后的残差（反映 AnySplat 自身预测的输入相机几何与真实阵列的偏差）。

| 设置 | 变体 | 位姿来源 | 窗口边长 | 渲染分辨率 | 模式 | eps2d | 3D 滤波 | 高斯数 | 编码 s | 渲染 ms/视点 | 输入视点自渲染 PSNR | 最大旋转误差° | 最大光心误差/基线 |
|---|---|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 38.6 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 37.8 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 41.1 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 36.0 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w30448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 33.7 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 37.8 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 36.9 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 41.1 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w40448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 32.1 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 26.9 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 33.2 | 29.69 | 0.26 | 0.013 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 250656 | 0.321 | 25.4 | 29.69 | 0.26 | 0.013 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.783 | 0.023 |
| in035 | mask_ent | 0.691 | 0.023 |
| in035 | mask_grad | 0.508 | 0.023 |
| in035 | r_col | 0.824 | 0.023 |
| in035 | r_warp | 0.892 | 0.023 |
