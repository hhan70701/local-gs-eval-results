# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 9.4% | 23.90 / 0.0179 | 22.16 / 0.0424 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.6% | 23.90 / 0.0185 | 22.73 / 0.0344 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.5% | 23.89 / 0.0175 | 22.92 / 0.0380 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.5% | 23.90 / 0.0178 | 22.87 / 0.0357 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.6% | 23.89 / 0.0176 | 21.20 / 0.0428 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.8% | 23.89 / 0.0181 | 21.89 / 0.0359 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.7% | 23.87 / 0.0179 | 21.77 / 0.0384 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.7% | 23.88 / 0.0178 | 21.73 / 0.0365 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 10.1% | 23.82 / 0.0196 | 23.03 / 0.0440 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 14.7% | 24.68 / 0.0172 | 22.06 / 0.0457 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.8% | 24.65 / 0.0172 | 22.31 / 0.0382 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.7% | 24.65 / 0.0172 | 22.49 / 0.0414 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.7% | 24.65 / 0.0171 | 22.34 / 0.0395 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 14.7% | 24.68 / 0.0172 | 22.06 / 0.0457 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.8% | 24.65 / 0.0172 | 22.31 / 0.0382 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.7% | 24.65 / 0.0172 | 22.49 / 0.0414 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.7% | 24.65 / 0.0171 | 22.34 / 0.0396 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 15.4% | 24.68 / 0.0178 | 23.49 / 0.0452 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 9.1% | 25.59 / 0.0134 | 22.00 / 0.0439 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 9.8% | 25.83 / 0.0138 | 23.86 / 0.0392 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 9.3% | 25.65 / 0.0135 | 23.28 / 0.0400 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 9.4% | 25.72 / 0.0136 | 23.68 / 0.0389 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 9.1% | 25.59 / 0.0134 | 22.00 / 0.0439 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 9.8% | 25.83 / 0.0138 | 23.86 / 0.0392 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 9.3% | 25.65 / 0.0135 | 23.28 / 0.0400 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 9.4% | 25.72 / 0.0136 | 23.68 / 0.0389 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.61 / 0.0671 | 31.39 / 0.0705 | 19.53 / 0.0194 | 31.02 / 0.0297 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.15 / 0.0868 | 30.81 / 0.0814 | 19.73 / 0.0251 | 30.79 / 0.0318 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.33 / 0.0801 | 30.61 / 0.0813 | 20.03 / 0.0216 | 30.82 / 0.0313 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.45 / 0.0840 | 30.91 / 0.0812 | 20.05 / 0.0232 | 30.86 / 0.0314 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.43 / 0.0819 | 30.90 / 0.0808 | 20.04 / 0.0224 | 30.84 / 0.0312 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.69 / 0.0862 | 30.76 / 0.0815 | 19.36 / 0.0256 | 30.59 / 0.0322 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.96 / 0.0802 | 30.99 / 0.0793 | 19.73 / 0.0219 | 30.66 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.95 / 0.0828 | 30.93 / 0.0807 | 19.65 / 0.0230 | 30.67 / 0.0318 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.92 / 0.0812 | 30.98 / 0.0794 | 19.64 / 0.0224 | 30.65 / 0.0317 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.65 / 0.0827 | 31.09 / 0.0844 | 20.42 / 0.0248 | 30.91 / 0.0310 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.55 / 0.0966 | 30.43 / 0.0889 | 19.54 / 0.0276 | 30.39 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.62 / 0.0877 | 30.37 / 0.0858 | 19.52 / 0.0245 | 30.46 / 0.0338 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.79 / 0.0922 | 30.53 / 0.0877 | 19.70 / 0.0257 | 30.53 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.69 / 0.0897 | 30.53 / 0.0864 | 19.58 / 0.0251 | 30.47 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.55 / 0.0966 | 30.43 / 0.0889 | 19.54 / 0.0276 | 30.39 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.62 / 0.0877 | 30.37 / 0.0858 | 19.52 / 0.0245 | 30.46 / 0.0338 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.79 / 0.0922 | 30.53 / 0.0877 | 19.70 / 0.0257 | 30.53 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.69 / 0.0897 | 30.53 / 0.0864 | 19.58 / 0.0251 | 30.47 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.50 / 0.0885 | 30.87 / 0.0878 | 20.42 / 0.0260 | 30.85 / 0.0320 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.80 / 0.0917 | 30.77 / 0.0917 | 19.55 / 0.0254 | 30.35 / 0.0329 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.44 / 0.0851 | 30.68 / 0.0883 | 20.30 / 0.0216 | 30.78 / 0.0322 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.24 / 0.0881 | 30.83 / 0.0901 | 20.00 / 0.0230 | 30.66 / 0.0325 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.38 / 0.0863 | 30.86 / 0.0889 | 20.16 / 0.0220 | 30.72 / 0.0325 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.80 / 0.0917 | 30.77 / 0.0917 | 19.55 / 0.0254 | 30.35 / 0.0329 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.44 / 0.0851 | 30.68 / 0.0883 | 20.30 / 0.0216 | 30.78 / 0.0322 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.24 / 0.0881 | 30.83 / 0.0901 | 20.00 / 0.0230 | 30.66 / 0.0325 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.38 / 0.0863 | 30.86 / 0.0889 | 20.16 / 0.0221 | 30.72 / 0.0325 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.1%） | — | — | 28.61 / 0.0671 | 31.39 / 0.0705 | 31.02 |
| in035 | rife | 5.5% | 9.1% | 27.80 / 0.0917 | 30.77 / 0.0917 | 30.35 |
| in035 | cnw_cnn | 6.7% | 9.4% | 28.15 / 0.0868 | 30.81 / 0.0814 | 30.79 |
| in035 | cnw_f5 | 10.5% | 14.7% | 27.55 / 0.0966 | 30.43 / 0.0889 | 30.39 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.84 / 0.0719 | -1.15 / +0.0304 (core 6.1%) | -0.46 / +0.0216 (core 8.2%) | -1.10 / +0.0313 (core 12.3%) |
| in035 | 2 | 0-3 | 28.40 / 0.0707 | -0.68 / +0.0332 (core 6.1%) | -0.28 / +0.0262 (core 8.2%) | -1.03 / +0.0378 (core 12.3%) |
| in035 | 4 | 3-5 | 29.58 / 0.0586 | -0.57 / +0.0102 (core 2.5%) | -0.64 / +0.0114 (core 2.6%) | -1.04 / +0.0194 (core 5.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.61 / 0.0671 | 31.39 | 31.02 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.15 / 0.0868 | 30.81 | 30.79 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 28.56 / 0.0749 | 31.30 | 31.01 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.33 / 0.0801 | 30.61 | 30.82 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 28.78 / 0.0707 | 31.33 | 31.01 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.45 / 0.0840 | 30.91 | 30.86 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 28.79 / 0.0733 | 31.33 | 31.01 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.43 / 0.0819 | 30.90 | 30.84 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 28.78 / 0.0721 | 31.33 | 31.01 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.69 / 0.0862 | 30.76 | 30.59 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 28.34 / 0.0745 | 31.29 | 31.01 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.96 / 0.0802 | 30.99 | 30.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.58 / 0.0705 | 31.38 | 31.01 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.95 / 0.0828 | 30.93 | 30.67 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.56 / 0.0721 | 31.36 | 31.02 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.92 / 0.0812 | 30.98 | 30.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.55 / 0.0713 | 31.37 | 31.01 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 28.65 / 0.0827 | 31.09 | 30.91 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.5% | 28.96 / 0.0721 | 31.49 | 31.02 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.55 / 0.0966 | 30.43 | 30.39 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 28.42 / 0.0783 | 31.11 | 30.98 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.62 / 0.0877 | 30.37 | 30.46 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 28.48 / 0.0736 | 31.05 | 30.98 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.79 / 0.0922 | 30.53 | 30.53 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 28.57 / 0.0761 | 31.10 | 30.99 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.69 / 0.0897 | 30.53 | 30.47 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 28.51 / 0.0747 | 31.09 | 30.98 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.55 / 0.0966 | 30.43 | 30.39 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 28.42 / 0.0783 | 31.11 | 30.98 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.62 / 0.0877 | 30.37 | 30.46 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 28.48 / 0.0735 | 31.05 | 30.98 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.79 / 0.0922 | 30.53 | 30.53 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 28.57 / 0.0761 | 31.10 | 30.99 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.69 / 0.0897 | 30.53 | 30.47 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 28.51 / 0.0747 | 31.09 | 30.98 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 28.50 / 0.0885 | 30.87 | 30.85 | 0/3 |
| in035 | cnw_f5_pix | oracle | 3.2% | 28.94 / 0.0735 | 31.40 | 31.02 | 0/3 |
| in035 | rife | 不复核 | —% | 27.80 / 0.0917 | 30.77 | 30.35 | 0/3 |
| in035 | rife | oracle | 1.6% | 28.51 / 0.0735 | 31.38 | 31.00 | 0/3 |
| in035 | rife | 不复核 | —% | 28.44 / 0.0851 | 30.68 | 30.78 | 0/3 |
| in035 | rife | oracle | 1.6% | 28.94 / 0.0697 | 31.39 | 31.02 | 0/3 |
| in035 | rife | 不复核 | —% | 28.24 / 0.0881 | 30.83 | 30.66 | 0/3 |
| in035 | rife | oracle | 1.6% | 28.78 / 0.0716 | 31.36 | 31.01 | 0/3 |
| in035 | rife | 不复核 | —% | 28.38 / 0.0863 | 30.86 | 30.72 | 0/3 |
| in035 | rife | oracle | 1.6% | 28.87 / 0.0706 | 31.38 | 31.02 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.80 / 0.0917 | 30.77 | 30.35 | 0/3 |
| in035 | rife_mw | oracle | 1.6% | 28.51 / 0.0735 | 31.38 | 31.00 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.44 / 0.0851 | 30.68 | 30.78 | 0/3 |
| in035 | rife_mw | oracle | 1.6% | 28.94 / 0.0697 | 31.39 | 31.02 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.24 / 0.0881 | 30.83 | 30.66 | 0/3 |
| in035 | rife_mw | oracle | 1.6% | 28.78 / 0.0716 | 31.36 | 31.01 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.38 / 0.0863 | 30.86 | 30.72 | 0/3 |
| in035 | rife_mw | oracle | 1.6% | 28.87 / 0.0706 | 31.38 | 31.02 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.61 / 0.0671 | 31.39 / 0.0705 | — |
| in035 | FF | 0（前馈） | 1008×639（61%） | 28.83 | 28.15 / 0.0868 | 30.81 / 0.0814 | 0/3 |
| in035 | 25 | 0.68 s | 1008×639（61%） | 29.93 | 28.45 / 0.0840 | 30.91 / 0.0812 | 0/3 |
| in035 | 50 | 1.35 s | 1008×639（61%） | 30.49 | 28.43 / 0.0819 | 30.90 / 0.0808 | 0/3 |
| in035 | 100 | 2.66 s | 1008×639（61%） | 31.03 | 28.33 / 0.0801 | 30.61 / 0.0813 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.61 / 0.0671 | 31.39 / 0.0705 | 31.02 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.15 / 0.0868 | 30.81 / 0.0814 | 30.79 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.56 / 0.0749 | 31.30 / 0.0739 | 31.01 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.45 / 0.0840 | 30.91 / 0.0812 | 30.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.79 / 0.0733 | 31.33 / 0.0736 | 31.01 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.43 / 0.0819 | 30.90 / 0.0808 | 30.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.78 / 0.0721 | 31.33 / 0.0732 | 31.01 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.33 / 0.0801 | 30.61 / 0.0813 | 30.82 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.78 / 0.0707 | 31.33 / 0.0730 | 31.01 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.69 / 0.0862 | 30.76 / 0.0815 | 30.59 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.34 / 0.0745 | 31.29 / 0.0741 | 31.01 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.95 / 0.0828 | 30.93 / 0.0807 | 30.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.56 / 0.0721 | 31.36 / 0.0735 | 31.02 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.92 / 0.0812 | 30.98 / 0.0794 | 30.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.55 / 0.0713 | 31.37 / 0.0729 | 31.01 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.96 / 0.0802 | 30.99 / 0.0793 | 30.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.58 / 0.0705 | 31.38 / 0.0725 | 31.01 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 27.55 / 0.0966 | 30.43 / 0.0889 | 30.39 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 28.42 / 0.0783 | 31.11 / 0.0774 | 30.98 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.79 / 0.0922 | 30.53 / 0.0877 | 30.53 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.57 / 0.0761 | 31.10 / 0.0771 | 30.99 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.69 / 0.0897 | 30.53 / 0.0864 | 30.47 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.51 / 0.0747 | 31.09 / 0.0764 | 30.98 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.62 / 0.0877 | 30.37 / 0.0858 | 30.46 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.48 / 0.0736 | 31.05 / 0.0760 | 30.98 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.55 / 0.0966 | 30.43 / 0.0889 | 30.39 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.42 / 0.0783 | 31.11 / 0.0774 | 30.98 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.79 / 0.0922 | 30.53 / 0.0877 | 30.53 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.57 / 0.0761 | 31.10 / 0.0771 | 30.99 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.69 / 0.0897 | 30.53 / 0.0864 | 30.47 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.51 / 0.0747 | 31.09 / 0.0764 | 30.98 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.62 / 0.0877 | 30.37 / 0.0858 | 30.46 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.48 / 0.0735 | 31.05 / 0.0760 | 30.98 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.80 / 0.0917 | 30.77 / 0.0917 | 30.35 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.51 / 0.0735 | 31.38 / 0.0743 | 31.00 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.24 / 0.0881 | 30.83 / 0.0901 | 30.66 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.78 / 0.0716 | 31.36 / 0.0741 | 31.01 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.38 / 0.0863 | 30.86 / 0.0889 | 30.72 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.87 / 0.0706 | 31.38 / 0.0734 | 31.02 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.44 / 0.0851 | 30.68 / 0.0883 | 30.78 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.94 / 0.0697 | 31.39 / 0.0729 | 31.02 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.80 / 0.0917 | 30.77 / 0.0917 | 30.35 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.51 / 0.0735 | 31.38 / 0.0743 | 31.00 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.24 / 0.0881 | 30.83 / 0.0901 | 30.66 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.78 / 0.0716 | 31.36 / 0.0741 | 31.01 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.38 / 0.0863 | 30.86 / 0.0889 | 30.72 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.87 / 0.0706 | 31.38 / 0.0734 | 31.02 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.44 / 0.0851 | 30.68 / 0.0883 | 30.78 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.94 / 0.0697 | 31.39 / 0.0728 | 31.02 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.39 / 0.0705 | 19.53 / 0.0194 | 31.02 / 0.0297 | 28.61 / 0.0671 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 37.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.39 | 0.8381 | 0.0705 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.45 | 0.5933 | 0.6849 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.52 | 0.5916 | 0.6810 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.48 | 0.5945 | 0.6825 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.50 | 0.5939 | 0.6811 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.27 | 0.4293 | 0.6871 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.32 | 0.4266 | 0.6836 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.29 | 0.4311 | 0.6846 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.30 | 0.4295 | 0.6848 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 7.98 | 0.1720 | 0.6565 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.87 | 0.6158 | 0.6617 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.90 | 0.6124 | 0.6553 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.88 | 0.6178 | 0.6591 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.89 | 0.6161 | 0.6571 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.87 | 0.6158 | 0.6617 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.90 | 0.6124 | 0.6553 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.88 | 0.6178 | 0.6591 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.89 | 0.6161 | 0.6571 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 8.28 | 0.2143 | 0.6372 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.40 | 0.5886 | 0.6755 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.47 | 0.5878 | 0.6688 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.43 | 0.5905 | 0.6720 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.45 | 0.5899 | 0.6701 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.40 | 0.5886 | 0.6755 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.47 | 0.5878 | 0.6689 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.43 | 0.5905 | 0.6720 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.45 | 0.5899 | 0.6701 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 31.30 | 0.8382 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.33 | 0.8386 | 0.0730 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.33 | 0.8385 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.33 | 0.8385 | 0.0732 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.29 | 0.8383 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.38 | 0.8389 | 0.0725 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.36 | 0.8388 | 0.0735 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.37 | 0.8388 | 0.0729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 31.49 | 0.8386 | 0.0714 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 31.11 | 0.8373 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.05 | 0.8369 | 0.0760 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.10 | 0.8371 | 0.0771 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.09 | 0.8370 | 0.0764 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.11 | 0.8373 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.05 | 0.8369 | 0.0760 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.10 | 0.8371 | 0.0771 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.09 | 0.8370 | 0.0764 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 31.40 | 0.8383 | 0.0726 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.38 | 0.8386 | 0.0743 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.39 | 0.8386 | 0.0729 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.36 | 0.8385 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.38 | 0.8385 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 31.38 | 0.8386 | 0.0743 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.39 | 0.8386 | 0.0728 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.36 | 0.8385 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.38 | 0.8385 | 0.0734 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.81 | 0.8352 | 0.0814 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.61 | 0.8348 | 0.0813 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.91 | 0.8359 | 0.0812 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.90 | 0.8359 | 0.0808 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.76 | 0.8353 | 0.0815 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.99 | 0.8357 | 0.0793 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.93 | 0.8360 | 0.0807 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.98 | 0.8360 | 0.0794 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.09 | 0.8368 | 0.0844 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.43 | 0.8330 | 0.0889 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.37 | 0.8329 | 0.0858 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.53 | 0.8340 | 0.0877 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.53 | 0.8338 | 0.0864 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.43 | 0.8330 | 0.0889 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.37 | 0.8329 | 0.0858 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.53 | 0.8340 | 0.0877 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.53 | 0.8338 | 0.0864 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.87 | 0.8356 | 0.0878 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.77 | 0.8349 | 0.0917 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.68 | 0.8347 | 0.0883 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.83 | 0.8356 | 0.0901 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.86 | 0.8357 | 0.0889 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.77 | 0.8349 | 0.0917 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.68 | 0.8347 | 0.0883 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.83 | 0.8356 | 0.0901 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.86 | 0.8357 | 0.0889 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.53 | 0.6039 | 0.0194 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.78 | 0.4203 | 0.1048 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.92 | 0.4550 | 0.0996 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.85 | 0.4493 | 0.1026 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.86 | 0.4538 | 0.1013 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.97 | 0.3942 | 0.1021 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.01 | 0.4156 | 0.0977 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.00 | 0.4163 | 0.0994 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.99 | 0.4162 | 0.0988 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.83 | 0.4156 | 0.0893 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 10.53 | 0.4796 | 0.0880 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.61 | 0.4958 | 0.0836 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.61 | 0.5050 | 0.0855 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.61 | 0.5030 | 0.0847 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 10.53 | 0.4796 | 0.0880 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.61 | 0.4958 | 0.0836 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.61 | 0.5050 | 0.0855 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.61 | 0.5030 | 0.0847 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.68 | 0.5007 | 0.0771 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.43 | 0.3803 | 0.1110 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.69 | 0.4256 | 0.1039 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.56 | 0.4125 | 0.1070 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.62 | 0.4196 | 0.1054 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.43 | 0.3803 | 0.1110 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.69 | 0.4256 | 0.1039 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.56 | 0.4125 | 0.1070 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.62 | 0.4196 | 0.1054 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.73 | 0.6396 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.04 | 0.6697 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.05 | 0.6639 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.04 | 0.6680 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.37 | 0.6332 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.74 | 0.6634 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.67 | 0.6584 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.66 | 0.6610 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.43 | 0.6740 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.56 | 0.6298 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.55 | 0.6490 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.72 | 0.6496 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.61 | 0.6504 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.56 | 0.6298 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.55 | 0.6490 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.72 | 0.6496 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.61 | 0.6504 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.42 | 0.6744 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.57 | 0.6261 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.31 | 0.6582 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.01 | 0.6452 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.16 | 0.6515 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.57 | 0.6261 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.31 | 0.6582 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.01 | 0.6452 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.16 | 0.6515 | 0.0218 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.73 | 0.6388 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.03 | 0.6687 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.05 | 0.6631 | 0.0232 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.04 | 0.6672 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.36 | 0.6324 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.73 | 0.6623 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.65 | 0.6577 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.64 | 0.6600 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.42 | 0.6725 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.54 | 0.6281 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.52 | 0.6474 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.70 | 0.6483 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.58 | 0.6490 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.54 | 0.6281 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.52 | 0.6474 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.70 | 0.6483 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.58 | 0.6490 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.42 | 0.6732 | 0.0260 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.55 | 0.6247 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.30 | 0.6571 | 0.0216 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.00 | 0.6445 | 0.0230 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.16 | 0.6507 | 0.0220 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.55 | 0.6247 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.30 | 0.6571 | 0.0216 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.00 | 0.6445 | 0.0230 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.16 | 0.6507 | 0.0221 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 52.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.26 | 0.7816 | 0.0389 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.43 | 0.5424 | 0.3662 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.54 | 0.5452 | 0.3541 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.47 | 0.5501 | 0.3617 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.50 | 0.5483 | 0.3578 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.84 | 0.4741 | 0.3547 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.88 | 0.4678 | 0.3446 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.85 | 0.4778 | 0.3500 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.86 | 0.4726 | 0.3472 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.12 | 0.3167 | 0.3113 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.52 | 0.5861 | 0.3197 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.60 | 0.5851 | 0.3049 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.55 | 0.5950 | 0.3131 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.57 | 0.5908 | 0.3090 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.52 | 0.5861 | 0.3197 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.60 | 0.5851 | 0.3049 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.55 | 0.5950 | 0.3131 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.57 | 0.5908 | 0.3090 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 10.98 | 0.3894 | 0.2785 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.40 | 0.5361 | 0.3511 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.56 | 0.5442 | 0.3360 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.45 | 0.5463 | 0.3453 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.50 | 0.5453 | 0.3410 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.40 | 0.5361 | 0.3511 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.56 | 0.5442 | 0.3360 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.45 | 0.5463 | 0.3453 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.50 | 0.5453 | 0.3410 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.10 | 0.7801 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.34 | 0.7843 | 0.0426 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.37 | 0.7840 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.34 | 0.7842 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.74 | 0.7775 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.93 | 0.7799 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.95 | 0.7804 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.90 | 0.7799 | 0.0430 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.57 | 0.7849 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.95 | 0.7775 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.97 | 0.7802 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.10 | 0.7811 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.02 | 0.7808 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.95 | 0.7775 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.97 | 0.7802 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.10 | 0.7811 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.02 | 0.7808 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.54 | 0.7843 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.03 | 0.7794 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.61 | 0.7840 | 0.0423 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.41 | 0.7829 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.52 | 0.7835 | 0.0432 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.03 | 0.7794 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.61 | 0.7840 | 0.0423 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.41 | 0.7829 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.52 | 0.7835 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.49 | 0.7746 | 0.0569 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.73 | 0.7787 | 0.0512 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.86 | 0.7802 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.83 | 0.7799 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.90 | 0.7700 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.13 | 0.7710 | 0.0507 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.16 | 0.7739 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.10 | 0.7723 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.86 | 0.7767 | 0.0572 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.76 | 0.7657 | 0.0660 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.79 | 0.7684 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.99 | 0.7721 | 0.0620 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.86 | 0.7707 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.76 | 0.7657 | 0.0660 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.79 | 0.7684 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.99 | 0.7721 | 0.0620 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.86 | 0.7707 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.42 | 0.7682 | 0.0669 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.02 | 0.7715 | 0.0650 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.64 | 0.7755 | 0.0621 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.52 | 0.7774 | 0.0625 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.64 | 0.7767 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.02 | 0.7715 | 0.0650 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.64 | 0.7755 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.52 | 0.7774 | 0.0625 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.64 | 0.7767 | 0.0620 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 49.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.19 | 0.7506 | 0.0439 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.64 | 0.4917 | 0.4442 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.72 | 0.5000 | 0.4325 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.66 | 0.5029 | 0.4397 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.68 | 0.5021 | 0.4361 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.53 | 0.4292 | 0.4237 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.57 | 0.4322 | 0.4145 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.53 | 0.4378 | 0.4196 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.54 | 0.4346 | 0.4171 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.86 | 0.3246 | 0.3635 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.00 | 0.5418 | 0.4015 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.10 | 0.5492 | 0.3871 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.03 | 0.5556 | 0.3952 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.06 | 0.5530 | 0.3913 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.00 | 0.5418 | 0.4015 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.10 | 0.5492 | 0.3871 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.03 | 0.5556 | 0.3952 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.06 | 0.5530 | 0.3913 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.62 | 0.4056 | 0.3282 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.83 | 0.4895 | 0.4357 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.94 | 0.5034 | 0.4195 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.87 | 0.5026 | 0.4292 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.90 | 0.5034 | 0.4242 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.83 | 0.4895 | 0.4357 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.94 | 0.5034 | 0.4194 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.87 | 0.5026 | 0.4292 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.90 | 0.5034 | 0.4242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.09 | 0.7505 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.37 | 0.7559 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.38 | 0.7553 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.38 | 0.7558 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.78 | 0.7489 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.09 | 0.7539 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.06 | 0.7535 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.04 | 0.7536 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.62 | 0.7569 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.91 | 0.7480 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.01 | 0.7520 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.09 | 0.7523 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.03 | 0.7523 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.91 | 0.7480 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.01 | 0.7520 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.09 | 0.7523 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.03 | 0.7523 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.57 | 0.7564 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.02 | 0.7497 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.59 | 0.7554 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.39 | 0.7534 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.51 | 0.7545 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.02 | 0.7497 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.59 | 0.7554 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.39 | 0.7534 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.51 | 0.7545 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.56 | 0.7471 | 0.0601 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.86 | 0.7525 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.97 | 0.7537 | 0.0575 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.94 | 0.7536 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.05 | 0.7437 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.40 | 0.7482 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.42 | 0.7498 | 0.0565 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.37 | 0.7488 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.25 | 0.7531 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.84 | 0.7381 | 0.0689 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.00 | 0.7435 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.15 | 0.7462 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.03 | 0.7453 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.84 | 0.7381 | 0.0689 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.00 | 0.7435 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.15 | 0.7462 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.03 | 0.7453 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.02 | 0.7500 | 0.0607 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.27 | 0.7448 | 0.0638 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.08 | 0.7523 | 0.0570 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.83 | 0.7514 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.00 | 0.7523 | 0.0582 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.27 | 0.7448 | 0.0638 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.08 | 0.7523 | 0.0570 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.83 | 0.7514 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.00 | 0.7523 | 0.0582 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 51.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.02 | 0.7636 | 0.0297 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.04 | 0.4344 | 0.3517 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.08 | 0.4364 | 0.3454 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.05 | 0.4391 | 0.3490 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.06 | 0.4380 | 0.3471 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.68 | 0.3209 | 0.3365 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.72 | 0.3214 | 0.3306 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.68 | 0.3248 | 0.3346 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.70 | 0.3229 | 0.3328 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.43 | 0.2222 | 0.2812 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.27 | 0.4964 | 0.3148 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.33 | 0.5002 | 0.3051 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.28 | 0.5054 | 0.3106 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.29 | 0.5029 | 0.3079 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.27 | 0.4964 | 0.3148 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.33 | 0.5002 | 0.3051 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.28 | 0.5054 | 0.3106 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.29 | 0.5029 | 0.3079 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.49 | 0.3204 | 0.2501 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.32 | 0.4418 | 0.3437 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.39 | 0.4453 | 0.3349 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.34 | 0.4471 | 0.3402 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.36 | 0.4463 | 0.3375 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.32 | 0.4418 | 0.3437 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.39 | 0.4453 | 0.3349 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.34 | 0.4471 | 0.3402 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.36 | 0.4463 | 0.3375 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 31.01 | 0.7633 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.01 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.01 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.01 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.01 | 0.7633 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.01 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.02 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.01 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 31.02 | 0.7636 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 30.98 | 0.7630 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.98 | 0.7633 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.99 | 0.7633 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.98 | 0.7633 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.98 | 0.7630 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.98 | 0.7633 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.99 | 0.7633 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.98 | 0.7633 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 31.02 | 0.7636 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.00 | 0.7633 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.02 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.01 | 0.7634 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.02 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 31.00 | 0.7633 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.02 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.01 | 0.7634 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.02 | 0.7635 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.79 | 0.7639 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.82 | 0.7638 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.86 | 0.7645 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.84 | 0.7642 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.59 | 0.7626 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.66 | 0.7628 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.67 | 0.7633 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.65 | 0.7630 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.91 | 0.7643 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.39 | 0.7620 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.46 | 0.7627 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.53 | 0.7637 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.47 | 0.7633 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.39 | 0.7620 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.46 | 0.7627 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.53 | 0.7637 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.47 | 0.7633 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.85 | 0.7648 | 0.0320 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.35 | 0.7614 | 0.0329 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.78 | 0.7628 | 0.0322 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.66 | 0.7626 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.72 | 0.7627 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.35 | 0.7614 | 0.0329 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.78 | 0.7628 | 0.0322 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.66 | 0.7626 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.72 | 0.7627 | 0.0325 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.61 | 0.7715 | 0.0671 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.16 | 0.4999 | 0.5434 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.22 | 0.5031 | 0.5267 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.18 | 0.5064 | 0.5370 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.19 | 0.5053 | 0.5320 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.76 | 0.4016 | 0.5283 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.79 | 0.4007 | 0.5131 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.76 | 0.4064 | 0.5219 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.77 | 0.4035 | 0.5175 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.12 | 0.2678 | 0.4667 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.22 | 0.5459 | 0.5019 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.29 | 0.5480 | 0.4792 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.24 | 0.5547 | 0.4924 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.26 | 0.5519 | 0.4860 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.22 | 0.5459 | 0.5019 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.29 | 0.5480 | 0.4792 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.24 | 0.5547 | 0.4924 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.26 | 0.5519 | 0.4860 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 10.86 | 0.3473 | 0.4241 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.20 | 0.4944 | 0.5303 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.29 | 0.5013 | 0.5089 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.23 | 0.5024 | 0.5216 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.26 | 0.5022 | 0.5153 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.20 | 0.4944 | 0.5303 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.29 | 0.5013 | 0.5089 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.23 | 0.5024 | 0.5217 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.26 | 0.5022 | 0.5153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.56 | 0.7716 | 0.0749 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.78 | 0.7745 | 0.0707 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.79 | 0.7742 | 0.0733 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.78 | 0.7745 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.34 | 0.7707 | 0.0745 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.58 | 0.7737 | 0.0705 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.56 | 0.7734 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.55 | 0.7735 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.96 | 0.7751 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.42 | 0.7701 | 0.0783 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.48 | 0.7722 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.57 | 0.7725 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.51 | 0.7724 | 0.0747 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.42 | 0.7701 | 0.0783 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.48 | 0.7722 | 0.0735 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.57 | 0.7724 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.51 | 0.7724 | 0.0747 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.94 | 0.7750 | 0.0735 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.51 | 0.7711 | 0.0735 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.94 | 0.7743 | 0.0697 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.78 | 0.7732 | 0.0716 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.87 | 0.7738 | 0.0706 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.51 | 0.7711 | 0.0735 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.94 | 0.7743 | 0.0697 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.78 | 0.7732 | 0.0716 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.87 | 0.7738 | 0.0706 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.15 | 0.7698 | 0.0868 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.33 | 0.7724 | 0.0801 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.45 | 0.7734 | 0.0840 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.43 | 0.7733 | 0.0819 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.69 | 0.7676 | 0.0862 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.96 | 0.7700 | 0.0802 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.95 | 0.7710 | 0.0828 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.92 | 0.7705 | 0.0812 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.65 | 0.7731 | 0.0827 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.55 | 0.7649 | 0.0966 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.62 | 0.7675 | 0.0877 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.79 | 0.7694 | 0.0922 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.69 | 0.7687 | 0.0897 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.55 | 0.7649 | 0.0966 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.62 | 0.7675 | 0.0877 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.79 | 0.7694 | 0.0922 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.69 | 0.7687 | 0.0897 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.50 | 0.7721 | 0.0885 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.80 | 0.7676 | 0.0917 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.44 | 0.7719 | 0.0851 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.24 | 0.7714 | 0.0881 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.38 | 0.7719 | 0.0863 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.80 | 0.7676 | 0.0917 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.44 | 0.7719 | 0.0851 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.24 | 0.7714 | 0.0881 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.38 | 0.7719 | 0.0863 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 388499 | 0.172 | 32.6 | 31.42 | 0.06 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 388499 | 0.172 | 33.6 | 31.42 | 0.06 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 388499 | 0.172 | 33.4 | 31.42 | 0.06 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 388499 | 0.172 | 34.9 | 31.42 | 0.06 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1126 | None | classic | 0.39 | False | 778826 | 0.686 | 124.5 | 30.53 | 0.23 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1126 | None | classic | 0.39 | False | 778826 | 0.686 | 124.9 | 30.53 | 0.23 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1126 | None | classic | 0.39 | False | 778826 | 0.686 | 115.0 | 30.53 | 0.23 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1126 | None | classic | 0.39 | False | 778826 | 0.686 | 122.8 | 30.53 | 0.23 | 0.005 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1390391 | 0.806 | 159.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.172 | 44.4 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.172 | 36.2 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.172 | 38.9 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.172 | 47.4 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.178 | 40.7 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.178 | 31.1 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.178 | 37.4 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 395341 | 0.178 | 32.2 | 31.37 | 0.08 | 0.011 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2002460 | 0.806 | 77.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.324 | 41.9 | 31.80 | 0.10 | 0.007 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.324 | 33.5 | 31.80 | 0.10 | 0.007 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.324 | 34.6 | 31.80 | 0.10 | 0.007 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.324 | 35.0 | 31.80 | 0.10 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.163 | 40.3 | 31.80 | 0.10 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.163 | 44.3 | 31.80 | 0.10 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.163 | 33.7 | 31.80 | 0.10 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 391721 | 0.163 | 38.4 | 31.80 | 0.10 | 0.007 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.705 | 0.021 |
| in035 | mask_ent | 0.792 | 0.021 |
| in035 | mask_grad | 0.498 | 0.021 |
| in035 | r_col | 0.690 | 0.021 |
| in035 | r_warp | 0.873 | 0.021 |
