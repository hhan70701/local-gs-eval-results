# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_tokrife448_nat_dil_al_local | 11.2% | 14.62 / 0.0676 | 19.90 / 0.0500 | — | — |
| cam3 | gs_tokrife448_nat_dil_al_tto100_local | 11.6% | 14.87 / 0.0680 | 21.93 / 0.0369 | — | — |
| cam3 | gs_tokrife448_nat_dil_al_tto25_local | 11.2% | 14.66 / 0.0680 | 20.66 / 0.0436 | — | — |
| cam3 | gs_tokrife448_nat_dil_al_tto50_local | 11.3% | 14.76 / 0.0681 | 21.29 / 0.0407 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_local | 4.6% | 20.84 / 0.0659 | 18.81 / 0.1144 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_tto100_local | 5.0% | 20.88 / 0.0683 | 23.12 / 0.0776 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_tto25_local | 4.7% | 20.67 / 0.0673 | 20.53 / 0.0952 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_tto50_local | 4.8% | 20.75 / 0.0706 | 21.93 / 0.0867 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.33 / 0.0538 | 17.33 / 0.1662 | 17.77 / 0.0380 | 33.49 / 0.0236 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.04 / 0.0478 | 18.94 / 0.1149 | 18.62 / 0.0317 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.68 / 0.0509 | 17.79 / 0.1450 | 18.17 / 0.0350 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.87 / 0.0491 | 18.22 / 0.1311 | 18.41 / 0.0331 | 33.51 / 0.0234 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.72 / 0.0421 | 20.23 / 0.0919 | 17.94 / 0.0209 | 31.36 / 0.0312 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.97 / 0.0387 | 22.32 / 0.0682 | 19.80 / 0.0148 | 31.43 / 0.0312 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.39 / 0.0404 | 21.02 / 0.0823 | 18.85 / 0.0175 | 31.41 / 0.0311 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.73 / 0.0394 | 21.72 / 0.0775 | 19.35 / 0.0160 | 31.43 / 0.0311 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.2%） | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 |
| cam3 | rife | 10.8% | 11.2% | 26.33 / 0.0538 | 17.33 / 0.1662 | 33.49 |
| cam5 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.2%） | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 |
| cam5 | rife | 3.8% | 4.6% | 27.72 / 0.0421 | 20.23 / 0.0919 | 31.36 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| cam3 | 1 | 0-4 | 19.25 / 0.1012 | — | +4.58 / -0.0266 (core 14.5%) | — | — | — |
| cam3 | 2 | 0-4 | 20.14 / 0.0784 | — | +4.51 / -0.0216 (core 14.5%) | — | — | — |
| cam3 | 3 | 0-4 | 22.11 / 0.0577 | — | +5.73 / -0.0096 (core 14.5%) | — | — | — |
| cam3 | 5 | 4-8 | 25.45 / 0.0357 | — | +2.88 / +0.0013 (core 2.5%) | — | — | — |
| cam3 | 6 | 4-8 | 24.03 / 0.0518 | — | +3.45 / +0.0001 (core 2.5%) | — | — | — |
| cam3 | 7 | 4-8 | 24.65 / 0.0526 | — | +1.23 / +0.0021 (core 2.5%) | — | — | — |
| cam5 | 1 | 0-2 | 23.87 / 0.0592 | — | +0.96 / +0.0019 (core 5.9%) | — | — | — |
| cam5 | 3 | 2-4 | 32.61 / 0.0248 | — | -1.80 / +0.0045 (core 3.7%) | — | — | — |
| cam5 | 5 | 4-6 | 28.67 / 0.0315 | — | -0.25 / +0.0015 (core 0.8%) | — | — | — |
| cam5 | 7 | 6-8 | 26.85 / 0.0428 | — | -0.01 / +0.0024 (core 0.4%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | 22.60 / 0.0629 | 14.53 | 33.53 | — |
| cam3 | rife | 不复核 | —% | 26.33 / 0.0538 | 17.33 | 33.49 | 3/6 |
| cam3 | rife | oracle | 5.4% | 26.53 / 0.0515 | 17.69 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | —% | 27.04 / 0.0478 | 18.94 | 33.51 | 6/6 |
| cam3 | rife | oracle | 5.5% | 27.17 / 0.0468 | 19.19 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | —% | 26.68 / 0.0509 | 17.79 | 33.51 | 5/6 |
| cam3 | rife | oracle | 5.4% | 26.84 / 0.0494 | 18.10 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | —% | 26.87 / 0.0491 | 18.22 | 33.51 | 6/6 |
| cam3 | rife | oracle | 5.4% | 27.02 / 0.0480 | 18.53 | 33.53 | 6/6 |
| cam5 | 纯光流 | — | — | 28.00 / 0.0396 | 20.41 | 31.46 | — |
| cam5 | rife | 不复核 | —% | 27.72 / 0.0421 | 20.23 | 31.36 | 0/4 |
| cam5 | rife | oracle | 1.6% | 27.98 / 0.0408 | 20.63 | 31.45 | 0/4 |
| cam5 | rife | 不复核 | —% | 28.97 / 0.0387 | 22.32 | 31.43 | 2/4 |
| cam5 | rife | oracle | 1.7% | 29.04 / 0.0375 | 22.42 | 31.46 | 2/4 |
| cam5 | rife | 不复核 | —% | 28.39 / 0.0404 | 21.02 | 31.41 | 1/4 |
| cam5 | rife | oracle | 1.6% | 28.52 / 0.0392 | 21.23 | 31.46 | 2/4 |
| cam5 | rife | 不复核 | —% | 28.73 / 0.0394 | 21.72 | 31.43 | 2/4 |
| cam5 | rife | oracle | 1.6% | 28.81 / 0.0383 | 21.85 | 31.46 | 2/4 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | — |
| cam3 | FF | 0（前馈） | 887×613（61%） | 27.63 | 26.33 / 0.0538 | 17.33 / 0.1662 | 3/6 |
| cam3 | 25 | 1.81 s | 887×613（61%） | 29.11 | 26.68 / 0.0509 | 17.79 / 0.1450 | 5/6 |
| cam3 | 50 | 3.68 s | 887×613（61%） | 29.79 | 26.87 / 0.0491 | 18.22 / 0.1311 | 6/6 |
| cam3 | 100 | 7.46 s | 887×613（61%） | 30.42 | 27.04 / 0.0478 | 18.94 / 0.1149 | 6/6 |
| cam5 | 纯光流 | — | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | — |
| cam5 | FF | 0（前馈） | 740×465（35%） | 26.66 | 27.72 / 0.0421 | 20.23 / 0.0919 | 0/4 |
| cam5 | 25 | 2.10 s | 740×465（35%） | 27.81 | 28.39 / 0.0404 | 21.02 / 0.0823 | 1/4 |
| cam5 | 50 | 4.25 s | 740×465（35%） | 28.33 | 28.73 / 0.0394 | 21.72 / 0.0775 | 2/4 |
| cam5 | 100 | 8.57 s | 740×465（35%） | 28.89 | 28.97 / 0.0387 | 22.32 / 0.0682 | 2/4 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| cam3 | — | 纯光流 | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 | — |
| cam3 | rife | GS 前馈颜色 | 直接 | 26.33 / 0.0538 | 17.33 / 0.1662 | 33.49 | 3/6 |
| cam3 | rife | GS 前馈颜色 | oracle | 26.53 / 0.0515 | 17.69 / 0.1558 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 25 步 | 直接 | 26.68 / 0.0509 | 17.79 / 0.1450 | 33.51 | 5/6 |
| cam3 | rife | GS 测试时优化 25 步 | oracle | 26.84 / 0.0494 | 18.10 / 0.1362 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 50 步 | 直接 | 26.87 / 0.0491 | 18.22 / 0.1311 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 50 步 | oracle | 27.02 / 0.0480 | 18.53 / 0.1241 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 100 步 | 直接 | 27.04 / 0.0478 | 18.94 / 0.1149 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 100 步 | oracle | 27.17 / 0.0468 | 19.19 / 0.1118 | 33.53 | 6/6 |
| cam5 | — | 纯光流 | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 | — |
| cam5 | rife | GS 前馈颜色 | 直接 | 27.72 / 0.0421 | 20.23 / 0.0919 | 31.36 | 0/4 |
| cam5 | rife | GS 前馈颜色 | oracle | 27.98 / 0.0408 | 20.63 / 0.0821 | 31.45 | 0/4 |
| cam5 | rife | GS 测试时优化 25 步 | 直接 | 28.39 / 0.0404 | 21.02 / 0.0823 | 31.41 | 1/4 |
| cam5 | rife | GS 测试时优化 25 步 | oracle | 28.52 / 0.0392 | 21.23 / 0.0753 | 31.46 | 2/4 |
| cam5 | rife | GS 测试时优化 50 步 | 直接 | 28.73 / 0.0394 | 21.72 / 0.0775 | 31.43 | 2/4 |
| cam5 | rife | GS 测试时优化 50 步 | oracle | 28.81 / 0.0383 | 21.85 / 0.0721 | 31.46 | 2/4 |
| cam5 | rife | GS 测试时优化 100 步 | 直接 | 28.97 / 0.0387 | 22.32 / 0.0682 | 31.43 | 2/4 |
| cam5 | rife | GS 测试时优化 100 步 | oracle | 29.04 / 0.0375 | 22.42 / 0.0642 | 31.46 | 2/4 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.63 | 0.6593 | 0.1707 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 19.91 | 0.7515 | 0.1023 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 18.34 | 0.7061 | 0.1448 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 18.99 | 0.7316 | 0.1249 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.69 | 0.6893 | 0.1558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.19 | 0.7525 | 0.1118 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.10 | 0.7236 | 0.1362 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.53 | 0.7397 | 0.1241 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.33 | 0.6716 | 0.1662 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.94 | 0.7413 | 0.1149 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 17.79 | 0.7095 | 0.1450 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.22 | 0.7269 | 0.1311 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.91 | 0.5586 | 0.1214 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.25 | 0.6200 | 0.1109 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.04 | 0.5950 | 0.1168 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.14 | 0.6108 | 0.1138 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.77 | 0.6892 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.61 | 0.7336 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.16 | 0.7148 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.40 | 0.7266 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.77 | 0.6884 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.62 | 0.7337 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.17 | 0.7143 | 0.0350 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.41 | 0.7264 | 0.0331 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.02 | 0.5769 | 0.2882 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.31 | 0.6160 | 0.2703 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.06 | 0.5991 | 0.2819 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.16 | 0.6087 | 0.2768 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.11 | 0.8563 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 23.88 | 0.8709 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 23.45 | 0.8646 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.67 | 0.8684 | 0.0401 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.74 | 0.8455 | 0.0489 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.59 | 0.8653 | 0.0413 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.10 | 0.8568 | 0.0453 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.31 | 0.8617 | 0.0434 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.15 | 0.6151 | 0.3258 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.27 | 0.6352 | 0.3134 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.17 | 0.6290 | 0.3204 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.21 | 0.6333 | 0.3169 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.25 | 0.9036 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.93 | 0.9119 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.58 | 0.9084 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.77 | 0.9106 | 0.0471 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.03 | 0.8994 | 0.0527 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.79 | 0.9102 | 0.0469 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.39 | 0.9061 | 0.0496 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.60 | 0.9088 | 0.0482 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.50 | 0.6125 | 0.3605 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.57 | 0.6139 | 0.3561 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.51 | 0.6146 | 0.3591 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.53 | 0.6146 | 0.3577 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 33.49 | 0.9615 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.45 | 0.6084 | 0.4189 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.54 | 0.6216 | 0.4045 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.46 | 0.6179 | 0.4131 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.49 | 0.6206 | 0.4087 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.53 | 0.9256 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.17 | 0.9310 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.84 | 0.9288 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.02 | 0.9303 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.33 | 0.9228 | 0.0538 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.04 | 0.9299 | 0.0478 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.68 | 0.9273 | 0.0509 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.87 | 0.9291 | 0.0491 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.71 | 0.5861 | 0.2774 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.61 | 0.6775 | 0.2196 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 15.28 | 0.6360 | 0.2566 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 15.77 | 0.6587 | 0.2407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.63 | 0.7690 | 0.0821 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.42 | 0.8240 | 0.0642 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.23 | 0.7966 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.85 | 0.8104 | 0.0721 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.23 | 0.7546 | 0.0919 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.32 | 0.8201 | 0.0682 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.02 | 0.7887 | 0.0823 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.72 | 0.8057 | 0.0775 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.39 | 0.3976 | 0.0961 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 11.11 | 0.4931 | 0.0875 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 10.69 | 0.4506 | 0.0918 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.83 | 0.4727 | 0.0897 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.94 | 0.6958 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.77 | 0.7715 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.81 | 0.7386 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.32 | 0.7562 | 0.0159 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.94 | 0.6941 | 0.0209 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.80 | 0.7717 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.85 | 0.7383 | 0.0175 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.35 | 0.7563 | 0.0160 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.05 | 0.4789 | 0.2193 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.30 | 0.5256 | 0.2095 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.08 | 0.5045 | 0.2156 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.15 | 0.5150 | 0.2130 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.26 | 0.8669 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.84 | 0.8925 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.02 | 0.8817 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.47 | 0.8874 | 0.0196 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.58 | 0.8493 | 0.0258 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.40 | 0.8829 | 0.0210 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.49 | 0.8699 | 0.0231 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.00 | 0.8771 | 0.0219 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.60 | 0.5571 | 0.3040 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.70 | 0.5794 | 0.2969 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.61 | 0.5713 | 0.3008 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.64 | 0.5759 | 0.2988 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.32 | 0.9184 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.83 | 0.9312 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.09 | 0.9262 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.50 | 0.9290 | 0.0341 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.00 | 0.9135 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.71 | 0.9295 | 0.0340 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.91 | 0.9237 | 0.0360 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.37 | 0.9273 | 0.0349 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.33 | 0.5811 | 0.4327 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.40 | 0.5839 | 0.4293 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.34 | 0.5829 | 0.4313 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.36 | 0.5832 | 0.4305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.36 | 0.9644 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 31.43 | 0.9644 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 31.41 | 0.9646 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 31.43 | 0.9646 | 0.0311 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.65 | 0.5677 | 0.4864 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.73 | 0.5775 | 0.4781 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.66 | 0.5739 | 0.4831 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.68 | 0.5758 | 0.4808 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.98 | 0.9484 | 0.0408 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.04 | 0.9531 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.52 | 0.9512 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.81 | 0.9523 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.72 | 0.9466 | 0.0421 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.97 | 0.9524 | 0.0387 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.39 | 0.9503 | 0.0404 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.73 | 0.9517 | 0.0394 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|

## 风险阈值扫描（风险区 vs oracle_fail，按 IoU 排序，前 8 名与配置默认值）

| 设置 | warp 阈值 | col 阈值 | 精确率 | 召回率 | IoU | 面积比 |
|---|---:|---:|---:|---:|---:|---:|

## t 估计对比（scale=1.0）

| 设置 | 目标相机 | t_uniform | t_pose (VGGT) | t_posecal (标定) | t_oracle |
|---|---:|---:|---:|---:|---:|
| cam3 | 1 | — | 0.305 | — | — |
| cam3 | 2 | — | 0.551 | — | — |
| cam3 | 3 | — | 0.802 | — | — |
| cam3 | 5 | — | 0.194 | — | — |
| cam3 | 6 | — | 0.463 | — | — |
| cam3 | 7 | — | 0.742 | — | — |
| cam5 | 1 | — | 0.554 | — | — |
| cam5 | 3 | — | 0.559 | — | — |
| cam5 | 5 | — | 0.419 | — | — |
| cam5 | 7 | — | 0.522 | — | — |

## AnySplat 运行统计

旋转/光心误差：vggt 行是联合估计与输入视点估计的一致性；calib/calibK 行是标定位姿经 Sim(3) 对齐到AnySplat 输入视点位姿后的残差（反映 AnySplat 自身预测的输入相机几何与真实阵列的偏差）。

| 设置 | 变体 | 位姿来源 | 窗口边长 | 渲染分辨率 | 模式 | eps2d | 3D 滤波 | 高斯数 | 编码 s | 渲染 ms/视点 | 输入视点自渲染 PSNR | 最大旋转误差° | 最大光心误差/基线 |
|---|---|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| cam3 | gs_tokrife448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368821 | 0.818 | 82.9 | 29.07 | 0.34 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 911 | None | classic | 1.94 | False | 368821 | 0.818 | 48.8 | 29.07 | 0.34 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 911 | None | classic | 1.94 | False | 368821 | 0.818 | 68.8 | 29.07 | 0.34 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 911 | None | classic | 1.94 | False | 368821 | 0.818 | 44.1 | 29.07 | 0.34 | 0.011 |
| cam5 | gs_tokrife448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528045 | 0.519 | 64.2 | 29.43 | 0.12 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 917 | None | classic | 1.96 | False | 528045 | 0.519 | 49.1 | 29.43 | 0.12 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 917 | None | classic | 1.96 | False | 528045 | 0.519 | 42.4 | 29.43 | 0.12 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 917 | None | classic | 1.96 | False | 528045 | 0.519 | 56.7 | 29.43 | 0.12 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| cam3 | g_disp | 0.735 | 0.054 |
| cam3 | mask_ent | 0.523 | 0.054 |
| cam3 | mask_grad | 0.263 | 0.054 |
| cam3 | r_col | 0.885 | 0.054 |
| cam3 | r_warp | 0.921 | 0.054 |
| cam5 | g_disp | 0.750 | 0.018 |
| cam5 | mask_ent | 0.505 | 0.018 |
| cam5 | mask_grad | 0.279 | 0.018 |
| cam5 | r_col | 0.921 | 0.018 |
| cam5 | r_warp | 0.909 | 0.018 |
