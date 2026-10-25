# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_tokrife448_nat_dil_al_local | 11.1% | 14.58 / 0.0677 | 20.01 / 0.0499 | — | — |
| cam3 | gs_tokrife448_nat_dil_al_tto100_local | 12.0% | 14.97 / 0.0686 | 22.74 / 0.0344 | — | — |
| cam3 | gs_tokrife448_nat_dil_al_tto200_local | 12.9% | 15.04 / 0.0667 | 22.92 / 0.0327 | — | — |
| cam3 | gs_tokrife448_nat_dil_al_tto50_local | 11.6% | 14.86 / 0.0680 | 22.01 / 0.0389 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_local | 4.6% | 20.85 / 0.0681 | 18.91 / 0.1149 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_tto100_local | 5.1% | 21.07 / 0.0671 | 24.14 / 0.0691 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_tto200_local | 5.6% | 21.45 / 0.0647 | 23.01 / 0.0721 | — | — |
| cam5 | gs_tokrife448_nat_dil_al_tto50_local | 4.8% | 20.97 / 0.0681 | 23.34 / 0.0832 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.40 / 0.0536 | 17.45 / 0.1634 | 17.83 / 0.0379 | 33.50 / 0.0236 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.29 / 0.0465 | 19.75 / 0.0959 | 18.93 / 0.0305 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 27.35 / 0.0458 | 20.12 / 0.0899 | 19.03 / 0.0300 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.09 / 0.0489 | 18.78 / 0.1188 | 18.67 / 0.0323 | 33.51 / 0.0234 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.76 / 0.0419 | 20.16 / 0.0922 | 18.02 / 0.0208 | 31.34 / 0.0312 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.98 / 0.0382 | 22.21 / 0.0622 | 19.99 / 0.0136 | 31.42 / 0.0314 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 28.35 / 0.0387 | 21.09 / 0.0598 | 18.96 / 0.0139 | 31.39 / 0.0317 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.04 / 0.0388 | 22.24 / 0.0708 | 19.95 / 0.0143 | 31.43 / 0.0312 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.2%） | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 |
| cam3 | rife | 10.8% | 11.1% | 26.40 / 0.0536 | 17.45 / 0.1634 | 33.50 |
| cam5 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.2%） | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 |
| cam5 | rife | 3.8% | 4.6% | 27.76 / 0.0419 | 20.16 / 0.0922 | 31.34 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| cam3 | 1 | 0-4 | 19.25 / 0.1012 | — | +4.67 / -0.0267 (core 14.5%) | — | — | — |
| cam3 | 2 | 0-4 | 20.14 / 0.0784 | — | +4.57 / -0.0215 (core 14.5%) | — | — | — |
| cam3 | 3 | 0-4 | 22.11 / 0.0577 | — | +5.82 / -0.0100 (core 14.5%) | — | — | — |
| cam3 | 5 | 4-8 | 25.45 / 0.0357 | — | +2.98 / +0.0008 (core 2.5%) | — | — | — |
| cam3 | 6 | 4-8 | 24.03 / 0.0518 | — | +3.55 / -0.0002 (core 2.5%) | — | — | — |
| cam3 | 7 | 4-8 | 24.65 / 0.0526 | — | +1.18 / +0.0020 (core 2.5%) | — | — | — |
| cam5 | 1 | 0-2 | 23.87 / 0.0592 | — | +0.91 / +0.0017 (core 5.9%) | — | — | — |
| cam5 | 3 | 2-4 | 32.61 / 0.0248 | — | -1.63 / +0.0040 (core 3.7%) | — | — | — |
| cam5 | 5 | 4-6 | 28.67 / 0.0315 | — | -0.23 / +0.0014 (core 0.8%) | — | — | — |
| cam5 | 7 | 6-8 | 26.85 / 0.0428 | — | -0.01 / +0.0023 (core 0.4%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | 22.60 / 0.0629 | 14.53 | 33.53 | — |
| cam3 | rife | 不复核 | —% | 26.40 / 0.0536 | 17.45 | 33.50 | 4/6 |
| cam3 | rife | oracle | 5.4% | 26.58 / 0.0513 | 17.81 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | —% | 27.29 / 0.0465 | 19.75 | 33.51 | 6/6 |
| cam3 | rife | oracle | 5.6% | 27.40 / 0.0454 | 19.95 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | —% | 27.35 / 0.0458 | 20.12 | 33.51 | 6/6 |
| cam3 | rife | oracle | 5.8% | 27.47 / 0.0448 | 20.36 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | —% | 27.09 / 0.0489 | 18.78 | 33.51 | 6/6 |
| cam3 | rife | oracle | 5.5% | 27.22 / 0.0472 | 19.13 | 33.53 | 6/6 |
| cam5 | 纯光流 | — | — | 28.00 / 0.0396 | 20.41 | 31.46 | — |
| cam5 | rife | 不复核 | —% | 27.76 / 0.0419 | 20.16 | 31.34 | 0/4 |
| cam5 | rife | oracle | 1.6% | 28.02 / 0.0406 | 20.58 | 31.45 | 0/4 |
| cam5 | rife | 不复核 | —% | 28.98 / 0.0382 | 22.21 | 31.42 | 2/4 |
| cam5 | rife | oracle | 1.7% | 29.12 / 0.0369 | 22.46 | 31.46 | 2/4 |
| cam5 | rife | 不复核 | —% | 28.35 / 0.0387 | 21.09 | 31.39 | 2/4 |
| cam5 | rife | oracle | 1.7% | 28.46 / 0.0369 | 21.27 | 31.46 | 2/4 |
| cam5 | rife | 不复核 | —% | 29.04 / 0.0388 | 22.24 | 31.43 | 2/4 |
| cam5 | rife | oracle | 1.6% | 29.11 / 0.0375 | 22.40 | 31.46 | 2/4 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | — |
| cam3 | FF | 0（前馈） | 887×613（61%） | 27.67 | 26.40 / 0.0536 | 17.45 / 0.1634 | 4/6 |
| cam3 | 50 | 2.41 s | 887×613（61%） | 30.45 | 27.09 / 0.0489 | 18.78 / 0.1188 | 6/6 |
| cam3 | 100 | 4.81 s | 887×613（61%） | 31.08 | 27.29 / 0.0465 | 19.75 / 0.0959 | 6/6 |
| cam3 | 200 | 9.67 s | 887×613（61%） | 31.66 | 27.35 / 0.0458 | 20.12 / 0.0899 | 6/6 |
| cam5 | 纯光流 | — | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | — |
| cam5 | FF | 0（前馈） | 739×465（35%） | 26.74 | 27.76 / 0.0419 | 20.16 / 0.0922 | 0/4 |
| cam5 | 50 | 3.02 s | 739×465（35%） | 29.21 | 29.04 / 0.0388 | 22.24 / 0.0708 | 2/4 |
| cam5 | 100 | 6.04 s | 739×465（35%） | 29.82 | 28.98 / 0.0382 | 22.21 / 0.0622 | 2/4 |
| cam5 | 200 | 12.11 s | 739×465（35%） | 30.43 | 28.35 / 0.0387 | 21.09 / 0.0598 | 2/4 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| cam3 | — | 纯光流 | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 | — |
| cam3 | rife | GS 前馈颜色 | 直接 | 26.40 / 0.0536 | 17.45 / 0.1634 | 33.50 | 4/6 |
| cam3 | rife | GS 前馈颜色 | oracle | 26.58 / 0.0513 | 17.81 / 0.1540 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 50 步 | 直接 | 27.09 / 0.0489 | 18.78 / 0.1188 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 50 步 | oracle | 27.22 / 0.0472 | 19.13 / 0.1128 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 100 步 | 直接 | 27.29 / 0.0465 | 19.75 / 0.0959 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 100 步 | oracle | 27.40 / 0.0454 | 19.95 / 0.0956 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 200 步 | 直接 | 27.35 / 0.0458 | 20.12 / 0.0899 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 200 步 | oracle | 27.47 / 0.0448 | 20.36 / 0.0913 | 33.53 | 6/6 |
| cam5 | — | 纯光流 | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 | — |
| cam5 | rife | GS 前馈颜色 | 直接 | 27.76 / 0.0419 | 20.16 / 0.0922 | 31.34 | 0/4 |
| cam5 | rife | GS 前馈颜色 | oracle | 28.02 / 0.0406 | 20.58 / 0.0814 | 31.45 | 0/4 |
| cam5 | rife | GS 测试时优化 50 步 | 直接 | 29.04 / 0.0388 | 22.24 / 0.0708 | 31.43 | 2/4 |
| cam5 | rife | GS 测试时优化 50 步 | oracle | 29.11 / 0.0375 | 22.40 / 0.0647 | 31.46 | 2/4 |
| cam5 | rife | GS 测试时优化 100 步 | 直接 | 28.98 / 0.0382 | 22.21 / 0.0622 | 31.42 | 2/4 |
| cam5 | rife | GS 测试时优化 100 步 | oracle | 29.12 / 0.0369 | 22.46 / 0.0571 | 31.46 | 2/4 |
| cam5 | rife | GS 测试时优化 200 步 | 直接 | 28.35 / 0.0387 | 21.09 / 0.0598 | 31.39 | 2/4 |
| cam5 | rife | GS 测试时优化 200 步 | oracle | 28.46 / 0.0369 | 21.27 / 0.0546 | 31.46 | 2/4 |

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
| gs_tokrife448_nat_dil_al_local | 17.79 | 0.6670 | 0.1685 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.99 | 0.7796 | 0.0771 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 21.21 | 0.7854 | 0.0695 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 19.82 | 0.7551 | 0.1055 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.81 | 0.6964 | 0.1540 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.95 | 0.7776 | 0.0956 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 20.36 | 0.7857 | 0.0913 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.13 | 0.7563 | 0.1128 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.45 | 0.6793 | 0.1634 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.75 | 0.7686 | 0.0959 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 20.12 | 0.7764 | 0.0899 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.78 | 0.7445 | 0.1188 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.92 | 0.5606 | 0.1211 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.47 | 0.6378 | 0.1061 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 12.73 | 0.6431 | 0.1023 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.26 | 0.6226 | 0.1111 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.83 | 0.6931 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.92 | 0.7481 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 19.02 | 0.7548 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.67 | 0.7355 | 0.0322 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.83 | 0.6922 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.93 | 0.7482 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 19.03 | 0.7550 | 0.0300 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.67 | 0.7353 | 0.0323 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.03 | 0.5776 | 0.2880 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.51 | 0.6251 | 0.2627 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 10.08 | 0.6368 | 0.2494 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.22 | 0.6135 | 0.2731 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.18 | 0.8576 | 0.0441 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.19 | 0.8759 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 24.34 | 0.8773 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.90 | 0.8714 | 0.0393 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.82 | 0.8470 | 0.0488 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.97 | 0.8718 | 0.0391 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.26 | 0.8740 | 0.0377 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.55 | 0.8650 | 0.0430 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.16 | 0.6153 | 0.3257 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.38 | 0.6379 | 0.3063 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 8.61 | 0.6386 | 0.3007 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.26 | 0.6354 | 0.3134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.30 | 0.9043 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.15 | 0.9145 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 26.20 | 0.9153 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.98 | 0.9124 | 0.0468 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.09 | 0.9002 | 0.0524 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.02 | 0.9128 | 0.0458 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 26.07 | 0.9133 | 0.0454 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.83 | 0.9105 | 0.0481 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.51 | 0.6126 | 0.3603 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.71 | 0.6129 | 0.3506 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.96 | 0.6110 | 0.3444 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.59 | 0.6138 | 0.3549 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.46 | 0.6087 | 0.4189 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.68 | 0.6236 | 0.3958 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 7.94 | 0.6242 | 0.3888 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.55 | 0.6219 | 0.4043 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.58 | 0.9260 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.40 | 0.9327 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.47 | 0.9332 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.22 | 0.9314 | 0.0472 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.40 | 0.9234 | 0.0536 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.29 | 0.9316 | 0.0465 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 27.35 | 0.9318 | 0.0458 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.09 | 0.9302 | 0.0489 | 1.00 |

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
| gs_tokrife448_nat_dil_al_local | 14.64 | 0.5845 | 0.2742 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.63 | 0.6993 | 0.2018 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 16.97 | 0.7071 | 0.1937 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 16.44 | 0.6828 | 0.2224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.58 | 0.7666 | 0.0814 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.46 | 0.8363 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 21.27 | 0.8367 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.40 | 0.8260 | 0.0647 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.16 | 0.7510 | 0.0922 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.21 | 0.8300 | 0.0622 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 21.09 | 0.8281 | 0.0598 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.24 | 0.8204 | 0.0708 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.42 | 0.4038 | 0.0956 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 11.13 | 0.5204 | 0.0855 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 11.30 | 0.5170 | 0.0836 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 11.03 | 0.5016 | 0.0874 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.01 | 0.6988 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.01 | 0.7880 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 18.97 | 0.7831 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.93 | 0.7775 | 0.0143 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.02 | 0.6974 | 0.0208 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.99 | 0.7877 | 0.0136 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 18.96 | 0.7829 | 0.0139 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.95 | 0.7774 | 0.0143 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.05 | 0.4804 | 0.2189 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.40 | 0.5382 | 0.2059 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 8.61 | 0.5428 | 0.2004 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.21 | 0.5262 | 0.2106 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.30 | 0.8672 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.00 | 0.8975 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 24.08 | 0.8964 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.94 | 0.8943 | 0.0189 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.63 | 0.8500 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.52 | 0.8882 | 0.0202 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 23.81 | 0.8876 | 0.0201 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.44 | 0.8842 | 0.0214 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.60 | 0.5579 | 0.3034 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.77 | 0.5837 | 0.2933 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 7.84 | 0.5803 | 0.2918 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.67 | 0.5814 | 0.2962 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.38 | 0.9186 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.97 | 0.9334 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 26.07 | 0.9326 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.94 | 0.9322 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.06 | 0.9139 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.77 | 0.9312 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.90 | 0.9290 | 0.0344 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.82 | 0.9308 | 0.0343 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.33 | 0.5811 | 0.4327 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.45 | 0.5844 | 0.4272 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.50 | 0.5834 | 0.4252 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.38 | 0.5840 | 0.4292 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.34 | 0.9643 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 31.42 | 0.9645 | 0.0314 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 31.39 | 0.9641 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 31.43 | 0.9647 | 0.0312 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.65 | 0.5678 | 0.4860 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.78 | 0.5797 | 0.4738 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.84 | 0.5783 | 0.4707 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.71 | 0.5784 | 0.4779 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.02 | 0.9484 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.12 | 0.9540 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 28.46 | 0.9538 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.11 | 0.9536 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.76 | 0.9466 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.98 | 0.9533 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 28.35 | 0.9523 | 0.0387 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.04 | 0.9531 | 0.0388 | 1.00 |

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
| cam3 | gs_tokrife448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 367642 | 0.945 | 87.8 | 29.11 | 0.38 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 911 | None | classic | 1.94 | False | 367642 | 0.945 | 45.7 | 29.11 | 0.38 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 911 | None | classic | 1.94 | False | 367642 | 0.945 | 52.0 | 29.11 | 0.38 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 911 | None | classic | 1.94 | False | 367642 | 0.945 | 68.6 | 29.11 | 0.38 | 0.011 |
| cam5 | gs_tokrife448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 526699 | 0.519 | 73.1 | 29.49 | 0.13 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 917 | None | classic | 1.96 | False | 526699 | 0.519 | 44.6 | 29.49 | 0.13 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 917 | None | classic | 1.96 | False | 526699 | 0.519 | 44.1 | 29.49 | 0.13 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 917 | None | classic | 1.96 | False | 526699 | 0.519 | 44.4 | 29.49 | 0.13 | 0.007 |

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
