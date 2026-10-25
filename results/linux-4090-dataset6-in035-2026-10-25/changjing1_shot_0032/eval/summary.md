# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 25.5% | 22.13 / 0.0351 | 20.77 / 0.0770 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 27.7% | 22.33 / 0.0370 | 22.38 / 0.0603 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | 29.3% | 22.43 / 0.0382 | 22.30 / 0.0630 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 27.0% | 22.27 / 0.0363 | 22.44 / 0.0620 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 25.19 / 0.0637 | 22.65 / 0.0960 | 18.16 / 0.0327 | 29.29 / 0.0247 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 24.32 / 0.1023 | 22.50 / 0.1690 | 18.39 / 0.0427 | 28.86 / 0.0295 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.25 / 0.0873 | 23.93 / 0.1288 | 19.36 / 0.0346 | 28.98 / 0.0281 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.11 / 0.0873 | 23.86 / 0.1253 | 19.34 / 0.0344 | 28.61 / 0.0293 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.21 / 0.0900 | 23.85 / 0.1345 | 19.27 / 0.0369 | 28.94 / 0.0286 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 13.8%） | — | — | 25.19 / 0.0637 | 22.65 / 0.0960 | 29.29 |
| in035 | rife | 17.7% | 25.5% | 24.32 / 0.1023 | 22.50 / 0.1690 | 28.86 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 23.96 / 0.0724 | — | -0.49 / +0.0466 (core 15.6%) | — | — | — |
| in035 | 2 | 0-3 | 25.41 / 0.0635 | — | -1.60 / +0.0428 (core 15.6%) | — | — | — |
| in035 | 4 | 3-5 | 26.21 / 0.0552 | — | -0.53 / +0.0265 (core 13.7%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 25.19 / 0.0637 | 22.65 | 29.29 | — |
| in035 | rife | 不复核 | —% | 24.32 / 0.1023 | 22.50 | 28.86 | 0/3 |
| in035 | rife | oracle | 6.9% | 25.14 / 0.0767 | 23.63 | 29.24 | 0/3 |
| in035 | rife | 不复核 | —% | 25.25 / 0.0873 | 23.93 | 28.98 | 0/3 |
| in035 | rife | oracle | 7.3% | 25.84 / 0.0671 | 24.98 | 29.23 | 0/3 |
| in035 | rife | 不复核 | —% | 25.11 / 0.0873 | 23.86 | 28.61 | 0/3 |
| in035 | rife | oracle | 7.5% | 25.79 / 0.0658 | 24.98 | 29.18 | 1/3 |
| in035 | rife | 不复核 | —% | 25.21 / 0.0900 | 23.85 | 28.94 | 0/3 |
| in035 | rife | oracle | 7.2% | 25.79 / 0.0695 | 24.84 | 29.23 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 25.19 / 0.0637 | 22.65 / 0.0960 | — |
| in035 | FF | 0（前馈） | 943×715（64%） | 26.83 | 24.32 / 0.1023 | 22.50 / 0.1690 | 0/3 |
| in035 | 50 | 1.19 s | 943×715（64%） | 28.83 | 25.21 / 0.0900 | 23.85 / 0.1345 | 0/3 |
| in035 | 100 | 2.33 s | 943×715（64%） | 29.52 | 25.25 / 0.0873 | 23.93 / 0.1288 | 0/3 |
| in035 | 200 | 4.60 s | 943×715（64%） | 30.31 | 25.11 / 0.0873 | 23.86 / 0.1253 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 25.19 / 0.0637 | 22.65 / 0.0960 | 29.29 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 24.32 / 0.1023 | 22.50 / 0.1690 | 28.86 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 25.14 / 0.0767 | 23.63 / 0.1290 | 29.24 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.21 / 0.0900 | 23.85 / 0.1345 | 28.94 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 25.79 / 0.0695 | 24.84 / 0.1051 | 29.23 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 25.25 / 0.0873 | 23.93 / 0.1288 | 28.98 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 25.84 / 0.0671 | 24.98 / 0.0978 | 29.23 | 0/3 |
| in035 | rife | GS 测试时优化 200 步 | 直接 | 25.11 / 0.0873 | 23.86 / 0.1253 | 28.61 | 0/3 |
| in035 | rife | GS 测试时优化 200 步 | oracle | 25.79 / 0.0658 | 24.98 / 0.0904 | 29.18 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 / 0.0960 | 18.16 / 0.0327 | 29.29 / 0.0247 | 25.19 / 0.0637 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 18.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 | 0.6881 | 0.0960 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.85 | 0.6441 | 0.2266 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.17 | 0.6938 | 0.1634 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 20.29 | 0.6838 | 0.1556 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.05 | 0.6930 | 0.1740 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.63 | 0.7081 | 0.1290 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.98 | 0.7397 | 0.0978 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 24.98 | 0.7376 | 0.0904 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.84 | 0.7368 | 0.1051 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.50 | 0.6753 | 0.1690 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.93 | 0.7149 | 0.1288 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 23.86 | 0.7057 | 0.1253 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.85 | 0.7148 | 0.1345 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 13.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.16 | 0.4942 | 0.0327 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.46 | 0.3907 | 0.1293 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.98 | 0.4553 | 0.1118 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 10.93 | 0.4580 | 0.1021 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.72 | 0.4469 | 0.1190 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.41 | 0.5370 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.38 | 0.5868 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 19.36 | 0.5845 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.29 | 0.5804 | 0.0366 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.39 | 0.5352 | 0.0427 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.36 | 0.5852 | 0.0346 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 19.34 | 0.5831 | 0.0344 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.27 | 0.5789 | 0.0369 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 51.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.24 | 0.7128 | 0.0458 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.67 | 0.5588 | 0.2328 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 10.43 | 0.5929 | 0.1992 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 11.12 | 0.5881 | 0.1864 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.99 | 0.5909 | 0.2098 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.19 | 0.7156 | 0.0593 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.15 | 0.7354 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 24.13 | 0.7341 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.07 | 0.7333 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.17 | 0.6914 | 0.0827 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.17 | 0.7149 | 0.0694 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 23.12 | 0.7076 | 0.0697 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.25 | 0.7163 | 0.0709 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 47.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.11 | 0.6955 | 0.0435 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.59 | 0.5062 | 0.2737 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.01 | 0.5365 | 0.2473 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 8.57 | 0.5339 | 0.2342 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.74 | 0.5366 | 0.2558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.29 | 0.7002 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.45 | 0.7186 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 25.38 | 0.7170 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.35 | 0.7167 | 0.0452 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.05 | 0.6780 | 0.0743 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.50 | 0.7024 | 0.0603 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.27 | 0.6945 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.43 | 0.7028 | 0.0624 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 56.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6956 | 0.0247 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.38 | 0.3249 | 0.2618 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.73 | 0.3281 | 0.2485 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 4.46 | 0.3394 | 0.2409 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.51 | 0.3291 | 0.2536 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.24 | 0.6949 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.23 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 29.18 | 0.6946 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.23 | 0.6948 | 0.0252 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.86 | 0.6908 | 0.0295 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.98 | 0.6923 | 0.0281 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 28.61 | 0.6895 | 0.0293 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.94 | 0.6920 | 0.0286 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.19 | 0.6979 | 0.0637 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.29 | 0.4224 | 0.3823 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.68 | 0.4415 | 0.3501 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.42 | 0.4450 | 0.3374 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.44 | 0.4413 | 0.3591 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.14 | 0.6983 | 0.0767 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.84 | 0.7077 | 0.0671 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 25.79 | 0.7065 | 0.0658 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.79 | 0.7068 | 0.0695 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.32 | 0.6853 | 0.1023 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.25 | 0.6980 | 0.0873 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.11 | 0.6931 | 0.0873 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.21 | 0.6983 | 0.0900 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 275004 | 0.317 | 44.5 | 29.10 | 0.40 | 0.031 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 275004 | 0.317 | 35.4 | 29.10 | 0.40 | 0.031 |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 1296 | None | classic | 2.51 | False | 275004 | 0.317 | 33.8 | 29.10 | 0.40 | 0.031 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 275004 | 0.317 | 31.7 | 29.10 | 0.40 | 0.031 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.650 | 0.061 |
| in035 | mask_ent | 0.652 | 0.061 |
| in035 | mask_grad | 0.451 | 0.061 |
| in035 | r_col | 0.810 | 0.061 |
| in035 | r_warp | 0.807 | 0.061 |
