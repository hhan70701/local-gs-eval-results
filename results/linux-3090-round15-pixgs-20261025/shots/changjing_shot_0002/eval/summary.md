# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 2.3% | 23.77 / 0.0057 | 23.04 / 0.0127 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.4% | 23.64 / 0.0061 | 24.32 / 0.0093 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.3% | 23.64 / 0.0059 | 23.76 / 0.0110 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.3% | 23.62 / 0.0059 | 23.95 / 0.0099 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.1% | 23.45 / 0.0055 | 22.83 / 0.0095 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.2% | 23.46 / 0.0057 | 23.76 / 0.0078 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.1% | 23.48 / 0.0054 | 23.52 / 0.0082 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.1% | 23.46 / 0.0056 | 23.68 / 0.0077 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 2.5% | 23.58 / 0.0063 | 21.49 / 0.0196 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 4.5% | 24.70 / 0.0073 | 21.87 / 0.0217 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.6% | 24.80 / 0.0073 | 23.71 / 0.0154 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.6% | 24.74 / 0.0072 | 23.00 / 0.0187 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.6% | 24.76 / 0.0073 | 23.36 / 0.0167 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 4.4% | 24.72 / 0.0070 | 22.18 / 0.0184 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.4% | 24.85 / 0.0076 | 23.11 / 0.0169 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.4% | 24.74 / 0.0073 | 22.91 / 0.0163 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.4% | 24.78 / 0.0074 | 22.96 / 0.0159 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 4.7% | 24.77 / 0.0080 | 22.36 / 0.0260 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 4.6% | 25.54 / 0.0123 | 23.22 / 0.0255 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 5.0% | 25.76 / 0.0122 | 23.64 / 0.0236 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 4.8% | 25.66 / 0.0124 | 23.78 / 0.0231 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 4.8% | 25.65 / 0.0123 | 23.80 / 0.0222 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 4.8% | 25.52 / 0.0125 | 22.69 / 0.0294 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 5.7% | 26.14 / 0.0133 | 22.96 / 0.0341 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 5.2% | 25.78 / 0.0127 | 23.43 / 0.0277 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 5.4% | 25.88 / 0.0131 | 23.52 / 0.0279 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.19 / 0.0732 | 36.69 / 0.0247 | 20.65 / 0.0141 | 29.20 / 0.0525 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.17 / 0.0789 | 36.69 / 0.0247 | 20.75 / 0.0150 | 29.21 / 0.0544 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.26 / 0.0763 | 36.69 / 0.0247 | 21.14 / 0.0141 | 29.22 / 0.0536 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.24 / 0.0778 | 36.69 / 0.0247 | 20.98 / 0.0145 | 29.22 / 0.0540 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.25 / 0.0769 | 36.69 / 0.0247 | 21.06 / 0.0142 | 29.22 / 0.0538 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.21 / 0.0759 | 36.69 / 0.0247 | 21.14 / 0.0145 | 29.21 / 0.0535 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.24 / 0.0746 | 36.69 / 0.0247 | 21.31 / 0.0141 | 29.21 / 0.0529 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.24 / 0.0752 | 36.69 / 0.0247 | 21.32 / 0.0140 | 29.21 / 0.0532 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.25 / 0.0747 | 36.69 / 0.0247 | 21.31 / 0.0140 | 29.21 / 0.0530 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.18 / 0.0772 | 36.69 / 0.0247 | 20.73 / 0.0155 | 29.21 / 0.0536 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.95 / 0.0834 | 36.69 / 0.0247 | 20.70 / 0.0163 | 29.15 / 0.0554 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.14 / 0.0787 | 36.69 / 0.0247 | 21.25 / 0.0147 | 29.18 / 0.0544 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.10 / 0.0813 | 36.69 / 0.0247 | 21.03 / 0.0154 | 29.18 / 0.0549 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.12 / 0.0799 | 36.69 / 0.0247 | 21.14 / 0.0149 | 29.18 / 0.0546 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.95 / 0.0802 | 36.69 / 0.0247 | 20.70 / 0.0156 | 29.11 / 0.0550 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.04 / 0.0784 | 36.69 / 0.0247 | 20.82 / 0.0157 | 29.16 / 0.0536 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.06 / 0.0787 | 36.69 / 0.0247 | 20.88 / 0.0150 | 29.16 / 0.0543 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.04 / 0.0782 | 36.69 / 0.0247 | 20.80 / 0.0153 | 29.16 / 0.0539 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.10 / 0.0801 | 36.69 / 0.0247 | 20.75 / 0.0167 | 29.18 / 0.0539 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 28.00 / 0.0794 | 35.12 / 0.0356 | 20.84 / 0.0118 | 29.03 / 0.0560 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.12 / 0.0767 | 36.01 / 0.0327 | 21.31 / 0.0107 | 29.08 / 0.0555 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.06 / 0.0782 | 35.64 / 0.0352 | 21.07 / 0.0111 | 29.05 / 0.0559 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.07 / 0.0777 | 35.83 / 0.0334 | 21.16 / 0.0110 | 29.07 / 0.0557 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.93 / 0.0805 | 35.38 / 0.0376 | 21.14 / 0.0111 | 29.00 / 0.0571 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.98 / 0.0786 | 34.86 / 0.0439 | 21.24 / 0.0108 | 28.94 / 0.0575 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.98 / 0.0796 | 35.51 / 0.0341 | 21.28 / 0.0107 | 28.95 / 0.0573 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.98 / 0.0789 | 35.46 / 0.0315 | 21.27 / 0.0106 | 28.95 / 0.0573 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.3%） | — | — | 28.19 / 0.0732 | 36.69 / 0.0247 | 29.20 |
| in035 | rife | 2.0% | 4.6% | 28.00 / 0.0794 | 35.12 / 0.0356 | 29.03 |
| in035 | cnw_cnn | 1.7% | 2.3% | 28.17 / 0.0789 | 36.69 / 0.0247 | 29.21 |
| in035 | cnw_f5 | 2.9% | 4.5% | 27.95 / 0.0834 | 36.69 / 0.0247 | 29.15 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.52 / 0.0714 | -0.04 / +0.0022 (core 1.6%) | -0.02 / +0.0056 (core 1.1%) | -0.23 / +0.0112 (core 2.7%) |
| in035 | 2 | 0-3 | 28.38 / 0.0773 | -0.40 / +0.0091 (core 1.6%) | -0.13 / +0.0055 (core 1.1%) | -0.44 / +0.0113 (core 2.7%) |
| in035 | 4 | 3-5 | 28.68 / 0.0708 | -0.15 / +0.0075 (core 1.7%) | +0.08 / +0.0062 (core 1.6%) | -0.05 / +0.0082 (core 2.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.19 / 0.0732 | 36.69 | 29.20 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.17 / 0.0789 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.19 / 0.0745 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.26 / 0.0763 | 36.69 | 29.22 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.26 / 0.0736 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.24 / 0.0778 | 36.69 | 29.22 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.23 / 0.0741 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.25 / 0.0769 | 36.69 | 29.22 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.25 / 0.0738 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.21 / 0.0759 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.25 / 0.0735 | 36.69 | 29.20 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.24 / 0.0746 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.28 / 0.0734 | 36.69 | 29.21 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.24 / 0.0752 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.28 / 0.0733 | 36.69 | 29.21 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.25 / 0.0747 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.28 / 0.0732 | 36.69 | 29.21 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 28.18 / 0.0772 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 0.5% | 28.20 / 0.0747 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.95 / 0.0834 | 36.69 | 29.15 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.14 / 0.0761 | 36.69 | 29.20 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.14 / 0.0787 | 36.69 | 29.18 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.25 / 0.0742 | 36.69 | 29.20 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.10 / 0.0813 | 36.69 | 29.18 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.21 / 0.0752 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.12 / 0.0799 | 36.69 | 29.18 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.23 / 0.0746 | 36.69 | 29.21 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.95 / 0.0802 | 36.69 | 29.11 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.9% | 28.13 / 0.0749 | 36.69 | 29.20 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.04 / 0.0784 | 36.69 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.9% | 28.15 / 0.0750 | 36.69 | 29.20 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.06 / 0.0787 | 36.69 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.9% | 28.17 / 0.0742 | 36.69 | 29.20 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.04 / 0.0782 | 36.69 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.9% | 28.14 / 0.0744 | 36.69 | 29.20 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 28.10 / 0.0801 | 36.69 | 29.18 | 0/3 |
| in035 | cnw_f5_pix | oracle | 0.9% | 28.20 / 0.0759 | 36.69 | 29.21 | 0/3 |
| in035 | rife | 不复核 | —% | 28.00 / 0.0794 | 35.12 | 29.03 | 0/3 |
| in035 | rife | oracle | 0.6% | 28.21 / 0.0719 | 36.69 | 29.20 | 1/3 |
| in035 | rife | 不复核 | —% | 28.12 / 0.0767 | 36.01 | 29.08 | 1/3 |
| in035 | rife | oracle | 0.6% | 28.29 / 0.0710 | 36.69 | 29.21 | 2/3 |
| in035 | rife | 不复核 | —% | 28.06 / 0.0782 | 35.64 | 29.05 | 0/3 |
| in035 | rife | oracle | 0.6% | 28.25 / 0.0715 | 36.69 | 29.21 | 1/3 |
| in035 | rife | 不复核 | —% | 28.07 / 0.0777 | 35.83 | 29.07 | 0/3 |
| in035 | rife | oracle | 0.6% | 28.26 / 0.0713 | 36.69 | 29.20 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.93 / 0.0805 | 35.38 | 29.00 | 0/3 |
| in035 | rife_mw | oracle | 0.7% | 28.27 / 0.0714 | 36.69 | 29.20 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 27.98 / 0.0786 | 34.86 | 28.94 | 0/3 |
| in035 | rife_mw | oracle | 0.7% | 28.29 / 0.0708 | 36.69 | 29.20 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.98 / 0.0796 | 35.51 | 28.95 | 0/3 |
| in035 | rife_mw | oracle | 0.7% | 28.30 / 0.0709 | 36.69 | 29.21 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 27.98 / 0.0789 | 35.46 | 28.95 | 0/3 |
| in035 | rife_mw | oracle | 0.7% | 28.30 / 0.0708 | 36.69 | 29.21 | 3/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.19 / 0.0732 | 36.69 / 0.0247 | — |
| in035 | FF | 0（前馈） | 1008×608（56%） | 28.81 | 28.17 / 0.0789 | 36.69 / 0.0247 | 0/3 |
| in035 | 25 | 1.06 s | 1008×608（56%） | 29.16 | 28.24 / 0.0778 | 36.69 / 0.0247 | 0/3 |
| in035 | 50 | 2.10 s | 1008×608（56%） | 29.30 | 28.25 / 0.0769 | 36.69 / 0.0247 | 0/3 |
| in035 | 100 | 4.19 s | 1008×608（56%） | 29.43 | 28.26 / 0.0763 | 36.69 / 0.0247 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.19 / 0.0732 | 36.69 / 0.0247 | 29.20 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.17 / 0.0789 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.19 / 0.0745 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.24 / 0.0778 | 36.69 / 0.0247 | 29.22 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.23 / 0.0741 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.25 / 0.0769 | 36.69 / 0.0247 | 29.22 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.25 / 0.0738 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.26 / 0.0763 | 36.69 / 0.0247 | 29.22 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.26 / 0.0736 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 28.21 / 0.0759 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.25 / 0.0735 | 36.69 / 0.0247 | 29.20 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.24 / 0.0752 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.28 / 0.0733 | 36.69 / 0.0247 | 29.21 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.25 / 0.0747 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.28 / 0.0732 | 36.69 / 0.0247 | 29.21 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.24 / 0.0746 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.28 / 0.0734 | 36.69 / 0.0247 | 29.21 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 27.95 / 0.0834 | 36.69 / 0.0247 | 29.15 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 28.14 / 0.0761 | 36.69 / 0.0247 | 29.20 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 28.10 / 0.0813 | 36.69 / 0.0247 | 29.18 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.21 / 0.0752 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 28.12 / 0.0799 | 36.69 / 0.0247 | 29.18 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.23 / 0.0746 | 36.69 / 0.0247 | 29.21 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 28.14 / 0.0787 | 36.69 / 0.0247 | 29.18 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.25 / 0.0742 | 36.69 / 0.0247 | 29.20 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.95 / 0.0802 | 36.69 / 0.0247 | 29.11 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.13 / 0.0749 | 36.69 / 0.0247 | 29.20 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.06 / 0.0787 | 36.69 / 0.0247 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.17 / 0.0742 | 36.69 / 0.0247 | 29.20 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.04 / 0.0782 | 36.69 / 0.0247 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.14 / 0.0744 | 36.69 / 0.0247 | 29.20 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.04 / 0.0784 | 36.69 / 0.0247 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.15 / 0.0750 | 36.69 / 0.0247 | 29.20 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 28.00 / 0.0794 | 35.12 / 0.0356 | 29.03 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.21 / 0.0719 | 36.69 / 0.0247 | 29.20 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.06 / 0.0782 | 35.64 / 0.0352 | 29.05 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.25 / 0.0715 | 36.69 / 0.0247 | 29.21 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.07 / 0.0777 | 35.83 / 0.0334 | 29.07 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.26 / 0.0713 | 36.69 / 0.0247 | 29.20 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.12 / 0.0767 | 36.01 / 0.0327 | 29.08 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.29 / 0.0710 | 36.69 / 0.0247 | 29.21 | 2/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.93 / 0.0805 | 35.38 / 0.0376 | 29.00 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.27 / 0.0714 | 36.69 / 0.0247 | 29.20 | 3/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.98 / 0.0796 | 35.51 / 0.0341 | 28.95 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.30 / 0.0709 | 36.69 / 0.0247 | 29.21 | 3/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.98 / 0.0789 | 35.46 / 0.0315 | 28.95 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.30 / 0.0708 | 36.69 / 0.0247 | 29.21 | 3/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.98 / 0.0786 | 34.86 / 0.0439 | 28.94 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.29 / 0.0708 | 36.69 / 0.0247 | 29.20 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 36.69 / 0.0247 | 20.65 / 0.0141 | 29.20 / 0.0525 | 28.19 / 0.0732 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 1.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 36.69 | 0.9226 | 0.0247 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.82 | 0.5527 | 0.6748 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.84 | 0.5520 | 0.6746 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.82 | 0.5527 | 0.6750 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.83 | 0.5527 | 0.6749 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.77 | 0.5548 | 0.6737 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.78 | 0.5531 | 0.6748 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.77 | 0.5540 | 0.6744 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.78 | 0.5533 | 0.6748 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 7.53 | 0.0198 | 0.6219 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.48 | 0.5606 | 0.6486 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.52 | 0.5563 | 0.6453 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.49 | 0.5581 | 0.6484 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.51 | 0.5569 | 0.6466 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.51 | 0.5618 | 0.6426 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.55 | 0.5566 | 0.6411 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.51 | 0.5599 | 0.6426 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.52 | 0.5586 | 0.6419 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 8.03 | 0.0912 | 0.6099 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.77 | 0.6183 | 0.5675 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.84 | 0.6315 | 0.5548 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.78 | 0.6261 | 0.5642 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.80 | 0.6291 | 0.5578 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.28 | 0.5945 | 0.5805 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.75 | 0.6230 | 0.5561 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.30 | 0.6003 | 0.5732 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.37 | 0.6050 | 0.5642 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 36.69 | 0.9226 | 0.0247 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 35.12 | 0.9088 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 36.01 | 0.9180 | 0.0327 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 35.64 | 0.9139 | 0.0352 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 35.83 | 0.9160 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 35.38 | 0.9121 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 34.86 | 0.9101 | 0.0439 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 35.51 | 0.9133 | 0.0341 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 35.46 | 0.9130 | 0.0315 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.65 | 0.6957 | 0.0141 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.42 | 0.2428 | 0.1240 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.49 | 0.2704 | 0.1211 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.45 | 0.2627 | 0.1226 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.47 | 0.2686 | 0.1219 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.41 | 0.2542 | 0.1247 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.46 | 0.2627 | 0.1236 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.42 | 0.2667 | 0.1243 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.43 | 0.2663 | 0.1241 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 9.90 | 0.1637 | 0.0855 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.31 | 0.3209 | 0.1101 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.40 | 0.3610 | 0.1060 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.36 | 0.3467 | 0.1079 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.38 | 0.3550 | 0.1067 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.28 | 0.3036 | 0.1091 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.30 | 0.3197 | 0.1076 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.30 | 0.3265 | 0.1078 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.30 | 0.3238 | 0.1076 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 10.77 | 0.2743 | 0.0746 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.25 | 0.2293 | 0.1223 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.31 | 0.2576 | 0.1198 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.27 | 0.2464 | 0.1210 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.29 | 0.2523 | 0.1205 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.09 | 0.2055 | 0.1127 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.12 | 0.2233 | 0.1115 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.10 | 0.2210 | 0.1120 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.11 | 0.2236 | 0.1117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.75 | 0.7091 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.13 | 0.7270 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.97 | 0.7214 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.05 | 0.7251 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.13 | 0.7206 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.30 | 0.7305 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.31 | 0.7315 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.31 | 0.7317 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.73 | 0.7077 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 20.70 | 0.7062 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.25 | 0.7317 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.02 | 0.7227 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.14 | 0.7282 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.70 | 0.7077 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.81 | 0.7168 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.87 | 0.7204 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.80 | 0.7190 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.75 | 0.7130 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.84 | 0.7278 | 0.0118 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.30 | 0.7491 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.06 | 0.7419 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.14 | 0.7461 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.14 | 0.7283 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.24 | 0.7390 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.28 | 0.7399 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.27 | 0.7413 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.75 | 0.7095 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.14 | 0.7276 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.98 | 0.7221 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.06 | 0.7258 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.14 | 0.7208 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.31 | 0.7310 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.32 | 0.7318 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.31 | 0.7321 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.73 | 0.7072 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 20.70 | 0.7059 | 0.0163 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.25 | 0.7317 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.03 | 0.7227 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.14 | 0.7283 | 0.0149 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.70 | 0.7075 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.82 | 0.7170 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.88 | 0.7209 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.80 | 0.7195 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.75 | 0.7122 | 0.0167 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.84 | 0.7279 | 0.0118 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.31 | 0.7501 | 0.0107 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.07 | 0.7427 | 0.0111 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.16 | 0.7471 | 0.0110 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.14 | 0.7277 | 0.0111 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.24 | 0.7389 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.28 | 0.7396 | 0.0107 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.27 | 0.7412 | 0.0106 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 24.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.06 | 0.7347 | 0.0238 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.28 | 0.4151 | 0.2924 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.35 | 0.4263 | 0.2859 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.30 | 0.4259 | 0.2901 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.32 | 0.4269 | 0.2881 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.21 | 0.4065 | 0.2911 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.27 | 0.4099 | 0.2863 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.22 | 0.4162 | 0.2892 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.23 | 0.4147 | 0.2879 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.37 | 0.1726 | 0.2105 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.06 | 0.4535 | 0.2671 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.22 | 0.4749 | 0.2566 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.11 | 0.4729 | 0.2627 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.15 | 0.4754 | 0.2600 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.05 | 0.4535 | 0.2637 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.15 | 0.4602 | 0.2571 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.07 | 0.4664 | 0.2610 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.10 | 0.4640 | 0.2594 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.22 | 0.2556 | 0.1912 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.63 | 0.4214 | 0.2768 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.81 | 0.4416 | 0.2672 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.69 | 0.4388 | 0.2728 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.73 | 0.4411 | 0.2704 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.98 | 0.3858 | 0.2586 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.36 | 0.4103 | 0.2479 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.01 | 0.4060 | 0.2547 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.11 | 0.4087 | 0.2518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.16 | 0.7365 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.50 | 0.7406 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.35 | 0.7395 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.43 | 0.7404 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.41 | 0.7383 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.57 | 0.7407 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.56 | 0.7408 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.57 | 0.7410 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.96 | 0.7347 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.90 | 0.7335 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.40 | 0.7403 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.22 | 0.7384 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.32 | 0.7398 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.04 | 0.7351 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.18 | 0.7378 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.19 | 0.7386 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.14 | 0.7383 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.87 | 0.7335 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.07 | 0.7400 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.48 | 0.7458 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.28 | 0.7438 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.36 | 0.7450 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.30 | 0.7397 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.43 | 0.7427 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.46 | 0.7430 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.45 | 0.7433 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.00 | 0.7358 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.39 | 0.7410 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.27 | 0.7408 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.34 | 0.7415 | 0.0265 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.04 | 0.7340 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.32 | 0.7378 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.28 | 0.7385 | 0.0255 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.32 | 0.7385 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.54 | 0.7149 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.97 | 0.7207 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.76 | 0.7329 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.53 | 0.7313 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.66 | 0.7330 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.25 | 0.7224 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.56 | 0.7289 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.58 | 0.7308 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.56 | 0.7306 | 0.0294 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.17 | 0.7035 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.19 | 0.7254 | 0.0332 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.20 | 0.7357 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.38 | 0.7351 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.39 | 0.7371 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.95 | 0.7134 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.91 | 0.7193 | 0.0343 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.35 | 0.7241 | 0.0321 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.32 | 0.7242 | 0.0322 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 35.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.84 | 0.6611 | 0.0354 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.67 | 0.2860 | 0.4896 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.69 | 0.2925 | 0.4839 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.68 | 0.2929 | 0.4873 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.68 | 0.2931 | 0.4857 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.61 | 0.2829 | 0.4880 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.63 | 0.2826 | 0.4838 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.62 | 0.2869 | 0.4865 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.62 | 0.2854 | 0.4851 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.77 | 0.1760 | 0.2835 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.24 | 0.3270 | 0.4602 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.30 | 0.3380 | 0.4510 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.26 | 0.3374 | 0.4566 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.27 | 0.3384 | 0.4539 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.24 | 0.3260 | 0.4575 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.26 | 0.3310 | 0.4508 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.24 | 0.3355 | 0.4548 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.25 | 0.3336 | 0.4528 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.90 | 0.2495 | 0.2597 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.44 | 0.2774 | 0.4669 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.46 | 0.2856 | 0.4613 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.45 | 0.2844 | 0.4646 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.45 | 0.2852 | 0.4632 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.51 | 0.2565 | 0.4064 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.39 | 0.2617 | 0.4024 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.35 | 0.2628 | 0.4046 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.34 | 0.2623 | 0.4035 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.84 | 0.6624 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.03 | 0.6644 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.95 | 0.6639 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.99 | 0.6644 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.00 | 0.6631 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.09 | 0.6644 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.08 | 0.6645 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.09 | 0.6646 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.85 | 0.6623 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.73 | 0.6609 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.02 | 0.6643 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.91 | 0.6634 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.96 | 0.6640 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.77 | 0.6613 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.78 | 0.6626 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.83 | 0.6632 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.77 | 0.6629 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.84 | 0.6624 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.88 | 0.6652 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.10 | 0.6678 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.99 | 0.6671 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.02 | 0.6676 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.04 | 0.6652 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.10 | 0.6666 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.13 | 0.6669 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.12 | 0.6670 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.78 | 0.6637 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.02 | 0.6662 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.96 | 0.6663 | 0.0391 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.99 | 0.6666 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.88 | 0.6633 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.98 | 0.6643 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.98 | 0.6653 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.99 | 0.6650 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.79 | 0.6624 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.37 | 0.6570 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.81 | 0.6634 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.69 | 0.6625 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.76 | 0.6634 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.45 | 0.6574 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.58 | 0.6612 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.64 | 0.6622 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.58 | 0.6620 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.63 | 0.6589 | 0.0413 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.57 | 0.6625 | 0.0395 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.84 | 0.6685 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.71 | 0.6668 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.74 | 0.6677 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.52 | 0.6598 | 0.0393 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.76 | 0.6633 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.70 | 0.6632 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.72 | 0.6633 | 0.0378 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.20 | 0.6522 | 0.0525 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 1.88 | 0.2311 | 0.5448 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 1.89 | 0.2318 | 0.5401 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 1.88 | 0.2328 | 0.5430 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 1.89 | 0.2323 | 0.5417 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 1.85 | 0.2288 | 0.5422 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 1.86 | 0.2274 | 0.5381 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 1.85 | 0.2296 | 0.5407 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 1.86 | 0.2285 | 0.5393 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.27 | 0.0897 | 0.3757 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.27 | 0.2615 | 0.5150 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.30 | 0.2635 | 0.5068 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.28 | 0.2652 | 0.5114 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.29 | 0.2647 | 0.5089 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.27 | 0.2598 | 0.5109 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.28 | 0.2601 | 0.5039 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.27 | 0.2638 | 0.5081 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.27 | 0.2621 | 0.5058 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.91 | 0.1443 | 0.3485 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 1.83 | 0.2275 | 0.5322 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 1.84 | 0.2287 | 0.5272 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 1.83 | 0.2295 | 0.5303 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 1.83 | 0.2292 | 0.5288 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.69 | 0.1904 | 0.4898 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.64 | 0.1915 | 0.4856 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.63 | 0.1922 | 0.4881 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.61 | 0.1917 | 0.4871 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.20 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.20 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.20 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.21 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.21 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.20 | 0.6520 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.20 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.20 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.20 | 0.6522 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.20 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.20 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.20 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.20 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.21 | 0.6522 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.21 | 0.6529 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.22 | 0.6530 | 0.0536 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.22 | 0.6531 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.22 | 0.6531 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.21 | 0.6527 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.21 | 0.6526 | 0.0529 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.21 | 0.6528 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.21 | 0.6527 | 0.0530 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.21 | 0.6527 | 0.0536 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.15 | 0.6519 | 0.0554 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.18 | 0.6526 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.18 | 0.6527 | 0.0549 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.18 | 0.6527 | 0.0546 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.11 | 0.6514 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.16 | 0.6523 | 0.0536 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.16 | 0.6523 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.16 | 0.6524 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.18 | 0.6522 | 0.0539 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.03 | 0.6501 | 0.0560 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.08 | 0.6509 | 0.0555 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.05 | 0.6506 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.07 | 0.6508 | 0.0557 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.00 | 0.6496 | 0.0571 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.94 | 0.6490 | 0.0575 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.95 | 0.6494 | 0.0573 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.95 | 0.6492 | 0.0573 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.19 | 0.6585 | 0.0732 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.15 | 0.2455 | 0.6237 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.17 | 0.2480 | 0.6144 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.15 | 0.2488 | 0.6201 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.16 | 0.2486 | 0.6171 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.12 | 0.2427 | 0.6179 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.13 | 0.2416 | 0.6106 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.12 | 0.2444 | 0.6150 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.12 | 0.2433 | 0.6125 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.02 | 0.1089 | 0.4979 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.58 | 0.2806 | 0.5911 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.61 | 0.2857 | 0.5750 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.59 | 0.2867 | 0.5847 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.60 | 0.2867 | 0.5799 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.58 | 0.2790 | 0.5829 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.60 | 0.2808 | 0.5698 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.58 | 0.2850 | 0.5780 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.59 | 0.2831 | 0.5739 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.76 | 0.1708 | 0.4568 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.07 | 0.2422 | 0.6022 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.09 | 0.2456 | 0.5921 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.08 | 0.2458 | 0.5983 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.08 | 0.2458 | 0.5954 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.80 | 0.2058 | 0.5660 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.75 | 0.2085 | 0.5580 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.74 | 0.2091 | 0.5628 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.73 | 0.2086 | 0.5606 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.19 | 0.6590 | 0.0745 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.26 | 0.6597 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.23 | 0.6596 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.25 | 0.6597 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.25 | 0.6592 | 0.0735 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.28 | 0.6597 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.28 | 0.6597 | 0.0733 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.28 | 0.6598 | 0.0732 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.20 | 0.6590 | 0.0747 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.14 | 0.6584 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.25 | 0.6597 | 0.0742 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.21 | 0.6594 | 0.0752 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.23 | 0.6596 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.13 | 0.6583 | 0.0749 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.15 | 0.6590 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.17 | 0.6592 | 0.0742 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.14 | 0.6591 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.20 | 0.6592 | 0.0759 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.21 | 0.6601 | 0.0719 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.29 | 0.6610 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.25 | 0.6608 | 0.0715 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.26 | 0.6609 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.27 | 0.6600 | 0.0714 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.29 | 0.6605 | 0.0708 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.30 | 0.6606 | 0.0709 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.30 | 0.6607 | 0.0708 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.17 | 0.6597 | 0.0789 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.26 | 0.6606 | 0.0763 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.24 | 0.6607 | 0.0778 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.25 | 0.6608 | 0.0769 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.21 | 0.6594 | 0.0759 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.24 | 0.6597 | 0.0746 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.24 | 0.6601 | 0.0752 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.25 | 0.6600 | 0.0747 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.18 | 0.6593 | 0.0772 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.95 | 0.6566 | 0.0834 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.14 | 0.6592 | 0.0787 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.10 | 0.6590 | 0.0813 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.12 | 0.6593 | 0.0799 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.95 | 0.6564 | 0.0802 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.04 | 0.6584 | 0.0784 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.06 | 0.6589 | 0.0787 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.04 | 0.6588 | 0.0782 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.10 | 0.6579 | 0.0801 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.00 | 0.6578 | 0.0794 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.12 | 0.6603 | 0.0767 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.06 | 0.6596 | 0.0782 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.07 | 0.6600 | 0.0777 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.93 | 0.6563 | 0.0805 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.98 | 0.6570 | 0.0786 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.98 | 0.6574 | 0.0796 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.98 | 0.6573 | 0.0789 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 252571 | 0.326 | 64.1 | 31.35 | 0.08 | 0.007 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 252571 | 0.326 | 77.2 | 31.35 | 0.08 | 0.007 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 252571 | 0.326 | 76.5 | 31.35 | 0.08 | 0.007 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 252571 | 0.326 | 75.6 | 31.35 | 0.08 | 0.007 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 597 | None | classic | 0.53 | False | 620291 | 1.303 | 215.0 | 31.59 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 597 | None | classic | 0.53 | False | 620291 | 1.303 | 216.8 | 31.59 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 597 | None | classic | 0.53 | False | 620291 | 1.303 | 214.7 | 31.59 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 597 | None | classic | 0.53 | False | 620291 | 1.303 | 243.2 | 31.59 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 636259 | 0.801 | 441.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 244726 | 0.329 | 53.5 | 30.59 | 0.11 | 0.002 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 244726 | 0.329 | 72.9 | 30.59 | 0.11 | 0.002 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 244726 | 0.329 | 83.1 | 30.59 | 0.11 | 0.002 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 244726 | 0.329 | 53.6 | 30.59 | 0.11 | 0.002 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 954 | None | classic | 1.36 | False | 576958 | 1.306 | 257.1 | 29.44 | 0.18 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 954 | None | classic | 1.36 | False | 576958 | 1.306 | 215.1 | 29.44 | 0.18 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 954 | None | classic | 1.36 | False | 576958 | 1.306 | 249.6 | 29.44 | 0.18 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 954 | None | classic | 1.36 | False | 576958 | 1.306 | 257.5 | 29.44 | 0.18 | 0.008 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1070024 | 0.801 | 91.9 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 247287 | 0.958 | 84.2 | 30.68 | 0.11 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 247287 | 0.958 | 67.0 | 30.68 | 0.11 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 247287 | 0.958 | 86.9 | 30.68 | 0.11 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 247287 | 0.958 | 70.7 | 30.68 | 0.11 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 765 | None | classic | 0.30 | False | 444786 | 0.975 | 167.4 | 31.39 | 0.33 | 0.034 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 765 | None | classic | 0.30 | False | 444786 | 0.975 | 173.2 | 31.39 | 0.33 | 0.034 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 765 | None | classic | 0.30 | False | 444786 | 0.975 | 180.3 | 31.39 | 0.33 | 0.034 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 765 | None | classic | 0.30 | False | 444786 | 0.975 | 162.7 | 31.39 | 0.33 | 0.034 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.642 | 0.014 |
| in035 | mask_ent | 0.739 | 0.014 |
| in035 | mask_grad | 0.420 | 0.014 |
| in035 | r_col | 0.707 | 0.014 |
| in035 | r_warp | 0.737 | 0.014 |
