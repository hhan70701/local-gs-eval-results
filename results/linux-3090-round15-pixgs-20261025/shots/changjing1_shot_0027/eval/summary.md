# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 28.1% | 23.16 / 0.0271 | 21.20 / 0.0683 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 28.7% | 23.08 / 0.0270 | 21.59 / 0.0554 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 28.4% | 23.14 / 0.0268 | 21.79 / 0.0606 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 28.5% | 23.12 / 0.0267 | 21.70 / 0.0579 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 28.0% | 23.14 / 0.0270 | 21.15 / 0.0676 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 28.7% | 23.08 / 0.0273 | 21.44 / 0.0564 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 28.3% | 23.14 / 0.0267 | 21.68 / 0.0607 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 28.4% | 23.12 / 0.0269 | 21.57 / 0.0585 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 28.4% | 23.17 / 0.0280 | 21.41 / 0.0741 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 31.9% | 23.34 / 0.0262 | 21.25 / 0.0681 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 32.6% | 23.31 / 0.0264 | 21.82 / 0.0533 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 32.2% | 23.31 / 0.0263 | 21.82 / 0.0607 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 32.3% | 23.30 / 0.0262 | 21.82 / 0.0565 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 31.8% | 23.33 / 0.0272 | 21.19 / 0.0677 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 32.5% | 23.28 / 0.0275 | 21.69 / 0.0555 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 32.1% | 23.30 / 0.0274 | 21.76 / 0.0603 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 32.2% | 23.28 / 0.0273 | 21.73 / 0.0573 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 32.0% | 23.37 / 0.0274 | 21.07 / 0.0776 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 21.2% | 22.76 / 0.0215 | 21.20 / 0.0536 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 23.6% | 22.98 / 0.0224 | 21.89 / 0.0504 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 22.3% | 22.83 / 0.0219 | 21.92 / 0.0489 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 22.6% | 22.85 / 0.0221 | 22.01 / 0.0487 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 22.0% | 22.78 / 0.0211 | 22.72 / 0.0435 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 23.6% | 22.96 / 0.0219 | 22.81 / 0.0429 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 22.6% | 22.86 / 0.0214 | 22.82 / 0.0416 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 22.9% | 22.89 / 0.0217 | 22.76 / 0.0416 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.26 / 0.0511 | 23.21 / 0.0836 | 18.64 / 0.0196 | 30.26 / 0.0246 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.65 / 0.0818 | 23.02 / 0.1724 | 18.87 / 0.0268 | 29.20 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.90 / 0.0732 | 23.34 / 0.1402 | 19.32 / 0.0222 | 28.96 / 0.0326 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.08 / 0.0777 | 23.66 / 0.1563 | 19.32 / 0.0245 | 29.28 / 0.0327 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.03 / 0.0752 | 23.56 / 0.1471 | 19.37 / 0.0232 | 29.12 / 0.0329 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.62 / 0.0815 | 23.11 / 0.1685 | 18.92 / 0.0266 | 29.17 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.78 / 0.0732 | 23.18 / 0.1390 | 19.26 / 0.0223 | 28.87 / 0.0327 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.03 / 0.0776 | 23.65 / 0.1537 | 19.35 / 0.0245 | 29.22 / 0.0328 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.95 / 0.0754 | 23.50 / 0.1459 | 19.38 / 0.0234 | 29.03 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.23 / 0.0672 | 24.05 / 0.1163 | 19.52 / 0.0236 | 29.75 / 0.0277 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.40 / 0.0887 | 23.38 / 0.1675 | 18.67 / 0.0266 | 29.02 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.70 / 0.0763 | 23.87 / 0.1306 | 19.13 / 0.0216 | 28.94 / 0.0333 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.82 / 0.0830 | 24.01 / 0.1491 | 19.05 / 0.0242 | 29.15 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.78 / 0.0792 | 23.96 / 0.1377 | 19.12 / 0.0228 | 29.04 / 0.0337 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.35 / 0.0864 | 23.31 / 0.1657 | 18.68 / 0.0265 | 28.95 / 0.0338 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.61 / 0.0753 | 23.76 / 0.1331 | 19.10 / 0.0219 | 28.83 / 0.0328 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.77 / 0.0808 | 23.95 / 0.1499 | 19.05 / 0.0241 | 29.09 / 0.0329 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.72 / 0.0778 | 23.92 / 0.1395 | 19.13 / 0.0228 | 28.96 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.93 / 0.0699 | 24.13 / 0.1162 | 19.33 / 0.0240 | 29.64 / 0.0289 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.04 / 0.0759 | 23.66 / 0.1434 | 19.21 / 0.0223 | 29.69 / 0.0295 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.43 / 0.0673 | 24.31 / 0.1106 | 19.58 / 0.0184 | 29.68 / 0.0286 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.39 / 0.0712 | 24.27 / 0.1257 | 19.51 / 0.0206 | 29.73 / 0.0292 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.43 / 0.0691 | 24.36 / 0.1169 | 19.58 / 0.0195 | 29.71 / 0.0289 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.78 / 0.0666 | 24.46 / 0.1120 | 20.16 / 0.0194 | 29.92 / 0.0278 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.96 / 0.0605 | 25.15 / 0.0867 | 20.40 / 0.0175 | 29.92 / 0.0272 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.83 / 0.0652 | 24.87 / 0.1009 | 20.23 / 0.0185 | 29.92 / 0.0276 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.85 / 0.0631 | 25.00 / 0.0933 | 20.29 / 0.0178 | 29.93 / 0.0274 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 10.3%） | — | — | 26.26 / 0.0511 | 23.21 / 0.0836 | 30.26 |
| in035 | rife | 11.7% | 21.2% | 26.04 / 0.0759 | 23.66 / 0.1434 | 29.69 |
| in035 | cnw_cnn | 19.7% | 28.1% | 25.65 / 0.0818 | 23.02 / 0.1724 | 29.20 |
| in035 | cnw_f5 | 22.9% | 31.9% | 25.40 / 0.0887 | 23.38 / 0.1675 | 29.02 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.33 / 0.0590 | +0.75 / +0.0237 (core 14.2%) | +0.62 / +0.0320 (core 25.3%) | +0.54 / +0.0378 (core 29.3%) |
| in035 | 2 | 0-3 | 25.81 / 0.0512 | -0.23 / +0.0374 (core 14.2%) | -0.31 / +0.0404 (core 25.3%) | -0.68 / +0.0517 (core 29.3%) |
| in035 | 4 | 3-5 | 28.63 / 0.0432 | -1.17 / +0.0132 (core 4.9%) | -2.13 / +0.0196 (core 7.2%) | -2.44 / +0.0231 (core 9.0%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.26 / 0.0511 | 23.21 | 30.26 | — |
| in035 | cnw_cnn | 不复核 | —% | 25.65 / 0.0818 | 23.02 | 29.20 | 0/3 |
| in035 | cnw_cnn | oracle | 7.3% | 26.44 / 0.0634 | 23.95 | 30.17 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.90 / 0.0732 | 23.34 | 28.96 | 0/3 |
| in035 | cnw_cnn | oracle | 7.4% | 26.72 / 0.0576 | 24.42 | 30.14 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.08 / 0.0777 | 23.66 | 29.28 | 0/3 |
| in035 | cnw_cnn | oracle | 7.4% | 26.76 / 0.0609 | 24.47 | 30.18 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.03 / 0.0752 | 23.56 | 29.12 | 0/3 |
| in035 | cnw_cnn | oracle | 7.4% | 26.77 / 0.0591 | 24.47 | 30.16 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.62 / 0.0815 | 23.11 | 29.17 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.3% | 26.46 / 0.0632 | 24.05 | 30.17 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.78 / 0.0732 | 23.18 | 28.87 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.4% | 26.67 / 0.0576 | 24.37 | 30.13 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.03 / 0.0776 | 23.65 | 29.22 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.3% | 26.76 / 0.0607 | 24.53 | 30.17 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.95 / 0.0754 | 23.50 | 29.03 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.4% | 26.77 / 0.0591 | 24.52 | 30.15 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.23 / 0.0672 | 24.05 | 29.75 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 7.4% | 26.82 / 0.0558 | 24.81 | 30.23 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.40 / 0.0887 | 23.38 | 29.02 | 0/3 |
| in035 | cnw_f5 | oracle | 7.7% | 26.36 / 0.0634 | 24.07 | 30.19 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.70 / 0.0763 | 23.87 | 28.94 | 0/3 |
| in035 | cnw_f5 | oracle | 7.8% | 26.65 / 0.0572 | 24.53 | 30.19 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.82 / 0.0830 | 24.01 | 29.15 | 0/3 |
| in035 | cnw_f5 | oracle | 7.8% | 26.64 / 0.0608 | 24.51 | 30.20 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.78 / 0.0792 | 23.96 | 29.04 | 0/3 |
| in035 | cnw_f5 | oracle | 7.8% | 26.67 / 0.0588 | 24.54 | 30.19 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.35 / 0.0864 | 23.31 | 28.95 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.7% | 26.35 / 0.0631 | 24.06 | 30.17 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.61 / 0.0753 | 23.76 | 28.83 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.8% | 26.61 / 0.0569 | 24.50 | 30.17 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.77 / 0.0808 | 23.95 | 29.09 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.8% | 26.63 / 0.0603 | 24.51 | 30.18 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.72 / 0.0778 | 23.92 | 28.96 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.8% | 26.66 / 0.0584 | 24.55 | 30.17 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 25.93 / 0.0699 | 24.13 | 29.64 | 0/3 |
| in035 | cnw_f5_pix | oracle | 7.7% | 26.66 / 0.0564 | 24.83 | 30.23 | 0/3 |
| in035 | rife | 不复核 | —% | 26.04 / 0.0759 | 23.66 | 29.69 | 0/3 |
| in035 | rife | oracle | 5.5% | 26.67 / 0.0568 | 24.30 | 30.21 | 0/3 |
| in035 | rife | 不复核 | —% | 26.43 / 0.0673 | 24.31 | 29.68 | 0/3 |
| in035 | rife | oracle | 5.7% | 26.92 / 0.0522 | 24.80 | 30.21 | 1/3 |
| in035 | rife | 不复核 | —% | 26.39 / 0.0712 | 24.27 | 29.73 | 0/3 |
| in035 | rife | oracle | 5.6% | 26.89 / 0.0548 | 24.71 | 30.21 | 0/3 |
| in035 | rife | 不复核 | —% | 26.43 / 0.0691 | 24.36 | 29.71 | 0/3 |
| in035 | rife | oracle | 5.6% | 26.92 / 0.0532 | 24.80 | 30.21 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 26.78 / 0.0666 | 24.46 | 29.92 | 0/3 |
| in035 | rife_mw | oracle | 5.5% | 27.16 / 0.0526 | 25.00 | 30.24 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.96 / 0.0605 | 25.15 | 29.92 | 0/3 |
| in035 | rife_mw | oracle | 5.6% | 27.33 / 0.0498 | 25.60 | 30.24 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 26.83 / 0.0652 | 24.87 | 29.92 | 0/3 |
| in035 | rife_mw | oracle | 5.6% | 27.25 / 0.0514 | 25.28 | 30.24 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 26.85 / 0.0631 | 25.00 | 29.93 | 0/3 |
| in035 | rife_mw | oracle | 5.6% | 27.28 / 0.0504 | 25.43 | 30.24 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 26.26 / 0.0511 | 23.21 / 0.0836 | — |
| in035 | FF | 0（前馈） | 1008×649（61%） | 26.85 | 25.65 / 0.0818 | 23.02 / 0.1724 | 0/3 |
| in035 | 25 | 1.36 s | 1008×649（61%） | 27.87 | 26.08 / 0.0777 | 23.66 / 0.1563 | 0/3 |
| in035 | 50 | 2.72 s | 1008×649（61%） | 28.38 | 26.03 / 0.0752 | 23.56 / 0.1471 | 0/3 |
| in035 | 100 | 5.47 s | 1008×649（61%） | 28.91 | 25.90 / 0.0732 | 23.34 / 0.1402 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.26 / 0.0511 | 23.21 / 0.0836 | 30.26 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 25.65 / 0.0818 | 23.02 / 0.1724 | 29.20 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 26.44 / 0.0634 | 23.95 / 0.1240 | 30.17 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.08 / 0.0777 | 23.66 / 0.1563 | 29.28 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 26.76 / 0.0609 | 24.47 / 0.1136 | 30.18 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.03 / 0.0752 | 23.56 / 0.1471 | 29.12 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 26.77 / 0.0591 | 24.47 / 0.1060 | 30.16 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 25.90 / 0.0732 | 23.34 / 0.1402 | 28.96 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 26.72 / 0.0576 | 24.42 / 0.0994 | 30.14 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 25.62 / 0.0815 | 23.11 / 0.1685 | 29.17 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 26.46 / 0.0632 | 24.05 / 0.1212 | 30.17 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 26.03 / 0.0776 | 23.65 / 0.1537 | 29.22 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 26.76 / 0.0607 | 24.53 / 0.1112 | 30.17 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 25.95 / 0.0754 | 23.50 / 0.1459 | 29.03 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 26.77 / 0.0591 | 24.52 / 0.1047 | 30.15 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 25.78 / 0.0732 | 23.18 / 0.1390 | 28.87 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 26.67 / 0.0576 | 24.37 / 0.0983 | 30.13 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 25.40 / 0.0887 | 23.38 / 0.1675 | 29.02 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.36 / 0.0634 | 24.07 / 0.1196 | 30.19 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 25.82 / 0.0830 | 24.01 / 0.1491 | 29.15 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 26.64 / 0.0608 | 24.51 / 0.1087 | 30.20 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 25.78 / 0.0792 | 23.96 / 0.1377 | 29.04 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 26.67 / 0.0588 | 24.54 / 0.1004 | 30.19 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 25.70 / 0.0763 | 23.87 / 0.1306 | 28.94 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 26.65 / 0.0572 | 24.53 / 0.0933 | 30.19 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 25.35 / 0.0864 | 23.31 / 0.1657 | 28.95 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.35 / 0.0631 | 24.06 / 0.1187 | 30.17 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 25.77 / 0.0808 | 23.95 / 0.1499 | 29.09 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 26.63 / 0.0603 | 24.51 / 0.1085 | 30.18 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 25.72 / 0.0778 | 23.92 / 0.1395 | 28.96 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 26.66 / 0.0584 | 24.55 / 0.1001 | 30.17 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 25.61 / 0.0753 | 23.76 / 0.1331 | 28.83 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 26.61 / 0.0569 | 24.50 / 0.0936 | 30.17 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.04 / 0.0759 | 23.66 / 0.1434 | 29.69 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.67 / 0.0568 | 24.30 / 0.0992 | 30.21 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.39 / 0.0712 | 24.27 / 0.1257 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 26.89 / 0.0548 | 24.71 / 0.0892 | 30.21 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.43 / 0.0691 | 24.36 / 0.1169 | 29.71 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 26.92 / 0.0532 | 24.80 / 0.0829 | 30.21 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.43 / 0.0673 | 24.31 / 0.1106 | 29.68 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 26.92 / 0.0522 | 24.80 / 0.0784 | 30.21 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.78 / 0.0666 | 24.46 / 0.1120 | 29.92 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.16 / 0.0526 | 25.00 / 0.0831 | 30.24 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 26.83 / 0.0652 | 24.87 / 0.1009 | 29.92 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.25 / 0.0514 | 25.28 / 0.0768 | 30.24 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 26.85 / 0.0631 | 25.00 / 0.0933 | 29.93 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.28 / 0.0504 | 25.43 / 0.0723 | 30.24 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 26.96 / 0.0605 | 25.15 / 0.0867 | 29.92 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.33 / 0.0498 | 25.60 / 0.0684 | 30.24 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.21 / 0.0836 | 18.64 / 0.0196 | 30.26 / 0.0246 | 26.26 / 0.0511 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 17.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.21 | 0.6690 | 0.0836 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 18.98 | 0.6332 | 0.2229 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 20.52 | 0.6513 | 0.1796 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 19.76 | 0.6588 | 0.2010 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 19.96 | 0.6567 | 0.1903 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 18.84 | 0.6372 | 0.2219 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 20.23 | 0.6425 | 0.1814 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 19.59 | 0.6565 | 0.2007 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 19.72 | 0.6511 | 0.1911 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 23.35 | 0.7130 | 0.1321 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 18.94 | 0.6167 | 0.2410 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 19.73 | 0.6389 | 0.1927 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 19.51 | 0.6422 | 0.2168 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 19.54 | 0.6409 | 0.2033 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.96 | 0.6131 | 0.2411 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.88 | 0.6324 | 0.1960 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 19.52 | 0.6375 | 0.2187 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.60 | 0.6362 | 0.2057 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 20.45 | 0.6667 | 0.1702 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.50 | 0.6018 | 0.2537 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 17.32 | 0.6329 | 0.2048 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 16.91 | 0.6285 | 0.2282 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 17.07 | 0.6328 | 0.2163 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 17.22 | 0.6072 | 0.2114 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 17.69 | 0.6379 | 0.1708 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 17.55 | 0.6311 | 0.1943 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 17.65 | 0.6358 | 0.1824 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 23.95 | 0.6996 | 0.1240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.42 | 0.7132 | 0.0994 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.47 | 0.7113 | 0.1136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.47 | 0.7130 | 0.1060 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.05 | 0.7038 | 0.1212 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.37 | 0.7105 | 0.0983 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.53 | 0.7122 | 0.1112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.52 | 0.7122 | 0.1047 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.81 | 0.7417 | 0.0883 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.07 | 0.7035 | 0.1196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.53 | 0.7203 | 0.0933 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.51 | 0.7161 | 0.1087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.54 | 0.7188 | 0.1004 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.06 | 0.7034 | 0.1187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.50 | 0.7161 | 0.0936 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.51 | 0.7141 | 0.1085 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.55 | 0.7161 | 0.1001 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.83 | 0.7428 | 0.0880 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.30 | 0.7112 | 0.0992 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.80 | 0.7253 | 0.0784 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.71 | 0.7209 | 0.0892 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.80 | 0.7241 | 0.0829 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.00 | 0.7120 | 0.0831 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.60 | 0.7343 | 0.0684 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.28 | 0.7244 | 0.0768 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.43 | 0.7315 | 0.0723 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.02 | 0.6601 | 0.1724 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.34 | 0.6749 | 0.1402 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.66 | 0.6806 | 0.1563 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.56 | 0.6798 | 0.1471 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.11 | 0.6657 | 0.1685 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.18 | 0.6696 | 0.1390 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.65 | 0.6801 | 0.1537 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.50 | 0.6767 | 0.1459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.05 | 0.7290 | 0.1163 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.38 | 0.6762 | 0.1675 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.87 | 0.6964 | 0.1306 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.01 | 0.6976 | 0.1491 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.96 | 0.6980 | 0.1377 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.31 | 0.6739 | 0.1657 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.76 | 0.6899 | 0.1331 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.95 | 0.6934 | 0.1499 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.92 | 0.6937 | 0.1395 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.13 | 0.7310 | 0.1162 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.66 | 0.6952 | 0.1434 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.31 | 0.7165 | 0.1106 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.27 | 0.7139 | 0.1257 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.36 | 0.7173 | 0.1169 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.46 | 0.7029 | 0.1120 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.15 | 0.7273 | 0.0867 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.87 | 0.7194 | 0.1009 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.00 | 0.7260 | 0.0933 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 10.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.64 | 0.5046 | 0.0196 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 13.55 | 0.4735 | 0.0564 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.77 | 0.5045 | 0.0516 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 13.76 | 0.5012 | 0.0540 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 13.76 | 0.5043 | 0.0527 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 13.57 | 0.4786 | 0.0569 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.74 | 0.5001 | 0.0519 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.76 | 0.5010 | 0.0544 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.76 | 0.5014 | 0.0532 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.49 | 0.5312 | 0.0362 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 15.49 | 0.4882 | 0.0467 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 15.92 | 0.5232 | 0.0409 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.82 | 0.5146 | 0.0442 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 15.89 | 0.5206 | 0.0425 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 15.56 | 0.4887 | 0.0463 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 15.93 | 0.5185 | 0.0411 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.87 | 0.5129 | 0.0438 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 15.92 | 0.5167 | 0.0425 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.73 | 0.5447 | 0.0327 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.10 | 0.4413 | 0.0719 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 11.50 | 0.4903 | 0.0645 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 11.34 | 0.4692 | 0.0688 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 11.45 | 0.4804 | 0.0670 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 11.76 | 0.4638 | 0.0644 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.02 | 0.5054 | 0.0598 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 11.79 | 0.4863 | 0.0628 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 11.88 | 0.4980 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.90 | 0.5432 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.35 | 0.5741 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.34 | 0.5670 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.39 | 0.5724 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.95 | 0.5480 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.29 | 0.5738 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.37 | 0.5683 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.40 | 0.5725 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.54 | 0.5952 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.71 | 0.5341 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.15 | 0.5713 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.06 | 0.5569 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.14 | 0.5655 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.70 | 0.5331 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.12 | 0.5664 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.07 | 0.5555 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.15 | 0.5626 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.34 | 0.5840 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.22 | 0.5652 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.58 | 0.5924 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.51 | 0.5827 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.58 | 0.5888 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.17 | 0.5789 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.41 | 0.6161 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.24 | 0.5964 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.29 | 0.6080 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.87 | 0.5395 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.32 | 0.5712 | 0.0222 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.32 | 0.5644 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.37 | 0.5697 | 0.0232 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.92 | 0.5447 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.26 | 0.5707 | 0.0223 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.35 | 0.5657 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.38 | 0.5696 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.52 | 0.5919 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.67 | 0.5295 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.13 | 0.5687 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.05 | 0.5542 | 0.0242 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.12 | 0.5624 | 0.0228 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.68 | 0.5295 | 0.0265 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.10 | 0.5637 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.05 | 0.5528 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.13 | 0.5599 | 0.0228 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.33 | 0.5807 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.21 | 0.5632 | 0.0223 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.58 | 0.5914 | 0.0184 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.51 | 0.5813 | 0.0206 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.58 | 0.5876 | 0.0195 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.16 | 0.5773 | 0.0194 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.40 | 0.6154 | 0.0175 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.23 | 0.5955 | 0.0185 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.29 | 0.6073 | 0.0178 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 47.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.26 | 0.7219 | 0.0302 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.97 | 0.5298 | 0.2175 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.29 | 0.5494 | 0.1997 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.08 | 0.5514 | 0.2092 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.15 | 0.5505 | 0.2051 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.97 | 0.5275 | 0.2181 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.28 | 0.5430 | 0.2003 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.08 | 0.5473 | 0.2095 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.14 | 0.5455 | 0.2052 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.17 | 0.4431 | 0.1786 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 10.56 | 0.5680 | 0.1892 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.98 | 0.5928 | 0.1648 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.71 | 0.5944 | 0.1773 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.81 | 0.5944 | 0.1709 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 10.54 | 0.5656 | 0.1881 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.93 | 0.5880 | 0.1658 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.68 | 0.5918 | 0.1769 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.77 | 0.5906 | 0.1715 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.65 | 0.4864 | 0.1658 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.57 | 0.5063 | 0.2332 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.88 | 0.5308 | 0.2134 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.66 | 0.5275 | 0.2250 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.73 | 0.5295 | 0.2201 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.65 | 0.4747 | 0.2039 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.97 | 0.4920 | 0.1869 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.72 | 0.4934 | 0.1973 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.80 | 0.4934 | 0.1926 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.13 | 0.7266 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.60 | 0.7359 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.54 | 0.7345 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.61 | 0.7358 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.15 | 0.7275 | 0.0414 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.56 | 0.7352 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.57 | 0.7344 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.63 | 0.7352 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.53 | 0.7384 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 23.94 | 0.7239 | 0.0421 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.45 | 0.7351 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.35 | 0.7323 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.44 | 0.7341 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.94 | 0.7234 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.41 | 0.7328 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.34 | 0.7316 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.43 | 0.7329 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.27 | 0.7322 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.47 | 0.7315 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.85 | 0.7405 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.77 | 0.7383 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.84 | 0.7397 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.25 | 0.7357 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.47 | 0.7458 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.35 | 0.7415 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.39 | 0.7444 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.01 | 0.7028 | 0.0553 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.58 | 0.7157 | 0.0474 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.59 | 0.7174 | 0.0510 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.60 | 0.7173 | 0.0492 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.00 | 0.7030 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.46 | 0.7129 | 0.0477 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.54 | 0.7156 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.53 | 0.7149 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.65 | 0.6949 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.66 | 0.6927 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.28 | 0.7090 | 0.0495 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.26 | 0.7100 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.29 | 0.7101 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.64 | 0.6910 | 0.0590 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.19 | 0.7055 | 0.0497 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.22 | 0.7084 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.24 | 0.7077 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.02 | 0.6712 | 0.0767 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.31 | 0.7123 | 0.0562 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.64 | 0.7209 | 0.0542 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.83 | 0.7247 | 0.0526 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.86 | 0.7245 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.39 | 0.7191 | 0.0481 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.31 | 0.7250 | 0.0476 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.45 | 0.7277 | 0.0469 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.34 | 0.7280 | 0.0467 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 54.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.34 | 0.7065 | 0.0356 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.29 | 0.4557 | 0.2732 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.42 | 0.4674 | 0.2603 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.34 | 0.4709 | 0.2677 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.37 | 0.4697 | 0.2647 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.28 | 0.4538 | 0.2743 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.41 | 0.4609 | 0.2618 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.33 | 0.4670 | 0.2692 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.36 | 0.4644 | 0.2661 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.96 | 0.4219 | 0.1804 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.75 | 0.4986 | 0.2514 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.92 | 0.5132 | 0.2344 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.82 | 0.5176 | 0.2439 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.86 | 0.5161 | 0.2397 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.73 | 0.5013 | 0.2496 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.89 | 0.5151 | 0.2319 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.79 | 0.5210 | 0.2411 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.83 | 0.5186 | 0.2370 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.74 | 0.4913 | 0.1588 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.06 | 0.4563 | 0.2821 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.15 | 0.4738 | 0.2645 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.10 | 0.4735 | 0.2742 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.11 | 0.4741 | 0.2700 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.58 | 0.4452 | 0.2323 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.59 | 0.4581 | 0.2219 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.60 | 0.4604 | 0.2286 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.59 | 0.4600 | 0.2254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.43 | 0.7117 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.90 | 0.7183 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.86 | 0.7175 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.93 | 0.7183 | 0.0402 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.44 | 0.7123 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.84 | 0.7175 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.86 | 0.7173 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.92 | 0.7178 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.72 | 0.7201 | 0.0394 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.26 | 0.7095 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.72 | 0.7176 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.68 | 0.7160 | 0.0423 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.74 | 0.7173 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.28 | 0.7096 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.72 | 0.7167 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.69 | 0.7160 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.77 | 0.7170 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.53 | 0.7170 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.83 | 0.7182 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.14 | 0.7246 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.10 | 0.7235 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.15 | 0.7243 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.47 | 0.7193 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.72 | 0.7278 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.59 | 0.7243 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.64 | 0.7267 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.58 | 0.6937 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.06 | 0.7012 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.16 | 0.7038 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.15 | 0.7031 | 0.0520 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.54 | 0.6940 | 0.0572 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.93 | 0.6989 | 0.0508 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.09 | 0.7024 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.06 | 0.7012 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.00 | 0.7084 | 0.0496 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.22 | 0.6848 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.73 | 0.6949 | 0.0536 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.80 | 0.6971 | 0.0592 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.80 | 0.6967 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.21 | 0.6850 | 0.0619 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.68 | 0.6940 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.78 | 0.6974 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.77 | 0.6963 | 0.0546 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.65 | 0.6995 | 0.0525 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.03 | 0.7085 | 0.0576 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.53 | 0.7173 | 0.0492 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.48 | 0.7180 | 0.0529 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.53 | 0.7182 | 0.0509 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.96 | 0.7127 | 0.0491 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.23 | 0.7217 | 0.0432 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.03 | 0.7197 | 0.0477 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.07 | 0.7212 | 0.0456 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 64.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.26 | 0.7382 | 0.0246 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.00 | 0.3901 | 0.2548 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.07 | 0.3916 | 0.2485 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.03 | 0.3977 | 0.2520 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.04 | 0.3952 | 0.2506 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.00 | 0.3889 | 0.2550 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.06 | 0.3882 | 0.2494 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.02 | 0.3955 | 0.2524 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.03 | 0.3922 | 0.2513 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.36 | 0.3042 | 0.1783 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.79 | 0.4244 | 0.2382 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.90 | 0.4258 | 0.2284 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.83 | 0.4337 | 0.2341 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.86 | 0.4303 | 0.2316 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.77 | 0.4255 | 0.2373 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.88 | 0.4261 | 0.2273 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.81 | 0.4353 | 0.2328 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.84 | 0.4309 | 0.2306 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.29 | 0.3657 | 0.1626 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.81 | 0.3675 | 0.2709 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.89 | 0.3765 | 0.2611 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.84 | 0.3772 | 0.2662 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.87 | 0.3773 | 0.2639 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.86 | 0.3297 | 0.2350 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.87 | 0.3330 | 0.2297 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.88 | 0.3392 | 0.2320 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.87 | 0.3365 | 0.2309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.17 | 0.7368 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.14 | 0.7367 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.18 | 0.7370 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.16 | 0.7369 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.17 | 0.7367 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.13 | 0.7366 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.17 | 0.7369 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.15 | 0.7367 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.23 | 0.7382 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 30.19 | 0.7370 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.19 | 0.7372 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.20 | 0.7372 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.19 | 0.7372 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.17 | 0.7369 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.17 | 0.7371 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.18 | 0.7371 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.17 | 0.7370 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 30.23 | 0.7383 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.21 | 0.7378 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.21 | 0.7380 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.21 | 0.7379 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.21 | 0.7380 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.24 | 0.7380 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.24 | 0.7380 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.24 | 0.7380 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.24 | 0.7380 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.20 | 0.7250 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.96 | 0.7242 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.28 | 0.7268 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.12 | 0.7256 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.17 | 0.7250 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.87 | 0.7234 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.22 | 0.7264 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.03 | 0.7249 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.75 | 0.7362 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.02 | 0.7241 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.94 | 0.7244 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.15 | 0.7265 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.04 | 0.7256 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.95 | 0.7241 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.83 | 0.7236 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.09 | 0.7263 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.96 | 0.7250 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.64 | 0.7360 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.69 | 0.7336 | 0.0295 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.68 | 0.7348 | 0.0286 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.73 | 0.7353 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.71 | 0.7352 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.92 | 0.7357 | 0.0278 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.92 | 0.7360 | 0.0272 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.92 | 0.7367 | 0.0276 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.93 | 0.7365 | 0.0274 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.26 | 0.7136 | 0.0511 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.40 | 0.4369 | 0.3354 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.50 | 0.4448 | 0.3162 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.44 | 0.4501 | 0.3274 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.46 | 0.4482 | 0.3222 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.40 | 0.4355 | 0.3364 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.49 | 0.4400 | 0.3172 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.43 | 0.4471 | 0.3286 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.45 | 0.4442 | 0.3235 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.25 | 0.3916 | 0.2461 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.32 | 0.4712 | 0.3137 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.45 | 0.4794 | 0.2878 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.37 | 0.4858 | 0.3024 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.40 | 0.4833 | 0.2952 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.31 | 0.4714 | 0.3101 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.43 | 0.4785 | 0.2848 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.35 | 0.4864 | 0.2981 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.38 | 0.4829 | 0.2913 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.36 | 0.4426 | 0.2209 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.01 | 0.4123 | 0.3517 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.10 | 0.4277 | 0.3289 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.05 | 0.4269 | 0.3414 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.07 | 0.4279 | 0.3358 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.97 | 0.3843 | 0.3066 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.00 | 0.3941 | 0.2914 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.99 | 0.3973 | 0.3010 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.99 | 0.3961 | 0.2967 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.44 | 0.7177 | 0.0634 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.72 | 0.7219 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.76 | 0.7217 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.77 | 0.7222 | 0.0591 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.46 | 0.7180 | 0.0632 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.67 | 0.7214 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.76 | 0.7215 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.77 | 0.7217 | 0.0591 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.82 | 0.7286 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.36 | 0.7171 | 0.0634 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.65 | 0.7222 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.64 | 0.7213 | 0.0608 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.67 | 0.7220 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.35 | 0.7168 | 0.0631 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.61 | 0.7210 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.63 | 0.7207 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.66 | 0.7211 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.66 | 0.7262 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.67 | 0.7210 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.92 | 0.7252 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.89 | 0.7243 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.92 | 0.7249 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.16 | 0.7218 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.33 | 0.7271 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.25 | 0.7250 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.28 | 0.7265 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.65 | 0.7027 | 0.0818 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.90 | 0.7072 | 0.0732 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.08 | 0.7100 | 0.0777 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.03 | 0.7092 | 0.0752 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.62 | 0.7028 | 0.0815 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.78 | 0.7056 | 0.0732 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.03 | 0.7091 | 0.0776 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.95 | 0.7078 | 0.0754 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.23 | 0.7217 | 0.0672 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.40 | 0.6983 | 0.0887 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.70 | 0.7045 | 0.0763 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.82 | 0.7067 | 0.0830 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.78 | 0.7060 | 0.0792 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.35 | 0.6976 | 0.0864 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.61 | 0.7027 | 0.0753 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.77 | 0.7059 | 0.0808 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.72 | 0.7046 | 0.0778 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.93 | 0.7159 | 0.0699 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.04 | 0.7145 | 0.0759 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.43 | 0.7207 | 0.0673 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.39 | 0.7209 | 0.0712 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.43 | 0.7212 | 0.0691 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.78 | 0.7180 | 0.0666 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.96 | 0.7237 | 0.0605 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.83 | 0.7227 | 0.0652 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.85 | 0.7235 | 0.0631 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 219959 | 0.327 | 60.4 | 29.16 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 219959 | 0.327 | 55.5 | 29.16 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 219959 | 0.327 | 62.9 | 29.16 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 219959 | 0.327 | 68.2 | 29.16 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 221594 | 0.342 | 68.7 | 28.99 | 0.10 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 221594 | 0.342 | 67.4 | 28.99 | 0.10 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 221594 | 0.342 | 69.5 | 28.99 | 0.10 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 221594 | 0.342 | 70.6 | 28.99 | 0.10 | 0.019 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1961529 | 0.808 | 535.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 218508 | 0.329 | 62.0 | 29.17 | 0.07 | 0.018 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 218508 | 0.329 | 65.2 | 29.17 | 0.07 | 0.018 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 218508 | 0.329 | 67.3 | 29.17 | 0.07 | 0.018 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 218508 | 0.329 | 50.0 | 29.17 | 0.07 | 0.018 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 0.57 | False | 451073 | 0.983 | 173.4 | 32.23 | 0.26 | 0.010 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 0.57 | False | 451073 | 0.983 | 155.1 | 32.23 | 0.26 | 0.010 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 0.57 | False | 451073 | 0.983 | 146.4 | 32.23 | 0.26 | 0.010 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 0.57 | False | 451073 | 0.983 | 188.8 | 32.23 | 0.26 | 0.010 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2221203 | 0.808 | 133.9 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 217188 | 0.914 | 80.9 | 29.53 | 0.10 | 0.012 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 217188 | 0.914 | 77.0 | 29.53 | 0.10 | 0.012 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 217188 | 0.914 | 83.1 | 29.53 | 0.10 | 0.012 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 217188 | 0.914 | 59.5 | 29.53 | 0.10 | 0.012 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 805 | None | classic | 0.36 | False | 497177 | 1.313 | 204.1 | 27.84 | 0.10 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 805 | None | classic | 0.36 | False | 497177 | 1.313 | 192.7 | 27.84 | 0.10 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 805 | None | classic | 0.36 | False | 497177 | 1.313 | 210.9 | 27.84 | 0.10 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 805 | None | classic | 0.36 | False | 497177 | 1.313 | 203.4 | 27.84 | 0.10 | 0.010 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.701 | 0.041 |
| in035 | mask_ent | 0.661 | 0.041 |
| in035 | mask_grad | 0.446 | 0.041 |
| in035 | r_col | 0.836 | 0.041 |
| in035 | r_warp | 0.875 | 0.041 |
