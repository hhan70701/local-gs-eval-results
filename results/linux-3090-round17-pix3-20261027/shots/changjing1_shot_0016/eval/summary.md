# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.4% | 24.33 / 0.0171 | 21.81 / 0.0265 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.0% | 23.67 / 0.0175 | 21.36 / 0.0371 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 4.3% | 20.80 / 0.0126 | 18.18 / 0.0271 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.1% | 24.29 / 0.0179 | 23.46 / 0.0228 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.1% | 24.30 / 0.0180 | 22.75 / 0.0300 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 3.8% | 20.39 / 0.0127 | 18.58 / 0.0206 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.87 / 0.0511 | — / — | 19.96 / 0.0141 | 29.48 / 0.0329 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.37 / 0.0571 | — / — | 19.78 / 0.0133 | 29.34 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.29 / 0.0602 | — / — | 20.01 / 0.0171 | 29.48 / 0.0333 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.35 / 0.0577 | — / — | 20.01 / 0.0167 | 29.48 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.71 / 0.0527 | — / — | 20.37 / 0.0143 | 29.48 / 0.0332 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.54 / 0.0573 | — / — | 20.22 / 0.0158 | 29.47 / 0.0337 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.59 / 0.0547 | — / — | 20.20 / 0.0157 | 29.48 / 0.0330 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.5%） | — | — | 27.87 / 0.0511 | — / — | 29.48 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.89 / 0.0532 | — | — | — |
| in035 | 2 | 0-3 | 27.96 / 0.0509 | — | — | — |
| in035 | 4 | 3-5 | 28.77 / 0.0491 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.87 / 0.0511 | — | 29.48 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.37 / 0.0571 | — | 29.34 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.79 / 0.0506 | — | 29.48 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.29 / 0.0602 | — | 29.48 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.3% | 27.77 / 0.0543 | — | 29.49 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.35 / 0.0577 | — | 29.48 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.7% | 27.78 / 0.0540 | — | 29.49 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.71 / 0.0527 | — | 29.48 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.4% | 27.93 / 0.0510 | — | 29.49 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.54 / 0.0573 | — | 29.47 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.4% | 27.87 / 0.0528 | — | 29.49 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.59 / 0.0547 | — | 29.48 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.7% | 27.86 / 0.0527 | — | 29.49 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.87 / 0.0511 | — / — | 29.48 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.37 / 0.0571 | — / — | 29.34 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.79 / 0.0506 | — / — | 29.48 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.96 / 0.0141 | 29.48 / 0.0329 | 27.87 / 0.0511 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.96 | 0.6330 | 0.0141 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.55 | 0.3809 | 0.0735 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.57 | 0.3787 | 0.0547 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.57 | 0.3787 | 0.0547 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.73 | 0.4184 | 0.0507 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.69 | 0.3906 | 0.0523 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.69 | 0.3906 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.80 | 0.6524 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.01 | 0.6682 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.02 | 0.6644 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.37 | 0.6905 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.24 | 0.6724 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.22 | 0.6648 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.78 | 0.6515 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.01 | 0.6668 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.01 | 0.6633 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.37 | 0.6906 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.22 | 0.6710 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.20 | 0.6636 | 0.0157 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 32.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.08 | 0.7572 | 0.0227 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.60 | 0.4519 | 0.1787 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.74 | 0.3871 | 0.1602 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.74 | 0.3871 | 0.1602 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.95 | 0.4322 | 0.1399 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.88 | 0.4107 | 0.1484 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.88 | 0.4107 | 0.1484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.76 | 0.7566 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.87 | 0.7593 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.86 | 0.7584 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.30 | 0.7673 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.14 | 0.7622 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.11 | 0.7602 | 0.0246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.26 | 0.7383 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.31 | 0.7366 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.49 | 0.7419 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.44 | 0.7588 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.94 | 0.7465 | 0.0309 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.05 | 0.7494 | 0.0281 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 77.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.48 | 0.7042 | 0.0329 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.57 | 0.2401 | 0.3180 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.41 | 0.1414 | 0.2526 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.41 | 0.1414 | 0.2526 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.44 | 0.1445 | 0.2481 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.44 | 0.1465 | 0.2516 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.44 | 0.1465 | 0.2516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.48 | 0.7042 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.49 | 0.7043 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.49 | 0.7042 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.49 | 0.7043 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.49 | 0.7043 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.49 | 0.7042 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.34 | 0.7029 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.48 | 0.7051 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.48 | 0.7043 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.48 | 0.7047 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.47 | 0.7052 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.48 | 0.7042 | 0.0330 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.87 | 0.7099 | 0.0511 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.12 | 0.2823 | 0.3777 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.74 | 0.2030 | 0.3374 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.74 | 0.2030 | 0.3374 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.79 | 0.2129 | 0.3225 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.79 | 0.2108 | 0.3317 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.79 | 0.2108 | 0.3317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.79 | 0.7103 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.77 | 0.7114 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.78 | 0.7111 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.93 | 0.7133 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.87 | 0.7119 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.86 | 0.7112 | 0.0527 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.37 | 0.7057 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.29 | 0.7080 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.35 | 0.7076 | 0.0577 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.71 | 0.7118 | 0.0527 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.54 | 0.7094 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.59 | 0.7088 | 0.0547 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 817 | None | classic | 0.30 | False | 457831 | 0.990 | 197.1 | 30.01 | 0.34 | 0.018 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1179582 | 0.806 | 189.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1179582 | 0.806 | 189.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 843652 | 0.806 | 8.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 843652 | 0.806 | 8.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 843652 | 0.806 | 8.5 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.750 | 0.018 |
| in035 | mask_ent | 0.690 | 0.018 |
| in035 | mask_grad | 0.491 | 0.018 |
| in035 | r_col | 0.851 | 0.018 |
| in035 | r_warp | 0.882 | 0.018 |
