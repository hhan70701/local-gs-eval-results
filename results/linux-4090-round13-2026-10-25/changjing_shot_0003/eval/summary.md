# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 9.4% | 23.98 / 0.0292 | 22.82 / 0.0671 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 10.6% | 24.37 / 0.0290 | 24.49 / 0.0552 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 10.1% | 24.23 / 0.0291 | 24.39 / 0.0581 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.3% | 24.30 / 0.0298 | 24.69 / 0.0555 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_local | 4.9% | 24.19 / 0.0241 | 22.47 / 0.0584 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | 5.5% | 24.75 / 0.0238 | 23.88 / 0.0495 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | 5.2% | 24.56 / 0.0232 | 23.61 / 0.0515 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | 5.4% | 24.68 / 0.0235 | 23.95 / 0.0500 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_local | 1.7% | 26.22 / 0.0130 | 20.48 / 0.0735 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | 1.9% | 26.39 / 0.0134 | 21.51 / 0.0743 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | 1.9% | 26.35 / 0.0132 | 21.59 / 0.0699 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | 1.9% | 26.39 / 0.0130 | 21.70 / 0.0707 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0823 | 33.66 / 0.0298 | 18.96 / 0.0235 | 29.29 / 0.0447 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.37 / 0.0988 | 31.14 / 0.0654 | 19.46 / 0.0198 | 29.21 / 0.0480 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.80 / 0.0938 | 32.86 / 0.0495 | 20.30 / 0.0178 | 29.27 / 0.0465 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.73 / 0.0958 | 32.69 / 0.0548 | 20.01 / 0.0186 | 29.26 / 0.0474 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.77 / 0.0949 | 32.77 / 0.0514 | 20.17 / 0.0180 | 29.27 / 0.0469 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 27.49 / 0.0924 | 32.73 / 0.0506 | 19.06 / 0.0225 | 29.23 / 0.0463 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.72 / 0.0907 | 33.02 / 0.0493 | 19.54 / 0.0201 | 29.28 / 0.0454 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.67 / 0.0912 | 32.95 / 0.0499 | 19.37 / 0.0211 | 29.28 / 0.0458 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.69 / 0.0909 | 33.01 / 0.0500 | 19.46 / 0.0204 | 29.28 / 0.0455 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 27.63 / 0.0889 | 32.59 / 0.0532 | 19.06 / 0.0235 | 29.24 / 0.0460 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 27.69 / 0.0893 | 32.91 / 0.0540 | 19.15 / 0.0231 | 29.27 / 0.0452 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 27.69 / 0.0889 | 32.77 / 0.0542 | 19.16 / 0.0229 | 29.27 / 0.0455 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 27.69 / 0.0890 | 32.85 / 0.0552 | 19.16 / 0.0229 | 29.28 / 0.0453 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.7%） | — | — | 27.80 / 0.0823 | 33.66 / 0.0298 | 29.29 |
| in035 | rife | 5.4% | 9.4% | 27.37 / 0.0988 | 31.14 / 0.0654 | 29.21 |
| in035 | rife_w30 | 2.3% | 4.9% | 27.49 / 0.0924 | 32.73 / 0.0506 | 29.23 |
| in035 | rife_w40 | 0.7% | 1.7% | 27.63 / 0.0889 | 32.59 / 0.0532 | 29.24 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | rife_w30 | rife_w40 | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.87 / 0.0834 | — | -0.40 / +0.0193 (core 5.3%) | -0.30 / +0.0145 (core 2.9%) | -0.06 / +0.0069 (core 0.9%) | — | — | — |
| in035 | 2 | 0-3 | 28.08 / 0.0845 | — | -0.91 / +0.0210 (core 5.3%) | -0.69 / +0.0158 (core 2.9%) | -0.37 / +0.0106 (core 0.9%) | — | — | — |
| in035 | 4 | 3-5 | 28.46 / 0.0791 | — | +0.01 / +0.0092 (core 3.3%) | +0.03 / +0.0000 (core 0.6%) | -0.08 / +0.0022 (core 0.2%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0823 | 33.66 | 29.29 | — |
| in035 | rife | 不复核 | —% | 27.37 / 0.0988 | 31.14 | 29.21 | 0/3 |
| in035 | rife | oracle | 1.8% | 27.86 / 0.0808 | 32.10 | 29.29 | 2/3 |
| in035 | rife | 不复核 | —% | 27.80 / 0.0938 | 32.86 | 29.27 | 0/3 |
| in035 | rife | oracle | 1.9% | 28.16 / 0.0788 | 33.36 | 29.29 | 3/3 |
| in035 | rife | 不复核 | —% | 27.73 / 0.0958 | 32.69 | 29.26 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.09 / 0.0794 | 33.05 | 29.29 | 3/3 |
| in035 | rife | 不复核 | —% | 27.77 / 0.0949 | 32.77 | 29.27 | 0/3 |
| in035 | rife | oracle | 1.9% | 28.14 / 0.0788 | 33.20 | 29.29 | 3/3 |
| in035 | rife_w30 | 不复核 | —% | 27.49 / 0.0924 | 32.73 | 29.23 | 0/3 |
| in035 | rife_w30 | oracle | 1.1% | 27.81 / 0.0821 | 33.66 | 29.29 | 2/3 |
| in035 | rife_w30 | 不复核 | —% | 27.72 / 0.0907 | 33.02 | 29.28 | 0/3 |
| in035 | rife_w30 | oracle | 1.1% | 27.99 / 0.0802 | 33.66 | 29.29 | 3/3 |
| in035 | rife_w30 | 不复核 | —% | 27.67 / 0.0912 | 32.95 | 29.28 | 0/3 |
| in035 | rife_w30 | oracle | 1.1% | 27.94 / 0.0809 | 33.66 | 29.29 | 3/3 |
| in035 | rife_w30 | 不复核 | —% | 27.69 / 0.0909 | 33.01 | 29.28 | 0/3 |
| in035 | rife_w30 | oracle | 1.1% | 27.97 / 0.0803 | 33.66 | 29.29 | 3/3 |
| in035 | rife_w40 | 不复核 | —% | 27.63 / 0.0889 | 32.59 | 29.24 | 0/3 |
| in035 | rife_w40 | oracle | 0.3% | 27.84 / 0.0821 | 33.66 | 29.29 | 1/3 |
| in035 | rife_w40 | 不复核 | —% | 27.69 / 0.0893 | 32.91 | 29.27 | 0/3 |
| in035 | rife_w40 | oracle | 0.3% | 27.87 / 0.0819 | 33.66 | 29.29 | 2/3 |
| in035 | rife_w40 | 不复核 | —% | 27.69 / 0.0889 | 32.77 | 29.27 | 0/3 |
| in035 | rife_w40 | oracle | 0.3% | 27.88 / 0.0818 | 33.66 | 29.29 | 2/3 |
| in035 | rife_w40 | 不复核 | —% | 27.69 / 0.0890 | 32.85 | 29.28 | 0/3 |
| in035 | rife_w40 | oracle | 0.3% | 27.88 / 0.0817 | 33.66 | 29.29 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.80 / 0.0823 | 33.66 / 0.0298 | — |
| in035 | FF | 0（前馈） | 1271×797（57%） | 27.68 | 27.37 / 0.0988 | 31.14 / 0.0654 | 0/3 |
| in035 | 25 | 1.25 s | 1271×797（57%） | 28.44 | 27.73 / 0.0958 | 32.69 / 0.0548 | 0/3 |
| in035 | 50 | 2.46 s | 1271×797（57%） | 28.67 | 27.77 / 0.0949 | 32.77 / 0.0514 | 0/3 |
| in035 | 100 | 4.89 s | 1271×797（57%） | 28.90 | 27.80 / 0.0938 | 32.86 / 0.0495 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0823 | 33.66 / 0.0298 | 29.29 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 27.37 / 0.0988 | 31.14 / 0.0654 | 29.21 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.86 / 0.0808 | 32.10 / 0.0348 | 29.29 | 2/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.73 / 0.0958 | 32.69 / 0.0548 | 29.26 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.09 / 0.0794 | 33.05 / 0.0330 | 29.29 | 3/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.77 / 0.0949 | 32.77 / 0.0514 | 29.27 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.14 / 0.0788 | 33.20 / 0.0329 | 29.29 | 3/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.80 / 0.0938 | 32.86 / 0.0495 | 29.27 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.16 / 0.0788 | 33.36 / 0.0329 | 29.29 | 3/3 |
| in035 | rife_w30 | GS 前馈颜色 | 直接 | 27.49 / 0.0924 | 32.73 / 0.0506 | 29.23 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | oracle | 27.81 / 0.0821 | 33.66 / 0.0298 | 29.29 | 2/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | 直接 | 27.67 / 0.0912 | 32.95 / 0.0499 | 29.28 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | oracle | 27.94 / 0.0809 | 33.66 / 0.0298 | 29.29 | 3/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | 直接 | 27.69 / 0.0909 | 33.01 / 0.0500 | 29.28 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | oracle | 27.97 / 0.0803 | 33.66 / 0.0298 | 29.29 | 3/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | 直接 | 27.72 / 0.0907 | 33.02 / 0.0493 | 29.28 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | oracle | 27.99 / 0.0802 | 33.66 / 0.0298 | 29.29 | 3/3 |
| in035 | rife_w40 | GS 前馈颜色 | 直接 | 27.63 / 0.0889 | 32.59 / 0.0532 | 29.24 | 0/3 |
| in035 | rife_w40 | GS 前馈颜色 | oracle | 27.84 / 0.0821 | 33.66 / 0.0298 | 29.29 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | 直接 | 27.69 / 0.0889 | 32.77 / 0.0542 | 29.27 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | oracle | 27.88 / 0.0818 | 33.66 / 0.0298 | 29.29 | 2/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | 直接 | 27.69 / 0.0890 | 32.85 / 0.0552 | 29.28 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | oracle | 27.88 / 0.0817 | 33.66 / 0.0298 | 29.29 | 2/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | 直接 | 27.69 / 0.0893 | 32.91 / 0.0540 | 29.27 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | oracle | 27.87 / 0.0819 | 33.66 / 0.0298 | 29.29 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.66 / 0.0298 | 18.96 / 0.0235 | 29.29 / 0.0447 | 27.80 / 0.0823 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.66 | 0.9063 | 0.0298 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.04 | 0.6788 | 0.4098 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.63 | 0.7031 | 0.3711 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.42 | 0.7038 | 0.3869 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.51 | 0.7057 | 0.3771 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 7.30 | 0.5701 | 0.5403 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 7.48 | 0.5760 | 0.5284 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 7.46 | 0.5777 | 0.5349 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 7.45 | 0.5776 | 0.5311 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 6.59 | 0.5573 | 0.5799 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 6.76 | 0.5604 | 0.5679 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 6.70 | 0.5641 | 0.5744 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 6.71 | 0.5633 | 0.5704 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 32.10 | 0.8986 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 33.36 | 0.9050 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 33.05 | 0.9037 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 33.20 | 0.9043 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 33.66 | 0.9063 | 0.0298 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.14 | 0.8889 | 0.0654 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 32.86 | 0.9054 | 0.0495 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 32.69 | 0.9042 | 0.0548 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 32.77 | 0.9059 | 0.0514 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 32.73 | 0.8986 | 0.0506 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 33.02 | 0.9014 | 0.0493 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 32.95 | 0.9019 | 0.0499 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 33.01 | 0.9018 | 0.0500 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 32.59 | 0.8965 | 0.0532 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 32.91 | 0.8987 | 0.0540 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 32.77 | 0.8988 | 0.0542 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 32.85 | 0.8987 | 0.0552 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.96 | 0.5870 | 0.0235 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.53 | 0.4046 | 0.1140 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.98 | 0.4521 | 0.1058 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.76 | 0.4397 | 0.1094 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.85 | 0.4484 | 0.1074 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 5.18 | 0.2998 | 0.1453 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 5.28 | 0.3229 | 0.1405 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 5.26 | 0.3208 | 0.1422 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 5.28 | 0.3239 | 0.1411 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 3.17 | 0.1731 | 0.1785 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 3.16 | 0.1658 | 0.1773 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 3.17 | 0.1753 | 0.1773 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 3.16 | 0.1714 | 0.1772 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.48 | 0.6389 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.32 | 0.6649 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.04 | 0.6582 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.21 | 0.6637 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 19.08 | 0.6155 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 19.55 | 0.6262 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 19.39 | 0.6250 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 19.49 | 0.6268 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 19.05 | 0.6014 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 19.15 | 0.6014 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 19.15 | 0.6023 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 19.15 | 0.6017 | 0.0228 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.46 | 0.6377 | 0.0198 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.30 | 0.6639 | 0.0178 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.01 | 0.6568 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.17 | 0.6624 | 0.0180 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 19.06 | 0.6147 | 0.0225 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 19.54 | 0.6252 | 0.0201 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 19.37 | 0.6237 | 0.0211 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 19.46 | 0.6255 | 0.0204 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 19.06 | 0.6008 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 19.15 | 0.6015 | 0.0231 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 19.16 | 0.6020 | 0.0229 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 19.16 | 0.6017 | 0.0229 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 39.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.37 | 0.6930 | 0.0409 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.07 | 0.4819 | 0.3037 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.26 | 0.5006 | 0.2859 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.15 | 0.5046 | 0.2953 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.19 | 0.5050 | 0.2905 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 3.83 | 0.3796 | 0.3494 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 3.88 | 0.3868 | 0.3381 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 3.86 | 0.3914 | 0.3439 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 3.87 | 0.3909 | 0.3407 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 2.64 | 0.2957 | 0.3867 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 2.66 | 0.2956 | 0.3813 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 2.65 | 0.3000 | 0.3843 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 2.65 | 0.2987 | 0.3826 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.60 | 0.6988 | 0.0434 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.22 | 0.7046 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.07 | 0.7036 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.18 | 0.7047 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 26.34 | 0.6946 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 26.69 | 0.6974 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 26.59 | 0.6971 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.65 | 0.6976 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 26.38 | 0.6935 | 0.0423 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.44 | 0.6940 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.44 | 0.6940 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.45 | 0.6940 | 0.0421 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.52 | 0.6835 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.15 | 0.6933 | 0.0570 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.20 | 0.6949 | 0.0584 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.27 | 0.6956 | 0.0573 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 25.64 | 0.6817 | 0.0557 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.98 | 0.6859 | 0.0536 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.95 | 0.6866 | 0.0541 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.01 | 0.6872 | 0.0535 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 25.86 | 0.6825 | 0.0514 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.94 | 0.6831 | 0.0517 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.99 | 0.6842 | 0.0512 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.99 | 0.6839 | 0.0512 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 43.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.64 | 0.6523 | 0.0479 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.10 | 0.3742 | 0.4451 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.21 | 0.3922 | 0.4308 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.15 | 0.3953 | 0.4369 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.17 | 0.3956 | 0.4335 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 2.74 | 0.2863 | 0.4871 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 2.77 | 0.2947 | 0.4806 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 2.77 | 0.2978 | 0.4834 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 2.77 | 0.2974 | 0.4818 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 1.90 | 0.2195 | 0.5257 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 1.91 | 0.2199 | 0.5235 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 1.91 | 0.2238 | 0.5244 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 1.91 | 0.2225 | 0.5238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.75 | 0.6558 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.29 | 0.6601 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.16 | 0.6598 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.25 | 0.6604 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 26.64 | 0.6546 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 26.96 | 0.6567 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 26.87 | 0.6568 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.92 | 0.6569 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 26.70 | 0.6543 | 0.0478 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.75 | 0.6543 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.76 | 0.6545 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.76 | 0.6544 | 0.0473 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.00 | 0.6477 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.70 | 0.6554 | 0.0553 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.58 | 0.6564 | 0.0568 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.66 | 0.6568 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 26.16 | 0.6472 | 0.0565 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 26.54 | 0.6503 | 0.0543 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 26.45 | 0.6511 | 0.0549 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.49 | 0.6511 | 0.0545 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 26.36 | 0.6481 | 0.0544 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.45 | 0.6480 | 0.0545 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.46 | 0.6488 | 0.0542 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.45 | 0.6485 | 0.0542 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 63.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6481 | 0.0447 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.28 | 0.2641 | 0.4388 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.32 | 0.2686 | 0.4290 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.30 | 0.2709 | 0.4342 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.31 | 0.2705 | 0.4316 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 1.73 | 0.2226 | 0.4705 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 1.73 | 0.2247 | 0.4660 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 1.73 | 0.2260 | 0.4682 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 1.74 | 0.2258 | 0.4669 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 1.48 | 0.1998 | 0.4990 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 1.48 | 0.2006 | 0.4973 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 1.48 | 0.2013 | 0.4979 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 1.48 | 0.2012 | 0.4976 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.21 | 0.6469 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.27 | 0.6480 | 0.0465 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.26 | 0.6479 | 0.0474 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.27 | 0.6480 | 0.0469 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 29.23 | 0.6475 | 0.0463 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.28 | 0.6480 | 0.0454 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.28 | 0.6480 | 0.0458 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.28 | 0.6481 | 0.0455 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 29.24 | 0.6475 | 0.0460 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 29.27 | 0.6477 | 0.0452 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.27 | 0.6478 | 0.0455 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 29.28 | 0.6478 | 0.0453 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.6599 | 0.0823 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.15 | 0.3293 | 0.5602 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.21 | 0.3384 | 0.5376 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.18 | 0.3412 | 0.5488 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.19 | 0.3410 | 0.5427 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 2.34 | 0.2722 | 0.5978 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 2.35 | 0.2767 | 0.5862 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 2.35 | 0.2790 | 0.5924 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 2.35 | 0.2786 | 0.5888 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 1.83 | 0.2284 | 0.6368 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 1.83 | 0.2288 | 0.6320 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 1.83 | 0.2310 | 0.6346 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 1.83 | 0.2304 | 0.6331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.86 | 0.6614 | 0.0808 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.16 | 0.6634 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.09 | 0.6632 | 0.0794 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.14 | 0.6635 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 27.81 | 0.6609 | 0.0821 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.99 | 0.6619 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.94 | 0.6620 | 0.0809 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.97 | 0.6620 | 0.0803 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 27.84 | 0.6609 | 0.0821 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 27.87 | 0.6609 | 0.0819 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 27.88 | 0.6610 | 0.0818 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 27.88 | 0.6609 | 0.0817 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.37 | 0.6570 | 0.0988 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.80 | 0.6609 | 0.0938 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.73 | 0.6613 | 0.0958 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.77 | 0.6615 | 0.0949 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 27.49 | 0.6574 | 0.0924 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.72 | 0.6590 | 0.0907 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.67 | 0.6593 | 0.0912 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.69 | 0.6593 | 0.0909 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 27.63 | 0.6580 | 0.0889 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 27.69 | 0.6580 | 0.0893 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 27.69 | 0.6583 | 0.0889 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 27.69 | 0.6582 | 0.0890 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 41.4 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 39.4 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 40.9 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 34.5 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w30448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 34.3 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 43.5 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 39.6 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 43.5 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w40448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 42.4 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 38.2 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 44.3 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 31.6 | 31.17 | 0.22 | 0.020 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.772 | 0.018 |
| in035 | mask_ent | 0.753 | 0.018 |
| in035 | mask_grad | 0.485 | 0.018 |
| in035 | r_col | 0.698 | 0.018 |
| in035 | r_warp | 0.870 | 0.018 |
