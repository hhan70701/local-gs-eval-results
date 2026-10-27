# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.9% | 24.94 / 0.0110 | 22.04 / 0.0221 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 9.7% | 24.23 / 0.0111 | 22.02 / 0.0237 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.5% | 20.75 / 0.0063 | 17.57 / 0.0136 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.2% | 24.80 / 0.0117 | 23.32 / 0.0160 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.1% | 24.75 / 0.0119 | 23.01 / 0.0205 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.8% | 21.30 / 0.0063 | 18.64 / 0.0112 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.85 / 0.0518 | — / — | 19.90 / 0.0125 | 29.89 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.99 / 0.0606 | — / — | 20.22 / 0.0146 | 29.10 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.25 / 0.0578 | — / — | 19.63 / 0.0157 | 29.69 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.30 / 0.0558 | — / — | 19.59 / 0.0154 | 29.70 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.37 / 0.0553 | — / — | 19.88 / 0.0149 | 29.84 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.29 / 0.0574 | — / — | 19.91 / 0.0151 | 29.73 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.35 / 0.0551 | — / — | 19.80 / 0.0149 | 29.81 / 0.0360 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.4%） | — | — | 27.85 / 0.0518 | — / — | 29.89 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.43 / 0.0485 | — | — | — |
| in035 | 2 | 0-3 | 27.51 / 0.0505 | — | — | — |
| in035 | 4 | 3-5 | 28.62 / 0.0565 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.85 / 0.0518 | — | 29.89 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.99 / 0.0606 | — | 29.10 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.75 / 0.0542 | — | 29.81 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.25 / 0.0578 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.9% | 27.57 / 0.0547 | — | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.30 / 0.0558 | — | 29.70 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.1% | 27.56 / 0.0543 | — | 29.86 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.37 / 0.0553 | — | 29.84 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.0% | 27.64 / 0.0535 | — | 29.86 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.29 / 0.0574 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.0% | 27.67 / 0.0540 | — | 29.86 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.35 / 0.0551 | — | 29.81 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.1% | 27.62 / 0.0536 | — | 29.86 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.85 / 0.0518 | — / — | 29.89 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 26.99 / 0.0606 | — / — | 29.10 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.75 / 0.0542 | — / — | 29.81 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.90 / 0.0125 | 29.89 / 0.0356 | 27.85 / 0.0518 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.90 | 0.6748 | 0.0125 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.42 | 0.3321 | 0.0917 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.86 | 0.3432 | 0.0598 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.86 | 0.3432 | 0.0598 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.21 | 0.3910 | 0.0571 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.20 | 0.3697 | 0.0572 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.20 | 0.3697 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.25 | 0.6928 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.64 | 0.6818 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.60 | 0.6764 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.89 | 0.6993 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.93 | 0.6881 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.82 | 0.6792 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.22 | 0.6904 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.63 | 0.6795 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.59 | 0.6746 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.88 | 0.6978 | 0.0149 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.91 | 0.6856 | 0.0151 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.80 | 0.6772 | 0.0149 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 28.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.64 | 0.7776 | 0.0201 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.53 | 0.4881 | 0.2014 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.72 | 0.4066 | 0.1526 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.72 | 0.4066 | 0.1526 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.82 | 0.4328 | 0.1432 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.82 | 0.4201 | 0.1472 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.82 | 0.4201 | 0.1472 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.79 | 0.7774 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.21 | 0.7761 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.18 | 0.7743 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.49 | 0.7828 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.51 | 0.7796 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.42 | 0.7763 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.53 | 0.7514 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.53 | 0.7586 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.69 | 0.7637 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.89 | 0.7723 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.78 | 0.7643 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.88 | 0.7655 | 0.0236 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.89 | 0.7333 | 0.0356 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.96 | 0.3353 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.65 | 0.1978 | 0.2763 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.65 | 0.1978 | 0.2763 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.82 | 0.2086 | 0.2679 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.81 | 0.2090 | 0.2726 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.81 | 0.2090 | 0.2726 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.81 | 0.7325 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.86 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.86 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.86 | 0.7332 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.86 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.86 | 0.7330 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.10 | 0.7274 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.69 | 0.7328 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.70 | 0.7323 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.84 | 0.7331 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.73 | 0.7330 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.81 | 0.7327 | 0.0360 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.85 | 0.7391 | 0.0518 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.47 | 0.3519 | 0.4198 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.76 | 0.2357 | 0.3596 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.76 | 0.2357 | 0.3596 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.92 | 0.2495 | 0.3446 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.91 | 0.2472 | 0.3519 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.91 | 0.2472 | 0.3519 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.75 | 0.7375 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.57 | 0.7379 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.56 | 0.7374 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.64 | 0.7392 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.67 | 0.7385 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.62 | 0.7376 | 0.0536 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.99 | 0.7280 | 0.0606 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.25 | 0.7349 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.30 | 0.7348 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.37 | 0.7367 | 0.0553 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.29 | 0.7351 | 0.0574 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.35 | 0.7349 | 0.0551 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 859 | None | classic | 1.10 | False | 470251 | 1.011 | 203.6 | 28.38 | 0.32 | 0.034 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1422992 | 0.801 | 196.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1422992 | 0.801 | 196.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1068092 | 0.801 | 8.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1068092 | 0.801 | 8.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1068092 | 0.801 | 8.4 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.651 | 0.021 |
| in035 | mask_ent | 0.710 | 0.021 |
| in035 | mask_grad | 0.479 | 0.021 |
| in035 | r_col | 0.798 | 0.021 |
| in035 | r_warp | 0.827 | 0.021 |
