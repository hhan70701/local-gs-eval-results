# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.5% | 25.18 / 0.0044 | 20.76 / 0.0080 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 2.8% | 24.75 / 0.0045 | 19.66 / 0.0119 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.3% | 23.74 / 0.0030 | 16.94 / 0.0083 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 3.2% | 25.22 / 0.0048 | 19.68 / 0.0120 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 3.2% | 25.19 / 0.0049 | 19.19 / 0.0125 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 1.4% | 24.18 / 0.0027 | 16.06 / 0.0084 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.74 / 0.0512 | — / — | 21.68 / 0.0095 | 29.73 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.60 / 0.0524 | — / — | 21.82 / 0.0089 | 29.71 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.03 / 0.0540 | — / — | 20.38 / 0.0110 | 29.72 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.05 / 0.0531 | — / — | 20.32 / 0.0107 | 29.73 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.03 / 0.0545 | — / — | 20.38 / 0.0115 | 29.68 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.06 / 0.0545 | — / — | 20.53 / 0.0111 | 29.64 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.07 / 0.0533 | — / — | 20.49 / 0.0107 | 29.64 / 0.0376 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.5%） | — | — | 28.74 / 0.0512 | — / — | 29.73 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 28.09 / 0.0523 | — | — | — |
| in035 | 2 | 0-3 | 28.83 / 0.0487 | — | — | — |
| in035 | 4 | 3-5 | 29.29 / 0.0525 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.74 / 0.0512 | — | 29.73 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.60 / 0.0524 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.75 / 0.0509 | — | 29.73 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.03 / 0.0540 | — | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.5% | 28.19 / 0.0525 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.05 / 0.0531 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.3% | 28.19 / 0.0521 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 28.03 / 0.0545 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 0.5% | 28.21 / 0.0528 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 28.06 / 0.0545 | — | 29.64 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 0.5% | 28.28 / 0.0526 | — | 29.70 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 28.07 / 0.0533 | — | 29.64 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.3% | 28.27 / 0.0521 | — | 29.70 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.74 / 0.0512 | — / — | 29.73 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.60 / 0.0524 | — / — | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.75 / 0.0509 | — / — | 29.73 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 21.68 / 0.0095 | 29.73 / 0.0371 | 28.74 / 0.0512 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.68 | 0.7527 | 0.0095 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.35 | 0.2370 | 0.1157 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.22 | 0.1581 | 0.0715 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.22 | 0.1581 | 0.0715 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.23 | 0.1597 | 0.0711 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.28 | 0.1567 | 0.0709 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.28 | 0.1567 | 0.0709 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.81 | 0.7654 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.38 | 0.7332 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.33 | 0.7295 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.41 | 0.7353 | 0.0115 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.57 | 0.7347 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.53 | 0.7313 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.82 | 0.7651 | 0.0089 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.38 | 0.7331 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.32 | 0.7293 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.38 | 0.7348 | 0.0115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.53 | 0.7340 | 0.0111 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.49 | 0.7305 | 0.0107 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 26.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.86 | 0.7939 | 0.0165 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.78 | 0.4210 | 0.2369 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.98 | 0.2401 | 0.1814 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.98 | 0.2401 | 0.1814 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.10 | 0.2577 | 0.1774 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.09 | 0.2522 | 0.1786 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.09 | 0.2522 | 0.1786 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7966 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.67 | 0.7878 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.62 | 0.7871 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.79 | 0.7895 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.93 | 0.7894 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.89 | 0.7887 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.47 | 0.7872 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.02 | 0.7751 | 0.0215 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.04 | 0.7768 | 0.0198 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.05 | 0.7784 | 0.0209 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.00 | 0.7757 | 0.0210 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.01 | 0.7763 | 0.0200 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 81.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.73 | 0.7129 | 0.0371 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.32 | 0.2841 | 0.4160 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.00 | 0.1043 | 0.3128 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.00 | 0.1043 | 0.3128 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.12 | 0.1134 | 0.3087 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.12 | 0.1151 | 0.3110 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.12 | 0.1151 | 0.3110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.71 | 0.7128 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.70 | 0.7128 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.70 | 0.7127 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7129 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.72 | 0.7129 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.73 | 0.7129 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.68 | 0.7126 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.64 | 0.7127 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.64 | 0.7125 | 0.0376 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.74 | 0.7243 | 0.0512 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.64 | 0.2971 | 0.4805 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.02 | 0.1309 | 0.4090 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.02 | 0.1309 | 0.4090 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.14 | 0.1409 | 0.4020 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.14 | 0.1417 | 0.4050 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.14 | 0.1417 | 0.4050 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.75 | 0.7247 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.19 | 0.7226 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.19 | 0.7225 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.21 | 0.7227 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.28 | 0.7227 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.27 | 0.7226 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.60 | 0.7235 | 0.0524 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.03 | 0.7210 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.05 | 0.7212 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.03 | 0.7211 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.06 | 0.7210 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.07 | 0.7209 | 0.0533 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 667 | None | classic | 0.50 | False | 449316 | 0.994 | 196.7 | 26.35 | 0.12 | 0.010 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 664873 | 0.812 | 181.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 664873 | 0.812 | 181.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 548083 | 0.812 | 10.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 548083 | 0.812 | 8.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 548083 | 0.812 | 8.3 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.581 | 0.011 |
| in035 | mask_ent | 0.755 | 0.011 |
| in035 | mask_grad | 0.431 | 0.011 |
| in035 | r_col | 0.687 | 0.011 |
| in035 | r_warp | 0.857 | 0.011 |
