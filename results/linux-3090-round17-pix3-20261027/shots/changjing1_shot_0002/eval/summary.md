# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 70.5% | 24.87 / 0.0873 | 26.60 / 0.1221 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 67.9% | 25.11 / 0.0866 | 26.06 / 0.1194 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 7.9% | 18.95 / 0.0404 | 19.97 / 0.0505 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 71.3% | 26.02 / 0.0924 | 27.99 / 0.0925 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 71.3% | 25.98 / 0.0915 | 27.54 / 0.1103 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 7.8% | 19.55 / 0.0418 | 21.42 / 0.0359 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.45 / 0.1183 | — / — | 16.84 / 0.0586 | 34.86 / 0.0245 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.93 / 0.1567 | — / — | 20.69 / 0.0379 | 33.81 / 0.0289 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.38 / 0.1425 | — / — | 19.20 / 0.0535 | 34.04 / 0.0302 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.84 / 0.1253 | — / — | 18.53 / 0.0542 | 33.40 / 0.0298 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.80 / 0.1274 | — / — | 19.79 / 0.0533 | 33.46 / 0.0240 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.52 / 0.1341 | — / — | 19.48 / 0.0466 | 33.27 / 0.0276 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.92 / 0.1162 | — / — | 18.70 / 0.0494 | 33.20 / 0.0254 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.3%） | — | — | 26.45 / 0.1183 | — / — | 34.86 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.21 / 0.1129 | — | — | — |
| in035 | 2 | 0-3 | 26.24 / 0.1144 | — | — | — |
| in035 | 4 | 3-5 | 26.89 / 0.1276 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.45 / 0.1183 | — | 34.86 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.93 / 0.1567 | — | 33.81 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.9% | 29.08 / 0.1026 | — | 34.84 | 3/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.38 / 0.1425 | — | 34.04 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 7.3% | 28.22 / 0.1173 | — | 34.87 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.84 / 0.1253 | — | 33.40 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 4.2% | 27.71 / 0.1158 | — | 34.86 | 2/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.80 / 0.1274 | — | 33.46 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 7.2% | 28.62 / 0.1162 | — | 34.86 | 2/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.52 / 0.1341 | — | 33.27 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 7.2% | 28.40 / 0.1101 | — | 34.86 | 3/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 26.92 / 0.1162 | — | 33.20 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 4.1% | 27.83 / 0.1107 | — | 34.86 | 3/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.45 / 0.1183 | — / — | 34.86 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.93 / 0.1567 | — / — | 33.81 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 29.08 / 0.1026 | — / — | 34.84 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 16.84 / 0.0586 | 34.86 / 0.0245 | 26.45 / 0.1183 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 16.84 | 0.5177 | 0.0586 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 19.77 | 0.7104 | 0.0483 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 17.86 | 0.6649 | 0.0674 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 17.86 | 0.6649 | 0.0674 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 19.78 | 0.6677 | 0.0603 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 19.13 | 0.6922 | 0.0536 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 19.13 | 0.6922 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.69 | 0.7155 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.22 | 0.6719 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.54 | 0.6147 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.82 | 0.6681 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.50 | 0.6854 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 18.71 | 0.6216 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.69 | 0.7163 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.20 | 0.6710 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.53 | 0.6138 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.79 | 0.6673 | 0.0533 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.48 | 0.6850 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 18.70 | 0.6211 | 0.0494 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 87.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.00 | 0.8131 | 0.1014 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 18.96 | 0.8083 | 0.2447 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.39 | 0.7468 | 0.2465 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.39 | 0.7468 | 0.2465 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 21.60 | 0.7562 | 0.2050 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 21.38 | 0.7762 | 0.2258 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 21.38 | 0.7762 | 0.2258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.90 | 0.8383 | 0.0926 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.85 | 0.8325 | 0.1088 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.29 | 0.8239 | 0.1052 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.35 | 0.8324 | 0.1053 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.11 | 0.8351 | 0.1003 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.44 | 0.8255 | 0.0984 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.59 | 0.8506 | 0.1414 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.72 | 0.8407 | 0.1376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.20 | 0.8185 | 0.1171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.45 | 0.8302 | 0.1137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.08 | 0.8459 | 0.1283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.46 | 0.8215 | 0.1053 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 19.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 34.86 | 0.8787 | 0.0245 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 24.99 | 0.8275 | 0.1496 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 25.72 | 0.7205 | 0.1478 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 25.72 | 0.7205 | 0.1478 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 25.98 | 0.7635 | 0.1088 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 25.90 | 0.7819 | 0.1150 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 25.90 | 0.7819 | 0.1150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 34.84 | 0.8782 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 34.87 | 0.8789 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 34.86 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 34.86 | 0.8788 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 34.86 | 0.8788 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 34.86 | 0.8787 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 33.81 | 0.8821 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 34.04 | 0.8820 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 33.40 | 0.8728 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 33.46 | 0.8646 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 33.27 | 0.8760 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 33.20 | 0.8706 | 0.0254 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.45 | 0.8242 | 0.1183 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 20.91 | 0.8117 | 0.2855 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.93 | 0.7250 | 0.2720 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.93 | 0.7250 | 0.2720 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 22.31 | 0.7537 | 0.2269 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 22.03 | 0.7792 | 0.2383 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 22.03 | 0.7792 | 0.2383 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.08 | 0.8460 | 0.1026 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.22 | 0.8418 | 0.1173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.71 | 0.8351 | 0.1158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.62 | 0.8404 | 0.1162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.40 | 0.8436 | 0.1101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.83 | 0.8360 | 0.1107 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.93 | 0.8603 | 0.1567 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.38 | 0.8544 | 0.1425 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.84 | 0.8313 | 0.1253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.80 | 0.8395 | 0.1274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.52 | 0.8591 | 0.1341 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.92 | 0.8326 | 0.1162 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1247 | None | classic | 2.32 | False | 233098 | 0.333 | 48.0 | 33.82 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2880123 | 0.799 | 229.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2880123 | 0.799 | 229.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2316848 | 0.799 | 9.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2316848 | 0.799 | 9.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2316848 | 0.799 | 9.4 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.718 | 0.052 |
| in035 | mask_ent | 0.760 | 0.052 |
| in035 | mask_grad | 0.472 | 0.052 |
| in035 | r_col | 0.721 | 0.052 |
| in035 | r_warp | 0.784 | 0.052 |
