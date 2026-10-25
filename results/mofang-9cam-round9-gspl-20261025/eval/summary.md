# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_tokr5448_nat_dil_al_local | 37.8% | 19.07 / 0.0542 | 21.98 / 0.0762 | 21.97 / 0.0739 | 0.59 |
| cam3 | gs_tokr5448_nat_dil_al_rpgs_local | 37.8% | 19.07 / 0.0542 | 17.04 / 0.2174 | 17.04 / 0.2174 | 0.00 |
| cam3 | gs_tokr5448_nat_dil_al_rpvggt_local | 37.8% | 19.07 / 0.0542 | 19.39 / 0.1911 | 19.58 / 0.1849 | 0.26 |
| cam3 | gs_tokr5448_nat_dil_alv_local | 37.8% | 19.08 / 0.0544 | 21.89 / 0.0759 | 22.14 / 0.0730 | 0.51 |
| cam3 | gs_tokrife448_nat_dil_al_local | 11.2% | 14.62 / 0.0673 | 19.92 / 0.0495 | 19.88 / 0.0488 | 0.77 |
| cam3 | gs_tokrife448_nat_dil_al_rpgs_local | 11.2% | 14.62 / 0.0673 | 15.67 / 0.1170 | 15.67 / 0.1170 | 0.00 |
| cam3 | gs_tokrife448_nat_dil_al_rpvggt_local | 11.2% | 14.62 / 0.0673 | 17.04 / 0.1304 | 17.07 / 0.1251 | 1.17 |
| cam3 | gs_tokrife448_nat_dil_alv_local | 11.1% | 14.58 / 0.0674 | 19.85 / 0.0496 | 19.46 / 0.0502 | 1.69 |
| cam3 | gs_tokrife_g448_nat_dil_al_local | 16.9% | 13.56 / 0.0907 | 20.48 / 0.0550 | 20.48 / 0.0550 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_al_rpgs_local | 16.9% | 13.56 / 0.0907 | 15.47 / 0.1365 | 15.47 / 0.1365 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_al_rpvggt_local | 16.9% | 13.56 / 0.0907 | 16.97 / 0.1627 | 16.97 / 0.1627 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_alv_local | 16.9% | 13.56 / 0.0904 | 20.27 / 0.0545 | 19.62 / 0.0572 | 1.05 |
| cam3 | gs_tokstrict448_nat_dil_al_local | 7.5% | 14.43 / 0.1303 | 18.96 / 0.0727 | 18.88 / 0.0780 | 1.75 |
| cam3 | gs_tokstrict448_nat_dil_al_rpgs_local | 7.5% | 14.43 / 0.1303 | 14.67 / 0.2187 | 14.67 / 0.2187 | 0.00 |
| cam3 | gs_tokstrict448_nat_dil_al_rpvggt_local | 7.5% | 14.43 / 0.1303 | 16.67 / 0.2161 | 16.79 / 0.2137 | 0.96 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | 7.4% | 14.42 / 0.1317 | 18.90 / 0.0788 | 18.86 / 0.0821 | 1.37 |
| cam3 | gs_tokstrict_g448_nat_dil_al_local | 14.0% | 12.86 / 0.1289 | 20.49 / 0.0633 | 20.49 / 0.0633 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_rpgs_local | 14.0% | 12.86 / 0.1289 | 15.17 / 0.1569 | 15.17 / 0.1569 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_rpvggt_local | 14.0% | 12.86 / 0.1289 | 16.66 / 0.2087 | 16.66 / 0.2087 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_local | 13.9% | 12.86 / 0.1286 | 20.19 / 0.0639 | 20.19 / 0.0639 | 0.00 |
| cam5 | gs_tokr5448_nat_dil_al_local | 18.3% | 23.74 / 0.0214 | 20.17 / 0.0521 | 21.05 / 0.0441 | 1.60 |
| cam5 | gs_tokr5448_nat_dil_al_rpgs_local | 18.3% | 23.74 / 0.0214 | 17.24 / 0.1158 | 17.24 / 0.1158 | 0.00 |
| cam5 | gs_tokr5448_nat_dil_al_rpvggt_local | 18.3% | 23.74 / 0.0214 | 19.89 / 0.1061 | 21.18 / 0.0883 | 1.50 |
| cam5 | gs_tokr5448_nat_dil_alv_local | 18.3% | 23.76 / 0.0214 | 19.88 / 0.0523 | 20.90 / 0.0441 | 1.76 |
| cam5 | gs_tokrife448_nat_dil_al_local | 4.6% | 20.89 / 0.0641 | 18.75 / 0.1184 | 19.00 / 0.1127 | 0.98 |
| cam5 | gs_tokrife448_nat_dil_al_rpgs_local | 4.6% | 20.89 / 0.0641 | 18.20 / 0.1607 | 18.20 / 0.1607 | 0.00 |
| cam5 | gs_tokrife448_nat_dil_al_rpvggt_local | 4.6% | 20.89 / 0.0641 | 18.87 / 0.2190 | 18.87 / 0.2190 | 0.00 |
| cam5 | gs_tokrife448_nat_dil_alv_local | 4.6% | 20.93 / 0.0635 | 18.45 / 0.1197 | 18.88 / 0.1117 | 1.41 |
| cam5 | gs_tokrife_g448_nat_dil_al_local | 7.9% | 20.65 / 0.0544 | 20.07 / 0.0888 | 20.39 / 0.0826 | 0.52 |
| cam5 | gs_tokrife_g448_nat_dil_al_rpgs_local | 7.9% | 20.65 / 0.0544 | 16.75 / 0.1502 | 16.75 / 0.1502 | 0.00 |
| cam5 | gs_tokrife_g448_nat_dil_al_rpvggt_local | 7.9% | 20.65 / 0.0544 | 18.76 / 0.2313 | 18.76 / 0.2313 | 0.00 |
| cam5 | gs_tokrife_g448_nat_dil_alv_local | 7.9% | 20.66 / 0.0540 | 19.42 / 0.0911 | 19.97 / 0.0782 | 1.12 |
| cam5 | gs_tokstrict448_nat_dil_al_local | 3.2% | 18.58 / 0.0849 | 17.53 / 0.0938 | 17.71 / 0.0894 | 0.86 |
| cam5 | gs_tokstrict448_nat_dil_al_rpgs_local | 3.2% | 18.58 / 0.0849 | 14.88 / 0.1969 | 14.88 / 0.1969 | 0.00 |
| cam5 | gs_tokstrict448_nat_dil_al_rpvggt_local | 3.2% | 18.58 / 0.0849 | 17.52 / 0.2092 | 17.52 / 0.2092 | 0.00 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | 3.2% | 18.55 / 0.0843 | 17.05 / 0.0978 | 17.31 / 0.0917 | 1.21 |
| cam5 | gs_tokstrict_g448_nat_dil_al_local | 5.8% | 15.30 / 0.1220 | 17.64 / 0.0949 | 17.64 / 0.0949 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_al_rpgs_local | 5.8% | 15.30 / 0.1220 | 15.07 / 0.1889 | 15.07 / 0.1889 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_al_rpvggt_local | 5.8% | 15.30 / 0.1220 | 16.09 / 0.2937 | 16.09 / 0.2937 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_local | 5.8% | 15.33 / 0.1211 | 16.83 / 0.0982 | 16.83 / 0.0982 | 0.00 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_local] | 25.43 / 0.0765 | 17.06 / 0.1772 | 17.89 / 0.0478 | 32.24 / 0.0318 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 20.61 / 0.2288 | 12.16 / 0.4792 | 12.98 / 0.1316 | 29.52 / 0.0872 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 22.83 / 0.2001 | 15.70 / 0.4689 | 15.46 / 0.1124 | 29.50 / 0.0876 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.30 / 0.0764 | 16.73 / 0.1799 | 17.68 / 0.0479 | 32.24 / 0.0315 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.38 / 0.0537 | 17.41 / 0.1632 | 17.82 / 0.0379 | 33.49 / 0.0235 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 23.48 / 0.0908 | 13.42 / 0.4003 | 14.41 / 0.0706 | 33.36 / 0.0253 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.52 / 0.0997 | 16.25 / 0.4160 | 15.75 / 0.0749 | 33.09 / 0.0300 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.31 / 0.0538 | 17.27 / 0.1644 | 17.72 / 0.0379 | 33.49 / 0.0236 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.12 / 0.0532 | 18.09 / 0.1363 | 15.76 / 0.0383 | 33.50 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.30 / 0.0764 | 15.88 / 0.2450 | 13.64 / 0.0610 | 33.37 / 0.0249 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 23.90 / 0.0861 | 17.22 / 0.2819 | 14.49 / 0.0668 | 33.21 / 0.0274 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 25.06 / 0.0532 | 17.94 / 0.1372 | 15.66 / 0.0382 | 33.50 / 0.0235 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.29 / 0.0519 | 17.57 / 0.1436 | 15.97 / 0.0371 | 33.53 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.41 / 0.0720 | 14.58 / 0.3103 | 13.81 / 0.0577 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.11 / 0.0807 | 16.82 / 0.3318 | 14.72 / 0.0631 | 33.48 / 0.0244 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.23 / 0.0520 | 17.43 / 0.1446 | 15.89 / 0.0371 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.10 / 0.0518 | 18.08 / 0.1376 | 15.64 / 0.0372 | 33.53 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.44 / 0.0681 | 15.88 / 0.2449 | 13.69 / 0.0548 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.97 / 0.0780 | 17.23 / 0.2817 | 14.48 / 0.0616 | 33.48 / 0.0244 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 25.04 / 0.0518 | 17.93 / 0.1387 | 15.55 / 0.0372 | 33.53 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.47 / 0.0766 | 16.65 / 0.1853 | 17.88 / 0.0482 | 32.33 / 0.0306 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 20.61 / 0.2288 | 12.16 / 0.4792 | 12.98 / 0.1316 | 29.52 / 0.0872 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 23.00 / 0.1945 | 15.89 / 0.4539 | 15.63 / 0.1095 | 29.61 / 0.0846 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.56 / 0.0760 | 16.89 / 0.1818 | 18.00 / 0.0468 | 32.35 / 0.0302 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.38 / 0.0537 | 17.28 / 0.1649 | 17.85 / 0.0383 | 33.50 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 23.48 / 0.0908 | 13.42 / 0.4003 | 14.41 / 0.0706 | 33.36 / 0.0253 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.49 / 0.0972 | 16.15 / 0.3978 | 15.72 / 0.0732 | 33.13 / 0.0295 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.08 / 0.0548 | 16.83 / 0.1745 | 17.57 / 0.0396 | 33.48 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.12 / 0.0532 | 18.09 / 0.1363 | 15.76 / 0.0383 | 33.50 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.30 / 0.0764 | 15.88 / 0.2450 | 13.64 / 0.0610 | 33.37 / 0.0249 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 23.90 / 0.0861 | 17.22 / 0.2819 | 14.49 / 0.0668 | 33.21 / 0.0274 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 24.81 / 0.0541 | 17.63 / 0.1446 | 15.42 / 0.0397 | 33.49 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.27 / 0.0520 | 17.56 / 0.1464 | 15.97 / 0.0374 | 33.53 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.41 / 0.0720 | 14.58 / 0.3103 | 13.81 / 0.0577 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.12 / 0.0805 | 16.80 / 0.3290 | 14.73 / 0.0630 | 33.48 / 0.0244 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.21 / 0.0521 | 17.38 / 0.1453 | 15.88 / 0.0373 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.10 / 0.0518 | 18.08 / 0.1376 | 15.64 / 0.0372 | 33.53 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.44 / 0.0681 | 15.88 / 0.2449 | 13.69 / 0.0548 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.97 / 0.0780 | 17.23 / 0.2817 | 14.48 / 0.0616 | 33.48 / 0.0244 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 25.04 / 0.0518 | 17.93 / 0.1387 | 15.55 / 0.0372 | 33.53 / 0.0233 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_local] | 26.01 / 0.0597 | 18.20 / 0.1569 | 16.63 / 0.0315 | 30.24 / 0.0405 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 23.48 / 0.1245 | 14.81 / 0.3657 | 13.31 / 0.0579 | 28.93 / 0.0640 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 25.65 / 0.1164 | 17.82 / 0.3671 | 16.53 / 0.0567 | 29.34 / 0.0692 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.75 / 0.0600 | 17.66 / 0.1590 | 16.20 / 0.0327 | 30.11 / 0.0405 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.71 / 0.0419 | 20.21 / 0.0903 | 17.91 / 0.0206 | 31.35 / 0.0311 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 26.54 / 0.0513 | 18.36 / 0.1838 | 16.05 / 0.0288 | 31.28 / 0.0318 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 27.39 / 0.0608 | 19.82 / 0.2124 | 17.58 / 0.0344 | 30.81 / 0.0378 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.50 / 0.0420 | 19.87 / 0.0938 | 17.57 / 0.0214 | 31.36 / 0.0311 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_local] | 27.78 / 0.0409 | 20.47 / 0.0837 | 17.96 / 0.0199 | 31.37 / 0.0308 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 26.70 / 0.0483 | 18.73 / 0.1495 | 16.18 / 0.0269 | 31.30 / 0.0310 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 27.40 / 0.0574 | 19.85 / 0.1924 | 17.54 / 0.0320 | 30.81 / 0.0371 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 27.59 / 0.0412 | 20.14 / 0.0861 | 17.63 / 0.0207 | 31.38 / 0.0308 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 27.92 / 0.0406 | 20.56 / 0.0780 | 17.94 / 0.0190 | 31.43 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 26.86 / 0.0464 | 18.91 / 0.1457 | 16.34 / 0.0249 | 31.41 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 27.66 / 0.0523 | 20.27 / 0.1572 | 17.69 / 0.0285 | 31.04 / 0.0344 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 27.78 / 0.0408 | 20.28 / 0.0817 | 17.69 / 0.0194 | 31.44 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 28.24 / 0.0396 | 21.09 / 0.0664 | 18.15 / 0.0175 | 31.45 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 27.96 / 0.0425 | 20.42 / 0.0918 | 17.57 / 0.0206 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 28.08 / 0.0468 | 20.74 / 0.1168 | 17.89 / 0.0236 | 31.44 / 0.0318 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 28.17 / 0.0398 | 20.90 / 0.0680 | 18.01 / 0.0177 | 31.45 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 26.66 / 0.0579 | 18.25 / 0.1510 | 17.40 / 0.0295 | 30.62 / 0.0365 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 23.48 / 0.1245 | 14.81 / 0.3657 | 13.31 / 0.0579 | 28.93 / 0.0640 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 26.39 / 0.1021 | 18.83 / 0.3116 | 17.50 / 0.0471 | 29.72 / 0.0602 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 26.49 / 0.0588 | 17.97 / 0.1532 | 17.09 / 0.0302 | 30.57 / 0.0365 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.90 / 0.0418 | 20.19 / 0.0914 | 18.21 / 0.0200 | 31.34 / 0.0312 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 26.54 / 0.0513 | 18.36 / 0.1838 | 16.05 / 0.0288 | 31.28 / 0.0318 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 27.39 / 0.0608 | 19.82 / 0.2124 | 17.58 / 0.0344 | 30.81 / 0.0378 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.81 / 0.0416 | 19.82 / 0.0934 | 18.06 / 0.0200 | 31.34 / 0.0311 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 27.96 / 0.0408 | 20.44 / 0.0857 | 18.24 / 0.0193 | 31.36 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 26.70 / 0.0483 | 18.73 / 0.1495 | 16.18 / 0.0269 | 31.30 / 0.0310 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 27.40 / 0.0574 | 19.85 / 0.1924 | 17.54 / 0.0320 | 30.81 / 0.0371 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 27.87 / 0.0408 | 20.10 / 0.0875 | 18.07 / 0.0192 | 31.36 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 28.05 / 0.0404 | 20.39 / 0.0787 | 18.18 / 0.0183 | 31.40 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 26.86 / 0.0464 | 18.91 / 0.1457 | 16.34 / 0.0249 | 31.41 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 27.66 / 0.0523 | 20.27 / 0.1572 | 17.69 / 0.0285 | 31.04 / 0.0344 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 27.98 / 0.0403 | 20.16 / 0.0834 | 18.11 / 0.0183 | 31.41 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 28.24 / 0.0396 | 21.09 / 0.0664 | 18.15 / 0.0175 | 31.45 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 27.96 / 0.0425 | 20.42 / 0.0918 | 17.57 / 0.0206 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 28.08 / 0.0468 | 20.74 / 0.1168 | 17.89 / 0.0236 | 31.44 / 0.0318 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 28.17 / 0.0398 | 20.90 / 0.0680 | 18.01 / 0.0177 | 31.45 / 0.0306 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.2%） | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 |
| cam3 | r5 | 30.7% | 37.8% | 25.43 / 0.0765 | 17.06 / 0.1772 | 32.24 |
| cam3 | rife | 10.8% | 11.2% | 26.38 / 0.0537 | 17.41 / 0.1632 | 33.49 |
| cam3 | strict | 8.4% | 7.5% | 25.29 / 0.0519 | 17.57 / 0.1436 | 33.53 |
| cam3 | rife_g | 9.7% | 8.5% | 25.12 / 0.0532 | 18.09 / 0.1363 | 33.50 |
| cam3 | strict_g | 8.3% | 7.0% | 25.10 / 0.0518 | 18.08 / 0.1376 | 33.53 |
| cam5 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.2%） | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 |
| cam5 | r5 | 15.7% | 18.3% | 26.01 / 0.0597 | 18.20 / 0.1569 | 30.24 |
| cam5 | rife | 3.8% | 4.6% | 27.71 / 0.0419 | 20.21 / 0.0903 | 31.35 |
| cam5 | strict | 2.4% | 2.4% | 27.92 / 0.0406 | 20.56 / 0.0780 | 31.43 |
| cam5 | rife_g | 3.5% | 4.0% | 27.78 / 0.0409 | 20.47 / 0.0837 | 31.37 |
| cam5 | strict_g | 1.6% | 1.5% | 28.24 / 0.0396 | 21.09 / 0.0664 | 31.45 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| cam3 | 1 | 0-4 | 19.25 / 0.1012 | +4.12 / -0.0059 (core 30.4%) | +4.63 / -0.0266 (core 14.5%) | +4.54 / -0.0284 (core 12.4%) | +4.63 / -0.0266 (core 14.5%) | +4.54 / -0.0284 (core 12.4%) |
| cam3 | 2 | 0-4 | 20.14 / 0.0784 | +4.07 / -0.0025 (core 30.4%) | +4.60 / -0.0222 (core 14.5%) | +4.54 / -0.0257 (core 12.4%) | +4.60 / -0.0222 (core 14.5%) | +4.54 / -0.0257 (core 12.4%) |
| cam3 | 3 | 0-4 | 22.11 / 0.0577 | +5.02 / +0.0060 (core 30.4%) | +5.85 / -0.0094 (core 14.5%) | +5.90 / -0.0124 (core 12.4%) | +5.85 / -0.0094 (core 14.5%) | +5.90 / -0.0124 (core 12.4%) |
| cam3 | 5 | 4-8 | 25.45 / 0.0357 | +1.85 / +0.0310 (core 24.9%) | +2.95 / +0.0010 (core 2.5%) | +0.41 / +0.0001 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam3 | 6 | 4-8 | 24.03 / 0.0518 | +1.99 / +0.0252 (core 24.9%) | +3.46 / -0.0002 (core 2.5%) | +0.25 / +0.0007 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam3 | 7 | 4-8 | 24.65 / 0.0526 | -0.13 / +0.0276 (core 24.9%) | +1.14 / +0.0026 (core 2.5%) | +0.46 / -0.0004 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam5 | 1 | 0-2 | 23.87 / 0.0592 | +0.01 / +0.0207 (core 18.8%) | +0.96 / +0.0014 (core 5.9%) | +0.94 / +0.0002 (core 4.0%) | +0.96 / +0.0014 (core 5.9%) | +0.94 / +0.0002 (core 4.0%) |
| cam5 | 3 | 2-4 | 32.61 / 0.0248 | -4.33 / +0.0193 (core 12.0%) | -1.83 / +0.0040 (core 3.7%) | -0.94 / +0.0033 (core 2.1%) | -1.83 / +0.0040 (core 3.7%) | +0.00 / +0.0000 (core 2.1%*) |
| cam5 | 5 | 4-6 | 28.67 / 0.0315 | -1.24 / +0.0180 (core 11.3%) | -0.28 / +0.0014 (core 0.8%) | -0.32 / +0.0005 (core 0.2%) | +0.00 / +0.0000 (core 0.8%*) | +0.00 / +0.0000 (core 0.2%*) |
| cam5 | 7 | 6-8 | 26.85 / 0.0428 | -2.42 / +0.0224 (core 7.1%) | -0.02 / +0.0024 (core 0.4%) | +0.00 / +0.0000 (core 0.0%) | +0.00 / +0.0000 (core 0.4%*) | +0.00 / +0.0000 (core 0.0%*) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | 22.60 / 0.0629 | 14.53 | 33.53 | — |
| cam3 | r5 | 不复核 | 37.8% | 25.43 / 0.0765 | 17.06 | 32.24 | 2/6 |
| cam3 | r5 | w20 | 13.7% | 26.15 / 0.0582 | 16.84 | 33.53 | 3/6 |
| cam3 | r5 | oracle | 8.5% | 26.51 / 0.0575 | 17.61 | 33.49 | 3/6 |
| cam3 | r5 | 不复核 | 37.8% | 20.61 / 0.2288 | 12.16 | 29.52 | 0/6 |
| cam3 | r5 | w20 | 13.7% | 22.52 / 0.1168 | 12.47 | 33.40 | 0/6 |
| cam3 | r5 | oracle | 8.5% | 22.33 / 0.1341 | 12.98 | 33.10 | 0/6 |
| cam3 | r5 | 不复核 | 37.8% | 22.83 / 0.2001 | 15.70 | 29.50 | 0/6 |
| cam3 | r5 | w20 | 13.7% | 24.25 / 0.1210 | 15.79 | 33.44 | 0/6 |
| cam3 | r5 | oracle | 8.5% | 24.53 / 0.1260 | 16.45 | 33.45 | 0/6 |
| cam3 | rife | 不复核 | 11.2% | 26.38 / 0.0537 | 17.41 | 33.49 | 4/6 |
| cam3 | rife | w20 | 9.5% | 26.17 / 0.0535 | 17.10 | 33.53 | 5/6 |
| cam3 | rife | oracle | 5.4% | 26.57 / 0.0512 | 17.77 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | 11.2% | 23.48 / 0.0908 | 13.42 | 33.36 | 0/6 |
| cam3 | rife | w20 | 9.5% | 23.53 / 0.0879 | 13.57 | 33.45 | 0/6 |
| cam3 | rife | oracle | 5.4% | 23.88 / 0.0803 | 14.06 | 33.53 | 0/6 |
| cam3 | rife | 不复核 | 11.2% | 24.52 / 0.0997 | 16.25 | 33.09 | 0/6 |
| cam3 | rife | w20 | 9.5% | 24.60 / 0.0947 | 16.14 | 33.51 | 0/6 |
| cam3 | rife | oracle | 5.4% | 25.00 / 0.0864 | 16.80 | 33.53 | 0/6 |
| cam3 | rife_g | 不复核 | 8.5% | 25.12 / 0.0532 | 18.09 | 33.50 | 6/6 |
| cam3 | rife_g | w20 | 7.7% | 24.93 / 0.0535 | 17.67 | 33.53 | 6/6 |
| cam3 | rife_g | oracle | 4.4% | 25.22 / 0.0517 | 18.09 | 33.53 | 6/6 |
| cam3 | rife_g | 不复核 | 8.5% | 23.30 / 0.0764 | 15.88 | 33.37 | 3/6 |
| cam3 | rife_g | w20 | 7.7% | 23.24 / 0.0758 | 15.73 | 33.45 | 3/6 |
| cam3 | rife_g | oracle | 4.4% | 23.40 / 0.0710 | 15.89 | 33.53 | 3/6 |
| cam3 | rife_g | 不复核 | 8.5% | 23.90 / 0.0861 | 17.22 | 33.21 | 3/6 |
| cam3 | rife_g | w20 | 7.7% | 23.83 / 0.0842 | 16.98 | 33.51 | 3/6 |
| cam3 | rife_g | oracle | 4.4% | 24.10 / 0.0780 | 17.25 | 33.53 | 3/6 |
| cam3 | strict | 不复核 | 7.5% | 25.29 / 0.0519 | 17.57 | 33.53 | 4/6 |
| cam3 | strict | w20 | 7.0% | 25.10 / 0.0522 | 17.20 | 33.53 | 5/6 |
| cam3 | strict | oracle | 4.2% | 25.36 / 0.0509 | 17.77 | 33.53 | 5/6 |
| cam3 | strict | 不复核 | 7.5% | 23.41 / 0.0720 | 14.58 | 33.53 | 0/6 |
| cam3 | strict | w20 | 7.0% | 23.36 / 0.0714 | 14.66 | 33.53 | 0/6 |
| cam3 | strict | oracle | 4.2% | 23.52 / 0.0682 | 15.13 | 33.53 | 1/6 |
| cam3 | strict | 不复核 | 7.5% | 24.11 / 0.0807 | 16.82 | 33.48 | 0/6 |
| cam3 | strict | w20 | 7.0% | 24.02 / 0.0805 | 16.66 | 33.52 | 0/6 |
| cam3 | strict | oracle | 4.2% | 24.29 / 0.0747 | 17.06 | 33.53 | 0/6 |
| cam3 | strict_g | 不复核 | 7.0% | 25.10 / 0.0518 | 18.08 | 33.53 | 6/6 |
| cam3 | strict_g | w20 | 6.7% | 24.91 / 0.0523 | 17.67 | 33.53 | 6/6 |
| cam3 | strict_g | oracle | 4.0% | 25.15 / 0.0510 | 18.08 | 33.53 | 6/6 |
| cam3 | strict_g | 不复核 | 7.0% | 23.44 / 0.0681 | 15.88 | 33.53 | 3/6 |
| cam3 | strict_g | w20 | 6.7% | 23.36 / 0.0684 | 15.73 | 33.53 | 3/6 |
| cam3 | strict_g | oracle | 4.0% | 23.48 / 0.0657 | 15.89 | 33.53 | 4/6 |
| cam3 | strict_g | 不复核 | 7.0% | 23.97 / 0.0780 | 17.23 | 33.48 | 3/6 |
| cam3 | strict_g | w20 | 6.7% | 23.87 / 0.0781 | 16.98 | 33.52 | 3/6 |
| cam3 | strict_g | oracle | 4.0% | 24.13 / 0.0729 | 17.25 | 33.53 | 3/6 |
| cam5 | 纯光流 | — | — | 28.00 / 0.0396 | 20.41 | 31.46 | — |
| cam5 | r5 | 不复核 | 18.3% | 26.01 / 0.0597 | 18.20 | 30.24 | 0/4 |
| cam5 | r5 | w20 | 3.9% | 27.59 / 0.0426 | 19.98 | 31.44 | 0/4 |
| cam5 | r5 | oracle | 3.5% | 27.36 / 0.0466 | 18.96 | 31.35 | 0/4 |
| cam5 | r5 | 不复核 | 18.3% | 23.48 / 0.1245 | 14.81 | 28.93 | 0/4 |
| cam5 | r5 | w20 | 3.9% | 26.28 / 0.0553 | 18.03 | 31.44 | 0/4 |
| cam5 | r5 | oracle | 3.5% | 25.05 / 0.0685 | 15.74 | 31.10 | 0/4 |
| cam5 | r5 | 不复核 | 18.3% | 25.65 / 0.1164 | 17.82 | 29.34 | 0/4 |
| cam5 | r5 | w20 | 3.9% | 27.50 / 0.0602 | 20.05 | 31.38 | 0/4 |
| cam5 | r5 | oracle | 3.5% | 27.28 / 0.0743 | 19.13 | 31.32 | 0/4 |
| cam5 | rife | 不复核 | 4.6% | 27.71 / 0.0419 | 20.21 | 31.35 | 0/4 |
| cam5 | rife | w20 | 2.8% | 27.74 / 0.0408 | 20.24 | 31.45 | 0/4 |
| cam5 | rife | oracle | 1.6% | 27.96 / 0.0406 | 20.61 | 31.45 | 0/4 |
| cam5 | rife | 不复核 | 4.6% | 26.54 / 0.0513 | 18.36 | 31.28 | 0/4 |
| cam5 | rife | w20 | 2.8% | 26.75 / 0.0480 | 18.80 | 31.46 | 0/4 |
| cam5 | rife | oracle | 1.6% | 26.73 / 0.0477 | 18.75 | 31.45 | 0/4 |
| cam5 | rife | 不复核 | 4.6% | 27.39 / 0.0608 | 19.82 | 30.81 | 0/4 |
| cam5 | rife | w20 | 2.8% | 27.68 / 0.0546 | 20.26 | 31.39 | 0/4 |
| cam5 | rife | oracle | 1.6% | 27.79 / 0.0543 | 20.35 | 31.44 | 0/4 |
| cam5 | rife_g | 不复核 | 4.0% | 27.78 / 0.0409 | 20.47 | 31.37 | 2/4 |
| cam5 | rife_g | w20 | 2.6% | 27.81 / 0.0406 | 20.45 | 31.45 | 2/4 |
| cam5 | rife_g | oracle | 1.4% | 28.01 / 0.0402 | 20.80 | 31.45 | 2/4 |
| cam5 | rife_g | 不复核 | 4.0% | 26.70 / 0.0483 | 18.73 | 31.30 | 2/4 |
| cam5 | rife_g | w20 | 2.6% | 26.82 / 0.0470 | 19.00 | 31.46 | 2/4 |
| cam5 | rife_g | oracle | 1.4% | 26.86 / 0.0460 | 19.09 | 31.45 | 2/4 |
| cam5 | rife_g | 不复核 | 4.0% | 27.40 / 0.0574 | 19.85 | 30.81 | 2/4 |
| cam5 | rife_g | w20 | 2.6% | 27.66 / 0.0540 | 20.28 | 31.39 | 2/4 |
| cam5 | rife_g | oracle | 1.4% | 27.76 / 0.0521 | 20.34 | 31.44 | 2/4 |
| cam5 | strict | 不复核 | 2.4% | 27.92 / 0.0406 | 20.56 | 31.43 | 1/4 |
| cam5 | strict | w20 | 1.7% | 27.94 / 0.0401 | 20.56 | 31.45 | 2/4 |
| cam5 | strict | oracle | 1.1% | 28.05 / 0.0400 | 20.78 | 31.45 | 2/4 |
| cam5 | strict | 不复核 | 2.4% | 26.86 / 0.0464 | 18.91 | 31.41 | 1/4 |
| cam5 | strict | w20 | 1.7% | 26.98 / 0.0453 | 19.21 | 31.46 | 1/4 |
| cam5 | strict | oracle | 1.1% | 26.98 / 0.0450 | 19.25 | 31.45 | 1/4 |
| cam5 | strict | 不复核 | 2.4% | 27.66 / 0.0523 | 20.27 | 31.04 | 1/4 |
| cam5 | strict | w20 | 1.7% | 27.77 / 0.0506 | 20.35 | 31.40 | 1/4 |
| cam5 | strict | oracle | 1.1% | 27.89 / 0.0490 | 20.49 | 31.45 | 1/4 |
| cam5 | strict_g | 不复核 | 1.5% | 28.24 / 0.0396 | 21.09 | 31.45 | 3/4 |
| cam5 | strict_g | w20 | 1.1% | 28.21 / 0.0395 | 20.99 | 31.46 | 4/4 |
| cam5 | strict_g | oracle | 0.8% | 28.26 / 0.0396 | 21.10 | 31.46 | 4/4 |
| cam5 | strict_g | 不复核 | 1.5% | 27.96 / 0.0425 | 20.42 | 31.46 | 3/4 |
| cam5 | strict_g | w20 | 1.1% | 27.96 / 0.0421 | 20.43 | 31.46 | 3/4 |
| cam5 | strict_g | oracle | 0.8% | 27.97 / 0.0424 | 20.42 | 31.46 | 3/4 |
| cam5 | strict_g | 不复核 | 1.5% | 28.08 / 0.0468 | 20.74 | 31.44 | 3/4 |
| cam5 | strict_g | w20 | 1.1% | 28.09 / 0.0460 | 20.75 | 31.45 | 3/4 |
| cam5 | strict_g | oracle | 0.8% | 28.11 / 0.0453 | 20.78 | 31.45 | 3/4 |
### 纹理取自输入图（第九轮：同一 token 贴回区，颜色来源不同；oracle = 只贴 core ∩ 真值失败区）
| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| cam3 | — | 纯光流 | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 | — |
| cam3 | r5 | GS 颜色 | 直接 | 25.43 / 0.0765 | 17.06 / 0.1772 | 32.24 | 2/6 |
| cam3 | r5 | GS 颜色 | oracle | 26.51 / 0.0575 | 17.61 / 0.1638 | 33.49 | 3/6 |
| cam3 | r5 | GS 几何 + 输入纹理 | 直接 | 20.61 / 0.2288 | 12.16 / 0.4792 | 29.52 | 0/6 |
| cam3 | r5 | GS 几何 + 输入纹理 | oracle | 22.33 / 0.1341 | 12.98 / 0.4293 | 33.10 | 0/6 |
| cam3 | r5 | VGGT 几何 + 输入纹理 | 直接 | 22.83 / 0.2001 | 15.70 / 0.4689 | 29.50 | 0/6 |
| cam3 | r5 | VGGT 几何 + 输入纹理 | oracle | 24.53 / 0.1260 | 16.45 / 0.4149 | 33.45 | 0/6 |
| cam3 | rife | GS 颜色 | 直接 | 26.38 / 0.0537 | 17.41 / 0.1632 | 33.49 | 4/6 |
| cam3 | rife | GS 颜色 | oracle | 26.57 / 0.0512 | 17.77 / 0.1512 | 33.53 | 6/6 |
| cam3 | rife | GS 几何 + 输入纹理 | 直接 | 23.48 / 0.0908 | 13.42 / 0.4003 | 33.36 | 0/6 |
| cam3 | rife | GS 几何 + 输入纹理 | oracle | 23.88 / 0.0803 | 14.06 / 0.3663 | 33.53 | 0/6 |
| cam3 | rife | VGGT 几何 + 输入纹理 | 直接 | 24.52 / 0.0997 | 16.25 / 0.4160 | 33.09 | 0/6 |
| cam3 | rife | VGGT 几何 + 输入纹理 | oracle | 25.00 / 0.0864 | 16.80 / 0.3794 | 33.53 | 0/6 |
| cam3 | rife_g | GS 颜色 | 直接 | 25.12 / 0.0532 | 18.09 / 0.1363 | 33.50 | 6/6 |
| cam3 | rife_g | GS 颜色 | oracle | 25.22 / 0.0517 | 18.09 / 0.1360 | 33.53 | 6/6 |
| cam3 | rife_g | GS 几何 + 输入纹理 | 直接 | 23.30 / 0.0764 | 15.88 / 0.2450 | 33.37 | 3/6 |
| cam3 | rife_g | GS 几何 + 输入纹理 | oracle | 23.40 / 0.0710 | 15.89 / 0.2447 | 33.53 | 3/6 |
| cam3 | rife_g | VGGT 几何 + 输入纹理 | 直接 | 23.90 / 0.0861 | 17.22 / 0.2819 | 33.21 | 3/6 |
| cam3 | rife_g | VGGT 几何 + 输入纹理 | oracle | 24.10 / 0.0780 | 17.25 / 0.2773 | 33.53 | 3/6 |
| cam3 | strict | GS 颜色 | 直接 | 25.29 / 0.0519 | 17.57 / 0.1436 | 33.53 | 4/6 |
| cam3 | strict | GS 颜色 | oracle | 25.36 / 0.0509 | 17.77 / 0.1400 | 33.53 | 5/6 |
| cam3 | strict | GS 几何 + 输入纹理 | 直接 | 23.41 / 0.0720 | 14.58 / 0.3103 | 33.53 | 0/6 |
| cam3 | strict | GS 几何 + 输入纹理 | oracle | 23.52 / 0.0682 | 15.13 / 0.2942 | 33.53 | 1/6 |
| cam3 | strict | VGGT 几何 + 输入纹理 | 直接 | 24.11 / 0.0807 | 16.82 / 0.3318 | 33.48 | 0/6 |
| cam3 | strict | VGGT 几何 + 输入纹理 | oracle | 24.29 / 0.0747 | 17.06 / 0.3084 | 33.53 | 0/6 |
| cam3 | strict_g | GS 颜色 | 直接 | 25.10 / 0.0518 | 18.08 / 0.1376 | 33.53 | 6/6 |
| cam3 | strict_g | GS 颜色 | oracle | 25.15 / 0.0510 | 18.08 / 0.1370 | 33.53 | 6/6 |
| cam3 | strict_g | GS 几何 + 输入纹理 | 直接 | 23.44 / 0.0681 | 15.88 / 0.2449 | 33.53 | 3/6 |
| cam3 | strict_g | GS 几何 + 输入纹理 | oracle | 23.48 / 0.0657 | 15.89 / 0.2447 | 33.53 | 4/6 |
| cam3 | strict_g | VGGT 几何 + 输入纹理 | 直接 | 23.97 / 0.0780 | 17.23 / 0.2817 | 33.48 | 3/6 |
| cam3 | strict_g | VGGT 几何 + 输入纹理 | oracle | 24.13 / 0.0729 | 17.25 / 0.2772 | 33.53 | 3/6 |
| cam5 | — | 纯光流 | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 | — |
| cam5 | r5 | GS 颜色 | 直接 | 26.01 / 0.0597 | 18.20 / 0.1569 | 30.24 | 0/4 |
| cam5 | r5 | GS 颜色 | oracle | 27.36 / 0.0466 | 18.96 / 0.1263 | 31.35 | 0/4 |
| cam5 | r5 | GS 几何 + 输入纹理 | 直接 | 23.48 / 0.1245 | 14.81 / 0.3657 | 28.93 | 0/4 |
| cam5 | r5 | GS 几何 + 输入纹理 | oracle | 25.05 / 0.0685 | 15.74 / 0.3122 | 31.10 | 0/4 |
| cam5 | r5 | VGGT 几何 + 输入纹理 | 直接 | 25.65 / 0.1164 | 17.82 / 0.3671 | 29.34 | 0/4 |
| cam5 | r5 | VGGT 几何 + 输入纹理 | oracle | 27.28 / 0.0743 | 19.13 / 0.2777 | 31.32 | 0/4 |
| cam5 | rife | GS 颜色 | 直接 | 27.71 / 0.0419 | 20.21 / 0.0903 | 31.35 | 0/4 |
| cam5 | rife | GS 颜色 | oracle | 27.96 / 0.0406 | 20.61 / 0.0802 | 31.45 | 0/4 |
| cam5 | rife | GS 几何 + 输入纹理 | 直接 | 26.54 / 0.0513 | 18.36 / 0.1838 | 31.28 | 0/4 |
| cam5 | rife | GS 几何 + 输入纹理 | oracle | 26.73 / 0.0477 | 18.75 / 0.1674 | 31.45 | 0/4 |
| cam5 | rife | VGGT 几何 + 输入纹理 | 直接 | 27.39 / 0.0608 | 19.82 / 0.2124 | 30.81 | 0/4 |
| cam5 | rife | VGGT 几何 + 输入纹理 | oracle | 27.79 / 0.0543 | 20.35 / 0.1712 | 31.44 | 0/4 |
| cam5 | rife_g | GS 颜色 | 直接 | 27.78 / 0.0409 | 20.47 / 0.0837 | 31.37 | 2/4 |
| cam5 | rife_g | GS 颜色 | oracle | 28.01 / 0.0402 | 20.80 / 0.0757 | 31.45 | 2/4 |
| cam5 | rife_g | GS 几何 + 输入纹理 | 直接 | 26.70 / 0.0483 | 18.73 / 0.1495 | 31.30 | 2/4 |
| cam5 | rife_g | GS 几何 + 输入纹理 | oracle | 26.86 / 0.0460 | 19.09 / 0.1359 | 31.45 | 2/4 |
| cam5 | rife_g | VGGT 几何 + 输入纹理 | 直接 | 27.40 / 0.0574 | 19.85 / 0.1924 | 30.81 | 2/4 |
| cam5 | rife_g | VGGT 几何 + 输入纹理 | oracle | 27.76 / 0.0521 | 20.34 / 0.1555 | 31.44 | 2/4 |
| cam5 | strict | GS 颜色 | 直接 | 27.92 / 0.0406 | 20.56 / 0.0780 | 31.43 | 1/4 |
| cam5 | strict | GS 颜色 | oracle | 28.05 / 0.0400 | 20.78 / 0.0739 | 31.45 | 2/4 |
| cam5 | strict | GS 几何 + 输入纹理 | 直接 | 26.86 / 0.0464 | 18.91 / 0.1457 | 31.41 | 1/4 |
| cam5 | strict | GS 几何 + 输入纹理 | oracle | 26.98 / 0.0450 | 19.25 / 0.1361 | 31.45 | 1/4 |
| cam5 | strict | VGGT 几何 + 输入纹理 | 直接 | 27.66 / 0.0523 | 20.27 / 0.1572 | 31.04 | 1/4 |
| cam5 | strict | VGGT 几何 + 输入纹理 | oracle | 27.89 / 0.0490 | 20.49 / 0.1377 | 31.45 | 1/4 |
| cam5 | strict_g | GS 颜色 | 直接 | 28.24 / 0.0396 | 21.09 / 0.0664 | 31.45 | 3/4 |
| cam5 | strict_g | GS 颜色 | oracle | 28.26 / 0.0396 | 21.10 / 0.0662 | 31.46 | 4/4 |
| cam5 | strict_g | GS 几何 + 输入纹理 | 直接 | 27.96 / 0.0425 | 20.42 / 0.0918 | 31.46 | 3/4 |
| cam5 | strict_g | GS 几何 + 输入纹理 | oracle | 27.97 / 0.0424 | 20.42 / 0.0924 | 31.46 | 3/4 |
| cam5 | strict_g | VGGT 几何 + 输入纹理 | 直接 | 28.08 / 0.0468 | 20.74 / 0.1168 | 31.44 | 3/4 |
| cam5 | strict_g | VGGT 几何 + 输入纹理 | oracle | 28.11 / 0.0453 | 20.78 / 0.1144 | 31.45 | 3/4 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：aligned_int → `gs_tok448_nat_dil_al`，aligned_vggt → `gs_tok448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=6.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 12.52 / 0.0568 | 32.36 / 0.0269 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |
| flow_s0.5_pose | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 | 22.93 / 0.0610 |
| gs_tok448_nat_dil_al | 18.36 / 0.1455 | 18.33 / 0.0458 | 29.15 / 0.0541 | 25.02 / 0.0937 |
| gs_tok448_nat_dil_al+reg | 18.16 / 0.1503 | 18.68 / 0.0443 | 29.44 / 0.0516 | 25.37 / 0.0925 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.17 / 0.1463 | 18.33 / 0.0458 | 33.53 / 0.0235 | 27.04 / 0.0568 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.12 / 0.1740 | 17.24 / 0.0427 | 33.54 / 0.0233 | 25.87 / 0.0587 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.93 / 0.1524 | 18.68 / 0.0443 | 33.54 / 0.0234 | 27.18 / 0.0563 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 16.94 / 0.1797 | 17.34 / 0.0430 | 33.54 / 0.0233 | 25.93 / 0.0589 |
| gs_tok448_nat_dil_alv | 17.83 / 0.1487 | 18.04 / 0.0460 | 29.28 / 0.0537 | 24.92 / 0.0933 |
| gs_tok448_nat_dil_alv+reg | 18.17 / 0.1483 | 18.75 / 0.0432 | 29.36 / 0.0509 | 25.39 / 0.0917 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.62 / 0.1486 | 18.04 / 0.0460 | 33.53 / 0.0235 | 26.86 / 0.0568 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 16.90 / 0.1746 | 17.07 / 0.0427 | 33.54 / 0.0233 | 25.75 / 0.0585 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.90 / 0.1471 | 18.75 / 0.0432 | 33.54 / 0.0234 | 27.22 / 0.0557 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.13 / 0.1725 | 17.37 / 0.0424 | 33.54 / 0.0233 | 25.96 / 0.0584 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_tok448_nat_dil_al | 18.36 | 0.6876 | 0.1455 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.16 | 0.6761 | 0.1503 | 1.00 |
| gs_tok448_nat_dil_alv | 17.83 | 0.6701 | 0.1487 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.17 | 0.6882 | 0.1483 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.81 | 0.6694 | 0.1649 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 10.71 | 0.2784 | 0.4853 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 16.08 | 0.4422 | 0.4701 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.35 | 0.6529 | 0.1702 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.80 | 0.6692 | 0.1654 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 10.71 | 0.2784 | 0.4853 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 16.08 | 0.4422 | 0.4701 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 17.34 | 0.6527 | 0.1708 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 10.88 | 0.3337 | 0.4124 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 10.71 | 0.2784 | 0.4853 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 16.08 | 0.4422 | 0.4701 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 10.64 | 0.3278 | 0.4133 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 14.91 | 0.6068 | 0.2443 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 10.71 | 0.2784 | 0.4853 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 16.08 | 0.4422 | 0.4701 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 14.63 | 0.5934 | 0.2445 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 10.86 | 0.3325 | 0.4142 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 10.71 | 0.2784 | 0.4853 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 16.08 | 0.4422 | 0.4701 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 10.63 | 0.3268 | 0.4152 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.93 | 0.7043 | 0.1524 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.17 | 0.7144 | 0.1463 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.90 | 0.7091 | 0.1471 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.62 | 0.7003 | 0.1486 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 17.10 | 0.6587 | 0.1709 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 17.30 | 0.6701 | 0.1661 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.21 | 0.6713 | 0.1693 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 16.87 | 0.6532 | 0.1697 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 16.94 | 0.6691 | 0.1797 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.12 | 0.6758 | 0.1740 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.13 | 0.6802 | 0.1725 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 16.90 | 0.6688 | 0.1746 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 17.61 | 0.6875 | 0.1638 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 12.98 | 0.3781 | 0.4293 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 16.45 | 0.5106 | 0.4149 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.77 | 0.6971 | 0.1512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 14.06 | 0.4515 | 0.3663 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 16.80 | 0.5421 | 0.3794 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 18.09 | 0.6833 | 0.1360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 15.89 | 0.5393 | 0.2447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 17.25 | 0.5709 | 0.2773 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 17.77 | 0.6862 | 0.1400 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 15.13 | 0.5118 | 0.2942 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 17.06 | 0.5642 | 0.3084 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 18.08 | 0.6826 | 0.1370 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 15.89 | 0.5393 | 0.2447 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 17.25 | 0.5709 | 0.2772 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 16.84 | 0.6652 | 0.1819 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 12.47 | 0.3500 | 0.4595 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 15.79 | 0.4777 | 0.4477 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 17.10 | 0.6811 | 0.1691 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 13.57 | 0.4280 | 0.3967 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 16.14 | 0.5129 | 0.4099 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 17.67 | 0.6792 | 0.1452 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 15.73 | 0.5406 | 0.2525 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 16.98 | 0.5671 | 0.2849 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 17.20 | 0.6769 | 0.1507 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 14.66 | 0.5018 | 0.3120 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 16.66 | 0.5508 | 0.3283 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 17.67 | 0.6783 | 0.1466 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 15.73 | 0.5404 | 0.2524 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 16.98 | 0.5668 | 0.2848 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 17.06 | 0.6590 | 0.1772 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 12.16 | 0.3078 | 0.4792 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 15.70 | 0.4415 | 0.4689 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 16.73 | 0.6449 | 0.1799 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.41 | 0.6807 | 0.1632 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 13.42 | 0.4091 | 0.4003 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 16.25 | 0.5009 | 0.4160 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.27 | 0.6741 | 0.1644 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 18.09 | 0.6837 | 0.1363 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 15.88 | 0.5401 | 0.2450 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 17.22 | 0.5671 | 0.2819 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 17.94 | 0.6784 | 0.1372 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 17.57 | 0.6789 | 0.1436 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 14.58 | 0.4923 | 0.3103 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 16.82 | 0.5448 | 0.3318 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 17.43 | 0.6730 | 0.1446 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 18.08 | 0.6829 | 0.1376 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 15.88 | 0.5401 | 0.2449 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 17.23 | 0.5672 | 0.2817 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 17.93 | 0.6776 | 0.1387 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 16.65 | 0.6342 | 0.1853 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 12.16 | 0.3078 | 0.4792 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 15.89 | 0.4542 | 0.4539 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 16.89 | 0.6540 | 0.1818 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 17.28 | 0.6781 | 0.1649 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 13.42 | 0.4091 | 0.4003 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 16.15 | 0.4973 | 0.3978 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 16.83 | 0.6545 | 0.1745 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 18.09 | 0.6837 | 0.1363 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 15.88 | 0.5401 | 0.2450 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 17.22 | 0.5671 | 0.2819 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 17.63 | 0.6606 | 0.1446 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 17.56 | 0.6727 | 0.1464 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 14.58 | 0.4923 | 0.3103 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 16.80 | 0.5392 | 0.3290 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 17.38 | 0.6681 | 0.1453 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 18.08 | 0.6829 | 0.1376 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 15.88 | 0.5401 | 0.2449 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 17.23 | 0.5672 | 0.2817 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 17.93 | 0.6776 | 0.1387 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 14.17 | 0.5985 | 0.0457 | 1.00 |
| flow_s0.5_pose | 13.30 | 0.5443 | 0.0482 | 1.00 |
| flow_s0.5_uniform | 13.88 | 0.5654 | 0.0513 | 1.00 |
| flow_s1.0_oracle | 13.03 | 0.5914 | 0.0498 | 1.00 |
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| flow_s1.0_uniform | 12.52 | 0.5342 | 0.0568 | 1.00 |
| gs_tok448_nat_dil_al | 18.33 | 0.7167 | 0.0458 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.68 | 0.7245 | 0.0443 | 1.00 |
| gs_tok448_nat_dil_alv | 18.04 | 0.7097 | 0.0460 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.75 | 0.7293 | 0.0432 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.44 | 0.6927 | 0.0502 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 10.28 | 0.3283 | 0.1750 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 15.57 | 0.5060 | 0.1154 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.20 | 0.6873 | 0.0504 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.92 | 0.5611 | 0.1213 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 10.28 | 0.3283 | 0.1750 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 15.57 | 0.5060 | 0.1154 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 11.87 | 0.5557 | 0.1215 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 8.39 | 0.3081 | 0.1695 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 10.28 | 0.3283 | 0.1750 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 15.57 | 0.5060 | 0.1154 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 8.35 | 0.3058 | 0.1693 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 10.16 | 0.4761 | 0.1504 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 10.28 | 0.3283 | 0.1750 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 15.57 | 0.5060 | 0.1154 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 10.14 | 0.4735 | 0.1504 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 7.52 | 0.2793 | 0.1844 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 10.28 | 0.3283 | 0.1750 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 15.57 | 0.5060 | 0.1154 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 7.49 | 0.2771 | 0.1844 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.68 | 0.7166 | 0.0443 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 18.33 | 0.7068 | 0.0458 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.75 | 0.7212 | 0.0432 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.04 | 0.6996 | 0.0460 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 17.80 | 0.7106 | 0.0460 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 17.55 | 0.7056 | 0.0468 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.86 | 0.7154 | 0.0451 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 17.32 | 0.6987 | 0.0470 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 17.34 | 0.7031 | 0.0430 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.24 | 0.7012 | 0.0427 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.37 | 0.7070 | 0.0424 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 17.07 | 0.6966 | 0.0427 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 17.90 | 0.6988 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 12.99 | 0.4182 | 0.1308 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 15.47 | 0.5059 | 0.1120 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.81 | 0.6931 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 14.43 | 0.5286 | 0.0698 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 15.76 | 0.5431 | 0.0748 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 15.76 | 0.6544 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 13.65 | 0.5529 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 14.49 | 0.5493 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 15.97 | 0.6562 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 13.82 | 0.5479 | 0.0573 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 14.73 | 0.5483 | 0.0630 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 15.65 | 0.6519 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 13.69 | 0.5599 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 14.48 | 0.5505 | 0.0615 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 17.77 | 0.7025 | 0.0425 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 13.65 | 0.4829 | 0.0916 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 15.61 | 0.5336 | 0.0921 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 17.37 | 0.6870 | 0.0387 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 14.30 | 0.5300 | 0.0698 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 15.59 | 0.5440 | 0.0745 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 15.49 | 0.6525 | 0.0389 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 13.55 | 0.5533 | 0.0611 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 14.35 | 0.5494 | 0.0669 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 15.71 | 0.6540 | 0.0379 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 13.72 | 0.5484 | 0.0577 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 14.58 | 0.5475 | 0.0634 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 15.38 | 0.6501 | 0.0379 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 13.60 | 0.5604 | 0.0551 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 14.34 | 0.5503 | 0.0619 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 17.89 | 0.6967 | 0.0478 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 12.98 | 0.4150 | 0.1316 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 15.46 | 0.5033 | 0.1124 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.68 | 0.6912 | 0.0479 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.82 | 0.6921 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 14.41 | 0.5262 | 0.0706 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 15.75 | 0.5418 | 0.0749 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.72 | 0.6900 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 15.76 | 0.6541 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 13.64 | 0.5527 | 0.0610 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 14.49 | 0.5492 | 0.0668 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 15.66 | 0.6514 | 0.0382 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 15.97 | 0.6561 | 0.0371 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 13.81 | 0.5471 | 0.0577 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 14.72 | 0.5479 | 0.0631 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 15.89 | 0.6541 | 0.0371 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 15.64 | 0.6518 | 0.0372 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 13.69 | 0.5599 | 0.0548 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 14.48 | 0.5504 | 0.0616 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 15.55 | 0.6490 | 0.0372 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.88 | 0.6882 | 0.0482 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 12.98 | 0.4150 | 0.1316 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 15.63 | 0.5158 | 0.1095 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 18.00 | 0.6973 | 0.0468 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 17.85 | 0.6922 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 14.41 | 0.5262 | 0.0706 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 15.72 | 0.5427 | 0.0732 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 17.57 | 0.6776 | 0.0396 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 15.76 | 0.6541 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 13.64 | 0.5527 | 0.0610 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 14.49 | 0.5492 | 0.0668 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 15.42 | 0.6388 | 0.0397 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 15.97 | 0.6526 | 0.0374 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 13.81 | 0.5471 | 0.0577 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 14.73 | 0.5459 | 0.0630 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 15.88 | 0.6522 | 0.0373 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 15.64 | 0.6518 | 0.0372 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 13.69 | 0.5599 | 0.0548 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 14.48 | 0.5504 | 0.0616 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 15.55 | 0.6490 | 0.0372 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8166 | 0.0498 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8102 | 0.0518 | 1.00 |
| flow_s0.5_uniform | 19.42 | 0.7885 | 0.0548 | 1.00 |
| flow_s1.0_oracle | 19.19 | 0.8296 | 0.0544 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| flow_s1.0_uniform | 18.45 | 0.7883 | 0.0601 | 1.00 |
| gs_tok448_nat_dil_al | 22.08 | 0.8029 | 0.0666 | 1.00 |
| gs_tok448_nat_dil_al+reg | 22.24 | 0.8093 | 0.0657 | 1.00 |
| gs_tok448_nat_dil_alv | 21.92 | 0.8022 | 0.0662 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 22.33 | 0.8137 | 0.0650 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 16.31 | 0.7494 | 0.1164 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 12.91 | 0.5112 | 0.2658 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 19.21 | 0.6669 | 0.1914 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 16.26 | 0.7495 | 0.1153 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.03 | 0.5775 | 0.2880 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 12.91 | 0.5112 | 0.2658 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 19.21 | 0.6669 | 0.1914 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 9.02 | 0.5760 | 0.2880 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.98 | 0.3159 | 0.3470 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 12.91 | 0.5112 | 0.2658 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 19.21 | 0.6669 | 0.1914 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.97 | 0.3153 | 0.3471 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.82 | 0.5235 | 0.3280 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 12.91 | 0.5112 | 0.2658 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 19.21 | 0.6669 | 0.1914 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.82 | 0.5222 | 0.3281 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 6.38 | 0.2916 | 0.3663 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 12.91 | 0.5112 | 0.2658 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 19.21 | 0.6669 | 0.1914 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 6.37 | 0.2907 | 0.3665 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 23.48 | 0.8551 | 0.0508 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 23.37 | 0.8542 | 0.0515 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 23.50 | 0.8558 | 0.0503 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 23.16 | 0.8521 | 0.0515 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 22.24 | 0.8068 | 0.0657 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 22.08 | 0.8005 | 0.0666 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 22.34 | 0.8112 | 0.0650 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 21.92 | 0.7998 | 0.0662 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 22.88 | 0.8495 | 0.0476 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 22.90 | 0.8501 | 0.0472 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 22.97 | 0.8513 | 0.0471 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 22.79 | 0.8493 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 23.04 | 0.8482 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 18.72 | 0.7411 | 0.1264 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 20.94 | 0.7709 | 0.1213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.16 | 0.8575 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 20.33 | 0.8040 | 0.0719 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 21.45 | 0.8034 | 0.0790 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 21.75 | 0.8528 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 19.86 | 0.8156 | 0.0627 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 20.57 | 0.8093 | 0.0702 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 21.87 | 0.8542 | 0.0429 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 19.96 | 0.8178 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.74 | 0.8112 | 0.0665 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 21.66 | 0.8537 | 0.0432 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 19.93 | 0.8216 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.59 | 0.8122 | 0.0648 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 22.49 | 0.8379 | 0.0539 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 18.87 | 0.7488 | 0.1086 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 20.67 | 0.7584 | 0.1160 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 22.58 | 0.8476 | 0.0483 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 19.95 | 0.7906 | 0.0795 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 21.07 | 0.7843 | 0.0874 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 21.45 | 0.8486 | 0.0467 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 19.72 | 0.8094 | 0.0673 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 20.35 | 0.7962 | 0.0764 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 21.62 | 0.8512 | 0.0447 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 19.82 | 0.8147 | 0.0628 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.52 | 0.7978 | 0.0722 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 21.44 | 0.8516 | 0.0447 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 19.85 | 0.8202 | 0.0600 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.38 | 0.8005 | 0.0699 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 21.59 | 0.7844 | 0.0777 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 16.99 | 0.6027 | 0.2104 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 19.45 | 0.6761 | 0.1811 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 21.49 | 0.7842 | 0.0771 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.77 | 0.8464 | 0.0490 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 19.88 | 0.7837 | 0.0826 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 20.96 | 0.7762 | 0.0916 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.70 | 0.8460 | 0.0488 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 21.64 | 0.8488 | 0.0463 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 19.78 | 0.8078 | 0.0678 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 20.42 | 0.7943 | 0.0776 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 21.56 | 0.8478 | 0.0464 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 21.81 | 0.8517 | 0.0444 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 19.85 | 0.8130 | 0.0637 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.60 | 0.7970 | 0.0726 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 21.72 | 0.8507 | 0.0444 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 21.64 | 0.8524 | 0.0441 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 19.92 | 0.8201 | 0.0599 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.47 | 0.8001 | 0.0699 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 21.54 | 0.8513 | 0.0441 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 21.31 | 0.7798 | 0.0790 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 16.99 | 0.6027 | 0.2104 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 19.63 | 0.6855 | 0.1760 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 21.48 | 0.7864 | 0.0778 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.74 | 0.8459 | 0.0487 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 19.88 | 0.7837 | 0.0826 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 20.96 | 0.7775 | 0.0888 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.46 | 0.8394 | 0.0497 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 21.64 | 0.8488 | 0.0463 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 19.78 | 0.8078 | 0.0678 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 20.42 | 0.7943 | 0.0776 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 21.36 | 0.8422 | 0.0472 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 21.80 | 0.8510 | 0.0445 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 19.85 | 0.8130 | 0.0637 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.60 | 0.7966 | 0.0724 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 21.70 | 0.8502 | 0.0444 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 21.64 | 0.8524 | 0.0441 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 19.92 | 0.8201 | 0.0599 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.47 | 0.8001 | 0.0699 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 21.54 | 0.8513 | 0.0441 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.88 | 0.8768 | 0.0597 | 1.00 |
| flow_s0.5_pose | 21.24 | 0.8722 | 0.0608 | 1.00 |
| flow_s0.5_uniform | 21.45 | 0.8596 | 0.0657 | 1.00 |
| flow_s1.0_oracle | 21.12 | 0.8872 | 0.0601 | 1.00 |
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| flow_s1.0_uniform | 20.48 | 0.8603 | 0.0677 | 1.00 |
| gs_tok448_nat_dil_al | 23.88 | 0.8592 | 0.0827 | 1.00 |
| gs_tok448_nat_dil_al+reg | 24.21 | 0.8644 | 0.0799 | 1.00 |
| gs_tok448_nat_dil_alv | 23.73 | 0.8586 | 0.0822 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 24.24 | 0.8665 | 0.0786 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 20.16 | 0.8259 | 0.1208 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 14.15 | 0.6371 | 0.3028 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 20.12 | 0.7136 | 0.2305 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 20.08 | 0.8255 | 0.1205 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.16 | 0.6155 | 0.3255 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 14.15 | 0.6371 | 0.3028 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 20.12 | 0.7136 | 0.2305 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.15 | 0.6144 | 0.3256 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.04 | 0.3295 | 0.3814 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 14.15 | 0.6371 | 0.3028 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 20.12 | 0.7136 | 0.2305 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.04 | 0.3292 | 0.3813 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.45 | 0.5756 | 0.3649 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 14.15 | 0.6371 | 0.3028 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 20.12 | 0.7136 | 0.2305 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.45 | 0.5747 | 0.3651 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.70 | 0.3088 | 0.4021 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 14.15 | 0.6371 | 0.3028 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 20.12 | 0.7136 | 0.2305 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.69 | 0.3082 | 0.4022 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 25.82 | 0.9046 | 0.0541 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 25.68 | 0.9039 | 0.0550 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 25.86 | 0.9050 | 0.0533 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 25.48 | 0.9027 | 0.0551 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 24.07 | 0.8763 | 0.0706 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 23.82 | 0.8720 | 0.0722 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 24.12 | 0.8781 | 0.0698 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 23.66 | 0.8710 | 0.0723 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 24.50 | 0.8980 | 0.0569 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 24.42 | 0.8977 | 0.0567 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 24.53 | 0.8985 | 0.0565 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 24.29 | 0.8966 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 25.35 | 0.9010 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 20.60 | 0.8364 | 0.1206 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 22.80 | 0.8498 | 0.1198 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.29 | 0.9043 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 22.26 | 0.8728 | 0.0763 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 23.38 | 0.8711 | 0.0826 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 23.72 | 0.9003 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.71 | 0.8797 | 0.0676 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.39 | 0.8749 | 0.0745 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 23.83 | 0.9007 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.87 | 0.8810 | 0.0645 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 22.59 | 0.8759 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 23.61 | 0.9005 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 21.81 | 0.8834 | 0.0625 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 22.42 | 0.8768 | 0.0698 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 24.85 | 0.8967 | 0.0564 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 20.80 | 0.8410 | 0.1077 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 22.51 | 0.8433 | 0.1147 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 24.80 | 0.9004 | 0.0520 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 21.87 | 0.8652 | 0.0823 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 22.95 | 0.8603 | 0.0894 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 23.39 | 0.8984 | 0.0519 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.53 | 0.8761 | 0.0711 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.10 | 0.8672 | 0.0795 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 23.54 | 0.8992 | 0.0507 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.70 | 0.8792 | 0.0667 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 22.31 | 0.8683 | 0.0758 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 23.34 | 0.8994 | 0.0508 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 21.70 | 0.8826 | 0.0641 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 22.16 | 0.8701 | 0.0738 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 24.24 | 0.8682 | 0.0732 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 18.93 | 0.7488 | 0.1971 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 20.99 | 0.7653 | 0.1869 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 24.08 | 0.8672 | 0.0732 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.06 | 0.9001 | 0.0525 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 21.84 | 0.8607 | 0.0855 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 22.85 | 0.8534 | 0.0944 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 24.97 | 0.8994 | 0.0526 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 23.61 | 0.8983 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.60 | 0.8747 | 0.0719 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.18 | 0.8649 | 0.0816 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 23.53 | 0.8976 | 0.0518 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 23.76 | 0.8996 | 0.0505 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.76 | 0.8784 | 0.0675 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 22.42 | 0.8679 | 0.0762 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 23.68 | 0.8989 | 0.0507 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 23.56 | 0.8998 | 0.0505 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 21.79 | 0.8826 | 0.0640 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 22.27 | 0.8698 | 0.0738 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 23.48 | 0.8990 | 0.0506 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 24.27 | 0.8671 | 0.0722 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 18.93 | 0.7488 | 0.1971 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 21.15 | 0.7714 | 0.1813 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 24.35 | 0.8702 | 0.0714 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 25.07 | 0.9000 | 0.0522 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 21.84 | 0.8607 | 0.0855 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 22.82 | 0.8536 | 0.0921 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 24.77 | 0.8964 | 0.0536 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 23.61 | 0.8983 | 0.0518 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.60 | 0.8747 | 0.0719 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.18 | 0.8649 | 0.0816 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 23.30 | 0.8948 | 0.0531 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 23.75 | 0.8990 | 0.0506 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.76 | 0.8784 | 0.0675 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 22.43 | 0.8677 | 0.0760 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 23.66 | 0.8986 | 0.0508 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 23.56 | 0.8998 | 0.0505 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 21.79 | 0.8826 | 0.0640 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 22.27 | 0.8698 | 0.0738 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 23.48 | 0.8990 | 0.0506 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.45 | 0.9592 | 0.0262 | 1.00 |
| flow_s0.5_pose | 32.82 | 0.9610 | 0.0252 | 1.00 |
| flow_s0.5_uniform | 32.06 | 0.9533 | 0.0285 | 1.00 |
| flow_s1.0_oracle | 33.41 | 0.9610 | 0.0236 | 1.00 |
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| flow_s1.0_uniform | 32.36 | 0.9509 | 0.0269 | 1.00 |
| gs_tok448_nat_dil_al | 29.15 | 0.9280 | 0.0541 | 1.00 |
| gs_tok448_nat_dil_al+reg | 29.44 | 0.9303 | 0.0516 | 1.00 |
| gs_tok448_nat_dil_alv | 29.28 | 0.9301 | 0.0537 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 29.36 | 0.9318 | 0.0509 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.23 | 0.8744 | 0.1114 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 16.30 | 0.7589 | 0.2807 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 24.65 | 0.8512 | 0.1620 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.24 | 0.8762 | 0.1106 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.50 | 0.6125 | 0.3604 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 16.30 | 0.7589 | 0.2807 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 24.65 | 0.8512 | 0.1620 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.50 | 0.6126 | 0.3604 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.28 | 0.3294 | 0.3958 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 16.30 | 0.7589 | 0.2807 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 24.65 | 0.8512 | 0.1620 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.28 | 0.3295 | 0.3958 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.16 | 0.5995 | 0.3928 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 16.30 | 0.7589 | 0.2807 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 24.65 | 0.8512 | 0.1620 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.16 | 0.5994 | 0.3929 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.08 | 0.3211 | 0.4149 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 16.30 | 0.7589 | 0.2807 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 24.65 | 0.8512 | 0.1620 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.08 | 0.3211 | 0.4149 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 33.53 | 0.9612 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 33.54 | 0.9614 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 33.53 | 0.9612 | 0.0235 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 33.48 | 0.9584 | 0.0239 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 33.45 | 0.9581 | 0.0243 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 33.48 | 0.9586 | 0.0238 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 33.46 | 0.9582 | 0.0242 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 33.49 | 0.9613 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 33.10 | 0.9595 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 33.45 | 0.9603 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 33.53 | 0.9616 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 33.40 | 0.9610 | 0.0246 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 33.44 | 0.9606 | 0.0258 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 33.45 | 0.9614 | 0.0241 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 33.51 | 0.9615 | 0.0242 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 33.45 | 0.9615 | 0.0240 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 33.51 | 0.9615 | 0.0242 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 33.52 | 0.9616 | 0.0239 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 33.52 | 0.9616 | 0.0239 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 32.24 | 0.9543 | 0.0318 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 29.52 | 0.9342 | 0.0872 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 29.50 | 0.9302 | 0.0876 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 32.24 | 0.9544 | 0.0315 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 33.49 | 0.9615 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 33.36 | 0.9609 | 0.0253 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 33.09 | 0.9598 | 0.0300 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 33.49 | 0.9615 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 33.37 | 0.9611 | 0.0249 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 33.21 | 0.9604 | 0.0274 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 33.48 | 0.9614 | 0.0244 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 33.48 | 0.9614 | 0.0244 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 32.33 | 0.9547 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 29.52 | 0.9342 | 0.0872 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 29.61 | 0.9317 | 0.0846 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 32.35 | 0.9551 | 0.0302 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 33.36 | 0.9609 | 0.0253 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 33.13 | 0.9599 | 0.0295 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 33.48 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 33.37 | 0.9611 | 0.0249 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 33.21 | 0.9604 | 0.0274 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 33.49 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 33.48 | 0.9614 | 0.0244 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 33.48 | 0.9614 | 0.0244 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_tok448_nat_dil_al | 25.02 | 0.8835 | 0.0937 | 1.00 |
| gs_tok448_nat_dil_al+reg | 25.37 | 0.8883 | 0.0925 | 1.00 |
| gs_tok448_nat_dil_alv | 24.92 | 0.8843 | 0.0933 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 25.39 | 0.8905 | 0.0917 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 19.06 | 0.8428 | 0.1534 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 14.48 | 0.6672 | 0.3678 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 21.70 | 0.7850 | 0.2610 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 19.03 | 0.8436 | 0.1528 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.45 | 0.6086 | 0.4190 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 14.48 | 0.6672 | 0.3678 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 21.70 | 0.7850 | 0.2610 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.45 | 0.6079 | 0.4191 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.84 | 0.3291 | 0.4895 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 14.48 | 0.6672 | 0.3678 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 21.70 | 0.7850 | 0.2610 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.84 | 0.3290 | 0.4894 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.89 | 0.5792 | 0.4695 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 14.48 | 0.6672 | 0.3678 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 21.70 | 0.7850 | 0.2610 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.89 | 0.5785 | 0.4695 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.52 | 0.3140 | 0.5127 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 14.48 | 0.6672 | 0.3678 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 21.70 | 0.7850 | 0.2610 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.52 | 0.3136 | 0.5126 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 27.18 | 0.9260 | 0.0563 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 27.04 | 0.9254 | 0.0568 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 27.22 | 0.9262 | 0.0557 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 26.86 | 0.9246 | 0.0568 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 25.45 | 0.9050 | 0.0745 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 25.19 | 0.9017 | 0.0753 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 25.50 | 0.9064 | 0.0741 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 25.05 | 0.9012 | 0.0752 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 25.93 | 0.9217 | 0.0589 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 25.87 | 0.9214 | 0.0587 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 25.96 | 0.9220 | 0.0584 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 25.75 | 0.9209 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 26.51 | 0.9230 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 22.33 | 0.8819 | 0.1341 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 24.53 | 0.8924 | 0.1260 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.57 | 0.9260 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 23.88 | 0.9057 | 0.0803 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 25.00 | 0.9050 | 0.0864 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 25.22 | 0.9240 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.40 | 0.9097 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 24.10 | 0.9071 | 0.0780 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 25.36 | 0.9243 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.52 | 0.9105 | 0.0682 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.29 | 0.9077 | 0.0747 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 25.15 | 0.9242 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.48 | 0.9119 | 0.0657 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 24.13 | 0.9082 | 0.0729 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 26.15 | 0.9204 | 0.0582 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 22.52 | 0.8853 | 0.1168 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 24.25 | 0.8879 | 0.1210 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 26.17 | 0.9235 | 0.0535 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 23.53 | 0.9005 | 0.0879 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.60 | 0.8977 | 0.0947 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 24.93 | 0.9225 | 0.0535 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.24 | 0.9069 | 0.0758 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 23.83 | 0.9016 | 0.0842 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 25.10 | 0.9232 | 0.0522 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.36 | 0.9091 | 0.0714 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.02 | 0.9021 | 0.0805 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 24.91 | 0.9233 | 0.0523 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.36 | 0.9111 | 0.0684 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.87 | 0.9031 | 0.0781 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 25.43 | 0.8992 | 0.0765 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 20.61 | 0.8171 | 0.2288 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 22.83 | 0.8390 | 0.2001 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.30 | 0.8988 | 0.0764 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.38 | 0.9233 | 0.0537 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 23.48 | 0.8978 | 0.0908 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.52 | 0.8936 | 0.0997 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.31 | 0.9229 | 0.0538 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.12 | 0.9225 | 0.0532 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.30 | 0.9060 | 0.0764 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 23.90 | 0.9001 | 0.0861 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 25.06 | 0.9221 | 0.0532 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.29 | 0.9234 | 0.0519 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.41 | 0.9085 | 0.0720 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.11 | 0.9017 | 0.0807 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.23 | 0.9230 | 0.0520 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.10 | 0.9235 | 0.0518 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.44 | 0.9110 | 0.0681 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.97 | 0.9028 | 0.0780 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 25.04 | 0.9231 | 0.0518 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.47 | 0.8993 | 0.0766 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 20.61 | 0.8171 | 0.2288 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 23.00 | 0.8433 | 0.1945 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.56 | 0.9013 | 0.0760 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.38 | 0.9232 | 0.0537 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 23.48 | 0.8978 | 0.0908 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.49 | 0.8938 | 0.0972 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.08 | 0.9205 | 0.0548 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.12 | 0.9225 | 0.0532 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.30 | 0.9060 | 0.0764 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 23.90 | 0.9001 | 0.0861 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 24.81 | 0.9198 | 0.0541 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.27 | 0.9231 | 0.0520 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.41 | 0.9085 | 0.0720 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.12 | 0.9015 | 0.0805 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.21 | 0.9228 | 0.0521 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.10 | 0.9235 | 0.0518 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.44 | 0.9110 | 0.0681 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.97 | 0.9028 | 0.0780 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 25.04 | 0.9231 | 0.0518 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：aligned_int → `gs_tok448_nat_dil_al`，aligned_vggt → `gs_tok448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=3.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 15.31 / 0.0249 | 30.29 / 0.0331 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |
| flow_s0.5_pose | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 | 27.45 / 0.0415 |
| gs_tok448_nat_dil_al | 18.34 / 0.1425 | 16.22 / 0.0340 | 27.18 / 0.0721 | 24.75 / 0.0885 |
| gs_tok448_nat_dil_al+reg | 18.92 / 0.1358 | 17.85 / 0.0282 | 28.30 / 0.0649 | 26.11 / 0.0849 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.85 / 0.1204 | 16.22 / 0.0340 | 31.44 / 0.0310 | 27.56 / 0.0479 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 20.53 / 0.0933 | 17.82 / 0.0226 | 31.45 / 0.0305 | 27.74 / 0.0434 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 20.53 / 0.1148 | 17.85 / 0.0282 | 31.46 / 0.0305 | 28.32 / 0.0461 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 20.77 / 0.0917 | 18.60 / 0.0218 | 31.45 / 0.0305 | 28.05 / 0.0429 |
| gs_tok448_nat_dil_alv | 17.74 / 0.1451 | 15.73 / 0.0355 | 27.12 / 0.0726 | 24.54 / 0.0890 |
| gs_tok448_nat_dil_alv+reg | 18.69 / 0.1366 | 17.81 / 0.0278 | 28.30 / 0.0650 | 26.10 / 0.0851 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 19.26 / 0.1208 | 15.73 / 0.0355 | 31.43 / 0.0310 | 27.22 / 0.0486 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 20.03 / 0.0984 | 17.42 / 0.0235 | 31.46 / 0.0305 | 27.47 / 0.0438 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 20.30 / 0.1152 | 17.81 / 0.0278 | 31.46 / 0.0305 | 28.29 / 0.0456 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 20.58 / 0.0925 | 18.52 / 0.0217 | 31.46 / 0.0305 | 28.00 / 0.0427 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_tok448_nat_dil_al | 18.34 | 0.6756 | 0.1425 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.92 | 0.7130 | 0.1358 | 1.00 |
| gs_tok448_nat_dil_alv | 17.74 | 0.6614 | 0.1451 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.69 | 0.7121 | 0.1366 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.82 | 0.6527 | 0.1707 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 11.09 | 0.3765 | 0.4295 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 17.11 | 0.5557 | 0.4048 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.26 | 0.6385 | 0.1733 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.69 | 0.5858 | 0.2755 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 11.09 | 0.3765 | 0.4295 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 17.11 | 0.5557 | 0.4048 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 14.14 | 0.5674 | 0.2796 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 11.49 | 0.3627 | 0.3984 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 11.09 | 0.3765 | 0.4295 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 17.11 | 0.5557 | 0.4048 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 10.97 | 0.3471 | 0.4021 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 13.13 | 0.4857 | 0.3296 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 11.09 | 0.3765 | 0.4295 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 17.11 | 0.5557 | 0.4048 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 12.66 | 0.4667 | 0.3354 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 7.36 | 0.1812 | 0.5314 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 11.09 | 0.3765 | 0.4295 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 17.11 | 0.5557 | 0.4048 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 7.08 | 0.1707 | 0.5328 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 20.53 | 0.7634 | 0.1148 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.85 | 0.7420 | 0.1204 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 20.30 | 0.7587 | 0.1152 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 19.26 | 0.7262 | 0.1208 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 19.31 | 0.7326 | 0.1254 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 18.79 | 0.7053 | 0.1329 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 19.07 | 0.7307 | 0.1254 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 18.19 | 0.6893 | 0.1354 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 20.77 | 0.7782 | 0.0917 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 20.53 | 0.7694 | 0.0933 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 20.58 | 0.7768 | 0.0925 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 20.03 | 0.7562 | 0.0984 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 18.96 | 0.7285 | 0.1263 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 15.74 | 0.5654 | 0.3122 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 19.13 | 0.6926 | 0.2777 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.61 | 0.7684 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 18.75 | 0.7038 | 0.1674 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 20.35 | 0.7390 | 0.1712 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 20.80 | 0.7700 | 0.0757 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 19.09 | 0.7200 | 0.1359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 20.34 | 0.7357 | 0.1555 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 20.78 | 0.7703 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 19.25 | 0.7263 | 0.1361 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.49 | 0.7517 | 0.1377 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 21.10 | 0.7754 | 0.0662 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 20.42 | 0.7554 | 0.0924 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.78 | 0.7538 | 0.1144 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 19.98 | 0.7485 | 0.0874 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 18.03 | 0.6840 | 0.1794 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 20.05 | 0.7263 | 0.1764 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 20.24 | 0.7534 | 0.0835 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 18.80 | 0.7046 | 0.1554 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 20.26 | 0.7311 | 0.1596 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 20.45 | 0.7577 | 0.0797 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 19.00 | 0.7158 | 0.1353 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 20.28 | 0.7291 | 0.1556 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 20.56 | 0.7602 | 0.0736 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 19.21 | 0.7249 | 0.1291 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.35 | 0.7404 | 0.1359 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 20.99 | 0.7714 | 0.0655 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 20.43 | 0.7571 | 0.0874 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.75 | 0.7524 | 0.1089 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 18.20 | 0.6790 | 0.1569 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 14.81 | 0.4818 | 0.3657 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 17.82 | 0.6022 | 0.3671 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.66 | 0.6625 | 0.1590 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.21 | 0.7538 | 0.0903 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 18.36 | 0.6796 | 0.1838 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 19.82 | 0.7048 | 0.2124 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 19.87 | 0.7434 | 0.0938 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 20.47 | 0.7572 | 0.0837 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 18.73 | 0.6981 | 0.1495 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 19.85 | 0.7046 | 0.1924 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 20.14 | 0.7486 | 0.0861 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 20.56 | 0.7621 | 0.0780 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 18.91 | 0.7130 | 0.1457 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.27 | 0.7340 | 0.1572 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 20.28 | 0.7550 | 0.0817 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 21.09 | 0.7748 | 0.0664 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 20.42 | 0.7553 | 0.0918 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.74 | 0.7496 | 0.1168 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 20.90 | 0.7683 | 0.0680 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 18.25 | 0.6915 | 0.1510 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 14.81 | 0.4818 | 0.3657 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 18.83 | 0.6425 | 0.3116 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.97 | 0.6856 | 0.1532 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 20.19 | 0.7522 | 0.0914 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 18.36 | 0.6796 | 0.1838 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 19.82 | 0.7048 | 0.2124 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 19.82 | 0.7439 | 0.0934 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 20.44 | 0.7559 | 0.0857 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 18.73 | 0.6981 | 0.1495 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 19.85 | 0.7046 | 0.1924 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 20.10 | 0.7471 | 0.0875 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 20.39 | 0.7563 | 0.0787 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 18.91 | 0.7130 | 0.1457 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 20.27 | 0.7340 | 0.1572 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 20.16 | 0.7462 | 0.0834 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 21.09 | 0.7748 | 0.0664 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 20.42 | 0.7553 | 0.0918 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 20.74 | 0.7496 | 0.1168 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 20.90 | 0.7683 | 0.0680 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.18 | 0.7600 | 0.0171 | 1.00 |
| flow_s0.5_pose | 17.06 | 0.6711 | 0.0195 | 1.00 |
| flow_s0.5_uniform | 15.30 | 0.5755 | 0.0247 | 1.00 |
| flow_s1.0_oracle | 19.73 | 0.7659 | 0.0154 | 1.00 |
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| flow_s1.0_uniform | 15.31 | 0.5619 | 0.0249 | 1.00 |
| gs_tok448_nat_dil_al | 16.22 | 0.6207 | 0.0340 | 1.00 |
| gs_tok448_nat_dil_al+reg | 17.85 | 0.6883 | 0.0282 | 1.00 |
| gs_tok448_nat_dil_alv | 15.73 | 0.5983 | 0.0355 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 17.81 | 0.6896 | 0.0278 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 15.64 | 0.5976 | 0.0405 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 9.83 | 0.3314 | 0.0900 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 16.02 | 0.5707 | 0.0614 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 15.24 | 0.5749 | 0.0419 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.38 | 0.3968 | 0.0958 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 9.83 | 0.3314 | 0.0900 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 16.02 | 0.5707 | 0.0614 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 10.22 | 0.3758 | 0.0968 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 8.05 | 0.2617 | 0.1301 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 9.83 | 0.3314 | 0.0900 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 16.02 | 0.5707 | 0.0614 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 7.89 | 0.2431 | 0.1311 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 9.06 | 0.3210 | 0.1180 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 9.83 | 0.3314 | 0.0900 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 16.02 | 0.5707 | 0.0614 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 8.93 | 0.3004 | 0.1187 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.39 | 0.1214 | 0.1548 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 9.83 | 0.3314 | 0.0900 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 16.02 | 0.5707 | 0.0614 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.34 | 0.1123 | 0.1550 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 17.85 | 0.6862 | 0.0282 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 16.22 | 0.6159 | 0.0340 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 17.81 | 0.6875 | 0.0278 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 15.73 | 0.5929 | 0.0355 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 18.09 | 0.6993 | 0.0269 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 16.78 | 0.6502 | 0.0302 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 18.01 | 0.6993 | 0.0267 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 16.31 | 0.6301 | 0.0312 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 18.60 | 0.7194 | 0.0218 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.82 | 0.6930 | 0.0226 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 18.52 | 0.7189 | 0.0217 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 17.42 | 0.6764 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 16.65 | 0.6406 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 13.34 | 0.4690 | 0.0573 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 16.54 | 0.6000 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.90 | 0.6951 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 16.08 | 0.6197 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 17.57 | 0.6602 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 17.95 | 0.6921 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 16.20 | 0.6209 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 17.53 | 0.6566 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 17.94 | 0.6927 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 16.35 | 0.6364 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 17.69 | 0.6666 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 18.15 | 0.6985 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 17.57 | 0.6766 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 17.89 | 0.6761 | 0.0236 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 17.66 | 0.6752 | 0.0218 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 15.45 | 0.5918 | 0.0329 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 17.40 | 0.6460 | 0.0361 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 17.82 | 0.6874 | 0.0202 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 16.19 | 0.6239 | 0.0271 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 17.61 | 0.6597 | 0.0315 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 17.88 | 0.6861 | 0.0198 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 16.24 | 0.6236 | 0.0261 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 17.55 | 0.6550 | 0.0310 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 17.88 | 0.6879 | 0.0188 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 16.41 | 0.6400 | 0.0241 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 17.64 | 0.6621 | 0.0279 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 18.08 | 0.6944 | 0.0175 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 17.57 | 0.6774 | 0.0203 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 17.86 | 0.6736 | 0.0231 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 16.63 | 0.6365 | 0.0315 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 13.31 | 0.4631 | 0.0579 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 16.53 | 0.5957 | 0.0567 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 16.20 | 0.6154 | 0.0327 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.91 | 0.6932 | 0.0206 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 16.05 | 0.6163 | 0.0288 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 17.58 | 0.6593 | 0.0344 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.57 | 0.6773 | 0.0214 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 17.96 | 0.6907 | 0.0199 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 16.18 | 0.6178 | 0.0269 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 17.54 | 0.6559 | 0.0320 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 17.63 | 0.6761 | 0.0207 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 17.94 | 0.6918 | 0.0190 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 16.34 | 0.6355 | 0.0249 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 17.69 | 0.6661 | 0.0285 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 17.69 | 0.6813 | 0.0194 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 18.15 | 0.6986 | 0.0175 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 17.57 | 0.6765 | 0.0206 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 17.89 | 0.6760 | 0.0236 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 18.01 | 0.6923 | 0.0177 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.40 | 0.6688 | 0.0295 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 13.31 | 0.4631 | 0.0579 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 17.50 | 0.6439 | 0.0471 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.09 | 0.6559 | 0.0302 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 18.21 | 0.7064 | 0.0200 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 16.05 | 0.6163 | 0.0288 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 17.58 | 0.6593 | 0.0344 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 18.06 | 0.7037 | 0.0200 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 18.24 | 0.7024 | 0.0193 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 16.18 | 0.6178 | 0.0269 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 17.54 | 0.6559 | 0.0320 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 18.07 | 0.6982 | 0.0192 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 18.18 | 0.6985 | 0.0183 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 16.34 | 0.6355 | 0.0249 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 17.69 | 0.6661 | 0.0285 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 18.11 | 0.6953 | 0.0183 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 18.15 | 0.6986 | 0.0175 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 17.57 | 0.6765 | 0.0206 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 17.89 | 0.6760 | 0.0236 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 18.01 | 0.6923 | 0.0177 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.73 | 0.8826 | 0.0204 | 1.00 |
| flow_s0.5_pose | 22.21 | 0.8504 | 0.0224 | 1.00 |
| flow_s0.5_uniform | 20.55 | 0.8064 | 0.0266 | 1.00 |
| flow_s1.0_oracle | 24.76 | 0.8987 | 0.0188 | 1.00 |
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| flow_s1.0_uniform | 20.86 | 0.8093 | 0.0253 | 1.00 |
| gs_tok448_nat_dil_al | 20.19 | 0.7468 | 0.0465 | 1.00 |
| gs_tok448_nat_dil_al+reg | 21.53 | 0.7929 | 0.0402 | 1.00 |
| gs_tok448_nat_dil_alv | 19.89 | 0.7395 | 0.0470 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 21.49 | 0.7937 | 0.0400 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.54 | 0.7096 | 0.0649 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 13.74 | 0.5426 | 0.1502 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 19.63 | 0.6908 | 0.1007 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.33 | 0.7027 | 0.0652 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.04 | 0.4789 | 0.2191 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 13.74 | 0.5426 | 0.1502 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 19.63 | 0.6908 | 0.1007 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.01 | 0.4719 | 0.2194 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.77 | 0.2822 | 0.2459 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 13.74 | 0.5426 | 0.1502 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 19.63 | 0.6908 | 0.1007 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.75 | 0.2759 | 0.2464 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.45 | 0.3845 | 0.2364 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 13.74 | 0.5426 | 0.1502 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 19.63 | 0.6908 | 0.1007 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.42 | 0.3776 | 0.2368 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.44 | 0.1373 | 0.2724 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 13.74 | 0.5426 | 0.1502 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 19.63 | 0.6908 | 0.1007 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.43 | 0.1336 | 0.2727 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 23.66 | 0.8659 | 0.0257 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 22.60 | 0.8504 | 0.0278 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 23.60 | 0.8656 | 0.0254 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 22.20 | 0.8434 | 0.0281 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 21.53 | 0.7924 | 0.0402 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 20.19 | 0.7470 | 0.0465 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 21.49 | 0.7931 | 0.0400 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 19.89 | 0.7397 | 0.0470 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 23.32 | 0.8610 | 0.0251 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 22.73 | 0.8497 | 0.0256 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 23.26 | 0.8611 | 0.0251 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 22.39 | 0.8439 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 21.96 | 0.8386 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 19.02 | 0.7765 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 21.88 | 0.8153 | 0.0581 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.23 | 0.8668 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 21.67 | 0.8457 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 22.93 | 0.8496 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 23.31 | 0.8664 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.83 | 0.8477 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.92 | 0.8501 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 23.34 | 0.8684 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.97 | 0.8525 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 23.10 | 0.8566 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 23.61 | 0.8723 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.12 | 0.8661 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.35 | 0.8620 | 0.0267 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 22.25 | 0.8355 | 0.0270 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 20.81 | 0.8129 | 0.0392 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 22.31 | 0.8233 | 0.0449 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 22.56 | 0.8501 | 0.0247 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 21.70 | 0.8393 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 22.70 | 0.8376 | 0.0385 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 22.95 | 0.8570 | 0.0234 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.76 | 0.8423 | 0.0291 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.81 | 0.8421 | 0.0369 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 23.14 | 0.8627 | 0.0217 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.94 | 0.8495 | 0.0272 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 22.95 | 0.8491 | 0.0328 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 23.51 | 0.8700 | 0.0209 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.11 | 0.8656 | 0.0229 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.31 | 0.8595 | 0.0271 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 20.00 | 0.7366 | 0.0475 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 17.27 | 0.6280 | 0.1081 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 20.06 | 0.7089 | 0.0942 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 19.73 | 0.7296 | 0.0475 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.55 | 0.8493 | 0.0256 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 21.45 | 0.8319 | 0.0336 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 22.45 | 0.8285 | 0.0432 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.30 | 0.8440 | 0.0255 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 22.96 | 0.8565 | 0.0238 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.64 | 0.8377 | 0.0306 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.66 | 0.8366 | 0.0392 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 22.70 | 0.8516 | 0.0238 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 23.14 | 0.8625 | 0.0223 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.81 | 0.8468 | 0.0285 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 22.92 | 0.8476 | 0.0340 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 22.93 | 0.8587 | 0.0225 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 23.56 | 0.8710 | 0.0210 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.10 | 0.8653 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.31 | 0.8593 | 0.0277 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 23.43 | 0.8684 | 0.0212 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 20.72 | 0.7650 | 0.0438 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 17.27 | 0.6280 | 0.1081 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 21.31 | 0.7616 | 0.0780 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 20.57 | 0.7643 | 0.0438 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.75 | 0.8536 | 0.0255 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 21.45 | 0.8319 | 0.0336 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 22.45 | 0.8285 | 0.0432 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.60 | 0.8515 | 0.0256 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 23.14 | 0.8601 | 0.0238 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 21.64 | 0.8377 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 22.66 | 0.8366 | 0.0392 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 22.96 | 0.8575 | 0.0239 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 23.31 | 0.8642 | 0.0220 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 21.81 | 0.8468 | 0.0285 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 22.92 | 0.8476 | 0.0340 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 23.16 | 0.8612 | 0.0223 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 23.56 | 0.8710 | 0.0210 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 23.10 | 0.8653 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 23.31 | 0.8593 | 0.0277 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 23.43 | 0.8684 | 0.0212 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.73 | 0.9248 | 0.0355 | 1.00 |
| flow_s0.5_pose | 24.65 | 0.9099 | 0.0374 | 1.00 |
| flow_s0.5_uniform | 23.02 | 0.8845 | 0.0430 | 1.00 |
| flow_s1.0_oracle | 26.44 | 0.9323 | 0.0341 | 1.00 |
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| flow_s1.0_uniform | 23.35 | 0.8857 | 0.0419 | 1.00 |
| gs_tok448_nat_dil_al | 22.34 | 0.8274 | 0.0676 | 1.00 |
| gs_tok448_nat_dil_al+reg | 23.78 | 0.8603 | 0.0579 | 1.00 |
| gs_tok448_nat_dil_alv | 22.06 | 0.8231 | 0.0685 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 23.79 | 0.8609 | 0.0573 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 13.18 | 0.7520 | 0.1488 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 15.71 | 0.6977 | 0.1921 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 20.94 | 0.7584 | 0.1466 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 13.15 | 0.7477 | 0.1496 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.59 | 0.5570 | 0.3038 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 15.71 | 0.6977 | 0.1921 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 20.94 | 0.7584 | 0.1466 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.58 | 0.5528 | 0.3043 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.78 | 0.3041 | 0.3463 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 15.71 | 0.6977 | 0.1921 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 20.94 | 0.7584 | 0.1466 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.77 | 0.3002 | 0.3468 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.56 | 0.4211 | 0.3331 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 15.71 | 0.6977 | 0.1921 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 20.94 | 0.7584 | 0.1466 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.55 | 0.4169 | 0.3336 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.53 | 0.1495 | 0.3818 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 15.71 | 0.6977 | 0.1921 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 20.94 | 0.7584 | 0.1466 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.53 | 0.1473 | 0.3820 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 25.81 | 0.9170 | 0.0402 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 24.86 | 0.9096 | 0.0422 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 25.77 | 0.9171 | 0.0397 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 24.46 | 0.9060 | 0.0432 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 24.41 | 0.8914 | 0.0481 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 23.26 | 0.8737 | 0.0528 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 24.36 | 0.8913 | 0.0475 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 22.95 | 0.8694 | 0.0535 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 25.36 | 0.9146 | 0.0386 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 24.90 | 0.9099 | 0.0393 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 25.30 | 0.9145 | 0.0384 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 24.58 | 0.9068 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 24.43 | 0.9069 | 0.0421 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 21.66 | 0.8793 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 24.18 | 0.8897 | 0.0672 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.29 | 0.9183 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 23.80 | 0.9081 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.97 | 0.9064 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 25.38 | 0.9177 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.91 | 0.9081 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 24.97 | 0.9068 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 25.36 | 0.9187 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 24.07 | 0.9110 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 25.13 | 0.9111 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 25.67 | 0.9203 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 25.23 | 0.9167 | 0.0384 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 25.43 | 0.9138 | 0.0412 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 24.74 | 0.9078 | 0.0390 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 23.02 | 0.8931 | 0.0503 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 24.57 | 0.8955 | 0.0555 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 24.99 | 0.9139 | 0.0374 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 23.76 | 0.9054 | 0.0436 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.88 | 0.9026 | 0.0501 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 25.11 | 0.9141 | 0.0372 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.85 | 0.9060 | 0.0429 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 24.84 | 0.9024 | 0.0496 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 25.22 | 0.9165 | 0.0365 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 24.01 | 0.9094 | 0.0410 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.99 | 0.9067 | 0.0462 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 25.59 | 0.9192 | 0.0360 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 25.23 | 0.9166 | 0.0380 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 25.41 | 0.9126 | 0.0418 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 22.98 | 0.8656 | 0.0544 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 19.96 | 0.8141 | 0.0973 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 22.32 | 0.8254 | 0.1046 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 22.68 | 0.8612 | 0.0551 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.98 | 0.9135 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 23.61 | 0.9024 | 0.0458 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.49 | 0.8950 | 0.0551 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 24.70 | 0.9103 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.11 | 0.9139 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.77 | 0.9039 | 0.0439 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 24.55 | 0.8969 | 0.0524 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 24.84 | 0.9110 | 0.0377 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.21 | 0.9168 | 0.0368 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.97 | 0.9088 | 0.0417 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.84 | 0.9045 | 0.0476 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.01 | 0.9146 | 0.0370 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.64 | 0.9197 | 0.0360 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 25.22 | 0.9164 | 0.0384 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 25.39 | 0.9120 | 0.0425 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 25.53 | 0.9182 | 0.0361 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 23.77 | 0.8796 | 0.0508 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 19.96 | 0.8141 | 0.0973 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 23.23 | 0.8467 | 0.0900 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 23.55 | 0.8782 | 0.0515 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 25.25 | 0.9159 | 0.0381 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 23.61 | 0.9024 | 0.0458 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 24.49 | 0.8950 | 0.0551 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 25.12 | 0.9147 | 0.0379 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.34 | 0.9157 | 0.0373 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 23.77 | 0.9039 | 0.0439 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 24.55 | 0.8969 | 0.0524 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 25.20 | 0.9142 | 0.0372 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.43 | 0.9173 | 0.0367 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 23.97 | 0.9088 | 0.0417 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 24.84 | 0.9045 | 0.0476 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.33 | 0.9157 | 0.0366 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.64 | 0.9197 | 0.0360 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 25.22 | 0.9164 | 0.0384 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 25.39 | 0.9120 | 0.0425 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 25.53 | 0.9182 | 0.0361 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.41 | 0.9667 | 0.0317 | 1.00 |
| flow_s0.5_pose | 31.22 | 0.9653 | 0.0318 | 1.00 |
| flow_s0.5_uniform | 30.53 | 0.9607 | 0.0346 | 1.00 |
| flow_s1.0_oracle | 31.56 | 0.9661 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| flow_s1.0_uniform | 30.29 | 0.9592 | 0.0331 | 1.00 |
| gs_tok448_nat_dil_al | 27.18 | 0.9123 | 0.0721 | 1.00 |
| gs_tok448_nat_dil_al+reg | 28.30 | 0.9257 | 0.0649 | 1.00 |
| gs_tok448_nat_dil_alv | 27.12 | 0.9123 | 0.0726 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 28.30 | 0.9257 | 0.0650 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 10.98 | 0.7622 | 0.2332 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 17.26 | 0.7903 | 0.2828 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 25.77 | 0.8937 | 0.1431 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 10.98 | 0.7623 | 0.2333 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.33 | 0.5811 | 0.4327 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 17.26 | 0.7903 | 0.2828 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 25.77 | 0.8937 | 0.1431 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.33 | 0.5809 | 0.4327 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.02 | 0.3103 | 0.4579 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 17.26 | 0.7903 | 0.2828 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 25.77 | 0.8937 | 0.1431 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.02 | 0.3100 | 0.4579 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 5.49 | 0.4362 | 0.4560 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 17.26 | 0.7903 | 0.2828 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 25.77 | 0.8937 | 0.1431 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 5.49 | 0.4360 | 0.4561 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.08 | 0.1562 | 0.4897 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 17.26 | 0.7903 | 0.2828 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 25.77 | 0.8937 | 0.1431 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.08 | 0.1561 | 0.4898 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 31.46 | 0.9642 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 31.44 | 0.9636 | 0.0310 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 31.46 | 0.9643 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 31.43 | 0.9634 | 0.0310 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 31.40 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 31.35 | 0.9615 | 0.0323 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 31.40 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 31.35 | 0.9614 | 0.0323 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 31.35 | 0.9640 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 31.10 | 0.9631 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 31.32 | 0.9631 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 31.44 | 0.9646 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 31.44 | 0.9646 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 31.44 | 0.9647 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 31.44 | 0.9646 | 0.0307 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 31.38 | 0.9641 | 0.0327 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 31.39 | 0.9643 | 0.0326 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 31.39 | 0.9643 | 0.0326 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 31.40 | 0.9644 | 0.0324 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 31.45 | 0.9647 | 0.0311 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 30.24 | 0.9566 | 0.0405 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 28.93 | 0.9499 | 0.0640 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 29.34 | 0.9479 | 0.0692 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 30.11 | 0.9564 | 0.0405 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.35 | 0.9643 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 31.28 | 0.9644 | 0.0318 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 30.81 | 0.9627 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 31.36 | 0.9643 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 31.37 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 31.30 | 0.9646 | 0.0310 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 30.81 | 0.9630 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 31.38 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 31.43 | 0.9648 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 31.41 | 0.9649 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 31.04 | 0.9637 | 0.0344 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 31.44 | 0.9648 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 31.44 | 0.9645 | 0.0318 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 30.62 | 0.9587 | 0.0365 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 28.93 | 0.9499 | 0.0640 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 29.72 | 0.9515 | 0.0602 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 30.57 | 0.9587 | 0.0365 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 31.34 | 0.9644 | 0.0312 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 31.28 | 0.9644 | 0.0318 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 30.81 | 0.9627 | 0.0378 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 31.34 | 0.9644 | 0.0311 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 31.36 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 31.30 | 0.9646 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 30.81 | 0.9630 | 0.0371 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 31.36 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 31.40 | 0.9648 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 31.41 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 31.04 | 0.9637 | 0.0344 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 31.41 | 0.9648 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 31.44 | 0.9645 | 0.0318 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_tok448_nat_dil_al | 24.75 | 0.8845 | 0.0885 | 1.00 |
| gs_tok448_nat_dil_al+reg | 26.11 | 0.9035 | 0.0849 | 1.00 |
| gs_tok448_nat_dil_alv | 24.54 | 0.8828 | 0.0890 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 26.10 | 0.9035 | 0.0851 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 11.59 | 0.7561 | 0.2493 | 1.00 |
| gs_tokr5448_nat_dil_al_rpgs_local | 16.31 | 0.7512 | 0.3210 | 1.00 |
| gs_tokr5448_nat_dil_al_rpvggt_local | 23.84 | 0.8615 | 0.1839 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 11.58 | 0.7545 | 0.2494 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.65 | 0.5677 | 0.4860 | 1.00 |
| gs_tokrife448_nat_dil_al_rpgs_local | 16.31 | 0.7512 | 0.3210 | 1.00 |
| gs_tokrife448_nat_dil_al_rpvggt_local | 23.84 | 0.8615 | 0.1839 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.64 | 0.5660 | 0.4863 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.26 | 0.3066 | 0.5303 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpgs_local | 16.31 | 0.7512 | 0.3210 | 1.00 |
| gs_tokrife_g448_nat_dil_al_rpvggt_local | 23.84 | 0.8615 | 0.1839 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.26 | 0.3050 | 0.5305 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 5.79 | 0.4278 | 0.5213 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpgs_local | 16.31 | 0.7512 | 0.3210 | 1.00 |
| gs_tokstrict448_nat_dil_al_rpvggt_local | 23.84 | 0.8615 | 0.1839 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 5.79 | 0.4262 | 0.5215 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.24 | 0.1530 | 0.5770 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpgs_local | 16.31 | 0.7512 | 0.3210 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_rpvggt_local | 23.84 | 0.8615 | 0.1839 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.24 | 0.1520 | 0.5771 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 28.32 | 0.9471 | 0.0461 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 27.56 | 0.9436 | 0.0479 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 28.29 | 0.9472 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 27.22 | 0.9420 | 0.0486 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 27.20 | 0.9347 | 0.0549 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 26.30 | 0.9273 | 0.0579 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 27.17 | 0.9347 | 0.0547 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 26.04 | 0.9258 | 0.0583 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 28.05 | 0.9471 | 0.0429 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 27.74 | 0.9455 | 0.0434 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 28.00 | 0.9470 | 0.0427 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 27.47 | 0.9444 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 27.36 | 0.9434 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpgs_local] | 25.05 | 0.9322 | 0.0685 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_rpvggt_local] | 27.28 | 0.9375 | 0.0743 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.96 | 0.9484 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpgs_local] | 26.73 | 0.9444 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_rpvggt_local] | 27.79 | 0.9441 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 28.01 | 0.9482 | 0.0402 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpgs_local] | 26.86 | 0.9447 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 27.76 | 0.9442 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 28.05 | 0.9486 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpgs_local] | 26.98 | 0.9456 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_rpvggt_local] | 27.89 | 0.9458 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 28.26 | 0.9491 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 27.97 | 0.9477 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 28.11 | 0.9466 | 0.0453 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 27.59 | 0.9446 | 0.0426 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpgs_local] | 26.28 | 0.9395 | 0.0553 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_rpvggt_local] | 27.50 | 0.9402 | 0.0602 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 27.74 | 0.9469 | 0.0408 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpgs_local] | 26.75 | 0.9438 | 0.0480 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_rpvggt_local] | 27.68 | 0.9427 | 0.0546 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 27.81 | 0.9470 | 0.0406 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpgs_local] | 26.82 | 0.9441 | 0.0470 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 27.66 | 0.9426 | 0.0540 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 27.94 | 0.9478 | 0.0401 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpgs_local] | 26.98 | 0.9453 | 0.0453 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_rpvggt_local] | 27.77 | 0.9442 | 0.0506 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 28.21 | 0.9486 | 0.0395 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 27.96 | 0.9476 | 0.0421 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 28.09 | 0.9460 | 0.0460 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 26.01 | 0.9231 | 0.0597 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpgs_local] | 23.48 | 0.8998 | 0.1245 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_rpvggt_local] | 25.65 | 0.9093 | 0.1164 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.75 | 0.9214 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.71 | 0.9466 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpgs_local] | 26.54 | 0.9423 | 0.0513 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_rpvggt_local] | 27.39 | 0.9398 | 0.0608 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.50 | 0.9454 | 0.0420 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 27.78 | 0.9468 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpgs_local] | 26.70 | 0.9431 | 0.0483 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 27.40 | 0.9404 | 0.0574 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 27.59 | 0.9457 | 0.0412 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 27.92 | 0.9478 | 0.0406 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpgs_local] | 26.86 | 0.9448 | 0.0464 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_rpvggt_local] | 27.66 | 0.9434 | 0.0523 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 27.78 | 0.9470 | 0.0408 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 28.24 | 0.9488 | 0.0396 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 27.96 | 0.9475 | 0.0425 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 28.08 | 0.9458 | 0.0468 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 28.17 | 0.9482 | 0.0398 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 26.66 | 0.9289 | 0.0579 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpgs_local] | 23.48 | 0.8998 | 0.1245 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_rpvggt_local] | 26.39 | 0.9197 | 0.1021 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 26.49 | 0.9285 | 0.0588 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.90 | 0.9473 | 0.0418 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpgs_local] | 26.54 | 0.9423 | 0.0513 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_rpvggt_local] | 27.39 | 0.9398 | 0.0608 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.81 | 0.9467 | 0.0416 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 27.96 | 0.9474 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpgs_local] | 26.70 | 0.9431 | 0.0483 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_rpvggt_local] | 27.40 | 0.9404 | 0.0574 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 27.87 | 0.9467 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 28.05 | 0.9479 | 0.0404 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpgs_local] | 26.86 | 0.9448 | 0.0464 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_rpvggt_local] | 27.66 | 0.9434 | 0.0523 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 27.98 | 0.9472 | 0.0403 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 28.24 | 0.9488 | 0.0396 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpgs_local] | 27.96 | 0.9475 | 0.0425 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_rpvggt_local] | 28.08 | 0.9458 | 0.0468 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 28.17 | 0.9482 | 0.0398 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_tok448_nat_dil_al | 0.45 | 0.50 |
| cam3 | gs_tok448_nat_dil_alv | 0.51 | 0.67 |
| cam5 | gs_tok448_nat_dil_al | 1.32 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv | 1.46 | 1.00 |

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
| cam3 | gs_tok448_nat_dil_al | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 42.9 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tok448_nat_dil_alv | aligned_vggt | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 26.8 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokr5448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 74.1 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokr5448_nat_dil_al_rpgs_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 955.2 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokr5448_nat_dil_al_rpvggt_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 966.0 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 48.2 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 64.4 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_rpgs_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 955.2 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al_rpvggt_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 966.0 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 73.9 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife_g448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 33.9 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife_g448_nat_dil_al_rpgs_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 955.2 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife_g448_nat_dil_al_rpvggt_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 966.0 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokrife_g448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 36.0 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 64.9 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict448_nat_dil_al_rpgs_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 955.2 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict448_nat_dil_al_rpvggt_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 966.0 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 49.8 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict_g448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 50.1 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict_g448_nat_dil_al_rpgs_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 955.2 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict_g448_nat_dil_al_rpvggt_local | aligned_int | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 966.0 | 29.14 | 0.33 | 0.011 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368197 | 0.842 | 35.8 | 29.14 | 0.33 | 0.011 |
| cam5 | gs_tok448_nat_dil_al | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 30.0 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tok448_nat_dil_alv | aligned_vggt | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 24.0 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokr5448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 42.9 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokr5448_nat_dil_al_rpgs_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 1188.0 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokr5448_nat_dil_al_rpvggt_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 972.9 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 45.1 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 42.3 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_al_rpgs_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 1188.0 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_al_rpvggt_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 972.9 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 43.3 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife_g448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 34.7 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife_g448_nat_dil_al_rpgs_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 1188.0 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife_g448_nat_dil_al_rpvggt_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 972.9 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokrife_g448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 35.2 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 43.1 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict448_nat_dil_al_rpgs_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 1188.0 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict448_nat_dil_al_rpvggt_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 972.9 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 40.6 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict_g448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 30.5 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict_g448_nat_dil_al_rpgs_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 1188.0 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict_g448_nat_dil_al_rpvggt_local | aligned_int | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 972.9 | 29.46 | 0.12 | 0.008 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 528829 | 0.524 | 31.1 | 29.46 | 0.12 | 0.008 |

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
