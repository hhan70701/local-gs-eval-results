# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 20.8% | 25.30 / 0.0387 | 25.06 / 0.0591 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 18.3% | 25.07 / 0.0368 | 26.31 / 0.0690 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 3.5% | 20.26 / 0.0307 | 21.49 / 0.0452 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 21.0% | 25.98 / 0.0392 | 28.36 / 0.0447 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 21.0% | 25.97 / 0.0394 | 28.31 / 0.0556 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 3.4% | 20.96 / 0.0342 | 23.68 / 0.0368 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.97 / 0.0729 | — / — | 18.57 / 0.0236 | 29.89 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.12 / 0.0889 | — / — | 19.65 / 0.0267 | 29.77 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.70 / 0.0968 | — / — | 20.86 / 0.0316 | 29.88 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.74 / 0.0847 | — / — | 20.60 / 0.0296 | 29.87 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.92 / 0.0813 | — / — | 20.81 / 0.0282 | 29.89 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.95 / 0.0882 | — / — | 20.99 / 0.0279 | 29.88 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.90 / 0.0779 | — / — | 20.65 / 0.0261 | 29.89 / 0.0352 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.5%） | — | — | 27.97 / 0.0729 | — / — | 29.89 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.51 / 0.0753 | — | — | — |
| in035 | 2 | 0-3 | 26.83 / 0.0803 | — | — | — |
| in035 | 4 | 3-5 | 29.57 / 0.0633 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.97 / 0.0729 | — | 29.89 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.12 / 0.0889 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.6% | 28.50 / 0.0750 | — | 29.87 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.70 / 0.0968 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.4% | 28.99 / 0.0807 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.74 / 0.0847 | — | 29.87 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.7% | 28.92 / 0.0792 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 28.92 / 0.0813 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.5% | 28.99 / 0.0776 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 28.95 / 0.0882 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.5% | 29.06 / 0.0773 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 28.90 / 0.0779 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.6% | 28.97 / 0.0761 | — | 29.89 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.97 / 0.0729 | — / — | 29.89 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.12 / 0.0889 | — / — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.50 / 0.0750 | — / — | 29.87 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 18.57 / 0.0236 | 29.89 / 0.0350 | 27.97 / 0.0729 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.57 | 0.5923 | 0.0236 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.36 | 0.4605 | 0.0941 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.62 | 0.4393 | 0.0871 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.62 | 0.4393 | 0.0871 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.74 | 0.4564 | 0.0817 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.75 | 0.4599 | 0.0820 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.75 | 0.4599 | 0.0820 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.65 | 0.6467 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.86 | 0.6734 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.60 | 0.6579 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.82 | 0.6755 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.99 | 0.6833 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.66 | 0.6611 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.65 | 0.6464 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.86 | 0.6734 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.60 | 0.6580 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.81 | 0.6758 | 0.0282 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.99 | 0.6834 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.65 | 0.6611 | 0.0261 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 47.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.65 | 0.7947 | 0.0404 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.21 | 0.6436 | 0.2529 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.02 | 0.5036 | 0.2372 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.02 | 0.5036 | 0.2372 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.11 | 0.5141 | 0.2098 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.10 | 0.5216 | 0.2208 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.10 | 0.5216 | 0.2208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.27 | 0.7985 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.26 | 0.8040 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.09 | 0.8018 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.31 | 0.8053 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.42 | 0.8068 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.18 | 0.8030 | 0.0440 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.44 | 0.7964 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.55 | 0.7983 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.65 | 0.7978 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.14 | 0.8028 | 0.0479 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.15 | 0.8082 | 0.0557 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.03 | 0.8021 | 0.0458 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 57.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.89 | 0.7134 | 0.0350 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.94 | 0.3224 | 0.3828 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.96 | 0.1606 | 0.3056 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.96 | 0.1606 | 0.3056 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.40 | 0.1805 | 0.2973 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.40 | 0.1846 | 0.3020 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.40 | 0.1846 | 0.3020 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.87 | 0.7134 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.89 | 0.7135 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7137 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.88 | 0.7136 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.87 | 0.7133 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.89 | 0.7131 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.88 | 0.7140 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.89 | 0.7135 | 0.0352 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.97 | 0.7525 | 0.0729 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.70 | 0.4798 | 0.4851 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.49 | 0.3359 | 0.4348 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.49 | 0.3359 | 0.4348 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.88 | 0.3499 | 0.4051 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.88 | 0.3581 | 0.4200 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.88 | 0.3581 | 0.4200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.50 | 0.7553 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.99 | 0.7574 | 0.0807 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.92 | 0.7567 | 0.0792 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.99 | 0.7575 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.06 | 0.7583 | 0.0773 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.97 | 0.7571 | 0.0761 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.12 | 0.7564 | 0.0889 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.70 | 0.7570 | 0.0968 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.74 | 0.7557 | 0.0847 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.92 | 0.7562 | 0.0813 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.95 | 0.7605 | 0.0882 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.90 | 0.7569 | 0.0779 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1056 | None | classic | 1.67 | False | 435491 | 0.645 | 118.2 | 30.28 | 0.11 | 0.005 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1535405 | 0.791 | 203.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1535405 | 0.791 | 203.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1139608 | 0.791 | 8.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1139608 | 0.791 | 8.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1139608 | 0.791 | 8.7 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.795 | 0.022 |
| in035 | mask_ent | 0.752 | 0.022 |
| in035 | mask_grad | 0.533 | 0.022 |
| in035 | r_col | 0.769 | 0.022 |
| in035 | r_warp | 0.824 | 0.022 |
