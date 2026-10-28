# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.9% | 24.88 / 0.0066 | 22.21 / 0.0097 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 6.1% | 25.13 / 0.0071 | 21.61 / 0.0151 | — | — |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | 9.3% | 27.70 / 0.0115 | 26.06 / 0.0266 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 9.3% | 27.70 / 0.0116 | 26.40 / 0.0280 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 2.3% | 24.18 / 0.0078 | 22.03 / 0.0212 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 9.2% | 27.70 / 0.0115 | 26.31 / 0.0248 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 9.2% | 27.72 / 0.0116 | 26.38 / 0.0256 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.35 / 0.0496 | — / — | 20.68 / 0.0107 | 29.69 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.22 / 0.0511 | — / — | 21.10 / 0.0102 | 29.61 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.61 / 0.0552 | — / — | 19.50 / 0.0133 | 29.67 / 0.0370 |
| in035 | hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.09 / 0.0554 | — / — | 21.02 / 0.0121 | 29.37 / 0.0385 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.12 / 0.0557 | — / — | 21.06 / 0.0121 | 29.40 / 0.0387 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.10 / 0.0537 | — / — | 20.95 / 0.0120 | 29.40 / 0.0384 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.08 / 0.0553 | — / — | 20.98 / 0.0125 | 29.40 / 0.0388 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.10 / 0.0555 | — / — | 21.02 / 0.0124 | 29.41 / 0.0387 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.3%） | — | — | 28.35 / 0.0496 | — / — | 29.69 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 | f4rq |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.79 / 0.0481 | — | — | — | — |
| in035 | 2 | 0-3 | 28.33 / 0.0483 | — | — | — | — |
| in035 | 4 | 3-5 | 28.93 / 0.0523 | — | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.35 / 0.0496 | — | 29.69 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.22 / 0.0511 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.2% | 28.43 / 0.0491 | — | 29.67 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.61 / 0.0552 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.1% | 27.79 / 0.0524 | — | 29.69 | 0/3 |
| in035 | f4rq_pix3_fsl | 不复核 | —% | 28.09 / 0.0554 | — | 29.37 | 0/3 |
| in035 | f4rq_pix3_fsl | oracle | 0.8% | 28.41 / 0.0506 | — | 29.66 | 0/3 |
| in035 | f4rq_pix3bg_fsl | 不复核 | —% | 28.12 / 0.0557 | — | 29.40 | 0/3 |
| in035 | f4rq_pix3bg_fsl | oracle | 0.8% | 28.43 / 0.0509 | — | 29.68 | 0/3 |
| in035 | f4rq_pix3bg_fsl_g | 不复核 | —% | 28.10 / 0.0537 | — | 29.40 | 0/3 |
| in035 | f4rq_pix3bg_fsl_g | oracle | 0.5% | 28.40 / 0.0508 | — | 29.67 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s25 | 不复核 | —% | 28.08 / 0.0553 | — | 29.40 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s25 | oracle | 0.8% | 28.41 / 0.0510 | — | 29.68 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | 不复核 | —% | 28.10 / 0.0555 | — | 29.41 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | oracle | 0.8% | 28.42 / 0.0509 | — | 29.68 | 0/3 |

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
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.82 | 0.1989 | 0.0711 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 11.29 | 0.2485 | 0.0658 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 11.33 | 0.2524 | 0.0658 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 11.33 | 0.2524 | 0.0658 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 11.32 | 0.2458 | 0.0665 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 11.32 | 0.2483 | 0.0663 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.12 | 0.7144 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.50 | 0.6641 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 21.05 | 0.6987 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.09 | 0.6988 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 20.98 | 0.6922 | 0.0118 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 21.02 | 0.6953 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.05 | 0.6961 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.10 | 0.7133 | 0.0102 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.50 | 0.6646 | 0.0133 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 21.02 | 0.6964 | 0.0121 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.06 | 0.6968 | 0.0121 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 20.95 | 0.6906 | 0.0120 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 20.98 | 0.6924 | 0.0125 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.02 | 0.6936 | 0.0124 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 26.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.61 | 0.7804 | 0.0174 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.74 | 0.3938 | 0.1865 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.77 | 0.3248 | 0.1564 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 13.86 | 0.4028 | 0.1370 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 13.86 | 0.4035 | 0.1370 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 13.86 | 0.4035 | 0.1370 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 13.82 | 0.4055 | 0.1361 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 13.83 | 0.4045 | 0.1365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.76 | 0.7879 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.58 | 0.7726 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 26.91 | 0.7827 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 26.92 | 0.7827 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.83 | 0.7811 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 26.85 | 0.7817 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 26.88 | 0.7821 | 0.0186 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.49 | 0.7779 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.78 | 0.7615 | 0.0245 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 26.38 | 0.7691 | 0.0247 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 26.44 | 0.7700 | 0.0245 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.42 | 0.7713 | 0.0223 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 26.27 | 0.7700 | 0.0237 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 26.36 | 0.7703 | 0.0238 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 80.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.69 | 0.7096 | 0.0366 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.71 | 0.2225 | 0.3601 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.54 | 0.1339 | 0.2907 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 13.24 | 0.1899 | 0.2663 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 13.24 | 0.1903 | 0.2662 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 13.24 | 0.1903 | 0.2662 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 13.23 | 0.1925 | 0.2656 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 13.24 | 0.1915 | 0.2655 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.67 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.66 | 0.7095 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.68 | 0.7096 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.67 | 0.7095 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.68 | 0.7096 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.68 | 0.7096 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7095 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.67 | 0.7097 | 0.0370 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.37 | 0.7080 | 0.0385 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.40 | 0.7081 | 0.0387 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.40 | 0.7078 | 0.0384 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.40 | 0.7082 | 0.0388 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.41 | 0.7082 | 0.0387 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.35 | 0.7204 | 0.0496 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.02 | 0.2499 | 0.4210 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.58 | 0.1725 | 0.3754 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 13.30 | 0.2293 | 0.3469 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 13.31 | 0.2298 | 0.3470 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 13.31 | 0.2298 | 0.3470 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 13.30 | 0.2312 | 0.3471 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 13.30 | 0.2306 | 0.3468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.43 | 0.7221 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.79 | 0.7185 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.41 | 0.7210 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.43 | 0.7210 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.40 | 0.7206 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.41 | 0.7208 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.42 | 0.7208 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.22 | 0.7206 | 0.0511 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.61 | 0.7170 | 0.0552 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.09 | 0.7178 | 0.0554 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.12 | 0.7179 | 0.0557 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.10 | 0.7177 | 0.0537 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.08 | 0.7179 | 0.0553 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.10 | 0.7179 | 0.0555 | 1.00 |

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
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 669857 | 0.797 | 10.1 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1133362 | 0.797 | 1.4 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1133446 | 0.797 | 1.4 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1133446 | 0.797 | 1.4 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1133446 | 0.797 | 1.4 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1133446 | 0.797 | 1.4 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.689 | 0.017 |
| in035 | mask_ent | 0.784 | 0.017 |
| in035 | mask_grad | 0.442 | 0.017 |
| in035 | r_col | 0.752 | 0.017 |
| in035 | r_warp | 0.887 | 0.017 |
