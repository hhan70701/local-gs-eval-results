# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 28.7% | 23.08 / 0.0273 | 21.44 / 0.0564 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 27.8% | 23.09 / 0.0284 | 23.51 / 0.0351 | — | — |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | 44.2% | 23.99 / 0.0298 | 23.69 / 0.0464 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 44.3% | 23.99 / 0.0309 | 23.70 / 0.0479 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 11.4% | 20.20 / 0.0168 | 19.44 / 0.0263 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 44.3% | 23.99 / 0.0310 | 23.91 / 0.0481 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 44.3% | 23.99 / 0.0310 | 23.77 / 0.0475 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.26 / 0.0511 | — / — | 18.64 / 0.0196 | 30.26 / 0.0246 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.78 / 0.0732 | — / — | 19.26 / 0.0223 | 28.87 / 0.0327 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.99 / 0.0567 | — / — | 20.19 / 0.0189 | 30.01 / 0.0266 |
| in035 | hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 26.42 / 0.0640 | — / — | 19.95 / 0.0200 | 29.47 / 0.0314 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 26.42 / 0.0638 | — / — | 19.95 / 0.0200 | 29.48 / 0.0311 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.44 / 0.0573 | — / — | 19.74 / 0.0206 | 29.74 / 0.0266 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 26.54 / 0.0636 | — / — | 20.18 / 0.0193 | 29.51 / 0.0314 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 26.45 / 0.0638 | — / — | 20.02 / 0.0196 | 29.44 / 0.0314 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 10.3%） | — | — | 26.26 / 0.0511 | — / — | 30.26 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 | f4rq |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.33 / 0.0590 | — | — | — | — |
| in035 | 2 | 0-3 | 25.81 / 0.0512 | — | — | — | — |
| in035 | 4 | 3-5 | 28.63 / 0.0432 | — | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.26 / 0.0511 | — | 30.26 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.78 / 0.0732 | — | 28.87 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.4% | 26.67 / 0.0576 | — | 30.13 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 26.99 / 0.0567 | — | 30.01 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 7.2% | 27.32 / 0.0510 | — | 30.24 | 1/3 |
| in035 | f4rq_pix3_fsl | 不复核 | —% | 26.42 / 0.0640 | — | 29.47 | 0/3 |
| in035 | f4rq_pix3_fsl | oracle | 8.7% | 27.12 / 0.0522 | — | 30.19 | 1/3 |
| in035 | f4rq_pix3bg_fsl | 不复核 | —% | 26.42 / 0.0638 | — | 29.48 | 0/3 |
| in035 | f4rq_pix3bg_fsl | oracle | 8.7% | 27.12 / 0.0522 | — | 30.19 | 1/3 |
| in035 | f4rq_pix3bg_fsl_g | 不复核 | —% | 26.44 / 0.0573 | — | 29.74 | 0/3 |
| in035 | f4rq_pix3bg_fsl_g | oracle | 5.4% | 26.99 / 0.0528 | — | 30.20 | 1/3 |
| in035 | f4rq_pix3bg_fsl_s25 | 不复核 | —% | 26.54 / 0.0636 | — | 29.51 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s25 | oracle | 8.7% | 27.24 / 0.0515 | — | 30.21 | 1/3 |
| in035 | f4rq_pix3bg_fsl_s50 | 不复核 | —% | 26.45 / 0.0638 | — | 29.44 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | oracle | 8.7% | 27.16 / 0.0517 | — | 30.19 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.26 / 0.0511 | — / — | 30.26 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 25.78 / 0.0732 | — / — | 28.87 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 26.67 / 0.0576 | — / — | 30.13 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 18.64 / 0.0196 | 30.26 / 0.0246 | 26.26 / 0.0511 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 10.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.64 | 0.5046 | 0.0196 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.74 | 0.5001 | 0.0519 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 18.02 | 0.5883 | 0.0308 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 19.54 | 0.6213 | 0.0239 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 19.56 | 0.6228 | 0.0234 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 19.56 | 0.6228 | 0.0234 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 19.75 | 0.6208 | 0.0231 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 19.62 | 0.6205 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.29 | 0.5738 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.21 | 0.6373 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 19.95 | 0.6274 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 19.95 | 0.6281 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 19.74 | 0.6003 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 20.18 | 0.6271 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 20.02 | 0.6265 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.26 | 0.5707 | 0.0223 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.19 | 0.6364 | 0.0189 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 19.95 | 0.6261 | 0.0200 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 19.95 | 0.6267 | 0.0200 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 19.74 | 0.5997 | 0.0206 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 20.18 | 0.6258 | 0.0193 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 20.02 | 0.6253 | 0.0196 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 47.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.26 | 0.7219 | 0.0302 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.28 | 0.5430 | 0.2003 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.93 | 0.5306 | 0.1432 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 18.72 | 0.6093 | 0.1132 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 19.26 | 0.6203 | 0.1093 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 19.26 | 0.6203 | 0.1093 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 19.25 | 0.6221 | 0.1082 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 19.24 | 0.6212 | 0.1090 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.56 | 0.7352 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.29 | 0.7553 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 25.00 | 0.7521 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 25.00 | 0.7525 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 24.84 | 0.7422 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 25.19 | 0.7526 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 25.08 | 0.7522 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.46 | 0.7129 | 0.0477 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.81 | 0.7454 | 0.0351 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 24.21 | 0.7309 | 0.0411 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 24.20 | 0.7312 | 0.0419 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 24.13 | 0.7250 | 0.0386 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 24.42 | 0.7339 | 0.0413 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 24.29 | 0.7326 | 0.0413 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 64.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.26 | 0.7382 | 0.0246 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.06 | 0.3882 | 0.2494 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.65 | 0.3251 | 0.1715 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 19.67 | 0.5144 | 0.1196 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 19.66 | 0.5156 | 0.1191 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 19.66 | 0.5156 | 0.1191 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 19.63 | 0.5192 | 0.1217 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 19.64 | 0.5173 | 0.1208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.13 | 0.7366 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.24 | 0.7386 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 30.19 | 0.7381 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 30.19 | 0.7381 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 30.20 | 0.7380 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 30.21 | 0.7382 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 30.19 | 0.7381 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.87 | 0.7234 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.01 | 0.7364 | 0.0266 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.47 | 0.7311 | 0.0314 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.48 | 0.7311 | 0.0311 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.74 | 0.7354 | 0.0266 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.51 | 0.7324 | 0.0314 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.44 | 0.7316 | 0.0314 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.26 | 0.7136 | 0.0511 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.49 | 0.4400 | 0.3172 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.60 | 0.4178 | 0.2276 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 20.11 | 0.5545 | 0.1658 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 20.12 | 0.5569 | 0.1638 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 20.12 | 0.5569 | 0.1638 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 20.11 | 0.5596 | 0.1666 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 20.11 | 0.5582 | 0.1652 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.67 | 0.7214 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.32 | 0.7348 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.12 | 0.7334 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.12 | 0.7336 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.99 | 0.7279 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.24 | 0.7332 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.16 | 0.7333 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.78 | 0.7056 | 0.0732 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.99 | 0.7300 | 0.0567 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 26.42 | 0.7219 | 0.0640 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 26.42 | 0.7221 | 0.0638 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.44 | 0.7214 | 0.0573 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 26.54 | 0.7236 | 0.0636 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 26.45 | 0.7227 | 0.0638 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 221594 | 0.342 | 67.4 | 28.99 | 0.10 | 0.019 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1388502 | 0.808 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2020731 | 0.808 | 3.4 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2142706 | 0.808 | 3.8 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2142706 | 0.808 | 3.8 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2142706 | 0.808 | 3.8 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2142706 | 0.808 | 3.8 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.701 | 0.041 |
| in035 | mask_ent | 0.661 | 0.041 |
| in035 | mask_grad | 0.446 | 0.041 |
| in035 | r_col | 0.836 | 0.041 |
| in035 | r_warp | 0.875 | 0.041 |
