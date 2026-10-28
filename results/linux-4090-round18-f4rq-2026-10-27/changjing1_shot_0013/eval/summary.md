# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.4% | 24.52 / 0.0148 | 22.24 / 0.0279 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.2% | 24.73 / 0.0160 | 23.25 / 0.0242 | — | — |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | 20.9% | 26.67 / 0.0248 | 27.72 / 0.0314 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 21.0% | 26.68 / 0.0248 | 27.69 / 0.0320 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 3.4% | 21.49 / 0.0104 | 21.61 / 0.0157 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 20.9% | 26.67 / 0.0247 | 27.76 / 0.0341 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 20.9% | 26.68 / 0.0248 | 27.79 / 0.0325 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.02 / 0.0578 | — / — | 19.50 / 0.0172 | 29.74 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.94 / 0.0668 | — / — | 20.31 / 0.0180 | 29.60 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.73 / 0.0629 | — / — | 19.86 / 0.0193 | 29.63 / 0.0347 |
| in035 | hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.46 / 0.0618 | — / — | 21.06 / 0.0168 | 29.66 / 0.0352 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.47 / 0.0620 | — / — | 21.07 / 0.0169 | 29.66 / 0.0352 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.29 / 0.0598 | — / — | 20.58 / 0.0177 | 29.65 / 0.0350 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.48 / 0.0640 | — / — | 21.21 / 0.0176 | 29.68 / 0.0355 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.47 / 0.0629 | — / — | 21.13 / 0.0172 | 29.67 / 0.0353 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.5%） | — | — | 28.02 / 0.0578 | — / — | 29.74 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 | f4rq |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.77 / 0.0623 | — | — | — | — |
| in035 | 2 | 0-3 | 28.34 / 0.0530 | — | — | — | — |
| in035 | 4 | 3-5 | 28.94 / 0.0581 | — | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.02 / 0.0578 | — | 29.74 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.94 / 0.0668 | — | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.27 / 0.0597 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.73 / 0.0629 | — | 29.63 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.4% | 28.05 / 0.0603 | — | 29.73 | 0/3 |
| in035 | f4rq_pix3_fsl | 不复核 | —% | 28.46 / 0.0618 | — | 29.66 | 1/3 |
| in035 | f4rq_pix3_fsl | oracle | 2.5% | 28.59 / 0.0584 | — | 29.74 | 2/3 |
| in035 | f4rq_pix3bg_fsl | 不复核 | —% | 28.47 / 0.0620 | — | 29.66 | 1/3 |
| in035 | f4rq_pix3bg_fsl | oracle | 2.5% | 28.59 / 0.0584 | — | 29.74 | 1/3 |
| in035 | f4rq_pix3bg_fsl_g | 不复核 | —% | 28.29 / 0.0598 | — | 29.65 | 1/3 |
| in035 | f4rq_pix3bg_fsl_g | oracle | 1.3% | 28.42 / 0.0584 | — | 29.74 | 1/3 |
| in035 | f4rq_pix3bg_fsl_s25 | 不复核 | —% | 28.48 / 0.0640 | — | 29.68 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s25 | oracle | 2.5% | 28.61 / 0.0590 | — | 29.74 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | 不复核 | —% | 28.47 / 0.0629 | — | 29.67 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | oracle | 2.5% | 28.60 / 0.0587 | — | 29.74 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.02 / 0.0578 | — / — | 29.74 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.94 / 0.0668 | — / — | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.27 / 0.0597 | — / — | 29.73 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.50 / 0.0172 | 29.74 / 0.0344 | 28.02 / 0.0578 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.50 | 0.5831 | 0.0172 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.95 | 0.4616 | 0.0935 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.65 | 0.4461 | 0.0579 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 13.60 | 0.4759 | 0.0503 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 13.60 | 0.4766 | 0.0504 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 13.60 | 0.4766 | 0.0504 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 13.63 | 0.4708 | 0.0512 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 13.61 | 0.4735 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.33 | 0.6649 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.87 | 0.6654 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 21.04 | 0.6994 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.05 | 0.6995 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 20.56 | 0.6537 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 21.19 | 0.6958 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.11 | 0.6983 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.31 | 0.6650 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.86 | 0.6647 | 0.0193 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 21.06 | 0.7001 | 0.0168 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.07 | 0.7001 | 0.0169 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 20.58 | 0.6542 | 0.0177 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 21.21 | 0.6963 | 0.0176 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.13 | 0.6989 | 0.0172 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.37 | 0.7729 | 0.0297 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.68 | 0.5640 | 0.2292 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.92 | 0.5076 | 0.1765 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 16.17 | 0.5972 | 0.1355 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 16.20 | 0.5989 | 0.1352 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 16.20 | 0.5989 | 0.1352 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 16.18 | 0.5963 | 0.1370 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 16.18 | 0.5980 | 0.1359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.59 | 0.7831 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.48 | 0.7887 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.42 | 0.7965 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.43 | 0.7965 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 27.06 | 0.7864 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.49 | 0.7953 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.46 | 0.7961 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.11 | 0.7693 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.56 | 0.7792 | 0.0370 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.03 | 0.7905 | 0.0363 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.01 | 0.7904 | 0.0367 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.67 | 0.7789 | 0.0348 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.03 | 0.7883 | 0.0386 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.05 | 0.7901 | 0.0373 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 71.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.74 | 0.7047 | 0.0344 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.72 | 0.3013 | 0.3529 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.26 | 0.1858 | 0.2502 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 13.47 | 0.2323 | 0.2257 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 13.47 | 0.2324 | 0.2255 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 13.47 | 0.2324 | 0.2255 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 13.46 | 0.2347 | 0.2277 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 13.46 | 0.2335 | 0.2266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7047 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.73 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.60 | 0.7047 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.63 | 0.7046 | 0.0347 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.66 | 0.7048 | 0.0352 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.66 | 0.7049 | 0.0352 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.65 | 0.7042 | 0.0350 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.68 | 0.7054 | 0.0355 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.67 | 0.7052 | 0.0353 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.02 | 0.7204 | 0.0578 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.70 | 0.3814 | 0.4245 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.90 | 0.2947 | 0.3403 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 14.13 | 0.3440 | 0.3045 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 14.13 | 0.3441 | 0.3047 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 14.13 | 0.3441 | 0.3047 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 14.12 | 0.3449 | 0.3093 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 14.12 | 0.3444 | 0.3069 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.27 | 0.7256 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.05 | 0.7267 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.59 | 0.7295 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.59 | 0.7295 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.42 | 0.7261 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.61 | 0.7290 | 0.0590 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.60 | 0.7293 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.94 | 0.7238 | 0.0668 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.73 | 0.7253 | 0.0629 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.46 | 0.7300 | 0.0618 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.47 | 0.7299 | 0.0620 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.29 | 0.7252 | 0.0598 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.48 | 0.7296 | 0.0640 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.47 | 0.7299 | 0.0629 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 905 | None | classic | 1.22 | False | 732752 | 0.688 | 113.3 | 28.90 | 0.13 | 0.017 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1151962 | 0.797 | 9.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1649338 | 0.797 | 1.5 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1666845 | 0.797 | 1.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1666845 | 0.797 | 1.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1666845 | 0.797 | 1.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1666845 | 0.797 | 1.6 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.741 | 0.019 |
| in035 | mask_ent | 0.634 | 0.019 |
| in035 | mask_grad | 0.460 | 0.019 |
| in035 | r_col | 0.839 | 0.019 |
| in035 | r_warp | 0.874 | 0.019 |
