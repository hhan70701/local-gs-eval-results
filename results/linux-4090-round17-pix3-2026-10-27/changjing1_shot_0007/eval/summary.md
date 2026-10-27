# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.9% | 24.88 / 0.0066 | 22.21 / 0.0097 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 4.7% | 24.28 / 0.0063 | 19.87 / 0.0180 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.2% | 23.68 / 0.0059 | 16.43 / 0.0182 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 6.1% | 25.13 / 0.0071 | 21.61 / 0.0151 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 6.1% | 25.06 / 0.0070 | 20.57 / 0.0165 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.5% | 23.59 / 0.0049 | 17.10 / 0.0131 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.35 / 0.0496 | — / — | 20.68 / 0.0107 | 29.69 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.22 / 0.0511 | — / — | 21.10 / 0.0102 | 29.61 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.62 / 0.0563 | — / — | 19.66 / 0.0137 | 29.65 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.67 / 0.0541 | — / — | 19.65 / 0.0130 | 29.65 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.61 / 0.0552 | — / — | 19.50 / 0.0133 | 29.67 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.61 / 0.0562 | — / — | 19.58 / 0.0138 | 29.67 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.63 / 0.0539 | — / — | 19.53 / 0.0132 | 29.66 / 0.0368 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.3%） | — | — | 28.35 / 0.0496 | — / — | 29.69 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.79 / 0.0481 | — | — | — |
| in035 | 2 | 0-3 | 28.33 / 0.0483 | — | — | — |
| in035 | 4 | 3-5 | 28.93 / 0.0523 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.35 / 0.0496 | — | 29.69 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.22 / 0.0511 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.2% | 28.43 / 0.0491 | — | 29.67 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.62 / 0.0563 | — | 29.65 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.1% | 27.86 / 0.0527 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.67 / 0.0541 | — | 29.65 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.7% | 27.88 / 0.0518 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.61 / 0.0552 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.1% | 27.79 / 0.0524 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.61 / 0.0562 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.1% | 27.82 / 0.0527 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.63 / 0.0539 | — | 29.66 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.7% | 27.82 / 0.0521 | — | 29.69 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.35 / 0.0496 | — / — | 29.69 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.22 / 0.0511 | — / — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.43 / 0.0491 | — / — | 29.67 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.68 / 0.0107 | 29.69 / 0.0366 | 28.35 / 0.0496 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.68 | 0.6783 | 0.0107 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.85 | 0.2571 | 0.0982 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.78 | 0.1842 | 0.0724 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.78 | 0.1842 | 0.0724 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.82 | 0.1989 | 0.0711 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.85 | 0.1878 | 0.0713 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.85 | 0.1878 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.12 | 0.7144 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.66 | 0.6617 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.66 | 0.6625 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.50 | 0.6641 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.58 | 0.6581 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.53 | 0.6558 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.10 | 0.7133 | 0.0102 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.66 | 0.6619 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.65 | 0.6628 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.50 | 0.6646 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.58 | 0.6584 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.53 | 0.6558 | 0.0132 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 26.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.61 | 0.7804 | 0.0174 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.74 | 0.3938 | 0.1865 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.57 | 0.2995 | 0.1642 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.57 | 0.2995 | 0.1642 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.77 | 0.3248 | 0.1564 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.72 | 0.3145 | 0.1590 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.72 | 0.3145 | 0.1590 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.76 | 0.7879 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.63 | 0.7708 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.66 | 0.7724 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.58 | 0.7726 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.57 | 0.7701 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.55 | 0.7706 | 0.0201 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.49 | 0.7779 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.40 | 0.7529 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.56 | 0.7596 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.78 | 0.7615 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.38 | 0.7553 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.46 | 0.7589 | 0.0241 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 80.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.69 | 0.7096 | 0.0366 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.71 | 0.2225 | 0.3601 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.43 | 0.1243 | 0.2955 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.43 | 0.1243 | 0.2955 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.54 | 0.1339 | 0.2907 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.55 | 0.1359 | 0.2930 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.55 | 0.1359 | 0.2930 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.67 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7095 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.65 | 0.7098 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.65 | 0.7094 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.67 | 0.7097 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.67 | 0.7103 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.66 | 0.7095 | 0.0368 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.35 | 0.7204 | 0.0496 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.02 | 0.2499 | 0.4210 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.47 | 0.1611 | 0.3864 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.47 | 0.1611 | 0.3864 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.58 | 0.1725 | 0.3754 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.59 | 0.1729 | 0.3791 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.59 | 0.1729 | 0.3791 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.43 | 0.7221 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.86 | 0.7181 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.88 | 0.7184 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.79 | 0.7185 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.82 | 0.7178 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.82 | 0.7179 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.22 | 0.7206 | 0.0511 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.62 | 0.7159 | 0.0563 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.67 | 0.7165 | 0.0541 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.61 | 0.7170 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.61 | 0.7163 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.63 | 0.7163 | 0.0539 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 648 | None | classic | 0.30 | False | 401359 | 0.520 | 97.4 | 28.72 | 0.36 | 0.015 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 825350 | 0.797 | 83.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 825350 | 0.797 | 83.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 669857 | 0.797 | 10.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 669857 | 0.797 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 669857 | 0.797 | 8.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.689 | 0.017 |
| in035 | mask_ent | 0.784 | 0.017 |
| in035 | mask_grad | 0.442 | 0.017 |
| in035 | r_col | 0.752 | 0.017 |
| in035 | r_warp | 0.887 | 0.017 |
