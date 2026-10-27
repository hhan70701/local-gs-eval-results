# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 36.6% | 24.19 / 0.0589 | 25.36 / 0.0796 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 35.4% | 24.16 / 0.0650 | 21.36 / 0.1335 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.5% | 19.77 / 0.0403 | 16.36 / 0.1030 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 37.0% | 24.32 / 0.0657 | 25.97 / 0.0758 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 37.0% | 24.31 / 0.0660 | 24.67 / 0.1111 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 8.3% | 18.77 / 0.0388 | 19.35 / 0.0683 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.21 / 0.0825 | — / — | 17.48 / 0.0377 | 29.57 / 0.0332 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.07 / 0.0999 | — / — | 19.70 / 0.0327 | 29.57 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.48 / 0.1302 | — / — | 18.47 / 0.0551 | 29.53 / 0.0346 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.46 / 0.1246 | — / — | 18.44 / 0.0547 | 29.48 / 0.0346 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.29 / 0.0962 | — / — | 19.75 / 0.0437 | 29.60 / 0.0327 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.53 / 0.1178 | — / — | 19.38 / 0.0494 | 29.55 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.54 / 0.1075 | — / — | 19.28 / 0.0490 | 29.48 / 0.0350 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 8.3%） | — | — | 26.21 / 0.0825 | — / — | 29.57 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.97 / 0.0857 | — | — | — |
| in035 | 2 | 0-3 | 26.01 / 0.0836 | — | — | — |
| in035 | 4 | 3-5 | 27.65 / 0.0783 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.21 / 0.0825 | — | 29.57 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.07 / 0.0999 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.7% | 27.36 / 0.0789 | — | 29.56 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 24.48 / 0.1302 | — | 29.53 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 5.5% | 26.54 / 0.1003 | — | 29.56 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 24.46 / 0.1246 | — | 29.48 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 4.5% | 26.52 / 0.0997 | — | 29.56 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.29 / 0.0962 | — | 29.60 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 5.5% | 27.42 / 0.0892 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 26.53 / 0.1178 | — | 29.55 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 5.5% | 27.18 / 0.0944 | — | 29.56 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 26.54 / 0.1075 | — | 29.48 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 4.3% | 27.13 / 0.0940 | — | 29.56 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.21 / 0.0825 | — / — | 29.57 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.07 / 0.0999 | — / — | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.36 / 0.0789 | — / — | 29.56 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 17.48 / 0.0377 | 29.57 / 0.0332 | 26.21 / 0.0825 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 8.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.48 | 0.5080 | 0.0377 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.80 | 0.5383 | 0.0847 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.70 | 0.4873 | 0.0896 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.70 | 0.4873 | 0.0896 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 16.81 | 0.5574 | 0.0734 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 16.49 | 0.5245 | 0.0815 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 16.49 | 0.5245 | 0.0815 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.71 | 0.6123 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 18.48 | 0.5621 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.44 | 0.5521 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.75 | 0.6148 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.40 | 0.5911 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.29 | 0.5750 | 0.0488 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.70 | 0.6115 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 18.47 | 0.5598 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.44 | 0.5499 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.75 | 0.6142 | 0.0437 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.38 | 0.5890 | 0.0494 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.28 | 0.5731 | 0.0490 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 53.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.54 | 0.7580 | 0.0600 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.70 | 0.6837 | 0.2246 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.68 | 0.6001 | 0.2189 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.68 | 0.6001 | 0.2189 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 17.79 | 0.6360 | 0.1780 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 17.54 | 0.6236 | 0.2014 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 17.54 | 0.6236 | 0.2014 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.97 | 0.7718 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.91 | 0.7586 | 0.0785 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.88 | 0.7569 | 0.0773 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.12 | 0.7721 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.79 | 0.7668 | 0.0720 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.71 | 0.7638 | 0.0712 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.45 | 0.7739 | 0.0762 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.26 | 0.7273 | 0.1106 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.25 | 0.7245 | 0.1060 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.91 | 0.7592 | 0.0726 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.86 | 0.7480 | 0.0939 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.91 | 0.7483 | 0.0868 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 52.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.57 | 0.6892 | 0.0332 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.04 | 0.3373 | 0.2932 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.06 | 0.2410 | 0.2127 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.06 | 0.2410 | 0.2127 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.51 | 0.2640 | 0.1975 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.50 | 0.2700 | 0.2054 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.50 | 0.2700 | 0.2054 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.57 | 0.6892 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.56 | 0.6890 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.57 | 0.6912 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.53 | 0.6903 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.48 | 0.6886 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.60 | 0.6889 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.55 | 0.6910 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.48 | 0.6882 | 0.0350 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.21 | 0.7197 | 0.0825 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.30 | 0.5106 | 0.3790 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.22 | 0.4313 | 0.3434 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.22 | 0.4313 | 0.3434 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 17.03 | 0.4588 | 0.2951 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 16.93 | 0.4575 | 0.3235 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 16.93 | 0.4575 | 0.3235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.36 | 0.7278 | 0.0789 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.54 | 0.7209 | 0.1003 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.52 | 0.7200 | 0.0997 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.42 | 0.7272 | 0.0892 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.18 | 0.7246 | 0.0944 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.13 | 0.7232 | 0.0940 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.07 | 0.7312 | 0.0999 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.48 | 0.7077 | 0.1302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.46 | 0.7049 | 0.1246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.29 | 0.7206 | 0.0962 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.53 | 0.7175 | 0.1178 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.54 | 0.7159 | 0.1075 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1144 | None | classic | 1.96 | False | 620222 | 0.992 | 139.0 | 31.24 | 0.10 | 0.004 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2034187 | 0.804 | 218.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2034187 | 0.804 | 218.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1670549 | 0.804 | 8.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1670549 | 0.804 | 8.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1670549 | 0.804 | 8.9 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.857 | 0.040 |
| in035 | mask_ent | 0.644 | 0.040 |
| in035 | mask_grad | 0.452 | 0.040 |
| in035 | r_col | 0.848 | 0.040 |
| in035 | r_warp | 0.843 | 0.040 |
