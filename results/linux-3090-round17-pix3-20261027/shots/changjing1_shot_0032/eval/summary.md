# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 33.0% | 22.09 / 0.0368 | 22.98 / 0.0537 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 29.8% | 21.81 / 0.0367 | 22.95 / 0.0628 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.4% | 18.54 / 0.0244 | 19.98 / 0.0425 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 34.0% | 22.32 / 0.0385 | 25.62 / 0.0346 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 34.0% | 22.31 / 0.0384 | 24.47 / 0.0505 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 9.3% | 18.22 / 0.0245 | 21.44 / 0.0269 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 25.19 / 0.0637 | — / — | 18.16 / 0.0327 | 29.29 / 0.0247 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.74 / 0.0813 | — / — | 19.98 / 0.0339 | 28.85 / 0.0287 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.85 / 0.0840 | — / — | 20.55 / 0.0389 | 29.12 / 0.0260 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.91 / 0.0777 | — / — | 20.44 / 0.0387 | 29.23 / 0.0251 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.10 / 0.0621 | — / — | 21.72 / 0.0279 | 29.08 / 0.0254 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.49 / 0.0755 | — / — | 20.89 / 0.0332 | 29.02 / 0.0266 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.57 / 0.0663 | — / — | 20.73 / 0.0328 | 29.22 / 0.0250 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 13.8%） | — | — | 25.19 / 0.0637 | — / — | 29.29 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 23.96 / 0.0724 | — | — | — |
| in035 | 2 | 0-3 | 25.41 / 0.0635 | — | — | — |
| in035 | 4 | 3-5 | 26.21 / 0.0552 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 25.19 / 0.0637 | — | 29.29 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.74 / 0.0813 | — | 28.85 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 10.0% | 26.23 / 0.0669 | — | 29.23 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 25.85 / 0.0840 | — | 29.12 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 9.7% | 26.56 / 0.0703 | — | 29.26 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 25.91 / 0.0777 | — | 29.23 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 6.3% | 26.50 / 0.0694 | — | 29.29 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.10 / 0.0621 | — | 29.08 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 9.9% | 27.27 / 0.0589 | — | 29.26 | 2/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 26.49 / 0.0755 | — | 29.02 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 9.9% | 26.80 / 0.0642 | — | 29.24 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 26.57 / 0.0663 | — | 29.22 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 6.1% | 26.72 / 0.0630 | — | 29.27 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 25.19 / 0.0637 | — / — | 29.29 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 25.74 / 0.0813 | — / — | 28.85 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 26.23 / 0.0669 | — / — | 29.23 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 18.16 / 0.0327 | 29.29 / 0.0247 | 25.19 / 0.0637 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 13.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.16 | 0.4943 | 0.0327 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.17 | 0.5203 | 0.0917 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.09 | 0.5461 | 0.0745 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.09 | 0.5461 | 0.0745 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 16.71 | 0.6180 | 0.0625 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 16.41 | 0.5645 | 0.0680 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 16.41 | 0.5645 | 0.0680 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.00 | 0.6254 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.55 | 0.6544 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.43 | 0.6400 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.72 | 0.7165 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.90 | 0.6697 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.73 | 0.6534 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.98 | 0.6248 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.55 | 0.6538 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.44 | 0.6399 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.72 | 0.7164 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.89 | 0.6691 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.73 | 0.6533 | 0.0328 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 51.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.24 | 0.7128 | 0.0458 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.88 | 0.6466 | 0.1683 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 17.82 | 0.6193 | 0.1557 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 17.82 | 0.6193 | 0.1557 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 18.46 | 0.6603 | 0.1259 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 18.20 | 0.6373 | 0.1416 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 18.20 | 0.6373 | 0.1416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.63 | 0.7477 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.96 | 0.7560 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.81 | 0.7493 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.91 | 0.7767 | 0.0410 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.32 | 0.7628 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.13 | 0.7553 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.92 | 0.7390 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.07 | 0.7396 | 0.0698 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.07 | 0.7366 | 0.0624 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.77 | 0.7732 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.98 | 0.7548 | 0.0572 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.93 | 0.7502 | 0.0497 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 56.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6955 | 0.0247 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.79 | 0.3768 | 0.2275 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.96 | 0.2869 | 0.1632 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.96 | 0.2869 | 0.1632 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.08 | 0.2984 | 0.1565 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 14.08 | 0.3019 | 0.1616 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 14.08 | 0.3019 | 0.1616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.23 | 0.6944 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.26 | 0.6950 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.29 | 0.6955 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.26 | 0.6952 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.24 | 0.6947 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.27 | 0.6954 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.85 | 0.6912 | 0.0287 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.12 | 0.6941 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.23 | 0.6953 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.08 | 0.6933 | 0.0254 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.02 | 0.6931 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.22 | 0.6952 | 0.0250 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.19 | 0.6979 | 0.0637 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.90 | 0.4959 | 0.3139 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.43 | 0.4453 | 0.2693 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.43 | 0.4453 | 0.2693 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.67 | 0.4709 | 0.2357 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.62 | 0.4608 | 0.2580 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.62 | 0.4608 | 0.2580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.23 | 0.7153 | 0.0669 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.56 | 0.7208 | 0.0703 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.50 | 0.7181 | 0.0694 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.27 | 0.7322 | 0.0589 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.80 | 0.7239 | 0.0642 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.72 | 0.7211 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.74 | 0.7100 | 0.0813 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.85 | 0.7133 | 0.0840 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.91 | 0.7121 | 0.0777 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.10 | 0.7294 | 0.0621 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.49 | 0.7189 | 0.0755 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.57 | 0.7187 | 0.0663 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1153 | None | classic | 1.99 | False | 453097 | 0.663 | 126.1 | 28.60 | 0.07 | 0.006 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2476363 | 0.800 | 221.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2476363 | 0.800 | 221.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1866489 | 0.800 | 8.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1866489 | 0.800 | 8.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1866489 | 0.800 | 8.9 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.650 | 0.061 |
| in035 | mask_ent | 0.652 | 0.061 |
| in035 | mask_grad | 0.451 | 0.061 |
| in035 | r_col | 0.810 | 0.061 |
| in035 | r_warp | 0.807 | 0.061 |
