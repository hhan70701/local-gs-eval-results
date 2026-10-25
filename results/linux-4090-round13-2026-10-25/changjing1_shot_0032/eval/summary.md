# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 25.7% | 22.14 / 0.0355 | 20.64 / 0.0789 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 27.5% | 22.27 / 0.0360 | 21.85 / 0.0635 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 26.6% | 22.19 / 0.0362 | 21.64 / 0.0712 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 26.9% | 22.21 / 0.0358 | 21.82 / 0.0669 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_local | 21.4% | 21.83 / 0.0410 | 20.88 / 0.0856 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | 22.9% | 21.96 / 0.0421 | 22.03 / 0.0681 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | 22.1% | 21.89 / 0.0418 | 21.93 / 0.0767 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | 22.5% | 21.92 / 0.0422 | 22.11 / 0.0717 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_local | 17.6% | 22.20 / 0.0428 | 21.50 / 0.0861 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | 18.6% | 22.29 / 0.0444 | 22.97 / 0.0693 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | 18.1% | 22.26 / 0.0445 | 22.74 / 0.0766 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | 18.3% | 22.28 / 0.0439 | 23.01 / 0.0717 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 25.19 / 0.0637 | 22.65 / 0.0960 | 18.16 / 0.0328 | 29.29 / 0.0247 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 24.15 / 0.1028 | 22.43 / 0.1676 | 18.22 / 0.0435 | 28.87 / 0.0292 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.95 / 0.0889 | 23.71 / 0.1285 | 18.85 / 0.0367 | 28.94 / 0.0283 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.80 / 0.0961 | 23.34 / 0.1497 | 18.70 / 0.0398 | 28.92 / 0.0289 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.90 / 0.0923 | 23.60 / 0.1376 | 18.78 / 0.0383 | 28.94 / 0.0287 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 24.46 / 0.0959 | 22.51 / 0.1585 | 18.38 / 0.0418 | 28.97 / 0.0281 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.14 / 0.0840 | 23.55 / 0.1244 | 18.96 / 0.0358 | 29.03 / 0.0273 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.04 / 0.0899 | 23.24 / 0.1436 | 18.82 / 0.0385 | 29.04 / 0.0278 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.13 / 0.0866 | 23.45 / 0.1328 | 18.89 / 0.0373 | 29.05 / 0.0275 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 24.64 / 0.0898 | 22.39 / 0.1547 | 18.45 / 0.0395 | 29.00 / 0.0275 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.26 / 0.0813 | 23.49 / 0.1253 | 19.08 / 0.0342 | 29.03 / 0.0270 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.15 / 0.0856 | 23.14 / 0.1410 | 18.92 / 0.0364 | 29.05 / 0.0272 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.24 / 0.0836 | 23.37 / 0.1318 | 19.02 / 0.0355 | 29.06 / 0.0270 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 13.8%） | — | — | 25.19 / 0.0637 | 22.65 / 0.0960 | 29.29 |
| in035 | rife | 17.7% | 25.7% | 24.15 / 0.1028 | 22.43 / 0.1676 | 28.87 |
| in035 | rife_w30 | 14.5% | 21.4% | 24.46 / 0.0959 | 22.51 / 0.1585 | 28.97 |
| in035 | rife_w40 | 11.8% | 17.6% | 24.64 / 0.0898 | 22.39 / 0.1547 | 29.00 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | rife_w30 | rife_w40 | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 23.96 / 0.0725 | — | -0.54 / +0.0455 (core 15.6%) | -0.25 / +0.0361 (core 12.3%) | +0.01 / +0.0283 (core 10.2%) | — | — | — |
| in035 | 2 | 0-3 | 25.41 / 0.0635 | — | -1.77 / +0.0434 (core 15.6%) | -1.47 / +0.0367 (core 12.3%) | -1.45 / +0.0352 (core 10.2%) | — | — | — |
| in035 | 4 | 3-5 | 26.21 / 0.0551 | — | -0.82 / +0.0284 (core 13.7%) | -0.47 / +0.0237 (core 11.0%) | -0.23 / +0.0147 (core 7.8%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 25.19 / 0.0637 | 22.65 | 29.29 | — |
| in035 | rife | 不复核 | —% | 24.15 / 0.1028 | 22.43 | 28.87 | 0/3 |
| in035 | rife | oracle | 6.9% | 25.03 / 0.0774 | 23.60 | 29.25 | 0/3 |
| in035 | rife | 不复核 | —% | 24.95 / 0.0889 | 23.71 | 28.94 | 0/3 |
| in035 | rife | oracle | 7.2% | 25.53 / 0.0691 | 24.66 | 29.23 | 0/3 |
| in035 | rife | 不复核 | —% | 24.80 / 0.0961 | 23.34 | 28.92 | 0/3 |
| in035 | rife | oracle | 7.1% | 25.42 / 0.0736 | 24.32 | 29.25 | 0/3 |
| in035 | rife | 不复核 | —% | 24.90 / 0.0923 | 23.60 | 28.94 | 0/3 |
| in035 | rife | oracle | 7.2% | 25.49 / 0.0712 | 24.55 | 29.25 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 24.46 / 0.0959 | 22.51 | 28.97 | 0/3 |
| in035 | rife_w30 | oracle | 6.1% | 25.16 / 0.0753 | 23.54 | 29.25 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 25.14 / 0.0840 | 23.55 | 29.03 | 0/3 |
| in035 | rife_w30 | oracle | 6.4% | 25.59 / 0.0682 | 24.39 | 29.23 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 25.04 / 0.0899 | 23.24 | 29.04 | 0/3 |
| in035 | rife_w30 | oracle | 6.3% | 25.51 / 0.0720 | 24.10 | 29.25 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 25.13 / 0.0866 | 23.45 | 29.05 | 0/3 |
| in035 | rife_w30 | oracle | 6.4% | 25.56 / 0.0700 | 24.29 | 29.24 | 0/3 |
| in035 | rife_w40 | 不复核 | —% | 24.64 / 0.0898 | 22.39 | 29.00 | 0/3 |
| in035 | rife_w40 | oracle | 5.0% | 25.24 / 0.0723 | 23.38 | 29.24 | 0/3 |
| in035 | rife_w40 | 不复核 | —% | 25.26 / 0.0813 | 23.49 | 29.03 | 0/3 |
| in035 | rife_w40 | oracle | 5.2% | 25.69 / 0.0666 | 24.34 | 29.22 | 2/3 |
| in035 | rife_w40 | 不复核 | —% | 25.15 / 0.0856 | 23.14 | 29.05 | 0/3 |
| in035 | rife_w40 | oracle | 5.0% | 25.59 / 0.0697 | 24.02 | 29.24 | 1/3 |
| in035 | rife_w40 | 不复核 | —% | 25.24 / 0.0836 | 23.37 | 29.06 | 0/3 |
| in035 | rife_w40 | oracle | 5.1% | 25.66 / 0.0681 | 24.23 | 29.24 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 25.19 / 0.0637 | 22.65 / 0.0960 | — |
| in035 | FF | 0（前馈） | 1198×905（62%） | 26.50 | 24.15 / 0.1028 | 22.43 / 0.1676 | 0/3 |
| in035 | 25 | 1.35 s | 1198×905（62%） | 27.45 | 24.80 / 0.0961 | 23.34 / 0.1497 | 0/3 |
| in035 | 50 | 2.67 s | 1198×905（62%） | 27.85 | 24.90 / 0.0923 | 23.60 / 0.1376 | 0/3 |
| in035 | 100 | 5.34 s | 1198×905（62%） | 28.25 | 24.95 / 0.0889 | 23.71 / 0.1285 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 25.19 / 0.0637 | 22.65 / 0.0960 | 29.29 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 24.15 / 0.1028 | 22.43 / 0.1676 | 28.87 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 25.03 / 0.0774 | 23.60 / 0.1268 | 29.25 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 24.80 / 0.0961 | 23.34 / 0.1497 | 28.92 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 25.42 / 0.0736 | 24.32 / 0.1159 | 29.25 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 24.90 / 0.0923 | 23.60 / 0.1376 | 28.94 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 25.49 / 0.0712 | 24.55 / 0.1078 | 29.25 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 24.95 / 0.0889 | 23.71 / 0.1285 | 28.94 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 25.53 / 0.0691 | 24.66 / 0.0998 | 29.23 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | 直接 | 24.46 / 0.0959 | 22.51 / 0.1585 | 28.97 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | oracle | 25.16 / 0.0753 | 23.54 / 0.1236 | 29.25 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | 直接 | 25.04 / 0.0899 | 23.24 / 0.1436 | 29.04 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | oracle | 25.51 / 0.0720 | 24.10 / 0.1136 | 29.25 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | 直接 | 25.13 / 0.0866 | 23.45 / 0.1328 | 29.05 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | oracle | 25.56 / 0.0700 | 24.29 / 0.1061 | 29.24 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | 直接 | 25.14 / 0.0840 | 23.55 / 0.1244 | 29.03 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | oracle | 25.59 / 0.0682 | 24.39 / 0.0987 | 29.23 | 0/3 |
| in035 | rife_w40 | GS 前馈颜色 | 直接 | 24.64 / 0.0898 | 22.39 / 0.1547 | 29.00 | 0/3 |
| in035 | rife_w40 | GS 前馈颜色 | oracle | 25.24 / 0.0723 | 23.38 / 0.1223 | 29.24 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | 直接 | 25.15 / 0.0856 | 23.14 / 0.1410 | 29.05 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | oracle | 25.59 / 0.0697 | 24.02 / 0.1122 | 29.24 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | 直接 | 25.24 / 0.0836 | 23.37 / 0.1318 | 29.06 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | oracle | 25.66 / 0.0681 | 24.23 / 0.1053 | 29.24 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | 直接 | 25.26 / 0.0813 | 23.49 / 0.1253 | 29.03 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | oracle | 25.69 / 0.0666 | 24.34 / 0.0991 | 29.22 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 / 0.0960 | 18.16 / 0.0328 | 29.29 / 0.0247 | 25.19 / 0.0637 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 18.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 | 0.6880 | 0.0960 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.98 | 0.6447 | 0.2239 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 19.89 | 0.6878 | 0.1689 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 19.86 | 0.6846 | 0.1962 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 19.91 | 0.6901 | 0.1802 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 16.85 | 0.6260 | 0.2408 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 17.49 | 0.6665 | 0.1886 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 17.48 | 0.6640 | 0.2141 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 17.52 | 0.6687 | 0.1993 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 15.11 | 0.6040 | 0.2642 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 15.65 | 0.6422 | 0.2156 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 15.58 | 0.6394 | 0.2393 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 15.60 | 0.6435 | 0.2257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.60 | 0.7110 | 0.1268 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.66 | 0.7393 | 0.0998 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.32 | 0.7300 | 0.1159 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.55 | 0.7360 | 0.1078 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 23.54 | 0.7086 | 0.1236 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 24.39 | 0.7349 | 0.0987 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.10 | 0.7259 | 0.1136 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 24.29 | 0.7315 | 0.1061 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 23.38 | 0.7064 | 0.1223 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 24.34 | 0.7312 | 0.0991 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 24.02 | 0.7218 | 0.1122 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 24.23 | 0.7272 | 0.1053 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.43 | 0.6737 | 0.1676 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.71 | 0.7143 | 0.1285 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.34 | 0.7058 | 0.1497 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.60 | 0.7123 | 0.1376 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 22.51 | 0.6757 | 0.1585 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 23.55 | 0.7125 | 0.1244 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 23.24 | 0.7041 | 0.1436 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 23.45 | 0.7099 | 0.1328 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 22.39 | 0.6733 | 0.1547 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 23.49 | 0.7072 | 0.1253 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 23.14 | 0.6983 | 0.1410 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 23.37 | 0.7040 | 0.1318 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 13.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.16 | 0.4943 | 0.0328 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.47 | 0.3916 | 0.1296 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.69 | 0.4243 | 0.1180 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.62 | 0.4186 | 0.1242 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.66 | 0.4237 | 0.1211 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 8.95 | 0.3742 | 0.1372 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 9.14 | 0.4078 | 0.1258 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 9.10 | 0.4010 | 0.1316 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 9.13 | 0.4065 | 0.1288 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 7.66 | 0.3526 | 0.1512 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 7.75 | 0.3839 | 0.1414 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 7.74 | 0.3771 | 0.1462 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 7.75 | 0.3819 | 0.1439 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.25 | 0.5321 | 0.0431 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.87 | 0.5656 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.72 | 0.5555 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.80 | 0.5621 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 18.39 | 0.5341 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 18.97 | 0.5682 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 18.83 | 0.5569 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 18.91 | 0.5638 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 18.47 | 0.5356 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 19.09 | 0.5694 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 18.93 | 0.5569 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 19.03 | 0.5645 | 0.0350 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.22 | 0.5304 | 0.0435 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.85 | 0.5643 | 0.0367 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.70 | 0.5542 | 0.0398 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.78 | 0.5605 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 18.38 | 0.5325 | 0.0418 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 18.96 | 0.5669 | 0.0358 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 18.82 | 0.5555 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 18.89 | 0.5622 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 18.45 | 0.5342 | 0.0395 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 19.08 | 0.5681 | 0.0342 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 18.92 | 0.5555 | 0.0364 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 19.02 | 0.5629 | 0.0355 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 51.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.24 | 0.7128 | 0.0458 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.62 | 0.5576 | 0.2336 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.94 | 0.5808 | 0.2085 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.77 | 0.5824 | 0.2212 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.84 | 0.5837 | 0.2145 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 8.42 | 0.5282 | 0.2558 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 8.67 | 0.5485 | 0.2334 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 8.57 | 0.5509 | 0.2444 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 8.60 | 0.5519 | 0.2383 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 7.20 | 0.4999 | 0.2777 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 7.39 | 0.5195 | 0.2577 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 7.30 | 0.5206 | 0.2677 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 7.33 | 0.5220 | 0.2622 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.03 | 0.7146 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 23.70 | 0.7282 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 23.55 | 0.7249 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.64 | 0.7274 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 23.22 | 0.7164 | 0.0574 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 23.82 | 0.7294 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 23.69 | 0.7261 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 23.77 | 0.7286 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 23.31 | 0.7183 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 23.93 | 0.7304 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 23.79 | 0.7270 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 23.89 | 0.7294 | 0.0501 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.96 | 0.6882 | 0.0842 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.83 | 0.7076 | 0.0712 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.74 | 0.7071 | 0.0773 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.83 | 0.7091 | 0.0736 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 22.37 | 0.6953 | 0.0771 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 23.11 | 0.7128 | 0.0674 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 23.10 | 0.7125 | 0.0711 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 23.18 | 0.7148 | 0.0682 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 22.61 | 0.6993 | 0.0715 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 23.33 | 0.7144 | 0.0638 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 23.26 | 0.7135 | 0.0664 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 23.35 | 0.7151 | 0.0647 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 47.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.11 | 0.6954 | 0.0435 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.57 | 0.5048 | 0.2744 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.73 | 0.5312 | 0.2533 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.66 | 0.5319 | 0.2646 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.68 | 0.5340 | 0.2592 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 6.78 | 0.4817 | 0.2911 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 6.89 | 0.5051 | 0.2718 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 6.87 | 0.5066 | 0.2816 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 6.88 | 0.5081 | 0.2767 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 6.00 | 0.4539 | 0.3131 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 6.08 | 0.4760 | 0.2968 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 6.06 | 0.4764 | 0.3058 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 6.07 | 0.4780 | 0.3016 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.10 | 0.6994 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.99 | 0.7131 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.78 | 0.7096 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.92 | 0.7123 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 24.33 | 0.7016 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.16 | 0.7147 | 0.0443 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.97 | 0.7112 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.09 | 0.7137 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 24.39 | 0.7023 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.21 | 0.7149 | 0.0441 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.02 | 0.7111 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.15 | 0.7136 | 0.0457 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.81 | 0.6755 | 0.0750 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.11 | 0.6968 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.83 | 0.6944 | 0.0684 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.02 | 0.6973 | 0.0650 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 23.28 | 0.6827 | 0.0692 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 24.45 | 0.7023 | 0.0578 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.24 | 0.6996 | 0.0632 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 24.41 | 0.7025 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 23.50 | 0.6847 | 0.0649 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 24.54 | 0.7019 | 0.0567 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 24.34 | 0.6993 | 0.0606 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 24.49 | 0.7014 | 0.0588 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 56.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6955 | 0.0247 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.44 | 0.3279 | 0.2625 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.64 | 0.3370 | 0.2538 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.53 | 0.3374 | 0.2593 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.58 | 0.3380 | 0.2567 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 3.06 | 0.3063 | 0.2765 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 3.21 | 0.3126 | 0.2700 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 3.15 | 0.3146 | 0.2734 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 3.18 | 0.3143 | 0.2715 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 2.66 | 0.2873 | 0.2906 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 2.69 | 0.2896 | 0.2857 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 2.67 | 0.2925 | 0.2882 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 2.68 | 0.2917 | 0.2869 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.25 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.23 | 0.6949 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.25 | 0.6951 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.25 | 0.6951 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 29.25 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.23 | 0.6948 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.25 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.24 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 29.24 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 29.22 | 0.6948 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.24 | 0.6951 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 29.24 | 0.6950 | 0.0251 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.87 | 0.6912 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.94 | 0.6923 | 0.0283 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.92 | 0.6924 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.94 | 0.6926 | 0.0287 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 28.97 | 0.6921 | 0.0281 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.03 | 0.6931 | 0.0273 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.04 | 0.6932 | 0.0278 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.05 | 0.6934 | 0.0275 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 29.00 | 0.6928 | 0.0275 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 29.03 | 0.6933 | 0.0270 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.05 | 0.6936 | 0.0272 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 29.06 | 0.6937 | 0.0270 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.19 | 0.6979 | 0.0637 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.33 | 0.4243 | 0.3839 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.54 | 0.4407 | 0.3573 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.43 | 0.4414 | 0.3719 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.48 | 0.4425 | 0.3648 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 4.85 | 0.4015 | 0.4035 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 5.00 | 0.4157 | 0.3787 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 4.94 | 0.4174 | 0.3918 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 4.97 | 0.4180 | 0.3849 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 4.30 | 0.3777 | 0.4245 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 4.34 | 0.3894 | 0.4028 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 4.32 | 0.3912 | 0.4141 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 4.33 | 0.3915 | 0.4082 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.03 | 0.6982 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.53 | 0.7049 | 0.0691 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.42 | 0.7033 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.49 | 0.7045 | 0.0712 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 25.16 | 0.6990 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.59 | 0.7054 | 0.0682 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.51 | 0.7038 | 0.0720 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.56 | 0.7050 | 0.0700 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 25.24 | 0.7000 | 0.0723 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.69 | 0.7060 | 0.0666 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.59 | 0.7043 | 0.0697 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.66 | 0.7055 | 0.0681 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.15 | 0.6845 | 0.1028 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.95 | 0.6954 | 0.0889 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.80 | 0.6945 | 0.0961 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.90 | 0.6958 | 0.0923 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 24.46 | 0.6880 | 0.0959 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.14 | 0.6979 | 0.0840 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.04 | 0.6969 | 0.0899 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.13 | 0.6983 | 0.0866 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 24.64 | 0.6899 | 0.0898 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.26 | 0.6983 | 0.0813 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.15 | 0.6974 | 0.0856 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.24 | 0.6983 | 0.0836 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 42.6 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 33.0 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 33.6 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 29.7 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w30448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 33.5 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 30.4 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 34.8 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 31.2 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w40448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 34.8 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 30.1 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 32.6 | 29.50 | 0.35 | 0.012 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 271639 | 0.321 | 28.6 | 29.50 | 0.35 | 0.012 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.650 | 0.061 |
| in035 | mask_ent | 0.652 | 0.061 |
| in035 | mask_grad | 0.451 | 0.061 |
| in035 | r_col | 0.810 | 0.061 |
| in035 | r_warp | 0.807 | 0.061 |
