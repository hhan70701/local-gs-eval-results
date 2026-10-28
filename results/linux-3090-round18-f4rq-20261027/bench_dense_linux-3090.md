# 密集视点计时（linux-3090，NVIDIA GeForce RTX 3090，渲染 gsplat，token f4rq，对应 data/disp_fs/{shot}，背景平面 data/bgplane/{room}）

每对相邻输入相机之间 N 个虚拟视点（in035 共 2 对）；6 组场景的中位数。全部在 GPU 上；token（R4 F4R-q，3 台相机约 28 ms / 帧）和对应关系（FoundationStereo，Windows RTX 3090 导出，单列）不在本表计时内。

## N = 30 / 对（共 60 个虚拟视点）

RIFE：逐个视点 fp32 1.62 s → 批量（4）fp16 **1.32 s**；对应关系（立体，Windows 导出）0.81 s

| 方法 | 建立 (s) | 联合优化 (s) | 渲染 (ms/视点) | 贴回 (ms/视点) | 合计含批量 RIFE (s) |
|---|---:|---:|---:|---:|---:|
| pix3n | 0.042 | 0.000 | 3.44 | 0.88 | 1.62 |
| pix3_s50 | 0.042 | 2.058 | 3.56 | 0.89 | 3.68 |
| pix3_s100 | 0.042 | 4.115 | 3.53 | 0.89 | 5.74 |

逐场景数据见 bench_dense_linux-3090.json。
