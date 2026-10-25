# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 20.6% | 25.62 / 0.0221 | 21.80 / 0.0585 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 23.7% | 25.98 / 0.0241 | 22.87 / 0.0537 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | 26.4% | 26.23 / 0.0254 | 21.07 / 0.0577 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 22.4% | 25.85 / 0.0228 | 23.29 / 0.0509 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.76 / 0.0513 | 26.59 / 0.0712 | 19.75 / 0.0167 | 29.67 / 0.0267 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.21 / 0.0800 | 24.15 / 0.1385 | 18.68 / 0.0216 | 28.83 / 0.0328 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.75 / 0.0713 | 24.38 / 0.1214 | 19.88 / 0.0180 | 28.74 / 0.0334 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.67 / 0.0724 | 24.51 / 0.1106 | 19.88 / 0.0177 | 27.24 / 0.0370 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.84 / 0.0723 | 24.67 / 0.1218 | 19.70 / 0.0190 | 28.90 / 0.0324 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.3%） | — | — | 27.76 / 0.0513 | 26.59 / 0.0712 | 29.67 |
| in035 | rife | 11.8% | 20.6% | 26.21 / 0.0800 | 24.15 / 0.1385 | 28.83 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.51 / 0.0569 | — | -1.40 / +0.0297 (core 12.6%) | — | — | — |
| in035 | 2 | 0-3 | 27.39 / 0.0519 | — | -2.22 / +0.0377 (core 12.6%) | — | — | — |
| in035 | 4 | 3-5 | 29.38 / 0.0452 | — | -1.03 / +0.0185 (core 6.3%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.76 / 0.0513 | 26.59 | 29.67 | — |
| in035 | rife | 不复核 | —% | 26.21 / 0.0800 | 24.15 | 28.83 | 0/3 |
| in035 | rife | oracle | 3.6% | 27.12 / 0.0587 | 25.50 | 29.59 | 0/3 |
| in035 | rife | 不复核 | —% | 26.75 / 0.0713 | 24.38 | 28.74 | 0/3 |
| in035 | rife | oracle | 3.8% | 27.67 / 0.0538 | 26.27 | 29.62 | 0/3 |
| in035 | rife | 不复核 | —% | 25.67 / 0.0724 | 24.51 | 27.24 | 0/3 |
| in035 | rife | oracle | 3.8% | 27.65 / 0.0528 | 26.65 | 29.61 | 0/3 |
| in035 | rife | 不复核 | —% | 26.84 / 0.0723 | 24.67 | 28.90 | 0/3 |
| in035 | rife | oracle | 3.7% | 27.62 / 0.0549 | 26.09 | 29.61 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.76 / 0.0513 | 26.59 / 0.0712 | — |
| in035 | FF | 0（前馈） | 969×680（63%） | 26.79 | 26.21 / 0.0800 | 24.15 / 0.1385 | 0/3 |
| in035 | 50 | 1.15 s | 969×680（63%） | 28.81 | 26.84 / 0.0723 | 24.67 / 0.1218 | 0/3 |
| in035 | 100 | 2.25 s | 969×680（63%） | 29.67 | 26.75 / 0.0713 | 24.38 / 0.1214 | 0/3 |
| in035 | 200 | 4.43 s | 969×680（63%） | 30.42 | 25.67 / 0.0724 | 24.51 / 0.1106 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.76 / 0.0513 | 26.59 / 0.0712 | 29.67 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 26.21 / 0.0800 | 24.15 / 0.1385 | 28.83 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.12 / 0.0587 | 25.50 / 0.0873 | 29.59 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.84 / 0.0723 | 24.67 / 0.1218 | 28.90 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.62 / 0.0549 | 26.09 / 0.0763 | 29.61 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.75 / 0.0713 | 24.38 / 0.1214 | 28.74 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.67 / 0.0538 | 26.27 / 0.0736 | 29.62 | 0/3 |
| in035 | rife | GS 测试时优化 200 步 | 直接 | 25.67 / 0.0724 | 24.51 / 0.1106 | 27.24 | 0/3 |
| in035 | rife | GS 测试时优化 200 步 | oracle | 27.65 / 0.0528 | 26.65 / 0.0701 | 29.61 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 / 0.0712 | 19.75 / 0.0167 | 29.67 / 0.0267 | 27.76 / 0.0513 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 6.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.7494 | 0.0712 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 19.00 | 0.7018 | 0.2170 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 21.95 | 0.7271 | 0.1473 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 22.77 | 0.7248 | 0.1291 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.78 | 0.7244 | 0.1716 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.50 | 0.7584 | 0.0873 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.27 | 0.7691 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 26.65 | 0.7710 | 0.0701 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.09 | 0.7679 | 0.0763 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.15 | 0.7374 | 0.1385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.38 | 0.7448 | 0.1214 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.51 | 0.7416 | 0.1106 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.67 | 0.7514 | 0.1218 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.75 | 0.6007 | 0.0167 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.06 | 0.4184 | 0.0711 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.53 | 0.4796 | 0.0631 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 9.71 | 0.4815 | 0.0602 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.33 | 0.4671 | 0.0660 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.70 | 0.5919 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.90 | 0.6423 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 19.90 | 0.6434 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.72 | 0.6347 | 0.0188 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.68 | 0.5895 | 0.0216 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.88 | 0.6397 | 0.0180 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 19.88 | 0.6409 | 0.0177 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.70 | 0.6322 | 0.0190 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 45.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.7718 | 0.0287 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.58 | 0.5208 | 0.2315 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.07 | 0.5438 | 0.2027 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 8.59 | 0.5431 | 0.1916 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.81 | 0.5423 | 0.2128 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.51 | 0.7640 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.46 | 0.7755 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 26.45 | 0.7756 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.36 | 0.7745 | 0.0340 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.17 | 0.7417 | 0.0580 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.74 | 0.7517 | 0.0516 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.82 | 0.7475 | 0.0502 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.01 | 0.7556 | 0.0521 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 53.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.98 | 0.7280 | 0.0352 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.32 | 0.4645 | 0.2831 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.70 | 0.4823 | 0.2575 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 7.08 | 0.4811 | 0.2480 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.51 | 0.4835 | 0.2668 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.42 | 0.7237 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.19 | 0.7321 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.19 | 0.7319 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.13 | 0.7318 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.28 | 0.7088 | 0.0606 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.02 | 0.7177 | 0.0520 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.02 | 0.7123 | 0.0522 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.16 | 0.7212 | 0.0534 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.67 | 0.7076 | 0.0267 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.92 | 0.3627 | 0.2680 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.24 | 0.3690 | 0.2526 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 4.55 | 0.3674 | 0.2475 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.08 | 0.3699 | 0.2588 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.59 | 0.7070 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.62 | 0.7072 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 29.61 | 0.7071 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.61 | 0.7072 | 0.0271 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.83 | 0.7037 | 0.0328 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.74 | 0.7028 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 27.24 | 0.6983 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.90 | 0.7044 | 0.0324 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.76 | 0.7224 | 0.0513 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.03 | 0.4186 | 0.3501 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.37 | 0.4321 | 0.3184 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 5.70 | 0.4307 | 0.3088 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.20 | 0.4323 | 0.3294 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.12 | 0.7186 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.67 | 0.7236 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.65 | 0.7234 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.62 | 0.7233 | 0.0549 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.21 | 0.7094 | 0.0800 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.75 | 0.7146 | 0.0713 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.67 | 0.7099 | 0.0724 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.84 | 0.7167 | 0.0723 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 262988 | 0.321 | 46.2 | 29.00 | 0.17 | 0.014 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 262988 | 0.321 | 33.5 | 29.00 | 0.17 | 0.014 |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 1296 | None | classic | 2.51 | False | 262988 | 0.321 | 35.0 | 29.00 | 0.17 | 0.014 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 262988 | 0.321 | 31.5 | 29.00 | 0.17 | 0.014 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.783 | 0.023 |
| in035 | mask_ent | 0.691 | 0.023 |
| in035 | mask_grad | 0.508 | 0.023 |
| in035 | r_col | 0.824 | 0.023 |
| in035 | r_warp | 0.891 | 0.023 |
