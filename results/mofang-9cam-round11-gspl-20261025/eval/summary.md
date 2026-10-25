# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_tokr5448_nat_dil_al_local | 37.9% | 19.08 / 0.0547 | 22.02 / 0.0759 | 22.07 / 0.0738 | 0.58 |
| cam3 | gs_tokr5448_nat_dil_al_tto100_local | 40.2% | 19.28 / 0.0562 | 24.19 / 0.0545 | 24.22 / 0.0543 | 0.06 |
| cam3 | gs_tokr5448_nat_dil_al_tto200_local | 42.5% | 19.43 / 0.0555 | 24.36 / 0.0507 | 24.31 / 0.0495 | 0.28 |
| cam3 | gs_tokr5448_nat_dil_al_tto25_local | 38.4% | 19.16 / 0.0557 | 23.21 / 0.0663 | 23.17 / 0.0654 | 0.28 |
| cam3 | gs_tokr5448_nat_dil_al_tto300_local | 44.0% | 19.54 / 0.0557 | 24.43 / 0.0509 | 24.51 / 0.0500 | 0.11 |
| cam3 | gs_tokr5448_nat_dil_al_tto50_local | 39.1% | 19.21 / 0.0562 | 23.74 / 0.0606 | 23.75 / 0.0605 | 0.03 |
| cam3 | gs_tokr5448_nat_dil_alv_local | 38.0% | 19.09 / 0.0546 | 21.93 / 0.0756 | 21.85 / 0.0730 | 0.71 |
| cam3 | gs_tokr5448_nat_dil_alv_tto100_local | 40.2% | 19.29 / 0.0563 | 24.15 / 0.0538 | 24.21 / 0.0536 | 0.05 |
| cam3 | gs_tokr5448_nat_dil_alv_tto200_local | 42.6% | 19.44 / 0.0555 | 24.30 / 0.0502 | 24.32 / 0.0494 | 0.20 |
| cam3 | gs_tokr5448_nat_dil_alv_tto25_local | 38.5% | 19.17 / 0.0556 | 23.16 / 0.0650 | 23.12 / 0.0646 | 0.19 |
| cam3 | gs_tokr5448_nat_dil_alv_tto300_local | 44.0% | 19.55 / 0.0556 | 24.38 / 0.0507 | 24.56 / 0.0495 | 0.16 |
| cam3 | gs_tokr5448_nat_dil_alv_tto50_local | 39.1% | 19.23 / 0.0558 | 23.70 / 0.0593 | 23.51 / 0.0597 | 0.24 |
| cam3 | gs_tokrife448_nat_dil_al_local | 11.1% | 14.60 / 0.0673 | 19.93 / 0.0500 | 19.56 / 0.0505 | 1.25 |
| cam3 | gs_tokrife448_nat_dil_al_tto100_local | 12.1% | 15.02 / 0.0696 | 22.68 / 0.0350 | 22.92 / 0.0344 | 0.56 |
| cam3 | gs_tokrife448_nat_dil_al_tto200_local | 12.9% | 15.06 / 0.0668 | 22.80 / 0.0338 | 23.03 / 0.0339 | 0.41 |
| cam3 | gs_tokrife448_nat_dil_al_tto25_local | 11.4% | 14.79 / 0.0684 | 21.39 / 0.0440 | 21.43 / 0.0429 | 0.49 |
| cam3 | gs_tokrife448_nat_dil_al_tto300_local | 13.5% | 15.13 / 0.0674 | 22.81 / 0.0362 | 22.16 / 0.0387 | 0.45 |
| cam3 | gs_tokrife448_nat_dil_al_tto50_local | 11.6% | 14.88 / 0.0682 | 22.00 / 0.0387 | 22.13 / 0.0375 | 0.42 |
| cam3 | gs_tokrife448_nat_dil_alv_local | 11.1% | 14.57 / 0.0676 | 19.83 / 0.0497 | 19.45 / 0.0503 | 1.47 |
| cam3 | gs_tokrife448_nat_dil_alv_tto100_local | 12.1% | 15.00 / 0.0698 | 22.61 / 0.0350 | 22.69 / 0.0341 | 0.35 |
| cam3 | gs_tokrife448_nat_dil_alv_tto200_local | 12.9% | 15.05 / 0.0670 | 22.77 / 0.0339 | 22.91 / 0.0337 | 0.36 |
| cam3 | gs_tokrife448_nat_dil_alv_tto25_local | 11.4% | 14.77 / 0.0687 | 21.33 / 0.0431 | 21.22 / 0.0423 | 0.69 |
| cam3 | gs_tokrife448_nat_dil_alv_tto300_local | 13.5% | 15.12 / 0.0680 | 22.83 / 0.0358 | 22.86 / 0.0354 | 0.11 |
| cam3 | gs_tokrife448_nat_dil_alv_tto50_local | 11.6% | 14.86 / 0.0675 | 21.92 / 0.0386 | 22.09 / 0.0376 | 0.63 |
| cam3 | gs_tokrife_g448_nat_dil_al_local | 16.9% | 13.56 / 0.0908 | 20.49 / 0.0557 | 20.49 / 0.0557 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto100_local | 17.5% | 13.69 / 0.0931 | 22.44 / 0.0402 | 22.44 / 0.0402 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto200_local | 18.0% | 13.75 / 0.0885 | 22.30 / 0.0386 | 22.30 / 0.0386 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto25_local | 17.1% | 13.62 / 0.0916 | 21.73 / 0.0470 | 21.73 / 0.0470 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto300_local | 18.5% | 13.86 / 0.0893 | 22.27 / 0.0411 | 22.27 / 0.0411 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto50_local | 17.3% | 13.65 / 0.0907 | 22.24 / 0.0411 | 22.24 / 0.0411 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_alv_local | 16.9% | 13.57 / 0.0908 | 20.21 / 0.0552 | 19.83 / 0.0566 | 0.62 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto100_local | 17.5% | 13.70 / 0.0932 | 21.91 / 0.0404 | 21.91 / 0.0404 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto200_local | 18.0% | 13.76 / 0.0881 | 21.77 / 0.0392 | 21.77 / 0.0392 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto25_local | 17.1% | 13.62 / 0.0916 | 21.33 / 0.0464 | 21.03 / 0.0467 | 0.19 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto300_local | 18.5% | 13.86 / 0.0895 | 21.77 / 0.0417 | 21.77 / 0.0417 | 0.00 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto50_local | 17.3% | 13.66 / 0.0894 | 21.78 / 0.0418 | 22.01 / 0.0413 | 0.43 |
| cam3 | gs_tokstrict448_nat_dil_al_local | 7.4% | 14.49 / 0.1271 | 18.85 / 0.0722 | 18.91 / 0.0733 | 1.25 |
| cam3 | gs_tokstrict448_nat_dil_al_tto100_local | 7.6% | 15.22 / 0.1374 | 22.33 / 0.0600 | 21.77 / 0.0735 | 2.02 |
| cam3 | gs_tokstrict448_nat_dil_al_tto200_local | 7.7% | 15.38 / 0.1310 | 22.41 / 0.0540 | 22.29 / 0.0572 | 0.25 |
| cam3 | gs_tokstrict448_nat_dil_al_tto25_local | 7.5% | 14.92 / 0.1374 | 20.97 / 0.0726 | 20.57 / 0.0764 | 1.03 |
| cam3 | gs_tokstrict448_nat_dil_al_tto300_local | 7.8% | 15.45 / 0.1316 | 22.21 / 0.0603 | 21.56 / 0.0699 | 1.18 |
| cam3 | gs_tokstrict448_nat_dil_al_tto50_local | 7.6% | 15.09 / 0.1394 | 22.05 / 0.0656 | 21.57 / 0.0696 | 1.05 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | 7.4% | 14.49 / 0.1279 | 18.88 / 0.0766 | 18.84 / 0.0798 | 1.41 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto100_local | 7.6% | 15.29 / 0.1362 | 22.29 / 0.0614 | 21.75 / 0.0692 | 1.08 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto200_local | 7.6% | 15.41 / 0.1343 | 22.44 / 0.0555 | 21.76 / 0.0608 | 1.06 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto25_local | 7.5% | 14.99 / 0.1374 | 21.03 / 0.0722 | 20.76 / 0.0752 | 0.85 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto300_local | 7.8% | 15.48 / 0.1381 | 22.27 / 0.0602 | 21.96 / 0.0670 | 0.33 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto50_local | 7.5% | 15.18 / 0.1369 | 22.05 / 0.0665 | 21.59 / 0.0707 | 1.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_local | 14.0% | 12.86 / 0.1298 | 20.46 / 0.0645 | 20.46 / 0.0645 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto100_local | 14.2% | 12.93 / 0.1299 | 22.55 / 0.0442 | 22.55 / 0.0442 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto200_local | 14.3% | 12.92 / 0.1312 | 22.52 / 0.0454 | 22.52 / 0.0454 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto25_local | 14.1% | 12.90 / 0.1315 | 21.77 / 0.0494 | 21.77 / 0.0494 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto300_local | 14.5% | 12.93 / 0.1287 | 22.34 / 0.0491 | 22.34 / 0.0491 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto50_local | 14.1% | 12.91 / 0.1333 | 22.36 / 0.0465 | 22.36 / 0.0465 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_local | 13.9% | 12.86 / 0.1296 | 20.10 / 0.0650 | 20.08 / 0.0679 | 0.63 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto100_local | 14.2% | 12.93 / 0.1297 | 21.92 / 0.0446 | 21.92 / 0.0446 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto200_local | 14.2% | 12.92 / 0.1308 | 21.88 / 0.0458 | 20.53 / 0.0564 | 2.12 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto25_local | 14.0% | 12.90 / 0.1310 | 21.26 / 0.0497 | 21.26 / 0.0497 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto300_local | 14.4% | 12.93 / 0.1291 | 21.76 / 0.0502 | 21.76 / 0.0502 | 0.00 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto50_local | 14.1% | 12.91 / 0.1316 | 21.79 / 0.0468 | 21.79 / 0.0468 | 0.00 |
| cam5 | gs_tokr5448_nat_dil_al_local | 18.3% | 23.73 / 0.0215 | 20.18 / 0.0523 | 21.02 / 0.0443 | 1.61 |
| cam5 | gs_tokr5448_nat_dil_al_tto100_local | 19.8% | 23.82 / 0.0231 | 22.91 / 0.0404 | 24.24 / 0.0297 | 1.97 |
| cam5 | gs_tokr5448_nat_dil_al_tto200_local | 21.4% | 24.00 / 0.0235 | 23.22 / 0.0406 | 24.41 / 0.0305 | 1.73 |
| cam5 | gs_tokr5448_nat_dil_al_tto25_local | 18.6% | 23.70 / 0.0227 | 22.12 / 0.0433 | 23.81 / 0.0310 | 1.64 |
| cam5 | gs_tokr5448_nat_dil_al_tto300_local | 22.1% | 24.04 / 0.0239 | 23.17 / 0.0434 | 24.61 / 0.0327 | 1.67 |
| cam5 | gs_tokr5448_nat_dil_al_tto50_local | 19.0% | 23.77 / 0.0234 | 22.63 / 0.0415 | 23.77 / 0.0304 | 2.00 |
| cam5 | gs_tokr5448_nat_dil_alv_local | 18.3% | 23.75 / 0.0212 | 19.84 / 0.0522 | 20.90 / 0.0436 | 1.63 |
| cam5 | gs_tokr5448_nat_dil_alv_tto100_local | 19.8% | 23.84 / 0.0231 | 22.37 / 0.0408 | 24.37 / 0.0286 | 1.83 |
| cam5 | gs_tokr5448_nat_dil_alv_tto200_local | 21.4% | 24.01 / 0.0233 | 22.70 / 0.0408 | 23.96 / 0.0313 | 1.82 |
| cam5 | gs_tokr5448_nat_dil_alv_tto25_local | 18.6% | 23.73 / 0.0228 | 21.63 / 0.0448 | 23.91 / 0.0310 | 1.83 |
| cam5 | gs_tokr5448_nat_dil_alv_tto300_local | 22.1% | 24.05 / 0.0236 | 22.68 / 0.0436 | 23.82 / 0.0341 | 1.89 |
| cam5 | gs_tokr5448_nat_dil_alv_tto50_local | 18.9% | 23.81 / 0.0232 | 22.11 / 0.0421 | 23.96 / 0.0294 | 1.90 |
| cam5 | gs_tokrife448_nat_dil_al_local | 4.6% | 20.91 / 0.0634 | 18.82 / 0.1169 | 18.93 / 0.1137 | 1.29 |
| cam5 | gs_tokrife448_nat_dil_al_tto100_local | 5.0% | 21.11 / 0.0629 | 24.25 / 0.0666 | 23.38 / 0.0663 | 1.53 |
| cam5 | gs_tokrife448_nat_dil_al_tto200_local | 5.4% | 21.31 / 0.0682 | 24.54 / 0.0660 | 23.22 / 0.0760 | 0.63 |
| cam5 | gs_tokrife448_nat_dil_al_tto25_local | 4.7% | 20.93 / 0.0696 | 22.10 / 0.0886 | 21.67 / 0.0844 | 2.00 |
| cam5 | gs_tokrife448_nat_dil_al_tto300_local | 5.6% | 21.29 / 0.0692 | 24.33 / 0.0698 | 23.16 / 0.0775 | 2.67 |
| cam5 | gs_tokrife448_nat_dil_al_tto50_local | 4.8% | 21.03 / 0.0675 | 23.39 / 0.0788 | 22.69 / 0.0745 | 2.32 |
| cam5 | gs_tokrife448_nat_dil_alv_local | 4.6% | 20.94 / 0.0625 | 18.47 / 0.1195 | 18.95 / 0.1107 | 1.39 |
| cam5 | gs_tokrife448_nat_dil_alv_tto100_local | 5.0% | 21.17 / 0.0671 | 23.13 / 0.0688 | 21.78 / 0.0719 | 2.88 |
| cam5 | gs_tokrife448_nat_dil_alv_tto200_local | 5.4% | 21.37 / 0.0666 | 23.45 / 0.0697 | 22.42 / 0.0775 | 2.03 |
| cam5 | gs_tokrife448_nat_dil_alv_tto25_local | 4.7% | 20.98 / 0.0700 | 21.33 / 0.0899 | 21.20 / 0.0887 | 2.14 |
| cam5 | gs_tokrife448_nat_dil_alv_tto300_local | 5.6% | 21.32 / 0.0660 | 23.25 / 0.0711 | 22.52 / 0.0776 | 1.60 |
| cam5 | gs_tokrife448_nat_dil_alv_tto50_local | 4.8% | 21.07 / 0.0676 | 22.33 / 0.0806 | 22.38 / 0.0780 | 1.66 |
| cam5 | gs_tokrife_g448_nat_dil_al_local | 7.9% | 20.62 / 0.0546 | 20.01 / 0.0890 | 20.22 / 0.0847 | 0.74 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto100_local | 8.6% | 20.56 / 0.0565 | 25.46 / 0.0440 | 25.46 / 0.0440 | 0.00 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto200_local | 9.2% | 20.72 / 0.0562 | 25.36 / 0.0457 | 25.36 / 0.0457 | 0.00 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto25_local | 8.2% | 20.46 / 0.0606 | 23.37 / 0.0556 | 23.35 / 0.0537 | 0.65 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto300_local | 9.5% | 20.75 / 0.0548 | 25.11 / 0.0496 | 25.11 / 0.0496 | 0.00 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto50_local | 8.3% | 20.50 / 0.0586 | 24.74 / 0.0508 | 24.10 / 0.0532 | 1.44 |
| cam5 | gs_tokrife_g448_nat_dil_alv_local | 7.9% | 20.61 / 0.0522 | 19.37 / 0.0897 | 20.07 / 0.0759 | 1.21 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto100_local | 8.6% | 20.58 / 0.0577 | 24.12 / 0.0470 | 22.95 / 0.0529 | 2.86 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto200_local | 9.2% | 20.74 / 0.0561 | 24.26 / 0.0485 | 22.44 / 0.0604 | 3.32 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto25_local | 8.1% | 20.45 / 0.0602 | 22.21 / 0.0576 | 22.58 / 0.0510 | 2.10 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto300_local | 9.5% | 20.74 / 0.0544 | 24.17 / 0.0509 | 23.63 / 0.0531 | 2.23 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto50_local | 8.2% | 20.51 / 0.0598 | 23.34 / 0.0535 | 23.77 / 0.0478 | 1.94 |
| cam5 | gs_tokstrict448_nat_dil_al_local | 3.2% | 18.65 / 0.0827 | 17.39 / 0.0926 | 17.45 / 0.0846 | 1.42 |
| cam5 | gs_tokstrict448_nat_dil_al_tto100_local | 3.7% | 19.12 / 0.0925 | 24.95 / 0.0446 | 20.75 / 0.0717 | 2.33 |
| cam5 | gs_tokstrict448_nat_dil_al_tto200_local | 4.1% | 19.42 / 0.0866 | 25.37 / 0.0380 | 23.05 / 0.0640 | 1.17 |
| cam5 | gs_tokstrict448_nat_dil_al_tto25_local | 3.4% | 18.80 / 0.0916 | 21.66 / 0.0772 | 21.15 / 0.0786 | 1.07 |
| cam5 | gs_tokstrict448_nat_dil_al_tto300_local | 4.2% | 19.53 / 0.0905 | 25.43 / 0.0408 | 22.73 / 0.0707 | 1.49 |
| cam5 | gs_tokstrict448_nat_dil_al_tto50_local | 3.4% | 18.92 / 0.0936 | 23.95 / 0.0586 | 22.35 / 0.0719 | 1.25 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | 3.2% | 18.61 / 0.0803 | 16.94 / 0.0974 | 17.54 / 0.0856 | 1.36 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto100_local | 3.7% | 19.13 / 0.0964 | 23.21 / 0.0580 | 20.42 / 0.0751 | 2.86 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto200_local | 4.1% | 19.40 / 0.0931 | 23.58 / 0.0539 | 22.65 / 0.0694 | 0.82 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto25_local | 3.4% | 18.80 / 0.0899 | 20.70 / 0.0823 | 19.47 / 0.0836 | 3.35 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto300_local | 4.2% | 19.52 / 0.0919 | 23.74 / 0.0561 | 22.73 / 0.0711 | 1.06 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto50_local | 3.4% | 18.92 / 0.0970 | 22.37 / 0.0686 | 18.85 / 0.0853 | 3.63 |
| cam5 | gs_tokstrict_g448_nat_dil_al_local | 5.8% | 15.30 / 0.1185 | 17.69 / 0.0932 | 17.69 / 0.0932 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto100_local | 6.8% | 15.86 / 0.1271 | 22.94 / 0.0597 | 19.22 / 0.0800 | 1.67 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto200_local | 7.8% | 16.23 / 0.1131 | 22.94 / 0.0612 | 22.94 / 0.0612 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto25_local | 6.1% | 15.53 / 0.1277 | 21.18 / 0.0781 | 21.18 / 0.0781 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto300_local | 8.0% | 16.32 / 0.1145 | 22.83 / 0.0666 | 22.11 / 0.0685 | 0.71 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto50_local | 6.3% | 15.71 / 0.1318 | 22.78 / 0.0689 | 22.78 / 0.0689 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_local | 5.8% | 15.32 / 0.1173 | 16.96 / 0.0989 | 16.96 / 0.0989 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto100_local | 6.8% | 15.93 / 0.1252 | 21.33 / 0.0652 | 19.28 / 0.0742 | 2.65 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto200_local | 7.8% | 16.25 / 0.1108 | 21.55 / 0.0642 | 21.55 / 0.0642 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto25_local | 6.1% | 15.57 / 0.1255 | 19.59 / 0.0865 | 19.93 / 0.0861 | 3.17 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto300_local | 8.0% | 16.34 / 0.1117 | 21.73 / 0.0702 | 21.73 / 0.0702 | 0.00 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto50_local | 6.3% | 15.80 / 0.1265 | 20.85 / 0.0771 | 20.03 / 0.0835 | 2.74 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_local] | 25.45 / 0.0767 | 16.98 / 0.1827 | 17.89 / 0.0479 | 32.20 / 0.0318 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 27.04 / 0.0538 | 19.73 / 0.0946 | 19.78 / 0.0329 | 32.61 / 0.0282 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 27.00 / 0.0524 | 20.00 / 0.0888 | 19.72 / 0.0317 | 32.61 / 0.0287 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 26.38 / 0.0657 | 18.11 / 0.1414 | 18.88 / 0.0406 | 32.46 / 0.0291 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 26.92 / 0.0533 | 19.98 / 0.0888 | 19.64 / 0.0321 | 32.58 / 0.0294 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 26.75 / 0.0598 | 18.79 / 0.1218 | 19.34 / 0.0364 | 32.56 / 0.0283 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.33 / 0.0766 | 16.64 / 0.1872 | 17.69 / 0.0479 | 32.21 / 0.0314 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 27.00 / 0.0533 | 20.32 / 0.0959 | 19.70 / 0.0326 | 32.59 / 0.0280 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 26.96 / 0.0519 | 20.72 / 0.0885 | 19.64 / 0.0316 | 32.58 / 0.0285 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 26.31 / 0.0651 | 18.10 / 0.1434 | 18.75 / 0.0404 | 32.44 / 0.0289 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 26.89 / 0.0528 | 20.77 / 0.0878 | 19.56 / 0.0321 | 32.54 / 0.0291 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 26.70 / 0.0592 | 19.01 / 0.1232 | 19.23 / 0.0362 | 32.54 / 0.0281 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.37 / 0.0536 | 17.36 / 0.1668 | 17.82 / 0.0380 | 33.50 / 0.0235 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.29 / 0.0465 | 19.63 / 0.0963 | 18.96 / 0.0305 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 27.33 / 0.0460 | 20.12 / 0.0895 | 19.00 / 0.0302 | 33.52 / 0.0235 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.85 / 0.0508 | 18.12 / 0.1375 | 18.38 / 0.0342 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 27.41 / 0.0465 | 20.16 / 0.0895 | 19.16 / 0.0303 | 33.51 / 0.0239 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.10 / 0.0487 | 18.78 / 0.1212 | 18.71 / 0.0321 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.29 / 0.0537 | 17.19 / 0.1687 | 17.71 / 0.0380 | 33.49 / 0.0236 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 27.24 / 0.0463 | 19.96 / 0.0971 | 18.84 / 0.0302 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 27.30 / 0.0456 | 20.60 / 0.0890 | 18.90 / 0.0300 | 33.51 / 0.0235 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 26.79 / 0.0508 | 18.08 / 0.1377 | 18.27 / 0.0342 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 27.38 / 0.0461 | 20.77 / 0.0877 | 19.07 / 0.0300 | 33.50 / 0.0240 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 27.05 / 0.0484 | 18.87 / 0.1214 | 18.60 / 0.0320 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.12 / 0.0531 | 18.09 / 0.1384 | 15.76 / 0.0383 | 33.50 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 25.62 / 0.0480 | 18.72 / 0.1027 | 16.32 / 0.0325 | 33.52 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 25.55 / 0.0480 | 18.74 / 0.0994 | 16.22 / 0.0325 | 33.52 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 25.43 / 0.0507 | 18.40 / 0.1228 | 16.10 / 0.0349 | 33.52 / 0.0233 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 25.50 / 0.0484 | 18.73 / 0.0994 | 16.17 / 0.0328 | 33.52 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 25.58 / 0.0492 | 18.63 / 0.1130 | 16.27 / 0.0334 | 33.52 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 25.05 / 0.0532 | 17.90 / 0.1406 | 15.64 / 0.0384 | 33.50 / 0.0235 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 25.53 / 0.0481 | 18.48 / 0.1072 | 16.16 / 0.0327 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 25.45 / 0.0480 | 18.50 / 0.1035 | 16.06 / 0.0326 | 33.52 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 25.35 / 0.0508 | 18.19 / 0.1255 | 15.96 / 0.0351 | 33.51 / 0.0234 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 25.41 / 0.0484 | 18.52 / 0.1027 | 16.01 / 0.0330 | 33.52 / 0.0235 |
| cam3 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 25.49 / 0.0492 | 18.40 / 0.1176 | 16.12 / 0.0336 | 33.52 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.27 / 0.0519 | 17.52 / 0.1466 | 15.95 / 0.0374 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 25.78 / 0.0477 | 18.81 / 0.1060 | 16.52 / 0.0323 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 25.72 / 0.0477 | 18.88 / 0.1010 | 16.43 / 0.0323 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 25.60 / 0.0493 | 18.02 / 0.1288 | 16.31 / 0.0342 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 25.68 / 0.0479 | 18.87 / 0.1004 | 16.39 / 0.0323 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 25.75 / 0.0483 | 18.57 / 0.1169 | 16.48 / 0.0330 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.21 / 0.0521 | 17.38 / 0.1482 | 15.85 / 0.0375 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 25.70 / 0.0477 | 18.63 / 0.1106 | 16.37 / 0.0324 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 25.63 / 0.0477 | 18.76 / 0.1040 | 16.28 / 0.0323 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 25.53 / 0.0495 | 17.86 / 0.1319 | 16.18 / 0.0343 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 25.60 / 0.0479 | 18.79 / 0.1029 | 16.25 / 0.0324 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 25.67 / 0.0484 | 18.40 / 0.1219 | 16.34 / 0.0332 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.10 / 0.0517 | 18.08 / 0.1399 | 15.65 / 0.0373 | 33.53 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.55 / 0.0478 | 18.71 / 0.1039 | 16.16 / 0.0327 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 25.49 / 0.0480 | 18.74 / 0.0999 | 16.09 / 0.0328 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.39 / 0.0493 | 18.39 / 0.1236 | 15.97 / 0.0343 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 25.45 / 0.0483 | 18.73 / 0.0998 | 16.05 / 0.0329 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 25.51 / 0.0484 | 18.62 / 0.1138 | 16.11 / 0.0333 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 25.03 / 0.0519 | 17.89 / 0.1423 | 15.53 / 0.0375 | 33.53 / 0.0234 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 25.46 / 0.0479 | 18.47 / 0.1086 | 16.01 / 0.0328 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 25.40 / 0.0481 | 18.50 / 0.1041 | 15.93 / 0.0329 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 25.31 / 0.0494 | 18.18 / 0.1266 | 15.84 / 0.0345 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 25.37 / 0.0483 | 18.52 / 0.1032 | 15.91 / 0.0330 | 33.54 / 0.0233 |
| cam3 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 25.43 / 0.0484 | 18.39 / 0.1188 | 15.98 / 0.0334 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.54 / 0.0764 | 16.67 / 0.1892 | 17.98 / 0.0482 | 32.32 / 0.0307 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 27.09 / 0.0537 | 19.60 / 0.0951 | 19.79 / 0.0328 | 32.66 / 0.0281 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 27.04 / 0.0520 | 19.02 / 0.0950 | 19.76 / 0.0313 | 32.67 / 0.0277 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 26.32 / 0.0655 | 17.68 / 0.1478 | 18.82 / 0.0408 | 32.46 / 0.0290 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 27.00 / 0.0525 | 19.80 / 0.0891 | 19.71 / 0.0314 | 32.63 / 0.0285 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 26.76 / 0.0597 | 18.77 / 0.1221 | 19.35 / 0.0363 | 32.57 / 0.0282 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.34 / 0.0774 | 16.35 / 0.1960 | 17.66 / 0.0491 | 32.24 / 0.0305 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 27.09 / 0.0532 | 20.36 / 0.0959 | 19.80 / 0.0324 | 32.64 / 0.0279 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 27.02 / 0.0518 | 19.77 / 0.0925 | 19.74 / 0.0313 | 32.60 / 0.0279 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 26.27 / 0.0653 | 17.77 / 0.1480 | 18.67 / 0.0413 | 32.44 / 0.0289 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 27.06 / 0.0517 | 20.78 / 0.0871 | 19.77 / 0.0311 | 32.63 / 0.0282 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 26.54 / 0.0601 | 18.36 / 0.1342 | 19.01 / 0.0379 | 32.51 / 0.0284 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.23 / 0.0542 | 16.98 / 0.1731 | 17.69 / 0.0391 | 33.49 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 27.34 / 0.0459 | 20.07 / 0.0937 | 19.03 / 0.0301 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 27.36 / 0.0456 | 20.77 / 0.0860 | 19.03 / 0.0300 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 26.87 / 0.0504 | 18.11 / 0.1365 | 18.45 / 0.0341 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 27.23 / 0.0472 | 19.34 / 0.0980 | 18.87 / 0.0314 | 33.50 / 0.0242 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 / 0.0483 | 18.94 / 0.1195 | 18.79 / 0.0320 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.10 / 0.0546 | 16.77 / 0.1771 | 17.56 / 0.0396 | 33.49 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 27.29 / 0.0460 | 19.73 / 0.0979 | 18.94 / 0.0299 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 27.35 / 0.0455 | 21.09 / 0.0850 | 19.01 / 0.0298 | 33.51 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 26.73 / 0.0508 | 17.86 / 0.1422 | 18.26 / 0.0346 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 27.40 / 0.0460 | 20.65 / 0.0875 | 19.12 / 0.0300 | 33.50 / 0.0240 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 27.13 / 0.0484 | 18.94 / 0.1220 | 18.76 / 0.0322 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.12 / 0.0531 | 18.09 / 0.1384 | 15.76 / 0.0383 | 33.50 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 25.62 / 0.0480 | 18.72 / 0.1027 | 16.32 / 0.0325 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 25.55 / 0.0480 | 18.74 / 0.0994 | 16.22 / 0.0325 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 25.43 / 0.0507 | 18.40 / 0.1228 | 16.10 / 0.0349 | 33.52 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 25.50 / 0.0484 | 18.73 / 0.0994 | 16.17 / 0.0328 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 25.58 / 0.0492 | 18.63 / 0.1130 | 16.27 / 0.0334 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 24.89 / 0.0537 | 17.71 / 0.1452 | 15.50 / 0.0392 | 33.49 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 25.53 / 0.0481 | 18.48 / 0.1072 | 16.16 / 0.0327 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 25.45 / 0.0480 | 18.50 / 0.1035 | 16.06 / 0.0326 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 25.25 / 0.0510 | 18.07 / 0.1276 | 15.85 / 0.0355 | 33.51 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 25.41 / 0.0484 | 18.52 / 0.1027 | 16.01 / 0.0330 | 33.52 / 0.0235 |
| cam3 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 25.53 / 0.0493 | 18.55 / 0.1161 | 16.18 / 0.0339 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.27 / 0.0519 | 17.51 / 0.1475 | 15.95 / 0.0375 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 25.75 / 0.0478 | 18.78 / 0.1094 | 16.50 / 0.0326 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 25.71 / 0.0477 | 18.86 / 0.1008 | 16.42 / 0.0322 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 25.58 / 0.0495 | 17.98 / 0.1290 | 16.29 / 0.0343 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 25.64 / 0.0480 | 18.79 / 0.1022 | 16.35 / 0.0324 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 25.72 / 0.0484 | 18.52 / 0.1182 | 16.46 / 0.0332 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.16 / 0.0525 | 17.32 / 0.1508 | 15.81 / 0.0380 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 25.67 / 0.0478 | 18.57 / 0.1121 | 16.35 / 0.0326 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 25.25 / 0.0489 | 18.28 / 0.1177 | 15.87 / 0.0346 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 25.51 / 0.0496 | 17.84 / 0.1316 | 16.17 / 0.0345 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 25.59 / 0.0479 | 18.74 / 0.1038 | 16.24 / 0.0324 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 25.65 / 0.0485 | 18.37 / 0.1226 | 16.32 / 0.0333 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.10 / 0.0517 | 18.08 / 0.1399 | 15.65 / 0.0373 | 33.53 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.55 / 0.0478 | 18.71 / 0.1039 | 16.16 / 0.0327 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 25.49 / 0.0480 | 18.74 / 0.0999 | 16.09 / 0.0328 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.39 / 0.0493 | 18.39 / 0.1236 | 15.97 / 0.0343 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 25.45 / 0.0483 | 18.73 / 0.0998 | 16.05 / 0.0329 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 25.51 / 0.0484 | 18.62 / 0.1138 | 16.11 / 0.0333 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 24.99 / 0.0522 | 17.85 / 0.1445 | 15.49 / 0.0378 | 33.53 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 25.46 / 0.0479 | 18.47 / 0.1086 | 16.01 / 0.0328 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 25.02 / 0.0493 | 18.03 / 0.1178 | 15.53 / 0.0352 | 33.52 / 0.0234 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 25.31 / 0.0494 | 18.18 / 0.1266 | 15.84 / 0.0345 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 25.37 / 0.0483 | 18.52 / 0.1032 | 15.91 / 0.0330 | 33.54 / 0.0233 |
| cam3 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 25.43 / 0.0484 | 18.39 / 0.1188 | 15.98 / 0.0334 | 33.54 / 0.0233 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_local] | 26.00 / 0.0594 | 18.20 / 0.1537 | 16.61 / 0.0315 | 30.25 / 0.0405 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 27.58 / 0.0477 | 22.44 / 0.0676 | 19.34 / 0.0196 | 30.55 / 0.0389 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 27.74 / 0.0482 | 22.67 / 0.0629 | 19.50 / 0.0193 | 30.55 / 0.0400 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 27.27 / 0.0511 | 20.49 / 0.1085 | 18.49 / 0.0229 | 30.64 / 0.0377 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 27.68 / 0.0492 | 22.48 / 0.0649 | 19.45 / 0.0194 | 30.47 / 0.0412 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 27.47 / 0.0492 | 21.62 / 0.0903 | 19.01 / 0.0213 | 30.60 / 0.0380 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.71 / 0.0599 | 17.61 / 0.1569 | 16.09 / 0.0328 | 30.13 / 0.0406 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 27.17 / 0.0481 | 20.98 / 0.0722 | 18.48 / 0.0211 | 30.42 / 0.0389 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 27.33 / 0.0484 | 21.21 / 0.0664 | 18.67 / 0.0206 | 30.43 / 0.0399 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 26.90 / 0.0517 | 19.54 / 0.1113 | 17.80 / 0.0245 | 30.52 / 0.0378 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 27.30 / 0.0495 | 21.14 / 0.0687 | 18.66 / 0.0208 | 30.35 / 0.0412 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 27.07 / 0.0496 | 20.42 / 0.0942 | 18.23 / 0.0226 | 30.47 / 0.0381 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.69 / 0.0419 | 20.19 / 0.0910 | 17.90 / 0.0208 | 31.34 / 0.0312 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.10 / 0.0378 | 22.56 / 0.0587 | 19.97 / 0.0139 | 31.44 / 0.0309 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 29.15 / 0.0382 | 22.79 / 0.0515 | 20.16 / 0.0134 | 31.41 / 0.0317 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.73 / 0.0396 | 21.67 / 0.0794 | 19.30 / 0.0159 | 31.42 / 0.0310 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 29.11 / 0.0384 | 22.82 / 0.0520 | 20.15 / 0.0134 | 31.38 / 0.0319 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.96 / 0.0389 | 22.17 / 0.0708 | 19.70 / 0.0149 | 31.44 / 0.0311 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.46 / 0.0421 | 19.84 / 0.0936 | 17.52 / 0.0216 | 31.35 / 0.0311 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 28.79 / 0.0382 | 21.84 / 0.0631 | 19.41 / 0.0148 | 31.44 / 0.0309 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 28.86 / 0.0384 | 22.11 / 0.0558 | 19.59 / 0.0144 | 31.40 / 0.0317 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 28.45 / 0.0398 | 21.10 / 0.0820 | 18.82 / 0.0170 | 31.42 / 0.0309 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 28.85 / 0.0386 | 22.19 / 0.0559 | 19.64 / 0.0144 | 31.38 / 0.0319 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 28.66 / 0.0392 | 21.52 / 0.0742 | 19.16 / 0.0158 | 31.44 / 0.0310 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_local] | 27.78 / 0.0409 | 20.45 / 0.0855 | 17.95 / 0.0200 | 31.36 / 0.0308 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 28.94 / 0.0372 | 22.39 / 0.0579 | 19.73 / 0.0139 | 31.45 / 0.0305 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 28.96 / 0.0376 | 22.54 / 0.0552 | 19.84 / 0.0136 | 31.42 / 0.0312 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 28.63 / 0.0385 | 21.64 / 0.0746 | 19.14 / 0.0156 | 31.44 / 0.0305 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 28.92 / 0.0378 | 22.55 / 0.0559 | 19.84 / 0.0135 | 31.40 / 0.0313 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 28.82 / 0.0380 | 22.04 / 0.0680 | 19.48 / 0.0147 | 31.45 / 0.0305 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 27.57 / 0.0412 | 20.13 / 0.0870 | 17.61 / 0.0208 | 31.37 / 0.0308 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 28.68 / 0.0376 | 21.74 / 0.0620 | 19.24 / 0.0148 | 31.45 / 0.0305 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 28.72 / 0.0379 | 21.96 / 0.0583 | 19.35 / 0.0145 | 31.41 / 0.0312 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 28.37 / 0.0389 | 21.11 / 0.0761 | 18.69 / 0.0166 | 31.44 / 0.0305 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 28.72 / 0.0380 | 22.03 / 0.0586 | 19.41 / 0.0144 | 31.39 / 0.0313 |
| cam5 | hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 28.55 / 0.0384 | 21.45 / 0.0706 | 18.99 / 0.0156 | 31.45 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 27.90 / 0.0405 | 20.53 / 0.0781 | 17.92 / 0.0190 | 31.43 / 0.0307 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 28.95 / 0.0375 | 22.21 / 0.0575 | 19.60 / 0.0142 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 28.98 / 0.0372 | 22.34 / 0.0523 | 19.68 / 0.0138 | 31.44 / 0.0308 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 28.62 / 0.0388 | 21.48 / 0.0729 | 18.99 / 0.0158 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 28.97 / 0.0374 | 22.38 / 0.0525 | 19.69 / 0.0137 | 31.43 / 0.0309 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 28.84 / 0.0382 | 21.90 / 0.0663 | 19.36 / 0.0150 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 27.76 / 0.0407 | 20.25 / 0.0816 | 17.66 / 0.0195 | 31.44 / 0.0307 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 28.78 / 0.0378 | 21.80 / 0.0609 | 19.25 / 0.0149 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 28.83 / 0.0375 | 22.03 / 0.0551 | 19.38 / 0.0144 | 31.45 / 0.0308 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 28.45 / 0.0391 | 21.12 / 0.0766 | 18.68 / 0.0165 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 28.85 / 0.0376 | 22.13 / 0.0547 | 19.45 / 0.0144 | 31.44 / 0.0310 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 28.65 / 0.0385 | 21.49 / 0.0701 | 19.00 / 0.0155 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 28.24 / 0.0396 | 21.10 / 0.0662 | 18.16 / 0.0175 | 31.45 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 28.50 / 0.0382 | 21.83 / 0.0566 | 18.75 / 0.0154 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 28.50 / 0.0381 | 21.89 / 0.0556 | 18.78 / 0.0153 | 31.45 / 0.0307 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 28.44 / 0.0387 | 21.55 / 0.0623 | 18.59 / 0.0160 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 28.50 / 0.0382 | 21.93 / 0.0562 | 18.81 / 0.0153 | 31.45 / 0.0308 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 28.48 / 0.0385 | 21.71 / 0.0601 | 18.70 / 0.0158 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 28.18 / 0.0398 | 20.93 / 0.0681 | 18.04 / 0.0177 | 31.45 / 0.0306 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 28.43 / 0.0384 | 21.50 / 0.0594 | 18.56 / 0.0158 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 28.45 / 0.0382 | 21.63 / 0.0576 | 18.64 / 0.0156 | 31.45 / 0.0307 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 28.35 / 0.0390 | 21.25 / 0.0659 | 18.38 / 0.0164 | 31.46 / 0.0305 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 28.46 / 0.0383 | 21.70 / 0.0578 | 18.70 / 0.0156 | 31.45 / 0.0308 |
| cam5 | hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 28.40 / 0.0388 | 21.38 / 0.0632 | 18.48 / 0.0161 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 26.62 / 0.0581 | 18.10 / 0.1518 | 17.26 / 0.0298 | 30.64 / 0.0364 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 28.42 / 0.0437 | 22.07 / 0.0632 | 20.32 / 0.0168 | 30.94 / 0.0335 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 28.35 / 0.0443 | 22.33 / 0.0587 | 20.26 / 0.0166 | 30.96 / 0.0341 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 28.29 / 0.0474 | 20.84 / 0.1042 | 19.77 / 0.0192 | 31.12 / 0.0322 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 28.43 / 0.0437 | 22.87 / 0.0576 | 20.74 / 0.0153 | 30.84 / 0.0348 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 28.23 / 0.0466 | 20.73 / 0.0940 | 19.56 / 0.0191 | 31.02 / 0.0334 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 26.50 / 0.0581 | 17.94 / 0.1484 | 17.03 / 0.0299 | 30.57 / 0.0364 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 28.41 / 0.0428 | 22.07 / 0.0649 | 20.32 / 0.0160 | 31.02 / 0.0330 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 27.86 / 0.0457 | 22.27 / 0.0625 | 19.76 / 0.0183 | 30.65 / 0.0351 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 28.37 / 0.0475 | 20.95 / 0.1009 | 19.89 / 0.0186 | 31.16 / 0.0324 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 27.87 / 0.0463 | 21.68 / 0.0678 | 19.47 / 0.0182 | 30.61 / 0.0362 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 28.22 / 0.0459 | 20.91 / 0.0917 | 19.49 / 0.0184 | 31.02 / 0.0328 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.81 / 0.0420 | 20.07 / 0.0940 | 18.08 / 0.0203 | 31.31 / 0.0313 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 29.04 / 0.0377 | 22.41 / 0.0571 | 20.01 / 0.0138 | 31.44 / 0.0309 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 29.00 / 0.0383 | 22.50 / 0.0542 | 19.93 / 0.0135 | 31.40 / 0.0317 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 28.65 / 0.0392 | 21.40 / 0.0809 | 19.40 / 0.0159 | 31.39 / 0.0310 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 28.98 / 0.0388 | 22.65 / 0.0538 | 19.79 / 0.0140 | 31.37 / 0.0321 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 28.80 / 0.0389 | 21.68 / 0.0714 | 19.69 / 0.0153 | 31.41 / 0.0310 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.82 / 0.0415 | 19.90 / 0.0937 | 18.12 / 0.0198 | 31.32 / 0.0312 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 28.46 / 0.0388 | 21.00 / 0.0674 | 19.19 / 0.0159 | 31.35 / 0.0310 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 28.45 / 0.0394 | 21.08 / 0.0666 | 19.15 / 0.0158 | 31.34 / 0.0319 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 28.49 / 0.0395 | 21.22 / 0.0795 | 19.09 / 0.0165 | 31.37 / 0.0310 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 28.73 / 0.0390 | 21.62 / 0.0611 | 19.60 / 0.0147 | 31.36 / 0.0320 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 28.70 / 0.0389 | 21.87 / 0.0706 | 19.50 / 0.0158 | 31.40 / 0.0311 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 27.91 / 0.0409 | 20.37 / 0.0884 | 18.16 / 0.0195 | 31.34 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 28.94 / 0.0372 | 22.39 / 0.0579 | 19.73 / 0.0139 | 31.45 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 28.96 / 0.0376 | 22.54 / 0.0552 | 19.84 / 0.0136 | 31.42 / 0.0312 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 28.62 / 0.0384 | 21.53 / 0.0757 | 19.20 / 0.0155 | 31.42 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 28.92 / 0.0378 | 22.55 / 0.0559 | 19.84 / 0.0135 | 31.40 / 0.0313 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 28.68 / 0.0382 | 21.65 / 0.0694 | 19.34 / 0.0152 | 31.43 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 27.91 / 0.0406 | 20.15 / 0.0884 | 18.18 / 0.0190 | 31.35 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 28.42 / 0.0384 | 21.09 / 0.0676 | 18.99 / 0.0158 | 31.36 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 28.33 / 0.0388 | 20.98 / 0.0688 | 18.93 / 0.0159 | 31.35 / 0.0314 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 28.48 / 0.0387 | 21.33 / 0.0757 | 19.05 / 0.0161 | 31.40 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 28.65 / 0.0383 | 21.61 / 0.0624 | 19.47 / 0.0147 | 31.37 / 0.0314 |
| cam5 | hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 28.62 / 0.0381 | 21.86 / 0.0684 | 19.36 / 0.0156 | 31.42 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 27.95 / 0.0404 | 20.26 / 0.0803 | 18.03 / 0.0185 | 31.39 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 28.54 / 0.0377 | 21.23 / 0.0623 | 18.88 / 0.0151 | 31.44 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 28.88 / 0.0373 | 22.15 / 0.0553 | 19.54 / 0.0139 | 31.44 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 28.58 / 0.0388 | 21.42 / 0.0740 | 18.94 / 0.0159 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 28.83 / 0.0376 | 22.06 / 0.0571 | 19.44 / 0.0140 | 31.43 / 0.0310 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 28.77 / 0.0382 | 21.76 / 0.0664 | 19.26 / 0.0150 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 28.08 / 0.0403 | 20.21 / 0.0827 | 18.23 / 0.0179 | 31.41 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 28.41 / 0.0383 | 21.26 / 0.0627 | 18.76 / 0.0161 | 31.43 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 28.79 / 0.0375 | 21.96 / 0.0568 | 19.32 / 0.0145 | 31.45 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 28.14 / 0.0390 | 20.51 / 0.0814 | 18.37 / 0.0169 | 31.45 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 28.80 / 0.0377 | 22.05 / 0.0575 | 19.37 / 0.0146 | 31.44 / 0.0310 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 27.90 / 0.0388 | 20.38 / 0.0770 | 18.10 / 0.0172 | 31.44 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 28.24 / 0.0396 | 21.10 / 0.0662 | 18.16 / 0.0175 | 31.45 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 28.31 / 0.0384 | 21.18 / 0.0602 | 18.26 / 0.0159 | 31.45 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 28.50 / 0.0381 | 21.89 / 0.0556 | 18.78 / 0.0153 | 31.45 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 28.44 / 0.0387 | 21.55 / 0.0623 | 18.59 / 0.0160 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 28.47 / 0.0383 | 21.80 / 0.0573 | 18.71 / 0.0154 | 31.45 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 28.48 / 0.0385 | 21.71 / 0.0601 | 18.70 / 0.0158 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 28.18 / 0.0398 | 20.93 / 0.0681 | 18.04 / 0.0177 | 31.45 / 0.0306 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 28.31 / 0.0387 | 21.17 / 0.0607 | 18.27 / 0.0161 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 28.45 / 0.0382 | 21.63 / 0.0576 | 18.64 / 0.0156 | 31.45 / 0.0307 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 28.37 / 0.0389 | 21.35 / 0.0647 | 18.41 / 0.0165 | 31.46 / 0.0305 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 28.46 / 0.0383 | 21.70 / 0.0578 | 18.70 / 0.0156 | 31.45 / 0.0308 |
| cam5 | hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 28.36 / 0.0389 | 21.34 / 0.0626 | 18.39 / 0.0162 | 31.46 / 0.0305 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.2%） | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 |
| cam3 | r5 | 30.7% | 37.9% | 25.45 / 0.0767 | 16.98 / 0.1827 | 32.20 |
| cam3 | rife | 10.8% | 11.1% | 26.37 / 0.0536 | 17.36 / 0.1668 | 33.50 |
| cam3 | strict | 8.4% | 7.4% | 25.27 / 0.0519 | 17.52 / 0.1466 | 33.53 |
| cam3 | rife_g | 9.7% | 8.5% | 25.12 / 0.0531 | 18.09 / 0.1384 | 33.50 |
| cam3 | strict_g | 8.3% | 7.0% | 25.10 / 0.0517 | 18.08 / 0.1399 | 33.53 |
| cam5 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.2%） | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 |
| cam5 | r5 | 15.7% | 18.3% | 26.00 / 0.0594 | 18.20 / 0.1537 | 30.25 |
| cam5 | rife | 3.8% | 4.6% | 27.69 / 0.0419 | 20.19 / 0.0910 | 31.34 |
| cam5 | strict | 2.4% | 2.4% | 27.90 / 0.0405 | 20.53 / 0.0781 | 31.43 |
| cam5 | rife_g | 3.5% | 4.0% | 27.78 / 0.0409 | 20.45 / 0.0855 | 31.36 |
| cam5 | strict_g | 1.6% | 1.5% | 28.24 / 0.0396 | 21.10 / 0.0662 | 31.45 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| cam3 | 1 | 0-4 | 19.25 / 0.1012 | +4.13 / -0.0065 (core 30.4%) | +4.62 / -0.0266 (core 14.5%) | +4.52 / -0.0284 (core 12.4%) | +4.62 / -0.0266 (core 14.5%) | +4.52 / -0.0284 (core 12.4%) |
| cam3 | 2 | 0-4 | 20.14 / 0.0784 | +4.07 / -0.0019 (core 30.4%) | +4.58 / -0.0221 (core 14.5%) | +4.50 / -0.0253 (core 12.4%) | +4.58 / -0.0221 (core 14.5%) | +4.50 / -0.0253 (core 12.4%) |
| cam3 | 3 | 0-4 | 22.11 / 0.0577 | +5.08 / +0.0062 (core 30.4%) | +5.93 / -0.0100 (core 14.5%) | +5.95 / -0.0131 (core 12.4%) | +5.93 / -0.0100 (core 14.5%) | +5.95 / -0.0131 (core 12.4%) |
| cam3 | 5 | 4-8 | 25.45 / 0.0357 | +1.88 / +0.0315 (core 24.9%) | +2.84 / +0.0010 (core 2.5%) | +0.38 / +0.0001 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam3 | 6 | 4-8 | 24.03 / 0.0518 | +1.99 / +0.0264 (core 24.9%) | +3.46 / -0.0003 (core 2.5%) | +0.22 / +0.0008 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam3 | 7 | 4-8 | 24.65 / 0.0526 | -0.08 / +0.0274 (core 24.9%) | +1.20 / +0.0021 (core 2.5%) | +0.44 / -0.0003 (core 0.4%) | +0.00 / +0.0000 (core 2.5%*) | +0.00 / +0.0000 (core 0.4%*) |
| cam5 | 1 | 0-2 | 23.87 / 0.0592 | +0.00 / +0.0202 (core 18.8%) | +0.95 / +0.0013 (core 5.9%) | +0.97 / -0.0000 (core 4.0%) | +0.95 / +0.0013 (core 5.9%) | +0.97 / -0.0000 (core 4.0%) |
| cam5 | 3 | 2-4 | 32.61 / 0.0248 | -4.33 / +0.0187 (core 12.0%) | -1.85 / +0.0040 (core 3.7%) | -0.97 / +0.0031 (core 2.1%) | -1.85 / +0.0040 (core 3.7%) | +0.00 / +0.0000 (core 2.1%*) |
| cam5 | 5 | 4-6 | 28.67 / 0.0315 | -1.26 / +0.0182 (core 11.3%) | -0.32 / +0.0016 (core 0.8%) | -0.39 / +0.0006 (core 0.2%) | +0.00 / +0.0000 (core 0.8%*) | +0.00 / +0.0000 (core 0.2%*) |
| cam5 | 7 | 6-8 | 26.85 / 0.0428 | -2.40 / +0.0224 (core 7.1%) | -0.02 / +0.0026 (core 0.4%) | +0.00 / +0.0000 (core 0.0%) | +0.00 / +0.0000 (core 0.4%*) | +0.00 / +0.0000 (core 0.0%*) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | 22.60 / 0.0629 | 14.53 | 33.53 | — |
| cam3 | r5 | 不复核 | 37.9% | 25.45 / 0.0767 | 16.98 | 32.20 | 2/6 |
| cam3 | r5 | w20 | 13.7% | 26.15 / 0.0581 | 16.76 | 33.53 | 3/6 |
| cam3 | r5 | oracle | 8.5% | 26.51 / 0.0576 | 17.52 | 33.50 | 3/6 |
| cam3 | r5 | 不复核 | 40.2% | 27.04 / 0.0538 | 19.73 | 32.61 | 3/6 |
| cam3 | r5 | w20 | 13.9% | 27.44 / 0.0467 | 19.47 | 33.54 | 6/6 |
| cam3 | r5 | oracle | 8.6% | 27.88 / 0.0454 | 19.99 | 33.52 | 6/6 |
| cam3 | r5 | 不复核 | 42.5% | 27.00 / 0.0524 | 20.00 | 32.61 | 4/6 |
| cam3 | r5 | w20 | 14.2% | 27.40 / 0.0460 | 19.76 | 33.54 | 6/6 |
| cam3 | r5 | oracle | 8.6% | 27.85 / 0.0443 | 20.27 | 33.52 | 6/6 |
| cam3 | r5 | 不复核 | 38.4% | 26.38 / 0.0657 | 18.11 | 32.46 | 3/6 |
| cam3 | r5 | w20 | 13.6% | 26.87 / 0.0530 | 17.82 | 33.53 | 4/6 |
| cam3 | r5 | oracle | 8.5% | 27.27 / 0.0520 | 18.52 | 33.51 | 4/6 |
| cam3 | r5 | 不复核 | 44.0% | 26.92 / 0.0533 | 19.98 | 32.58 | 3/6 |
| cam3 | r5 | w20 | 14.3% | 27.34 / 0.0463 | 19.76 | 33.54 | 6/6 |
| cam3 | r5 | oracle | 8.6% | 27.79 / 0.0445 | 20.25 | 33.52 | 6/6 |
| cam3 | r5 | 不复核 | 39.1% | 26.75 / 0.0598 | 18.79 | 32.56 | 3/6 |
| cam3 | r5 | w20 | 13.7% | 27.18 / 0.0498 | 18.51 | 33.53 | 5/6 |
| cam3 | r5 | oracle | 8.5% | 27.59 / 0.0487 | 19.18 | 33.51 | 4/6 |
| cam3 | rife | 不复核 | 11.1% | 26.37 / 0.0536 | 17.36 | 33.50 | 4/6 |
| cam3 | rife | w20 | 9.5% | 26.16 / 0.0533 | 17.06 | 33.53 | 5/6 |
| cam3 | rife | oracle | 5.4% | 26.57 / 0.0513 | 17.71 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | 12.1% | 27.29 / 0.0465 | 19.63 | 33.51 | 6/6 |
| cam3 | rife | w20 | 10.0% | 26.98 / 0.0469 | 19.24 | 33.53 | 6/6 |
| cam3 | rife | oracle | 5.6% | 27.41 / 0.0454 | 19.84 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | 12.9% | 27.33 / 0.0460 | 20.12 | 33.52 | 6/6 |
| cam3 | rife | w20 | 10.4% | 27.03 / 0.0464 | 19.76 | 33.53 | 6/6 |
| cam3 | rife | oracle | 5.8% | 27.46 / 0.0448 | 20.34 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | 11.4% | 26.85 / 0.0508 | 18.12 | 33.51 | 5/6 |
| cam3 | rife | w20 | 9.5% | 26.58 / 0.0509 | 17.76 | 33.53 | 5/6 |
| cam3 | rife | oracle | 5.5% | 26.99 / 0.0488 | 18.45 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | 13.5% | 27.41 / 0.0465 | 20.16 | 33.51 | 6/6 |
| cam3 | rife | w20 | 10.5% | 27.12 / 0.0465 | 19.84 | 33.53 | 6/6 |
| cam3 | rife | oracle | 5.9% | 27.55 / 0.0448 | 20.41 | 33.53 | 6/6 |
| cam3 | rife | 不复核 | 11.6% | 27.10 / 0.0487 | 18.78 | 33.51 | 6/6 |
| cam3 | rife | w20 | 9.7% | 26.81 / 0.0489 | 18.39 | 33.54 | 6/6 |
| cam3 | rife | oracle | 5.5% | 27.22 / 0.0472 | 19.10 | 33.53 | 6/6 |
| cam3 | rife_g | 不复核 | 8.5% | 25.12 / 0.0531 | 18.09 | 33.50 | 6/6 |
| cam3 | rife_g | w20 | 7.7% | 24.94 / 0.0534 | 17.67 | 33.53 | 6/6 |
| cam3 | rife_g | oracle | 4.4% | 25.22 / 0.0518 | 18.09 | 33.53 | 6/6 |
| cam3 | rife_g | 不复核 | 8.8% | 25.62 / 0.0480 | 18.72 | 33.52 | 6/6 |
| cam3 | rife_g | w20 | 7.9% | 25.39 / 0.0486 | 18.19 | 33.54 | 6/6 |
| cam3 | rife_g | oracle | 4.5% | 25.68 / 0.0473 | 18.71 | 33.53 | 6/6 |
| cam3 | rife_g | 不复核 | 9.0% | 25.55 / 0.0480 | 18.74 | 33.52 | 6/6 |
| cam3 | rife_g | w20 | 8.0% | 25.31 / 0.0486 | 18.20 | 33.54 | 6/6 |
| cam3 | rife_g | oracle | 4.5% | 25.60 / 0.0472 | 18.73 | 33.53 | 6/6 |
| cam3 | rife_g | 不复核 | 8.5% | 25.43 / 0.0507 | 18.40 | 33.52 | 6/6 |
| cam3 | rife_g | w20 | 7.7% | 25.22 / 0.0512 | 17.92 | 33.54 | 6/6 |
| cam3 | rife_g | oracle | 4.5% | 25.50 / 0.0494 | 18.40 | 33.53 | 6/6 |
| cam3 | rife_g | 不复核 | 9.3% | 25.50 / 0.0484 | 18.73 | 33.52 | 6/6 |
| cam3 | rife_g | w20 | 8.0% | 25.27 / 0.0489 | 18.20 | 33.53 | 6/6 |
| cam3 | rife_g | oracle | 4.5% | 25.56 / 0.0473 | 18.72 | 33.53 | 6/6 |
| cam3 | rife_g | 不复核 | 8.6% | 25.58 / 0.0492 | 18.63 | 33.52 | 6/6 |
| cam3 | rife_g | w20 | 7.8% | 25.35 / 0.0497 | 18.11 | 33.54 | 6/6 |
| cam3 | rife_g | oracle | 4.5% | 25.63 / 0.0483 | 18.62 | 33.53 | 6/6 |
| cam3 | strict | 不复核 | 7.4% | 25.27 / 0.0519 | 17.52 | 33.53 | 4/6 |
| cam3 | strict | w20 | 7.0% | 25.09 / 0.0522 | 17.15 | 33.53 | 5/6 |
| cam3 | strict | oracle | 4.2% | 25.35 / 0.0510 | 17.70 | 33.53 | 5/6 |
| cam3 | strict | 不复核 | 7.6% | 25.78 / 0.0477 | 18.81 | 33.54 | 4/6 |
| cam3 | strict | w20 | 7.1% | 25.56 / 0.0482 | 18.33 | 33.53 | 5/6 |
| cam3 | strict | oracle | 4.3% | 25.81 / 0.0473 | 18.85 | 33.53 | 5/6 |
| cam3 | strict | 不复核 | 7.7% | 25.72 / 0.0477 | 18.88 | 33.54 | 5/6 |
| cam3 | strict | w20 | 7.2% | 25.49 / 0.0483 | 18.41 | 33.53 | 5/6 |
| cam3 | strict | oracle | 4.3% | 25.74 / 0.0471 | 18.93 | 33.53 | 5/6 |
| cam3 | strict | 不复核 | 7.5% | 25.60 / 0.0493 | 18.02 | 33.54 | 4/6 |
| cam3 | strict | w20 | 7.0% | 25.39 / 0.0499 | 17.58 | 33.54 | 4/6 |
| cam3 | strict | oracle | 4.2% | 25.64 / 0.0488 | 18.17 | 33.53 | 4/6 |
| cam3 | strict | 不复核 | 7.8% | 25.68 / 0.0479 | 18.87 | 33.54 | 5/6 |
| cam3 | strict | w20 | 7.2% | 25.46 / 0.0485 | 18.42 | 33.53 | 5/6 |
| cam3 | strict | oracle | 4.3% | 25.71 / 0.0471 | 18.93 | 33.53 | 5/6 |
| cam3 | strict | 不复核 | 7.6% | 25.75 / 0.0483 | 18.57 | 33.54 | 4/6 |
| cam3 | strict | w20 | 7.1% | 25.52 / 0.0489 | 18.09 | 33.54 | 4/6 |
| cam3 | strict | oracle | 4.3% | 25.77 / 0.0480 | 18.63 | 33.53 | 5/6 |
| cam3 | strict_g | 不复核 | 7.0% | 25.10 / 0.0517 | 18.08 | 33.53 | 6/6 |
| cam3 | strict_g | w20 | 6.7% | 24.91 / 0.0523 | 17.66 | 33.53 | 6/6 |
| cam3 | strict_g | oracle | 4.0% | 25.16 / 0.0511 | 18.08 | 33.53 | 6/6 |
| cam3 | strict_g | 不复核 | 7.1% | 25.55 / 0.0478 | 18.71 | 33.54 | 6/6 |
| cam3 | strict_g | w20 | 6.8% | 25.32 / 0.0485 | 18.18 | 33.53 | 6/6 |
| cam3 | strict_g | oracle | 4.1% | 25.56 / 0.0475 | 18.70 | 33.53 | 6/6 |
| cam3 | strict_g | 不复核 | 7.1% | 25.49 / 0.0480 | 18.74 | 33.54 | 6/6 |
| cam3 | strict_g | w20 | 6.8% | 25.26 / 0.0487 | 18.20 | 33.53 | 6/6 |
| cam3 | strict_g | oracle | 4.1% | 25.51 / 0.0476 | 18.72 | 33.53 | 6/6 |
| cam3 | strict_g | 不复核 | 7.0% | 25.39 / 0.0493 | 18.39 | 33.54 | 6/6 |
| cam3 | strict_g | w20 | 6.7% | 25.17 / 0.0499 | 17.92 | 33.54 | 6/6 |
| cam3 | strict_g | oracle | 4.0% | 25.41 / 0.0489 | 18.39 | 33.53 | 6/6 |
| cam3 | strict_g | 不复核 | 7.2% | 25.45 / 0.0483 | 18.73 | 33.54 | 6/6 |
| cam3 | strict_g | w20 | 6.8% | 25.23 / 0.0490 | 18.20 | 33.53 | 6/6 |
| cam3 | strict_g | oracle | 4.1% | 25.48 / 0.0476 | 18.72 | 33.53 | 6/6 |
| cam3 | strict_g | 不复核 | 7.1% | 25.51 / 0.0484 | 18.62 | 33.54 | 6/6 |
| cam3 | strict_g | w20 | 6.7% | 25.28 / 0.0491 | 18.10 | 33.54 | 6/6 |
| cam3 | strict_g | oracle | 4.0% | 25.53 / 0.0482 | 18.61 | 33.53 | 6/6 |
| cam5 | 纯光流 | — | — | 28.00 / 0.0396 | 20.41 | 31.46 | — |
| cam5 | r5 | 不复核 | 18.3% | 26.00 / 0.0594 | 18.20 | 30.25 | 0/4 |
| cam5 | r5 | w20 | 3.9% | 27.58 / 0.0425 | 19.97 | 31.44 | 0/4 |
| cam5 | r5 | oracle | 3.5% | 27.35 / 0.0465 | 18.96 | 31.35 | 0/4 |
| cam5 | r5 | 不复核 | 19.8% | 27.58 / 0.0477 | 22.44 | 30.55 | 0/4 |
| cam5 | r5 | w20 | 3.9% | 28.69 / 0.0386 | 21.97 | 31.45 | 2/4 |
| cam5 | r5 | oracle | 3.5% | 29.06 / 0.0384 | 22.83 | 31.41 | 3/4 |
| cam5 | r5 | 不复核 | 21.4% | 27.74 / 0.0482 | 22.67 | 30.55 | 0/4 |
| cam5 | r5 | w20 | 4.1% | 28.75 / 0.0381 | 22.16 | 31.45 | 3/4 |
| cam5 | r5 | oracle | 3.5% | 29.16 / 0.0381 | 23.13 | 31.42 | 3/4 |
| cam5 | r5 | 不复核 | 18.6% | 27.27 / 0.0511 | 20.49 | 30.64 | 0/4 |
| cam5 | r5 | w20 | 3.8% | 28.33 / 0.0405 | 20.94 | 31.45 | 1/4 |
| cam5 | r5 | oracle | 3.5% | 28.50 / 0.0414 | 21.03 | 31.41 | 1/4 |
| cam5 | r5 | 不复核 | 22.1% | 27.68 / 0.0492 | 22.48 | 30.47 | 0/4 |
| cam5 | r5 | w20 | 4.1% | 28.74 / 0.0381 | 22.14 | 31.45 | 3/4 |
| cam5 | r5 | oracle | 3.5% | 29.13 / 0.0380 | 22.97 | 31.42 | 3/4 |
| cam5 | r5 | 不复核 | 19.0% | 27.47 / 0.0492 | 21.62 | 30.60 | 0/4 |
| cam5 | r5 | w20 | 3.8% | 28.56 / 0.0399 | 21.46 | 31.45 | 1/4 |
| cam5 | r5 | oracle | 3.4% | 28.81 / 0.0398 | 22.08 | 31.41 | 2/4 |
| cam5 | rife | 不复核 | 4.6% | 27.69 / 0.0419 | 20.19 | 31.34 | 0/4 |
| cam5 | rife | w20 | 2.8% | 27.72 / 0.0408 | 20.22 | 31.45 | 0/4 |
| cam5 | rife | oracle | 1.6% | 27.94 / 0.0405 | 20.59 | 31.45 | 0/4 |
| cam5 | rife | 不复核 | 5.0% | 29.10 / 0.0378 | 22.56 | 31.44 | 2/4 |
| cam5 | rife | w20 | 2.8% | 28.94 / 0.0375 | 22.09 | 31.46 | 2/4 |
| cam5 | rife | oracle | 1.6% | 29.15 / 0.0369 | 22.62 | 31.46 | 3/4 |
| cam5 | rife | 不复核 | 5.4% | 29.15 / 0.0382 | 22.79 | 31.41 | 3/4 |
| cam5 | rife | w20 | 2.9% | 28.98 / 0.0371 | 22.21 | 31.46 | 3/4 |
| cam5 | rife | oracle | 1.7% | 29.23 / 0.0364 | 22.90 | 31.46 | 3/4 |
| cam5 | rife | 不复核 | 4.7% | 28.73 / 0.0396 | 21.67 | 31.42 | 2/4 |
| cam5 | rife | w20 | 2.8% | 28.62 / 0.0388 | 21.40 | 31.46 | 2/4 |
| cam5 | rife | oracle | 1.6% | 28.80 / 0.0385 | 21.83 | 31.46 | 2/4 |
| cam5 | rife | 不复核 | 5.6% | 29.11 / 0.0384 | 22.82 | 31.38 | 3/4 |
| cam5 | rife | w20 | 2.9% | 28.96 / 0.0371 | 22.21 | 31.46 | 3/4 |
| cam5 | rife | oracle | 1.7% | 29.23 / 0.0363 | 22.96 | 31.46 | 3/4 |
| cam5 | rife | 不复核 | 4.8% | 28.96 / 0.0389 | 22.17 | 31.44 | 2/4 |
| cam5 | rife | w20 | 2.8% | 28.82 / 0.0383 | 21.76 | 31.46 | 2/4 |
| cam5 | rife | oracle | 1.6% | 29.02 / 0.0378 | 22.29 | 31.46 | 3/4 |
| cam5 | rife_g | 不复核 | 4.0% | 27.78 / 0.0409 | 20.45 | 31.36 | 2/4 |
| cam5 | rife_g | w20 | 2.7% | 27.80 / 0.0406 | 20.44 | 31.45 | 2/4 |
| cam5 | rife_g | oracle | 1.4% | 28.01 / 0.0401 | 20.80 | 31.45 | 2/4 |
| cam5 | rife_g | 不复核 | 4.3% | 28.94 / 0.0372 | 22.39 | 31.45 | 4/4 |
| cam5 | rife_g | w20 | 2.7% | 28.87 / 0.0374 | 22.02 | 31.46 | 4/4 |
| cam5 | rife_g | oracle | 1.4% | 28.98 / 0.0368 | 22.43 | 31.46 | 4/4 |
| cam5 | rife_g | 不复核 | 4.6% | 28.96 / 0.0376 | 22.54 | 31.42 | 4/4 |
| cam5 | rife_g | w20 | 2.7% | 28.89 / 0.0372 | 22.11 | 31.46 | 4/4 |
| cam5 | rife_g | oracle | 1.4% | 29.03 / 0.0365 | 22.63 | 31.46 | 4/4 |
| cam5 | rife_g | 不复核 | 4.1% | 28.63 / 0.0385 | 21.64 | 31.44 | 4/4 |
| cam5 | rife_g | w20 | 2.6% | 28.58 / 0.0385 | 21.41 | 31.46 | 4/4 |
| cam5 | rife_g | oracle | 1.4% | 28.69 / 0.0381 | 21.77 | 31.46 | 4/4 |
| cam5 | rife_g | 不复核 | 4.7% | 28.92 / 0.0378 | 22.55 | 31.40 | 4/4 |
| cam5 | rife_g | w20 | 2.7% | 28.86 / 0.0372 | 22.10 | 31.46 | 4/4 |
| cam5 | rife_g | oracle | 1.5% | 29.02 / 0.0364 | 22.68 | 31.46 | 4/4 |
| cam5 | rife_g | 不复核 | 4.1% | 28.82 / 0.0380 | 22.04 | 31.45 | 4/4 |
| cam5 | rife_g | w20 | 2.6% | 28.75 / 0.0381 | 21.71 | 31.46 | 4/4 |
| cam5 | rife_g | oracle | 1.4% | 28.87 / 0.0376 | 22.14 | 31.46 | 4/4 |
| cam5 | strict | 不复核 | 2.4% | 27.90 / 0.0405 | 20.53 | 31.43 | 2/4 |
| cam5 | strict | w20 | 1.7% | 27.92 / 0.0400 | 20.52 | 31.45 | 2/4 |
| cam5 | strict | oracle | 1.1% | 28.02 / 0.0399 | 20.74 | 31.45 | 2/4 |
| cam5 | strict | 不复核 | 2.8% | 28.95 / 0.0375 | 22.21 | 31.46 | 3/4 |
| cam5 | strict | w20 | 1.8% | 28.85 / 0.0375 | 21.85 | 31.46 | 3/4 |
| cam5 | strict | oracle | 1.2% | 28.96 / 0.0372 | 22.27 | 31.46 | 3/4 |
| cam5 | strict | 不复核 | 3.1% | 28.98 / 0.0372 | 22.34 | 31.44 | 4/4 |
| cam5 | strict | w20 | 1.9% | 28.88 / 0.0371 | 21.95 | 31.46 | 4/4 |
| cam5 | strict | oracle | 1.2% | 29.00 / 0.0367 | 22.39 | 31.46 | 4/4 |
| cam5 | strict | 不复核 | 2.5% | 28.62 / 0.0388 | 21.48 | 31.46 | 3/4 |
| cam5 | strict | w20 | 1.7% | 28.56 / 0.0386 | 21.28 | 31.46 | 3/4 |
| cam5 | strict | oracle | 1.1% | 28.66 / 0.0385 | 21.59 | 31.46 | 3/4 |
| cam5 | strict | 不复核 | 3.2% | 28.97 / 0.0374 | 22.38 | 31.43 | 4/4 |
| cam5 | strict | w20 | 1.9% | 28.88 / 0.0371 | 22.00 | 31.46 | 4/4 |
| cam5 | strict | oracle | 1.2% | 29.00 / 0.0367 | 22.44 | 31.46 | 4/4 |
| cam5 | strict | 不复核 | 2.6% | 28.84 / 0.0382 | 21.90 | 31.46 | 3/4 |
| cam5 | strict | w20 | 1.7% | 28.76 / 0.0381 | 21.61 | 31.46 | 3/4 |
| cam5 | strict | oracle | 1.1% | 28.85 / 0.0380 | 21.99 | 31.46 | 3/4 |
| cam5 | strict_g | 不复核 | 1.5% | 28.24 / 0.0396 | 21.10 | 31.45 | 4/4 |
| cam5 | strict_g | w20 | 1.1% | 28.21 / 0.0395 | 21.01 | 31.46 | 4/4 |
| cam5 | strict_g | oracle | 0.8% | 28.27 / 0.0395 | 21.11 | 31.46 | 4/4 |
| cam5 | strict_g | 不复核 | 1.7% | 28.50 / 0.0382 | 21.83 | 31.46 | 4/4 |
| cam5 | strict_g | w20 | 1.2% | 28.43 / 0.0383 | 21.53 | 31.46 | 4/4 |
| cam5 | strict_g | oracle | 0.8% | 28.50 / 0.0381 | 21.83 | 31.46 | 4/4 |
| cam5 | strict_g | 不复核 | 1.9% | 28.50 / 0.0381 | 21.89 | 31.45 | 4/4 |
| cam5 | strict_g | w20 | 1.3% | 28.44 / 0.0381 | 21.58 | 31.46 | 4/4 |
| cam5 | strict_g | oracle | 0.9% | 28.50 / 0.0378 | 21.91 | 31.46 | 4/4 |
| cam5 | strict_g | 不复核 | 1.5% | 28.44 / 0.0387 | 21.55 | 31.46 | 4/4 |
| cam5 | strict_g | w20 | 1.2% | 28.39 / 0.0387 | 21.36 | 31.46 | 4/4 |
| cam5 | strict_g | oracle | 0.8% | 28.44 / 0.0387 | 21.55 | 31.46 | 4/4 |
| cam5 | strict_g | 不复核 | 2.0% | 28.50 / 0.0382 | 21.93 | 31.45 | 4/4 |
| cam5 | strict_g | w20 | 1.3% | 28.44 / 0.0381 | 21.62 | 31.46 | 4/4 |
| cam5 | strict_g | oracle | 0.9% | 28.51 / 0.0378 | 21.96 | 31.46 | 4/4 |
| cam5 | strict_g | 不复核 | 1.6% | 28.48 / 0.0385 | 21.71 | 31.46 | 4/4 |
| cam5 | strict_g | w20 | 1.2% | 28.42 / 0.0386 | 21.46 | 31.46 | 4/4 |
| cam5 | strict_g | oracle | 0.8% | 28.48 / 0.0385 | 21.71 | 31.46 | 4/4 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | — |
| cam3 | FF | 0（前馈） | 911×878（96%） | 28.75 | 26.37 / 0.0536 | 17.36 / 0.1668 | 4/6 |
| cam3 | 25 | 1.73 s | 911×878（96%） | 32.18 | 26.85 / 0.0508 | 18.12 / 0.1375 | 5/6 |
| cam3 | 50 | 3.48 s | 911×878（96%） | 33.30 | 27.10 / 0.0487 | 18.78 / 0.1212 | 6/6 |
| cam3 | 100 | 7.00 s | 911×878（96%） | 34.59 | 27.29 / 0.0465 | 19.63 / 0.0963 | 6/6 |
| cam3 | 200 | 14.11 s | 911×878（96%） | 36.33 | 27.33 / 0.0460 | 20.12 / 0.0895 | 6/6 |
| cam3 | 300 | 21.26 s | 911×878（96%） | 37.61 | 27.41 / 0.0465 | 20.16 / 0.0895 | 6/6 |
| cam5 | 纯光流 | — | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | — |
| cam5 | FF | 0（前馈） | 917×839（91%） | 28.84 | 27.69 / 0.0419 | 20.19 / 0.0910 | 0/4 |
| cam5 | 25 | 3.01 s | 917×839（91%） | 31.59 | 28.73 / 0.0396 | 21.67 / 0.0794 | 2/4 |
| cam5 | 50 | 6.04 s | 917×839（91%） | 32.45 | 28.96 / 0.0389 | 22.17 / 0.0708 | 2/4 |
| cam5 | 100 | 12.13 s | 917×839（91%） | 33.54 | 29.10 / 0.0378 | 22.56 / 0.0587 | 2/4 |
| cam5 | 200 | 24.54 s | 917×839（91%） | 34.93 | 29.15 / 0.0382 | 22.79 / 0.0515 | 3/4 |
| cam5 | 300 | 37.01 s | 917×839（91%） | 35.83 | 29.11 / 0.0384 | 22.82 / 0.0520 | 3/4 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| cam3 | — | 纯光流 | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 | — |
| cam3 | r5 | GS 前馈颜色 | 直接 | 25.45 / 0.0767 | 16.98 / 0.1827 | 32.20 | 2/6 |
| cam3 | r5 | GS 前馈颜色 | oracle | 26.51 / 0.0576 | 17.52 / 0.1694 | 33.50 | 3/6 |
| cam3 | r5 | GS 测试时优化 25 步 | 直接 | 26.38 / 0.0657 | 18.11 / 0.1414 | 32.46 | 3/6 |
| cam3 | r5 | GS 测试时优化 25 步 | oracle | 27.27 / 0.0520 | 18.52 / 0.1321 | 33.51 | 4/6 |
| cam3 | r5 | GS 测试时优化 50 步 | 直接 | 26.75 / 0.0598 | 18.79 / 0.1218 | 32.56 | 3/6 |
| cam3 | r5 | GS 测试时优化 50 步 | oracle | 27.59 / 0.0487 | 19.18 / 0.1147 | 33.51 | 4/6 |
| cam3 | r5 | GS 测试时优化 100 步 | 直接 | 27.04 / 0.0538 | 19.73 / 0.0946 | 32.61 | 3/6 |
| cam3 | r5 | GS 测试时优化 100 步 | oracle | 27.88 / 0.0454 | 19.99 / 0.0940 | 33.52 | 6/6 |
| cam3 | r5 | GS 测试时优化 200 步 | 直接 | 27.00 / 0.0524 | 20.00 / 0.0888 | 32.61 | 4/6 |
| cam3 | r5 | GS 测试时优化 200 步 | oracle | 27.85 / 0.0443 | 20.27 / 0.0894 | 33.52 | 6/6 |
| cam3 | r5 | GS 测试时优化 300 步 | 直接 | 26.92 / 0.0533 | 19.98 / 0.0888 | 32.58 | 3/6 |
| cam3 | r5 | GS 测试时优化 300 步 | oracle | 27.79 / 0.0445 | 20.25 / 0.0895 | 33.52 | 6/6 |
| cam3 | r5 (alv) | GS 前馈颜色 | 直接 | 25.33 / 0.0766 | 16.64 / 0.1872 | 32.21 | 2/6 |
| cam3 | r5 (alv) | GS 测试时优化 25 步 | 直接 | 26.31 / 0.0651 | 18.10 / 0.1434 | 32.44 | 3/6 |
| cam3 | r5 (alv) | GS 测试时优化 50 步 | 直接 | 26.70 / 0.0592 | 19.01 / 0.1232 | 32.54 | 3/6 |
| cam3 | r5 (alv) | GS 测试时优化 100 步 | 直接 | 27.00 / 0.0533 | 20.32 / 0.0959 | 32.59 | 3/6 |
| cam3 | r5 (alv) | GS 测试时优化 200 步 | 直接 | 26.96 / 0.0519 | 20.72 / 0.0885 | 32.58 | 4/6 |
| cam3 | r5 (alv) | GS 测试时优化 300 步 | 直接 | 26.89 / 0.0528 | 20.77 / 0.0878 | 32.54 | 4/6 |
| cam3 | rife | GS 前馈颜色 | 直接 | 26.37 / 0.0536 | 17.36 / 0.1668 | 33.50 | 4/6 |
| cam3 | rife | GS 前馈颜色 | oracle | 26.57 / 0.0513 | 17.71 / 0.1570 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 25 步 | 直接 | 26.85 / 0.0508 | 18.12 / 0.1375 | 33.51 | 5/6 |
| cam3 | rife | GS 测试时优化 25 步 | oracle | 26.99 / 0.0488 | 18.45 / 0.1304 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 50 步 | 直接 | 27.10 / 0.0487 | 18.78 / 0.1212 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 50 步 | oracle | 27.22 / 0.0472 | 19.10 / 0.1150 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 100 步 | 直接 | 27.29 / 0.0465 | 19.63 / 0.0963 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 100 步 | oracle | 27.41 / 0.0454 | 19.84 / 0.0957 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 200 步 | 直接 | 27.33 / 0.0460 | 20.12 / 0.0895 | 33.52 | 6/6 |
| cam3 | rife | GS 测试时优化 200 步 | oracle | 27.46 / 0.0448 | 20.34 / 0.0895 | 33.53 | 6/6 |
| cam3 | rife | GS 测试时优化 300 步 | 直接 | 27.41 / 0.0465 | 20.16 / 0.0895 | 33.51 | 6/6 |
| cam3 | rife | GS 测试时优化 300 步 | oracle | 27.55 / 0.0448 | 20.41 / 0.0894 | 33.53 | 6/6 |
| cam3 | rife (alv) | GS 前馈颜色 | 直接 | 26.29 / 0.0537 | 17.19 / 0.1687 | 33.49 | 3/6 |
| cam3 | rife (alv) | GS 测试时优化 25 步 | 直接 | 26.79 / 0.0508 | 18.08 / 0.1377 | 33.51 | 4/6 |
| cam3 | rife (alv) | GS 测试时优化 50 步 | 直接 | 27.05 / 0.0484 | 18.87 / 0.1214 | 33.51 | 6/6 |
| cam3 | rife (alv) | GS 测试时优化 100 步 | 直接 | 27.24 / 0.0463 | 19.96 / 0.0971 | 33.51 | 6/6 |
| cam3 | rife (alv) | GS 测试时优化 200 步 | 直接 | 27.30 / 0.0456 | 20.60 / 0.0890 | 33.51 | 6/6 |
| cam3 | rife (alv) | GS 测试时优化 300 步 | 直接 | 27.38 / 0.0461 | 20.77 / 0.0877 | 33.50 | 6/6 |
| cam3 | rife_g | GS 前馈颜色 | 直接 | 25.12 / 0.0531 | 18.09 / 0.1384 | 33.50 | 6/6 |
| cam3 | rife_g | GS 前馈颜色 | oracle | 25.22 / 0.0518 | 18.09 / 0.1385 | 33.53 | 6/6 |
| cam3 | rife_g | GS 测试时优化 25 步 | 直接 | 25.43 / 0.0507 | 18.40 / 0.1228 | 33.52 | 6/6 |
| cam3 | rife_g | GS 测试时优化 25 步 | oracle | 25.50 / 0.0494 | 18.40 / 0.1222 | 33.53 | 6/6 |
| cam3 | rife_g | GS 测试时优化 50 步 | 直接 | 25.58 / 0.0492 | 18.63 / 0.1130 | 33.52 | 6/6 |
| cam3 | rife_g | GS 测试时优化 50 步 | oracle | 25.63 / 0.0483 | 18.62 / 0.1131 | 33.53 | 6/6 |
| cam3 | rife_g | GS 测试时优化 100 步 | 直接 | 25.62 / 0.0480 | 18.72 / 0.1027 | 33.52 | 6/6 |
| cam3 | rife_g | GS 测试时优化 100 步 | oracle | 25.68 / 0.0473 | 18.71 / 0.1042 | 33.53 | 6/6 |
| cam3 | rife_g | GS 测试时优化 200 步 | 直接 | 25.55 / 0.0480 | 18.74 / 0.0994 | 33.52 | 6/6 |
| cam3 | rife_g | GS 测试时优化 200 步 | oracle | 25.60 / 0.0472 | 18.73 / 0.1017 | 33.53 | 6/6 |
| cam3 | rife_g | GS 测试时优化 300 步 | 直接 | 25.50 / 0.0484 | 18.73 / 0.0994 | 33.52 | 6/6 |
| cam3 | rife_g | GS 测试时优化 300 步 | oracle | 25.56 / 0.0473 | 18.72 / 0.1018 | 33.53 | 6/6 |
| cam3 | rife_g (alv) | GS 前馈颜色 | 直接 | 25.05 / 0.0532 | 17.90 / 0.1406 | 33.50 | 6/6 |
| cam3 | rife_g (alv) | GS 测试时优化 25 步 | 直接 | 25.35 / 0.0508 | 18.19 / 0.1255 | 33.51 | 6/6 |
| cam3 | rife_g (alv) | GS 测试时优化 50 步 | 直接 | 25.49 / 0.0492 | 18.40 / 0.1176 | 33.52 | 6/6 |
| cam3 | rife_g (alv) | GS 测试时优化 100 步 | 直接 | 25.53 / 0.0481 | 18.48 / 0.1072 | 33.51 | 6/6 |
| cam3 | rife_g (alv) | GS 测试时优化 200 步 | 直接 | 25.45 / 0.0480 | 18.50 / 0.1035 | 33.52 | 6/6 |
| cam3 | rife_g (alv) | GS 测试时优化 300 步 | 直接 | 25.41 / 0.0484 | 18.52 / 0.1027 | 33.52 | 6/6 |
| cam3 | strict | GS 前馈颜色 | 直接 | 25.27 / 0.0519 | 17.52 / 0.1466 | 33.53 | 4/6 |
| cam3 | strict | GS 前馈颜色 | oracle | 25.35 / 0.0510 | 17.70 / 0.1435 | 33.53 | 5/6 |
| cam3 | strict | GS 测试时优化 25 步 | 直接 | 25.60 / 0.0493 | 18.02 / 0.1288 | 33.54 | 4/6 |
| cam3 | strict | GS 测试时优化 25 步 | oracle | 25.64 / 0.0488 | 18.17 / 0.1263 | 33.53 | 4/6 |
| cam3 | strict | GS 测试时优化 50 步 | 直接 | 25.75 / 0.0483 | 18.57 / 0.1169 | 33.54 | 4/6 |
| cam3 | strict | GS 测试时优化 50 步 | oracle | 25.77 / 0.0480 | 18.63 / 0.1154 | 33.53 | 5/6 |
| cam3 | strict | GS 测试时优化 100 步 | 直接 | 25.78 / 0.0477 | 18.81 / 0.1060 | 33.54 | 4/6 |
| cam3 | strict | GS 测试时优化 100 步 | oracle | 25.81 / 0.0473 | 18.85 / 0.1057 | 33.53 | 5/6 |
| cam3 | strict | GS 测试时优化 200 步 | 直接 | 25.72 / 0.0477 | 18.88 / 0.1010 | 33.54 | 5/6 |
| cam3 | strict | GS 测试时优化 200 步 | oracle | 25.74 / 0.0471 | 18.93 / 0.1021 | 33.53 | 5/6 |
| cam3 | strict | GS 测试时优化 300 步 | 直接 | 25.68 / 0.0479 | 18.87 / 0.1004 | 33.54 | 5/6 |
| cam3 | strict | GS 测试时优化 300 步 | oracle | 25.71 / 0.0471 | 18.93 / 0.1016 | 33.53 | 5/6 |
| cam3 | strict (alv) | GS 前馈颜色 | 直接 | 25.21 / 0.0521 | 17.38 / 0.1482 | 33.53 | 5/6 |
| cam3 | strict (alv) | GS 测试时优化 25 步 | 直接 | 25.53 / 0.0495 | 17.86 / 0.1319 | 33.54 | 4/6 |
| cam3 | strict (alv) | GS 测试时优化 50 步 | 直接 | 25.67 / 0.0484 | 18.40 / 0.1219 | 33.54 | 4/6 |
| cam3 | strict (alv) | GS 测试时优化 100 步 | 直接 | 25.70 / 0.0477 | 18.63 / 0.1106 | 33.54 | 5/6 |
| cam3 | strict (alv) | GS 测试时优化 200 步 | 直接 | 25.63 / 0.0477 | 18.76 / 0.1040 | 33.54 | 5/6 |
| cam3 | strict (alv) | GS 测试时优化 300 步 | 直接 | 25.60 / 0.0479 | 18.79 / 0.1029 | 33.54 | 5/6 |
| cam3 | strict_g | GS 前馈颜色 | 直接 | 25.10 / 0.0517 | 18.08 / 0.1399 | 33.53 | 6/6 |
| cam3 | strict_g | GS 前馈颜色 | oracle | 25.16 / 0.0511 | 18.08 / 0.1394 | 33.53 | 6/6 |
| cam3 | strict_g | GS 测试时优化 25 步 | 直接 | 25.39 / 0.0493 | 18.39 / 0.1236 | 33.54 | 6/6 |
| cam3 | strict_g | GS 测试时优化 25 步 | oracle | 25.41 / 0.0489 | 18.39 / 0.1229 | 33.53 | 6/6 |
| cam3 | strict_g | GS 测试时优化 50 步 | 直接 | 25.51 / 0.0484 | 18.62 / 0.1138 | 33.54 | 6/6 |
| cam3 | strict_g | GS 测试时优化 50 步 | oracle | 25.53 / 0.0482 | 18.61 / 0.1138 | 33.53 | 6/6 |
| cam3 | strict_g | GS 测试时优化 100 步 | 直接 | 25.55 / 0.0478 | 18.71 / 0.1039 | 33.54 | 6/6 |
| cam3 | strict_g | GS 测试时优化 100 步 | oracle | 25.56 / 0.0475 | 18.70 / 0.1050 | 33.53 | 6/6 |
| cam3 | strict_g | GS 测试时优化 200 步 | 直接 | 25.49 / 0.0480 | 18.74 / 0.0999 | 33.54 | 6/6 |
| cam3 | strict_g | GS 测试时优化 200 步 | oracle | 25.51 / 0.0476 | 18.72 / 0.1020 | 33.53 | 6/6 |
| cam3 | strict_g | GS 测试时优化 300 步 | 直接 | 25.45 / 0.0483 | 18.73 / 0.0998 | 33.54 | 6/6 |
| cam3 | strict_g | GS 测试时优化 300 步 | oracle | 25.48 / 0.0476 | 18.72 / 0.1021 | 33.53 | 6/6 |
| cam3 | strict_g (alv) | GS 前馈颜色 | 直接 | 25.03 / 0.0519 | 17.89 / 0.1423 | 33.53 | 6/6 |
| cam3 | strict_g (alv) | GS 测试时优化 25 步 | 直接 | 25.31 / 0.0494 | 18.18 / 0.1266 | 33.54 | 6/6 |
| cam3 | strict_g (alv) | GS 测试时优化 50 步 | 直接 | 25.43 / 0.0484 | 18.39 / 0.1188 | 33.54 | 6/6 |
| cam3 | strict_g (alv) | GS 测试时优化 100 步 | 直接 | 25.46 / 0.0479 | 18.47 / 0.1086 | 33.54 | 6/6 |
| cam3 | strict_g (alv) | GS 测试时优化 200 步 | 直接 | 25.40 / 0.0481 | 18.50 / 0.1041 | 33.54 | 6/6 |
| cam3 | strict_g (alv) | GS 测试时优化 300 步 | 直接 | 25.37 / 0.0483 | 18.52 / 0.1032 | 33.54 | 6/6 |
| cam5 | — | 纯光流 | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 | — |
| cam5 | r5 | GS 前馈颜色 | 直接 | 26.00 / 0.0594 | 18.20 / 0.1537 | 30.25 | 0/4 |
| cam5 | r5 | GS 前馈颜色 | oracle | 27.35 / 0.0465 | 18.96 / 0.1234 | 31.35 | 0/4 |
| cam5 | r5 | GS 测试时优化 25 步 | 直接 | 27.27 / 0.0511 | 20.49 / 0.1085 | 30.64 | 0/4 |
| cam5 | r5 | GS 测试时优化 25 步 | oracle | 28.50 / 0.0414 | 21.03 / 0.0923 | 31.41 | 1/4 |
| cam5 | r5 | GS 测试时优化 50 步 | 直接 | 27.47 / 0.0492 | 21.62 / 0.0903 | 30.60 | 0/4 |
| cam5 | r5 | GS 测试时优化 50 步 | oracle | 28.81 / 0.0398 | 22.08 / 0.0790 | 31.41 | 2/4 |
| cam5 | r5 | GS 测试时优化 100 步 | 直接 | 27.58 / 0.0477 | 22.44 / 0.0676 | 30.55 | 0/4 |
| cam5 | r5 | GS 测试时优化 100 步 | oracle | 29.06 / 0.0384 | 22.83 / 0.0598 | 31.41 | 3/4 |
| cam5 | r5 | GS 测试时优化 200 步 | 直接 | 27.74 / 0.0482 | 22.67 / 0.0629 | 30.55 | 0/4 |
| cam5 | r5 | GS 测试时优化 200 步 | oracle | 29.16 / 0.0381 | 23.13 / 0.0538 | 31.42 | 3/4 |
| cam5 | r5 | GS 测试时优化 300 步 | 直接 | 27.68 / 0.0492 | 22.48 / 0.0649 | 30.47 | 0/4 |
| cam5 | r5 | GS 测试时优化 300 步 | oracle | 29.13 / 0.0380 | 22.97 / 0.0542 | 31.42 | 3/4 |
| cam5 | r5 (alv) | GS 前馈颜色 | 直接 | 25.71 / 0.0599 | 17.61 / 0.1569 | 30.13 | 0/4 |
| cam5 | r5 (alv) | GS 测试时优化 25 步 | 直接 | 26.90 / 0.0517 | 19.54 / 0.1113 | 30.52 | 0/4 |
| cam5 | r5 (alv) | GS 测试时优化 50 步 | 直接 | 27.07 / 0.0496 | 20.42 / 0.0942 | 30.47 | 0/4 |
| cam5 | r5 (alv) | GS 测试时优化 100 步 | 直接 | 27.17 / 0.0481 | 20.98 / 0.0722 | 30.42 | 0/4 |
| cam5 | r5 (alv) | GS 测试时优化 200 步 | 直接 | 27.33 / 0.0484 | 21.21 / 0.0664 | 30.43 | 0/4 |
| cam5 | r5 (alv) | GS 测试时优化 300 步 | 直接 | 27.30 / 0.0495 | 21.14 / 0.0687 | 30.35 | 0/4 |
| cam5 | rife | GS 前馈颜色 | 直接 | 27.69 / 0.0419 | 20.19 / 0.0910 | 31.34 | 0/4 |
| cam5 | rife | GS 前馈颜色 | oracle | 27.94 / 0.0405 | 20.59 / 0.0811 | 31.45 | 0/4 |
| cam5 | rife | GS 测试时优化 25 步 | 直接 | 28.73 / 0.0396 | 21.67 / 0.0794 | 31.42 | 2/4 |
| cam5 | rife | GS 测试时优化 25 步 | oracle | 28.80 / 0.0385 | 21.83 / 0.0727 | 31.46 | 2/4 |
| cam5 | rife | GS 测试时优化 50 步 | 直接 | 28.96 / 0.0389 | 22.17 / 0.0708 | 31.44 | 2/4 |
| cam5 | rife | GS 测试时优化 50 步 | oracle | 29.02 / 0.0378 | 22.29 / 0.0667 | 31.46 | 3/4 |
| cam5 | rife | GS 测试时优化 100 步 | 直接 | 29.10 / 0.0378 | 22.56 / 0.0587 | 31.44 | 2/4 |
| cam5 | rife | GS 测试时优化 100 步 | oracle | 29.15 / 0.0369 | 22.62 / 0.0559 | 31.46 | 3/4 |
| cam5 | rife | GS 测试时优化 200 步 | 直接 | 29.15 / 0.0382 | 22.79 / 0.0515 | 31.41 | 3/4 |
| cam5 | rife | GS 测试时优化 200 步 | oracle | 29.23 / 0.0364 | 22.90 / 0.0483 | 31.46 | 3/4 |
| cam5 | rife | GS 测试时优化 300 步 | 直接 | 29.11 / 0.0384 | 22.82 / 0.0520 | 31.38 | 3/4 |
| cam5 | rife | GS 测试时优化 300 步 | oracle | 29.23 / 0.0363 | 22.96 / 0.0474 | 31.46 | 3/4 |
| cam5 | rife (alv) | GS 前馈颜色 | 直接 | 27.46 / 0.0421 | 19.84 / 0.0936 | 31.35 | 0/4 |
| cam5 | rife (alv) | GS 测试时优化 25 步 | 直接 | 28.45 / 0.0398 | 21.10 / 0.0820 | 31.42 | 1/4 |
| cam5 | rife (alv) | GS 测试时优化 50 步 | 直接 | 28.66 / 0.0392 | 21.52 / 0.0742 | 31.44 | 2/4 |
| cam5 | rife (alv) | GS 测试时优化 100 步 | 直接 | 28.79 / 0.0382 | 21.84 / 0.0631 | 31.44 | 2/4 |
| cam5 | rife (alv) | GS 测试时优化 200 步 | 直接 | 28.86 / 0.0384 | 22.11 / 0.0558 | 31.40 | 3/4 |
| cam5 | rife (alv) | GS 测试时优化 300 步 | 直接 | 28.85 / 0.0386 | 22.19 / 0.0559 | 31.38 | 3/4 |
| cam5 | rife_g | GS 前馈颜色 | 直接 | 27.78 / 0.0409 | 20.45 / 0.0855 | 31.36 | 2/4 |
| cam5 | rife_g | GS 前馈颜色 | oracle | 28.01 / 0.0401 | 20.80 / 0.0771 | 31.45 | 2/4 |
| cam5 | rife_g | GS 测试时优化 25 步 | 直接 | 28.63 / 0.0385 | 21.64 / 0.0746 | 31.44 | 4/4 |
| cam5 | rife_g | GS 测试时优化 25 步 | oracle | 28.69 / 0.0381 | 21.77 / 0.0693 | 31.46 | 4/4 |
| cam5 | rife_g | GS 测试时优化 50 步 | 直接 | 28.82 / 0.0380 | 22.04 / 0.0680 | 31.45 | 4/4 |
| cam5 | rife_g | GS 测试时优化 50 步 | oracle | 28.87 / 0.0376 | 22.14 / 0.0647 | 31.46 | 4/4 |
| cam5 | rife_g | GS 测试时优化 100 步 | 直接 | 28.94 / 0.0372 | 22.39 / 0.0579 | 31.45 | 4/4 |
| cam5 | rife_g | GS 测试时优化 100 步 | oracle | 28.98 / 0.0368 | 22.43 / 0.0559 | 31.46 | 4/4 |
| cam5 | rife_g | GS 测试时优化 200 步 | 直接 | 28.96 / 0.0376 | 22.54 / 0.0552 | 31.42 | 4/4 |
| cam5 | rife_g | GS 测试时优化 200 步 | oracle | 29.03 / 0.0365 | 22.63 / 0.0522 | 31.46 | 4/4 |
| cam5 | rife_g | GS 测试时优化 300 步 | 直接 | 28.92 / 0.0378 | 22.55 / 0.0559 | 31.40 | 4/4 |
| cam5 | rife_g | GS 测试时优化 300 步 | oracle | 29.02 / 0.0364 | 22.68 / 0.0516 | 31.46 | 4/4 |
| cam5 | rife_g (alv) | GS 前馈颜色 | 直接 | 27.57 / 0.0412 | 20.13 / 0.0870 | 31.37 | 2/4 |
| cam5 | rife_g (alv) | GS 测试时优化 25 步 | 直接 | 28.37 / 0.0389 | 21.11 / 0.0761 | 31.44 | 3/4 |
| cam5 | rife_g (alv) | GS 测试时优化 50 步 | 直接 | 28.55 / 0.0384 | 21.45 / 0.0706 | 31.45 | 4/4 |
| cam5 | rife_g (alv) | GS 测试时优化 100 步 | 直接 | 28.68 / 0.0376 | 21.74 / 0.0620 | 31.45 | 4/4 |
| cam5 | rife_g (alv) | GS 测试时优化 200 步 | 直接 | 28.72 / 0.0379 | 21.96 / 0.0583 | 31.41 | 4/4 |
| cam5 | rife_g (alv) | GS 测试时优化 300 步 | 直接 | 28.72 / 0.0380 | 22.03 / 0.0586 | 31.39 | 4/4 |
| cam5 | strict | GS 前馈颜色 | 直接 | 27.90 / 0.0405 | 20.53 / 0.0781 | 31.43 | 2/4 |
| cam5 | strict | GS 前馈颜色 | oracle | 28.02 / 0.0399 | 20.74 / 0.0734 | 31.45 | 2/4 |
| cam5 | strict | GS 测试时优化 25 步 | 直接 | 28.62 / 0.0388 | 21.48 / 0.0729 | 31.46 | 3/4 |
| cam5 | strict | GS 测试时优化 25 步 | oracle | 28.66 / 0.0385 | 21.59 / 0.0700 | 31.46 | 3/4 |
| cam5 | strict | GS 测试时优化 50 步 | 直接 | 28.84 / 0.0382 | 21.90 / 0.0663 | 31.46 | 3/4 |
| cam5 | strict | GS 测试时优化 50 步 | oracle | 28.85 / 0.0380 | 21.99 / 0.0640 | 31.46 | 3/4 |
| cam5 | strict | GS 测试时优化 100 步 | 直接 | 28.95 / 0.0375 | 22.21 / 0.0575 | 31.46 | 3/4 |
| cam5 | strict | GS 测试时优化 100 步 | oracle | 28.96 / 0.0372 | 22.27 / 0.0555 | 31.46 | 3/4 |
| cam5 | strict | GS 测试时优化 200 步 | 直接 | 28.98 / 0.0372 | 22.34 / 0.0523 | 31.44 | 4/4 |
| cam5 | strict | GS 测试时优化 200 步 | oracle | 29.00 / 0.0367 | 22.39 / 0.0498 | 31.46 | 4/4 |
| cam5 | strict | GS 测试时优化 300 步 | 直接 | 28.97 / 0.0374 | 22.38 / 0.0525 | 31.43 | 4/4 |
| cam5 | strict | GS 测试时优化 300 步 | oracle | 29.00 / 0.0367 | 22.44 / 0.0491 | 31.46 | 4/4 |
| cam5 | strict (alv) | GS 前馈颜色 | 直接 | 27.76 / 0.0407 | 20.25 / 0.0816 | 31.44 | 1/4 |
| cam5 | strict (alv) | GS 测试时优化 25 步 | 直接 | 28.45 / 0.0391 | 21.12 / 0.0766 | 31.46 | 3/4 |
| cam5 | strict (alv) | GS 测试时优化 50 步 | 直接 | 28.65 / 0.0385 | 21.49 / 0.0701 | 31.46 | 3/4 |
| cam5 | strict (alv) | GS 测试时优化 100 步 | 直接 | 28.78 / 0.0378 | 21.80 / 0.0609 | 31.46 | 3/4 |
| cam5 | strict (alv) | GS 测试时优化 200 步 | 直接 | 28.83 / 0.0375 | 22.03 / 0.0551 | 31.45 | 4/4 |
| cam5 | strict (alv) | GS 测试时优化 300 步 | 直接 | 28.85 / 0.0376 | 22.13 / 0.0547 | 31.44 | 4/4 |
| cam5 | strict_g | GS 前馈颜色 | 直接 | 28.24 / 0.0396 | 21.10 / 0.0662 | 31.45 | 4/4 |
| cam5 | strict_g | GS 前馈颜色 | oracle | 28.27 / 0.0395 | 21.11 / 0.0659 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 25 步 | 直接 | 28.44 / 0.0387 | 21.55 / 0.0623 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 25 步 | oracle | 28.44 / 0.0387 | 21.55 / 0.0623 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 50 步 | 直接 | 28.48 / 0.0385 | 21.71 / 0.0601 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 50 步 | oracle | 28.48 / 0.0385 | 21.71 / 0.0601 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 100 步 | 直接 | 28.50 / 0.0382 | 21.83 / 0.0566 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 100 步 | oracle | 28.50 / 0.0381 | 21.83 / 0.0563 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 200 步 | 直接 | 28.50 / 0.0381 | 21.89 / 0.0556 | 31.45 | 4/4 |
| cam5 | strict_g | GS 测试时优化 200 步 | oracle | 28.50 / 0.0378 | 21.91 / 0.0539 | 31.46 | 4/4 |
| cam5 | strict_g | GS 测试时优化 300 步 | 直接 | 28.50 / 0.0382 | 21.93 / 0.0562 | 31.45 | 4/4 |
| cam5 | strict_g | GS 测试时优化 300 步 | oracle | 28.51 / 0.0378 | 21.96 / 0.0536 | 31.46 | 4/4 |
| cam5 | strict_g (alv) | GS 前馈颜色 | 直接 | 28.18 / 0.0398 | 20.93 / 0.0681 | 31.45 | 3/4 |
| cam5 | strict_g (alv) | GS 测试时优化 25 步 | 直接 | 28.35 / 0.0390 | 21.25 / 0.0659 | 31.46 | 4/4 |
| cam5 | strict_g (alv) | GS 测试时优化 50 步 | 直接 | 28.40 / 0.0388 | 21.38 / 0.0632 | 31.46 | 4/4 |
| cam5 | strict_g (alv) | GS 测试时优化 100 步 | 直接 | 28.43 / 0.0384 | 21.50 / 0.0594 | 31.46 | 4/4 |
| cam5 | strict_g (alv) | GS 测试时优化 200 步 | 直接 | 28.45 / 0.0382 | 21.63 / 0.0576 | 31.45 | 4/4 |
| cam5 | strict_g (alv) | GS 测试时优化 300 步 | 直接 | 28.46 / 0.0383 | 21.70 / 0.0578 | 31.45 | 4/4 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_tok448_nat_dil_alv_tto300`，aligned_int → `gs_tok448_nat_dil_al`，aligned_vggt → `gs_tok448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=6.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 12.52 / 0.0568 | 32.36 / 0.0269 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |
| flow_s0.5_pose | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 | 22.93 / 0.0610 |
| gs_tok448_nat_dil_alv_tto300 | 21.69 / 0.0687 | 20.45 / 0.0290 | 31.33 / 0.0335 | 27.39 / 0.0527 |
| gs_tok448_nat_dil_alv_tto300+reg | 22.22 / 0.0659 | 21.66 / 0.0241 | 31.98 / 0.0287 | 28.36 / 0.0484 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 21.58 / 0.0821 | 20.45 / 0.0290 | 33.54 / 0.0233 | 28.41 / 0.0439 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 20.20 / 0.1045 | 18.46 / 0.0320 | 33.54 / 0.0233 | 27.06 / 0.0471 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 22.28 / 0.0796 | 21.66 / 0.0241 | 33.55 / 0.0232 | 28.96 / 0.0416 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 20.34 / 0.1022 | 18.83 / 0.0316 | 33.54 / 0.0233 | 27.33 / 0.0468 |
| gs_tok448_nat_dil_al | 18.27 / 0.1504 | 18.32 / 0.0461 | 29.12 / 0.0546 | 25.00 / 0.0945 |
| gs_tok448_nat_dil_al+reg | 18.22 / 0.1546 | 18.68 / 0.0445 | 29.37 / 0.0524 | 25.33 / 0.0941 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.07 / 0.1506 | 18.32 / 0.0461 | 33.53 / 0.0235 | 27.03 / 0.0571 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.05 / 0.1761 | 17.24 / 0.0429 | 33.54 / 0.0233 | 25.86 / 0.0585 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.96 / 0.1547 | 18.68 / 0.0445 | 33.54 / 0.0234 | 27.19 / 0.0567 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 16.96 / 0.1807 | 17.34 / 0.0432 | 33.54 / 0.0233 | 25.93 / 0.0591 |
| gs_tok448_nat_dil_alv | 17.73 / 0.1543 | 18.05 / 0.0462 | 29.27 / 0.0541 | 24.92 / 0.0942 |
| gs_tok448_nat_dil_alv+reg | 18.16 / 0.1545 | 18.70 / 0.0439 | 29.49 / 0.0517 | 25.41 / 0.0938 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.51 / 0.1532 | 18.05 / 0.0462 | 33.53 / 0.0235 | 26.86 / 0.0570 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 16.82 / 0.1777 | 17.07 / 0.0430 | 33.54 / 0.0233 | 25.74 / 0.0585 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.86 / 0.1531 | 18.70 / 0.0439 | 33.54 / 0.0234 | 27.19 / 0.0564 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.06 / 0.1765 | 17.34 / 0.0431 | 33.54 / 0.0233 | 25.94 / 0.0590 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_tok448_nat_dil_al | 18.27 | 0.6845 | 0.1504 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.22 | 0.6796 | 0.1546 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 21.13 | 0.7835 | 0.0723 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 21.28 | 0.7879 | 0.0720 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 21.14 | 0.7824 | 0.0702 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 21.07 | 0.7794 | 0.0697 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 20.08 | 0.7571 | 0.1028 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 20.19 | 0.7588 | 0.1037 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 21.09 | 0.7782 | 0.0713 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 21.07 | 0.7777 | 0.0704 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 20.83 | 0.7766 | 0.0851 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 20.98 | 0.7816 | 0.0856 | 1.00 |
| gs_tok448_nat_dil_alv | 17.73 | 0.6688 | 0.1543 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.16 | 0.6878 | 0.1545 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 21.51 | 0.7955 | 0.0713 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 22.07 | 0.8235 | 0.0695 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 21.64 | 0.7964 | 0.0681 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 22.19 | 0.8248 | 0.0655 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 19.92 | 0.7619 | 0.1033 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 20.45 | 0.7814 | 0.1018 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 21.69 | 0.7944 | 0.0687 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 22.22 | 0.8218 | 0.0659 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 20.96 | 0.7852 | 0.0835 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 21.45 | 0.8089 | 0.0828 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.70 | 0.6658 | 0.1726 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 20.89 | 0.7749 | 0.0775 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 21.15 | 0.7800 | 0.0701 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 18.80 | 0.7271 | 0.1320 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 21.12 | 0.7777 | 0.0696 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 19.83 | 0.7527 | 0.1068 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.24 | 0.6513 | 0.1773 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 21.27 | 0.7862 | 0.0784 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 21.64 | 0.7933 | 0.0696 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 18.49 | 0.7292 | 0.1350 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 21.71 | 0.7932 | 0.0687 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 19.75 | 0.7590 | 0.1081 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.70 | 0.6657 | 0.1730 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.88 | 0.7745 | 0.0778 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 21.14 | 0.7797 | 0.0702 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 18.79 | 0.7270 | 0.1322 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 21.12 | 0.7775 | 0.0697 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 19.81 | 0.7525 | 0.1072 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 17.23 | 0.6511 | 0.1775 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 21.26 | 0.7859 | 0.0787 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 21.64 | 0.7931 | 0.0697 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 18.48 | 0.7290 | 0.1352 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 21.70 | 0.7930 | 0.0689 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 19.73 | 0.7587 | 0.1084 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 10.87 | 0.3344 | 0.4155 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 11.80 | 0.3713 | 0.3755 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 11.85 | 0.3757 | 0.3706 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 11.25 | 0.3527 | 0.4007 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 11.83 | 0.3751 | 0.3701 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 11.62 | 0.3643 | 0.3881 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 10.59 | 0.3258 | 0.4175 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 11.35 | 0.3570 | 0.3796 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 11.39 | 0.3608 | 0.3745 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 10.90 | 0.3429 | 0.4036 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 11.42 | 0.3613 | 0.3738 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 11.21 | 0.3519 | 0.3920 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 14.86 | 0.6018 | 0.2510 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 16.45 | 0.6857 | 0.1925 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 16.42 | 0.6931 | 0.1813 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 15.45 | 0.6491 | 0.2242 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 16.49 | 0.6928 | 0.1778 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 16.15 | 0.6688 | 0.2082 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 14.54 | 0.5915 | 0.2529 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 15.97 | 0.6851 | 0.1953 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 15.95 | 0.6927 | 0.1850 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 15.07 | 0.6447 | 0.2275 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 16.07 | 0.6946 | 0.1815 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 15.73 | 0.6660 | 0.2117 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 10.86 | 0.3333 | 0.4173 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 11.78 | 0.3705 | 0.3771 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 11.84 | 0.3753 | 0.3710 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 11.23 | 0.3516 | 0.4025 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 11.83 | 0.3749 | 0.3704 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 11.59 | 0.3631 | 0.3897 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 10.57 | 0.3248 | 0.4195 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 11.34 | 0.3562 | 0.3813 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 11.39 | 0.3605 | 0.3749 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 10.88 | 0.3419 | 0.4053 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 11.41 | 0.3611 | 0.3741 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 11.19 | 0.3508 | 0.3939 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.96 | 0.7085 | 0.1547 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.07 | 0.7131 | 0.1506 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 21.49 | 0.8000 | 0.0894 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 21.39 | 0.7945 | 0.0892 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 21.32 | 0.7949 | 0.0885 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 21.39 | 0.7947 | 0.0878 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 20.55 | 0.7711 | 0.1123 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 20.51 | 0.7690 | 0.1106 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 21.31 | 0.7935 | 0.0893 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 21.35 | 0.7921 | 0.0891 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 21.23 | 0.7928 | 0.0988 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 21.11 | 0.7865 | 0.0986 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.86 | 0.7100 | 0.1531 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.51 | 0.6980 | 0.1532 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 22.13 | 0.8236 | 0.0830 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 21.43 | 0.7943 | 0.0843 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 22.26 | 0.8265 | 0.0788 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 21.54 | 0.7960 | 0.0815 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 20.72 | 0.7840 | 0.1080 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 20.26 | 0.7657 | 0.1089 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 22.28 | 0.8248 | 0.0796 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 21.58 | 0.7949 | 0.0821 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 21.58 | 0.8085 | 0.0935 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 21.02 | 0.7845 | 0.0945 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 17.14 | 0.6619 | 0.1747 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 17.22 | 0.6673 | 0.1705 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 19.73 | 0.7684 | 0.0965 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 19.71 | 0.7656 | 0.0963 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 19.55 | 0.7596 | 0.0949 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 19.71 | 0.7642 | 0.0945 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 18.83 | 0.7389 | 0.1270 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 18.83 | 0.7390 | 0.1249 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 19.58 | 0.7579 | 0.0959 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 19.68 | 0.7600 | 0.0958 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 19.42 | 0.7603 | 0.1105 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 19.45 | 0.7577 | 0.1088 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.15 | 0.6706 | 0.1746 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 16.79 | 0.6525 | 0.1746 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 20.54 | 0.8043 | 0.0936 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 20.33 | 0.7784 | 0.0958 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 20.67 | 0.8052 | 0.0903 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 20.47 | 0.7789 | 0.0929 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 19.17 | 0.7622 | 0.1243 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 18.87 | 0.7446 | 0.1250 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 20.71 | 0.8021 | 0.0909 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 20.51 | 0.7768 | 0.0940 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 19.99 | 0.7889 | 0.1070 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 19.81 | 0.7671 | 0.1075 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 16.96 | 0.6726 | 0.1807 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.05 | 0.6747 | 0.1761 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 19.52 | 0.7795 | 0.1095 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 19.47 | 0.7733 | 0.1096 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 19.40 | 0.7748 | 0.1090 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 19.51 | 0.7734 | 0.1080 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 18.58 | 0.7474 | 0.1383 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 18.59 | 0.7455 | 0.1362 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 19.43 | 0.7724 | 0.1098 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 19.50 | 0.7702 | 0.1089 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 19.18 | 0.7697 | 0.1229 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 19.20 | 0.7645 | 0.1217 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.06 | 0.6799 | 0.1765 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 16.82 | 0.6672 | 0.1777 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 20.16 | 0.8019 | 0.1040 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 20.03 | 0.7783 | 0.1056 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 20.32 | 0.8044 | 0.1007 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 20.18 | 0.7796 | 0.1031 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 18.89 | 0.7634 | 0.1330 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 18.69 | 0.7473 | 0.1334 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 20.34 | 0.8011 | 0.1022 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 20.20 | 0.7774 | 0.1045 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 19.65 | 0.7878 | 0.1168 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 19.56 | 0.7680 | 0.1173 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 17.52 | 0.6856 | 0.1694 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 19.99 | 0.7758 | 0.0940 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 20.27 | 0.7792 | 0.0894 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 18.52 | 0.7402 | 0.1321 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 20.25 | 0.7771 | 0.0895 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 19.18 | 0.7595 | 0.1147 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.71 | 0.6960 | 0.1570 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.84 | 0.7732 | 0.0957 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 20.34 | 0.7841 | 0.0895 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.45 | 0.7364 | 0.1304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 20.41 | 0.7827 | 0.0894 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.10 | 0.7544 | 0.1150 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 18.09 | 0.6840 | 0.1385 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 18.71 | 0.7206 | 0.1042 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 18.73 | 0.7226 | 0.1017 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 18.40 | 0.7039 | 0.1222 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 18.72 | 0.7215 | 0.1018 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 18.62 | 0.7139 | 0.1131 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 17.70 | 0.6857 | 0.1435 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 18.85 | 0.7336 | 0.1057 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 18.93 | 0.7384 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 18.17 | 0.7109 | 0.1263 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 18.93 | 0.7378 | 0.1016 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 18.63 | 0.7245 | 0.1154 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 18.08 | 0.6833 | 0.1394 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.70 | 0.7200 | 0.1050 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.72 | 0.7224 | 0.1020 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 18.39 | 0.7032 | 0.1229 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.72 | 0.7214 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.61 | 0.7132 | 0.1138 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 16.76 | 0.6634 | 0.1858 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 19.47 | 0.7693 | 0.1038 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 19.76 | 0.7744 | 0.0980 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 17.82 | 0.7276 | 0.1488 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 19.76 | 0.7722 | 0.0981 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 18.51 | 0.7486 | 0.1306 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 17.06 | 0.6797 | 0.1717 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 19.24 | 0.7645 | 0.1053 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 19.76 | 0.7767 | 0.0979 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 17.76 | 0.7255 | 0.1453 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 19.84 | 0.7754 | 0.0979 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 18.39 | 0.7434 | 0.1299 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 17.67 | 0.6801 | 0.1470 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 18.19 | 0.7142 | 0.1133 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 18.20 | 0.7171 | 0.1103 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 17.92 | 0.6986 | 0.1324 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 18.20 | 0.7162 | 0.1103 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 18.11 | 0.7080 | 0.1230 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 17.15 | 0.6762 | 0.1531 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 18.33 | 0.7253 | 0.1157 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 18.41 | 0.7311 | 0.1112 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 17.58 | 0.7034 | 0.1374 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 18.42 | 0.7309 | 0.1105 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 18.09 | 0.7165 | 0.1259 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 17.66 | 0.6792 | 0.1485 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.18 | 0.7135 | 0.1146 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.20 | 0.7167 | 0.1108 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 17.92 | 0.6979 | 0.1333 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.20 | 0.7159 | 0.1107 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.10 | 0.7072 | 0.1240 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 16.98 | 0.6558 | 0.1827 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 19.73 | 0.7611 | 0.0946 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 20.00 | 0.7650 | 0.0888 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 18.11 | 0.7199 | 0.1414 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 19.98 | 0.7623 | 0.0888 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 18.79 | 0.7410 | 0.1218 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 16.64 | 0.6436 | 0.1872 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 20.32 | 0.7725 | 0.0959 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 20.72 | 0.7784 | 0.0885 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 18.10 | 0.7251 | 0.1434 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 20.77 | 0.7778 | 0.0878 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 19.01 | 0.7498 | 0.1232 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.36 | 0.6786 | 0.1668 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.63 | 0.7626 | 0.0963 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 20.12 | 0.7731 | 0.0895 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.12 | 0.7242 | 0.1375 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 20.16 | 0.7702 | 0.0895 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.78 | 0.7423 | 0.1212 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.19 | 0.6714 | 0.1687 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 19.96 | 0.7658 | 0.0971 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 20.60 | 0.7794 | 0.0890 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 18.08 | 0.7245 | 0.1377 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 20.77 | 0.7798 | 0.0877 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 18.87 | 0.7433 | 0.1214 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 18.09 | 0.6845 | 0.1384 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 18.72 | 0.7200 | 0.1027 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 18.74 | 0.7232 | 0.0994 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 18.40 | 0.7040 | 0.1228 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 18.73 | 0.7223 | 0.0994 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 18.63 | 0.7138 | 0.1130 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 17.90 | 0.6768 | 0.1406 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 18.48 | 0.7059 | 0.1072 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 18.50 | 0.7084 | 0.1035 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 18.19 | 0.6946 | 0.1255 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 18.52 | 0.7085 | 0.1027 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 18.40 | 0.7017 | 0.1176 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 17.52 | 0.6779 | 0.1466 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 18.81 | 0.7279 | 0.1060 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 18.88 | 0.7335 | 0.1010 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 18.02 | 0.7060 | 0.1288 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 18.87 | 0.7330 | 0.1004 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 18.57 | 0.7196 | 0.1169 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 17.38 | 0.6729 | 0.1482 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 18.63 | 0.7201 | 0.1106 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 18.76 | 0.7262 | 0.1040 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 17.86 | 0.6992 | 0.1319 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 18.79 | 0.7269 | 0.1029 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 18.40 | 0.7120 | 0.1219 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 18.08 | 0.6837 | 0.1399 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.71 | 0.7196 | 0.1039 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.74 | 0.7230 | 0.0999 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 18.39 | 0.7035 | 0.1236 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.73 | 0.7223 | 0.0998 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.62 | 0.7133 | 0.1138 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 17.89 | 0.6761 | 0.1423 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 18.47 | 0.7054 | 0.1086 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 18.50 | 0.7082 | 0.1041 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 18.18 | 0.6941 | 0.1266 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 18.52 | 0.7084 | 0.1032 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 18.39 | 0.7012 | 0.1188 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 16.67 | 0.6357 | 0.1892 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 19.60 | 0.7577 | 0.0951 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 19.02 | 0.7209 | 0.0950 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 17.68 | 0.6956 | 0.1478 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 19.80 | 0.7555 | 0.0891 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 18.77 | 0.7401 | 0.1221 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 16.35 | 0.6218 | 0.1960 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 20.36 | 0.7740 | 0.0959 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 19.77 | 0.7522 | 0.0925 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 17.77 | 0.7047 | 0.1480 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 20.78 | 0.7786 | 0.0871 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 18.36 | 0.7134 | 0.1342 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 16.98 | 0.6584 | 0.1731 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 20.07 | 0.7781 | 0.0937 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 20.77 | 0.7915 | 0.0860 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 18.11 | 0.7244 | 0.1365 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 19.34 | 0.7421 | 0.0980 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 18.94 | 0.7482 | 0.1195 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 16.77 | 0.6513 | 0.1771 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 19.73 | 0.7634 | 0.0979 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 21.09 | 0.7912 | 0.0850 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 17.86 | 0.7136 | 0.1422 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 20.65 | 0.7786 | 0.0875 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 18.94 | 0.7537 | 0.1220 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 18.09 | 0.6845 | 0.1384 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 18.72 | 0.7200 | 0.1027 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 18.74 | 0.7232 | 0.0994 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 18.40 | 0.7040 | 0.1228 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 18.73 | 0.7223 | 0.0994 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 18.63 | 0.7138 | 0.1130 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 17.71 | 0.6667 | 0.1452 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 18.48 | 0.7059 | 0.1072 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 18.50 | 0.7084 | 0.1035 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 18.07 | 0.6876 | 0.1276 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 18.52 | 0.7085 | 0.1027 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 18.55 | 0.7128 | 0.1161 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 17.51 | 0.6746 | 0.1475 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 18.78 | 0.7193 | 0.1094 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 18.86 | 0.7318 | 0.1008 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 17.98 | 0.7005 | 0.1290 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 18.79 | 0.7216 | 0.1022 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 18.52 | 0.7137 | 0.1182 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 17.32 | 0.6674 | 0.1508 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 18.57 | 0.7106 | 0.1121 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 18.28 | 0.6877 | 0.1177 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 17.84 | 0.6948 | 0.1316 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 18.74 | 0.7189 | 0.1038 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 18.37 | 0.7057 | 0.1226 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 18.08 | 0.6837 | 0.1399 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.71 | 0.7196 | 0.1039 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.74 | 0.7230 | 0.0999 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 18.39 | 0.7035 | 0.1236 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.73 | 0.7223 | 0.0998 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.62 | 0.7133 | 0.1138 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 17.85 | 0.6746 | 0.1445 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 18.47 | 0.7054 | 0.1086 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 18.03 | 0.6698 | 0.1178 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 18.18 | 0.6941 | 0.1266 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 18.52 | 0.7084 | 0.1032 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 18.39 | 0.7012 | 0.1188 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 14.17 | 0.5985 | 0.0457 | 1.00 |
| flow_s0.5_pose | 13.30 | 0.5443 | 0.0482 | 1.00 |
| flow_s0.5_uniform | 13.88 | 0.5654 | 0.0513 | 1.00 |
| flow_s1.0_oracle | 13.03 | 0.5914 | 0.0498 | 1.00 |
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| flow_s1.0_uniform | 12.52 | 0.5342 | 0.0568 | 1.00 |
| gs_tok448_nat_dil_al | 18.32 | 0.7180 | 0.0461 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.68 | 0.7271 | 0.0445 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 20.67 | 0.8040 | 0.0275 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 21.42 | 0.8284 | 0.0236 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 20.63 | 0.8011 | 0.0280 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 21.33 | 0.8238 | 0.0238 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 20.08 | 0.7841 | 0.0321 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 20.60 | 0.8006 | 0.0293 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 20.57 | 0.7975 | 0.0287 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 21.29 | 0.8210 | 0.0244 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 20.55 | 0.7991 | 0.0285 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 21.16 | 0.8214 | 0.0254 | 1.00 |
| gs_tok448_nat_dil_alv | 18.05 | 0.7117 | 0.0462 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.70 | 0.7302 | 0.0439 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 20.50 | 0.8011 | 0.0277 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 21.60 | 0.8377 | 0.0238 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 20.49 | 0.7991 | 0.0282 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 21.76 | 0.8390 | 0.0232 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 19.87 | 0.7803 | 0.0323 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 20.75 | 0.8078 | 0.0285 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 20.45 | 0.7961 | 0.0290 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 21.66 | 0.8349 | 0.0241 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 20.36 | 0.7954 | 0.0288 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 21.37 | 0.8285 | 0.0249 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.42 | 0.6931 | 0.0505 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 20.68 | 0.7870 | 0.0327 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 20.49 | 0.7909 | 0.0311 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 19.55 | 0.7463 | 0.0413 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 20.40 | 0.7884 | 0.0313 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 20.20 | 0.7687 | 0.0367 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.18 | 0.6882 | 0.0506 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 20.54 | 0.7844 | 0.0327 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 20.34 | 0.7888 | 0.0313 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 19.35 | 0.7425 | 0.0413 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 20.26 | 0.7869 | 0.0315 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 20.02 | 0.7649 | 0.0367 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.92 | 0.5611 | 0.1213 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.32 | 0.6348 | 0.1084 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 12.38 | 0.6368 | 0.1064 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.11 | 0.6054 | 0.1151 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 12.41 | 0.6352 | 0.1064 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.22 | 0.6228 | 0.1118 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 11.87 | 0.5559 | 0.1215 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 12.27 | 0.6326 | 0.1081 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 12.33 | 0.6352 | 0.1062 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 12.05 | 0.6012 | 0.1151 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 12.37 | 0.6342 | 0.1063 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 12.17 | 0.6190 | 0.1115 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 8.39 | 0.3080 | 0.1694 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 8.63 | 0.3430 | 0.1612 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 8.65 | 0.3463 | 0.1603 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 8.52 | 0.3288 | 0.1652 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 8.65 | 0.3451 | 0.1608 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 8.59 | 0.3378 | 0.1630 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 8.35 | 0.3042 | 0.1694 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 8.57 | 0.3339 | 0.1615 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 8.59 | 0.3367 | 0.1607 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 8.46 | 0.3225 | 0.1654 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 8.59 | 0.3359 | 0.1612 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 8.53 | 0.3298 | 0.1632 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 10.15 | 0.4744 | 0.1506 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 10.38 | 0.5269 | 0.1427 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 10.37 | 0.5283 | 0.1419 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 10.27 | 0.5035 | 0.1470 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 10.36 | 0.5267 | 0.1422 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 10.34 | 0.5158 | 0.1450 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 10.12 | 0.4717 | 0.1507 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 10.33 | 0.5204 | 0.1430 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 10.32 | 0.5219 | 0.1422 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 10.23 | 0.4981 | 0.1472 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 10.32 | 0.5208 | 0.1425 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 10.30 | 0.5093 | 0.1452 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 7.52 | 0.2795 | 0.1844 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 7.65 | 0.3096 | 0.1792 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 7.64 | 0.3117 | 0.1789 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 7.60 | 0.2978 | 0.1816 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 7.62 | 0.3103 | 0.1794 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 7.64 | 0.3050 | 0.1803 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 7.49 | 0.2759 | 0.1845 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 7.60 | 0.3004 | 0.1795 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 7.59 | 0.3021 | 0.1792 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 7.56 | 0.2916 | 0.1818 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 7.58 | 0.3010 | 0.1797 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 7.59 | 0.2970 | 0.1805 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 18.68 | 0.7185 | 0.0445 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 18.32 | 0.7074 | 0.0461 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 21.42 | 0.8197 | 0.0236 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 20.67 | 0.7959 | 0.0275 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 21.33 | 0.8159 | 0.0238 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 20.63 | 0.7935 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 20.60 | 0.7917 | 0.0293 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 20.08 | 0.7751 | 0.0321 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 21.29 | 0.8133 | 0.0244 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 20.57 | 0.7902 | 0.0287 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 21.16 | 0.8125 | 0.0254 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 20.55 | 0.7906 | 0.0285 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 18.70 | 0.7213 | 0.0439 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 18.05 | 0.7009 | 0.0462 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 21.60 | 0.8289 | 0.0238 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 20.50 | 0.7927 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 21.76 | 0.8305 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 20.49 | 0.7911 | 0.0282 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 20.76 | 0.7989 | 0.0285 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 19.87 | 0.7712 | 0.0323 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 21.66 | 0.8267 | 0.0241 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 20.45 | 0.7884 | 0.0290 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 21.37 | 0.8195 | 0.0249 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 20.36 | 0.7867 | 0.0288 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 17.79 | 0.7132 | 0.0462 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 17.54 | 0.7069 | 0.0470 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 19.98 | 0.8117 | 0.0268 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 19.48 | 0.7906 | 0.0297 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 19.92 | 0.8069 | 0.0272 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 19.45 | 0.7875 | 0.0303 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 19.33 | 0.7847 | 0.0321 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 18.99 | 0.7711 | 0.0340 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 19.90 | 0.8043 | 0.0277 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 19.40 | 0.7841 | 0.0310 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 19.77 | 0.8046 | 0.0284 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 19.37 | 0.7856 | 0.0306 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.80 | 0.7163 | 0.0458 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 17.33 | 0.7008 | 0.0471 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 20.14 | 0.8214 | 0.0269 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 19.38 | 0.7882 | 0.0297 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 20.25 | 0.8221 | 0.0266 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 19.37 | 0.7860 | 0.0303 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 19.45 | 0.7920 | 0.0314 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 18.85 | 0.7677 | 0.0341 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 20.18 | 0.8183 | 0.0274 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 19.34 | 0.7832 | 0.0310 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 19.94 | 0.8122 | 0.0279 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 19.26 | 0.7823 | 0.0307 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 17.34 | 0.7055 | 0.0432 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.24 | 0.7017 | 0.0429 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 18.72 | 0.7840 | 0.0310 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 18.54 | 0.7714 | 0.0317 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 18.68 | 0.7807 | 0.0313 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 18.53 | 0.7701 | 0.0319 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 18.33 | 0.7617 | 0.0348 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 18.20 | 0.7542 | 0.0351 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 18.66 | 0.7786 | 0.0317 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 18.51 | 0.7678 | 0.0323 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 18.61 | 0.7781 | 0.0323 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 18.47 | 0.7662 | 0.0327 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 17.34 | 0.7081 | 0.0431 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 17.07 | 0.6970 | 0.0430 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 18.81 | 0.7916 | 0.0310 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 18.47 | 0.7687 | 0.0314 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 18.87 | 0.7923 | 0.0310 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 18.48 | 0.7680 | 0.0316 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 18.39 | 0.7676 | 0.0345 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 18.10 | 0.7510 | 0.0350 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 18.83 | 0.7892 | 0.0316 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 18.46 | 0.7659 | 0.0320 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 18.70 | 0.7838 | 0.0320 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 18.39 | 0.7631 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 17.89 | 0.6993 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 19.78 | 0.7833 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 19.72 | 0.7837 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 18.88 | 0.7521 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 19.63 | 0.7803 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 19.34 | 0.7700 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.82 | 0.6931 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.95 | 0.7474 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 18.99 | 0.7558 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.37 | 0.7254 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 19.15 | 0.7562 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.70 | 0.7370 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 15.76 | 0.6543 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 16.32 | 0.6831 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 16.22 | 0.6835 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 16.10 | 0.6730 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 16.17 | 0.6824 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 16.26 | 0.6797 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 15.95 | 0.6552 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 16.52 | 0.6893 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 16.43 | 0.6908 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 16.31 | 0.6774 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 16.39 | 0.6913 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 16.48 | 0.6854 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 15.65 | 0.6521 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 16.16 | 0.6791 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 16.09 | 0.6786 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 15.97 | 0.6703 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 16.06 | 0.6787 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 16.11 | 0.6763 | 0.0333 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 17.76 | 0.7027 | 0.0425 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 19.23 | 0.7766 | 0.0308 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 19.15 | 0.7771 | 0.0303 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 18.52 | 0.7503 | 0.0366 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 19.08 | 0.7744 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 18.90 | 0.7656 | 0.0335 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 17.37 | 0.6873 | 0.0388 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 18.31 | 0.7403 | 0.0314 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 18.37 | 0.7487 | 0.0311 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 17.83 | 0.7187 | 0.0350 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 18.51 | 0.7495 | 0.0311 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 18.10 | 0.7299 | 0.0331 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 15.49 | 0.6526 | 0.0389 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 15.97 | 0.6804 | 0.0333 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 15.87 | 0.6807 | 0.0334 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 15.78 | 0.6706 | 0.0357 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 15.82 | 0.6798 | 0.0337 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 15.92 | 0.6771 | 0.0343 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 15.69 | 0.6530 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 16.20 | 0.6867 | 0.0332 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 16.10 | 0.6882 | 0.0332 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 16.01 | 0.6747 | 0.0350 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 16.07 | 0.6886 | 0.0332 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 16.16 | 0.6824 | 0.0340 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 15.39 | 0.6503 | 0.0380 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 15.83 | 0.6766 | 0.0336 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 15.76 | 0.6760 | 0.0337 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 15.67 | 0.6680 | 0.0351 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 15.73 | 0.6762 | 0.0338 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 15.80 | 0.6737 | 0.0342 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 17.89 | 0.6973 | 0.0479 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 19.78 | 0.7825 | 0.0329 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 19.72 | 0.7832 | 0.0317 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 18.88 | 0.7506 | 0.0406 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 19.64 | 0.7797 | 0.0321 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 19.34 | 0.7686 | 0.0364 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.69 | 0.6923 | 0.0479 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 19.70 | 0.7801 | 0.0326 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 19.64 | 0.7814 | 0.0316 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 18.75 | 0.7476 | 0.0404 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 19.56 | 0.7786 | 0.0321 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 19.23 | 0.7657 | 0.0362 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.82 | 0.6924 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.96 | 0.7477 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 19.00 | 0.7560 | 0.0302 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.38 | 0.7251 | 0.0342 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 19.16 | 0.7562 | 0.0303 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.71 | 0.7369 | 0.0321 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.71 | 0.6896 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 18.84 | 0.7437 | 0.0302 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 18.90 | 0.7531 | 0.0300 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 18.27 | 0.7214 | 0.0342 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 19.07 | 0.7542 | 0.0300 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 18.60 | 0.7327 | 0.0320 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 15.76 | 0.6541 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 16.32 | 0.6832 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 16.22 | 0.6836 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 16.10 | 0.6730 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 16.17 | 0.6827 | 0.0328 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 16.27 | 0.6797 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 15.64 | 0.6501 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 16.16 | 0.6743 | 0.0327 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 16.06 | 0.6744 | 0.0326 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 15.96 | 0.6665 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 16.01 | 0.6737 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 16.12 | 0.6718 | 0.0336 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 15.95 | 0.6551 | 0.0374 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 16.52 | 0.6897 | 0.0323 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 16.43 | 0.6913 | 0.0323 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 16.31 | 0.6774 | 0.0342 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 16.39 | 0.6916 | 0.0323 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 16.48 | 0.6855 | 0.0330 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 15.85 | 0.6529 | 0.0375 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 16.37 | 0.6827 | 0.0324 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 16.28 | 0.6841 | 0.0323 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 16.18 | 0.6722 | 0.0343 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 16.25 | 0.6852 | 0.0324 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 16.34 | 0.6791 | 0.0332 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 15.65 | 0.6520 | 0.0373 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 16.16 | 0.6792 | 0.0327 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 16.09 | 0.6787 | 0.0328 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 15.97 | 0.6704 | 0.0343 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 16.05 | 0.6789 | 0.0329 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 16.11 | 0.6764 | 0.0333 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 15.53 | 0.6479 | 0.0375 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 16.01 | 0.6704 | 0.0328 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 15.93 | 0.6695 | 0.0329 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 15.84 | 0.6640 | 0.0345 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 15.91 | 0.6700 | 0.0330 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 15.98 | 0.6685 | 0.0334 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.98 | 0.6930 | 0.0482 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 19.79 | 0.7820 | 0.0328 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 19.76 | 0.7779 | 0.0313 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 18.82 | 0.7460 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 19.71 | 0.7824 | 0.0314 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 19.35 | 0.7693 | 0.0363 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.66 | 0.6817 | 0.0491 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 19.80 | 0.7824 | 0.0324 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 19.74 | 0.7791 | 0.0313 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 18.67 | 0.7418 | 0.0413 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 19.77 | 0.7852 | 0.0311 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 19.01 | 0.7523 | 0.0379 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 17.69 | 0.6818 | 0.0391 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 19.03 | 0.7532 | 0.0301 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 19.03 | 0.7616 | 0.0300 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 18.45 | 0.7276 | 0.0341 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 18.87 | 0.7416 | 0.0314 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 18.79 | 0.7414 | 0.0320 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 17.56 | 0.6777 | 0.0396 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 18.94 | 0.7464 | 0.0299 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 19.01 | 0.7564 | 0.0298 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 18.26 | 0.7192 | 0.0346 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 19.12 | 0.7547 | 0.0300 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 18.76 | 0.7418 | 0.0322 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 15.76 | 0.6541 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 16.32 | 0.6832 | 0.0325 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 16.22 | 0.6836 | 0.0325 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 16.10 | 0.6730 | 0.0349 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 16.17 | 0.6827 | 0.0328 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 16.27 | 0.6797 | 0.0334 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 15.50 | 0.6430 | 0.0392 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 16.16 | 0.6743 | 0.0327 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 16.06 | 0.6744 | 0.0326 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 15.85 | 0.6618 | 0.0355 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 16.01 | 0.6737 | 0.0330 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 16.18 | 0.6781 | 0.0339 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 15.95 | 0.6540 | 0.0375 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 16.50 | 0.6849 | 0.0326 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 16.42 | 0.6901 | 0.0322 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 16.29 | 0.6741 | 0.0343 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 16.35 | 0.6850 | 0.0324 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 16.46 | 0.6821 | 0.0332 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 15.81 | 0.6480 | 0.0380 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 16.35 | 0.6774 | 0.0326 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 15.87 | 0.6582 | 0.0346 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 16.17 | 0.6693 | 0.0345 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 16.24 | 0.6805 | 0.0324 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 16.32 | 0.6752 | 0.0333 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 15.65 | 0.6520 | 0.0373 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 16.16 | 0.6792 | 0.0327 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 16.09 | 0.6787 | 0.0328 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 15.97 | 0.6704 | 0.0343 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 16.05 | 0.6789 | 0.0329 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 16.11 | 0.6764 | 0.0333 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 15.49 | 0.6448 | 0.0378 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 16.01 | 0.6704 | 0.0328 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 15.53 | 0.6436 | 0.0352 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 15.84 | 0.6640 | 0.0345 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 15.91 | 0.6700 | 0.0330 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 15.98 | 0.6685 | 0.0334 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8166 | 0.0498 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8102 | 0.0518 | 1.00 |
| flow_s0.5_uniform | 19.42 | 0.7885 | 0.0548 | 1.00 |
| flow_s1.0_oracle | 19.19 | 0.8296 | 0.0544 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| flow_s1.0_uniform | 18.45 | 0.7883 | 0.0601 | 1.00 |
| gs_tok448_nat_dil_al | 22.08 | 0.8042 | 0.0670 | 1.00 |
| gs_tok448_nat_dil_al+reg | 22.26 | 0.8106 | 0.0668 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 24.62 | 0.8747 | 0.0366 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 25.39 | 0.8957 | 0.0334 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 24.57 | 0.8708 | 0.0376 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 25.26 | 0.8915 | 0.0340 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 23.99 | 0.8605 | 0.0437 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 24.51 | 0.8755 | 0.0416 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 24.52 | 0.8663 | 0.0390 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 25.22 | 0.8875 | 0.0351 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 24.49 | 0.8718 | 0.0383 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 25.12 | 0.8902 | 0.0354 | 1.00 |
| gs_tok448_nat_dil_alv | 21.94 | 0.8042 | 0.0666 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 22.33 | 0.8146 | 0.0664 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 24.57 | 0.8743 | 0.0367 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 25.49 | 0.8981 | 0.0336 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 24.52 | 0.8706 | 0.0377 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 25.60 | 0.8972 | 0.0336 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 23.91 | 0.8604 | 0.0434 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 24.70 | 0.8802 | 0.0408 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 24.49 | 0.8663 | 0.0391 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 25.48 | 0.8916 | 0.0351 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 24.42 | 0.8715 | 0.0381 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 25.35 | 0.8945 | 0.0352 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 16.31 | 0.7510 | 0.1168 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 19.58 | 0.8290 | 0.0779 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 21.79 | 0.8401 | 0.0652 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 16.70 | 0.7923 | 0.1013 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 22.42 | 0.8402 | 0.0625 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 17.43 | 0.8084 | 0.0921 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 16.27 | 0.7517 | 0.1157 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 19.50 | 0.8289 | 0.0773 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 21.74 | 0.8402 | 0.0650 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 16.65 | 0.7927 | 0.1003 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 22.40 | 0.8404 | 0.0623 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 17.38 | 0.8086 | 0.0912 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.03 | 0.5782 | 0.2879 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.38 | 0.6239 | 0.2671 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 9.66 | 0.6290 | 0.2599 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.09 | 0.6038 | 0.2799 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 9.78 | 0.6292 | 0.2572 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.19 | 0.6136 | 0.2749 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 9.02 | 0.5769 | 0.2879 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 9.37 | 0.6228 | 0.2674 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 9.65 | 0.6282 | 0.2602 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 9.08 | 0.6025 | 0.2800 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 9.77 | 0.6287 | 0.2574 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 9.18 | 0.6123 | 0.2750 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.99 | 0.3164 | 0.3466 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 7.17 | 0.3378 | 0.3365 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 7.33 | 0.3403 | 0.3333 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 7.02 | 0.3304 | 0.3422 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 7.39 | 0.3398 | 0.3319 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 7.07 | 0.3352 | 0.3395 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.98 | 0.3153 | 0.3468 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 7.15 | 0.3333 | 0.3368 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 7.31 | 0.3358 | 0.3336 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 7.01 | 0.3273 | 0.3423 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 7.38 | 0.3354 | 0.3322 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 7.06 | 0.3313 | 0.3397 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.82 | 0.5238 | 0.3280 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 8.02 | 0.5479 | 0.3177 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 8.17 | 0.5506 | 0.3133 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 7.86 | 0.5377 | 0.3237 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 8.21 | 0.5505 | 0.3118 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 7.91 | 0.5424 | 0.3212 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.82 | 0.5226 | 0.3281 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 8.01 | 0.5456 | 0.3180 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 8.16 | 0.5482 | 0.3135 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 7.85 | 0.5359 | 0.3238 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 8.20 | 0.5484 | 0.3120 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 7.91 | 0.5402 | 0.3213 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 6.38 | 0.2925 | 0.3661 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 6.47 | 0.3063 | 0.3600 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 6.55 | 0.3075 | 0.3580 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 6.40 | 0.3020 | 0.3630 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 6.57 | 0.3069 | 0.3571 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 6.42 | 0.3049 | 0.3614 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 6.38 | 0.2910 | 0.3663 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 6.46 | 0.3021 | 0.3604 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 6.54 | 0.3033 | 0.3584 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 6.39 | 0.2992 | 0.3632 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 6.56 | 0.3027 | 0.3574 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 6.42 | 0.3012 | 0.3617 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 23.48 | 0.8554 | 0.0510 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 23.36 | 0.8541 | 0.0516 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 25.09 | 0.8889 | 0.0366 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 24.79 | 0.8828 | 0.0380 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 25.03 | 0.8880 | 0.0365 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 24.77 | 0.8825 | 0.0381 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 24.64 | 0.8794 | 0.0410 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 24.44 | 0.8754 | 0.0419 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 25.01 | 0.8871 | 0.0368 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 24.73 | 0.8814 | 0.0386 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 24.94 | 0.8862 | 0.0381 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 24.72 | 0.8807 | 0.0393 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 23.48 | 0.8557 | 0.0508 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 23.16 | 0.8521 | 0.0516 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 25.17 | 0.8899 | 0.0368 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 24.68 | 0.8804 | 0.0381 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 25.24 | 0.8909 | 0.0366 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 24.67 | 0.8802 | 0.0383 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 24.71 | 0.8806 | 0.0408 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 24.30 | 0.8732 | 0.0419 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 25.18 | 0.8894 | 0.0369 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 24.64 | 0.8792 | 0.0387 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 25.06 | 0.8871 | 0.0381 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 24.59 | 0.8783 | 0.0393 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 22.27 | 0.8082 | 0.0668 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 22.08 | 0.8018 | 0.0670 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 25.38 | 0.8939 | 0.0334 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 24.62 | 0.8731 | 0.0366 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 25.26 | 0.8899 | 0.0340 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 24.57 | 0.8694 | 0.0376 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 24.51 | 0.8736 | 0.0416 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 23.99 | 0.8586 | 0.0437 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 25.22 | 0.8860 | 0.0351 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 24.52 | 0.8651 | 0.0390 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 25.11 | 0.8883 | 0.0355 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 24.49 | 0.8700 | 0.0383 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 22.34 | 0.8122 | 0.0664 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 21.94 | 0.8018 | 0.0666 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 25.49 | 0.8965 | 0.0336 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 24.57 | 0.8728 | 0.0367 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 25.60 | 0.8957 | 0.0336 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 24.52 | 0.8693 | 0.0377 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 24.70 | 0.8784 | 0.0408 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 23.91 | 0.8586 | 0.0434 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 25.48 | 0.8902 | 0.0351 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 24.49 | 0.8652 | 0.0391 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 25.34 | 0.8927 | 0.0353 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 24.42 | 0.8697 | 0.0381 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 22.92 | 0.8509 | 0.0478 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 22.91 | 0.8506 | 0.0472 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 24.68 | 0.8893 | 0.0347 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 24.48 | 0.8835 | 0.0350 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 24.63 | 0.8878 | 0.0349 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 24.47 | 0.8825 | 0.0353 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 24.20 | 0.8796 | 0.0387 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 24.05 | 0.8759 | 0.0387 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 24.61 | 0.8861 | 0.0353 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 24.44 | 0.8808 | 0.0358 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 24.54 | 0.8869 | 0.0361 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 24.38 | 0.8814 | 0.0362 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 22.97 | 0.8520 | 0.0475 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 22.79 | 0.8496 | 0.0470 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 24.77 | 0.8908 | 0.0345 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 24.44 | 0.8823 | 0.0348 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 24.83 | 0.8909 | 0.0345 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 24.44 | 0.8815 | 0.0350 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 24.28 | 0.8812 | 0.0383 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 23.99 | 0.8748 | 0.0385 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 24.77 | 0.8886 | 0.0350 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 24.42 | 0.8799 | 0.0355 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 24.65 | 0.8883 | 0.0358 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 24.33 | 0.8803 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 23.04 | 0.8484 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 24.61 | 0.8800 | 0.0384 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 24.75 | 0.8811 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 23.82 | 0.8680 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 24.72 | 0.8798 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 24.19 | 0.8746 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.15 | 0.8575 | 0.0441 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.17 | 0.8753 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 24.31 | 0.8773 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 23.64 | 0.8680 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 24.44 | 0.8770 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.91 | 0.8716 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 21.75 | 0.8529 | 0.0443 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 22.27 | 0.8644 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.29 | 0.8647 | 0.0395 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 22.04 | 0.8603 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.28 | 0.8641 | 0.0395 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 22.20 | 0.8630 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 21.85 | 0.8541 | 0.0431 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 22.38 | 0.8652 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 22.38 | 0.8655 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 22.16 | 0.8616 | 0.0408 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 22.41 | 0.8654 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 22.32 | 0.8640 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 21.66 | 0.8538 | 0.0432 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 22.13 | 0.8635 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 22.13 | 0.8634 | 0.0394 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.94 | 0.8605 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 22.16 | 0.8632 | 0.0395 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 22.07 | 0.8625 | 0.0404 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 22.50 | 0.8385 | 0.0539 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 24.02 | 0.8741 | 0.0405 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 24.24 | 0.8758 | 0.0390 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 23.26 | 0.8613 | 0.0479 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 24.22 | 0.8746 | 0.0388 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 23.59 | 0.8677 | 0.0447 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 22.59 | 0.8481 | 0.0482 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 23.61 | 0.8706 | 0.0392 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 23.89 | 0.8732 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 23.06 | 0.8615 | 0.0446 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 24.04 | 0.8731 | 0.0379 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 23.26 | 0.8655 | 0.0424 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 21.46 | 0.8491 | 0.0466 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 21.97 | 0.8622 | 0.0412 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.06 | 0.8625 | 0.0407 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 21.75 | 0.8578 | 0.0440 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.08 | 0.8621 | 0.0407 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 21.87 | 0.8609 | 0.0426 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 21.60 | 0.8511 | 0.0447 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 22.15 | 0.8634 | 0.0403 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 22.19 | 0.8638 | 0.0399 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 21.92 | 0.8599 | 0.0421 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 22.24 | 0.8637 | 0.0401 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 22.08 | 0.8624 | 0.0411 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 21.44 | 0.8518 | 0.0446 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 21.91 | 0.8622 | 0.0406 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 21.95 | 0.8621 | 0.0403 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.72 | 0.8595 | 0.0422 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 22.00 | 0.8620 | 0.0405 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 21.84 | 0.8616 | 0.0414 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 21.63 | 0.7862 | 0.0778 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 23.27 | 0.8460 | 0.0538 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 23.59 | 0.8497 | 0.0497 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 22.48 | 0.8255 | 0.0669 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 23.62 | 0.8472 | 0.0495 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 22.84 | 0.8364 | 0.0607 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 21.53 | 0.7866 | 0.0770 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 23.22 | 0.8459 | 0.0534 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 23.53 | 0.8494 | 0.0496 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 22.41 | 0.8259 | 0.0659 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 23.57 | 0.8472 | 0.0492 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 22.78 | 0.8367 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.77 | 0.8468 | 0.0489 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.94 | 0.8710 | 0.0392 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.21 | 0.8731 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.31 | 0.8612 | 0.0450 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 24.34 | 0.8722 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.54 | 0.8654 | 0.0425 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.69 | 0.8461 | 0.0488 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 23.84 | 0.8696 | 0.0393 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 24.13 | 0.8721 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 23.22 | 0.8602 | 0.0450 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 24.27 | 0.8715 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 23.44 | 0.8641 | 0.0424 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 21.65 | 0.8492 | 0.0463 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 22.23 | 0.8630 | 0.0407 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.32 | 0.8630 | 0.0404 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 21.98 | 0.8584 | 0.0435 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.32 | 0.8624 | 0.0405 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 22.12 | 0.8617 | 0.0420 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 21.54 | 0.8476 | 0.0462 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 22.06 | 0.8592 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 22.14 | 0.8591 | 0.0407 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 21.83 | 0.8557 | 0.0436 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 22.15 | 0.8585 | 0.0408 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 21.96 | 0.8584 | 0.0421 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 21.79 | 0.8516 | 0.0444 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 22.39 | 0.8642 | 0.0397 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 22.44 | 0.8647 | 0.0393 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 22.14 | 0.8607 | 0.0418 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 22.47 | 0.8642 | 0.0396 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 22.32 | 0.8633 | 0.0406 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 21.69 | 0.8505 | 0.0444 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 22.23 | 0.8615 | 0.0398 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 22.27 | 0.8619 | 0.0394 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 22.00 | 0.8585 | 0.0419 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 22.32 | 0.8616 | 0.0398 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 22.16 | 0.8608 | 0.0408 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 21.63 | 0.8525 | 0.0441 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 22.15 | 0.8632 | 0.0399 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 22.20 | 0.8631 | 0.0396 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.94 | 0.8605 | 0.0415 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 22.24 | 0.8626 | 0.0400 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 22.08 | 0.8626 | 0.0407 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 21.52 | 0.8510 | 0.0441 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 21.99 | 0.8597 | 0.0401 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 22.03 | 0.8594 | 0.0398 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 21.80 | 0.8578 | 0.0417 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 22.08 | 0.8590 | 0.0402 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 21.93 | 0.8594 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 21.40 | 0.7824 | 0.0791 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 23.29 | 0.8466 | 0.0538 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 23.51 | 0.8493 | 0.0490 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 22.25 | 0.8215 | 0.0679 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 23.69 | 0.8503 | 0.0485 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 22.85 | 0.8370 | 0.0605 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 21.28 | 0.7796 | 0.0794 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 23.27 | 0.8471 | 0.0534 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 23.52 | 0.8497 | 0.0493 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 22.23 | 0.8221 | 0.0670 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 23.75 | 0.8524 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 22.44 | 0.8272 | 0.0618 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.57 | 0.8428 | 0.0492 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 24.04 | 0.8731 | 0.0390 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 24.29 | 0.8753 | 0.0381 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 23.35 | 0.8617 | 0.0450 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 24.00 | 0.8657 | 0.0389 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 23.60 | 0.8668 | 0.0424 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.45 | 0.8400 | 0.0493 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 23.89 | 0.8702 | 0.0392 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 24.19 | 0.8732 | 0.0381 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 23.17 | 0.8583 | 0.0454 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 24.29 | 0.8716 | 0.0379 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 23.52 | 0.8663 | 0.0425 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 21.65 | 0.8492 | 0.0463 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 22.23 | 0.8630 | 0.0407 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.32 | 0.8630 | 0.0404 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 21.98 | 0.8584 | 0.0435 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.32 | 0.8624 | 0.0405 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 22.12 | 0.8617 | 0.0420 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 21.43 | 0.8443 | 0.0467 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 22.06 | 0.8592 | 0.0409 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 22.14 | 0.8591 | 0.0407 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 21.77 | 0.8539 | 0.0438 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 22.15 | 0.8585 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 22.03 | 0.8605 | 0.0420 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 21.79 | 0.8513 | 0.0444 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 22.37 | 0.8630 | 0.0398 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 22.43 | 0.8644 | 0.0393 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 22.12 | 0.8600 | 0.0418 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 22.43 | 0.8627 | 0.0397 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 22.29 | 0.8626 | 0.0407 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 21.67 | 0.8487 | 0.0446 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 22.20 | 0.8604 | 0.0399 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 21.85 | 0.8512 | 0.0410 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 21.99 | 0.8579 | 0.0419 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 22.31 | 0.8606 | 0.0398 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 22.14 | 0.8600 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 21.63 | 0.8525 | 0.0441 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 22.15 | 0.8632 | 0.0399 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 22.20 | 0.8631 | 0.0396 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.94 | 0.8605 | 0.0415 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 22.24 | 0.8626 | 0.0400 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 22.08 | 0.8626 | 0.0407 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 21.50 | 0.8496 | 0.0443 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 21.99 | 0.8597 | 0.0401 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 21.61 | 0.8486 | 0.0414 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 21.80 | 0.8578 | 0.0417 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 22.08 | 0.8590 | 0.0402 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 21.93 | 0.8594 | 0.0408 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.88 | 0.8768 | 0.0597 | 1.00 |
| flow_s0.5_pose | 21.24 | 0.8722 | 0.0608 | 1.00 |
| flow_s0.5_uniform | 21.45 | 0.8596 | 0.0657 | 1.00 |
| flow_s1.0_oracle | 21.12 | 0.8872 | 0.0601 | 1.00 |
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| flow_s1.0_uniform | 20.48 | 0.8603 | 0.0677 | 1.00 |
| gs_tok448_nat_dil_al | 23.83 | 0.8590 | 0.0835 | 1.00 |
| gs_tok448_nat_dil_al+reg | 24.12 | 0.8638 | 0.0812 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 26.42 | 0.9105 | 0.0479 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 27.09 | 0.9243 | 0.0425 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 26.39 | 0.9065 | 0.0496 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 27.01 | 0.9202 | 0.0436 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 25.89 | 0.9029 | 0.0544 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 26.36 | 0.9131 | 0.0513 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 26.36 | 0.9020 | 0.0516 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 26.98 | 0.9161 | 0.0456 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 26.33 | 0.9099 | 0.0491 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 26.87 | 0.9221 | 0.0449 | 1.00 |
| gs_tok448_nat_dil_alv | 23.70 | 0.8590 | 0.0830 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 24.19 | 0.8661 | 0.0802 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 26.34 | 0.9102 | 0.0478 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 27.12 | 0.9256 | 0.0424 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 26.32 | 0.9064 | 0.0493 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 27.27 | 0.9240 | 0.0428 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 25.78 | 0.9029 | 0.0541 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 26.53 | 0.9156 | 0.0497 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 26.30 | 0.9022 | 0.0514 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 27.19 | 0.9189 | 0.0451 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 26.23 | 0.9096 | 0.0489 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 27.07 | 0.9245 | 0.0440 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 20.09 | 0.8254 | 0.1211 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 21.05 | 0.8722 | 0.0910 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 21.00 | 0.8717 | 0.0892 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 20.64 | 0.8568 | 0.1039 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 20.96 | 0.8676 | 0.0900 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 20.86 | 0.8661 | 0.0966 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 20.01 | 0.8257 | 0.1207 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 20.93 | 0.8721 | 0.0906 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 20.90 | 0.8716 | 0.0889 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 20.54 | 0.8568 | 0.1035 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 20.87 | 0.8678 | 0.0897 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 20.75 | 0.8660 | 0.0962 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.16 | 0.6157 | 0.3253 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.24 | 0.6377 | 0.3125 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 8.33 | 0.6360 | 0.3098 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.19 | 0.6312 | 0.3192 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 8.38 | 0.6332 | 0.3092 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.21 | 0.6355 | 0.3159 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.16 | 0.6148 | 0.3255 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 8.24 | 0.6367 | 0.3123 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 8.33 | 0.6350 | 0.3095 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 8.18 | 0.6302 | 0.3191 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 8.38 | 0.6325 | 0.3090 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 8.20 | 0.6344 | 0.3158 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.05 | 0.3292 | 0.3813 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 6.08 | 0.3407 | 0.3735 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 6.14 | 0.3395 | 0.3720 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 6.06 | 0.3376 | 0.3772 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 6.16 | 0.3372 | 0.3719 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 6.07 | 0.3401 | 0.3752 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.04 | 0.3286 | 0.3813 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 6.08 | 0.3380 | 0.3737 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 6.13 | 0.3368 | 0.3722 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 6.06 | 0.3357 | 0.3773 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 6.15 | 0.3346 | 0.3722 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 6.07 | 0.3378 | 0.3754 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.46 | 0.5755 | 0.3649 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 7.50 | 0.5873 | 0.3581 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 7.55 | 0.5855 | 0.3568 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 7.47 | 0.5831 | 0.3614 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 7.57 | 0.5838 | 0.3566 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 7.49 | 0.5858 | 0.3597 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.45 | 0.5747 | 0.3651 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 7.50 | 0.5858 | 0.3585 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 7.55 | 0.5839 | 0.3571 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 7.47 | 0.5821 | 0.3618 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 7.56 | 0.5823 | 0.3569 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 7.48 | 0.5844 | 0.3601 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.70 | 0.3091 | 0.4021 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 5.72 | 0.3163 | 0.3975 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 5.74 | 0.3147 | 0.3969 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 5.71 | 0.3142 | 0.3994 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 5.75 | 0.3130 | 0.3968 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 5.72 | 0.3159 | 0.3983 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.70 | 0.3082 | 0.4022 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 5.71 | 0.3137 | 0.3978 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 5.74 | 0.3121 | 0.3972 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 5.71 | 0.3125 | 0.3997 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 5.75 | 0.3104 | 0.3970 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 5.71 | 0.3138 | 0.3986 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 25.79 | 0.9047 | 0.0542 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 25.64 | 0.9037 | 0.0550 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 27.60 | 0.9251 | 0.0413 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 27.28 | 0.9214 | 0.0428 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 27.55 | 0.9246 | 0.0412 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 27.25 | 0.9212 | 0.0430 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 27.12 | 0.9196 | 0.0457 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 26.91 | 0.9170 | 0.0463 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 27.52 | 0.9240 | 0.0414 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 27.22 | 0.9205 | 0.0434 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 27.43 | 0.9237 | 0.0429 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 27.21 | 0.9202 | 0.0439 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 25.79 | 0.9048 | 0.0538 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 25.46 | 0.9026 | 0.0550 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 27.68 | 0.9259 | 0.0414 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 27.15 | 0.9198 | 0.0428 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 27.75 | 0.9263 | 0.0407 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 27.13 | 0.9196 | 0.0429 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 27.20 | 0.9204 | 0.0452 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 26.77 | 0.9157 | 0.0463 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 27.68 | 0.9254 | 0.0411 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 27.10 | 0.9190 | 0.0433 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 27.56 | 0.9243 | 0.0426 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 27.07 | 0.9186 | 0.0439 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 24.01 | 0.8761 | 0.0713 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 23.78 | 0.8721 | 0.0724 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 26.49 | 0.9225 | 0.0441 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 26.03 | 0.9127 | 0.0476 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 26.45 | 0.9205 | 0.0444 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 26.01 | 0.9107 | 0.0483 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 25.84 | 0.9128 | 0.0513 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 25.52 | 0.9055 | 0.0534 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 26.43 | 0.9183 | 0.0452 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 25.99 | 0.9084 | 0.0493 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 26.26 | 0.9202 | 0.0465 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 25.91 | 0.9114 | 0.0491 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 24.05 | 0.8778 | 0.0708 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 23.65 | 0.8715 | 0.0724 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 26.59 | 0.9243 | 0.0443 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 25.97 | 0.9121 | 0.0474 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 26.68 | 0.9236 | 0.0440 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 25.96 | 0.9102 | 0.0481 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 25.97 | 0.9151 | 0.0507 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 25.43 | 0.9050 | 0.0533 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 26.62 | 0.9208 | 0.0451 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 25.94 | 0.9081 | 0.0491 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 26.43 | 0.9225 | 0.0462 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 25.84 | 0.9107 | 0.0490 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 24.48 | 0.8984 | 0.0569 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 24.40 | 0.8976 | 0.0566 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 25.95 | 0.9199 | 0.0453 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 25.77 | 0.9167 | 0.0460 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 25.92 | 0.9191 | 0.0455 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 25.76 | 0.9162 | 0.0461 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 25.57 | 0.9147 | 0.0488 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 25.45 | 0.9126 | 0.0492 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 25.90 | 0.9182 | 0.0458 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 25.75 | 0.9154 | 0.0465 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 25.83 | 0.9188 | 0.0465 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 25.69 | 0.9156 | 0.0469 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 24.49 | 0.8986 | 0.0569 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 24.28 | 0.8966 | 0.0566 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 26.01 | 0.9210 | 0.0454 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 25.71 | 0.9156 | 0.0457 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 26.05 | 0.9209 | 0.0453 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 25.71 | 0.9151 | 0.0458 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 25.63 | 0.9157 | 0.0488 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 25.37 | 0.9115 | 0.0490 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 26.01 | 0.9198 | 0.0457 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 25.70 | 0.9144 | 0.0462 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 25.91 | 0.9197 | 0.0465 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 25.63 | 0.9145 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 25.32 | 0.9008 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 26.82 | 0.9194 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 26.75 | 0.9195 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 26.18 | 0.9127 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 26.66 | 0.9186 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 26.53 | 0.9167 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.28 | 0.9042 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.16 | 0.9143 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 26.17 | 0.9153 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.74 | 0.9104 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 26.28 | 0.9152 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.99 | 0.9126 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 23.71 | 0.9003 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 24.17 | 0.9067 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 24.08 | 0.9068 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 23.99 | 0.9044 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 24.02 | 0.9065 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 24.12 | 0.9060 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 23.81 | 0.9006 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 24.26 | 0.9068 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 24.17 | 0.9069 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 24.10 | 0.9048 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 24.14 | 0.9070 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 24.23 | 0.9062 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 23.61 | 0.9005 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 23.99 | 0.9058 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 23.93 | 0.9057 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.86 | 0.9042 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 23.90 | 0.9057 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 23.96 | 0.9053 | 0.0477 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 24.84 | 0.8967 | 0.0561 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 26.24 | 0.9164 | 0.0458 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 26.16 | 0.9162 | 0.0452 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 25.65 | 0.9102 | 0.0517 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 26.09 | 0.9153 | 0.0456 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 25.99 | 0.9141 | 0.0487 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 24.80 | 0.9004 | 0.0517 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 25.64 | 0.9119 | 0.0459 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 25.64 | 0.9126 | 0.0457 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 25.23 | 0.9079 | 0.0496 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 25.75 | 0.9124 | 0.0458 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 25.47 | 0.9104 | 0.0479 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 23.39 | 0.8986 | 0.0517 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 23.83 | 0.9055 | 0.0478 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 23.74 | 0.9053 | 0.0481 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 23.66 | 0.9033 | 0.0500 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 23.68 | 0.9049 | 0.0483 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 23.79 | 0.9050 | 0.0488 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 23.52 | 0.8991 | 0.0506 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 23.97 | 0.9058 | 0.0474 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 23.88 | 0.9057 | 0.0476 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 23.81 | 0.9039 | 0.0487 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 23.84 | 0.9056 | 0.0478 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 23.94 | 0.9053 | 0.0479 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 23.33 | 0.8995 | 0.0507 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 23.70 | 0.9050 | 0.0478 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 23.63 | 0.9047 | 0.0482 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.58 | 0.9035 | 0.0489 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 23.60 | 0.9046 | 0.0483 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 23.67 | 0.9047 | 0.0482 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 24.22 | 0.8682 | 0.0730 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 26.03 | 0.9045 | 0.0531 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 25.96 | 0.9033 | 0.0521 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 25.27 | 0.8936 | 0.0636 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 25.86 | 0.9003 | 0.0530 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 25.70 | 0.9003 | 0.0583 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 24.07 | 0.8677 | 0.0730 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 25.97 | 0.9039 | 0.0529 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 25.89 | 0.9027 | 0.0519 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 25.19 | 0.8933 | 0.0633 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 25.80 | 0.8999 | 0.0529 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 25.63 | 0.8998 | 0.0582 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.06 | 0.9002 | 0.0522 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.04 | 0.9127 | 0.0458 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 26.04 | 0.9132 | 0.0455 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.57 | 0.9083 | 0.0499 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 26.14 | 0.9126 | 0.0457 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.85 | 0.9109 | 0.0479 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 24.95 | 0.8993 | 0.0524 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 25.96 | 0.9115 | 0.0458 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 25.98 | 0.9121 | 0.0453 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 25.49 | 0.9074 | 0.0500 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 26.08 | 0.9117 | 0.0456 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 25.78 | 0.9098 | 0.0479 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 23.61 | 0.8984 | 0.0516 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 24.12 | 0.9059 | 0.0474 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 24.02 | 0.9058 | 0.0477 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 23.92 | 0.9035 | 0.0496 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 23.96 | 0.9052 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 24.06 | 0.9053 | 0.0484 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 23.51 | 0.8974 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 23.98 | 0.9035 | 0.0477 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 23.89 | 0.9033 | 0.0479 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 23.80 | 0.9018 | 0.0499 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 23.82 | 0.9027 | 0.0484 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 23.94 | 0.9032 | 0.0487 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 23.74 | 0.8994 | 0.0504 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 24.24 | 0.9063 | 0.0470 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 24.15 | 0.9062 | 0.0472 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 24.06 | 0.9045 | 0.0484 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 24.10 | 0.9061 | 0.0474 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 24.20 | 0.9060 | 0.0475 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 23.65 | 0.8987 | 0.0506 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 24.11 | 0.9045 | 0.0473 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 24.03 | 0.9044 | 0.0474 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 23.96 | 0.9031 | 0.0487 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 23.99 | 0.9044 | 0.0476 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 24.09 | 0.9043 | 0.0479 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 23.56 | 0.8998 | 0.0504 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 23.98 | 0.9055 | 0.0473 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 23.91 | 0.9052 | 0.0477 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.83 | 0.9040 | 0.0484 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 23.86 | 0.9050 | 0.0479 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 23.94 | 0.9052 | 0.0477 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 23.46 | 0.8988 | 0.0505 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 23.85 | 0.9032 | 0.0476 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 23.78 | 0.9028 | 0.0479 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 23.72 | 0.9023 | 0.0487 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 23.74 | 0.9027 | 0.0481 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 23.83 | 0.9032 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 24.32 | 0.8679 | 0.0717 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 26.07 | 0.9049 | 0.0530 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 25.97 | 0.9036 | 0.0513 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 25.21 | 0.8926 | 0.0632 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 25.93 | 0.9024 | 0.0518 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 25.72 | 0.9006 | 0.0581 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 24.09 | 0.8659 | 0.0731 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 26.04 | 0.9047 | 0.0528 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 25.94 | 0.9033 | 0.0515 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 25.13 | 0.8920 | 0.0632 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 25.96 | 0.9032 | 0.0512 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 25.45 | 0.8958 | 0.0591 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 24.89 | 0.8978 | 0.0526 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 26.10 | 0.9139 | 0.0452 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 26.08 | 0.9144 | 0.0451 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 25.60 | 0.9087 | 0.0493 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 25.93 | 0.9092 | 0.0467 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 25.90 | 0.9117 | 0.0474 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 24.77 | 0.8965 | 0.0533 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 26.02 | 0.9120 | 0.0455 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 26.05 | 0.9127 | 0.0452 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 25.44 | 0.9066 | 0.0498 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 26.11 | 0.9118 | 0.0455 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 25.88 | 0.9117 | 0.0477 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 23.61 | 0.8984 | 0.0516 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 24.12 | 0.9059 | 0.0474 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 24.02 | 0.9058 | 0.0477 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 23.92 | 0.9035 | 0.0496 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 23.96 | 0.9052 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 24.06 | 0.9053 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 23.37 | 0.8958 | 0.0525 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 23.98 | 0.9035 | 0.0477 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 23.89 | 0.9033 | 0.0479 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 23.70 | 0.9008 | 0.0501 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 23.82 | 0.9027 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 23.99 | 0.9048 | 0.0487 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 23.73 | 0.8992 | 0.0505 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 24.22 | 0.9055 | 0.0471 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 24.14 | 0.9061 | 0.0472 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 24.05 | 0.9040 | 0.0485 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 24.07 | 0.9051 | 0.0475 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 24.19 | 0.9055 | 0.0476 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 23.61 | 0.8977 | 0.0510 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 24.09 | 0.9038 | 0.0473 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 23.63 | 0.8989 | 0.0488 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 23.95 | 0.9027 | 0.0488 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 23.98 | 0.9037 | 0.0476 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 24.08 | 0.9038 | 0.0479 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 23.56 | 0.8998 | 0.0504 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 23.98 | 0.9055 | 0.0473 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 23.91 | 0.9052 | 0.0477 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.83 | 0.9040 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 23.86 | 0.9050 | 0.0479 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 23.94 | 0.9052 | 0.0477 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 23.42 | 0.8981 | 0.0508 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 23.85 | 0.9032 | 0.0476 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 23.37 | 0.8973 | 0.0493 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 23.72 | 0.9023 | 0.0487 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 23.74 | 0.9027 | 0.0481 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 23.83 | 0.9032 | 0.0480 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.45 | 0.9592 | 0.0262 | 1.00 |
| flow_s0.5_pose | 32.82 | 0.9610 | 0.0252 | 1.00 |
| flow_s0.5_uniform | 32.06 | 0.9533 | 0.0285 | 1.00 |
| flow_s1.0_oracle | 33.41 | 0.9610 | 0.0236 | 1.00 |
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| flow_s1.0_uniform | 32.36 | 0.9509 | 0.0269 | 1.00 |
| gs_tok448_nat_dil_al | 29.12 | 0.9282 | 0.0546 | 1.00 |
| gs_tok448_nat_dil_al+reg | 29.37 | 0.9303 | 0.0524 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 31.31 | 0.9529 | 0.0302 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 32.09 | 0.9619 | 0.0263 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 31.24 | 0.9504 | 0.0319 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 31.98 | 0.9593 | 0.0274 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 31.24 | 0.9508 | 0.0332 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 31.79 | 0.9577 | 0.0302 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 31.27 | 0.9472 | 0.0337 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 31.92 | 0.9562 | 0.0290 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 31.43 | 0.9532 | 0.0302 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 32.25 | 0.9615 | 0.0267 | 1.00 |
| gs_tok448_nat_dil_alv | 29.27 | 0.9303 | 0.0541 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 29.49 | 0.9323 | 0.0517 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 31.41 | 0.9546 | 0.0301 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 32.09 | 0.9625 | 0.0260 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 31.32 | 0.9520 | 0.0317 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 32.01 | 0.9604 | 0.0270 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 31.39 | 0.9529 | 0.0328 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 32.23 | 0.9604 | 0.0292 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 31.33 | 0.9489 | 0.0335 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 31.98 | 0.9570 | 0.0287 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 31.56 | 0.9551 | 0.0300 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 32.45 | 0.9631 | 0.0262 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.19 | 0.8745 | 0.1121 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 19.15 | 0.8908 | 0.0920 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 19.28 | 0.8884 | 0.0900 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 18.48 | 0.8868 | 0.0994 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 19.34 | 0.8837 | 0.0914 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 18.67 | 0.8895 | 0.0952 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.19 | 0.8763 | 0.1113 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 19.12 | 0.8915 | 0.0914 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 19.25 | 0.8889 | 0.0896 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 18.47 | 0.8880 | 0.0987 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 19.31 | 0.8843 | 0.0909 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 18.65 | 0.8905 | 0.0944 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.51 | 0.6126 | 0.3601 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.55 | 0.6122 | 0.3564 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.65 | 0.6100 | 0.3537 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.52 | 0.6138 | 0.3588 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 6.71 | 0.6081 | 0.3530 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.53 | 0.6133 | 0.3581 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.51 | 0.6126 | 0.3602 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 6.55 | 0.6119 | 0.3565 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 6.65 | 0.6098 | 0.3537 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 6.52 | 0.6136 | 0.3587 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 6.71 | 0.6079 | 0.3530 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 6.53 | 0.6130 | 0.3580 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.29 | 0.3293 | 0.3957 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 5.31 | 0.3295 | 0.3933 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 5.36 | 0.3278 | 0.3916 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 5.29 | 0.3303 | 0.3949 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 5.39 | 0.3266 | 0.3915 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 5.30 | 0.3302 | 0.3945 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.29 | 0.3294 | 0.3957 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 5.31 | 0.3292 | 0.3934 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 5.36 | 0.3275 | 0.3916 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 5.29 | 0.3301 | 0.3948 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 5.39 | 0.3263 | 0.3914 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 5.30 | 0.3300 | 0.3944 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.16 | 0.5994 | 0.3928 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 6.18 | 0.5993 | 0.3914 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 6.23 | 0.5983 | 0.3893 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 6.17 | 0.5999 | 0.3926 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 6.26 | 0.5978 | 0.3885 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 6.17 | 0.5998 | 0.3922 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.16 | 0.5993 | 0.3929 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 6.18 | 0.5991 | 0.3915 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 6.23 | 0.5981 | 0.3893 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 6.17 | 0.5997 | 0.3926 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 6.25 | 0.5976 | 0.3885 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 6.17 | 0.5996 | 0.3923 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.08 | 0.3211 | 0.4149 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 5.09 | 0.3209 | 0.4140 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 5.12 | 0.3198 | 0.4125 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 5.08 | 0.3215 | 0.4147 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 5.14 | 0.3193 | 0.4118 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 5.08 | 0.3214 | 0.4144 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.08 | 0.3210 | 0.4150 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 5.09 | 0.3207 | 0.4141 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 5.12 | 0.3196 | 0.4125 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 5.08 | 0.3213 | 0.4148 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 5.14 | 0.3190 | 0.4118 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 5.08 | 0.3212 | 0.4144 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 33.53 | 0.9612 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 33.54 | 0.9616 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 33.54 | 0.9616 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 33.54 | 0.9617 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 33.54 | 0.9616 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 33.54 | 0.9616 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 33.54 | 0.9616 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 33.53 | 0.9612 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 33.54 | 0.9616 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 33.54 | 0.9616 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 33.54 | 0.9617 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 33.54 | 0.9616 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 33.54 | 0.9616 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 33.55 | 0.9618 | 0.0232 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 33.54 | 0.9616 | 0.0233 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 33.48 | 0.9584 | 0.0239 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 33.45 | 0.9582 | 0.0243 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 33.57 | 0.9617 | 0.0226 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 33.53 | 0.9610 | 0.0231 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 33.56 | 0.9617 | 0.0228 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 33.52 | 0.9609 | 0.0234 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 33.56 | 0.9612 | 0.0225 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 33.54 | 0.9606 | 0.0230 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 33.57 | 0.9616 | 0.0229 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 33.53 | 0.9608 | 0.0234 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 33.57 | 0.9616 | 0.0225 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 33.54 | 0.9609 | 0.0230 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 33.49 | 0.9586 | 0.0239 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 33.46 | 0.9583 | 0.0242 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 33.57 | 0.9617 | 0.0226 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 33.53 | 0.9610 | 0.0231 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 33.57 | 0.9618 | 0.0228 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 33.52 | 0.9610 | 0.0233 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 33.57 | 0.9613 | 0.0224 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 33.54 | 0.9607 | 0.0229 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 33.57 | 0.9616 | 0.0229 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 33.53 | 0.9609 | 0.0234 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 33.57 | 0.9616 | 0.0224 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 33.54 | 0.9610 | 0.0229 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 33.50 | 0.9613 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 33.52 | 0.9616 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 33.52 | 0.9616 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 33.51 | 0.9615 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 33.52 | 0.9616 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 33.51 | 0.9615 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 33.53 | 0.9616 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 33.53 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 33.53 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 33.53 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 33.53 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 33.53 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 33.53 | 0.9618 | 0.0233 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 32.20 | 0.9542 | 0.0318 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 32.61 | 0.9581 | 0.0282 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 32.61 | 0.9571 | 0.0287 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 32.46 | 0.9573 | 0.0291 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 32.58 | 0.9559 | 0.0294 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 32.56 | 0.9579 | 0.0283 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 32.21 | 0.9544 | 0.0314 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 32.59 | 0.9582 | 0.0280 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 32.58 | 0.9572 | 0.0285 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 32.44 | 0.9574 | 0.0289 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 32.54 | 0.9561 | 0.0291 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 32.54 | 0.9580 | 0.0281 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 33.52 | 0.9616 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 33.51 | 0.9613 | 0.0239 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 33.49 | 0.9615 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 33.51 | 0.9616 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 33.50 | 0.9613 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 33.52 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 33.52 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 33.52 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 33.52 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 33.50 | 0.9615 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 33.51 | 0.9616 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 33.52 | 0.9616 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 33.52 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 32.32 | 0.9547 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 32.66 | 0.9582 | 0.0281 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 32.67 | 0.9582 | 0.0277 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 32.46 | 0.9574 | 0.0290 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 32.63 | 0.9567 | 0.0285 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 32.57 | 0.9580 | 0.0282 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 32.24 | 0.9547 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 32.64 | 0.9583 | 0.0279 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 32.60 | 0.9579 | 0.0279 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 32.44 | 0.9574 | 0.0289 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 32.63 | 0.9570 | 0.0282 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 32.51 | 0.9576 | 0.0284 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 33.49 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 33.50 | 0.9612 | 0.0242 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 33.49 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 33.51 | 0.9616 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 33.50 | 0.9613 | 0.0240 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 33.50 | 0.9615 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 33.52 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 33.52 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 33.52 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 33.52 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 33.49 | 0.9615 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 33.51 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 33.51 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 33.52 | 0.9616 | 0.0235 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 33.53 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 33.52 | 0.9616 | 0.0234 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 33.54 | 0.9617 | 0.0233 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_tok448_nat_dil_al | 25.00 | 0.8840 | 0.0945 | 1.00 |
| gs_tok448_nat_dil_al+reg | 25.33 | 0.8886 | 0.0941 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 27.51 | 0.9256 | 0.0492 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 28.31 | 0.9393 | 0.0460 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 27.45 | 0.9227 | 0.0504 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 28.19 | 0.9364 | 0.0465 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 27.03 | 0.9193 | 0.0591 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 27.65 | 0.9301 | 0.0583 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 27.41 | 0.9190 | 0.0530 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 28.15 | 0.9329 | 0.0489 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 27.44 | 0.9247 | 0.0519 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 28.16 | 0.9375 | 0.0500 | 1.00 |
| gs_tok448_nat_dil_alv | 24.92 | 0.8850 | 0.0942 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 25.41 | 0.8912 | 0.0938 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 27.47 | 0.9262 | 0.0491 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 28.39 | 0.9408 | 0.0462 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 27.42 | 0.9233 | 0.0502 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 28.44 | 0.9390 | 0.0456 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 26.97 | 0.9204 | 0.0588 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 27.86 | 0.9332 | 0.0571 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 27.39 | 0.9198 | 0.0527 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 28.36 | 0.9350 | 0.0484 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 27.39 | 0.9256 | 0.0517 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 28.38 | 0.9398 | 0.0494 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 19.03 | 0.8433 | 0.1546 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 20.13 | 0.8776 | 0.1118 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 20.21 | 0.8766 | 0.1077 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 19.47 | 0.8667 | 0.1296 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 20.27 | 0.8724 | 0.1091 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 19.71 | 0.8733 | 0.1205 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.99 | 0.8444 | 0.1540 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 20.06 | 0.8777 | 0.1112 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 20.14 | 0.8766 | 0.1072 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 19.42 | 0.8672 | 0.1290 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 20.19 | 0.8725 | 0.1084 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 19.65 | 0.8736 | 0.1199 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.46 | 0.6089 | 0.4184 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.52 | 0.6226 | 0.4037 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 7.63 | 0.6214 | 0.3998 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.48 | 0.6190 | 0.4113 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 7.69 | 0.6194 | 0.3991 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.49 | 0.6216 | 0.4078 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.46 | 0.6083 | 0.4186 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 7.52 | 0.6218 | 0.4036 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 7.63 | 0.6207 | 0.3995 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 7.48 | 0.6182 | 0.4112 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 7.69 | 0.6188 | 0.3987 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 7.49 | 0.6207 | 0.4075 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.84 | 0.3292 | 0.4890 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 5.88 | 0.3373 | 0.4797 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 5.94 | 0.3362 | 0.4772 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 5.85 | 0.3353 | 0.4844 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 5.96 | 0.3346 | 0.4768 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 5.87 | 0.3370 | 0.4820 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.84 | 0.3289 | 0.4891 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 5.88 | 0.3354 | 0.4798 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 5.94 | 0.3344 | 0.4774 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 5.85 | 0.3341 | 0.4844 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 5.96 | 0.3328 | 0.4769 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 5.86 | 0.3354 | 0.4821 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.90 | 0.5792 | 0.4697 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 6.93 | 0.5874 | 0.4617 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 6.98 | 0.5863 | 0.4597 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 6.91 | 0.5848 | 0.4656 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 7.00 | 0.5853 | 0.4589 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 6.92 | 0.5865 | 0.4638 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.89 | 0.5786 | 0.4698 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 6.93 | 0.5862 | 0.4619 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 6.98 | 0.5851 | 0.4598 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 6.91 | 0.5839 | 0.4657 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 7.00 | 0.5841 | 0.4590 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 6.91 | 0.5854 | 0.4639 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.53 | 0.3143 | 0.5126 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 5.55 | 0.3197 | 0.5068 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 5.58 | 0.3187 | 0.5052 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 5.54 | 0.3183 | 0.5095 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 5.60 | 0.3177 | 0.5046 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 5.54 | 0.3195 | 0.5080 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.53 | 0.3136 | 0.5128 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 5.55 | 0.3179 | 0.5070 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 5.58 | 0.3169 | 0.5053 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 5.53 | 0.3171 | 0.5096 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 5.59 | 0.3159 | 0.5048 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 5.54 | 0.3179 | 0.5082 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 27.19 | 0.9262 | 0.0567 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 27.03 | 0.9253 | 0.0571 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 28.85 | 0.9393 | 0.0417 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 28.54 | 0.9366 | 0.0434 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 28.82 | 0.9391 | 0.0414 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 28.52 | 0.9365 | 0.0434 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 28.36 | 0.9357 | 0.0467 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 28.15 | 0.9338 | 0.0474 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 28.80 | 0.9387 | 0.0418 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 28.49 | 0.9361 | 0.0439 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 28.68 | 0.9384 | 0.0436 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 28.45 | 0.9358 | 0.0448 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 27.19 | 0.9263 | 0.0564 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 26.86 | 0.9245 | 0.0570 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 28.92 | 0.9398 | 0.0420 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 28.43 | 0.9356 | 0.0435 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 29.01 | 0.9402 | 0.0410 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 28.43 | 0.9355 | 0.0435 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 28.43 | 0.9362 | 0.0462 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 28.03 | 0.9328 | 0.0475 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 28.96 | 0.9396 | 0.0416 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 28.41 | 0.9351 | 0.0439 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 28.78 | 0.9387 | 0.0434 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 28.34 | 0.9348 | 0.0448 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 25.43 | 0.9053 | 0.0755 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 25.19 | 0.9021 | 0.0757 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 27.69 | 0.9374 | 0.0459 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 27.22 | 0.9293 | 0.0482 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 27.66 | 0.9362 | 0.0458 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 27.20 | 0.9282 | 0.0486 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 27.10 | 0.9306 | 0.0546 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 26.74 | 0.9243 | 0.0552 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 27.65 | 0.9348 | 0.0466 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 27.18 | 0.9267 | 0.0496 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 27.50 | 0.9357 | 0.0492 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 27.10 | 0.9283 | 0.0505 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 25.47 | 0.9066 | 0.0755 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 25.06 | 0.9019 | 0.0756 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 27.80 | 0.9386 | 0.0462 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 27.17 | 0.9290 | 0.0480 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 27.88 | 0.9382 | 0.0453 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 27.17 | 0.9279 | 0.0483 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 27.21 | 0.9321 | 0.0541 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 26.67 | 0.9240 | 0.0550 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 27.84 | 0.9365 | 0.0465 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 27.15 | 0.9265 | 0.0492 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 27.64 | 0.9371 | 0.0489 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 27.04 | 0.9280 | 0.0502 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 25.93 | 0.9220 | 0.0591 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 25.86 | 0.9215 | 0.0585 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 27.25 | 0.9357 | 0.0465 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 27.10 | 0.9335 | 0.0469 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 27.23 | 0.9352 | 0.0466 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 27.11 | 0.9332 | 0.0471 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 26.89 | 0.9323 | 0.0505 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 26.78 | 0.9308 | 0.0505 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 27.22 | 0.9346 | 0.0470 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 27.09 | 0.9326 | 0.0476 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 27.14 | 0.9350 | 0.0480 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 27.02 | 0.9328 | 0.0482 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 25.94 | 0.9222 | 0.0590 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 25.74 | 0.9208 | 0.0585 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 27.31 | 0.9363 | 0.0465 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 27.06 | 0.9328 | 0.0465 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 27.36 | 0.9363 | 0.0463 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 27.07 | 0.9326 | 0.0467 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 26.93 | 0.9329 | 0.0504 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 26.71 | 0.9301 | 0.0503 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 27.33 | 0.9356 | 0.0468 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 27.06 | 0.9320 | 0.0471 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 27.20 | 0.9354 | 0.0479 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 26.97 | 0.9321 | 0.0478 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 26.51 | 0.9230 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 27.88 | 0.9349 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 27.85 | 0.9350 | 0.0443 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 27.27 | 0.9307 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 27.79 | 0.9344 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 27.59 | 0.9332 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.57 | 0.9260 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.41 | 0.9325 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.46 | 0.9332 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.99 | 0.9301 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 27.55 | 0.9330 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.22 | 0.9315 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 25.22 | 0.9240 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 25.68 | 0.9285 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 25.60 | 0.9285 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 25.50 | 0.9270 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 25.56 | 0.9283 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 25.63 | 0.9280 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 25.35 | 0.9243 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 25.81 | 0.9286 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 25.74 | 0.9287 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 25.64 | 0.9273 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 25.71 | 0.9287 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 25.77 | 0.9282 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 25.16 | 0.9242 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.56 | 0.9280 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 25.51 | 0.9280 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.41 | 0.9269 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 25.48 | 0.9279 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 25.53 | 0.9277 | 0.0482 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 26.15 | 0.9205 | 0.0581 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 27.44 | 0.9331 | 0.0467 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 27.40 | 0.9331 | 0.0460 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 26.87 | 0.9292 | 0.0530 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 27.34 | 0.9324 | 0.0463 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 27.18 | 0.9317 | 0.0498 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 26.16 | 0.9236 | 0.0533 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 26.98 | 0.9310 | 0.0469 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 27.03 | 0.9314 | 0.0464 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 26.58 | 0.9285 | 0.0509 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 27.12 | 0.9312 | 0.0465 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 26.81 | 0.9301 | 0.0489 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 24.94 | 0.9227 | 0.0534 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 25.39 | 0.9276 | 0.0486 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 25.31 | 0.9275 | 0.0486 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 25.22 | 0.9262 | 0.0512 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 25.27 | 0.9272 | 0.0489 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 25.35 | 0.9273 | 0.0497 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 25.09 | 0.9231 | 0.0522 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 25.56 | 0.9279 | 0.0482 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 25.49 | 0.9279 | 0.0483 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 25.39 | 0.9267 | 0.0499 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 25.46 | 0.9277 | 0.0485 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 25.52 | 0.9276 | 0.0489 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 24.91 | 0.9233 | 0.0523 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.32 | 0.9274 | 0.0485 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 25.26 | 0.9272 | 0.0487 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.17 | 0.9264 | 0.0499 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 25.23 | 0.9271 | 0.0490 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 25.28 | 0.9272 | 0.0491 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 25.45 | 0.8997 | 0.0767 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 27.04 | 0.9235 | 0.0538 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 27.00 | 0.9227 | 0.0524 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 26.38 | 0.9163 | 0.0657 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 26.92 | 0.9206 | 0.0533 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 26.75 | 0.9208 | 0.0598 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.33 | 0.8995 | 0.0766 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 27.00 | 0.9232 | 0.0533 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 26.96 | 0.9224 | 0.0519 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 26.31 | 0.9161 | 0.0651 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 26.89 | 0.9204 | 0.0528 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 26.70 | 0.9205 | 0.0592 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.37 | 0.9233 | 0.0536 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.29 | 0.9314 | 0.0465 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 27.33 | 0.9317 | 0.0460 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.85 | 0.9288 | 0.0508 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 27.41 | 0.9310 | 0.0465 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.10 | 0.9304 | 0.0487 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.29 | 0.9228 | 0.0537 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 27.24 | 0.9307 | 0.0463 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 27.30 | 0.9310 | 0.0456 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 26.79 | 0.9281 | 0.0508 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 27.38 | 0.9305 | 0.0461 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 27.05 | 0.9296 | 0.0484 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.12 | 0.9226 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 25.62 | 0.9279 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 25.55 | 0.9278 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 25.43 | 0.9264 | 0.0507 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 25.50 | 0.9274 | 0.0484 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 25.58 | 0.9275 | 0.0492 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 25.05 | 0.9220 | 0.0532 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 25.53 | 0.9265 | 0.0481 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 25.45 | 0.9263 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 25.35 | 0.9253 | 0.0508 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 25.41 | 0.9259 | 0.0484 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 25.49 | 0.9262 | 0.0492 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.27 | 0.9234 | 0.0519 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 25.78 | 0.9283 | 0.0477 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 25.72 | 0.9282 | 0.0477 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 25.60 | 0.9271 | 0.0493 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 25.68 | 0.9280 | 0.0479 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 25.75 | 0.9280 | 0.0483 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.21 | 0.9229 | 0.0521 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 25.70 | 0.9272 | 0.0477 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 25.63 | 0.9271 | 0.0477 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 25.53 | 0.9262 | 0.0495 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 25.60 | 0.9270 | 0.0479 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 25.67 | 0.9270 | 0.0484 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.10 | 0.9235 | 0.0517 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.55 | 0.9278 | 0.0478 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 25.49 | 0.9276 | 0.0480 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.39 | 0.9268 | 0.0493 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 25.45 | 0.9274 | 0.0483 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 25.51 | 0.9276 | 0.0484 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 25.03 | 0.9229 | 0.0519 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 25.46 | 0.9264 | 0.0479 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 25.40 | 0.9261 | 0.0481 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 25.31 | 0.9257 | 0.0494 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 25.37 | 0.9260 | 0.0483 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 25.43 | 0.9263 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.54 | 0.9001 | 0.0764 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 27.09 | 0.9239 | 0.0537 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 27.04 | 0.9237 | 0.0520 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 26.32 | 0.9160 | 0.0655 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 27.00 | 0.9223 | 0.0525 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 26.76 | 0.9210 | 0.0597 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.34 | 0.8984 | 0.0774 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 27.09 | 0.9238 | 0.0532 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 27.02 | 0.9233 | 0.0518 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 26.27 | 0.9156 | 0.0653 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 27.06 | 0.9229 | 0.0517 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 26.54 | 0.9180 | 0.0601 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.23 | 0.9221 | 0.0542 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 27.34 | 0.9321 | 0.0459 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 27.36 | 0.9323 | 0.0456 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 26.87 | 0.9290 | 0.0504 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 27.23 | 0.9290 | 0.0472 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 | 0.9308 | 0.0483 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.10 | 0.9208 | 0.0546 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 27.29 | 0.9310 | 0.0460 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 27.35 | 0.9313 | 0.0455 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 26.73 | 0.9275 | 0.0508 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 27.40 | 0.9305 | 0.0460 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 27.13 | 0.9308 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.12 | 0.9226 | 0.0531 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 25.62 | 0.9279 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 25.55 | 0.9278 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 25.43 | 0.9264 | 0.0507 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 25.50 | 0.9274 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 25.58 | 0.9275 | 0.0492 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 24.89 | 0.9206 | 0.0537 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 25.53 | 0.9265 | 0.0481 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 25.45 | 0.9263 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 25.25 | 0.9245 | 0.0510 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 25.41 | 0.9259 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 25.53 | 0.9272 | 0.0493 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.27 | 0.9232 | 0.0519 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 25.75 | 0.9277 | 0.0478 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 25.71 | 0.9281 | 0.0477 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 25.58 | 0.9268 | 0.0495 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 25.64 | 0.9274 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 25.72 | 0.9277 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.16 | 0.9222 | 0.0525 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 25.67 | 0.9267 | 0.0478 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 25.25 | 0.9230 | 0.0489 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 25.51 | 0.9259 | 0.0496 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 25.59 | 0.9266 | 0.0479 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 25.65 | 0.9267 | 0.0485 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.10 | 0.9235 | 0.0517 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.55 | 0.9278 | 0.0478 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 25.49 | 0.9276 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.39 | 0.9268 | 0.0493 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 25.45 | 0.9274 | 0.0483 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 25.51 | 0.9276 | 0.0484 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 24.99 | 0.9224 | 0.0522 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 25.46 | 0.9264 | 0.0479 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 25.02 | 0.9221 | 0.0493 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 25.31 | 0.9257 | 0.0494 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 25.37 | 0.9260 | 0.0483 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 25.43 | 0.9263 | 0.0484 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_tok448_nat_dil_al_tto100`，aligned_int → `gs_tok448_nat_dil_al`，aligned_vggt → `gs_tok448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=3.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 15.31 / 0.0249 | 30.29 / 0.0331 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |
| flow_s0.5_pose | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 | 27.45 / 0.0415 |
| gs_tok448_nat_dil_al_tto100 | 22.93 / 0.0611 | 19.30 / 0.0203 | 28.36 / 0.0511 | 26.73 / 0.0573 |
| gs_tok448_nat_dil_al_tto100+reg | 24.90 / 0.0474 | 22.65 / 0.0116 | 30.55 / 0.0365 | 29.40 / 0.0434 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 23.42 / 0.0579 | 19.30 / 0.0203 | 31.44 / 0.0308 | 29.19 / 0.0398 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 23.89 / 0.0456 | 20.43 / 0.0144 | 31.46 / 0.0305 | 29.35 / 0.0375 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 25.06 / 0.0480 | 22.65 / 0.0116 | 31.48 / 0.0303 | 30.11 / 0.0358 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 24.40 / 0.0444 | 21.27 / 0.0127 | 31.46 / 0.0305 | 29.59 / 0.0366 |
| gs_tok448_nat_dil_al | 18.34 / 0.1390 | 16.22 / 0.0337 | 27.21 / 0.0717 | 24.77 / 0.0876 |
| gs_tok448_nat_dil_al+reg | 18.83 / 0.1324 | 17.78 / 0.0281 | 28.34 / 0.0633 | 26.08 / 0.0821 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.81 / 0.1173 | 16.22 / 0.0337 | 31.44 / 0.0310 | 27.56 / 0.0478 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 20.51 / 0.0913 | 17.83 / 0.0227 | 31.45 / 0.0305 | 27.73 / 0.0433 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 20.41 / 0.1140 | 17.78 / 0.0281 | 31.46 / 0.0305 | 28.29 / 0.0456 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 20.72 / 0.0895 | 18.53 / 0.0222 | 31.45 / 0.0305 | 28.00 / 0.0428 |
| gs_tok448_nat_dil_alv | 17.69 / 0.1417 | 15.66 / 0.0355 | 27.15 / 0.0720 | 24.54 / 0.0881 |
| gs_tok448_nat_dil_alv+reg | 18.68 / 0.1335 | 17.64 / 0.0285 | 28.30 / 0.0647 | 26.06 / 0.0848 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 19.13 / 0.1200 | 15.66 / 0.0355 | 31.43 / 0.0310 | 27.16 / 0.0487 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 19.96 / 0.0979 | 17.36 / 0.0236 | 31.46 / 0.0305 | 27.43 / 0.0438 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 20.18 / 0.1138 | 17.64 / 0.0285 | 31.46 / 0.0305 | 28.21 / 0.0461 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 20.55 / 0.0916 | 18.45 / 0.0219 | 31.46 / 0.0305 | 27.98 / 0.0429 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_tok448_nat_dil_al | 18.34 | 0.6761 | 0.1390 | 1.00 |
| gs_tok448_nat_dil_al+reg | 18.83 | 0.7093 | 0.1324 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 22.93 | 0.8163 | 0.0611 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 24.90 | 0.8891 | 0.0474 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 22.78 | 0.8094 | 0.0627 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 24.98 | 0.8851 | 0.0463 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 21.14 | 0.7778 | 0.0901 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 22.18 | 0.8300 | 0.0811 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 22.53 | 0.8028 | 0.0654 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 24.71 | 0.8784 | 0.0493 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 22.32 | 0.8055 | 0.0733 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 23.82 | 0.8694 | 0.0615 | 1.00 |
| gs_tok448_nat_dil_alv | 17.69 | 0.6589 | 0.1417 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 18.68 | 0.7120 | 0.1335 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 21.16 | 0.7878 | 0.0644 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 24.88 | 0.8902 | 0.0488 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 21.23 | 0.7835 | 0.0644 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 24.73 | 0.8828 | 0.0472 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 19.86 | 0.7533 | 0.0932 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 22.04 | 0.8333 | 0.0812 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 21.12 | 0.7778 | 0.0669 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 23.57 | 0.8607 | 0.0524 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 20.73 | 0.7792 | 0.0755 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 23.76 | 0.8720 | 0.0620 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.84 | 0.6543 | 0.1666 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 22.24 | 0.8052 | 0.0701 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 22.46 | 0.8050 | 0.0658 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 19.71 | 0.7458 | 0.1240 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 22.28 | 0.7987 | 0.0674 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 20.88 | 0.7777 | 0.1023 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.24 | 0.6371 | 0.1696 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 20.83 | 0.7767 | 0.0745 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 21.04 | 0.7781 | 0.0686 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 18.83 | 0.7229 | 0.1272 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 20.97 | 0.7726 | 0.0702 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 19.78 | 0.7525 | 0.1062 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.70 | 0.5846 | 0.2725 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 17.26 | 0.7029 | 0.2050 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 17.51 | 0.7063 | 0.1998 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 15.75 | 0.6585 | 0.2420 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 17.49 | 0.7013 | 0.1989 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 16.47 | 0.6826 | 0.2242 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 14.12 | 0.5635 | 0.2768 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 16.13 | 0.6670 | 0.2108 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 16.59 | 0.6730 | 0.2053 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 14.96 | 0.6298 | 0.2459 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 16.67 | 0.6690 | 0.2050 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 15.50 | 0.6507 | 0.2293 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 11.52 | 0.3632 | 0.3977 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 13.70 | 0.4358 | 0.3569 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 13.76 | 0.4347 | 0.3550 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 12.41 | 0.4064 | 0.3816 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 13.71 | 0.4311 | 0.3555 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 13.05 | 0.4232 | 0.3712 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 10.97 | 0.3468 | 0.4012 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 12.64 | 0.4097 | 0.3621 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 12.91 | 0.4130 | 0.3587 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 11.65 | 0.3853 | 0.3849 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 12.96 | 0.4110 | 0.3590 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 12.12 | 0.3995 | 0.3755 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 13.14 | 0.4850 | 0.3287 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 14.85 | 0.5832 | 0.2794 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 14.92 | 0.5841 | 0.2747 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 13.87 | 0.5462 | 0.3068 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 14.94 | 0.5810 | 0.2741 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 14.30 | 0.5680 | 0.2941 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 12.66 | 0.4635 | 0.3350 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 14.08 | 0.5443 | 0.2867 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 14.36 | 0.5491 | 0.2802 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 13.21 | 0.5153 | 0.3125 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 14.45 | 0.5470 | 0.2799 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 13.56 | 0.5331 | 0.3008 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 7.37 | 0.1809 | 0.5318 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 8.12 | 0.2101 | 0.5173 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 8.06 | 0.2063 | 0.5179 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 7.81 | 0.2016 | 0.5273 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 8.05 | 0.2039 | 0.5189 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 8.01 | 0.2072 | 0.5233 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 7.11 | 0.1714 | 0.5329 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 7.72 | 0.1961 | 0.5191 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 7.74 | 0.1940 | 0.5193 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 7.41 | 0.1873 | 0.5284 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 7.76 | 0.1924 | 0.5202 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 7.59 | 0.1937 | 0.5247 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 20.41 | 0.7604 | 0.1140 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 19.81 | 0.7414 | 0.1173 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 25.06 | 0.8880 | 0.0480 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 23.42 | 0.8468 | 0.0579 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 25.10 | 0.8883 | 0.0442 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 23.29 | 0.8455 | 0.0563 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 22.98 | 0.8412 | 0.0745 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 22.06 | 0.8146 | 0.0813 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 24.90 | 0.8848 | 0.0452 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 23.11 | 0.8424 | 0.0576 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 24.28 | 0.8716 | 0.0601 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 23.01 | 0.8365 | 0.0684 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 20.18 | 0.7566 | 0.1138 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 19.13 | 0.7219 | 0.1200 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 25.02 | 0.8869 | 0.0482 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 21.94 | 0.8192 | 0.0629 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 24.93 | 0.8857 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 21.99 | 0.8193 | 0.0605 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 22.86 | 0.8404 | 0.0746 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 20.91 | 0.7892 | 0.0841 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 24.06 | 0.8736 | 0.0498 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 21.92 | 0.8169 | 0.0618 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 24.23 | 0.8711 | 0.0595 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 21.65 | 0.8101 | 0.0713 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 19.19 | 0.7288 | 0.1227 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 18.77 | 0.7057 | 0.1298 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 24.89 | 0.8901 | 0.0455 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 23.32 | 0.8408 | 0.0576 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 25.03 | 0.8887 | 0.0443 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 23.19 | 0.8359 | 0.0585 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 22.40 | 0.8374 | 0.0748 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 21.54 | 0.8033 | 0.0841 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 24.80 | 0.8833 | 0.0468 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 22.95 | 0.8306 | 0.0609 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 23.90 | 0.8719 | 0.0580 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 22.71 | 0.8294 | 0.0688 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 19.04 | 0.7304 | 0.1225 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 18.12 | 0.6863 | 0.1324 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 24.65 | 0.8874 | 0.0471 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 21.53 | 0.8058 | 0.0613 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 24.65 | 0.8836 | 0.0455 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 21.61 | 0.8030 | 0.0611 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 22.20 | 0.8375 | 0.0743 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 20.24 | 0.7737 | 0.0865 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 23.63 | 0.8649 | 0.0502 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 21.52 | 0.7988 | 0.0633 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 23.71 | 0.8711 | 0.0587 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 21.09 | 0.7971 | 0.0715 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 20.72 | 0.7766 | 0.0895 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 20.51 | 0.7694 | 0.0913 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 24.40 | 0.8785 | 0.0444 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 23.89 | 0.8677 | 0.0456 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 24.64 | 0.8781 | 0.0435 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 23.91 | 0.8645 | 0.0459 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 22.76 | 0.8470 | 0.0625 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 22.54 | 0.8415 | 0.0629 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 24.51 | 0.8748 | 0.0443 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 23.76 | 0.8608 | 0.0472 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 23.65 | 0.8670 | 0.0533 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 23.35 | 0.8588 | 0.0538 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 20.55 | 0.7765 | 0.0916 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 19.96 | 0.7526 | 0.0979 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 23.97 | 0.8711 | 0.0463 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 22.40 | 0.8316 | 0.0531 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 24.05 | 0.8689 | 0.0460 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 22.51 | 0.8291 | 0.0534 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 22.54 | 0.8443 | 0.0631 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 21.45 | 0.8114 | 0.0688 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 23.50 | 0.8589 | 0.0485 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 22.46 | 0.8254 | 0.0545 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 23.37 | 0.8623 | 0.0541 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 22.00 | 0.8254 | 0.0606 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 18.96 | 0.7298 | 0.1234 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 22.83 | 0.8432 | 0.0598 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 23.13 | 0.8454 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 21.03 | 0.8037 | 0.0923 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 22.97 | 0.8412 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 22.08 | 0.8277 | 0.0790 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.59 | 0.7680 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.62 | 0.8370 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 22.90 | 0.8448 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.83 | 0.8099 | 0.0727 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 22.96 | 0.8449 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.29 | 0.8249 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 20.80 | 0.7699 | 0.0771 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 22.43 | 0.8175 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.63 | 0.8202 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 21.77 | 0.7983 | 0.0693 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.68 | 0.8203 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 22.14 | 0.8086 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 20.74 | 0.7696 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 22.27 | 0.8233 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 22.39 | 0.8283 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 21.59 | 0.7997 | 0.0700 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 22.44 | 0.8283 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 21.99 | 0.8126 | 0.0640 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 21.11 | 0.7755 | 0.0659 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 21.83 | 0.8020 | 0.0563 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 21.91 | 0.8038 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.55 | 0.7913 | 0.0623 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 21.96 | 0.8039 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 21.71 | 0.7970 | 0.0601 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 19.97 | 0.7486 | 0.0884 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 21.97 | 0.8148 | 0.0597 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 22.16 | 0.8177 | 0.0544 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 20.94 | 0.7884 | 0.0810 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 22.14 | 0.8158 | 0.0539 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 21.46 | 0.8022 | 0.0747 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 20.22 | 0.7533 | 0.0840 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 22.09 | 0.8112 | 0.0600 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 22.21 | 0.8144 | 0.0530 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 21.40 | 0.7901 | 0.0764 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 22.21 | 0.8135 | 0.0525 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 21.76 | 0.8013 | 0.0702 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 20.44 | 0.7574 | 0.0813 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 22.02 | 0.8036 | 0.0591 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.11 | 0.8044 | 0.0561 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 21.41 | 0.7864 | 0.0724 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.10 | 0.8031 | 0.0560 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 21.71 | 0.7952 | 0.0680 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 20.52 | 0.7596 | 0.0736 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 21.85 | 0.8039 | 0.0583 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 21.95 | 0.8075 | 0.0526 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 21.28 | 0.7861 | 0.0705 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 22.00 | 0.8077 | 0.0517 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 21.61 | 0.7957 | 0.0652 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 21.01 | 0.7717 | 0.0655 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 21.53 | 0.7913 | 0.0580 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 21.58 | 0.7920 | 0.0560 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.36 | 0.7846 | 0.0621 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 21.62 | 0.7923 | 0.0557 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 21.46 | 0.7881 | 0.0609 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 18.20 | 0.6795 | 0.1537 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 22.44 | 0.8181 | 0.0676 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 22.67 | 0.8159 | 0.0629 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 20.49 | 0.7738 | 0.1085 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 22.48 | 0.8091 | 0.0649 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 21.62 | 0.8022 | 0.0903 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.61 | 0.6599 | 0.1569 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 20.98 | 0.7851 | 0.0722 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 21.21 | 0.7851 | 0.0664 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 19.54 | 0.7458 | 0.1113 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 21.14 | 0.7793 | 0.0687 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 20.42 | 0.7723 | 0.0942 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.19 | 0.7533 | 0.0910 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.56 | 0.8335 | 0.0587 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 22.79 | 0.8391 | 0.0515 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.67 | 0.8045 | 0.0794 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 22.82 | 0.8373 | 0.0520 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.17 | 0.8210 | 0.0708 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 19.84 | 0.7416 | 0.0936 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 21.84 | 0.8077 | 0.0631 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 22.11 | 0.8135 | 0.0558 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 21.10 | 0.7849 | 0.0820 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 22.19 | 0.8123 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 21.52 | 0.7988 | 0.0742 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 20.45 | 0.7567 | 0.0855 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 22.39 | 0.8144 | 0.0579 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.54 | 0.8150 | 0.0552 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 21.64 | 0.7936 | 0.0746 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.55 | 0.8131 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 22.04 | 0.8052 | 0.0680 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 20.13 | 0.7481 | 0.0870 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 21.74 | 0.7966 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 21.96 | 0.7998 | 0.0583 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 21.11 | 0.7793 | 0.0761 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 22.03 | 0.7986 | 0.0586 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 21.45 | 0.7897 | 0.0706 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 20.53 | 0.7616 | 0.0781 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 22.21 | 0.8204 | 0.0575 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 22.34 | 0.8244 | 0.0523 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 21.48 | 0.7955 | 0.0729 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 22.38 | 0.8232 | 0.0525 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 21.90 | 0.8098 | 0.0663 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 20.25 | 0.7538 | 0.0816 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 21.80 | 0.8033 | 0.0609 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 22.03 | 0.8089 | 0.0551 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 21.12 | 0.7830 | 0.0766 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 22.13 | 0.8086 | 0.0547 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 21.49 | 0.7950 | 0.0701 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 21.10 | 0.7750 | 0.0662 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 21.83 | 0.8011 | 0.0566 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 21.89 | 0.8008 | 0.0556 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.55 | 0.7914 | 0.0623 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 21.93 | 0.7999 | 0.0562 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 21.71 | 0.7969 | 0.0601 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 20.93 | 0.7693 | 0.0681 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 21.50 | 0.7904 | 0.0594 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 21.63 | 0.7924 | 0.0576 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 21.25 | 0.7818 | 0.0659 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 21.70 | 0.7921 | 0.0578 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 21.38 | 0.7870 | 0.0632 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 18.10 | 0.6853 | 0.1518 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 22.07 | 0.8255 | 0.0632 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 22.33 | 0.8356 | 0.0587 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 20.84 | 0.7958 | 0.1042 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 22.87 | 0.8481 | 0.0576 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 20.73 | 0.7857 | 0.0940 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.94 | 0.6852 | 0.1484 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 22.07 | 0.8307 | 0.0649 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 22.27 | 0.8207 | 0.0625 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 20.95 | 0.8054 | 0.1009 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 21.68 | 0.8036 | 0.0678 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 20.91 | 0.7960 | 0.0917 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 20.07 | 0.7470 | 0.0940 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 22.41 | 0.8212 | 0.0571 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 22.50 | 0.8148 | 0.0542 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 21.40 | 0.7913 | 0.0809 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 22.65 | 0.8246 | 0.0538 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 21.68 | 0.8036 | 0.0714 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 19.90 | 0.7418 | 0.0937 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 21.00 | 0.7773 | 0.0674 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 21.08 | 0.7889 | 0.0666 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 21.22 | 0.7846 | 0.0795 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 21.62 | 0.7954 | 0.0611 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 21.87 | 0.8058 | 0.0706 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 20.37 | 0.7541 | 0.0884 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 22.39 | 0.8144 | 0.0579 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 22.54 | 0.8150 | 0.0552 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 21.53 | 0.7903 | 0.0757 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 22.55 | 0.8131 | 0.0559 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 21.65 | 0.7957 | 0.0694 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 20.15 | 0.7472 | 0.0884 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 21.09 | 0.7809 | 0.0676 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 20.98 | 0.7783 | 0.0688 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 21.33 | 0.7844 | 0.0757 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 21.61 | 0.7922 | 0.0624 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 21.86 | 0.8003 | 0.0684 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 20.26 | 0.7524 | 0.0803 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 21.23 | 0.7748 | 0.0623 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 22.15 | 0.8041 | 0.0553 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 21.42 | 0.7877 | 0.0740 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 22.06 | 0.7986 | 0.0571 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 21.76 | 0.7956 | 0.0664 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 20.21 | 0.7485 | 0.0827 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 21.26 | 0.7783 | 0.0627 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 21.96 | 0.7991 | 0.0568 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 20.51 | 0.7634 | 0.0814 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 22.05 | 0.7983 | 0.0575 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 20.38 | 0.7574 | 0.0770 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 21.10 | 0.7750 | 0.0662 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 21.18 | 0.7780 | 0.0602 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 21.89 | 0.8008 | 0.0556 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 21.55 | 0.7914 | 0.0623 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 21.80 | 0.7966 | 0.0573 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 21.71 | 0.7969 | 0.0601 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 20.93 | 0.7693 | 0.0681 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 21.17 | 0.7798 | 0.0607 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 21.63 | 0.7924 | 0.0576 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 21.35 | 0.7852 | 0.0647 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 21.70 | 0.7921 | 0.0578 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 21.34 | 0.7850 | 0.0626 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.18 | 0.7600 | 0.0171 | 1.00 |
| flow_s0.5_pose | 17.06 | 0.6711 | 0.0195 | 1.00 |
| flow_s0.5_uniform | 15.30 | 0.5755 | 0.0247 | 1.00 |
| flow_s1.0_oracle | 19.73 | 0.7659 | 0.0154 | 1.00 |
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| flow_s1.0_uniform | 15.31 | 0.5619 | 0.0249 | 1.00 |
| gs_tok448_nat_dil_al | 16.22 | 0.6220 | 0.0337 | 1.00 |
| gs_tok448_nat_dil_al+reg | 17.78 | 0.6877 | 0.0281 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 19.30 | 0.7556 | 0.0203 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 22.65 | 0.8671 | 0.0116 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 19.30 | 0.7522 | 0.0208 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 22.50 | 0.8612 | 0.0122 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 18.49 | 0.7259 | 0.0227 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 20.76 | 0.8109 | 0.0158 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 19.20 | 0.7481 | 0.0212 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 22.23 | 0.8538 | 0.0130 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 19.05 | 0.7480 | 0.0210 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 22.14 | 0.8506 | 0.0124 | 1.00 |
| gs_tok448_nat_dil_alv | 15.66 | 0.5951 | 0.0355 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 17.64 | 0.6845 | 0.0285 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 18.25 | 0.7237 | 0.0223 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 22.72 | 0.8715 | 0.0120 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 18.33 | 0.7242 | 0.0225 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 22.55 | 0.8666 | 0.0125 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 17.61 | 0.6954 | 0.0246 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 20.99 | 0.8216 | 0.0148 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 18.31 | 0.7219 | 0.0229 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 21.54 | 0.8433 | 0.0141 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 18.08 | 0.7163 | 0.0228 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 22.23 | 0.8566 | 0.0125 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 15.64 | 0.5998 | 0.0402 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 17.87 | 0.7352 | 0.0272 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 17.75 | 0.7358 | 0.0272 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 17.18 | 0.6904 | 0.0311 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 17.71 | 0.7327 | 0.0272 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 17.65 | 0.7159 | 0.0290 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 15.19 | 0.5721 | 0.0419 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 17.31 | 0.7018 | 0.0290 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 17.27 | 0.7060 | 0.0288 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 16.66 | 0.6604 | 0.0329 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 17.28 | 0.7054 | 0.0287 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 17.09 | 0.6843 | 0.0306 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.38 | 0.3971 | 0.0958 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 11.11 | 0.5140 | 0.0863 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 11.22 | 0.5202 | 0.0851 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 10.82 | 0.4703 | 0.0898 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 11.22 | 0.5169 | 0.0850 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.97 | 0.4932 | 0.0882 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 10.19 | 0.3725 | 0.0969 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 10.94 | 0.4829 | 0.0878 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 11.08 | 0.4928 | 0.0863 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 10.65 | 0.4431 | 0.0912 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 11.11 | 0.4914 | 0.0861 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 10.79 | 0.4640 | 0.0895 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 8.05 | 0.2623 | 0.1302 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 8.63 | 0.3495 | 0.1227 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 8.64 | 0.3512 | 0.1224 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 8.44 | 0.3186 | 0.1251 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 8.64 | 0.3493 | 0.1223 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 8.56 | 0.3366 | 0.1239 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 7.88 | 0.2420 | 0.1312 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 8.48 | 0.3261 | 0.1240 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 8.52 | 0.3320 | 0.1236 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 8.28 | 0.2979 | 0.1264 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 8.53 | 0.3324 | 0.1234 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 8.40 | 0.3147 | 0.1251 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 9.05 | 0.3206 | 0.1180 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 9.57 | 0.4246 | 0.1108 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 9.60 | 0.4274 | 0.1102 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 9.38 | 0.3886 | 0.1136 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 9.61 | 0.4257 | 0.1099 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 9.48 | 0.4095 | 0.1122 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 8.92 | 0.2972 | 0.1189 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 9.45 | 0.3926 | 0.1121 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 9.51 | 0.4005 | 0.1113 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 9.25 | 0.3605 | 0.1147 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 9.54 | 0.4016 | 0.1109 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 9.35 | 0.3788 | 0.1133 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.40 | 0.1214 | 0.1548 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 5.54 | 0.1534 | 0.1521 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 5.54 | 0.1526 | 0.1521 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 5.50 | 0.1455 | 0.1530 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 5.55 | 0.1522 | 0.1518 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 5.52 | 0.1505 | 0.1526 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.35 | 0.1131 | 0.1550 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 5.50 | 0.1440 | 0.1526 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 5.51 | 0.1448 | 0.1525 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 5.44 | 0.1348 | 0.1535 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 5.53 | 0.1451 | 0.1522 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 5.47 | 0.1411 | 0.1531 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 17.78 | 0.6853 | 0.0281 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 16.22 | 0.6169 | 0.0337 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 22.65 | 0.8625 | 0.0116 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 19.30 | 0.7548 | 0.0203 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 22.50 | 0.8574 | 0.0122 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 19.30 | 0.7523 | 0.0208 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 20.76 | 0.8048 | 0.0158 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 18.49 | 0.7224 | 0.0227 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 22.23 | 0.8504 | 0.0130 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 19.20 | 0.7481 | 0.0212 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 22.14 | 0.8455 | 0.0124 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 19.05 | 0.7459 | 0.0210 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 17.64 | 0.6814 | 0.0285 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 15.66 | 0.5892 | 0.0355 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 22.72 | 0.8675 | 0.0120 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 18.25 | 0.7228 | 0.0223 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 22.55 | 0.8634 | 0.0125 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 18.33 | 0.7239 | 0.0225 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 20.99 | 0.8162 | 0.0148 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 17.61 | 0.6915 | 0.0246 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 21.54 | 0.8405 | 0.0141 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 18.31 | 0.7216 | 0.0229 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 22.23 | 0.8522 | 0.0125 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 18.08 | 0.7141 | 0.0228 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 17.95 | 0.6961 | 0.0272 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 16.75 | 0.6500 | 0.0303 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 22.43 | 0.8609 | 0.0117 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 19.95 | 0.7793 | 0.0175 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 22.36 | 0.8588 | 0.0119 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 19.94 | 0.7769 | 0.0176 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 20.73 | 0.8095 | 0.0162 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 19.07 | 0.7491 | 0.0203 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 22.15 | 0.8532 | 0.0123 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 19.83 | 0.7732 | 0.0179 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 21.94 | 0.8448 | 0.0130 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 19.69 | 0.7709 | 0.0185 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 17.86 | 0.6950 | 0.0273 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 16.20 | 0.6255 | 0.0314 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 22.43 | 0.8631 | 0.0124 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 18.91 | 0.7488 | 0.0189 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 22.40 | 0.8617 | 0.0123 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 18.98 | 0.7495 | 0.0189 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 20.89 | 0.8177 | 0.0154 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 18.21 | 0.7205 | 0.0217 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 21.53 | 0.8414 | 0.0133 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 18.95 | 0.7475 | 0.0193 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 21.98 | 0.8490 | 0.0133 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 18.72 | 0.7411 | 0.0198 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 18.53 | 0.7182 | 0.0222 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 17.83 | 0.6939 | 0.0227 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 21.27 | 0.8266 | 0.0127 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 20.43 | 0.7974 | 0.0144 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 21.28 | 0.8261 | 0.0126 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 20.44 | 0.7960 | 0.0144 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 20.29 | 0.7923 | 0.0155 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 19.67 | 0.7702 | 0.0165 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 21.20 | 0.8231 | 0.0127 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 20.36 | 0.7931 | 0.0145 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 20.94 | 0.8152 | 0.0136 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 20.19 | 0.7887 | 0.0151 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 18.45 | 0.7173 | 0.0219 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 17.36 | 0.6739 | 0.0236 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 21.31 | 0.8262 | 0.0129 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 19.56 | 0.7683 | 0.0157 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 21.34 | 0.8262 | 0.0128 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 19.60 | 0.7688 | 0.0157 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 20.46 | 0.7990 | 0.0147 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 18.96 | 0.7439 | 0.0177 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 20.74 | 0.8112 | 0.0135 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 19.58 | 0.7665 | 0.0158 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 21.05 | 0.8177 | 0.0135 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 19.38 | 0.7606 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 16.63 | 0.6417 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 19.42 | 0.7650 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 19.57 | 0.7672 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 18.51 | 0.7317 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 19.50 | 0.7632 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 19.06 | 0.7525 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 17.89 | 0.6951 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.95 | 0.7845 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 20.15 | 0.7923 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.27 | 0.7562 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 20.14 | 0.7914 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.68 | 0.7720 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 17.94 | 0.6925 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 19.70 | 0.7663 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 19.83 | 0.7701 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 19.10 | 0.7432 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 19.84 | 0.7698 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 19.46 | 0.7558 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 17.92 | 0.6925 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 19.59 | 0.7666 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 19.67 | 0.7715 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 18.99 | 0.7401 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 19.68 | 0.7709 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 19.36 | 0.7551 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 18.16 | 0.6989 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.75 | 0.7297 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.78 | 0.7317 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 18.59 | 0.7204 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.81 | 0.7318 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.70 | 0.7256 | 0.0158 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 17.66 | 0.6761 | 0.0219 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 19.40 | 0.7577 | 0.0155 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 19.52 | 0.7594 | 0.0152 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 18.76 | 0.7305 | 0.0176 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 19.50 | 0.7580 | 0.0152 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 19.13 | 0.7454 | 0.0166 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 17.80 | 0.6874 | 0.0203 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 19.61 | 0.7641 | 0.0141 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 19.71 | 0.7670 | 0.0137 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 19.01 | 0.7407 | 0.0158 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 19.69 | 0.7659 | 0.0137 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 19.35 | 0.7531 | 0.0149 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 17.87 | 0.6866 | 0.0199 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 19.49 | 0.7550 | 0.0141 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 19.54 | 0.7564 | 0.0138 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 18.94 | 0.7343 | 0.0156 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 19.51 | 0.7553 | 0.0138 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 19.24 | 0.7451 | 0.0148 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 17.86 | 0.6878 | 0.0189 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 19.35 | 0.7523 | 0.0143 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 19.40 | 0.7555 | 0.0139 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 18.83 | 0.7311 | 0.0158 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 19.41 | 0.7553 | 0.0139 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 19.14 | 0.7428 | 0.0150 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 18.09 | 0.6948 | 0.0175 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.56 | 0.7200 | 0.0155 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.57 | 0.7210 | 0.0154 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 18.45 | 0.7137 | 0.0160 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.60 | 0.7214 | 0.0154 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.52 | 0.7171 | 0.0158 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 16.61 | 0.6374 | 0.0315 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 19.34 | 0.7619 | 0.0196 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 19.50 | 0.7632 | 0.0193 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 18.49 | 0.7287 | 0.0229 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 19.45 | 0.7597 | 0.0194 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 19.01 | 0.7496 | 0.0213 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 16.09 | 0.6113 | 0.0328 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 18.48 | 0.7309 | 0.0211 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 18.67 | 0.7354 | 0.0206 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 17.80 | 0.6999 | 0.0245 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 18.66 | 0.7339 | 0.0208 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 18.23 | 0.7203 | 0.0226 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 17.90 | 0.6933 | 0.0208 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.97 | 0.7843 | 0.0139 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 20.16 | 0.7920 | 0.0134 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.30 | 0.7557 | 0.0159 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 20.15 | 0.7910 | 0.0134 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.70 | 0.7716 | 0.0149 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 17.52 | 0.6754 | 0.0216 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 19.41 | 0.7597 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 19.59 | 0.7682 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 18.82 | 0.7342 | 0.0170 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 19.64 | 0.7682 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 19.16 | 0.7491 | 0.0158 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 17.95 | 0.6911 | 0.0200 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 19.73 | 0.7665 | 0.0139 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 19.84 | 0.7700 | 0.0136 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 19.14 | 0.7431 | 0.0156 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 19.84 | 0.7696 | 0.0135 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 19.48 | 0.7558 | 0.0147 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 17.61 | 0.6759 | 0.0208 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 19.24 | 0.7477 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 19.35 | 0.7533 | 0.0145 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 18.69 | 0.7256 | 0.0166 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 19.41 | 0.7540 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 18.99 | 0.7384 | 0.0156 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 17.92 | 0.6918 | 0.0190 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 19.60 | 0.7668 | 0.0142 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 19.68 | 0.7718 | 0.0138 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 18.99 | 0.7398 | 0.0158 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 19.69 | 0.7713 | 0.0137 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 19.36 | 0.7551 | 0.0150 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 17.66 | 0.6804 | 0.0195 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 19.25 | 0.7487 | 0.0149 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 19.38 | 0.7560 | 0.0144 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 18.68 | 0.7253 | 0.0165 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 19.45 | 0.7569 | 0.0144 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 19.00 | 0.7390 | 0.0155 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 18.16 | 0.6990 | 0.0175 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.75 | 0.7298 | 0.0154 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.78 | 0.7318 | 0.0153 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 18.59 | 0.7205 | 0.0160 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.81 | 0.7319 | 0.0153 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.70 | 0.7256 | 0.0158 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 18.04 | 0.6932 | 0.0177 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 18.56 | 0.7207 | 0.0158 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 18.64 | 0.7251 | 0.0156 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 18.38 | 0.7119 | 0.0164 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 18.70 | 0.7259 | 0.0156 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 18.48 | 0.7171 | 0.0161 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.26 | 0.6653 | 0.0298 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 20.32 | 0.8052 | 0.0168 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 20.26 | 0.8129 | 0.0166 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 19.77 | 0.7842 | 0.0192 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 20.74 | 0.8241 | 0.0153 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 19.56 | 0.7788 | 0.0191 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.03 | 0.6536 | 0.0299 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 20.32 | 0.8170 | 0.0160 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 19.76 | 0.7878 | 0.0183 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 19.89 | 0.7896 | 0.0186 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 19.47 | 0.7766 | 0.0182 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 19.49 | 0.7811 | 0.0184 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 18.08 | 0.7014 | 0.0203 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 20.01 | 0.7790 | 0.0138 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 19.93 | 0.7753 | 0.0135 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 19.40 | 0.7527 | 0.0159 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 19.79 | 0.7797 | 0.0140 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 19.69 | 0.7657 | 0.0153 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 18.12 | 0.7040 | 0.0198 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 19.19 | 0.7388 | 0.0159 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 19.15 | 0.7466 | 0.0158 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 19.09 | 0.7412 | 0.0165 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 19.60 | 0.7610 | 0.0147 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 19.50 | 0.7603 | 0.0158 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 18.16 | 0.7004 | 0.0195 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 19.73 | 0.7665 | 0.0139 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 19.84 | 0.7700 | 0.0136 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 19.20 | 0.7428 | 0.0155 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 19.84 | 0.7696 | 0.0135 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 19.34 | 0.7505 | 0.0152 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 18.18 | 0.7026 | 0.0190 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 18.99 | 0.7332 | 0.0158 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 18.93 | 0.7333 | 0.0159 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 19.05 | 0.7356 | 0.0161 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 19.47 | 0.7530 | 0.0147 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 19.36 | 0.7511 | 0.0156 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 18.03 | 0.6952 | 0.0185 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 18.88 | 0.7244 | 0.0151 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 19.54 | 0.7594 | 0.0139 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 18.94 | 0.7350 | 0.0159 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 19.44 | 0.7531 | 0.0140 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 19.26 | 0.7463 | 0.0150 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 18.23 | 0.6995 | 0.0179 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 18.76 | 0.7215 | 0.0161 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 19.32 | 0.7499 | 0.0145 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 18.37 | 0.7160 | 0.0169 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 19.37 | 0.7502 | 0.0146 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 18.10 | 0.7062 | 0.0172 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 18.16 | 0.6990 | 0.0175 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 18.26 | 0.7035 | 0.0159 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 18.78 | 0.7318 | 0.0153 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 18.59 | 0.7205 | 0.0160 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 18.71 | 0.7268 | 0.0154 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 18.70 | 0.7256 | 0.0158 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 18.04 | 0.6932 | 0.0177 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 18.27 | 0.7077 | 0.0161 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 18.64 | 0.7251 | 0.0156 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 18.41 | 0.7130 | 0.0165 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 18.70 | 0.7259 | 0.0156 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 18.39 | 0.7117 | 0.0162 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.73 | 0.8826 | 0.0204 | 1.00 |
| flow_s0.5_pose | 22.21 | 0.8504 | 0.0224 | 1.00 |
| flow_s0.5_uniform | 20.55 | 0.8064 | 0.0266 | 1.00 |
| flow_s1.0_oracle | 24.76 | 0.8987 | 0.0188 | 1.00 |
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| flow_s1.0_uniform | 20.86 | 0.8093 | 0.0253 | 1.00 |
| gs_tok448_nat_dil_al | 20.19 | 0.7478 | 0.0462 | 1.00 |
| gs_tok448_nat_dil_al+reg | 21.40 | 0.7891 | 0.0401 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 23.06 | 0.8236 | 0.0287 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 26.36 | 0.9106 | 0.0180 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 23.13 | 0.8141 | 0.0301 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 26.18 | 0.8996 | 0.0195 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 22.48 | 0.8168 | 0.0315 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 24.85 | 0.8868 | 0.0227 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 23.03 | 0.8072 | 0.0313 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 25.88 | 0.8902 | 0.0208 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 22.90 | 0.8253 | 0.0292 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 26.00 | 0.9071 | 0.0192 | 1.00 |
| gs_tok448_nat_dil_alv | 19.85 | 0.7396 | 0.0467 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 21.43 | 0.7928 | 0.0402 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 22.38 | 0.8124 | 0.0296 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 26.19 | 0.9083 | 0.0185 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 22.48 | 0.8044 | 0.0307 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 25.97 | 0.8978 | 0.0198 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 21.88 | 0.8060 | 0.0324 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 24.92 | 0.8896 | 0.0225 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 22.42 | 0.7979 | 0.0319 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 25.34 | 0.8839 | 0.0213 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 22.25 | 0.8140 | 0.0302 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 25.88 | 0.9059 | 0.0196 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.55 | 0.7105 | 0.0646 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 20.44 | 0.7873 | 0.0440 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 21.21 | 0.7873 | 0.0419 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 18.55 | 0.7650 | 0.0528 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 21.21 | 0.7815 | 0.0425 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 19.29 | 0.7777 | 0.0485 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.33 | 0.7026 | 0.0649 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 20.10 | 0.7767 | 0.0447 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 20.88 | 0.7774 | 0.0422 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 18.28 | 0.7549 | 0.0535 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 20.91 | 0.7719 | 0.0428 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 19.00 | 0.7672 | 0.0493 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.04 | 0.4785 | 0.2191 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.30 | 0.5331 | 0.2082 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 8.40 | 0.5365 | 0.2056 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.10 | 0.5136 | 0.2141 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 8.43 | 0.5327 | 0.2055 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.17 | 0.5233 | 0.2117 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.01 | 0.4707 | 0.2195 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 8.27 | 0.5223 | 0.2087 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 8.39 | 0.5266 | 0.2060 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 8.08 | 0.5038 | 0.2145 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 8.41 | 0.5231 | 0.2059 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 8.15 | 0.5130 | 0.2122 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 6.77 | 0.2818 | 0.2460 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 6.94 | 0.3208 | 0.2381 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 6.97 | 0.3210 | 0.2367 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 6.83 | 0.3082 | 0.2423 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 6.97 | 0.3186 | 0.2369 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 6.87 | 0.3153 | 0.2407 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 6.75 | 0.2753 | 0.2464 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 6.92 | 0.3127 | 0.2385 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 6.96 | 0.3140 | 0.2370 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 6.82 | 0.3008 | 0.2427 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 6.96 | 0.3121 | 0.2372 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 6.86 | 0.3075 | 0.2411 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.45 | 0.3842 | 0.2364 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 7.62 | 0.4283 | 0.2286 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 7.67 | 0.4285 | 0.2269 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 7.50 | 0.4140 | 0.2325 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 7.69 | 0.4257 | 0.2267 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 7.54 | 0.4226 | 0.2309 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.42 | 0.3767 | 0.2367 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 7.59 | 0.4164 | 0.2291 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 7.66 | 0.4178 | 0.2274 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 7.47 | 0.4037 | 0.2329 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 7.68 | 0.4155 | 0.2272 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 7.52 | 0.4114 | 0.2314 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 5.44 | 0.1372 | 0.2724 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 5.48 | 0.1524 | 0.2694 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 5.49 | 0.1508 | 0.2691 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 5.46 | 0.1488 | 0.2707 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 5.49 | 0.1495 | 0.2689 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 5.47 | 0.1512 | 0.2701 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 5.43 | 0.1338 | 0.2726 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 5.47 | 0.1482 | 0.2698 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 5.48 | 0.1474 | 0.2693 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 5.45 | 0.1442 | 0.2711 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 5.48 | 0.1463 | 0.2692 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 5.46 | 0.1470 | 0.2705 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 23.56 | 0.8650 | 0.0257 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 22.58 | 0.8503 | 0.0279 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 26.94 | 0.9179 | 0.0165 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 25.15 | 0.8932 | 0.0197 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 26.90 | 0.9171 | 0.0164 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 25.13 | 0.8921 | 0.0196 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 25.79 | 0.9022 | 0.0193 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 24.51 | 0.8842 | 0.0217 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 26.77 | 0.9152 | 0.0167 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 25.05 | 0.8909 | 0.0198 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 26.62 | 0.9136 | 0.0175 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 24.98 | 0.8909 | 0.0206 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 23.48 | 0.8638 | 0.0258 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 22.11 | 0.8420 | 0.0283 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 26.86 | 0.9175 | 0.0170 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 24.39 | 0.8832 | 0.0206 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 26.82 | 0.9170 | 0.0167 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 24.43 | 0.8829 | 0.0204 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 25.86 | 0.9041 | 0.0192 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 23.83 | 0.8745 | 0.0226 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 26.34 | 0.9116 | 0.0172 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 24.40 | 0.8820 | 0.0206 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 26.59 | 0.9137 | 0.0179 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 24.24 | 0.8810 | 0.0215 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 21.40 | 0.7885 | 0.0401 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 20.19 | 0.7480 | 0.0462 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 26.36 | 0.9101 | 0.0180 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 23.06 | 0.8250 | 0.0287 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 26.18 | 0.8998 | 0.0195 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 23.13 | 0.8160 | 0.0301 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 24.85 | 0.8860 | 0.0227 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 22.48 | 0.8176 | 0.0315 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 25.88 | 0.8906 | 0.0208 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 23.03 | 0.8092 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 26.00 | 0.9063 | 0.0192 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 22.90 | 0.8265 | 0.0292 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 21.43 | 0.7923 | 0.0402 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 19.85 | 0.7399 | 0.0467 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 26.19 | 0.9078 | 0.0185 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 22.38 | 0.8139 | 0.0296 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 25.97 | 0.8979 | 0.0198 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 22.48 | 0.8062 | 0.0307 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 24.92 | 0.8888 | 0.0225 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 21.88 | 0.8068 | 0.0324 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 25.34 | 0.8842 | 0.0213 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 22.42 | 0.7999 | 0.0319 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 25.88 | 0.9051 | 0.0196 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 22.25 | 0.8152 | 0.0302 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 23.24 | 0.8592 | 0.0251 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 22.73 | 0.8500 | 0.0255 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 26.05 | 0.9114 | 0.0178 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 25.23 | 0.8952 | 0.0187 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 26.04 | 0.9082 | 0.0178 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 25.21 | 0.8914 | 0.0187 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 25.15 | 0.8994 | 0.0199 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 24.51 | 0.8871 | 0.0206 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 25.92 | 0.9049 | 0.0181 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 25.09 | 0.8880 | 0.0191 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 25.72 | 0.9083 | 0.0188 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 24.98 | 0.8937 | 0.0196 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 23.24 | 0.8609 | 0.0251 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 22.36 | 0.8434 | 0.0259 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 25.94 | 0.9095 | 0.0181 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 24.47 | 0.8842 | 0.0195 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 25.92 | 0.9062 | 0.0181 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 24.50 | 0.8810 | 0.0194 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 25.19 | 0.9007 | 0.0200 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 23.88 | 0.8772 | 0.0212 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 25.51 | 0.8997 | 0.0185 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 24.42 | 0.8778 | 0.0197 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 25.68 | 0.9074 | 0.0190 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 24.25 | 0.8830 | 0.0203 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 21.95 | 0.8388 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 24.57 | 0.8850 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 24.73 | 0.8853 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 23.68 | 0.8740 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 24.68 | 0.8834 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 24.19 | 0.8809 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.22 | 0.8667 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.00 | 0.8967 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 25.15 | 0.8987 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.45 | 0.8877 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 25.15 | 0.8982 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.79 | 0.8928 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 23.31 | 0.8663 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 24.78 | 0.8906 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 24.87 | 0.8912 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 24.31 | 0.8833 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 24.87 | 0.8907 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 24.59 | 0.8874 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 23.32 | 0.8684 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 24.74 | 0.8917 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 24.81 | 0.8930 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 24.25 | 0.8837 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 24.81 | 0.8926 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 24.54 | 0.8881 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 23.62 | 0.8725 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 24.10 | 0.8832 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 24.12 | 0.8835 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.97 | 0.8798 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 24.14 | 0.8833 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 24.05 | 0.8817 | 0.0195 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 22.25 | 0.8354 | 0.0270 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 23.69 | 0.8698 | 0.0217 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 23.81 | 0.8709 | 0.0210 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 23.28 | 0.8618 | 0.0242 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 23.80 | 0.8692 | 0.0210 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 23.59 | 0.8672 | 0.0229 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 22.57 | 0.8498 | 0.0247 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 24.35 | 0.8822 | 0.0197 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 24.50 | 0.8838 | 0.0191 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 23.82 | 0.8741 | 0.0218 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 24.45 | 0.8823 | 0.0192 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 24.12 | 0.8781 | 0.0208 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 22.93 | 0.8564 | 0.0235 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 24.45 | 0.8836 | 0.0192 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 24.48 | 0.8832 | 0.0189 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 23.96 | 0.8771 | 0.0206 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 24.44 | 0.8819 | 0.0190 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 24.24 | 0.8812 | 0.0197 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 23.11 | 0.8624 | 0.0217 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 24.51 | 0.8856 | 0.0184 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 24.58 | 0.8865 | 0.0179 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 24.04 | 0.8789 | 0.0199 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 24.58 | 0.8858 | 0.0180 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 24.31 | 0.8826 | 0.0191 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 23.52 | 0.8701 | 0.0209 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 23.96 | 0.8799 | 0.0192 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 23.97 | 0.8797 | 0.0191 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.86 | 0.8775 | 0.0198 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 23.98 | 0.8792 | 0.0192 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 23.92 | 0.8789 | 0.0195 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 19.99 | 0.7371 | 0.0475 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 22.15 | 0.8030 | 0.0329 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 22.37 | 0.7989 | 0.0330 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 21.69 | 0.7941 | 0.0371 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 22.34 | 0.7924 | 0.0339 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 22.02 | 0.8023 | 0.0347 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 19.68 | 0.7289 | 0.0476 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 21.68 | 0.7926 | 0.0331 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 21.89 | 0.7891 | 0.0332 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 21.23 | 0.7839 | 0.0380 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 21.89 | 0.7830 | 0.0341 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 21.52 | 0.7916 | 0.0353 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.56 | 0.8491 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.59 | 0.8874 | 0.0200 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.78 | 0.8893 | 0.0194 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.98 | 0.8773 | 0.0222 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 24.73 | 0.8872 | 0.0197 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.34 | 0.8829 | 0.0212 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.28 | 0.8434 | 0.0256 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 24.18 | 0.8790 | 0.0203 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 24.39 | 0.8811 | 0.0197 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 23.60 | 0.8700 | 0.0226 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 24.39 | 0.8793 | 0.0199 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 23.90 | 0.8751 | 0.0215 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 22.94 | 0.8560 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 24.61 | 0.8867 | 0.0192 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 24.66 | 0.8861 | 0.0189 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 24.08 | 0.8794 | 0.0206 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 24.63 | 0.8846 | 0.0191 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 24.39 | 0.8841 | 0.0198 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 22.69 | 0.8512 | 0.0238 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 24.24 | 0.8801 | 0.0195 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 24.34 | 0.8802 | 0.0192 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 23.72 | 0.8732 | 0.0209 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 24.36 | 0.8790 | 0.0194 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 24.00 | 0.8778 | 0.0201 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 23.11 | 0.8622 | 0.0223 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 24.70 | 0.8896 | 0.0185 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 24.78 | 0.8909 | 0.0180 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 24.14 | 0.8808 | 0.0202 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 24.78 | 0.8899 | 0.0182 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 24.46 | 0.8858 | 0.0193 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 22.91 | 0.8583 | 0.0225 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 24.40 | 0.8832 | 0.0189 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 24.53 | 0.8852 | 0.0184 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 23.87 | 0.8753 | 0.0205 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 24.57 | 0.8846 | 0.0185 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 24.15 | 0.8797 | 0.0197 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 23.57 | 0.8712 | 0.0210 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 24.11 | 0.8828 | 0.0191 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 24.12 | 0.8827 | 0.0190 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.96 | 0.8796 | 0.0198 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 24.13 | 0.8820 | 0.0191 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 24.06 | 0.8816 | 0.0194 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 23.46 | 0.8687 | 0.0212 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 23.94 | 0.8793 | 0.0195 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 24.00 | 0.8800 | 0.0192 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 23.77 | 0.8760 | 0.0202 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 24.03 | 0.8797 | 0.0193 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 23.87 | 0.8780 | 0.0198 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 20.70 | 0.7659 | 0.0439 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 23.48 | 0.8537 | 0.0260 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 23.55 | 0.8556 | 0.0263 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 23.23 | 0.8505 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 23.79 | 0.8550 | 0.0268 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 23.13 | 0.8439 | 0.0290 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 20.58 | 0.7642 | 0.0435 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 23.60 | 0.8616 | 0.0253 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 23.16 | 0.8460 | 0.0269 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 23.21 | 0.8522 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 23.09 | 0.8361 | 0.0280 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 23.22 | 0.8537 | 0.0282 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.66 | 0.8513 | 0.0256 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 24.57 | 0.8861 | 0.0200 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 24.56 | 0.8834 | 0.0197 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 24.00 | 0.8759 | 0.0223 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 24.43 | 0.8824 | 0.0199 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 24.23 | 0.8800 | 0.0213 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.64 | 0.8509 | 0.0255 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 23.69 | 0.8681 | 0.0212 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 23.66 | 0.8695 | 0.0209 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 23.71 | 0.8703 | 0.0223 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 24.05 | 0.8739 | 0.0206 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 24.04 | 0.8760 | 0.0215 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 23.06 | 0.8584 | 0.0239 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 24.61 | 0.8867 | 0.0192 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 24.66 | 0.8861 | 0.0189 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 24.10 | 0.8783 | 0.0207 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 24.63 | 0.8846 | 0.0191 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 24.25 | 0.8805 | 0.0199 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 23.01 | 0.8579 | 0.0239 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 23.78 | 0.8711 | 0.0203 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 23.63 | 0.8687 | 0.0204 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 23.89 | 0.8741 | 0.0209 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 24.11 | 0.8757 | 0.0199 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 24.15 | 0.8787 | 0.0202 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 23.18 | 0.8622 | 0.0223 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 23.98 | 0.8740 | 0.0191 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 24.64 | 0.8861 | 0.0181 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 24.09 | 0.8788 | 0.0202 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 24.55 | 0.8834 | 0.0184 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 24.36 | 0.8825 | 0.0193 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 23.28 | 0.8629 | 0.0222 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 23.74 | 0.8721 | 0.0193 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 24.47 | 0.8827 | 0.0185 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 23.52 | 0.8708 | 0.0204 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 24.49 | 0.8818 | 0.0186 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 23.24 | 0.8677 | 0.0201 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 23.57 | 0.8712 | 0.0210 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 23.70 | 0.8738 | 0.0195 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 24.12 | 0.8827 | 0.0190 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 23.96 | 0.8796 | 0.0198 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 24.05 | 0.8807 | 0.0192 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 24.06 | 0.8816 | 0.0194 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 23.46 | 0.8687 | 0.0212 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 23.71 | 0.8748 | 0.0195 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 24.00 | 0.8800 | 0.0192 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 23.82 | 0.8767 | 0.0199 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 24.03 | 0.8797 | 0.0193 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 23.80 | 0.8760 | 0.0197 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.73 | 0.9248 | 0.0355 | 1.00 |
| flow_s0.5_pose | 24.65 | 0.9099 | 0.0374 | 1.00 |
| flow_s0.5_uniform | 23.02 | 0.8845 | 0.0430 | 1.00 |
| flow_s1.0_oracle | 26.44 | 0.9323 | 0.0341 | 1.00 |
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| flow_s1.0_uniform | 23.35 | 0.8857 | 0.0419 | 1.00 |
| gs_tok448_nat_dil_al | 22.33 | 0.8275 | 0.0672 | 1.00 |
| gs_tok448_nat_dil_al+reg | 23.71 | 0.8579 | 0.0569 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 24.63 | 0.8728 | 0.0485 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 27.44 | 0.9314 | 0.0324 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 24.78 | 0.8649 | 0.0504 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 27.41 | 0.9229 | 0.0345 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 24.34 | 0.8728 | 0.0492 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 26.48 | 0.9196 | 0.0362 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 24.78 | 0.8594 | 0.0520 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 27.25 | 0.9155 | 0.0364 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 24.57 | 0.8759 | 0.0477 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 27.30 | 0.9316 | 0.0321 | 1.00 |
| gs_tok448_nat_dil_alv | 22.03 | 0.8229 | 0.0681 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 23.70 | 0.8600 | 0.0581 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 24.15 | 0.8662 | 0.0492 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 27.45 | 0.9308 | 0.0337 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 24.30 | 0.8593 | 0.0510 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 27.44 | 0.9226 | 0.0349 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 23.88 | 0.8661 | 0.0498 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 26.65 | 0.9227 | 0.0354 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 24.32 | 0.8541 | 0.0525 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 26.89 | 0.9133 | 0.0372 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 24.09 | 0.8690 | 0.0485 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 27.29 | 0.9312 | 0.0331 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 13.17 | 0.7526 | 0.1482 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 13.69 | 0.7832 | 0.1306 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 13.94 | 0.7787 | 0.1292 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 13.36 | 0.7816 | 0.1361 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 14.02 | 0.7735 | 0.1298 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 13.49 | 0.7842 | 0.1332 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 13.15 | 0.7480 | 0.1491 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 13.68 | 0.7763 | 0.1314 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 13.93 | 0.7726 | 0.1297 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 13.34 | 0.7749 | 0.1371 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 14.02 | 0.7678 | 0.1302 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 13.47 | 0.7773 | 0.1340 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.59 | 0.5567 | 0.3037 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.72 | 0.5813 | 0.2955 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 7.79 | 0.5803 | 0.2947 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.63 | 0.5756 | 0.2988 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 7.82 | 0.5775 | 0.2946 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.65 | 0.5789 | 0.2973 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.59 | 0.5523 | 0.3042 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 7.71 | 0.5757 | 0.2961 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 7.78 | 0.5754 | 0.2952 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 7.62 | 0.5702 | 0.2995 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 7.81 | 0.5730 | 0.2950 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 7.64 | 0.5734 | 0.2979 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.78 | 0.3038 | 0.3462 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 5.88 | 0.3219 | 0.3401 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 5.92 | 0.3208 | 0.3400 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 5.81 | 0.3176 | 0.3424 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 5.94 | 0.3192 | 0.3399 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 5.83 | 0.3203 | 0.3414 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.77 | 0.2999 | 0.3466 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 5.87 | 0.3173 | 0.3406 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 5.91 | 0.3170 | 0.3403 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 5.80 | 0.3131 | 0.3429 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 5.94 | 0.3157 | 0.3400 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 5.82 | 0.3158 | 0.3419 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.57 | 0.4209 | 0.3330 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 6.66 | 0.4406 | 0.3270 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 6.68 | 0.4386 | 0.3268 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 6.59 | 0.4356 | 0.3294 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 6.69 | 0.4370 | 0.3270 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 6.61 | 0.4388 | 0.3285 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.56 | 0.4165 | 0.3335 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 6.65 | 0.4341 | 0.3278 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 6.68 | 0.4330 | 0.3274 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 6.58 | 0.4296 | 0.3302 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 6.68 | 0.4317 | 0.3274 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 6.60 | 0.4325 | 0.3293 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.53 | 0.1494 | 0.3816 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 4.56 | 0.1562 | 0.3789 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 4.56 | 0.1549 | 0.3789 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 4.54 | 0.1553 | 0.3799 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 4.56 | 0.1541 | 0.3791 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 4.55 | 0.1562 | 0.3796 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.53 | 0.1474 | 0.3818 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 4.55 | 0.1537 | 0.3791 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 4.56 | 0.1528 | 0.3790 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 4.54 | 0.1525 | 0.3802 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 4.56 | 0.1522 | 0.3792 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 4.54 | 0.1537 | 0.3798 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 25.74 | 0.9168 | 0.0397 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 24.84 | 0.9096 | 0.0421 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 28.41 | 0.9424 | 0.0307 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 27.06 | 0.9311 | 0.0352 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 28.43 | 0.9420 | 0.0306 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 27.11 | 0.9305 | 0.0352 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 27.52 | 0.9351 | 0.0337 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 26.53 | 0.9270 | 0.0368 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 28.36 | 0.9411 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 27.09 | 0.9299 | 0.0352 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 28.14 | 0.9405 | 0.0317 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 26.89 | 0.9300 | 0.0359 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 25.66 | 0.9162 | 0.0402 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 24.40 | 0.9055 | 0.0433 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 28.40 | 0.9422 | 0.0314 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 26.41 | 0.9265 | 0.0363 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 28.46 | 0.9421 | 0.0311 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 26.50 | 0.9263 | 0.0362 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 27.67 | 0.9361 | 0.0334 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 25.94 | 0.9222 | 0.0379 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 28.00 | 0.9397 | 0.0315 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 26.52 | 0.9259 | 0.0362 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 28.19 | 0.9405 | 0.0321 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 26.26 | 0.9253 | 0.0369 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 24.28 | 0.8892 | 0.0474 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 23.23 | 0.8737 | 0.0524 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 27.76 | 0.9385 | 0.0322 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 25.74 | 0.9100 | 0.0403 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 27.82 | 0.9353 | 0.0327 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 25.91 | 0.9071 | 0.0411 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 26.75 | 0.9292 | 0.0367 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 25.24 | 0.9067 | 0.0424 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 27.67 | 0.9317 | 0.0335 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 25.87 | 0.9044 | 0.0417 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 27.47 | 0.9371 | 0.0333 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 25.57 | 0.9104 | 0.0409 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 24.29 | 0.8909 | 0.0482 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 22.89 | 0.8691 | 0.0533 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 27.69 | 0.9379 | 0.0333 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 25.17 | 0.9042 | 0.0411 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 27.78 | 0.9349 | 0.0331 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 25.35 | 0.9018 | 0.0417 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 26.83 | 0.9306 | 0.0363 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 24.71 | 0.9008 | 0.0432 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 27.27 | 0.9295 | 0.0342 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 25.34 | 0.8993 | 0.0422 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 27.43 | 0.9368 | 0.0341 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 25.01 | 0.9044 | 0.0417 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 25.29 | 0.9137 | 0.0386 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 24.90 | 0.9100 | 0.0393 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 27.59 | 0.9381 | 0.0319 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 27.09 | 0.9316 | 0.0332 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 27.68 | 0.9370 | 0.0320 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 27.16 | 0.9302 | 0.0334 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 26.81 | 0.9323 | 0.0340 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 26.42 | 0.9276 | 0.0348 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 27.61 | 0.9356 | 0.0322 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 27.09 | 0.9287 | 0.0336 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 27.29 | 0.9367 | 0.0328 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 26.82 | 0.9309 | 0.0340 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 25.27 | 0.9145 | 0.0385 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 24.55 | 0.9066 | 0.0400 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 27.54 | 0.9373 | 0.0322 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 26.46 | 0.9266 | 0.0341 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 27.66 | 0.9364 | 0.0322 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 26.57 | 0.9255 | 0.0342 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 26.86 | 0.9329 | 0.0337 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 25.89 | 0.9228 | 0.0356 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 27.28 | 0.9336 | 0.0328 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 26.54 | 0.9241 | 0.0345 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 27.28 | 0.9362 | 0.0329 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 26.22 | 0.9258 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 24.41 | 0.9069 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 26.62 | 0.9284 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 26.82 | 0.9283 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 25.90 | 0.9238 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 26.80 | 0.9274 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 26.30 | 0.9266 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.27 | 0.9182 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.96 | 0.9330 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.09 | 0.9336 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.47 | 0.9291 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 27.09 | 0.9333 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.78 | 0.9315 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 25.37 | 0.9176 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 26.75 | 0.9296 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 26.84 | 0.9296 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 26.33 | 0.9264 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 26.83 | 0.9295 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 26.58 | 0.9283 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 25.33 | 0.9187 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 26.68 | 0.9300 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 26.74 | 0.9305 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 26.25 | 0.9265 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 26.74 | 0.9304 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 26.53 | 0.9285 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 25.68 | 0.9204 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 26.05 | 0.9261 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 26.06 | 0.9262 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.98 | 0.9245 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 26.07 | 0.9261 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 26.03 | 0.9255 | 0.0346 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 24.73 | 0.9078 | 0.0390 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 26.26 | 0.9242 | 0.0348 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 26.35 | 0.9236 | 0.0344 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 25.77 | 0.9206 | 0.0368 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 26.33 | 0.9226 | 0.0343 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 26.07 | 0.9231 | 0.0362 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 24.96 | 0.9137 | 0.0374 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 26.70 | 0.9288 | 0.0334 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 26.77 | 0.9285 | 0.0331 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 26.22 | 0.9255 | 0.0348 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 26.73 | 0.9279 | 0.0332 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 26.51 | 0.9276 | 0.0343 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 25.10 | 0.9140 | 0.0372 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 26.58 | 0.9270 | 0.0335 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 26.61 | 0.9264 | 0.0333 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 26.16 | 0.9244 | 0.0347 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 26.57 | 0.9258 | 0.0333 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 26.40 | 0.9262 | 0.0343 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 25.19 | 0.9164 | 0.0364 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 26.55 | 0.9276 | 0.0335 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 26.60 | 0.9277 | 0.0331 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 26.13 | 0.9247 | 0.0347 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 26.60 | 0.9274 | 0.0331 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 26.41 | 0.9266 | 0.0341 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 25.60 | 0.9193 | 0.0360 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.94 | 0.9243 | 0.0344 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 25.95 | 0.9242 | 0.0342 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.89 | 0.9233 | 0.0350 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 25.96 | 0.9241 | 0.0342 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 25.94 | 0.9240 | 0.0348 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 22.96 | 0.8655 | 0.0544 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 24.88 | 0.8948 | 0.0433 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 25.12 | 0.8904 | 0.0441 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 24.55 | 0.8934 | 0.0461 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 25.10 | 0.8858 | 0.0452 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 24.78 | 0.8957 | 0.0443 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 22.63 | 0.8607 | 0.0551 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 24.44 | 0.8887 | 0.0438 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 24.67 | 0.8850 | 0.0445 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 24.12 | 0.8873 | 0.0470 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 24.67 | 0.8809 | 0.0456 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 24.33 | 0.8895 | 0.0452 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.95 | 0.9132 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.86 | 0.9312 | 0.0335 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 26.96 | 0.9306 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.36 | 0.9274 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 26.92 | 0.9294 | 0.0338 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.68 | 0.9300 | 0.0345 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 24.67 | 0.9099 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 26.45 | 0.9268 | 0.0339 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 26.57 | 0.9266 | 0.0338 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 25.97 | 0.9232 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 26.57 | 0.9256 | 0.0340 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 26.26 | 0.9257 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 25.09 | 0.9137 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 26.67 | 0.9287 | 0.0333 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 26.73 | 0.9279 | 0.0333 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 26.23 | 0.9257 | 0.0345 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 26.70 | 0.9270 | 0.0336 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 26.50 | 0.9279 | 0.0340 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 24.83 | 0.9108 | 0.0377 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 26.30 | 0.9251 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 26.38 | 0.9248 | 0.0336 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 25.87 | 0.9222 | 0.0350 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 26.39 | 0.9242 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 26.12 | 0.9244 | 0.0345 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.18 | 0.9167 | 0.0368 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 26.66 | 0.9295 | 0.0333 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 26.71 | 0.9296 | 0.0331 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 26.19 | 0.9259 | 0.0348 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 26.70 | 0.9291 | 0.0332 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 26.50 | 0.9282 | 0.0341 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 24.99 | 0.9145 | 0.0370 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 26.42 | 0.9263 | 0.0337 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 26.52 | 0.9268 | 0.0334 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 25.96 | 0.9230 | 0.0352 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 26.56 | 0.9265 | 0.0334 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 26.23 | 0.9251 | 0.0345 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 25.64 | 0.9198 | 0.0360 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 26.05 | 0.9259 | 0.0341 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 26.06 | 0.9258 | 0.0341 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.97 | 0.9244 | 0.0348 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 26.06 | 0.9255 | 0.0341 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 26.03 | 0.9255 | 0.0346 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 25.55 | 0.9184 | 0.0361 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 25.93 | 0.9240 | 0.0344 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 25.97 | 0.9243 | 0.0342 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 25.83 | 0.9225 | 0.0352 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 25.99 | 0.9241 | 0.0342 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 25.89 | 0.9236 | 0.0349 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 23.72 | 0.8797 | 0.0508 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 26.14 | 0.9171 | 0.0374 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 26.03 | 0.9150 | 0.0382 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 25.85 | 0.9173 | 0.0406 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 26.19 | 0.9130 | 0.0380 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 25.82 | 0.9143 | 0.0401 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 23.55 | 0.8781 | 0.0508 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 26.11 | 0.9211 | 0.0365 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 25.50 | 0.9099 | 0.0398 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 25.87 | 0.9178 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 25.46 | 0.9040 | 0.0409 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 25.75 | 0.9175 | 0.0396 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 25.14 | 0.9147 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 26.88 | 0.9310 | 0.0335 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 26.85 | 0.9283 | 0.0338 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 26.38 | 0.9261 | 0.0351 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 26.73 | 0.9269 | 0.0345 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 26.55 | 0.9281 | 0.0348 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 25.13 | 0.9140 | 0.0379 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 26.08 | 0.9219 | 0.0346 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 26.03 | 0.9214 | 0.0347 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 26.13 | 0.9234 | 0.0354 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 26.42 | 0.9234 | 0.0345 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 26.37 | 0.9262 | 0.0347 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 25.27 | 0.9151 | 0.0373 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 26.67 | 0.9287 | 0.0333 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 26.73 | 0.9279 | 0.0333 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 26.25 | 0.9249 | 0.0344 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 26.70 | 0.9270 | 0.0336 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 26.35 | 0.9259 | 0.0342 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 25.25 | 0.9144 | 0.0370 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 25.94 | 0.9209 | 0.0344 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 25.84 | 0.9194 | 0.0345 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 26.05 | 0.9223 | 0.0348 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 26.28 | 0.9225 | 0.0341 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 26.24 | 0.9246 | 0.0342 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 25.29 | 0.9165 | 0.0367 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 26.12 | 0.9215 | 0.0339 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 26.63 | 0.9275 | 0.0333 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 26.16 | 0.9248 | 0.0348 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 26.55 | 0.9260 | 0.0335 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 26.45 | 0.9268 | 0.0342 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.46 | 0.9165 | 0.0365 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 25.91 | 0.9210 | 0.0345 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 26.47 | 0.9255 | 0.0335 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 25.64 | 0.9209 | 0.0353 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 26.49 | 0.9250 | 0.0335 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 25.36 | 0.9192 | 0.0352 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 25.64 | 0.9198 | 0.0360 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 25.74 | 0.9209 | 0.0345 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 26.06 | 0.9258 | 0.0341 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 25.97 | 0.9244 | 0.0348 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 26.01 | 0.9248 | 0.0341 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 26.03 | 0.9255 | 0.0346 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 25.55 | 0.9184 | 0.0361 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 25.74 | 0.9217 | 0.0348 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 25.97 | 0.9243 | 0.0342 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 25.87 | 0.9232 | 0.0352 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 25.99 | 0.9241 | 0.0342 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 25.84 | 0.9228 | 0.0351 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.41 | 0.9667 | 0.0317 | 1.00 |
| flow_s0.5_pose | 31.22 | 0.9653 | 0.0318 | 1.00 |
| flow_s0.5_uniform | 30.53 | 0.9607 | 0.0346 | 1.00 |
| flow_s1.0_oracle | 31.56 | 0.9661 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| flow_s1.0_uniform | 30.29 | 0.9592 | 0.0331 | 1.00 |
| gs_tok448_nat_dil_al | 27.21 | 0.9123 | 0.0717 | 1.00 |
| gs_tok448_nat_dil_al+reg | 28.34 | 0.9246 | 0.0633 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 28.36 | 0.9288 | 0.0511 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 30.55 | 0.9602 | 0.0365 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 28.28 | 0.9243 | 0.0539 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 30.20 | 0.9552 | 0.0394 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 28.54 | 0.9301 | 0.0518 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 30.69 | 0.9562 | 0.0387 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 28.24 | 0.9209 | 0.0564 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 30.00 | 0.9512 | 0.0421 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 28.51 | 0.9308 | 0.0501 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 30.88 | 0.9611 | 0.0356 | 1.00 |
| gs_tok448_nat_dil_alv | 27.15 | 0.9124 | 0.0720 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 28.30 | 0.9257 | 0.0647 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 28.21 | 0.9273 | 0.0515 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 30.65 | 0.9601 | 0.0366 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 28.14 | 0.9231 | 0.0541 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 30.27 | 0.9554 | 0.0394 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 28.40 | 0.9289 | 0.0522 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 30.86 | 0.9579 | 0.0379 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 28.11 | 0.9199 | 0.0566 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 30.00 | 0.9515 | 0.0423 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 28.37 | 0.9293 | 0.0505 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 30.97 | 0.9611 | 0.0355 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 10.97 | 0.7625 | 0.2326 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 11.35 | 0.7666 | 0.2117 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 11.69 | 0.7602 | 0.2095 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 11.05 | 0.7692 | 0.2189 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 11.89 | 0.7541 | 0.2102 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 11.15 | 0.7689 | 0.2155 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 10.98 | 0.7627 | 0.2326 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 11.35 | 0.7650 | 0.2120 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 11.69 | 0.7589 | 0.2098 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 11.05 | 0.7677 | 0.2191 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 11.89 | 0.7529 | 0.2104 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 11.16 | 0.7672 | 0.2157 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.33 | 0.5810 | 0.4328 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.41 | 0.5828 | 0.4295 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.47 | 0.5822 | 0.4284 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.35 | 0.5828 | 0.4307 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 6.49 | 0.5812 | 0.4282 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.36 | 0.5829 | 0.4302 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.33 | 0.5809 | 0.4328 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 6.41 | 0.5825 | 0.4295 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 6.47 | 0.5820 | 0.4284 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 6.35 | 0.5826 | 0.4307 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 6.48 | 0.5811 | 0.4282 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 6.36 | 0.5826 | 0.4303 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.02 | 0.3102 | 0.4579 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 5.09 | 0.3119 | 0.4553 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 5.13 | 0.3113 | 0.4547 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 5.04 | 0.3117 | 0.4563 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 5.14 | 0.3107 | 0.4544 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 5.05 | 0.3118 | 0.4560 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.02 | 0.3100 | 0.4580 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 5.09 | 0.3115 | 0.4554 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 5.13 | 0.3110 | 0.4548 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 5.04 | 0.3113 | 0.4564 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 5.14 | 0.3104 | 0.4544 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 5.05 | 0.3113 | 0.4562 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 5.49 | 0.4362 | 0.4561 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 5.55 | 0.4375 | 0.4542 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 5.60 | 0.4366 | 0.4537 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 5.50 | 0.4373 | 0.4550 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 5.60 | 0.4362 | 0.4536 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 5.52 | 0.4374 | 0.4549 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 5.49 | 0.4361 | 0.4561 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 5.55 | 0.4371 | 0.4542 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 5.60 | 0.4364 | 0.4537 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 5.50 | 0.4370 | 0.4551 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 5.60 | 0.4360 | 0.4536 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 5.51 | 0.4371 | 0.4550 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.08 | 0.1562 | 0.4898 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 4.10 | 0.1565 | 0.4891 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 4.11 | 0.1558 | 0.4888 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 4.08 | 0.1566 | 0.4893 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 4.11 | 0.1556 | 0.4889 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 4.09 | 0.1566 | 0.4893 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.08 | 0.1561 | 0.4898 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 4.10 | 0.1563 | 0.4891 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 4.11 | 0.1557 | 0.4888 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 4.08 | 0.1564 | 0.4893 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 4.11 | 0.1555 | 0.4889 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 4.09 | 0.1565 | 0.4893 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 31.46 | 0.9643 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 31.44 | 0.9636 | 0.0310 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 31.48 | 0.9650 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 31.44 | 0.9641 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 31.48 | 0.9649 | 0.0304 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 31.44 | 0.9641 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 31.48 | 0.9648 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 31.45 | 0.9641 | 0.0307 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 31.47 | 0.9649 | 0.0304 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 31.45 | 0.9641 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 31.48 | 0.9650 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 31.45 | 0.9641 | 0.0307 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 31.46 | 0.9642 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 31.43 | 0.9635 | 0.0310 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 31.48 | 0.9650 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 31.44 | 0.9640 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 31.48 | 0.9650 | 0.0304 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 31.44 | 0.9640 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 31.48 | 0.9648 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 31.45 | 0.9639 | 0.0307 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 31.48 | 0.9649 | 0.0304 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 31.44 | 0.9640 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 31.48 | 0.9650 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 31.44 | 0.9640 | 0.0308 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 31.40 | 0.9624 | 0.0312 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 31.35 | 0.9615 | 0.0322 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 31.48 | 0.9647 | 0.0302 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 31.42 | 0.9631 | 0.0315 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 31.48 | 0.9646 | 0.0304 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 31.42 | 0.9629 | 0.0317 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 31.47 | 0.9644 | 0.0301 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 31.42 | 0.9630 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 31.47 | 0.9645 | 0.0304 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 31.42 | 0.9628 | 0.0318 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 31.48 | 0.9647 | 0.0301 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 31.42 | 0.9631 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 31.40 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 31.35 | 0.9615 | 0.0322 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 31.48 | 0.9647 | 0.0302 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 31.42 | 0.9630 | 0.0315 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 31.48 | 0.9646 | 0.0304 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 31.43 | 0.9629 | 0.0317 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 31.48 | 0.9644 | 0.0301 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 31.42 | 0.9630 | 0.0313 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 31.48 | 0.9644 | 0.0304 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 31.43 | 0.9628 | 0.0317 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 31.48 | 0.9647 | 0.0301 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 31.42 | 0.9631 | 0.0313 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 31.35 | 0.9640 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 31.41 | 0.9644 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 31.42 | 0.9643 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 31.41 | 0.9644 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 31.42 | 0.9643 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 31.41 | 0.9644 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 31.44 | 0.9647 | 0.0307 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 31.45 | 0.9648 | 0.0304 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 31.45 | 0.9647 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 31.46 | 0.9649 | 0.0306 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 30.25 | 0.9565 | 0.0405 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 30.55 | 0.9569 | 0.0389 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 30.55 | 0.9547 | 0.0400 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 30.64 | 0.9582 | 0.0377 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 30.47 | 0.9531 | 0.0412 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 30.60 | 0.9579 | 0.0380 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 30.13 | 0.9564 | 0.0406 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 30.42 | 0.9567 | 0.0389 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 30.43 | 0.9546 | 0.0399 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 30.52 | 0.9580 | 0.0378 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 30.35 | 0.9531 | 0.0412 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 30.47 | 0.9577 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.34 | 0.9643 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 31.44 | 0.9646 | 0.0309 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 31.41 | 0.9638 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 31.42 | 0.9646 | 0.0310 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 31.38 | 0.9635 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 31.44 | 0.9646 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 31.35 | 0.9643 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 31.44 | 0.9646 | 0.0309 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 31.40 | 0.9638 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 31.42 | 0.9646 | 0.0309 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 31.38 | 0.9635 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 31.44 | 0.9646 | 0.0310 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 31.36 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 31.42 | 0.9642 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 31.44 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 31.40 | 0.9640 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 31.45 | 0.9650 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 31.37 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 31.41 | 0.9641 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 31.44 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 31.39 | 0.9639 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 31.43 | 0.9648 | 0.0307 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 31.44 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 31.46 | 0.9650 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 31.43 | 0.9645 | 0.0309 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 31.46 | 0.9650 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 31.44 | 0.9648 | 0.0307 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 31.45 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 31.44 | 0.9644 | 0.0310 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 31.45 | 0.9647 | 0.0307 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 31.45 | 0.9646 | 0.0308 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 31.45 | 0.9647 | 0.0307 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 31.45 | 0.9645 | 0.0308 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 30.64 | 0.9588 | 0.0364 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 30.94 | 0.9618 | 0.0335 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 30.96 | 0.9606 | 0.0341 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 31.12 | 0.9627 | 0.0322 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 30.84 | 0.9595 | 0.0348 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 31.02 | 0.9618 | 0.0334 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 30.57 | 0.9587 | 0.0364 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 31.02 | 0.9625 | 0.0330 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 30.65 | 0.9598 | 0.0351 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 31.16 | 0.9627 | 0.0324 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 30.61 | 0.9581 | 0.0362 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 31.02 | 0.9624 | 0.0328 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 31.31 | 0.9642 | 0.0313 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 31.44 | 0.9647 | 0.0309 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 31.40 | 0.9638 | 0.0317 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 31.39 | 0.9646 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 31.37 | 0.9632 | 0.0321 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 31.41 | 0.9646 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 31.32 | 0.9643 | 0.0312 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 31.35 | 0.9645 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 31.34 | 0.9636 | 0.0319 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 31.37 | 0.9646 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 31.36 | 0.9634 | 0.0320 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 31.40 | 0.9646 | 0.0311 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 31.34 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 31.42 | 0.9642 | 0.0312 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 31.42 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 31.40 | 0.9640 | 0.0313 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 31.43 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 31.35 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 31.36 | 0.9647 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 31.35 | 0.9639 | 0.0314 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 31.40 | 0.9648 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 31.37 | 0.9638 | 0.0314 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 31.42 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 31.39 | 0.9648 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 31.44 | 0.9648 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 31.44 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 31.46 | 0.9650 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 31.43 | 0.9645 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 31.46 | 0.9650 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 31.41 | 0.9648 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 31.43 | 0.9648 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 31.45 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 31.44 | 0.9644 | 0.0310 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 31.44 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 31.45 | 0.9647 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 31.45 | 0.9646 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 31.45 | 0.9649 | 0.0306 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 31.45 | 0.9647 | 0.0307 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 31.45 | 0.9645 | 0.0308 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 31.46 | 0.9649 | 0.0305 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_tok448_nat_dil_al | 24.77 | 0.8847 | 0.0876 | 1.00 |
| gs_tok448_nat_dil_al+reg | 26.08 | 0.9017 | 0.0821 | 1.00 |
| gs_tok448_nat_dil_al_tto100 | 26.73 | 0.9124 | 0.0573 | 1.00 |
| gs_tok448_nat_dil_al_tto100+reg | 29.40 | 0.9524 | 0.0434 | 1.00 |
| gs_tok448_nat_dil_al_tto200 | 26.73 | 0.9074 | 0.0595 | 1.00 |
| gs_tok448_nat_dil_al_tto200+reg | 29.13 | 0.9467 | 0.0459 | 1.00 |
| gs_tok448_nat_dil_al_tto25 | 26.57 | 0.9120 | 0.0612 | 1.00 |
| gs_tok448_nat_dil_al_tto25+reg | 28.89 | 0.9448 | 0.0510 | 1.00 |
| gs_tok448_nat_dil_al_tto300 | 26.67 | 0.9035 | 0.0622 | 1.00 |
| gs_tok448_nat_dil_al_tto300+reg | 28.90 | 0.9418 | 0.0488 | 1.00 |
| gs_tok448_nat_dil_al_tto50 | 26.75 | 0.9142 | 0.0578 | 1.00 |
| gs_tok448_nat_dil_al_tto50+reg | 29.48 | 0.9524 | 0.0445 | 1.00 |
| gs_tok448_nat_dil_alv | 24.54 | 0.8829 | 0.0881 | 1.00 |
| gs_tok448_nat_dil_alv+reg | 26.06 | 0.9034 | 0.0848 | 1.00 |
| gs_tok448_nat_dil_alv_tto100 | 26.32 | 0.9089 | 0.0580 | 1.00 |
| gs_tok448_nat_dil_alv_tto100+reg | 29.42 | 0.9520 | 0.0445 | 1.00 |
| gs_tok448_nat_dil_alv_tto200 | 26.34 | 0.9044 | 0.0600 | 1.00 |
| gs_tok448_nat_dil_alv_tto200+reg | 29.14 | 0.9467 | 0.0461 | 1.00 |
| gs_tok448_nat_dil_alv_tto25 | 26.19 | 0.9087 | 0.0616 | 1.00 |
| gs_tok448_nat_dil_alv_tto25+reg | 29.03 | 0.9466 | 0.0502 | 1.00 |
| gs_tok448_nat_dil_alv_tto300 | 26.30 | 0.9007 | 0.0626 | 1.00 |
| gs_tok448_nat_dil_alv_tto300+reg | 28.67 | 0.9413 | 0.0495 | 1.00 |
| gs_tok448_nat_dil_alv_tto50 | 26.34 | 0.9106 | 0.0584 | 1.00 |
| gs_tok448_nat_dil_alv_tto50+reg | 29.51 | 0.9522 | 0.0453 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 11.59 | 0.7565 | 0.2483 | 1.00 |
| gs_tokr5448_nat_dil_al_tto100_local | 12.00 | 0.7720 | 0.2168 | 1.00 |
| gs_tokr5448_nat_dil_al_tto200_local | 12.33 | 0.7657 | 0.2141 | 1.00 |
| gs_tokr5448_nat_dil_al_tto25_local | 11.71 | 0.7720 | 0.2284 | 1.00 |
| gs_tokr5448_nat_dil_al_tto300_local | 12.51 | 0.7594 | 0.2150 | 1.00 |
| gs_tokr5448_nat_dil_al_tto50_local | 11.81 | 0.7733 | 0.2231 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 11.58 | 0.7548 | 0.2485 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto100_local | 12.00 | 0.7684 | 0.2174 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto200_local | 12.32 | 0.7626 | 0.2144 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto25_local | 11.70 | 0.7685 | 0.2287 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto300_local | 12.51 | 0.7565 | 0.2151 | 1.00 |
| gs_tokr5448_nat_dil_alv_tto50_local | 11.81 | 0.7697 | 0.2235 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.65 | 0.5676 | 0.4856 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.73 | 0.5778 | 0.4769 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.79 | 0.5770 | 0.4754 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.67 | 0.5756 | 0.4807 | 1.00 |
| gs_tokrife448_nat_dil_al_tto300_local | 6.81 | 0.5755 | 0.4749 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.69 | 0.5771 | 0.4791 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 6.64 | 0.5658 | 0.4860 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto100_local | 6.73 | 0.5755 | 0.4773 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto200_local | 6.79 | 0.5750 | 0.4758 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto25_local | 6.67 | 0.5734 | 0.4812 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto300_local | 6.81 | 0.5736 | 0.4752 | 1.00 |
| gs_tokrife448_nat_dil_alv_tto50_local | 6.68 | 0.5748 | 0.4795 | 1.00 |
| gs_tokrife_g448_nat_dil_al_local | 5.26 | 0.3065 | 0.5300 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto100_local | 5.33 | 0.3146 | 0.5231 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto200_local | 5.37 | 0.3137 | 0.5224 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto25_local | 5.28 | 0.3127 | 0.5262 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto300_local | 5.38 | 0.3127 | 0.5219 | 1.00 |
| gs_tokrife_g448_nat_dil_al_tto50_local | 5.30 | 0.3139 | 0.5249 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_local | 5.26 | 0.3049 | 0.5303 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto100_local | 5.33 | 0.3126 | 0.5234 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto200_local | 5.37 | 0.3122 | 0.5226 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto25_local | 5.28 | 0.3108 | 0.5264 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto300_local | 5.38 | 0.3114 | 0.5220 | 1.00 |
| gs_tokrife_g448_nat_dil_alv_tto50_local | 5.29 | 0.3120 | 0.5252 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 5.79 | 0.4278 | 0.5211 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto100_local | 5.86 | 0.4362 | 0.5145 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto200_local | 5.90 | 0.4351 | 0.5134 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto25_local | 5.81 | 0.4342 | 0.5176 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto300_local | 5.90 | 0.4343 | 0.5128 | 1.00 |
| gs_tokstrict448_nat_dil_al_tto50_local | 5.82 | 0.4356 | 0.5164 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 5.79 | 0.4260 | 0.5215 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto100_local | 5.85 | 0.4336 | 0.5151 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto200_local | 5.89 | 0.4329 | 0.5138 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto25_local | 5.80 | 0.4318 | 0.5181 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto300_local | 5.90 | 0.4321 | 0.5131 | 1.00 |
| gs_tokstrict448_nat_dil_alv_tto50_local | 5.82 | 0.4330 | 0.5170 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_local | 4.24 | 0.1529 | 0.5770 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto100_local | 4.27 | 0.1563 | 0.5744 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto200_local | 4.28 | 0.1555 | 0.5739 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto25_local | 4.25 | 0.1559 | 0.5755 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto300_local | 4.28 | 0.1550 | 0.5738 | 1.00 |
| gs_tokstrict_g448_nat_dil_al_tto50_local | 4.26 | 0.1564 | 0.5751 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_local | 4.24 | 0.1521 | 0.5771 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto100_local | 4.27 | 0.1553 | 0.5746 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto200_local | 4.28 | 0.1546 | 0.5740 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto25_local | 4.25 | 0.1547 | 0.5757 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto300_local | 4.28 | 0.1542 | 0.5739 | 1.00 |
| gs_tokstrict_g448_nat_dil_alv_tto50_local | 4.26 | 0.1553 | 0.5752 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al+reg] | 28.29 | 0.9472 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al] | 27.56 | 0.9436 | 0.0478 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100+reg] | 30.11 | 0.9577 | 0.0358 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto100] | 29.19 | 0.9523 | 0.0398 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200+reg] | 30.12 | 0.9574 | 0.0360 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto200] | 29.21 | 0.9520 | 0.0399 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25+reg] | 29.54 | 0.9546 | 0.0390 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto25] | 28.78 | 0.9506 | 0.0415 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300+reg] | 30.07 | 0.9570 | 0.0363 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto300] | 29.18 | 0.9517 | 0.0401 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50+reg] | 29.94 | 0.9569 | 0.0368 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_al_tto50] | 29.05 | 0.9518 | 0.0404 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv+reg] | 28.21 | 0.9468 | 0.0461 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv] | 27.16 | 0.9418 | 0.0487 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100+reg] | 30.11 | 0.9576 | 0.0363 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto100] | 28.66 | 0.9501 | 0.0406 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200+reg] | 30.14 | 0.9574 | 0.0362 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto200] | 28.73 | 0.9500 | 0.0407 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25+reg] | 29.63 | 0.9549 | 0.0385 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto25] | 28.30 | 0.9484 | 0.0423 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300+reg] | 29.79 | 0.9565 | 0.0369 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto300] | 28.72 | 0.9499 | 0.0409 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50+reg] | 29.98 | 0.9569 | 0.0370 | 1.00 |
| hyb_oracle_fail[gs_tok448_nat_dil_alv_tto50] | 28.53 | 0.9497 | 0.0413 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al+reg] | 27.13 | 0.9337 | 0.0539 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al] | 26.29 | 0.9275 | 0.0575 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100+reg] | 29.67 | 0.9559 | 0.0376 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto100] | 28.32 | 0.9428 | 0.0447 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200+reg] | 29.70 | 0.9546 | 0.0378 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto200] | 28.43 | 0.9415 | 0.0453 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25+reg] | 28.94 | 0.9515 | 0.0425 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto25] | 27.86 | 0.9411 | 0.0473 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300+reg] | 29.60 | 0.9532 | 0.0387 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto300] | 28.39 | 0.9404 | 0.0459 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50+reg] | 29.44 | 0.9551 | 0.0389 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_al_tto50] | 28.15 | 0.9428 | 0.0454 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv+reg] | 27.13 | 0.9347 | 0.0552 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv] | 26.00 | 0.9257 | 0.0581 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100+reg] | 29.62 | 0.9556 | 0.0385 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto100] | 27.84 | 0.9406 | 0.0453 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200+reg] | 29.67 | 0.9544 | 0.0381 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto200] | 27.98 | 0.9395 | 0.0456 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25+reg] | 29.00 | 0.9519 | 0.0420 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto25] | 27.44 | 0.9389 | 0.0478 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300+reg] | 29.28 | 0.9523 | 0.0392 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto300] | 27.96 | 0.9385 | 0.0462 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50+reg] | 29.43 | 0.9549 | 0.0395 | 1.00 |
| hyb_risk[gs_tok448_nat_dil_alv_tto50] | 27.69 | 0.9406 | 0.0459 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al+reg] | 28.00 | 0.9467 | 0.0428 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al] | 27.73 | 0.9455 | 0.0433 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100+reg] | 29.59 | 0.9556 | 0.0366 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto100] | 29.35 | 0.9534 | 0.0375 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200+reg] | 29.65 | 0.9552 | 0.0365 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto200] | 29.38 | 0.9528 | 0.0375 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25+reg] | 29.05 | 0.9535 | 0.0387 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto25] | 28.85 | 0.9520 | 0.0391 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300+reg] | 29.61 | 0.9547 | 0.0368 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto300] | 29.33 | 0.9523 | 0.0378 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50+reg] | 29.39 | 0.9551 | 0.0375 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_al_tto50] | 29.15 | 0.9531 | 0.0383 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv+reg] | 27.98 | 0.9470 | 0.0429 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv] | 27.43 | 0.9443 | 0.0438 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100+reg] | 29.56 | 0.9552 | 0.0367 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto100] | 28.88 | 0.9515 | 0.0381 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200+reg] | 29.62 | 0.9549 | 0.0365 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto200] | 28.95 | 0.9511 | 0.0381 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25+reg] | 29.10 | 0.9536 | 0.0383 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto25] | 28.44 | 0.9502 | 0.0395 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300+reg] | 29.37 | 0.9539 | 0.0371 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto300] | 28.92 | 0.9505 | 0.0383 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50+reg] | 29.38 | 0.9549 | 0.0374 | 1.00 |
| hyb_risktuned[gs_tok448_nat_dil_alv_tto50] | 28.70 | 0.9513 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_local] | 27.35 | 0.9434 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto100_local] | 29.06 | 0.9520 | 0.0384 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto200_local] | 29.16 | 0.9518 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto25_local] | 28.50 | 0.9502 | 0.0414 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto300_local] | 29.13 | 0.9513 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokr5448_nat_dil_al_tto50_local] | 28.81 | 0.9514 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.94 | 0.9483 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.15 | 0.9538 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 29.23 | 0.9541 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.80 | 0.9524 | 0.0385 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto300_local] | 29.23 | 0.9540 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.02 | 0.9533 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_local] | 28.01 | 0.9482 | 0.0401 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto100_local] | 28.98 | 0.9527 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto200_local] | 29.03 | 0.9527 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto25_local] | 28.69 | 0.9515 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto300_local] | 29.02 | 0.9526 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_g448_nat_dil_al_tto50_local] | 28.87 | 0.9523 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_local] | 28.02 | 0.9486 | 0.0399 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto100_local] | 28.96 | 0.9529 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto200_local] | 29.00 | 0.9531 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto25_local] | 28.66 | 0.9515 | 0.0385 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto300_local] | 29.00 | 0.9530 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict448_nat_dil_al_tto50_local] | 28.85 | 0.9523 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_local] | 28.27 | 0.9492 | 0.0395 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto100_local] | 28.50 | 0.9516 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto200_local] | 28.50 | 0.9516 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto25_local] | 28.44 | 0.9509 | 0.0387 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto300_local] | 28.51 | 0.9516 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokstrict_g448_nat_dil_al_tto50_local] | 28.48 | 0.9513 | 0.0385 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_local] | 27.58 | 0.9446 | 0.0425 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto100_local] | 28.69 | 0.9504 | 0.0386 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto200_local] | 28.75 | 0.9501 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto25_local] | 28.33 | 0.9492 | 0.0405 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto300_local] | 28.74 | 0.9498 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokr5448_nat_dil_al_tto50_local] | 28.56 | 0.9500 | 0.0399 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_local] | 27.72 | 0.9468 | 0.0408 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto100_local] | 28.94 | 0.9521 | 0.0375 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto200_local] | 28.98 | 0.9520 | 0.0371 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto25_local] | 28.62 | 0.9510 | 0.0388 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto300_local] | 28.96 | 0.9517 | 0.0371 | 1.00 |
| hyb_tokchk_w20[gs_tokrife448_nat_dil_al_tto50_local] | 28.82 | 0.9518 | 0.0383 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_local] | 27.80 | 0.9469 | 0.0406 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto100_local] | 28.87 | 0.9516 | 0.0374 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto200_local] | 28.89 | 0.9514 | 0.0372 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto25_local] | 28.58 | 0.9507 | 0.0385 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto300_local] | 28.86 | 0.9512 | 0.0372 | 1.00 |
| hyb_tokchk_w20[gs_tokrife_g448_nat_dil_al_tto50_local] | 28.75 | 0.9513 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_local] | 27.92 | 0.9478 | 0.0400 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto100_local] | 28.85 | 0.9518 | 0.0375 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto200_local] | 28.88 | 0.9518 | 0.0371 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto25_local] | 28.56 | 0.9508 | 0.0386 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto300_local] | 28.88 | 0.9517 | 0.0371 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict448_nat_dil_al_tto50_local] | 28.76 | 0.9515 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_local] | 28.21 | 0.9486 | 0.0395 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto100_local] | 28.43 | 0.9508 | 0.0383 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto200_local] | 28.44 | 0.9508 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto25_local] | 28.39 | 0.9504 | 0.0387 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto300_local] | 28.44 | 0.9507 | 0.0381 | 1.00 |
| hyb_tokchk_w20[gs_tokstrict_g448_nat_dil_al_tto50_local] | 28.42 | 0.9507 | 0.0386 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 26.00 | 0.9231 | 0.0594 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto100_local] | 27.58 | 0.9350 | 0.0477 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto200_local] | 27.74 | 0.9323 | 0.0482 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto25_local] | 27.27 | 0.9345 | 0.0511 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto300_local] | 27.68 | 0.9299 | 0.0492 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_tto50_local] | 27.47 | 0.9357 | 0.0492 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.71 | 0.9213 | 0.0599 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto100_local] | 27.17 | 0.9327 | 0.0481 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto200_local] | 27.33 | 0.9304 | 0.0484 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto25_local] | 26.90 | 0.9322 | 0.0517 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto300_local] | 27.30 | 0.9281 | 0.0495 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_tto50_local] | 27.07 | 0.9334 | 0.0496 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.69 | 0.9465 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.10 | 0.9532 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 29.15 | 0.9525 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.73 | 0.9518 | 0.0396 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto300_local] | 29.11 | 0.9519 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.96 | 0.9528 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.46 | 0.9453 | 0.0421 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto100_local] | 28.79 | 0.9515 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto200_local] | 28.86 | 0.9509 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto25_local] | 28.45 | 0.9502 | 0.0398 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto300_local] | 28.85 | 0.9504 | 0.0386 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_tto50_local] | 28.66 | 0.9512 | 0.0392 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_local] | 27.78 | 0.9467 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto100_local] | 28.94 | 0.9524 | 0.0372 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto200_local] | 28.96 | 0.9516 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto25_local] | 28.63 | 0.9513 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto300_local] | 28.92 | 0.9511 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_al_tto50_local] | 28.82 | 0.9521 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_local] | 27.57 | 0.9457 | 0.0412 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto100_local] | 28.68 | 0.9510 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto200_local] | 28.72 | 0.9504 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto25_local] | 28.37 | 0.9499 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto300_local] | 28.72 | 0.9500 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife_g448_nat_dil_alv_tto50_local] | 28.55 | 0.9508 | 0.0384 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 27.90 | 0.9478 | 0.0405 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto100_local] | 28.95 | 0.9527 | 0.0375 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto200_local] | 28.98 | 0.9526 | 0.0372 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto25_local] | 28.62 | 0.9513 | 0.0388 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto300_local] | 28.97 | 0.9523 | 0.0374 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_tto50_local] | 28.84 | 0.9523 | 0.0382 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 27.76 | 0.9469 | 0.0407 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto100_local] | 28.78 | 0.9514 | 0.0378 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto200_local] | 28.83 | 0.9515 | 0.0375 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto25_local] | 28.45 | 0.9502 | 0.0391 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto300_local] | 28.85 | 0.9512 | 0.0376 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_tto50_local] | 28.65 | 0.9510 | 0.0385 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_local] | 28.24 | 0.9489 | 0.0396 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto100_local] | 28.50 | 0.9515 | 0.0382 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto200_local] | 28.50 | 0.9513 | 0.0381 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto25_local] | 28.44 | 0.9509 | 0.0387 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto300_local] | 28.50 | 0.9511 | 0.0382 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_al_tto50_local] | 28.48 | 0.9513 | 0.0385 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_local] | 28.18 | 0.9483 | 0.0398 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 28.43 | 0.9507 | 0.0384 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 28.45 | 0.9507 | 0.0382 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 28.35 | 0.9501 | 0.0390 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 28.46 | 0.9505 | 0.0383 | 1.00 |
| hyb_token[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 28.40 | 0.9505 | 0.0388 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 26.62 | 0.9292 | 0.0581 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto100_local] | 28.42 | 0.9467 | 0.0437 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto200_local] | 28.35 | 0.9452 | 0.0443 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto25_local] | 28.29 | 0.9465 | 0.0474 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto300_local] | 28.43 | 0.9442 | 0.0437 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_tto50_local] | 28.23 | 0.9452 | 0.0466 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 26.50 | 0.9285 | 0.0581 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto100_local] | 28.41 | 0.9484 | 0.0428 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto200_local] | 27.86 | 0.9433 | 0.0457 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto25_local] | 28.37 | 0.9466 | 0.0475 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto300_local] | 27.87 | 0.9403 | 0.0463 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_tto50_local] | 28.22 | 0.9469 | 0.0459 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.81 | 0.9468 | 0.0420 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto100_local] | 29.04 | 0.9529 | 0.0377 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto200_local] | 29.00 | 0.9515 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto25_local] | 28.65 | 0.9512 | 0.0392 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto300_local] | 28.98 | 0.9509 | 0.0388 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_tto50_local] | 28.80 | 0.9520 | 0.0389 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.82 | 0.9465 | 0.0415 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto100_local] | 28.46 | 0.9498 | 0.0388 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto200_local] | 28.45 | 0.9493 | 0.0394 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto25_local] | 28.49 | 0.9501 | 0.0395 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto300_local] | 28.73 | 0.9496 | 0.0390 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_tto50_local] | 28.70 | 0.9514 | 0.0389 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_local] | 27.91 | 0.9472 | 0.0409 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto100_local] | 28.94 | 0.9524 | 0.0372 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto200_local] | 28.96 | 0.9516 | 0.0376 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto25_local] | 28.62 | 0.9510 | 0.0384 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto300_local] | 28.92 | 0.9511 | 0.0378 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_al_tto50_local] | 28.68 | 0.9514 | 0.0382 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_local] | 27.91 | 0.9468 | 0.0406 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto100_local] | 28.42 | 0.9497 | 0.0384 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto200_local] | 28.33 | 0.9488 | 0.0388 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto25_local] | 28.48 | 0.9500 | 0.0387 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto300_local] | 28.65 | 0.9496 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokrife_g448_nat_dil_alv_tto50_local] | 28.62 | 0.9510 | 0.0381 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 27.95 | 0.9476 | 0.0404 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto100_local] | 28.54 | 0.9494 | 0.0377 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto200_local] | 28.88 | 0.9518 | 0.0373 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto25_local] | 28.58 | 0.9510 | 0.0388 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto300_local] | 28.83 | 0.9511 | 0.0376 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_tto50_local] | 28.77 | 0.9517 | 0.0382 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 28.08 | 0.9475 | 0.0403 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto100_local] | 28.41 | 0.9494 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto200_local] | 28.79 | 0.9510 | 0.0375 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto25_local] | 28.14 | 0.9493 | 0.0390 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto300_local] | 28.80 | 0.9508 | 0.0377 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_tto50_local] | 27.90 | 0.9487 | 0.0388 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_local] | 28.24 | 0.9489 | 0.0396 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto100_local] | 28.31 | 0.9494 | 0.0384 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto200_local] | 28.50 | 0.9513 | 0.0381 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto25_local] | 28.44 | 0.9509 | 0.0387 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto300_local] | 28.47 | 0.9508 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_al_tto50_local] | 28.48 | 0.9513 | 0.0385 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_local] | 28.18 | 0.9483 | 0.0398 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto100_local] | 28.31 | 0.9497 | 0.0387 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto200_local] | 28.45 | 0.9507 | 0.0382 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto25_local] | 28.37 | 0.9502 | 0.0389 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto300_local] | 28.46 | 0.9505 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokstrict_g448_nat_dil_alv_tto50_local] | 28.36 | 0.9501 | 0.0389 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_tok448_nat_dil_al | 0.50 | 0.83 |
| cam3 | gs_tok448_nat_dil_al_tto100 | 0.80 | 1.00 |
| cam3 | gs_tok448_nat_dil_al_tto200 | 0.83 | 1.00 |
| cam3 | gs_tok448_nat_dil_al_tto25 | 0.78 | 1.00 |
| cam3 | gs_tok448_nat_dil_al_tto300 | 0.82 | 1.00 |
| cam3 | gs_tok448_nat_dil_al_tto50 | 0.78 | 1.00 |
| cam3 | gs_tok448_nat_dil_alv | 0.64 | 1.00 |
| cam3 | gs_tok448_nat_dil_alv_tto100 | 0.83 | 1.00 |
| cam3 | gs_tok448_nat_dil_alv_tto200 | 0.89 | 1.00 |
| cam3 | gs_tok448_nat_dil_alv_tto25 | 0.91 | 1.00 |
| cam3 | gs_tok448_nat_dil_alv_tto300 | 0.85 | 1.00 |
| cam3 | gs_tok448_nat_dil_alv_tto50 | 0.89 | 1.00 |
| cam5 | gs_tok448_nat_dil_al | 1.28 | 1.00 |
| cam5 | gs_tok448_nat_dil_al_tto100 | 1.34 | 1.00 |
| cam5 | gs_tok448_nat_dil_al_tto200 | 1.32 | 1.00 |
| cam5 | gs_tok448_nat_dil_al_tto25 | 1.29 | 1.00 |
| cam5 | gs_tok448_nat_dil_al_tto300 | 1.31 | 1.00 |
| cam5 | gs_tok448_nat_dil_al_tto50 | 1.34 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv | 1.42 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv_tto100 | 1.43 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv_tto200 | 1.42 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv_tto25 | 1.44 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv_tto300 | 1.36 | 1.00 |
| cam5 | gs_tok448_nat_dil_alv_tto50 | 1.44 | 1.00 |

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
| cam3 | gs_tok448_nat_dil_al | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 46.7 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_al_tto100 | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 25.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_al_tto200 | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 28.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_al_tto25 | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 26.1 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_al_tto300 | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 28.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_al_tto50 | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 31.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_alv | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 27.7 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_alv_tto100 | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 26.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_alv_tto200 | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 26.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_alv_tto25 | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 27.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_alv_tto300 | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 25.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tok448_nat_dil_alv_tto50 | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 31.4 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 67.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_al_tto100_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 44.3 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_al_tto200_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 48.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_al_tto25_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 41.3 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_al_tto300_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 41.8 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_al_tto50_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 45.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 58.7 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_alv_tto100_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 41.5 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_alv_tto200_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 42.4 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_alv_tto25_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 42.5 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_alv_tto300_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 44.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokr5448_nat_dil_alv_tto50_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 47.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 65.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 72.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 69.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 64.4 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_al_tto300_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 66.3 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 60.3 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 78.4 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_alv_tto100_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 62.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_alv_tto200_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 60.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_alv_tto25_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 54.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_alv_tto300_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 58.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife448_nat_dil_alv_tto50_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 67.1 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 35.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto100_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 34.8 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto200_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 41.8 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto25_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 40.5 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto300_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 35.8 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_al_tto50_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 35.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 42.5 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto100_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 37.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto200_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 36.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto25_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 36.5 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto300_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 42.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokrife_g448_nat_dil_alv_tto50_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 37.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 45.7 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_al_tto100_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 55.1 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_al_tto200_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 48.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_al_tto25_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 52.3 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_al_tto300_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 51.8 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_al_tto50_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 57.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 53.7 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto100_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 49.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto200_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 44.1 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto25_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 62.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto300_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 53.8 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict448_nat_dil_alv_tto50_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 44.9 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 36.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto100_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 43.3 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto200_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 36.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto25_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 39.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto300_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 35.3 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_al_tto50_local | aligned_int | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 35.8 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 37.7 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto100_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 36.1 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto200_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 33.0 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto25_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 42.6 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto300_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 43.2 | 29.12 | 0.35 | 0.010 |
| cam3 | gs_tokstrict_g448_nat_dil_alv_tto50_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368444 | 0.825 | 42.6 | 29.12 | 0.35 | 0.010 |
| cam5 | gs_tok448_nat_dil_al | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 44.6 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_al_tto100 | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 32.3 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_al_tto200 | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 25.2 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_al_tto25 | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 32.3 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_al_tto300 | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 25.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_al_tto50 | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 40.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_alv | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 32.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_alv_tto100 | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 25.7 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_alv_tto200 | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 39.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_alv_tto25 | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 40.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_alv_tto300 | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 24.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tok448_nat_dil_alv_tto50 | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 26.1 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 42.7 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_al_tto100_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 45.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_al_tto200_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 44.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_al_tto25_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 43.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_al_tto300_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 42.2 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_al_tto50_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 45.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 43.1 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv_tto100_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 43.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv_tto200_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 43.2 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv_tto25_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 43.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv_tto300_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 42.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv_tto50_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 44.6 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 68.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 53.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 65.7 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 50.3 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto300_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 63.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 71.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 60.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_alv_tto100_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 64.1 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_alv_tto200_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 63.6 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_alv_tto25_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 64.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_alv_tto300_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 62.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_alv_tto50_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 67.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 44.2 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto100_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 44.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto200_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 36.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto25_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 38.6 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto300_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 50.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_al_tto50_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 51.1 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 44.2 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto100_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 38.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto200_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 51.6 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto25_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 48.7 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto300_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 50.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokrife_g448_nat_dil_alv_tto50_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 43.8 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 58.1 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_al_tto100_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 51.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_al_tto200_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 50.7 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_al_tto25_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 61.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_al_tto300_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 51.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_al_tto50_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 51.6 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 46.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto100_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 61.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto200_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 45.0 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto25_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 57.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto300_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 51.2 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict448_nat_dil_alv_tto50_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 43.3 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 34.7 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto100_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 33.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto200_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 31.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto25_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 31.4 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto300_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 33.5 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_al_tto50_local | aligned_int | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 34.1 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 35.2 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto100_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 37.1 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto200_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 34.7 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto25_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 33.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto300_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 34.9 | 29.43 | 0.11 | 0.007 |
| cam5 | gs_tokstrict_g448_nat_dil_alv_tto50_local | aligned_vggt | 917 | None | classic | 1.96 | False | 529224 | 0.516 | 36.1 | 29.43 | 0.11 | 0.007 |

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
