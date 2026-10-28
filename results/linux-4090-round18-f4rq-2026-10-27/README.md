# linux-4090 round18 F4R-q

源码标签 [linux-4090-round18-f4rq](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-4090-round18-f4rq)，提交 `80a09871a3d7a6bd815e24ddffa0421e8ef7970b`。

按本轮默认参数运行 4090 分配的六组：changjing 0000/0003，changjing1 0001/0007/0013/0022。输入 0/3/5，目标 1/2/4，共 18 个目标视点。
只覆盖 work_root 为原 work/dataset6_round15_pixgs；复用 aligned、flow、cnw_cnn pix3 与 AnySplat TTO100 基线。重跑 tokens，再运行 pixgs/evaluate/validate，之后执行密集视点计时。

## 全部完成后的统一统计

- [实验汇总](summary_all.md)：F4R-q pix3、背景平面 pix3bg、门控、同次优化的 25/50 步快照与 100 步对比，含 fg、失败区及按可见性拆开的失败区，直接与 oracle 贴回。
- 6 组验证全部 PASS，18 张主对比图齐全，每组 5 个 F4R-q 输出变体使用 gsplat。26 项测试通过。
- 实验 282.03 秒，密集计时 32.86 秒。验证警告 0 条，详见 [完整性记录](completion_check.json)。
- [运行日志](dataset6_r18.log)、[计时日志](bench_dense.log)、[计时汇总](bench_dense_linux-4090.md)、[计时数据](bench_dense_linux-4090.json)。
- 计时按默认全部六组、每对 30 个（共 60 个）虚拟视点，比较 0/50/100 步优化，以及 RIFE 逐视点 fp32 和 batch=4 fp16。GPU 计时前无其他计算进程；记录见 environment/benchmark_*。
- 总计时包含批量 RIFE、建立、优化、渲染和贴回；token 检测引用既有 R4 报告，对应关系 Windows 导出时间单列，均不在本次 GPU 合计内。

## 基线与复现

本次场景 timing.json 仅记录 tokens/pixgs/evaluate/validate。cnw_cnn pix3 与 AnySplat 未重算，252 份复用 GS JSON 均与 [round17 发布结果](https://github.com/hhan70701/local-gs-eval-results/tree/experiment/linux-4090-round17-pix3-2026-10-27/results/linux-4090-round17-pix3-2026-10-27) 的哈希一致。
旧 eval、tokens、日志、配置、计时已本地归档；本轮 eval 从空目录生成。
完整配置见 [base_config.yaml](base_config.yaml)，源码提交、输入哈希及基线环境见 [environment_and_inputs.json](environment_and_inputs.json) 和 environment/。
F4R-q 掩码来自仓库提供的五折交叉验证导出，使用未在各场景上训练的折；cnw_cnn 泛化结论仅看三组试点（changjing 0000，changjing1 0001/0022）。Oracle 只作诊断。
沿用用户授权的半像素矩阵 H_halfpx[i] = T(-0.5,-0.5) @ H_existing[i]，矩阵与生成记录见 calibration/ 及 environment/halfpx-generation.json。
完整输出保留在主机；上传评估、日志、配置、GS JSON 和计时报告，不含数据集、模型权重或 GS 渲染大图。只发布 4090 六组结果。
