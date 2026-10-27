# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.1% | 25.34 / 0.0091 | 23.30 / 0.0171 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.0% | 24.59 / 0.0096 | 20.72 / 0.0260 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.4% | 22.00 / 0.0065 | 17.49 / 0.0170 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 7.7% | 25.43 / 0.0103 | 21.87 / 0.0177 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 7.7% | 25.43 / 0.0102 | 21.82 / 0.0213 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.5% | 22.20 / 0.0059 | 17.62 / 0.0132 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.36 / 0.0499 | — / — | 20.30 / 0.0110 | 30.03 / 0.0336 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.06 / 0.0547 | — / — | 20.52 / 0.0112 | 29.88 / 0.0353 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.57 / 0.0571 | — / — | 19.96 / 0.0141 | 29.78 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.60 / 0.0551 | — / — | 19.94 / 0.0139 | 29.79 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.57 / 0.0541 | — / — | 20.00 / 0.0125 | 29.80 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.63 / 0.0558 | — / — | 20.11 / 0.0127 | 29.81 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.65 / 0.0532 | — / — | 20.04 / 0.0126 | 29.81 / 0.0344 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.4%） | — | — | 28.36 / 0.0499 | — / — | 30.03 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.77 / 0.0529 | — | — | — |
| in035 | 2 | 0-3 | 28.32 / 0.0476 | — | — | — |
| in035 | 4 | 3-5 | 28.99 / 0.0491 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.36 / 0.0499 | — | 30.03 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.06 / 0.0547 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 28.40 / 0.0501 | — | 30.03 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.57 / 0.0571 | — | 29.78 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.2% | 28.07 / 0.0527 | — | 30.02 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.60 / 0.0551 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.9% | 28.07 / 0.0524 | — | 30.02 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.57 / 0.0541 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.2% | 28.08 / 0.0511 | — | 30.02 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.63 / 0.0558 | — | 29.81 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.2% | 28.12 / 0.0515 | — | 30.02 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.65 / 0.0532 | — | 29.81 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.9% | 28.10 / 0.0513 | — | 30.02 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.36 / 0.0499 | — / — | 30.03 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.06 / 0.0547 | — / — | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.40 / 0.0501 | — / — | 30.03 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.30 / 0.0110 | 30.03 / 0.0336 | 28.36 / 0.0499 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.30 | 0.6607 | 0.0110 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.32 | 0.3449 | 0.0833 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.53 | 0.2901 | 0.0607 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.53 | 0.2901 | 0.0607 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.67 | 0.3287 | 0.0587 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.74 | 0.3190 | 0.0586 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.74 | 0.3190 | 0.0586 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.52 | 0.6795 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.98 | 0.6658 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.96 | 0.6643 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.02 | 0.6840 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.12 | 0.6773 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.06 | 0.6713 | 0.0125 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.52 | 0.6786 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.96 | 0.6634 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.94 | 0.6618 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.00 | 0.6821 | 0.0125 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.11 | 0.6753 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.04 | 0.6693 | 0.0126 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 31.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.27 | 0.7764 | 0.0200 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.32 | 0.4246 | 0.2224 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.03 | 0.3473 | 0.1841 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.03 | 0.3473 | 0.1841 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.22 | 0.3776 | 0.1707 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.21 | 0.3667 | 0.1752 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.21 | 0.3667 | 0.1752 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.36 | 0.7790 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.73 | 0.7726 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.73 | 0.7724 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.78 | 0.7773 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.85 | 0.7750 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.82 | 0.7739 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.47 | 0.7642 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.92 | 0.7554 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.05 | 0.7607 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.04 | 0.7674 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.00 | 0.7603 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.04 | 0.7620 | 0.0248 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.03 | 0.7368 | 0.0336 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.91 | 0.2982 | 0.3472 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.99 | 0.1998 | 0.2769 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.99 | 0.1998 | 0.2769 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.36 | 0.2286 | 0.2641 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.36 | 0.2308 | 0.2689 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.36 | 0.2308 | 0.2689 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.03 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7361 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.78 | 0.7354 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.79 | 0.7351 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.80 | 0.7357 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.81 | 0.7360 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.81 | 0.7353 | 0.0344 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.36 | 0.7393 | 0.0499 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.18 | 0.3176 | 0.4075 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.24 | 0.2300 | 0.3638 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.24 | 0.2300 | 0.3638 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.58 | 0.2597 | 0.3429 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.59 | 0.2594 | 0.3506 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.59 | 0.2594 | 0.3506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.40 | 0.7400 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.07 | 0.7376 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.07 | 0.7375 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.08 | 0.7387 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.12 | 0.7381 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.10 | 0.7378 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.06 | 0.7368 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.57 | 0.7336 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.60 | 0.7337 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.57 | 0.7356 | 0.0541 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.63 | 0.7348 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.65 | 0.7343 | 0.0532 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 893 | None | classic | 0.30 | False | 418608 | 0.503 | 102.7 | 29.15 | 0.59 | 0.011 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207263 | 0.813 | 87.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207263 | 0.813 | 87.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 960054 | 0.813 | 10.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 960054 | 0.813 | 8.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 960054 | 0.813 | 8.6 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.635 | 0.017 |
| in035 | mask_ent | 0.665 | 0.017 |
| in035 | mask_grad | 0.447 | 0.017 |
| in035 | r_col | 0.801 | 0.017 |
| in035 | r_warp | 0.851 | 0.017 |
