# 密集视点计时（linux-4090，NVIDIA GeForce RTX 4090，渲染 gsplat，token f4rq，对应 data/disp_fs/{shot}，背景平面 data/bgplane/{room}）

每对相邻输入相机之间 N 个虚拟视点（in035 共 2 对）；6 组场景的中位数。全部在 GPU 上；token（R4 F4R-q，3 台相机约 28 ms / 帧）和对应关系（FoundationStereo，Windows RTX 3090 导出，单列）不在本表计时内。

## N = 30 / 对（共 60 个虚拟视点）

RIFE：逐个视点 fp32 0.90 s → 批量（4）fp16 **0.89 s**；对应关系（立体，Windows 导出）0.80 s

| 方法 | 建立 (s) | 联合优化 (s) | 渲染 (ms/视点) | 贴回 (ms/视点) | 合计含批量 RIFE (s) |
|---|---:|---:|---:|---:|---:|
| pix3n | 0.025 | 0.000 | 1.50 | 0.39 | 1.03 |
| pix3_s50 | 0.024 | 0.849 | 1.51 | 0.39 | 1.88 |
| pix3_s100 | 0.024 | 1.643 | 1.50 | 0.38 | 2.67 |

逐场景数据见 bench_dense_linux-4090.json。
