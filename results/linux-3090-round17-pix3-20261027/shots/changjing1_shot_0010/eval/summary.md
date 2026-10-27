# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.9% | 25.01 / 0.0082 | 20.48 / 0.0225 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.5% | 24.52 / 0.0079 | 21.10 / 0.0242 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.4% | 21.51 / 0.0043 | 17.69 / 0.0162 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 7.7% | 24.87 / 0.0085 | 23.17 / 0.0144 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 7.8% | 24.85 / 0.0082 | 22.31 / 0.0186 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.2% | 20.81 / 0.0042 | 17.94 / 0.0106 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.23 / 0.0449 | — / — | 20.25 / 0.0094 | 29.72 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.22 / 0.0523 | — / — | 19.16 / 0.0108 | 29.57 / 0.0323 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 / 0.0506 | — / — | 20.11 / 0.0120 | 29.72 / 0.0308 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.82 / 0.0482 | — / — | 20.11 / 0.0115 | 29.71 / 0.0306 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.85 / 0.0476 | — / — | 20.20 / 0.0110 | 29.73 / 0.0307 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.77 / 0.0491 | — / — | 20.09 / 0.0110 | 29.70 / 0.0312 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.80 / 0.0474 | — / — | 20.01 / 0.0110 | 29.70 / 0.0306 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.2%） | — | — | 28.23 / 0.0449 | — / — | 29.72 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.83 / 0.0439 | — | — | — |
| in035 | 2 | 0-3 | 28.26 / 0.0426 | — | — | — |
| in035 | 4 | 3-5 | 28.59 / 0.0483 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.23 / 0.0449 | — | 29.72 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.22 / 0.0523 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.4% | 27.76 / 0.0469 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.76 / 0.0506 | — | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.2% | 28.07 / 0.0470 | — | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.82 / 0.0482 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.9% | 28.07 / 0.0466 | — | 29.72 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.85 / 0.0476 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.3% | 28.08 / 0.0458 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.77 / 0.0491 | — | 29.70 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.3% | 28.04 / 0.0460 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.80 / 0.0474 | — | 29.70 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.8% | 28.02 / 0.0459 | — | 29.72 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.23 / 0.0449 | — / — | 29.72 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.22 / 0.0523 | — / — | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.76 / 0.0469 | — / — | 29.73 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.25 / 0.0094 | 29.72 / 0.0305 | 28.23 / 0.0449 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.25 | 0.6700 | 0.0094 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.24 | 0.3060 | 0.0749 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.14 | 0.3318 | 0.0513 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.14 | 0.3318 | 0.0513 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.34 | 0.3845 | 0.0482 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.29 | 0.3512 | 0.0486 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.29 | 0.3512 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.19 | 0.6405 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.13 | 0.6664 | 0.0118 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.13 | 0.6654 | 0.0114 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.22 | 0.6901 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.11 | 0.6759 | 0.0109 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.03 | 0.6681 | 0.0109 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.16 | 0.6390 | 0.0108 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.11 | 0.6646 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.11 | 0.6638 | 0.0115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.20 | 0.6891 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.09 | 0.6744 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.01 | 0.6669 | 0.0110 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 31.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.71 | 0.7785 | 0.0169 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.95 | 0.4049 | 0.1970 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.49 | 0.3503 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.49 | 0.3503 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.68 | 0.3975 | 0.1444 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.63 | 0.3769 | 0.1501 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.63 | 0.3769 | 0.1501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.63 | 0.7683 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.46 | 0.7734 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.47 | 0.7739 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.62 | 0.7810 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.51 | 0.7774 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.45 | 0.7761 | 0.0182 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.22 | 0.7452 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.12 | 0.7492 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.33 | 0.7585 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.87 | 0.7709 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.49 | 0.7595 | 0.0237 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.60 | 0.7643 | 0.0211 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 76.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.72 | 0.7102 | 0.0305 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.83 | 0.2550 | 0.3131 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.18 | 0.1799 | 0.2433 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.18 | 0.1799 | 0.2433 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.29 | 0.1896 | 0.2361 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.28 | 0.1909 | 0.2394 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.28 | 0.1909 | 0.2394 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.73 | 0.7104 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.57 | 0.7088 | 0.0323 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.72 | 0.7107 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.71 | 0.7102 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.73 | 0.7107 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.70 | 0.7106 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.70 | 0.7100 | 0.0306 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.23 | 0.7195 | 0.0449 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.27 | 0.2774 | 0.3754 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.35 | 0.2231 | 0.3152 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.35 | 0.2231 | 0.3152 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.47 | 0.2381 | 0.3010 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.47 | 0.2358 | 0.3077 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.47 | 0.2358 | 0.3077 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.76 | 0.7169 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.07 | 0.7179 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.07 | 0.7180 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.08 | 0.7197 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.04 | 0.7186 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.02 | 0.7182 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.22 | 0.7100 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 | 0.7144 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.82 | 0.7155 | 0.0482 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.85 | 0.7176 | 0.0476 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.77 | 0.7156 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.80 | 0.7157 | 0.0474 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1245 | None | classic | 0.38 | False | 573564 | 0.987 | 178.6 | 30.90 | 0.30 | 0.019 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1165884 | 0.804 | 193.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1165884 | 0.804 | 193.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 838365 | 0.804 | 7.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 838365 | 0.804 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 838365 | 0.804 | 8.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.711 | 0.016 |
| in035 | mask_ent | 0.783 | 0.016 |
| in035 | mask_grad | 0.436 | 0.016 |
| in035 | r_col | 0.811 | 0.016 |
| in035 | r_warp | 0.857 | 0.016 |
