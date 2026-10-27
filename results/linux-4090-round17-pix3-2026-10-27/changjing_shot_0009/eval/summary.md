# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.8% | 23.89 / 0.0181 | 21.89 / 0.0359 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.0% | 23.28 / 0.0175 | 22.91 / 0.0412 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.9% | 20.59 / 0.0138 | 20.02 / 0.0289 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.1% | 24.60 / 0.0195 | 26.29 / 0.0226 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.1% | 24.57 / 0.0194 | 25.95 / 0.0282 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.8% | 20.58 / 0.0123 | 22.94 / 0.0139 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.61 / 0.0671 | — / — | 19.53 / 0.0194 | 31.02 / 0.0297 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.96 / 0.0802 | — / — | 19.73 / 0.0219 | 30.66 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.70 / 0.0834 | — / — | 20.45 / 0.0250 | 30.96 / 0.0303 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.75 / 0.0771 | — / — | 20.36 / 0.0240 | 30.94 / 0.0299 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.20 / 0.0718 | — / — | 21.01 / 0.0210 | 30.97 / 0.0301 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.15 / 0.0749 | — / — | 20.95 / 0.0213 | 30.97 / 0.0308 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.15 / 0.0697 | — / — | 20.78 / 0.0208 | 30.97 / 0.0299 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.1%） | — | — | 28.61 / 0.0671 | — / — | 31.02 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.84 / 0.0719 | — | — | — |
| in035 | 2 | 0-3 | 28.40 / 0.0707 | — | — | — |
| in035 | 4 | 3-5 | 29.58 / 0.0586 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.61 / 0.0671 | — | 31.02 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.96 / 0.0802 | — | 30.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.58 / 0.0705 | — | 31.01 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.70 / 0.0834 | — | 30.96 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.3% | 28.99 / 0.0734 | — | 31.03 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.75 / 0.0771 | — | 30.94 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.6% | 28.96 / 0.0722 | — | 31.02 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 29.20 / 0.0718 | — | 30.97 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.4% | 29.29 / 0.0687 | — | 31.03 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 29.15 / 0.0749 | — | 30.97 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.4% | 29.26 / 0.0693 | — | 31.02 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 29.15 / 0.0697 | — | 30.97 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.5% | 29.20 / 0.0686 | — | 31.03 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.61 / 0.0671 | — / — | 31.02 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.96 / 0.0802 | — / — | 30.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.58 / 0.0705 | — / — | 31.01 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.53 / 0.0194 | 31.02 / 0.0297 | 28.61 / 0.0671 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.53 | 0.6039 | 0.0194 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.01 | 0.4156 | 0.0977 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.85 | 0.4271 | 0.0905 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.85 | 0.4271 | 0.0905 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.99 | 0.4637 | 0.0845 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.95 | 0.4517 | 0.0847 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.95 | 0.4517 | 0.0847 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.74 | 0.6634 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.45 | 0.6800 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.36 | 0.6664 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.00 | 0.7083 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.95 | 0.6984 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.78 | 0.6789 | 0.0207 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.73 | 0.6623 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.45 | 0.6798 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.36 | 0.6664 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.01 | 0.7074 | 0.0210 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.95 | 0.6979 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.78 | 0.6790 | 0.0208 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 52.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.26 | 0.7816 | 0.0389 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.88 | 0.4678 | 0.3446 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.19 | 0.3347 | 0.3137 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.19 | 0.3347 | 0.3137 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.55 | 0.3622 | 0.2926 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.54 | 0.3672 | 0.2990 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.54 | 0.3672 | 0.2990 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.93 | 0.7799 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.72 | 0.7877 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.68 | 0.7863 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.18 | 0.7934 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.14 | 0.7918 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.05 | 0.7892 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.13 | 0.7710 | 0.0507 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.22 | 0.7823 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.33 | 0.7830 | 0.0498 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.05 | 0.7910 | 0.0434 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.98 | 0.7905 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.99 | 0.7888 | 0.0414 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 51.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.02 | 0.7636 | 0.0297 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.72 | 0.3214 | 0.3306 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.49 | 0.2331 | 0.2817 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.49 | 0.2331 | 0.2817 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.83 | 0.2570 | 0.2739 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.82 | 0.2630 | 0.2787 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.82 | 0.2630 | 0.2787 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.01 | 0.7635 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.03 | 0.7636 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.02 | 0.7636 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 31.03 | 0.7636 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 31.02 | 0.7636 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 31.03 | 0.7636 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.66 | 0.7628 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.96 | 0.7646 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.94 | 0.7635 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.97 | 0.7636 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 30.97 | 0.7649 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 30.97 | 0.7633 | 0.0299 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.61 | 0.7715 | 0.0671 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.79 | 0.4007 | 0.5131 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.18 | 0.2798 | 0.4702 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.18 | 0.2798 | 0.4702 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.57 | 0.3050 | 0.4441 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.56 | 0.3113 | 0.4551 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.56 | 0.3113 | 0.4551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.58 | 0.7737 | 0.0705 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.99 | 0.7759 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.96 | 0.7749 | 0.0722 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.29 | 0.7783 | 0.0687 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.26 | 0.7776 | 0.0693 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.20 | 0.7762 | 0.0686 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.96 | 0.7700 | 0.0802 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.70 | 0.7744 | 0.0834 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.75 | 0.7736 | 0.0771 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.20 | 0.7772 | 0.0718 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.15 | 0.7781 | 0.0749 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.15 | 0.7760 | 0.0697 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1126 | None | classic | 0.39 | False | 778826 | 0.686 | 124.9 | 30.53 | 0.23 | 0.005 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1391705 | 0.806 | 91.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1391705 | 0.806 | 91.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1075996 | 0.806 | 9.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1075996 | 0.806 | 6.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1075996 | 0.806 | 6.6 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.705 | 0.021 |
| in035 | mask_ent | 0.792 | 0.021 |
| in035 | mask_grad | 0.498 | 0.021 |
| in035 | r_col | 0.690 | 0.021 |
| in035 | r_warp | 0.873 | 0.021 |
