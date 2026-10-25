# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_tokr5448_nat_dil_al_local | 38.0% | 19.08 / 0.0543 | 21.95 / 0.0766 | 21.96 / 0.0745 | 0.55 |
| cam3 | gs_tokr5448_nat_dil_alv_local | 38.0% | 19.09 / 0.0544 | 21.87 / 0.0761 | 22.02 / 0.0736 | 0.58 |
| cam3 | gs_tokrife448_nat_dil_al_local | 11.1% | 14.63 / 0.0674 | 19.81 / 0.0499 | 19.70 / 0.0496 | 0.74 |
| cam3 | gs_tokrife448_nat_dil_alv_local | 11.1% | 14.59 / 0.0679 | 19.75 / 0.0503 | 19.57 / 0.0504 | 1.19 |
| cam3 | gs_tokrife_g448_nat_dil_al_local | 16.9% | 13.55 / 0.0907 | 20.36 / 0.0556 | 20.36 / 0.0556 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_alv_local | 16.9% | 13.56 / 0.0910 | 20.09 / 0.0555 | 20.01 / 0.0563 | 0.35 |
| cam3 | gs_tokstrict448_nat_dil_al_local | 7.4% | 14.46 / 0.1303 | 18.69 / 0.0751 | 18.69 / 0.0751 | 0.00 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | 7.4% | 14.46 / 0.1295 | 18.73 / 0.0762 | 18.74 / 0.0776 | 1.50 |
| cam3 | gs_tokstrict_g448_nat_dil_al_local | 14.0% | 12.85 / 0.1299 | 20.29 / 0.0655 | 20.29 / 0.0655 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_local | 13.9% | 12.85 / 0.1296 | 19.95 / 0.0663 | 19.95 / 0.0663 | 0.00 |
| cam5 | gs_tokr5448_nat_dil_al_local | 18.3% | 23.73 / 0.0216 | 20.21 / 0.0526 | 20.97 / 0.0444 | 1.56 |
| cam5 | gs_tokr5448_nat_dil_alv_local | 18.3% | 23.74 / 0.0213 | 19.91 / 0.0525 | 20.79 / 0.0443 | 1.68 |
| cam5 | gs_tokrife448_nat_dil_al_local | 4.6% | 20.90 / 0.0647 | 18.81 / 0.1160 | 18.77 / 0.1129 | 1.50 |
| cam5 | gs_tokrife448_nat_dil_alv_local | 4.6% | 20.91 / 0.0627 | 18.47 / 0.1173 | 18.86 / 0.1107 | 1.06 |
| cam5 | gs_tokrife_g448_nat_dil_al_local | 8.0% | 20.66 / 0.0531 | 20.06 / 0.0904 | 20.07 / 0.0866 | 0.79 |
| cam5 | gs_tokrife_g448_nat_dil_alv_local | 7.9% | 20.67 / 0.0530 | 19.47 / 0.0908 | 20.05 / 0.0788 | 0.88 |
| cam5 | gs_tokstrict448_nat_dil_al_local | 3.3% | 18.62 / 0.0826 | 17.35 / 0.0948 | 17.51 / 0.0874 | 1.25 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | 3.3% | 18.56 / 0.0806 | 16.93 / 0.0967 | 17.29 / 0.0883 | 1.50 |
| cam5 | gs_tokstrict_g448_nat_dil_al_local | 5.9% | 15.32 / 0.1179 | 17.55 / 0.0977 | 17.55 / 0.0977 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_local | 5.9% | 15.35 / 0.1173 | 16.78 / 0.1029 | 16.78 / 0.1029 | 0.00 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_local] | 25.40 / 0.0768 | 16.90 / 0.1837 | 17.83 / 0.0484 | 32.20 / 0.0319 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.28 / 0.0768 | 16.59 / 0.1871 | 17.64 / 0.0483 | 32.20 / 0.0315 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.31 / 0.0536 | 17.26 / 0.1685 | 17.73 / 0.0382 | 33.49 / 0.0236 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.25 / 0.0538 | 17.13 / 0.1689 | 17.64 / 0.0382 | 33.49 / 0.0236 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.09 / 0.0531 | 18.02 / 0.1392 | 15.72 / 0.0385 | 33.50 / 0.0235 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 25.02 / 0.0533 | 17.85 / 0.1410 | 15.61 / 0.0385 | 33.50 / 0.0235 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.22 / 0.0519 | 17.45 / 0.1471 | 15.89 / 0.0377 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.16 / 0.0521 | 17.34 / 0.1484 | 15.80 / 0.0377 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.06 / 0.0519 | 18.01 / 0.1406 | 15.60 / 0.0376 | 33.53 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 24.99 / 0.0520 | 17.84 / 0.1426 | 15.50 / 0.0377 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.46 / 0.0771 | 16.60 / 0.1893 | 17.85 / 0.0487 | 32.30 / 0.0310 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.48 / 0.0769 | 16.60 / 0.1897 | 17.85 / 0.0481 | 32.31 / 0.0305 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.29 / 0.0538 | 17.06 / 0.1700 | 17.75 / 0.0389 | 33.50 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.20 / 0.0543 | 16.96 / 0.1735 | 17.66 / 0.0391 | 33.49 / 0.0236 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.09 / 0.0531 | 18.02 / 0.1392 | 15.72 / 0.0385 | 33.50 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 24.97 / 0.0535 | 17.81 / 0.1434 | 15.56 / 0.0390 | 33.50 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.22 / 0.0519 | 17.45 / 0.1471 | 15.89 / 0.0377 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.15 / 0.0522 | 17.31 / 0.1498 | 15.79 / 0.0378 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.06 / 0.0519 | 18.01 / 0.1406 | 15.60 / 0.0376 | 33.53 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 24.99 / 0.0520 | 17.84 / 0.1426 | 15.50 / 0.0377 | 33.53 / 0.0234 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_local] | 26.05 / 0.0595 | 18.19 / 0.1538 | 16.71 / 0.0313 | 30.25 / 0.0401 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.79 / 0.0598 | 17.67 / 0.1579 | 16.24 / 0.0324 | 30.15 / 0.0402 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.71 / 0.0420 | 20.18 / 0.0910 | 17.93 / 0.0208 | 31.35 / 0.0312 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.51 / 0.0421 | 19.87 / 0.0941 | 17.60 / 0.0214 | 31.36 / 0.0311 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_local] | 27.79 / 0.0410 | 20.45 / 0.0851 | 17.96 / 0.0200 | 31.37 / 0.0308 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 27.61 / 0.0412 | 20.15 / 0.0871 | 17.66 / 0.0207 | 31.38 / 0.0308 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 27.91 / 0.0406 | 20.51 / 0.0787 | 17.94 / 0.0191 | 31.43 / 0.0307 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 27.78 / 0.0408 | 20.24 / 0.0828 | 17.70 / 0.0195 | 31.44 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 28.23 / 0.0397 | 21.07 / 0.0674 | 18.14 / 0.0176 | 31.45 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 28.16 / 0.0398 | 20.88 / 0.0690 | 18.00 / 0.0177 | 31.45 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 26.62 / 0.0579 | 18.02 / 0.1515 | 17.29 / 0.0297 | 30.61 / 0.0364 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 26.44 / 0.0589 | 17.80 / 0.1539 | 16.98 / 0.0302 | 30.56 / 0.0366 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.77 / 0.0421 | 19.99 / 0.0959 | 18.02 / 0.0206 | 31.33 / 0.0312 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.81 / 0.0417 | 19.90 / 0.0943 | 18.07 / 0.0199 | 31.33 / 0.0312 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 27.87 / 0.0411 | 20.33 / 0.0888 | 18.11 / 0.0198 | 31.36 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 27.90 / 0.0408 | 20.17 / 0.0884 | 18.11 / 0.0192 | 31.37 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 28.04 / 0.0404 | 20.31 / 0.0805 | 18.16 / 0.0184 | 31.41 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 27.99 / 0.0404 | 20.12 / 0.0844 | 18.09 / 0.0183 | 31.42 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 28.23 / 0.0397 | 21.07 / 0.0674 | 18.14 / 0.0176 | 31.45 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 28.16 / 0.0398 | 20.88 / 0.0690 | 18.00 / 0.0177 | 31.45 / 0.0306 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.2%） | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 |
| cam3 | r5 | 30.7% | 38.0% | 25.40 / 0.0768 | 16.90 / 0.1837 | 32.20 |
| cam3 | rife | 10.8% | 11.1% | 26.31 / 0.0536 | 17.26 / 0.1685 | 33.49 |
| cam3 | strict | 8.4% | 7.4% | 25.22 / 0.0519 | 17.45 / 0.1471 | 33.53 |
| cam3 | rife_g | 9.7% | 8.5% | 25.09 / 0.0531 | 18.02 / 0.1392 | 33.50 |
| cam3 | strict_g | 8.3% | 7.0% | 25.06 / 0.0519 | 18.01 / 0.1406 | 33.53 |
| cam5 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.2%） | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 |
| cam5 | r5 | 15.7% | 18.3% | 26.05 / 0.0595 | 18.19 / 0.1538 | 30.25 |
| cam5 | rife | 3.8% | 4.6% | 27.71 / 0.0420 | 20.18 / 0.0910 | 31.35 |
| cam5 | strict | 2.4% | 2.4% | 27.91 / 0.0406 | 20.51 / 0.0787 | 31.43 |
| cam5 | rife_g | 3.5% | 4.0% | 27.79 / 0.0410 | 20.45 / 0.0851 | 31.37 |
| cam5 | strict_g | 1.6% | 1.5% | 28.23 / 0.0397 | 21.07 / 0.0674 | 31.45 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| cam3 | 1 | 0-4 | 19.25 / 0.1012 | +4.11 / -0.0066 (core 30.4%) | +4.59 / -0.0265 (core 14.5%) | +4.48 / -0.0283 (core 12.4%) | +4.59 / -0.0265 (core 14.5%) | +4.48 / -0.0283 (core 12.4%) |
| cam3 | 2 | 0-4 | 20.14 / 0.0784 | +3.98 / -0.0013 (core 30.4%) | +4.51 / -0.0216 (core 14.5%) | +4.42 / -0.0246 (core 12.4%) | +4.51 / -0.0216 (core 14.5%) | +4.42 / -0.0246 (core 12.4%) |
| cam3 | 3 | 0-4 | 22.11 / 0.0577 | +4.96 / +0.0062 (core 30.4%) | +5.80 / -0.0103 (core 14.5%) | +5.82 / -0.0132 (core 12.4%) | +5.80 / -0.0103 (core 14.5%) | +5.82 / -0.0132 (core 12.4%) |
| cam3 | 5 | 4-8 | 25.45 / 0.0357 | +1.85 / +0.0321 (core 24.9%) | +2.80 / +0.0011 (core 2.5%) | +0.35 / +0.0000 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam3 | 6 | 4-8 | 24.03 / 0.0518 | +1.93 / +0.0262 (core 24.9%) | +3.37 / -0.0002 (core 2.5%) | +0.20 / +0.0007 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam3 | 7 | 4-8 | 24.65 / 0.0526 | -0.05 / +0.0270 (core 24.9%) | +1.17 / +0.0019 (core 2.5%) | +0.43 / -0.0005 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam5 | 1 | 0-2 | 23.87 / 0.0592 | -0.02 / +0.0204 (core 18.8%) | +0.90 / +0.0016 (core 5.9%) | +0.91 / +0.0004 (core 4.0%) | +0.90 / +0.0016 (core 5.9%) | +0.91 / +0.0004 (core 4.0%) |
| cam5 | 3 | 2-4 | 32.61 / 0.0248 | -4.28 / +0.0193 (core 12.0%) | -1.74 / +0.0041 (core 3.7%) | -0.91 / +0.0033 (core 2.1%) | -1.74 / +0.0041 (core 3.7%) | +0.00 / +0.0000 (core 2.1%*) |
| cam5 | 5 | 4-6 | 28.67 / 0.0315 | -1.16 / +0.0176 (core 11.3%) | -0.30 / +0.0014 (core 0.8%) | -0.36 / +0.0006 (core 0.2%) | +0.00 / +0.0000 (core 0.8%*) | +0.00 / +0.0000 (core 0.2%*) |
| cam5 | 7 | 6-8 | 26.85 / 0.0428 | -2.36 / +0.0222 (core 7.1%) | -0.02 / +0.0024 (core 0.4%) | +0.00 / +0.0000 (core 0.0%) | +0.00 / +0.0000 (core 0.4%*) | +0.00 / +0.0000 (core 0.0%*) |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：aligned_int → `gs_tok448_nat_dil_al`，aligned_vggt → `gs_tok448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=6.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 12.52 / 0.0568 | 32.36 / 0.0269 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |
| flow_s0.5_pose | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 | 22.93 / 0.0610 |
| gs_tok448_nat_dil_al | 18.20 / 0.1512 | 18.29 / 0.0465 | 29.04 / 0.0548 | 24.96 / 0.0949 |
| gs_tok448_nat_dil_al+reg | 18.10 / 0.1567 | 18.62 / 0.0448 | 29.44 / 0.0525 | 25.33 / 0.0944 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 18.99 / 0.1499 | 18.29 / 0.0465 | 33.53 / 0.0235 | 27.00 / 0.0573 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.02 / 0.1774 | 17.19 / 0.0432 | 33.54 / 0.0233 | 25.83 / 0.0587 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.86 / 0.1548 | 18.62 / 0.0448 | 33.54 / 0.0234 | 27.16 / 0.0569 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 16.89 / 0.1831 | 17.29 / 0.0434 | 33.54 / 0.0233 | 25.90 / 0.0592 |
| gs_tok448_nat_dil_alv | 17.70 / 0.1541 | 18.02 / 0.0465 | 29.19 / 0.0542 | 24.87 / 0.0945 |
| gs_tok448_nat_dil_alv+reg | 18.10 / 0.1545 | 18.67 / 0.0440 | 29.57 / 0.0516 | 25.42 / 0.0941 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.46 / 0.1516 | 18.02 / 0.0465 | 33.53 / 0.0235 | 26.84 / 0.0573 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 16.81 / 0.1778 | 17.04 / 0.0431 | 33.54 / 0.0233 | 25.72 / 0.0586 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.80 / 0.1512 | 18.68 / 0.0440 | 33.54 / 0.0234 | 27.18 / 0.0566 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.01 / 0.1776 | 17.32 / 0.0432 | 33.54 / 0.0233 | 25.93 / 0.0592 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_tok448_nat_dil_al | 18.20 | 0.6782 | 0.1512 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.10 | 0.6721 | 0.1567 | 1.00 |
| gs_tok448_nat_dil_alv | 17.70 | 0.6644 | 0.1541 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.10 | 0.6828 | 0.1545 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.63 | 0.6591 | 0.1713 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.18 | 0.6458 | 0.1759 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.62 | 0.6590 | 0.1718 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 17.18 | 0.6457 | 0.1762 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 10.79 | 0.3305 | 0.4152 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 10.52 | 0.3238 | 0.4171 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 14.76 | 0.5941 | 0.2503 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 14.47 | 0.5855 | 0.2520 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 10.77 | 0.3295 | 0.4170 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 10.51 | 0.3227 | 0.4190 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.86 | 0.7033 | 0.1548 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 18.99 | 0.7077 | 0.1499 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.80 | 0.7068 | 0.1512 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.46 | 0.6945 | 0.1516 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 17.04 | 0.6543 | 0.1773 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 17.18 | 0.6610 | 0.1717 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.11 | 0.6651 | 0.1753 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 16.78 | 0.6477 | 0.1747 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 16.89 | 0.6662 | 0.1831 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.02 | 0.6690 | 0.1774 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.01 | 0.6750 | 0.1776 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 16.81 | 0.6632 | 0.1778 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 16.90 | 0.6483 | 0.1837 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 16.59 | 0.6373 | 0.1871 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.26 | 0.6698 | 0.1685 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.13 | 0.6658 | 0.1689 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 18.02 | 0.6802 | 0.1392 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 17.85 | 0.6741 | 0.1410 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 17.45 | 0.6708 | 0.1471 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 17.34 | 0.6688 | 0.1484 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 18.01 | 0.6794 | 0.1406 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 17.84 | 0.6734 | 0.1426 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 16.60 | 0.6291 | 0.1893 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 16.60 | 0.6344 | 0.1897 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 17.06 | 0.6626 | 0.1700 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 16.96 | 0.6583 | 0.1735 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 18.02 | 0.6802 | 0.1392 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 17.81 | 0.6725 | 0.1434 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 17.45 | 0.6708 | 0.1471 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 17.31 | 0.6641 | 0.1498 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 18.01 | 0.6794 | 0.1406 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 17.84 | 0.6734 | 0.1426 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 14.17 | 0.5985 | 0.0457 | 1.00 |
| flow_s0.5_pose | 13.30 | 0.5443 | 0.0482 | 1.00 |
| flow_s0.5_uniform | 13.88 | 0.5654 | 0.0513 | 1.00 |
| flow_s1.0_oracle | 13.03 | 0.5914 | 0.0498 | 1.00 |
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| flow_s1.0_uniform | 12.52 | 0.5342 | 0.0568 | 1.00 |
| gs_tok448_nat_dil_al | 18.29 | 0.7150 | 0.0465 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.62 | 0.7232 | 0.0448 | 1.00 |
| gs_tok448_nat_dil_alv | 18.02 | 0.7090 | 0.0465 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.67 | 0.7265 | 0.0440 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.38 | 0.6908 | 0.0509 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.14 | 0.6863 | 0.0509 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.92 | 0.5594 | 0.1213 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 11.86 | 0.5545 | 0.1214 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 8.39 | 0.3069 | 0.1695 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 8.34 | 0.3039 | 0.1694 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 10.14 | 0.4716 | 0.1508 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 10.11 | 0.4697 | 0.1508 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 7.51 | 0.2779 | 0.1847 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 7.48 | 0.2748 | 0.1848 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.62 | 0.7150 | 0.0448 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 18.29 | 0.7046 | 0.0465 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.68 | 0.7182 | 0.0440 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.02 | 0.6984 | 0.0465 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 17.74 | 0.7091 | 0.0466 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 17.51 | 0.7037 | 0.0474 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.79 | 0.7123 | 0.0460 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 17.30 | 0.6979 | 0.0474 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 17.29 | 0.7017 | 0.0434 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.19 | 0.6982 | 0.0432 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.32 | 0.7046 | 0.0432 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 17.04 | 0.6939 | 0.0431 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 17.83 | 0.6944 | 0.0484 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.64 | 0.6897 | 0.0483 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.73 | 0.6880 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.64 | 0.6864 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 15.72 | 0.6524 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 15.61 | 0.6489 | 0.0385 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 15.89 | 0.6521 | 0.0377 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 15.80 | 0.6508 | 0.0377 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 15.60 | 0.6500 | 0.0376 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 15.50 | 0.6465 | 0.0377 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.85 | 0.6863 | 0.0487 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.85 | 0.6877 | 0.0481 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 17.75 | 0.6858 | 0.0389 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 17.66 | 0.6809 | 0.0391 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 15.72 | 0.6524 | 0.0385 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 15.56 | 0.6464 | 0.0390 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 15.89 | 0.6521 | 0.0377 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 15.79 | 0.6491 | 0.0378 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 15.60 | 0.6500 | 0.0376 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 15.50 | 0.6465 | 0.0377 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8166 | 0.0498 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8102 | 0.0518 | 1.00 |
| flow_s0.5_uniform | 19.42 | 0.7885 | 0.0548 | 1.00 |
| flow_s1.0_oracle | 19.19 | 0.8296 | 0.0544 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| flow_s1.0_uniform | 18.45 | 0.7883 | 0.0601 | 1.00 |
| gs_tok448_nat_dil_al | 22.04 | 0.8016 | 0.0674 | 1.00 |
| gs_tok448_nat_dil_al+reg | 22.22 | 0.8083 | 0.0671 | 1.00 |
| gs_tok448_nat_dil_alv | 21.90 | 0.8018 | 0.0669 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 22.31 | 0.8124 | 0.0667 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 16.30 | 0.7486 | 0.1169 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 16.25 | 0.7492 | 0.1158 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.03 | 0.5770 | 0.2877 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 9.02 | 0.5757 | 0.2878 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.99 | 0.3157 | 0.3466 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.98 | 0.3147 | 0.3468 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.82 | 0.5224 | 0.3281 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.81 | 0.5212 | 0.3282 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 6.38 | 0.2915 | 0.3662 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 6.37 | 0.2901 | 0.3664 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 23.44 | 0.8547 | 0.0511 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 23.33 | 0.8534 | 0.0518 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 23.45 | 0.8550 | 0.0509 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 23.13 | 0.8514 | 0.0517 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 22.21 | 0.8059 | 0.0671 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 22.04 | 0.7993 | 0.0674 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 22.31 | 0.8100 | 0.0667 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 21.90 | 0.7994 | 0.0669 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 22.88 | 0.8498 | 0.0479 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 22.87 | 0.8495 | 0.0474 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 22.94 | 0.8510 | 0.0477 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 22.76 | 0.8487 | 0.0471 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 21.57 | 0.7838 | 0.0779 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 21.47 | 0.7841 | 0.0772 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.70 | 0.8453 | 0.0488 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.64 | 0.8449 | 0.0489 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 21.61 | 0.8484 | 0.0462 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 21.51 | 0.8470 | 0.0464 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 21.74 | 0.8505 | 0.0444 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 21.65 | 0.8497 | 0.0445 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 21.59 | 0.8517 | 0.0442 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 21.48 | 0.8504 | 0.0442 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 21.34 | 0.7797 | 0.0794 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 21.35 | 0.7824 | 0.0784 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.63 | 0.8436 | 0.0488 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.54 | 0.8416 | 0.0491 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 21.61 | 0.8484 | 0.0462 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 21.48 | 0.8458 | 0.0465 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 21.74 | 0.8505 | 0.0444 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 21.63 | 0.8493 | 0.0445 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 21.59 | 0.8517 | 0.0442 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 21.48 | 0.8504 | 0.0442 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.88 | 0.8768 | 0.0597 | 1.00 |
| flow_s0.5_pose | 21.24 | 0.8722 | 0.0608 | 1.00 |
| flow_s0.5_uniform | 21.45 | 0.8596 | 0.0657 | 1.00 |
| flow_s1.0_oracle | 21.12 | 0.8872 | 0.0601 | 1.00 |
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| flow_s1.0_uniform | 20.48 | 0.8603 | 0.0677 | 1.00 |
| gs_tok448_nat_dil_al | 23.81 | 0.8576 | 0.0840 | 1.00 |
| gs_tok448_nat_dil_al+reg | 24.14 | 0.8625 | 0.0816 | 1.00 |
| gs_tok448_nat_dil_alv | 23.68 | 0.8577 | 0.0834 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 24.22 | 0.8651 | 0.0806 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 20.12 | 0.8240 | 0.1216 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 20.04 | 0.8242 | 0.1211 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.16 | 0.6152 | 0.3253 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.16 | 0.6144 | 0.3254 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.04 | 0.3290 | 0.3814 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.04 | 0.3285 | 0.3814 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.45 | 0.5748 | 0.3651 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.45 | 0.5741 | 0.3653 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.70 | 0.3086 | 0.4023 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.69 | 0.3077 | 0.4023 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 25.77 | 0.9042 | 0.0545 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 25.63 | 0.9034 | 0.0552 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 25.80 | 0.9045 | 0.0541 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 25.45 | 0.9023 | 0.0551 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 23.98 | 0.8751 | 0.0718 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 23.77 | 0.8709 | 0.0729 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 24.05 | 0.8768 | 0.0713 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 23.63 | 0.8705 | 0.0728 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 24.46 | 0.8978 | 0.0571 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 24.39 | 0.8972 | 0.0569 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 24.49 | 0.8981 | 0.0571 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 24.26 | 0.8962 | 0.0569 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 24.18 | 0.8669 | 0.0736 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 24.03 | 0.8664 | 0.0735 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.99 | 0.8993 | 0.0525 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 24.90 | 0.8987 | 0.0526 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 23.58 | 0.8980 | 0.0519 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 23.48 | 0.8971 | 0.0520 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 23.69 | 0.8988 | 0.0507 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 23.60 | 0.8982 | 0.0508 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 23.52 | 0.8994 | 0.0507 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 23.42 | 0.8984 | 0.0507 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 24.23 | 0.8661 | 0.0729 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 24.23 | 0.8673 | 0.0723 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 24.97 | 0.8985 | 0.0526 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 24.87 | 0.8971 | 0.0529 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 23.58 | 0.8980 | 0.0519 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 23.45 | 0.8967 | 0.0522 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 23.69 | 0.8988 | 0.0507 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 23.59 | 0.8979 | 0.0509 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 23.52 | 0.8994 | 0.0507 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 23.42 | 0.8984 | 0.0507 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.45 | 0.9592 | 0.0262 | 1.00 |
| flow_s0.5_pose | 32.82 | 0.9610 | 0.0252 | 1.00 |
| flow_s0.5_uniform | 32.06 | 0.9533 | 0.0285 | 1.00 |
| flow_s1.0_oracle | 33.41 | 0.9610 | 0.0236 | 1.00 |
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| flow_s1.0_uniform | 32.36 | 0.9509 | 0.0269 | 1.00 |
| gs_tok448_nat_dil_al | 29.04 | 0.9265 | 0.0548 | 1.00 |
| gs_tok448_nat_dil_al+reg | 29.44 | 0.9290 | 0.0525 | 1.00 |
| gs_tok448_nat_dil_alv | 29.19 | 0.9285 | 0.0542 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 29.57 | 0.9314 | 0.0516 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.25 | 0.8733 | 0.1119 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.25 | 0.8751 | 0.1112 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.51 | 0.6123 | 0.3600 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.51 | 0.6123 | 0.3601 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.28 | 0.3291 | 0.3955 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.28 | 0.3292 | 0.3956 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.16 | 0.5992 | 0.3929 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.16 | 0.5991 | 0.3930 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.08 | 0.3209 | 0.4149 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.08 | 0.3208 | 0.4150 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 33.53 | 0.9612 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 33.54 | 0.9614 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 33.53 | 0.9611 | 0.0235 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 33.48 | 0.9583 | 0.0239 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 33.45 | 0.9580 | 0.0243 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 33.48 | 0.9585 | 0.0238 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 33.46 | 0.9582 | 0.0242 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 32.20 | 0.9540 | 0.0319 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 32.20 | 0.9542 | 0.0315 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 33.49 | 0.9615 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 33.49 | 0.9614 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 32.30 | 0.9545 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 32.31 | 0.9548 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 33.49 | 0.9614 | 0.0236 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_tok448_nat_dil_al | 24.96 | 0.8820 | 0.0949 | 1.00 |
| gs_tok448_nat_dil_al+reg | 25.33 | 0.8870 | 0.0944 | 1.00 |
| gs_tok448_nat_dil_alv | 24.87 | 0.8830 | 0.0945 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 25.42 | 0.8899 | 0.0941 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 19.06 | 0.8417 | 0.1544 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 19.03 | 0.8427 | 0.1539 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.46 | 0.6083 | 0.4183 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.46 | 0.6076 | 0.4186 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.84 | 0.3288 | 0.4889 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.84 | 0.3285 | 0.4890 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.89 | 0.5786 | 0.4695 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.89 | 0.5780 | 0.4696 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.53 | 0.3138 | 0.5126 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.52 | 0.3131 | 0.5127 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 27.16 | 0.9259 | 0.0569 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 27.00 | 0.9250 | 0.0573 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 27.18 | 0.9261 | 0.0566 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 26.84 | 0.9242 | 0.0573 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 25.39 | 0.9044 | 0.0760 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 25.16 | 0.9010 | 0.0761 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 25.46 | 0.9059 | 0.0759 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 25.03 | 0.9009 | 0.0759 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 25.90 | 0.9217 | 0.0592 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 25.83 | 0.9211 | 0.0587 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 25.93 | 0.9219 | 0.0592 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 25.72 | 0.9205 | 0.0586 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 25.40 | 0.8986 | 0.0768 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.28 | 0.8985 | 0.0768 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.31 | 0.9228 | 0.0536 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.25 | 0.9224 | 0.0538 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.09 | 0.9223 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 25.02 | 0.9217 | 0.0533 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.22 | 0.9229 | 0.0519 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.16 | 0.9226 | 0.0521 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.06 | 0.9232 | 0.0519 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 24.99 | 0.9227 | 0.0520 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.46 | 0.8988 | 0.0771 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.48 | 0.8998 | 0.0769 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.29 | 0.9223 | 0.0538 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.20 | 0.9213 | 0.0543 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.09 | 0.9223 | 0.0531 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 24.97 | 0.9213 | 0.0535 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.22 | 0.9229 | 0.0519 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.15 | 0.9224 | 0.0522 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.06 | 0.9232 | 0.0519 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 24.99 | 0.9227 | 0.0520 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：aligned_int → `gs_tok448_nat_dil_al`，aligned_vggt → `gs_tok448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=3.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 15.31 / 0.0249 | 30.29 / 0.0331 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |
| flow_s0.5_pose | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 | 27.45 / 0.0415 |
| gs_tok448_nat_dil_al | 18.31 / 0.1396 | 16.30 / 0.0338 | 27.16 / 0.0718 | 24.77 / 0.0882 |
| gs_tok448_nat_dil_al+reg | 18.82 / 0.1337 | 17.86 / 0.0277 | 28.17 / 0.0652 | 26.06 / 0.0849 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.82 / 0.1189 | 16.30 / 0.0338 | 31.44 / 0.0309 | 27.61 / 0.0478 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 20.54 / 0.0917 | 17.89 / 0.0226 | 31.45 / 0.0305 | 27.76 / 0.0434 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 20.41 / 0.1137 | 17.86 / 0.0277 | 31.46 / 0.0305 | 28.33 / 0.0456 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 20.70 / 0.0901 | 18.56 / 0.0218 | 31.45 / 0.0305 | 28.03 / 0.0428 |
| gs_tok448_nat_dil_alv | 17.72 / 0.1448 | 15.77 / 0.0354 | 27.11 / 0.0723 | 24.55 / 0.0887 |
| gs_tok448_nat_dil_alv+reg | 18.59 / 0.1361 | 17.70 / 0.0280 | 28.20 / 0.0652 | 26.01 / 0.0853 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 19.19 / 0.1218 | 15.77 / 0.0354 | 31.43 / 0.0310 | 27.25 / 0.0486 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 20.06 / 0.0979 | 17.47 / 0.0234 | 31.46 / 0.0305 | 27.50 / 0.0438 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 20.13 / 0.1154 | 17.70 / 0.0280 | 31.46 / 0.0305 | 28.25 / 0.0458 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 20.53 / 0.0921 | 18.47 / 0.0218 | 31.46 / 0.0305 | 27.98 / 0.0429 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_tok448_nat_dil_al | 18.31 | 0.6765 | 0.1396 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.82 | 0.7107 | 0.1337 | 1.00 |
| gs_tok448_nat_dil_alv | 17.72 | 0.6598 | 0.1448 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.59 | 0.7078 | 0.1361 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.81 | 0.6543 | 0.1673 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.26 | 0.6379 | 0.1724 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.67 | 0.5850 | 0.2741 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 14.17 | 0.5664 | 0.2791 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 11.49 | 0.3612 | 0.3977 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 11.01 | 0.3474 | 0.4015 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 13.10 | 0.4840 | 0.3288 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 12.67 | 0.4652 | 0.3357 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 7.31 | 0.1799 | 0.5322 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 7.06 | 0.1701 | 0.5334 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 20.41 | 0.7607 | 0.1137 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.82 | 0.7416 | 0.1189 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 20.13 | 0.7544 | 0.1154 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 19.19 | 0.7226 | 0.1218 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 19.21 | 0.7302 | 0.1241 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 18.76 | 0.7055 | 0.1312 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 18.98 | 0.7271 | 0.1255 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 18.17 | 0.6876 | 0.1359 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 20.70 | 0.7761 | 0.0901 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 20.54 | 0.7688 | 0.0917 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 20.53 | 0.7744 | 0.0921 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 20.06 | 0.7543 | 0.0979 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 18.19 | 0.6794 | 0.1538 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.67 | 0.6615 | 0.1579 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.18 | 0.7531 | 0.0910 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 19.87 | 0.7422 | 0.0941 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 20.45 | 0.7558 | 0.0851 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 20.15 | 0.7472 | 0.0871 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 20.51 | 0.7614 | 0.0787 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 20.24 | 0.7534 | 0.0828 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 21.07 | 0.7748 | 0.0674 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 20.88 | 0.7682 | 0.0690 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 18.02 | 0.6816 | 0.1515 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.80 | 0.6766 | 0.1539 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 19.99 | 0.7449 | 0.0959 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 19.90 | 0.7429 | 0.0943 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 20.33 | 0.7525 | 0.0888 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 20.17 | 0.7473 | 0.0884 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 20.31 | 0.7537 | 0.0805 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 20.12 | 0.7466 | 0.0844 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 21.07 | 0.7748 | 0.0674 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 20.88 | 0.7682 | 0.0690 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.18 | 0.7600 | 0.0171 | 1.00 |
| flow_s0.5_pose | 17.06 | 0.6711 | 0.0195 | 1.00 |
| flow_s0.5_uniform | 15.30 | 0.5755 | 0.0247 | 1.00 |
| flow_s1.0_oracle | 19.73 | 0.7659 | 0.0154 | 1.00 |
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| flow_s1.0_uniform | 15.31 | 0.5619 | 0.0249 | 1.00 |
| gs_tok448_nat_dil_al | 16.30 | 0.6255 | 0.0338 | 1.00 |
| gs_tok448_nat_dil_al+reg | 17.86 | 0.6896 | 0.0277 | 1.00 |
| gs_tok448_nat_dil_alv | 15.77 | 0.6001 | 0.0354 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 17.70 | 0.6860 | 0.0280 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 15.70 | 0.6031 | 0.0403 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 15.28 | 0.5777 | 0.0416 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.39 | 0.3994 | 0.0959 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 10.24 | 0.3777 | 0.0966 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 8.06 | 0.2627 | 0.1302 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 7.92 | 0.2453 | 0.1310 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 9.06 | 0.3215 | 0.1181 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 8.94 | 0.3000 | 0.1187 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.39 | 0.1207 | 0.1549 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.34 | 0.1120 | 0.1550 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 17.86 | 0.6876 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 16.30 | 0.6209 | 0.0338 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 17.70 | 0.6836 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 15.77 | 0.5946 | 0.0354 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 18.06 | 0.6999 | 0.0266 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 16.85 | 0.6543 | 0.0301 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.92 | 0.6969 | 0.0268 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 16.35 | 0.6317 | 0.0311 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 18.56 | 0.7190 | 0.0218 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.89 | 0.6959 | 0.0226 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 18.47 | 0.7174 | 0.0218 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 17.47 | 0.6779 | 0.0234 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 16.71 | 0.6416 | 0.0313 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 16.24 | 0.6183 | 0.0324 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.93 | 0.6952 | 0.0208 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.60 | 0.6788 | 0.0214 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 17.96 | 0.6917 | 0.0200 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 17.66 | 0.6777 | 0.0207 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 17.94 | 0.6925 | 0.0191 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 17.70 | 0.6810 | 0.0195 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 18.14 | 0.6987 | 0.0176 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 18.00 | 0.6922 | 0.0177 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.29 | 0.6645 | 0.0297 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 16.98 | 0.6513 | 0.0302 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 18.02 | 0.7012 | 0.0206 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 18.07 | 0.7018 | 0.0199 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 18.11 | 0.6993 | 0.0198 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 18.11 | 0.6989 | 0.0192 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 18.16 | 0.7008 | 0.0184 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 18.09 | 0.6963 | 0.0183 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 18.14 | 0.6987 | 0.0176 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 18.00 | 0.6922 | 0.0177 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.73 | 0.8826 | 0.0204 | 1.00 |
| flow_s0.5_pose | 22.21 | 0.8504 | 0.0224 | 1.00 |
| flow_s0.5_uniform | 20.55 | 0.8064 | 0.0266 | 1.00 |
| flow_s1.0_oracle | 24.76 | 0.8987 | 0.0188 | 1.00 |
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| flow_s1.0_uniform | 20.86 | 0.8093 | 0.0253 | 1.00 |
| gs_tok448_nat_dil_al | 20.23 | 0.7497 | 0.0462 | 1.00 |
| gs_tok448_nat_dil_al+reg | 21.54 | 0.7946 | 0.0400 | 1.00 |
| gs_tok448_nat_dil_alv | 19.91 | 0.7419 | 0.0467 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 21.44 | 0.7932 | 0.0401 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.55 | 0.7125 | 0.0646 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.35 | 0.7051 | 0.0649 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.04 | 0.4795 | 0.2190 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.02 | 0.4726 | 0.2193 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.78 | 0.2820 | 0.2459 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.76 | 0.2765 | 0.2463 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.45 | 0.3842 | 0.2363 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.42 | 0.3776 | 0.2366 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.44 | 0.1369 | 0.2724 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.43 | 0.1334 | 0.2726 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 23.65 | 0.8664 | 0.0255 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 22.66 | 0.8516 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 23.53 | 0.8649 | 0.0254 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 22.23 | 0.8439 | 0.0281 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 21.54 | 0.7941 | 0.0400 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 20.23 | 0.7498 | 0.0462 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 21.44 | 0.7927 | 0.0401 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 19.91 | 0.7420 | 0.0467 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 23.31 | 0.8611 | 0.0251 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 22.77 | 0.8509 | 0.0255 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 23.25 | 0.8610 | 0.0251 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 22.44 | 0.8449 | 0.0258 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 20.05 | 0.7396 | 0.0471 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 19.76 | 0.7319 | 0.0472 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.58 | 0.8498 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.32 | 0.8444 | 0.0256 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 22.96 | 0.8562 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 22.73 | 0.8516 | 0.0238 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 23.11 | 0.8624 | 0.0223 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 22.92 | 0.8585 | 0.0225 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 23.55 | 0.8710 | 0.0211 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 23.42 | 0.8682 | 0.0212 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 20.66 | 0.7650 | 0.0440 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 20.50 | 0.7622 | 0.0437 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.59 | 0.8510 | 0.0258 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.63 | 0.8510 | 0.0255 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 23.01 | 0.8579 | 0.0241 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 23.00 | 0.8574 | 0.0239 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 23.27 | 0.8639 | 0.0222 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 23.17 | 0.8618 | 0.0224 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 23.55 | 0.8710 | 0.0211 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 23.42 | 0.8682 | 0.0212 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.73 | 0.9248 | 0.0355 | 1.00 |
| flow_s0.5_pose | 24.65 | 0.9099 | 0.0374 | 1.00 |
| flow_s0.5_uniform | 23.02 | 0.8845 | 0.0430 | 1.00 |
| flow_s1.0_oracle | 26.44 | 0.9323 | 0.0341 | 1.00 |
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| flow_s1.0_uniform | 23.35 | 0.8857 | 0.0419 | 1.00 |
| gs_tok448_nat_dil_al | 22.37 | 0.8291 | 0.0673 | 1.00 |
| gs_tok448_nat_dil_al+reg | 23.81 | 0.8615 | 0.0572 | 1.00 |
| gs_tok448_nat_dil_alv | 22.09 | 0.8245 | 0.0681 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 23.75 | 0.8610 | 0.0576 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 13.18 | 0.7538 | 0.1480 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 13.16 | 0.7493 | 0.1488 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.59 | 0.5573 | 0.3037 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.59 | 0.5532 | 0.3041 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.78 | 0.3039 | 0.3464 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.78 | 0.3005 | 0.3468 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.57 | 0.4209 | 0.3331 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.56 | 0.4169 | 0.3335 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.53 | 0.1492 | 0.3818 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.53 | 0.1472 | 0.3820 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 25.82 | 0.9176 | 0.0396 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 24.92 | 0.9102 | 0.0422 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 25.71 | 0.9168 | 0.0399 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 24.51 | 0.9063 | 0.0432 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 24.41 | 0.8918 | 0.0472 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 23.28 | 0.8745 | 0.0524 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 24.32 | 0.8911 | 0.0478 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 22.96 | 0.8701 | 0.0533 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 25.34 | 0.9145 | 0.0385 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 24.94 | 0.9103 | 0.0394 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 25.28 | 0.9143 | 0.0386 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 24.62 | 0.9073 | 0.0400 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 23.00 | 0.8665 | 0.0542 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 22.70 | 0.8620 | 0.0549 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.97 | 0.9135 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 24.72 | 0.9105 | 0.0386 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.11 | 0.9138 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 24.87 | 0.9111 | 0.0378 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.18 | 0.9167 | 0.0369 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.01 | 0.9145 | 0.0371 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.62 | 0.9197 | 0.0360 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 25.52 | 0.9181 | 0.0362 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 23.71 | 0.8791 | 0.0507 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 23.47 | 0.8772 | 0.0517 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 25.11 | 0.9148 | 0.0384 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 25.11 | 0.9141 | 0.0381 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.22 | 0.9148 | 0.0376 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 25.23 | 0.9141 | 0.0373 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.41 | 0.9172 | 0.0366 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.33 | 0.9159 | 0.0367 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.62 | 0.9197 | 0.0360 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 25.52 | 0.9181 | 0.0362 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.41 | 0.9667 | 0.0317 | 1.00 |
| flow_s0.5_pose | 31.22 | 0.9653 | 0.0318 | 1.00 |
| flow_s0.5_uniform | 30.53 | 0.9607 | 0.0346 | 1.00 |
| flow_s1.0_oracle | 31.56 | 0.9661 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| flow_s1.0_uniform | 30.29 | 0.9592 | 0.0331 | 1.00 |
| gs_tok448_nat_dil_al | 27.16 | 0.9120 | 0.0718 | 1.00 |
| gs_tok448_nat_dil_al+reg | 28.17 | 0.9250 | 0.0652 | 1.00 |
| gs_tok448_nat_dil_alv | 27.11 | 0.9121 | 0.0723 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 28.20 | 0.9253 | 0.0652 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 10.98 | 0.7622 | 0.2327 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 10.98 | 0.7624 | 0.2328 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.33 | 0.5811 | 0.4326 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.33 | 0.5810 | 0.4326 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.02 | 0.3103 | 0.4579 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.02 | 0.3101 | 0.4579 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 5.49 | 0.4362 | 0.4560 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 5.49 | 0.4360 | 0.4560 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.08 | 0.1561 | 0.4898 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.08 | 0.1561 | 0.4898 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 31.46 | 0.9643 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 31.44 | 0.9636 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 31.46 | 0.9642 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 31.43 | 0.9634 | 0.0310 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 31.40 | 0.9624 | 0.0312 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 31.35 | 0.9615 | 0.0322 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 31.40 | 0.9623 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 31.36 | 0.9615 | 0.0322 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 30.25 | 0.9566 | 0.0401 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 30.15 | 0.9565 | 0.0402 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.35 | 0.9643 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 31.36 | 0.9643 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 31.37 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 31.38 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 31.43 | 0.9648 | 0.0307 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 31.44 | 0.9648 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 30.61 | 0.9588 | 0.0364 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 30.56 | 0.9587 | 0.0366 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 31.33 | 0.9643 | 0.0312 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 31.33 | 0.9643 | 0.0312 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 31.36 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 31.37 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 31.41 | 0.9648 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 31.42 | 0.9648 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 31.45 | 0.9648 | 0.0306 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_tok448_nat_dil_al | 24.77 | 0.8846 | 0.0882 | 1.00 |
| gs_tok448_nat_dil_al+reg | 26.06 | 0.9032 | 0.0849 | 1.00 |
| gs_tok448_nat_dil_alv | 24.55 | 0.8829 | 0.0887 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 26.01 | 0.9030 | 0.0853 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 11.59 | 0.7565 | 0.2488 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 11.58 | 0.7549 | 0.2490 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.65 | 0.5678 | 0.4859 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.64 | 0.5662 | 0.4862 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.26 | 0.3065 | 0.5304 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.26 | 0.3051 | 0.5306 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 5.79 | 0.4277 | 0.5211 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 5.79 | 0.4261 | 0.5215 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.24 | 0.1528 | 0.5770 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.24 | 0.1519 | 0.5771 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 28.33 | 0.9474 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 27.61 | 0.9438 | 0.0478 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 28.25 | 0.9470 | 0.0458 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 27.25 | 0.9421 | 0.0486 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 27.20 | 0.9349 | 0.0544 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 26.32 | 0.9277 | 0.0576 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 27.14 | 0.9346 | 0.0549 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 26.06 | 0.9260 | 0.0581 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 28.03 | 0.9471 | 0.0428 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 27.76 | 0.9456 | 0.0434 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 27.98 | 0.9469 | 0.0429 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 27.50 | 0.9445 | 0.0438 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 26.05 | 0.9235 | 0.0595 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.79 | 0.9218 | 0.0598 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.71 | 0.9466 | 0.0420 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.51 | 0.9454 | 0.0421 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 27.79 | 0.9467 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 27.61 | 0.9457 | 0.0412 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 27.91 | 0.9478 | 0.0406 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 27.78 | 0.9469 | 0.0408 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 28.23 | 0.9488 | 0.0397 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 28.16 | 0.9482 | 0.0398 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 26.62 | 0.9290 | 0.0579 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 26.44 | 0.9280 | 0.0589 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.77 | 0.9468 | 0.0421 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.81 | 0.9465 | 0.0417 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 27.87 | 0.9470 | 0.0411 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 27.90 | 0.9466 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 28.04 | 0.9479 | 0.0404 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 27.99 | 0.9473 | 0.0404 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 28.23 | 0.9488 | 0.0397 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 28.16 | 0.9482 | 0.0398 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_tok448_nat_dil_al | 0.53 | 0.83 |
| cam3 | gs_tok448_nat_dil_alv | 0.70 | 1.00 |
| cam5 | gs_tok448_nat_dil_al | 1.33 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv | 1.44 | 1.00 |

## 风险阈值扫描（风险区 vs oracle_fail，按 IoU 排序，前 8 名与配置默认值）

| 设置 | warp 阈值 | col 阈值 | 精确率 | 召回率 | IoU | 面积比 |
|---|---:|---:|---:|---:|---:|---:|
| cam3 | 0.20 | 6.0 | 0.444 | 0.710 | 0.377 | 1.66 |
| cam3 | 0.25 | 6.0 | 0.478 | 0.628 | 0.373 | 1.34 |
| cam3 | 0.20 | 不用 | 0.456 | 0.681 | 0.373 | 1.55 |
| cam3 | 0.20 | 4.0 | 0.418 | 0.732 | 0.365 | 1.82 |
| cam3 | 0.25 | 4.0 | 0.440 | 0.664 | 0.364 | 1.55 |
| cam3 | 0.25 | 不用 | 0.499 | 0.592 | 0.364 | 1.22 |
| cam3 | 0.30 | 6.0 | 0.500 | 0.564 | 0.361 | 1.15 |
| cam3 | 0.30 | 4.0 | 0.452 | 0.609 | 0.356 | 1.37 |
| cam3 | 0.08（默认） | 2.0 | 0.225 | 0.941 | 0.221 | 4.88 |
| cam5 | 0.20 | 3.0 | 0.308 | 0.516 | 0.237 | 1.71 |
| cam5 | 0.15 | 3.0 | 0.287 | 0.577 | 0.236 | 2.07 |
| cam5 | 0.12 | 3.0 | 0.271 | 0.659 | 0.235 | 2.57 |
| cam5 | 0.20 | 2.0 | 0.282 | 0.581 | 0.235 | 2.07 |
| cam5 | 0.12 | 不用 | 0.299 | 0.576 | 0.235 | 2.06 |
| cam5 | 0.15 | 2.0 | 0.268 | 0.632 | 0.232 | 2.40 |
| cam5 | 0.25 | 2.0 | 0.285 | 0.544 | 0.231 | 1.90 |
| cam5 | 0.25 | 3.0 | 0.312 | 0.471 | 0.230 | 1.51 |
| cam5 | 0.08（默认） | 2.0 | 0.188 | 0.823 | 0.181 | 4.78 |

## t 估计对比（scale=1.0）

| 设置 | 目标相机 | t_uniform | t_pose (VGGT) | t_posecal (标定) | t_oracle |
|---|---:|---:|---:|---:|---:|
| cam3 | 1 | 0.250 | 0.305 | — | 0.320 |
| cam3 | 2 | 0.500 | 0.551 | — | 0.550 |
| cam3 | 3 | 0.750 | 0.802 | — | 0.760 |
| cam3 | 5 | 0.250 | 0.194 | — | 0.220 |
| cam3 | 6 | 0.500 | 0.463 | — | 0.470 |
| cam3 | 7 | 0.750 | 0.742 | — | 0.740 |
| cam5 | 1 | 0.500 | 0.554 | — | 0.560 |
| cam5 | 3 | 0.500 | 0.559 | — | 0.550 |
| cam5 | 5 | 0.500 | 0.419 | — | 0.450 |
| cam5 | 7 | 0.500 | 0.522 | — | 0.530 |

## AnySplat 运行统计

旋转/光心误差：vggt 行是联合估计与输入视点估计的一致性；calib/calibK 行是标定位姿经 Sim(3) 对齐到AnySplat 输入视点位姿后的残差（反映 AnySplat 自身预测的输入相机几何与真实阵列的偏差）。

| 设置 | 变体 | 位姿来源 | 窗口边长 | 渲染分辨率 | 模式 | eps2d | 3D 滤波 | 高斯数 | 编码 s | 渲染 ms/视点 | 输入视点自渲染 PSNR | 最大旋转误差° | 最大光心误差/基线 |
|---|---|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| cam3 | gs_tok448_nat_dil_al | aligned_int | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 46.9 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tok448_nat_dil_alv | aligned_vggt | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 28.9 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 157.6 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 43.1 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 161.1 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 66.6 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 39.1 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 51.9 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 64.5 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 64.1 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 43.6 | 29.11 | 0.34 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368382 | 0.828 | 36.0 | 29.11 | 0.34 | 0.010 |
| cam5 | gs_tok448_nat_dil_al | aligned_int | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 50.6 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tok448_nat_dil_alv | aligned_vggt | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 34.8 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokr5448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 44.4 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 60.5 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 51.5 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 69.1 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokrife_g448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 37.8 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokrife_g448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 51.6 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokstrict448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 44.3 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 50.8 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokstrict_g448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 35.2 | 29.44 | 0.13 | 0.008 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 527417 | 0.519 | 32.6 | 29.44 | 0.13 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| cam3 | g_disp | 0.735 | 0.054 |
| cam3 | mask_ent | 0.523 | 0.054 |
| cam3 | mask_grad | 0.263 | 0.054 |
| cam3 | r_col | 0.885 | 0.054 |
| cam3 | r_warp | 0.921 | 0.054 |
| cam5 | g_disp | 0.750 | 0.018 |
| cam5 | mask_ent | 0.505 | 0.018 |
| cam5 | mask_grad | 0.279 | 0.018 |
| cam5 | r_col | 0.921 | 0.018 |
| cam5 | r_warp | 0.909 | 0.018 |
