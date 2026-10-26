# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 4.7% | 25.71 / 0.0091 | 22.49 / 0.0169 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.9% | 25.79 / 0.0095 | 21.99 / 0.0169 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.8% | 25.75 / 0.0094 | 22.26 / 0.0171 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.9% | 25.77 / 0.0097 | 21.93 / 0.0170 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.7% | 25.64 / 0.0090 | 21.87 / 0.0186 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.8% | 25.79 / 0.0094 | 20.88 / 0.0187 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.8% | 25.66 / 0.0094 | 21.11 / 0.0192 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.8% | 25.70 / 0.0092 | 20.73 / 0.0183 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 4.9% | 25.67 / 0.0098 | 22.52 / 0.0294 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 8.9% | 26.16 / 0.0105 | 21.21 / 0.0317 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.2% | 26.26 / 0.0111 | 22.37 / 0.0234 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.1% | 26.21 / 0.0110 | 22.26 / 0.0271 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.2% | 26.22 / 0.0109 | 22.32 / 0.0246 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 8.9% | 26.15 / 0.0103 | 21.58 / 0.0298 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.3% | 26.26 / 0.0103 | 23.35 / 0.0204 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.1% | 26.19 / 0.0103 | 22.96 / 0.0257 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.2% | 26.23 / 0.0102 | 23.23 / 0.0224 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 8.8% | 26.01 / 0.0108 | 23.10 / 0.0297 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 1.6% | 25.50 / 0.0420 | 25.53 / 0.0251 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 1.7% | 25.84 / 0.0320 | 25.77 / 0.0221 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 1.6% | 25.60 / 0.0283 | 25.71 / 0.0227 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 1.6% | 25.70 / 0.0281 | 25.67 / 0.0227 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 1.4% | 25.12 / 0.0267 | 27.53 / 0.0122 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 1.5% | 25.25 / 0.0287 | 28.95 / 0.0113 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 1.5% | 25.16 / 0.0280 | 28.69 / 0.0108 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 1.5% | 25.18 / 0.0285 | 29.05 / 0.0101 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.18 / 0.0517 | 35.95 / 0.0248 | 20.95 / 0.0114 | 29.75 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.81 / 0.0565 | 35.95 / 0.0248 | 20.60 / 0.0126 | 29.68 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.72 / 0.0547 | 35.95 / 0.0248 | 20.52 / 0.0116 | 29.67 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.80 / 0.0556 | 35.95 / 0.0248 | 20.60 / 0.0118 | 29.70 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.72 / 0.0550 | 35.95 / 0.0248 | 20.51 / 0.0117 | 29.68 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.73 / 0.0570 | 35.95 / 0.0248 | 20.37 / 0.0130 | 29.69 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.48 / 0.0550 | 35.95 / 0.0248 | 20.11 / 0.0124 | 29.61 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.58 / 0.0561 | 35.95 / 0.0248 | 20.23 / 0.0126 | 29.66 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.46 / 0.0552 | 35.95 / 0.0248 | 20.09 / 0.0123 | 29.63 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.99 / 0.0572 | 35.95 / 0.0248 | 20.89 / 0.0146 | 29.74 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.91 / 0.0694 | 35.95 / 0.0248 | 20.30 / 0.0161 | 29.10 / 0.0449 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.21 / 0.0620 | 35.95 / 0.0248 | 20.57 / 0.0140 | 29.25 / 0.0429 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.23 / 0.0660 | 35.95 / 0.0248 | 20.52 / 0.0147 | 29.31 / 0.0436 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.22 / 0.0635 | 35.95 / 0.0248 | 20.56 / 0.0142 | 29.28 / 0.0431 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.12 / 0.0680 | 35.95 / 0.0248 | 20.33 / 0.0153 | 29.33 / 0.0438 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.63 / 0.0607 | 35.96 / 0.0248 | 20.83 / 0.0128 | 29.55 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.54 / 0.0648 | 35.96 / 0.0248 | 20.66 / 0.0140 | 29.54 / 0.0423 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.61 / 0.0626 | 35.96 / 0.0248 | 20.81 / 0.0132 | 29.54 / 0.0417 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.81 / 0.0607 | 36.29 / 0.0251 | 20.74 / 0.0153 | 29.72 / 0.0391 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 28.09 / 0.0529 | 35.99 / 0.0254 | 20.94 / 0.0110 | 29.69 / 0.0383 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.11 / 0.0521 | 35.97 / 0.0258 | 21.00 / 0.0107 | 29.69 / 0.0383 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.10 / 0.0525 | 35.99 / 0.0257 | 21.02 / 0.0108 | 29.67 / 0.0383 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.09 / 0.0522 | 35.98 / 0.0258 | 20.99 / 0.0108 | 29.67 / 0.0383 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.22 / 0.0521 | 36.01 / 0.0257 | 21.11 / 0.0109 | 29.74 / 0.0379 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.25 / 0.0515 | 36.00 / 0.0254 | 21.13 / 0.0108 | 29.75 / 0.0379 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.24 / 0.0518 | 36.00 / 0.0257 | 21.12 / 0.0108 | 29.74 / 0.0379 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.25 / 0.0516 | 36.00 / 0.0255 | 21.13 / 0.0108 | 29.74 / 0.0379 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.7%） | — | — | 28.18 / 0.0517 | 35.95 / 0.0248 | 29.75 |
| in035 | rife | 0.8% | 1.6% | 28.09 / 0.0529 | 35.99 / 0.0254 | 29.69 |
| in035 | cnw_cnn | 3.0% | 4.7% | 27.81 / 0.0565 | 35.95 / 0.0248 | 29.68 |
| in035 | cnw_f5 | 5.9% | 8.9% | 26.91 / 0.0694 | 35.95 / 0.0248 | 29.10 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.39 / 0.0542 | -0.07 / +0.0016 (core 1.0%) | -0.46 / +0.0063 (core 3.9%) | -1.22 / +0.0197 (core 6.8%) |
| in035 | 2 | 0-3 | 28.60 / 0.0519 | -0.24 / +0.0024 (core 1.0%) | -0.46 / +0.0065 (core 3.9%) | -1.63 / +0.0230 (core 6.8%) |
| in035 | 4 | 3-5 | 28.56 / 0.0489 | +0.02 / -0.0004 (core 0.2%) | -0.20 / +0.0018 (core 0.8%) | -0.96 / +0.0104 (core 2.9%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.18 / 0.0517 | — | 29.75 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.81 / 0.0565 | — | 29.68 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 28.01 / 0.0529 | — | 29.75 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.72 / 0.0547 | — | 29.67 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.95 / 0.0522 | — | 29.75 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.80 / 0.0556 | — | 29.70 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 28.00 / 0.0525 | — | 29.75 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.72 / 0.0550 | — | 29.68 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.95 / 0.0522 | — | 29.75 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.73 / 0.0570 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.93 / 0.0535 | — | 29.75 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.48 / 0.0550 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.78 / 0.0524 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.58 / 0.0561 | — | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.85 / 0.0529 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.46 / 0.0552 | — | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.77 / 0.0524 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.99 / 0.0572 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.3% | 28.12 / 0.0548 | — | 29.75 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.91 / 0.0694 | — | 29.10 | 0/3 |
| in035 | cnw_f5 | oracle | 1.6% | 27.82 / 0.0572 | — | 29.72 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.21 / 0.0620 | — | 29.25 | 0/3 |
| in035 | cnw_f5 | oracle | 1.6% | 27.96 / 0.0541 | — | 29.72 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.23 / 0.0660 | — | 29.31 | 0/3 |
| in035 | cnw_f5 | oracle | 1.7% | 27.95 / 0.0555 | — | 29.73 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.22 / 0.0635 | — | 29.28 | 0/3 |
| in035 | cnw_f5 | oracle | 1.7% | 27.96 / 0.0546 | — | 29.73 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.12 / 0.0680 | — | 29.33 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.6% | 27.85 / 0.0566 | — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.63 / 0.0607 | — | 29.55 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.7% | 28.09 / 0.0535 | — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.54 / 0.0648 | — | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.7% | 28.01 / 0.0551 | — | 29.75 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.61 / 0.0626 | — | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.7% | 28.08 / 0.0542 | — | 29.74 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.81 / 0.0607 | — | 29.72 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.7% | 28.05 / 0.0557 | — | 29.75 | 0/3 |
| in035 | rife | 不复核 | —% | 28.09 / 0.0529 | — | 29.69 | 1/3 |
| in035 | rife | oracle | 0.3% | 28.18 / 0.0513 | — | 29.75 | 1/3 |
| in035 | rife | 不复核 | —% | 28.11 / 0.0521 | — | 29.69 | 1/3 |
| in035 | rife | oracle | 0.3% | 28.20 / 0.0509 | — | 29.75 | 2/3 |
| in035 | rife | 不复核 | —% | 28.10 / 0.0525 | — | 29.67 | 1/3 |
| in035 | rife | oracle | 0.3% | 28.21 / 0.0511 | — | 29.75 | 3/3 |
| in035 | rife | 不复核 | —% | 28.09 / 0.0522 | — | 29.67 | 1/3 |
| in035 | rife | oracle | 0.3% | 28.20 / 0.0510 | — | 29.75 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.22 / 0.0521 | — | 29.74 | 1/3 |
| in035 | rife_mw | oracle | 0.3% | 28.25 / 0.0512 | — | 29.75 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.25 / 0.0515 | — | 29.75 | 1/3 |
| in035 | rife_mw | oracle | 0.3% | 28.26 / 0.0509 | — | 29.75 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.24 / 0.0518 | — | 29.74 | 1/3 |
| in035 | rife_mw | oracle | 0.3% | 28.25 / 0.0510 | — | 29.75 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.25 / 0.0516 | — | 29.74 | 1/3 |
| in035 | rife_mw | oracle | 0.3% | 28.25 / 0.0509 | — | 29.75 | 3/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.18 / 0.0517 | — / — | — |
| in035 | FF | 0（前馈） | 884×821（67%） | 27.42 | 27.81 / 0.0565 | — / — | 0/3 |
| in035 | 25 | 0.47 s | 884×821（67%） | 27.95 | 27.80 / 0.0556 | — / — | 0/3 |
| in035 | 50 | 0.92 s | 884×821（67%） | 28.18 | 27.72 / 0.0550 | — / — | 0/3 |
| in035 | 100 | 1.80 s | 884×821（67%） | 28.41 | 27.72 / 0.0547 | — / — | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.18 / 0.0517 | — / — | 29.75 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.81 / 0.0565 | — / — | 29.68 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.01 / 0.0529 | — / — | 29.75 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.80 / 0.0556 | — / — | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.00 / 0.0525 | — / — | 29.75 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.72 / 0.0550 | — / — | 29.68 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.95 / 0.0522 | — / — | 29.75 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.72 / 0.0547 | — / — | 29.67 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.95 / 0.0522 | — / — | 29.75 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.73 / 0.0570 | — / — | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.93 / 0.0535 | — / — | 29.75 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.58 / 0.0561 | — / — | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.85 / 0.0529 | — / — | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.46 / 0.0552 | — / — | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.77 / 0.0524 | — / — | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.48 / 0.0550 | — / — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.78 / 0.0524 | — / — | 29.74 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.91 / 0.0694 | — / — | 29.10 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.82 / 0.0572 | — / — | 29.72 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.23 / 0.0660 | — / — | 29.31 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.95 / 0.0555 | — / — | 29.73 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.22 / 0.0635 | — / — | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.96 / 0.0546 | — / — | 29.73 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.21 / 0.0620 | — / — | 29.25 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.96 / 0.0541 | — / — | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.12 / 0.0680 | — / — | 29.33 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.85 / 0.0566 | — / — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.54 / 0.0648 | — / — | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.01 / 0.0551 | — / — | 29.75 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.61 / 0.0626 | — / — | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.08 / 0.0542 | — / — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.63 / 0.0607 | — / — | 29.55 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.09 / 0.0535 | — / — | 29.74 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 28.09 / 0.0529 | — / — | 29.69 | 1/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.18 / 0.0513 | — / — | 29.75 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.10 / 0.0525 | — / — | 29.67 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.21 / 0.0511 | — / — | 29.75 | 3/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.09 / 0.0522 | — / — | 29.67 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.20 / 0.0510 | — / — | 29.75 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.11 / 0.0521 | — / — | 29.69 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.20 / 0.0509 | — / — | 29.75 | 2/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.22 / 0.0521 | — / — | 29.74 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.25 / 0.0512 | — / — | 29.75 | 3/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.24 / 0.0518 | — / — | 29.74 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.25 / 0.0510 | — / — | 29.75 | 3/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.25 / 0.0516 | — / — | 29.74 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.25 / 0.0509 | — / — | 29.75 | 3/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.25 / 0.0515 | — / — | 29.75 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.26 / 0.0509 | — / — | 29.75 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 35.95 / 0.0248 | 20.95 / 0.0114 | 29.75 / 0.0376 | 28.18 / 0.0517 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 35.95 | 0.9176 | 0.0248 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.47 | 0.5456 | 0.7135 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.49 | 0.5448 | 0.7123 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.47 | 0.5459 | 0.7137 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.48 | 0.5455 | 0.7127 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.47 | 0.5420 | 0.7141 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.53 | 0.5384 | 0.7155 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.48 | 0.5418 | 0.7141 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.50 | 0.5401 | 0.7149 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 8.10 | 0.0231 | 0.6380 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.89 | 0.5458 | 0.6909 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.96 | 0.5480 | 0.6877 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.91 | 0.5477 | 0.6896 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.94 | 0.5483 | 0.6887 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.86 | 0.5466 | 0.6909 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.94 | 0.5483 | 0.6853 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.89 | 0.5488 | 0.6898 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.91 | 0.5487 | 0.6881 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 8.48 | 0.0781 | 0.6360 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.83 | 0.6455 | 0.5537 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.97 | 0.6474 | 0.5394 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.86 | 0.6491 | 0.5474 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.91 | 0.6499 | 0.5423 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.77 | 0.6448 | 0.5516 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.87 | 0.6438 | 0.5503 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.80 | 0.6458 | 0.5498 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.84 | 0.6451 | 0.5508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 35.96 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 35.96 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 35.96 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 36.22 | 0.9184 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 35.95 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 35.96 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 35.96 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 35.96 | 0.9176 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 36.29 | 0.9185 | 0.0251 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 35.99 | 0.9188 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 35.97 | 0.9185 | 0.0258 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 35.99 | 0.9189 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 35.98 | 0.9188 | 0.0258 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 36.01 | 0.9190 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 36.00 | 0.9187 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 36.00 | 0.9191 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 36.00 | 0.9189 | 0.0255 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.95 | 0.7269 | 0.0114 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.25 | 0.2862 | 0.1108 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.29 | 0.2818 | 0.1079 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.27 | 0.2914 | 0.1092 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.27 | 0.2859 | 0.1087 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.22 | 0.2726 | 0.1112 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.25 | 0.2594 | 0.1100 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.22 | 0.2680 | 0.1109 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.23 | 0.2606 | 0.1106 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.46 | 0.2684 | 0.0762 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.39 | 0.3177 | 0.0970 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.46 | 0.3428 | 0.0931 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.42 | 0.3371 | 0.0948 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.44 | 0.3404 | 0.0939 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.39 | 0.3315 | 0.0961 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.49 | 0.3695 | 0.0920 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.43 | 0.3583 | 0.0940 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.46 | 0.3656 | 0.0928 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.55 | 0.3753 | 0.0640 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.38 | 0.1202 | 0.1459 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.39 | 0.1220 | 0.1452 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.38 | 0.1234 | 0.1457 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.38 | 0.1227 | 0.1454 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.38 | 0.1287 | 0.1459 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.38 | 0.1324 | 0.1449 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.38 | 0.1317 | 0.1453 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.38 | 0.1324 | 0.1450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.62 | 0.7198 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.53 | 0.7222 | 0.0115 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.61 | 0.7225 | 0.0117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.52 | 0.7215 | 0.0115 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.39 | 0.7051 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.12 | 0.7043 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.24 | 0.7040 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.10 | 0.7018 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.89 | 0.7312 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 20.32 | 0.7010 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.58 | 0.7199 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.54 | 0.7133 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.57 | 0.7160 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.35 | 0.7054 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.83 | 0.7306 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.66 | 0.7234 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.81 | 0.7288 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.74 | 0.7295 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.94 | 0.7369 | 0.0109 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.99 | 0.7379 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.01 | 0.7397 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.98 | 0.7389 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.11 | 0.7424 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.13 | 0.7446 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.11 | 0.7444 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.13 | 0.7449 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.60 | 0.7188 | 0.0126 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.52 | 0.7215 | 0.0116 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.60 | 0.7219 | 0.0118 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.51 | 0.7209 | 0.0117 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.37 | 0.7040 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.11 | 0.7034 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.23 | 0.7031 | 0.0126 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.09 | 0.7007 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.89 | 0.7304 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 20.30 | 0.6993 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.57 | 0.7185 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.52 | 0.7118 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.56 | 0.7146 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.33 | 0.7036 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.83 | 0.7297 | 0.0128 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.66 | 0.7222 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.81 | 0.7278 | 0.0132 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.74 | 0.7282 | 0.0153 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.94 | 0.7367 | 0.0110 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.00 | 0.7380 | 0.0107 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.02 | 0.7396 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.99 | 0.7389 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.11 | 0.7422 | 0.0109 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.13 | 0.7447 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.12 | 0.7447 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.13 | 0.7450 | 0.0108 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 22.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.41 | 0.7779 | 0.0165 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.03 | 0.4179 | 0.2150 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.07 | 0.4205 | 0.2099 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.04 | 0.4284 | 0.2130 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.05 | 0.4251 | 0.2115 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.00 | 0.4113 | 0.2149 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.04 | 0.4088 | 0.2112 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.01 | 0.4163 | 0.2137 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.02 | 0.4121 | 0.2126 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.66 | 0.2517 | 0.1606 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.96 | 0.4420 | 0.1917 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.04 | 0.4700 | 0.1828 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.99 | 0.4664 | 0.1878 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.01 | 0.4695 | 0.1852 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.96 | 0.4484 | 0.1905 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.05 | 0.4836 | 0.1811 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.99 | 0.4788 | 0.1866 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.01 | 0.4836 | 0.1836 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.20 | 0.3473 | 0.1434 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.29 | 0.3064 | 0.2574 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.32 | 0.3076 | 0.2544 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.30 | 0.3097 | 0.2565 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.31 | 0.3089 | 0.2557 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.28 | 0.3109 | 0.2570 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.30 | 0.3129 | 0.2550 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.28 | 0.3152 | 0.2563 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.29 | 0.3148 | 0.2557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.96 | 0.7721 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.93 | 0.7748 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.02 | 0.7754 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.92 | 0.7750 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.74 | 0.7670 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.49 | 0.7676 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.61 | 0.7680 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.46 | 0.7672 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.10 | 0.7742 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.54 | 0.7614 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.89 | 0.7727 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.85 | 0.7699 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.87 | 0.7712 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.54 | 0.7632 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.18 | 0.7773 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.95 | 0.7740 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.11 | 0.7763 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.88 | 0.7708 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.39 | 0.7807 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.45 | 0.7816 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.48 | 0.7821 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.44 | 0.7819 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.59 | 0.7834 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.62 | 0.7845 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.60 | 0.7844 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.61 | 0.7846 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.49 | 0.7611 | 0.0212 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.36 | 0.7653 | 0.0196 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.50 | 0.7676 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.35 | 0.7664 | 0.0200 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.27 | 0.7543 | 0.0218 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.79 | 0.7545 | 0.0203 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.97 | 0.7568 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.75 | 0.7547 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.07 | 0.7542 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.00 | 0.7232 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.52 | 0.7441 | 0.0238 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.51 | 0.7397 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.51 | 0.7424 | 0.0246 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.17 | 0.7278 | 0.0275 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.13 | 0.7549 | 0.0220 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.89 | 0.7498 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.05 | 0.7535 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.30 | 0.7341 | 0.0322 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.19 | 0.7773 | 0.0185 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.17 | 0.7778 | 0.0183 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.27 | 0.7795 | 0.0185 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.21 | 0.7789 | 0.0184 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.48 | 0.7814 | 0.0169 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.55 | 0.7840 | 0.0174 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.55 | 0.7848 | 0.0166 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.57 | 0.7848 | 0.0168 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 39.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.77 | 0.7320 | 0.0266 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.84 | 0.3521 | 0.3610 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.89 | 0.3557 | 0.3552 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.86 | 0.3613 | 0.3584 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.87 | 0.3585 | 0.3567 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.84 | 0.3498 | 0.3609 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.88 | 0.3455 | 0.3560 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.85 | 0.3531 | 0.3589 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.86 | 0.3484 | 0.3574 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.36 | 0.2550 | 0.2223 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.93 | 0.3902 | 0.3332 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.00 | 0.4131 | 0.3213 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.95 | 0.4121 | 0.3272 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.97 | 0.4137 | 0.3242 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.93 | 0.3988 | 0.3308 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.02 | 0.4267 | 0.3181 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.97 | 0.4247 | 0.3253 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.99 | 0.4273 | 0.3215 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.72 | 0.3562 | 0.1939 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.52 | 0.2551 | 0.4068 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.53 | 0.2568 | 0.4038 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.52 | 0.2580 | 0.4056 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.53 | 0.2572 | 0.4046 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.50 | 0.2583 | 0.4061 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.52 | 0.2611 | 0.4033 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.51 | 0.2618 | 0.4048 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.51 | 0.2616 | 0.4042 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.39 | 0.7284 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.31 | 0.7296 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.40 | 0.7300 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.31 | 0.7296 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.23 | 0.7256 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.00 | 0.7253 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.11 | 0.7257 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.98 | 0.7250 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.60 | 0.7315 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.07 | 0.7218 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.36 | 0.7279 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.33 | 0.7265 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.35 | 0.7272 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.08 | 0.7231 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.54 | 0.7309 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.40 | 0.7292 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.51 | 0.7304 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.43 | 0.7302 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.76 | 0.7333 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.80 | 0.7338 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.82 | 0.7342 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.80 | 0.7340 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.90 | 0.7350 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.92 | 0.7357 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.91 | 0.7357 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.92 | 0.7358 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.00 | 0.7226 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.84 | 0.7246 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.99 | 0.7262 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.84 | 0.7253 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.85 | 0.7191 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.43 | 0.7182 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.58 | 0.7198 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.39 | 0.7184 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.33 | 0.7279 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.73 | 0.6983 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.23 | 0.7115 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.25 | 0.7098 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.24 | 0.7112 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.92 | 0.7020 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.72 | 0.7191 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.56 | 0.7164 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.67 | 0.7185 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.95 | 0.7229 | 0.0348 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.58 | 0.7313 | 0.0278 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.62 | 0.7321 | 0.0270 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.60 | 0.7326 | 0.0274 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.58 | 0.7324 | 0.0271 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.84 | 0.7342 | 0.0271 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.92 | 0.7361 | 0.0264 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.89 | 0.7361 | 0.0267 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.91 | 0.7362 | 0.0265 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.75 | 0.7113 | 0.0376 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.89 | 0.3047 | 0.4122 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.94 | 0.3065 | 0.4065 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.91 | 0.3106 | 0.4100 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.92 | 0.3087 | 0.4082 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.90 | 0.3052 | 0.4117 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.95 | 0.3039 | 0.4065 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.91 | 0.3091 | 0.4102 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.93 | 0.3062 | 0.4085 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.53 | 0.1641 | 0.2997 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.64 | 0.3448 | 0.3857 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.70 | 0.3566 | 0.3740 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.66 | 0.3592 | 0.3804 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.68 | 0.3584 | 0.3772 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.65 | 0.3516 | 0.3840 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.72 | 0.3641 | 0.3704 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.68 | 0.3664 | 0.3777 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.69 | 0.3659 | 0.3737 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.61 | 0.2476 | 0.2692 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.00 | 0.2429 | 0.4463 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.02 | 0.2434 | 0.4442 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.01 | 0.2439 | 0.4456 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.01 | 0.2435 | 0.4449 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 1.99 | 0.2422 | 0.4455 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.00 | 0.2428 | 0.4435 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 1.99 | 0.2434 | 0.4446 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 1.99 | 0.2431 | 0.4440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.75 | 0.7114 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.75 | 0.7114 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.75 | 0.7114 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.75 | 0.7114 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.75 | 0.7114 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.74 | 0.7113 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.74 | 0.7113 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.74 | 0.7113 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.75 | 0.7115 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.72 | 0.7109 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.72 | 0.7110 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.73 | 0.7111 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.73 | 0.7111 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.74 | 0.7111 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.74 | 0.7113 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.75 | 0.7113 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.74 | 0.7113 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.75 | 0.7116 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.68 | 0.7109 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.67 | 0.7110 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.70 | 0.7114 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.68 | 0.7112 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.69 | 0.7108 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7105 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.66 | 0.7110 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.63 | 0.7108 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.74 | 0.7116 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.10 | 0.7062 | 0.0449 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.25 | 0.7079 | 0.0429 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.31 | 0.7088 | 0.0436 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.28 | 0.7085 | 0.0431 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.33 | 0.7076 | 0.0438 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.55 | 0.7105 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.54 | 0.7107 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.54 | 0.7106 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.72 | 0.7120 | 0.0391 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.69 | 0.7111 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.69 | 0.7111 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.67 | 0.7111 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.67 | 0.7111 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.74 | 0.7113 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.75 | 0.7114 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.74 | 0.7114 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.74 | 0.7114 | 0.0379 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.18 | 0.7209 | 0.0517 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.21 | 0.3146 | 0.4678 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.26 | 0.3167 | 0.4568 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.23 | 0.3213 | 0.4629 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.24 | 0.3191 | 0.4594 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.22 | 0.3137 | 0.4665 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.26 | 0.3113 | 0.4569 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.23 | 0.3172 | 0.4627 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.24 | 0.3137 | 0.4595 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.34 | 0.1878 | 0.3785 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.97 | 0.3508 | 0.4418 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.03 | 0.3658 | 0.4199 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.99 | 0.3671 | 0.4319 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.01 | 0.3670 | 0.4254 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.98 | 0.3587 | 0.4397 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.04 | 0.3765 | 0.4176 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.00 | 0.3769 | 0.4305 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.02 | 0.3776 | 0.4235 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.55 | 0.2764 | 0.3345 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.18 | 0.2367 | 0.5232 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.19 | 0.2375 | 0.5194 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.18 | 0.2381 | 0.5219 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.19 | 0.2377 | 0.5206 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.17 | 0.2377 | 0.5206 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.17 | 0.2391 | 0.5175 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.17 | 0.2394 | 0.5191 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.17 | 0.2393 | 0.5183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.01 | 0.7195 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.95 | 0.7199 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.00 | 0.7201 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.95 | 0.7199 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.93 | 0.7183 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7180 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.85 | 0.7182 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.77 | 0.7179 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.12 | 0.7209 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.82 | 0.7164 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.96 | 0.7189 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.95 | 0.7184 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.96 | 0.7187 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.85 | 0.7172 | 0.0566 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.09 | 0.7205 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.01 | 0.7198 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7204 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.05 | 0.7204 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.18 | 0.7214 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.20 | 0.7216 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.21 | 0.7217 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.20 | 0.7217 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.25 | 0.7221 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.26 | 0.7224 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.25 | 0.7224 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.25 | 0.7224 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.81 | 0.7171 | 0.0565 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.72 | 0.7179 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.80 | 0.7187 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.72 | 0.7183 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.73 | 0.7156 | 0.0570 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.48 | 0.7151 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.58 | 0.7160 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.46 | 0.7152 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.99 | 0.7195 | 0.0572 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.91 | 0.7050 | 0.0694 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.21 | 0.7106 | 0.0620 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.23 | 0.7105 | 0.0660 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.22 | 0.7107 | 0.0635 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.12 | 0.7073 | 0.0680 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.63 | 0.7156 | 0.0607 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.54 | 0.7146 | 0.0648 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.61 | 0.7154 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.81 | 0.7179 | 0.0607 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.09 | 0.7205 | 0.0529 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.11 | 0.7209 | 0.0521 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.10 | 0.7211 | 0.0525 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.09 | 0.7210 | 0.0522 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.22 | 0.7218 | 0.0521 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.25 | 0.7225 | 0.0515 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.24 | 0.7225 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.25 | 0.7225 | 0.0516 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1027 | None | classic | 1.58 | False | 189427 | 0.172 | 28.9 | 29.01 | 0.14 | 0.019 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1027 | None | classic | 1.58 | False | 189427 | 0.172 | 37.2 | 29.01 | 0.14 | 0.019 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1027 | None | classic | 1.58 | False | 189427 | 0.172 | 32.5 | 29.01 | 0.14 | 0.019 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1027 | None | classic | 1.58 | False | 189427 | 0.172 | 29.0 | 29.01 | 0.14 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 995 | None | classic | 1.48 | False | 185178 | 0.173 | 34.1 | 28.61 | 0.25 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 995 | None | classic | 1.48 | False | 185178 | 0.173 | 35.5 | 28.61 | 0.25 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 995 | None | classic | 1.48 | False | 185178 | 0.173 | 32.7 | 28.61 | 0.25 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 995 | None | classic | 1.48 | False | 185178 | 0.173 | 33.0 | 28.61 | 0.25 | 0.011 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 697503 | 0.790 | 147.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1224 | None | classic | 2.24 | False | 312217 | 0.166 | 35.9 | 29.30 | 0.07 | 0.006 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1224 | None | classic | 2.24 | False | 312217 | 0.166 | 40.1 | 29.30 | 0.07 | 0.006 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1224 | None | classic | 2.24 | False | 312217 | 0.166 | 33.9 | 29.30 | 0.07 | 0.006 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1224 | None | classic | 2.24 | False | 312217 | 0.166 | 37.5 | 29.30 | 0.07 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1192 | None | classic | 2.12 | False | 286262 | 0.169 | 34.8 | 29.55 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1192 | None | classic | 2.12 | False | 286262 | 0.169 | 36.5 | 29.55 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1192 | None | classic | 2.12 | False | 286262 | 0.169 | 37.9 | 29.55 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1192 | None | classic | 2.12 | False | 286262 | 0.169 | 33.8 | 29.55 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1063573 | 0.790 | 66.0 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 878 | None | classic | 1.15 | False | 171015 | 0.320 | 44.0 | 27.99 | 0.11 | 0.018 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 878 | None | classic | 1.15 | False | 171015 | 0.320 | 35.3 | 27.99 | 0.11 | 0.018 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 878 | None | classic | 1.15 | False | 171015 | 0.320 | 27.4 | 27.99 | 0.11 | 0.018 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 878 | None | classic | 1.15 | False | 171015 | 0.320 | 28.9 | 27.99 | 0.11 | 0.018 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 519 | None | classic | 0.40 | False | 341924 | 0.342 | 55.9 | 30.92 | 0.13 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 519 | None | classic | 0.40 | False | 341924 | 0.342 | 60.3 | 30.92 | 0.13 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 519 | None | classic | 0.40 | False | 341924 | 0.342 | 53.8 | 30.92 | 0.13 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 519 | None | classic | 0.40 | False | 341924 | 0.342 | 55.3 | 30.92 | 0.13 | 0.010 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.611 | 0.020 |
| in035 | mask_ent | 0.754 | 0.020 |
| in035 | mask_grad | 0.428 | 0.020 |
| in035 | r_col | 0.689 | 0.020 |
| in035 | r_warp | 0.863 | 0.020 |
