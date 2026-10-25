# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 41.8% | 23.68 / 0.0786 | 23.45 / 0.1623 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 42.9% | 23.69 / 0.0797 | 23.65 / 0.1289 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 42.3% | 23.70 / 0.0789 | 23.88 / 0.1451 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 42.5% | 23.69 / 0.0791 | 23.81 / 0.1314 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_local | 13.3% | 22.11 / 0.0378 | 21.38 / 0.0761 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | 13.9% | 22.16 / 0.0386 | 21.67 / 0.0699 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | 13.6% | 22.19 / 0.0381 | 21.88 / 0.0733 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | 13.7% | 22.19 / 0.0384 | 21.81 / 0.0710 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_local | 5.8% | 21.95 / 0.0216 | 20.61 / 0.0432 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | 6.3% | 22.03 / 0.0214 | 20.72 / 0.0418 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | 6.1% | 21.99 / 0.0211 | 21.03 / 0.0416 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | 6.2% | 21.99 / 0.0215 | 21.01 / 0.0404 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 25.66 / 0.1132 | 26.75 / 0.1238 | 17.16 / 0.0514 | 30.07 / 0.0245 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.51 / 0.1849 | 26.85 / 0.2122 | 18.16 / 0.0580 | 30.09 / 0.0284 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.63 / 0.1570 | 27.05 / 0.1710 | 18.31 / 0.0542 | 30.18 / 0.0276 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.73 / 0.1710 | 27.15 / 0.1901 | 18.31 / 0.0554 | 30.24 / 0.0276 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.70 / 0.1607 | 27.12 / 0.1739 | 18.33 / 0.0548 | 30.21 / 0.0277 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 25.35 / 0.1457 | 26.77 / 0.1434 | 17.63 / 0.0592 | 29.89 / 0.0256 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.46 / 0.1388 | 26.76 / 0.1391 | 17.68 / 0.0578 | 29.98 / 0.0254 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.49 / 0.1430 | 26.83 / 0.1416 | 17.68 / 0.0588 | 29.94 / 0.0254 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.47 / 0.1405 | 26.79 / 0.1400 | 17.67 / 0.0584 | 29.97 / 0.0254 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 25.42 / 0.1311 | 26.62 / 0.1284 | 17.35 / 0.0569 | 30.03 / 0.0251 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.46 / 0.1285 | 26.60 / 0.1273 | 17.35 / 0.0562 | 30.04 / 0.0249 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.48 / 0.1310 | 26.61 / 0.1282 | 17.36 / 0.0568 | 30.06 / 0.0249 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.48 / 0.1295 | 26.60 / 0.1278 | 17.36 / 0.0566 | 30.05 / 0.0248 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 10.6%） | — | — | 25.66 / 0.1132 | 26.75 / 0.1238 | 30.07 |
| in035 | rife | 35.3% | 41.8% | 25.51 / 0.1849 | 26.85 / 0.2122 | 30.09 |
| in035 | rife_w30 | 9.5% | 13.3% | 25.35 / 0.1457 | 26.77 / 0.1434 | 29.89 |
| in035 | rife_w40 | 3.9% | 5.8% | 25.42 / 0.1311 | 26.62 / 0.1284 | 30.03 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | rife_w30 | rife_w40 | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.76 / 0.1171 | — | -0.18 / +0.0897 (core 47.9%) | -0.43 / +0.0400 (core 10.4%) | -0.04 / +0.0158 (core 3.8%) | — | — | — |
| in035 | 2 | 0-3 | 25.28 / 0.1154 | — | +0.06 / +0.0984 (core 47.9%) | -0.16 / +0.0384 (core 10.4%) | -0.35 / +0.0226 (core 3.8%) | — | — | — |
| in035 | 4 | 3-5 | 26.94 / 0.1070 | — | -0.33 / +0.0270 (core 6.7%) | -0.33 / +0.0190 (core 4.4%) | -0.32 / +0.0153 (core 2.2%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 25.66 / 0.1132 | 26.75 | 30.07 | — |
| in035 | rife | 不复核 | —% | 25.51 / 0.1849 | 26.85 | 30.09 | 0/3 |
| in035 | rife | oracle | 6.2% | 26.16 / 0.1225 | 27.62 | 30.06 | 0/3 |
| in035 | rife | 不复核 | —% | 25.63 / 0.1570 | 27.05 | 30.18 | 0/3 |
| in035 | rife | oracle | 6.5% | 26.29 / 0.1170 | 27.69 | 30.07 | 0/3 |
| in035 | rife | 不复核 | —% | 25.73 / 0.1710 | 27.15 | 30.24 | 0/3 |
| in035 | rife | oracle | 6.3% | 26.30 / 0.1202 | 27.76 | 30.06 | 0/3 |
| in035 | rife | 不复核 | —% | 25.70 / 0.1607 | 27.12 | 30.21 | 0/3 |
| in035 | rife | oracle | 6.4% | 26.31 / 0.1183 | 27.74 | 30.06 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 25.35 / 0.1457 | 26.77 | 29.89 | 0/3 |
| in035 | rife_w30 | oracle | 3.0% | 25.88 / 0.1217 | 27.24 | 30.06 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 25.46 / 0.1388 | 26.76 | 29.98 | 0/3 |
| in035 | rife_w30 | oracle | 3.2% | 25.94 / 0.1189 | 27.19 | 30.07 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 25.49 / 0.1430 | 26.83 | 29.94 | 0/3 |
| in035 | rife_w30 | oracle | 3.1% | 25.94 / 0.1208 | 27.23 | 30.07 | 0/3 |
| in035 | rife_w30 | 不复核 | —% | 25.47 / 0.1405 | 26.79 | 29.97 | 0/3 |
| in035 | rife_w30 | oracle | 3.1% | 25.94 / 0.1197 | 27.20 | 30.06 | 0/3 |
| in035 | rife_w40 | 不复核 | —% | 25.42 / 0.1311 | 26.62 | 30.03 | 0/3 |
| in035 | rife_w40 | oracle | 1.5% | 25.75 / 0.1191 | 26.72 | 30.07 | 0/3 |
| in035 | rife_w40 | 不复核 | —% | 25.46 / 0.1285 | 26.60 | 30.04 | 0/3 |
| in035 | rife_w40 | oracle | 1.6% | 25.75 / 0.1182 | 26.70 | 30.07 | 1/3 |
| in035 | rife_w40 | 不复核 | —% | 25.48 / 0.1310 | 26.61 | 30.06 | 0/3 |
| in035 | rife_w40 | oracle | 1.5% | 25.75 / 0.1192 | 26.69 | 30.07 | 0/3 |
| in035 | rife_w40 | 不复核 | —% | 25.48 / 0.1295 | 26.60 | 30.05 | 0/3 |
| in035 | rife_w40 | oracle | 1.6% | 25.76 / 0.1184 | 26.70 | 30.07 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 25.66 / 0.1132 | 26.75 / 0.1238 | — |
| in035 | FF | 0（前馈） | 1265×840（61%） | 29.44 | 25.51 / 0.1849 | 26.85 / 0.2122 | 0/3 |
| in035 | 25 | 1.63 s | 1265×840（61%） | 31.18 | 25.73 / 0.1710 | 27.15 / 0.1901 | 0/3 |
| in035 | 50 | 3.24 s | 1265×840（61%） | 31.84 | 25.70 / 0.1607 | 27.12 / 0.1739 | 0/3 |
| in035 | 100 | 6.50 s | 1265×840（61%） | 32.43 | 25.63 / 0.1570 | 27.05 / 0.1710 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 25.66 / 0.1132 | 26.75 / 0.1238 | 30.07 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 25.51 / 0.1849 | 26.85 / 0.2122 | 30.09 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.16 / 0.1225 | 27.62 / 0.1263 | 30.06 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 25.73 / 0.1710 | 27.15 / 0.1901 | 30.24 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 26.30 / 0.1202 | 27.76 / 0.1238 | 30.06 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.70 / 0.1607 | 27.12 / 0.1739 | 30.21 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 26.31 / 0.1183 | 27.74 / 0.1226 | 30.06 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 25.63 / 0.1570 | 27.05 / 0.1710 | 30.18 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 26.29 / 0.1170 | 27.69 / 0.1229 | 30.07 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | 直接 | 25.35 / 0.1457 | 26.77 / 0.1434 | 29.89 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | oracle | 25.88 / 0.1217 | 27.24 / 0.1264 | 30.06 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | 直接 | 25.49 / 0.1430 | 26.83 / 0.1416 | 29.94 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | oracle | 25.94 / 0.1208 | 27.23 / 0.1262 | 30.07 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | 直接 | 25.47 / 0.1405 | 26.79 / 0.1400 | 29.97 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | oracle | 25.94 / 0.1197 | 27.20 / 0.1258 | 30.06 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | 直接 | 25.46 / 0.1388 | 26.76 / 0.1391 | 29.98 | 0/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | oracle | 25.94 / 0.1189 | 27.19 / 0.1253 | 30.07 | 0/3 |
| in035 | rife_w40 | GS 前馈颜色 | 直接 | 25.42 / 0.1311 | 26.62 / 0.1284 | 30.03 | 0/3 |
| in035 | rife_w40 | GS 前馈颜色 | oracle | 25.75 / 0.1191 | 26.72 / 0.1257 | 30.07 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | 直接 | 25.48 / 0.1310 | 26.61 / 0.1282 | 30.06 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | oracle | 25.75 / 0.1192 | 26.69 / 0.1255 | 30.07 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | 直接 | 25.48 / 0.1295 | 26.60 / 0.1278 | 30.05 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | oracle | 25.76 / 0.1184 | 26.70 / 0.1254 | 30.07 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | 直接 | 25.46 / 0.1285 | 26.60 / 0.1273 | 30.04 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | oracle | 25.75 / 0.1182 | 26.70 / 0.1251 | 30.07 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.75 / 0.1238 | 17.16 / 0.0514 | 30.07 / 0.0245 | 25.66 / 0.1132 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 55.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.75 | 0.7927 | 0.1238 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.79 | 0.7270 | 0.4769 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 10.88 | 0.7221 | 0.4284 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 10.82 | 0.7314 | 0.4498 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.84 | 0.7280 | 0.4326 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 6.25 | 0.6067 | 0.6577 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 6.25 | 0.6023 | 0.6514 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 6.25 | 0.6076 | 0.6552 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 6.24 | 0.6055 | 0.6531 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 4.72 | 0.5695 | 0.7215 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 4.72 | 0.5677 | 0.7197 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 4.72 | 0.5695 | 0.7208 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 4.72 | 0.5688 | 0.7199 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.62 | 0.8045 | 0.1263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.69 | 0.8052 | 0.1229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.76 | 0.8064 | 0.1238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.74 | 0.8060 | 0.1226 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 27.24 | 0.7974 | 0.1264 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 27.19 | 0.7966 | 0.1253 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 27.23 | 0.7973 | 0.1262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 27.20 | 0.7969 | 0.1258 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 26.72 | 0.7921 | 0.1257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.70 | 0.7921 | 0.1251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.69 | 0.7920 | 0.1255 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.70 | 0.7921 | 0.1254 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.85 | 0.8189 | 0.2122 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.05 | 0.8156 | 0.1710 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.15 | 0.8228 | 0.1901 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.12 | 0.8204 | 0.1739 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 26.77 | 0.7964 | 0.1434 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 26.76 | 0.7947 | 0.1391 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 26.83 | 0.7967 | 0.1416 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 26.79 | 0.7958 | 0.1400 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 26.62 | 0.7913 | 0.1284 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 26.60 | 0.7912 | 0.1273 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 26.61 | 0.7913 | 0.1282 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 26.60 | 0.7913 | 0.1278 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 10.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.16 | 0.4794 | 0.0514 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.05 | 0.5138 | 0.1169 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.54 | 0.5258 | 0.1062 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.30 | 0.5277 | 0.1112 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.38 | 0.5265 | 0.1090 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 9.07 | 0.4117 | 0.1646 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 9.33 | 0.4206 | 0.1558 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 9.17 | 0.4184 | 0.1610 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 9.22 | 0.4192 | 0.1587 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 5.77 | 0.3212 | 0.2104 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 5.89 | 0.3270 | 0.2040 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 5.83 | 0.3241 | 0.2074 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 5.86 | 0.3256 | 0.2059 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.17 | 0.5919 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.32 | 0.5966 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.32 | 0.6013 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.34 | 0.5999 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 17.63 | 0.5312 | 0.0590 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 17.69 | 0.5287 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 17.68 | 0.5332 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 17.68 | 0.5310 | 0.0582 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 17.36 | 0.5018 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 17.36 | 0.5001 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 17.36 | 0.5024 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 17.37 | 0.5020 | 0.0565 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.16 | 0.5917 | 0.0580 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.31 | 0.5958 | 0.0542 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.31 | 0.6011 | 0.0554 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.33 | 0.5994 | 0.0548 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 17.63 | 0.5310 | 0.0592 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 17.68 | 0.5281 | 0.0578 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 17.68 | 0.5331 | 0.0588 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 17.67 | 0.5308 | 0.0584 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 17.35 | 0.5016 | 0.0569 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 17.35 | 0.4995 | 0.0562 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 17.36 | 0.5024 | 0.0568 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 17.36 | 0.5018 | 0.0566 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 81.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.96 | 0.7294 | 0.0942 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.82 | 0.6462 | 0.3673 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 10.03 | 0.6481 | 0.3297 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.92 | 0.6578 | 0.3493 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.96 | 0.6544 | 0.3370 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 6.31 | 0.5405 | 0.4760 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 6.38 | 0.5418 | 0.4615 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 6.34 | 0.5476 | 0.4710 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 6.36 | 0.5455 | 0.4664 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 4.70 | 0.4857 | 0.5286 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 4.76 | 0.4860 | 0.5199 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 4.73 | 0.4898 | 0.5258 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 4.74 | 0.4885 | 0.5229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.47 | 0.7401 | 0.1041 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.61 | 0.7422 | 0.0987 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.62 | 0.7431 | 0.1019 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.63 | 0.7430 | 0.0998 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 25.18 | 0.7335 | 0.1034 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.24 | 0.7337 | 0.1004 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.25 | 0.7347 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.25 | 0.7343 | 0.1011 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 25.05 | 0.7303 | 0.0998 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.03 | 0.7301 | 0.0985 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.05 | 0.7306 | 0.0994 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.06 | 0.7307 | 0.0985 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.77 | 0.7480 | 0.1638 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.87 | 0.7470 | 0.1385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.00 | 0.7545 | 0.1509 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.97 | 0.7522 | 0.1410 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 24.60 | 0.7302 | 0.1278 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 24.68 | 0.7293 | 0.1220 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.77 | 0.7335 | 0.1248 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 24.73 | 0.7322 | 0.1226 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 24.68 | 0.7266 | 0.1115 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 24.66 | 0.7252 | 0.1103 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 24.75 | 0.7280 | 0.1108 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 24.74 | 0.7274 | 0.1099 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 58.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.25 | 0.7083 | 0.0909 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.57 | 0.6184 | 0.3430 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.79 | 0.6230 | 0.3181 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.70 | 0.6310 | 0.3317 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.73 | 0.6283 | 0.3251 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 6.30 | 0.5225 | 0.4652 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 6.37 | 0.5250 | 0.4520 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 6.34 | 0.5302 | 0.4600 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 6.35 | 0.5285 | 0.4561 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 4.78 | 0.4721 | 0.5228 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 4.82 | 0.4745 | 0.5137 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 4.81 | 0.4773 | 0.5196 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 4.82 | 0.4764 | 0.5168 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.87 | 0.7238 | 0.0954 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.01 | 0.7263 | 0.0906 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.03 | 0.7273 | 0.0932 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.03 | 0.7272 | 0.0918 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 24.53 | 0.7144 | 0.0977 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 24.59 | 0.7149 | 0.0956 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.60 | 0.7159 | 0.0972 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 24.59 | 0.7156 | 0.0963 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 24.35 | 0.7100 | 0.0968 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 24.35 | 0.7104 | 0.0960 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 24.35 | 0.7106 | 0.0969 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 24.36 | 0.7108 | 0.0962 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.26 | 0.7296 | 0.1320 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.32 | 0.7290 | 0.1165 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.43 | 0.7354 | 0.1248 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.39 | 0.7334 | 0.1203 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 23.99 | 0.7112 | 0.1178 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 24.10 | 0.7104 | 0.1121 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.13 | 0.7142 | 0.1157 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 24.11 | 0.7129 | 0.1138 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 23.95 | 0.7059 | 0.1081 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 24.00 | 0.7060 | 0.1059 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 24.03 | 0.7077 | 0.1080 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 24.02 | 0.7073 | 0.1067 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 23.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.07 | 0.6732 | 0.0245 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.21 | 0.4558 | 0.1743 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.33 | 0.4557 | 0.1666 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.24 | 0.4659 | 0.1711 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.27 | 0.4620 | 0.1686 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 3.64 | 0.3680 | 0.2064 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 3.66 | 0.3647 | 0.2034 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 3.66 | 0.3724 | 0.2052 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 3.66 | 0.3694 | 0.2041 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 2.87 | 0.3378 | 0.2280 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 2.87 | 0.3354 | 0.2260 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 2.88 | 0.3400 | 0.2270 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 2.87 | 0.3383 | 0.2265 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.06 | 0.6733 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.07 | 0.6733 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 30.07 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 30.07 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 30.07 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 30.07 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 30.07 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 30.07 | 0.6732 | 0.0245 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.09 | 0.6799 | 0.0284 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.18 | 0.6796 | 0.0276 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.24 | 0.6818 | 0.0276 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.21 | 0.6810 | 0.0277 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 29.89 | 0.6735 | 0.0256 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.98 | 0.6737 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.94 | 0.6739 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.97 | 0.6738 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 30.03 | 0.6734 | 0.0251 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 30.04 | 0.6735 | 0.0249 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 30.06 | 0.6737 | 0.0249 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 30.05 | 0.6736 | 0.0248 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.66 | 0.7284 | 0.1132 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.98 | 0.6318 | 0.4240 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.14 | 0.6326 | 0.3832 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.06 | 0.6416 | 0.4038 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.08 | 0.6385 | 0.3909 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 5.72 | 0.5253 | 0.5371 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 5.75 | 0.5255 | 0.5207 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 5.74 | 0.5306 | 0.5308 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 5.74 | 0.5288 | 0.5258 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 4.36 | 0.4796 | 0.5875 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 4.38 | 0.4800 | 0.5767 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 4.38 | 0.4828 | 0.5841 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 4.38 | 0.4819 | 0.5806 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.16 | 0.7385 | 0.1225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.29 | 0.7401 | 0.1170 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.30 | 0.7408 | 0.1202 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.31 | 0.7407 | 0.1183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 25.88 | 0.7323 | 0.1217 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.94 | 0.7326 | 0.1189 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.94 | 0.7332 | 0.1208 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.94 | 0.7330 | 0.1197 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 25.75 | 0.7295 | 0.1191 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.75 | 0.7298 | 0.1182 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.75 | 0.7299 | 0.1192 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.76 | 0.7300 | 0.1184 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.51 | 0.7476 | 0.1849 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.63 | 0.7462 | 0.1570 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.73 | 0.7523 | 0.1710 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.70 | 0.7503 | 0.1607 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 25.35 | 0.7305 | 0.1457 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 25.46 | 0.7298 | 0.1388 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 25.49 | 0.7325 | 0.1430 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 25.47 | 0.7315 | 0.1405 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 25.42 | 0.7272 | 0.1311 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 25.46 | 0.7273 | 0.1285 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 25.48 | 0.7283 | 0.1310 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 25.48 | 0.7281 | 0.1295 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 40.8 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 34.2 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 36.1 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 36.0 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 33.9 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 37.4 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 38.1 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 34.2 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 34.0 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 35.9 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 40.2 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.325 | 33.6 | 32.55 | 0.25 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.671 | 0.052 |
| in035 | mask_ent | 0.793 | 0.052 |
| in035 | mask_grad | 0.500 | 0.052 |
| in035 | r_col | 0.630 | 0.052 |
| in035 | r_warp | 0.780 | 0.052 |
