# linux-4090 round15 pixgs

源码标签 [linux-4090-round15-pixgs](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-4090-round15-pixgs)，提交 `cae8a7b2a4245f20c966fc1cc15137f52a5e083c`。

按 README 从头运行 4090 分配的 23 组场景，输入相机 0/3/5、目标相机 1/2/4，共 69 个目标视点。
包含 AnySplat 单窗口、多窗口（前馈和 TTO 25/50/100 步）、cnw_cnn_pix、cnw_f5_pix 与纯光流对照。
pixgs 不做 TTO；其 FoundationStereo 位移由仓库提供。AnySplat/立体位移和各方案的计时含义以汇总和 meta.json 为准。

## 结果与检查

- [汇总](summary_all.md)、[运行日志](run.log)、[完整性记录](completion_check.json)。
- 23 组结果验证全部 PASS；69 张主对比图齐全，pixgs 均使用 gsplat GPU 渲染。
- 22 项单元测试通过；正式运行 3795.69 秒。
- 各场景包含配置、耗时、poses、logs、完整 eval、prepare/tokens 元数据，以及 GS 各阶段/窗口的 JSON 元数据。
- 验证警告数量：4，具体见各场景 validation.json 和 completion_check.json。

## 比较范围

cnw_cnn 及其 pixgs 变体的有效泛化结论应以汇总中的“第七轮试点场景合计”为准：本机分配的试点为 changjing/shot_0000、changjing1/shot_0001、changjing1/shot_0022。
其余场景参与过检测 CNN 训练。rife/cnw_f5 不依赖此 CNN，可查看全部场景合计。Oracle 使用真值失败区，仅作诊断上限。

## 环境与输入

只覆盖输出路径为 work/dataset6_round15_pixgs，实验参数保持标签默认值；完整配置见 [base_config.yaml](base_config.yaml)。
GPU、依赖版本、源码提交、模型权重及输入文件哈希见 [environment_and_inputs.json](environment_and_inputs.json) 和 environment/。
沿用此前经用户授权生成的半像素矩阵：H_halfpx[i] = T(-0.5,-0.5) @ H_existing[i]，裁剪起点 (192.5,104.5)。
两份矩阵在 calibration/，生成记录在 environment/halfpx-generation.json。

不包含原始数据、模型权重和 aligned/flow/gs 大图；这些完整输出保留在主机。
本分支仅发布 linux-4090 的 23 组场景。
