# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 18.8% | 15.05 / 0.0464 | 18.94 / 0.0442 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 18.2% | 14.98 / 0.0464 | 15.53 / 0.0534 | — | — |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | 26.8% | 16.41 / 0.0500 | 16.06 / 0.0747 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 26.9% | 16.41 / 0.0501 | 16.08 / 0.0738 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 14.9% | 14.01 / 0.0428 | 13.65 / 0.0625 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 26.8% | 16.41 / 0.0499 | 17.49 / 0.0662 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 26.8% | 16.41 / 0.0500 | 17.15 / 0.0697 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 21.54 / 0.0828 | — / — | 13.44 / 0.0450 | 29.95 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.59 / 0.0780 | — / — | 17.55 / 0.0345 | 29.68 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.02 / 0.0862 | — / — | 14.40 / 0.0439 | 29.71 / 0.0367 |
| in035 | hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 21.21 / 0.1043 | — / — | 13.82 / 0.0472 | 28.56 / 0.0480 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.23 / 0.1044 | — / — | 13.85 / 0.0471 | 28.47 / 0.0483 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 21.23 / 0.0998 | — / — | 13.84 / 0.0470 | 28.50 / 0.0451 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 22.42 / 0.0953 | — / — | 15.44 / 0.0369 | 28.44 / 0.0490 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 22.11 / 0.1000 | — / — | 15.04 / 0.0410 | 28.40 / 0.0494 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 13.5%） | — | — | 21.54 / 0.0828 | — / — | 29.95 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 | f4rq |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 22.44 / 0.0772 | — | — | — | — |
| in035 | 2 | 0-3 | 19.37 / 0.0894 | — | — | — | — |
| in035 | 4 | 3-5 | 22.81 / 0.0817 | — | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 21.54 / 0.0828 | — | 29.95 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 24.59 / 0.0780 | — | 29.68 | 3/3 |
| in035 | cnw_cnn_mw | oracle | 9.9% | 24.80 / 0.0732 | — | 29.94 | 3/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 22.02 / 0.0862 | — | 29.71 | 2/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 9.5% | 22.26 / 0.0817 | — | 29.92 | 2/3 |
| in035 | f4rq_pix3_fsl | 不复核 | —% | 21.21 / 0.1043 | — | 28.56 | 0/3 |
| in035 | f4rq_pix3_fsl | oracle | 10.1% | 21.73 / 0.0860 | — | 29.87 | 2/3 |
| in035 | f4rq_pix3bg_fsl | 不复核 | —% | 21.23 / 0.1044 | — | 28.47 | 0/3 |
| in035 | f4rq_pix3bg_fsl | oracle | 10.1% | 21.76 / 0.0860 | — | 29.88 | 2/3 |
| in035 | f4rq_pix3bg_fsl_g | 不复核 | —% | 21.23 / 0.0998 | — | 28.50 | 0/3 |
| in035 | f4rq_pix3bg_fsl_g | oracle | 9.5% | 21.75 / 0.0857 | — | 29.87 | 2/3 |
| in035 | f4rq_pix3bg_fsl_s25 | 不复核 | —% | 22.42 / 0.0953 | — | 28.44 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s25 | oracle | 10.1% | 23.08 / 0.0753 | — | 29.88 | 2/3 |
| in035 | f4rq_pix3bg_fsl_s50 | 不复核 | —% | 22.11 / 0.1000 | — | 28.40 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | oracle | 10.1% | 22.74 / 0.0800 | — | 29.87 | 2/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 21.54 / 0.0828 | — / — | 29.95 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 24.59 / 0.0780 | — / — | 29.68 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 24.80 / 0.0732 | — / — | 29.94 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 13.44 / 0.0450 | 29.95 / 0.0356 | 21.54 / 0.0828 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 13.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 13.44 | 0.3787 | 0.0450 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.68 | 0.4284 | 0.1163 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.53 | 0.3337 | 0.0914 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 12.63 | 0.3636 | 0.0830 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 12.66 | 0.3633 | 0.0832 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 12.66 | 0.3633 | 0.0832 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 13.82 | 0.4899 | 0.0728 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 13.55 | 0.4200 | 0.0772 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 17.55 | 0.5580 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 14.40 | 0.4641 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 13.82 | 0.4531 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 13.86 | 0.4533 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 13.85 | 0.4493 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 15.45 | 0.5822 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 15.05 | 0.5114 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 17.55 | 0.5579 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 14.40 | 0.4634 | 0.0439 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 13.82 | 0.4523 | 0.0472 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 13.85 | 0.4525 | 0.0471 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 13.84 | 0.4490 | 0.0470 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 15.44 | 0.5813 | 0.0369 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 15.04 | 0.5105 | 0.0410 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 36.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.50 | 0.6367 | 0.0515 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.55 | 0.4901 | 0.2325 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.30 | 0.3642 | 0.1923 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 14.11 | 0.4423 | 0.1630 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 14.15 | 0.4452 | 0.1611 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 14.15 | 0.4452 | 0.1611 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 14.81 | 0.4922 | 0.1534 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 14.63 | 0.4656 | 0.1565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.31 | 0.7078 | 0.0430 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 18.31 | 0.6661 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 17.75 | 0.6591 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 17.78 | 0.6592 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 17.77 | 0.6565 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 19.28 | 0.7086 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 18.91 | 0.6815 | 0.0485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.93 | 0.7017 | 0.0482 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 18.03 | 0.6543 | 0.0567 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 17.32 | 0.6282 | 0.0695 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 17.35 | 0.6287 | 0.0692 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 17.34 | 0.6284 | 0.0668 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 18.72 | 0.6771 | 0.0619 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 18.39 | 0.6500 | 0.0651 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 71.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.95 | 0.7213 | 0.0356 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.74 | 0.3212 | 0.3710 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.70 | 0.1703 | 0.2746 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 14.75 | 0.3234 | 0.2280 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 14.75 | 0.3233 | 0.2283 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 14.75 | 0.3233 | 0.2283 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 14.75 | 0.3264 | 0.2301 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 14.74 | 0.3245 | 0.2299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.94 | 0.7213 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.92 | 0.7211 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.87 | 0.7207 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.88 | 0.7207 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.87 | 0.7206 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.88 | 0.7207 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.87 | 0.7206 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7211 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.71 | 0.7204 | 0.0367 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.56 | 0.7114 | 0.0480 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.47 | 0.7110 | 0.0483 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.50 | 0.7125 | 0.0451 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.44 | 0.7114 | 0.0490 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.40 | 0.7109 | 0.0494 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.54 | 0.6863 | 0.0828 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.67 | 0.3587 | 0.4458 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.78 | 0.2226 | 0.3867 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 14.36 | 0.3517 | 0.3225 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 14.37 | 0.3517 | 0.3229 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 14.37 | 0.3517 | 0.3229 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 14.63 | 0.3724 | 0.3157 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 14.55 | 0.3607 | 0.3189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.80 | 0.7106 | 0.0732 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.26 | 0.6953 | 0.0817 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 21.73 | 0.6917 | 0.0860 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.76 | 0.6918 | 0.0860 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 21.75 | 0.6909 | 0.0857 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 23.08 | 0.7101 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 22.74 | 0.7000 | 0.0800 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.59 | 0.7091 | 0.0780 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.02 | 0.6919 | 0.0862 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 21.21 | 0.6761 | 0.1043 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.23 | 0.6760 | 0.1044 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 21.23 | 0.6768 | 0.0998 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 22.42 | 0.6950 | 0.0953 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 22.11 | 0.6842 | 0.1000 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1064 | None | classic | 1.69 | False | 401387 | 0.330 | 70.3 | 24.87 | 0.11 | 0.025 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1156306 | 0.799 | 10.0 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1982723 | 0.799 | 1.8 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2008584 | 0.799 | 1.8 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2008584 | 0.799 | 1.8 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2008584 | 0.799 | 1.8 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2008584 | 0.799 | 1.8 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.748 | 0.092 |
| in035 | mask_ent | 0.680 | 0.092 |
| in035 | mask_grad | 0.278 | 0.092 |
| in035 | r_col | 0.920 | 0.092 |
| in035 | r_warp | 0.962 | 0.092 |
