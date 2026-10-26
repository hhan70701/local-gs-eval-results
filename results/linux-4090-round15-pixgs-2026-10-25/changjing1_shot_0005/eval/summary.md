# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 5.7% | 26.55 / 0.0349 | 23.85 / 0.0646 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.8% | 26.54 / 0.0317 | 25.52 / 0.0458 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.9% | 26.58 / 0.0343 | 25.46 / 0.0485 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.8% | 26.56 / 0.0324 | 25.57 / 0.0461 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.7% | 26.77 / 0.0322 | 23.16 / 0.0753 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.1% | 26.71 / 0.0329 | 25.76 / 0.0510 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.0% | 26.74 / 0.0320 | 25.03 / 0.0556 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.0% | 26.73 / 0.0325 | 25.48 / 0.0529 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 6.0% | 26.69 / 0.0346 | 20.41 / 0.1243 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 6.6% | 26.34 / 0.0371 | 24.97 / 0.0657 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.8% | 26.35 / 0.0381 | 26.33 / 0.0456 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.7% | 26.35 / 0.0372 | 26.77 / 0.0450 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.7% | 26.35 / 0.0368 | 26.61 / 0.0438 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 6.6% | 26.41 / 0.0370 | 24.40 / 0.0646 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.8% | 26.45 / 0.0377 | 26.41 / 0.0451 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.8% | 26.45 / 0.0379 | 26.20 / 0.0495 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.8% | 26.45 / 0.0380 | 26.39 / 0.0479 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 6.9% | 26.35 / 0.0389 | 20.32 / 0.1373 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 3.0% | 25.86 / 0.0378 | 23.79 / 0.0726 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 3.5% | 26.13 / 0.0354 | 24.50 / 0.0543 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 3.1% | 25.92 / 0.0370 | 23.50 / 0.0664 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 3.3% | 25.97 / 0.0376 | 23.33 / 0.0641 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 3.1% | 25.96 / 0.0378 | 23.60 / 0.0662 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 3.5% | 26.25 / 0.0350 | 22.78 / 0.0638 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 3.2% | 26.06 / 0.0364 | 22.26 / 0.0733 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 3.3% | 26.09 / 0.0369 | 22.02 / 0.0651 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 31.25 / 0.0654 | 31.70 / 0.0613 | 21.17 / 0.0158 | 32.59 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.97 / 0.0688 | 31.40 / 0.0639 | 22.20 / 0.0145 | 32.48 / 0.0422 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.09 / 0.0668 | 31.51 / 0.0627 | 22.19 / 0.0150 | 32.52 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.21 / 0.0675 | 31.61 / 0.0629 | 22.34 / 0.0144 | 32.55 / 0.0417 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.13 / 0.0673 | 31.57 / 0.0628 | 22.25 / 0.0148 | 32.53 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.63 / 0.0709 | 31.32 / 0.0637 | 21.95 / 0.0159 | 32.48 / 0.0425 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.16 / 0.0682 | 31.62 / 0.0625 | 22.23 / 0.0155 | 32.50 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.06 / 0.0693 | 31.64 / 0.0627 | 22.33 / 0.0154 | 32.52 / 0.0422 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.11 / 0.0688 | 31.63 / 0.0626 | 22.24 / 0.0154 | 32.51 / 0.0420 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.07 / 0.0768 | 30.47 / 0.0696 | 18.49 / 0.0283 | 32.63 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 31.02 / 0.0688 | 31.40 / 0.0643 | 22.29 / 0.0150 | 32.47 / 0.0422 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.19 / 0.0665 | 31.58 / 0.0628 | 22.65 / 0.0146 | 32.53 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.28 / 0.0671 | 31.69 / 0.0629 | 22.74 / 0.0143 | 32.58 / 0.0415 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.23 / 0.0667 | 31.63 / 0.0628 | 22.65 / 0.0147 | 32.56 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.87 / 0.0690 | 31.42 / 0.0639 | 21.79 / 0.0151 | 32.51 / 0.0420 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.22 / 0.0667 | 31.66 / 0.0626 | 22.55 / 0.0143 | 32.54 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.20 / 0.0677 | 31.67 / 0.0629 | 22.31 / 0.0147 | 32.59 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.21 / 0.0673 | 31.66 / 0.0628 | 22.39 / 0.0144 | 32.57 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.04 / 0.0774 | 30.41 / 0.0701 | 18.32 / 0.0291 | 32.65 / 0.0415 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 31.19 / 0.0678 | 31.69 / 0.0619 | 21.85 / 0.0153 | 32.51 / 0.0412 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 31.31 / 0.0657 | 31.70 / 0.0615 | 21.97 / 0.0156 | 32.58 / 0.0409 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 31.17 / 0.0673 | 31.72 / 0.0615 | 21.97 / 0.0152 | 32.55 / 0.0410 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 31.21 / 0.0666 | 31.70 / 0.0615 | 21.95 / 0.0153 | 32.57 / 0.0409 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 31.23 / 0.0674 | 31.64 / 0.0617 | 21.80 / 0.0154 | 32.54 / 0.0412 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.08 / 0.0670 | 31.59 / 0.0616 | 21.68 / 0.0163 | 32.53 / 0.0411 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.87 / 0.0683 | 31.61 / 0.0617 | 21.56 / 0.0161 | 32.49 / 0.0413 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.91 / 0.0678 | 31.60 / 0.0615 | 21.57 / 0.0163 | 32.51 / 0.0412 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 2.7%） | — | — | 31.25 / 0.0654 | 31.70 / 0.0613 | 32.59 |
| in035 | rife | 1.1% | 3.0% | 31.19 / 0.0678 | 31.69 / 0.0619 | 32.51 |
| in035 | cnw_cnn | 3.1% | 5.7% | 30.97 / 0.0688 | 31.40 / 0.0639 | 32.48 |
| in035 | cnw_f5 | 3.8% | 6.6% | 31.02 / 0.0688 | 31.40 / 0.0643 | 32.47 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 29.75 / 0.0739 | -0.02 / +0.0038 (core 1.4%) | -0.26 / +0.0030 (core 3.1%) | -0.15 / +0.0021 (core 4.0%) |
| in035 | 2 | 0-3 | 31.42 / 0.0621 | -0.04 / +0.0031 (core 1.4%) | -0.38 / +0.0051 (core 3.1%) | -0.34 / +0.0059 (core 4.0%) |
| in035 | 4 | 3-5 | 32.60 / 0.0603 | -0.12 / +0.0003 (core 0.3%) | -0.20 / +0.0021 (core 1.8%) | -0.20 / +0.0021 (core 2.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 31.25 / 0.0654 | 31.70 | 32.59 | — |
| in035 | cnw_cnn | 不复核 | —% | 30.97 / 0.0688 | 31.40 | 32.48 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 31.40 / 0.0641 | 31.68 | 32.59 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 31.09 / 0.0668 | 31.51 | 32.52 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 31.39 / 0.0633 | 31.72 | 32.60 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 31.21 / 0.0675 | 31.61 | 32.55 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 31.45 / 0.0634 | 31.75 | 32.60 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 31.13 / 0.0673 | 31.57 | 32.53 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 31.41 / 0.0634 | 31.74 | 32.60 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 30.63 / 0.0709 | 31.32 | 32.48 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 31.25 / 0.0653 | 31.68 | 32.59 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.16 / 0.0682 | 31.62 | 32.50 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 31.42 / 0.0640 | 31.78 | 32.59 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.06 / 0.0693 | 31.64 | 32.52 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 31.40 / 0.0644 | 31.80 | 32.59 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.11 / 0.0688 | 31.63 | 32.51 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 31.41 / 0.0644 | 31.79 | 32.59 | 2/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 30.07 / 0.0768 | 30.47 | 32.63 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 0.8% | 30.59 / 0.0703 | 30.94 | 32.59 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 31.02 / 0.0688 | 31.40 | 32.47 | 0/3 |
| in035 | cnw_f5 | oracle | 1.0% | 31.39 / 0.0640 | 31.70 | 32.59 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 31.19 / 0.0665 | 31.58 | 32.53 | 1/3 |
| in035 | cnw_f5 | oracle | 1.0% | 31.48 / 0.0633 | 31.80 | 32.59 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 31.28 / 0.0671 | 31.69 | 32.58 | 1/3 |
| in035 | cnw_f5 | oracle | 1.0% | 31.51 / 0.0632 | 31.82 | 32.59 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 31.23 / 0.0667 | 31.63 | 32.56 | 1/3 |
| in035 | cnw_f5 | oracle | 1.0% | 31.50 / 0.0634 | 31.81 | 32.59 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 30.87 / 0.0690 | 31.42 | 32.51 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.0% | 31.31 / 0.0644 | 31.68 | 32.59 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 31.22 / 0.0667 | 31.66 | 32.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.0% | 31.48 / 0.0636 | 31.83 | 32.59 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 31.20 / 0.0677 | 31.67 | 32.59 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.0% | 31.47 / 0.0638 | 31.82 | 32.60 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 31.21 / 0.0673 | 31.66 | 32.57 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.0% | 31.47 / 0.0638 | 31.82 | 32.59 | 3/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 30.04 / 0.0774 | 30.41 | 32.65 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.0% | 30.53 / 0.0714 | 30.91 | 32.60 | 0/3 |
| in035 | rife | 不复核 | —% | 31.19 / 0.0678 | 31.69 | 32.51 | 0/3 |
| in035 | rife | oracle | 0.5% | 31.41 / 0.0645 | 31.73 | 32.58 | 2/3 |
| in035 | rife | 不复核 | —% | 31.31 / 0.0657 | 31.70 | 32.58 | 1/3 |
| in035 | rife | oracle | 0.6% | 31.42 / 0.0641 | 31.75 | 32.59 | 2/3 |
| in035 | rife | 不复核 | —% | 31.17 / 0.0673 | 31.72 | 32.55 | 0/3 |
| in035 | rife | oracle | 0.5% | 31.43 / 0.0643 | 31.77 | 32.58 | 2/3 |
| in035 | rife | 不复核 | —% | 31.21 / 0.0666 | 31.70 | 32.57 | 0/3 |
| in035 | rife | oracle | 0.6% | 31.42 / 0.0641 | 31.76 | 32.59 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 31.23 / 0.0674 | 31.64 | 32.54 | 0/3 |
| in035 | rife_mw | oracle | 0.5% | 31.42 / 0.0642 | 31.72 | 32.58 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 31.08 / 0.0670 | 31.59 | 32.53 | 0/3 |
| in035 | rife_mw | oracle | 0.5% | 31.36 / 0.0645 | 31.71 | 32.58 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 30.87 / 0.0683 | 31.61 | 32.49 | 0/3 |
| in035 | rife_mw | oracle | 0.5% | 31.34 / 0.0647 | 31.71 | 32.57 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 30.91 / 0.0678 | 31.60 | 32.51 | 0/3 |
| in035 | rife_mw | oracle | 0.5% | 31.34 / 0.0648 | 31.71 | 32.58 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 31.25 / 0.0654 | 31.70 / 0.0613 | — |
| in035 | FF | 0（前馈） | 394×561（56%） | 28.96 | 30.97 / 0.0688 | 31.40 / 0.0639 | 0/3 |
| in035 | 25 | 0.32 s | 394×561（56%） | 30.38 | 31.21 / 0.0675 | 31.61 / 0.0629 | 0/3 |
| in035 | 50 | 0.64 s | 394×561（56%） | 30.90 | 31.13 / 0.0673 | 31.57 / 0.0628 | 0/3 |
| in035 | 100 | 1.25 s | 394×561（56%） | 31.45 | 31.09 / 0.0668 | 31.51 / 0.0627 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 31.25 / 0.0654 | 31.70 / 0.0613 | 32.59 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 30.97 / 0.0688 | 31.40 / 0.0639 | 32.48 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 31.40 / 0.0641 | 31.68 / 0.0617 | 32.59 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 31.21 / 0.0675 | 31.61 / 0.0629 | 32.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 31.45 / 0.0634 | 31.75 / 0.0613 | 32.60 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 31.13 / 0.0673 | 31.57 / 0.0628 | 32.53 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 31.41 / 0.0634 | 31.74 / 0.0612 | 32.60 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 31.09 / 0.0668 | 31.51 / 0.0627 | 32.52 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 31.39 / 0.0633 | 31.72 / 0.0613 | 32.60 | 2/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 30.63 / 0.0709 | 31.32 / 0.0637 | 32.48 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 31.25 / 0.0653 | 31.68 / 0.0616 | 32.59 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 31.06 / 0.0693 | 31.64 / 0.0627 | 32.52 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 31.40 / 0.0644 | 31.80 / 0.0612 | 32.59 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 31.11 / 0.0688 | 31.63 / 0.0626 | 32.51 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 31.41 / 0.0644 | 31.79 / 0.0612 | 32.59 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 31.16 / 0.0682 | 31.62 / 0.0625 | 32.50 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 31.42 / 0.0640 | 31.78 / 0.0613 | 32.59 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 31.02 / 0.0688 | 31.40 / 0.0643 | 32.47 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 31.39 / 0.0640 | 31.70 / 0.0617 | 32.59 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 31.28 / 0.0671 | 31.69 / 0.0629 | 32.58 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 31.51 / 0.0632 | 31.82 / 0.0611 | 32.59 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 31.23 / 0.0667 | 31.63 / 0.0628 | 32.56 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 31.50 / 0.0634 | 31.81 / 0.0611 | 32.59 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 31.19 / 0.0665 | 31.58 / 0.0628 | 32.53 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 31.48 / 0.0633 | 31.80 / 0.0611 | 32.59 | 2/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 30.87 / 0.0690 | 31.42 / 0.0639 | 32.51 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 31.31 / 0.0644 | 31.68 / 0.0615 | 32.59 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 31.20 / 0.0677 | 31.67 / 0.0629 | 32.59 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 31.47 / 0.0638 | 31.82 / 0.0611 | 32.60 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 31.21 / 0.0673 | 31.66 / 0.0628 | 32.57 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 31.47 / 0.0638 | 31.82 / 0.0611 | 32.59 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 31.22 / 0.0667 | 31.66 / 0.0626 | 32.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 31.48 / 0.0636 | 31.83 / 0.0612 | 32.59 | 3/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 31.19 / 0.0678 | 31.69 / 0.0619 | 32.51 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 31.41 / 0.0645 | 31.73 / 0.0615 | 32.58 | 2/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 31.17 / 0.0673 | 31.72 / 0.0615 | 32.55 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 31.43 / 0.0643 | 31.77 / 0.0612 | 32.58 | 2/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 31.21 / 0.0666 | 31.70 / 0.0615 | 32.57 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 31.42 / 0.0641 | 31.76 / 0.0612 | 32.59 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 31.31 / 0.0657 | 31.70 / 0.0615 | 32.58 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 31.42 / 0.0641 | 31.75 / 0.0613 | 32.59 | 2/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 31.23 / 0.0674 | 31.64 / 0.0617 | 32.54 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 31.42 / 0.0642 | 31.72 / 0.0613 | 32.58 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 30.87 / 0.0683 | 31.61 / 0.0617 | 32.49 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 31.34 / 0.0647 | 31.71 / 0.0613 | 32.57 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 30.91 / 0.0678 | 31.60 / 0.0615 | 32.51 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 31.34 / 0.0648 | 31.71 / 0.0613 | 32.58 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 31.08 / 0.0670 | 31.59 / 0.0616 | 32.53 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 31.36 / 0.0645 | 31.71 / 0.0613 | 32.58 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.70 / 0.0613 | 21.17 / 0.0158 | 32.59 / 0.0406 | 31.25 / 0.0654 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 82.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.70 | 0.8219 | 0.0613 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.43 | 0.5352 | 0.6629 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.46 | 0.5360 | 0.6567 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.44 | 0.5387 | 0.6599 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.44 | 0.5377 | 0.6583 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.43 | 0.5359 | 0.6625 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.46 | 0.5376 | 0.6562 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.44 | 0.5398 | 0.6598 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.45 | 0.5389 | 0.6577 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 8.63 | 0.0988 | 0.6467 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.48 | 0.5363 | 0.6631 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.53 | 0.5398 | 0.6550 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.50 | 0.5413 | 0.6594 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.52 | 0.5407 | 0.6573 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.49 | 0.5374 | 0.6625 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.55 | 0.5403 | 0.6558 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.51 | 0.5419 | 0.6596 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.53 | 0.5412 | 0.6575 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 8.64 | 0.1025 | 0.6454 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.88 | 0.5063 | 0.7034 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.89 | 0.5065 | 0.7008 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.88 | 0.5072 | 0.7023 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.89 | 0.5069 | 0.7016 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.88 | 0.5045 | 0.7032 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.90 | 0.5051 | 0.7014 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.88 | 0.5058 | 0.7022 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.89 | 0.5054 | 0.7017 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 31.68 | 0.8221 | 0.0617 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.72 | 0.8222 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.75 | 0.8224 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.74 | 0.8223 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.68 | 0.8224 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.78 | 0.8226 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.80 | 0.8227 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.79 | 0.8227 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.94 | 0.8201 | 0.0657 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 31.70 | 0.8225 | 0.0617 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.80 | 0.8229 | 0.0611 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.82 | 0.8231 | 0.0611 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.81 | 0.8231 | 0.0611 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.68 | 0.8226 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.83 | 0.8230 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.82 | 0.8231 | 0.0611 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.82 | 0.8230 | 0.0611 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 30.91 | 0.8202 | 0.0661 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.73 | 0.8221 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.75 | 0.8223 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.77 | 0.8223 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.76 | 0.8223 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 31.72 | 0.8219 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.71 | 0.8220 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.71 | 0.8220 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.71 | 0.8220 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 31.40 | 0.8207 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.51 | 0.8209 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.61 | 0.8218 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.57 | 0.8214 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.32 | 0.8209 | 0.0637 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.62 | 0.8216 | 0.0625 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.64 | 0.8221 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.63 | 0.8219 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.47 | 0.8178 | 0.0696 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 31.40 | 0.8211 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.58 | 0.8222 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.69 | 0.8230 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.63 | 0.8227 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.42 | 0.8214 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.66 | 0.8223 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.67 | 0.8229 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.66 | 0.8226 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.41 | 0.8177 | 0.0701 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.69 | 0.8216 | 0.0619 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 31.70 | 0.8218 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 31.72 | 0.8220 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 31.70 | 0.8219 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 31.64 | 0.8210 | 0.0617 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.59 | 0.8212 | 0.0616 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.61 | 0.8213 | 0.0617 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.60 | 0.8213 | 0.0615 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 2.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.17 | 0.6195 | 0.0158 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 11.27 | 0.5793 | 0.0943 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.57 | 0.5879 | 0.0927 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.41 | 0.5879 | 0.0932 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.44 | 0.5911 | 0.0933 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 11.19 | 0.5970 | 0.0953 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.58 | 0.6010 | 0.0924 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.40 | 0.6031 | 0.0938 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.45 | 0.6040 | 0.0930 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.34 | 0.3599 | 0.0841 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.76 | 0.6165 | 0.0869 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.37 | 0.6402 | 0.0801 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.06 | 0.6408 | 0.0832 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.16 | 0.6420 | 0.0821 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.55 | 0.6198 | 0.0863 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.18 | 0.6357 | 0.0805 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.84 | 0.6310 | 0.0839 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.94 | 0.6323 | 0.0827 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.60 | 0.3733 | 0.0818 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.02 | 0.4480 | 0.1516 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.08 | 0.4518 | 0.1503 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.02 | 0.4533 | 0.1510 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.03 | 0.4535 | 0.1508 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.05 | 0.4212 | 0.1509 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.08 | 0.4246 | 0.1518 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.04 | 0.4206 | 0.1520 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.04 | 0.4232 | 0.1522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.17 | 0.6902 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.21 | 0.6825 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.32 | 0.6859 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.24 | 0.6863 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.96 | 0.6984 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.21 | 0.6916 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.33 | 0.6930 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.22 | 0.6929 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 18.50 | 0.5344 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.30 | 0.7066 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.66 | 0.7104 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.76 | 0.7158 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.69 | 0.7150 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.80 | 0.6999 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.55 | 0.7060 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.33 | 0.7014 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.39 | 0.7029 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.32 | 0.5351 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 21.89 | 0.6480 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.98 | 0.6512 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.98 | 0.6529 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.96 | 0.6523 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.82 | 0.6416 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.68 | 0.6430 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.57 | 0.6399 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.57 | 0.6421 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.20 | 0.6893 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.19 | 0.6807 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.34 | 0.6850 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.25 | 0.6853 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.95 | 0.6954 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.23 | 0.6916 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.33 | 0.6920 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.24 | 0.6931 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 18.49 | 0.5294 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.29 | 0.7044 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.65 | 0.7087 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.74 | 0.7139 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.65 | 0.7136 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.79 | 0.6984 | 0.0151 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.55 | 0.7051 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.31 | 0.7004 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.39 | 0.7021 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.32 | 0.5310 | 0.0291 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.85 | 0.6456 | 0.0153 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.97 | 0.6500 | 0.0156 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.97 | 0.6514 | 0.0152 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.95 | 0.6509 | 0.0153 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.80 | 0.6393 | 0.0154 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.68 | 0.6418 | 0.0163 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.56 | 0.6384 | 0.0161 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.57 | 0.6407 | 0.0163 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 41.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.71 | 0.8138 | 0.0317 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.23 | 0.5359 | 0.3824 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.34 | 0.5394 | 0.3730 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.26 | 0.5449 | 0.3778 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.28 | 0.5425 | 0.3761 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.23 | 0.5337 | 0.3835 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.34 | 0.5396 | 0.3735 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.26 | 0.5428 | 0.3779 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.29 | 0.5422 | 0.3757 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.47 | 0.1819 | 0.3521 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.42 | 0.5422 | 0.3708 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.57 | 0.5567 | 0.3596 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.47 | 0.5569 | 0.3645 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.50 | 0.5572 | 0.3627 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.43 | 0.5455 | 0.3711 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.57 | 0.5570 | 0.3605 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.48 | 0.5575 | 0.3659 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.51 | 0.5581 | 0.3637 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 10.54 | 0.1904 | 0.3507 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.97 | 0.4744 | 0.4292 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.02 | 0.4772 | 0.4243 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.98 | 0.4777 | 0.4282 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.99 | 0.4770 | 0.4271 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.97 | 0.4718 | 0.4288 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.02 | 0.4715 | 0.4260 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.97 | 0.4735 | 0.4291 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.98 | 0.4724 | 0.4282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.90 | 0.8168 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.93 | 0.8160 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.01 | 0.8171 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.97 | 0.8167 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.72 | 0.8169 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.96 | 0.8168 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.94 | 0.8168 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.96 | 0.8170 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.09 | 0.8037 | 0.0387 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.96 | 0.8173 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.15 | 0.8185 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.17 | 0.8190 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.16 | 0.8189 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.81 | 0.8179 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.15 | 0.8190 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.07 | 0.8187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.12 | 0.8190 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.97 | 0.8035 | 0.0395 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.92 | 0.8154 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.96 | 0.8156 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.93 | 0.8157 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.91 | 0.8156 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.89 | 0.8150 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.82 | 0.8147 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.78 | 0.8146 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.77 | 0.8146 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.56 | 0.8064 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.23 | 0.8083 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.24 | 0.8109 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.28 | 0.8101 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.96 | 0.8030 | 0.0400 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.21 | 0.8071 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.94 | 0.8070 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.13 | 0.8077 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.06 | 0.7757 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.88 | 0.8083 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.49 | 0.8126 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.53 | 0.8144 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.51 | 0.8140 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.45 | 0.8095 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.51 | 0.8127 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.30 | 0.8130 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.43 | 0.8132 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.73 | 0.7729 | 0.0553 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.36 | 0.8096 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.44 | 0.8118 | 0.0342 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.23 | 0.8106 | 0.0348 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.17 | 0.8107 | 0.0345 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.38 | 0.8088 | 0.0346 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.97 | 0.8085 | 0.0354 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.86 | 0.8079 | 0.0363 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.74 | 0.8077 | 0.0361 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.09 | 0.8156 | 0.0340 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.65 | 0.5486 | 0.5092 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.72 | 0.5471 | 0.5034 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.67 | 0.5540 | 0.5071 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.68 | 0.5507 | 0.5057 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.65 | 0.5480 | 0.5093 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.72 | 0.5505 | 0.5037 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.67 | 0.5548 | 0.5071 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.68 | 0.5529 | 0.5055 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 9.95 | 0.2448 | 0.4709 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.81 | 0.5537 | 0.5018 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.94 | 0.5630 | 0.4926 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.85 | 0.5652 | 0.4974 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.88 | 0.5641 | 0.4957 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.81 | 0.5554 | 0.5014 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.93 | 0.5639 | 0.4923 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.85 | 0.5661 | 0.4976 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.89 | 0.5650 | 0.4954 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 9.97 | 0.2521 | 0.4687 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.10 | 0.4671 | 0.5526 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.14 | 0.4686 | 0.5484 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.11 | 0.4697 | 0.5515 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.12 | 0.4688 | 0.5501 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.11 | 0.4651 | 0.5520 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.15 | 0.4636 | 0.5501 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.11 | 0.4655 | 0.5525 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.12 | 0.4641 | 0.5516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.35 | 0.8189 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.34 | 0.8184 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.45 | 0.8194 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.38 | 0.8189 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.12 | 0.8183 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.38 | 0.8188 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.38 | 0.8188 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.37 | 0.8188 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.82 | 0.8098 | 0.0393 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 30.38 | 0.8194 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.53 | 0.8208 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.58 | 0.8214 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.56 | 0.8212 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.21 | 0.8198 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.52 | 0.8208 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.48 | 0.8210 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.50 | 0.8208 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.72 | 0.8097 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.37 | 0.8176 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.40 | 0.8180 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.40 | 0.8182 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.39 | 0.8181 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.38 | 0.8173 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.26 | 0.8172 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.22 | 0.8172 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.22 | 0.8172 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.59 | 0.8135 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.77 | 0.8132 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.97 | 0.8160 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.85 | 0.8146 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.02 | 0.8109 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.90 | 0.8139 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.72 | 0.8143 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.82 | 0.8143 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.93 | 0.7999 | 0.0451 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.72 | 0.8151 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.98 | 0.8176 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.11 | 0.8194 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.04 | 0.8186 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.41 | 0.8156 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.02 | 0.8176 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.94 | 0.8189 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.99 | 0.8183 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.86 | 0.8016 | 0.0457 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.97 | 0.8151 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.17 | 0.8165 | 0.0338 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.91 | 0.8160 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.98 | 0.8161 | 0.0345 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.01 | 0.8144 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.73 | 0.8140 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.39 | 0.8135 | 0.0361 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.45 | 0.8136 | 0.0358 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 68.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 32.59 | 0.8225 | 0.0406 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.59 | 0.5340 | 0.5399 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.65 | 0.5346 | 0.5322 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.61 | 0.5381 | 0.5368 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.62 | 0.5364 | 0.5347 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.59 | 0.5359 | 0.5399 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.65 | 0.5358 | 0.5342 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.61 | 0.5394 | 0.5378 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.62 | 0.5377 | 0.5362 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 9.09 | 0.1462 | 0.4813 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.70 | 0.5403 | 0.5348 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.79 | 0.5428 | 0.5256 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.73 | 0.5455 | 0.5310 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.75 | 0.5442 | 0.5287 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.70 | 0.5419 | 0.5341 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.79 | 0.5431 | 0.5269 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.73 | 0.5463 | 0.5314 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.75 | 0.5449 | 0.5293 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 9.13 | 0.1553 | 0.4808 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.82 | 0.4920 | 0.5843 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.84 | 0.4921 | 0.5817 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.83 | 0.4934 | 0.5835 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.83 | 0.4928 | 0.5827 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.83 | 0.4919 | 0.5841 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.84 | 0.4912 | 0.5824 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.83 | 0.4929 | 0.5837 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.83 | 0.4919 | 0.5831 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 32.60 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 32.60 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.60 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 32.59 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 32.59 | 0.8226 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 32.59 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 32.59 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 32.59 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 32.59 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 32.59 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 32.60 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 32.59 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 32.60 | 0.8227 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 32.58 | 0.8224 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 32.59 | 0.8225 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 32.58 | 0.8225 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 32.59 | 0.8225 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 32.58 | 0.8225 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 32.58 | 0.8225 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 32.57 | 0.8224 | 0.0408 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 32.58 | 0.8225 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 32.48 | 0.8220 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 32.52 | 0.8220 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 32.55 | 0.8226 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.53 | 0.8223 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 32.48 | 0.8223 | 0.0425 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.50 | 0.8221 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 32.52 | 0.8228 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.51 | 0.8224 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 32.63 | 0.8239 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 32.47 | 0.8224 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 32.53 | 0.8229 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 32.58 | 0.8235 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 32.56 | 0.8232 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 32.51 | 0.8227 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 32.54 | 0.8229 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 32.59 | 0.8237 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 32.57 | 0.8233 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 32.65 | 0.8245 | 0.0415 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 32.51 | 0.8224 | 0.0412 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 32.58 | 0.8227 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 32.55 | 0.8228 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 32.57 | 0.8228 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 32.54 | 0.8225 | 0.0412 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 32.53 | 0.8225 | 0.0411 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 32.49 | 0.8227 | 0.0413 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 32.51 | 0.8226 | 0.0412 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.25 | 0.8156 | 0.0654 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.67 | 0.5358 | 0.6297 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.74 | 0.5360 | 0.6214 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.69 | 0.5396 | 0.6268 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.71 | 0.5377 | 0.6243 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.67 | 0.5364 | 0.6301 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.73 | 0.5375 | 0.6221 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.69 | 0.5402 | 0.6275 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.70 | 0.5389 | 0.6246 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 9.06 | 0.1459 | 0.5890 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.76 | 0.5405 | 0.6244 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.85 | 0.5453 | 0.6134 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.79 | 0.5471 | 0.6194 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.81 | 0.5461 | 0.6166 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.76 | 0.5419 | 0.6238 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.84 | 0.5455 | 0.6143 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.79 | 0.5476 | 0.6198 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.81 | 0.5467 | 0.6169 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 9.08 | 0.1524 | 0.5868 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.88 | 0.4919 | 0.6697 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.90 | 0.4925 | 0.6641 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.88 | 0.4934 | 0.6679 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.89 | 0.4928 | 0.6660 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.88 | 0.4914 | 0.6685 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.90 | 0.4902 | 0.6652 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.89 | 0.4917 | 0.6680 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.89 | 0.4907 | 0.6668 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 31.40 | 0.8170 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.39 | 0.8168 | 0.0633 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.45 | 0.8172 | 0.0634 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.41 | 0.8170 | 0.0634 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.25 | 0.8166 | 0.0653 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.42 | 0.8169 | 0.0640 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.40 | 0.8168 | 0.0644 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.41 | 0.8169 | 0.0644 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.59 | 0.8133 | 0.0703 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 31.39 | 0.8171 | 0.0640 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.48 | 0.8177 | 0.0633 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.51 | 0.8180 | 0.0632 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.50 | 0.8179 | 0.0634 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.31 | 0.8172 | 0.0644 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.48 | 0.8177 | 0.0636 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.47 | 0.8178 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.47 | 0.8178 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 30.53 | 0.8134 | 0.0714 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.41 | 0.8164 | 0.0645 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.42 | 0.8166 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.43 | 0.8167 | 0.0643 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.42 | 0.8166 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 31.42 | 0.8163 | 0.0642 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.36 | 0.8162 | 0.0645 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.34 | 0.8162 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.34 | 0.8162 | 0.0648 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.97 | 0.8147 | 0.0688 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.09 | 0.8146 | 0.0668 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.21 | 0.8159 | 0.0675 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.13 | 0.8152 | 0.0673 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.63 | 0.8135 | 0.0709 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.16 | 0.8148 | 0.0682 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.06 | 0.8150 | 0.0693 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.11 | 0.8150 | 0.0688 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.07 | 0.8099 | 0.0768 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 31.02 | 0.8153 | 0.0688 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.19 | 0.8165 | 0.0665 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.28 | 0.8174 | 0.0671 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.23 | 0.8170 | 0.0667 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.87 | 0.8155 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.22 | 0.8165 | 0.0667 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.20 | 0.8173 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.21 | 0.8170 | 0.0673 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.04 | 0.8108 | 0.0774 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.19 | 0.8153 | 0.0678 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 31.31 | 0.8161 | 0.0657 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 31.17 | 0.8159 | 0.0673 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 31.21 | 0.8159 | 0.0666 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 31.23 | 0.8152 | 0.0674 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.08 | 0.8150 | 0.0670 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.87 | 0.8148 | 0.0683 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.91 | 0.8149 | 0.0678 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 623 | None | classic | 0.58 | False | 109472 | 0.169 | 28.1 | 30.85 | 0.24 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 623 | None | classic | 0.58 | False | 109472 | 0.169 | 26.6 | 30.85 | 0.24 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 623 | None | classic | 0.58 | False | 109472 | 0.169 | 28.2 | 30.85 | 0.24 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 623 | None | classic | 0.58 | False | 109472 | 0.169 | 27.7 | 30.85 | 0.24 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 591 | None | classic | 0.52 | False | 115382 | 0.171 | 27.3 | 30.92 | 0.20 | 0.014 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 591 | None | classic | 0.52 | False | 115382 | 0.171 | 27.7 | 30.92 | 0.20 | 0.014 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 591 | None | classic | 0.52 | False | 115382 | 0.171 | 27.1 | 30.92 | 0.20 | 0.014 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 591 | None | classic | 0.52 | False | 115382 | 0.171 | 29.5 | 30.92 | 0.20 | 0.014 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 451754 | 0.804 | 144.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 619 | None | classic | 0.57 | False | 110382 | 0.168 | 27.7 | 31.32 | 0.22 | 0.021 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 619 | None | classic | 0.57 | False | 110382 | 0.168 | 27.9 | 31.32 | 0.22 | 0.021 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 619 | None | classic | 0.57 | False | 110382 | 0.168 | 28.9 | 31.32 | 0.22 | 0.021 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 619 | None | classic | 0.57 | False | 110382 | 0.168 | 29.3 | 31.32 | 0.22 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 587 | None | classic | 0.52 | False | 115311 | 0.170 | 27.5 | 31.82 | 0.17 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 587 | None | classic | 0.52 | False | 115311 | 0.170 | 27.8 | 31.82 | 0.17 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 587 | None | classic | 0.52 | False | 115311 | 0.170 | 31.9 | 31.82 | 0.17 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 587 | None | classic | 0.52 | False | 115311 | 0.170 | 27.7 | 31.82 | 0.17 | 0.015 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 473227 | 0.804 | 53.9 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 604 | None | classic | 0.55 | False | 112614 | 0.322 | 40.3 | 31.59 | 0.11 | 0.011 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 604 | None | classic | 0.55 | False | 112614 | 0.322 | 26.7 | 31.59 | 0.11 | 0.011 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 604 | None | classic | 0.55 | False | 112614 | 0.322 | 29.0 | 31.59 | 0.11 | 0.011 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 604 | None | classic | 0.55 | False | 112614 | 0.322 | 27.6 | 31.59 | 0.11 | 0.011 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 572 | None | classic | 0.49 | False | 111091 | 0.170 | 27.4 | 31.43 | 0.19 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 572 | None | classic | 0.49 | False | 111091 | 0.170 | 27.6 | 31.43 | 0.19 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 572 | None | classic | 0.49 | False | 111091 | 0.170 | 27.5 | 31.43 | 0.19 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 572 | None | classic | 0.49 | False | 111091 | 0.170 | 27.7 | 31.43 | 0.19 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.852 | 0.009 |
| in035 | mask_ent | 0.779 | 0.009 |
| in035 | mask_grad | 0.507 | 0.009 |
| in035 | r_col | 0.644 | 0.009 |
| in035 | r_warp | 0.880 | 0.009 |
