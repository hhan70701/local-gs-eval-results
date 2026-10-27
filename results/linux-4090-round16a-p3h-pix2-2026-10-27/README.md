# linux-4090 round16a p3h / pix2

源码标签 [linux-4090-round16a-p3h-pix2](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-4090-round16a-p3h-pix2)，提交 `34ee4649f2a76980c36d0d600a6ddf3b93a70296`。

按照 README，在第十五轮工作目录复用已完成的 aligned、token、flow、AnySplat、pixgs 结果，补跑本机 23 组场景的 p3h/pix2 FS-L、FS-S、FLW 共六个变体及四个 gated 变体，然后重新 evaluate/validate。输入相机 0/3/5，目标相机 1/2/4，共 69 个目标视点。

## 结果与检查

- [实验汇总](summary_all.md)、[密集视点计时](bench_dense_linux-4090.md)、[逐场景计时数据](bench_dense_linux-4090.json)。
- 23 组验证全部 PASS，69 张主对比图齐全，每组 10 个新变体；pix2 使用 gsplat，p3h 使用 splat。
- 24 项单元测试通过。补跑评估 3524.12 秒，密集计时 57.60 秒。
- 验证警告共 4 条，详情见 [完整性检查](completion_check.json) 及各场景 eval/validation.json。
- [补跑日志](dataset6_r16a.log)、[计时日志](bench_dense.log)；各场景包含完整 eval、logs、配置、poses、GS JSON 元数据。

## 复用与计时说明

原始完整基线见 [round15 已发布结果](https://github.com/hhan70701/local-gs-eval-results/tree/experiment/linux-4090-round15-pixgs-2026-10-25/results/linux-4090-round15-pixgs-2026-10-25)，本次复用的全部旧 GS JSON 与其逐字节一致。
本次场景 timing.json 仅记录 pixgs/evaluate/validate 三步，旧 AnySplat/TTO 时间来自旧元数据，不是本次重测。
只覆盖 work_root 为 work/dataset6_round15_pixgs；其余配置等于本轮源码默认值。
密集视点计时按默认前六组、cnw_cnn、FS-L、pix2/p3h、每对 41/60 视点执行，计时前无其他 GPU 计算进程，证据见 environment/benchmark_*。
合计不含对应关系推理时间；对应关系的 Windows RTX 3090 导出时间单列；token 检测引用既有报告，未在本次计时。

## 比较范围与环境

cnw_cnn 及其新变体的泛化结论仅看汇总中的三组试点：changjing/shot_0000、changjing1/shot_0001、changjing1/shot_0022。其余场景参与过 CNN 训练。Oracle 使用真值失败区，仅作诊断。
源码、基线提交、输入哈希、GPU、依赖见 [environment_and_inputs.json](environment_and_inputs.json)、environment/；配置见 [base_config.yaml](base_config.yaml)。
沿用用户授权生成的半像素矩阵 H_halfpx[i] = T(-0.5,-0.5) @ H_existing[i]，裁剪起点 (192.5,104.5)。矩阵见 calibration/，生成记录见 environment/halfpx-generation.json。
完整输出保留在主机；此分支不包含原始数据、模型权重和 aligned/flow/gs 大图，只发布 4090 结果。
