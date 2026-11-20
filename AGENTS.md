# AGENTS.md · 稀音 Codex 桌宠合集

本仓库维护六套稀音 Codex 桌面宠物。`scene`、`scene-biezhi`、`scene-new-terrain` 是插画版，同名加 `-official` 后缀的是官方素材版。以宠物 ID 确认造型和版本。局部修改以当前图集为基准，先记录要改的槽位和应保留的特征。

## 1. 定位成品和制作记录

- 每套顶层使用 `README.md`、`NOTICE.md`、`pet.json`、`spritesheet.webp` 和 `validation.json`。保持目录名与 `pet.json.id` 一致。
- 正式预览在 `preview/`。用当前图集待机首帧生成 `idle.png`，总览和逐格图分别使用 `animation-overview.gif` 和 `contact-sheet.png`。悬停对应 `jumping.gif`，有无损动图时可优先展示 `jumping.webp`。
- 改插画版时查 `source/pet_request.json` 及 `source/qa/` 的对应记录。追溯素材时查 `source/references/`、`source/decoded/` 和 `source/prompts/`。改视线时查本套 `source/final/spritesheet-extended.json`，原版姿态约束另见 `scene/source/qa/look-mechanics.md`。
- 改官方素材版时查 `source/frame-map.json` 和 `source/generated/`。共用的基建原始素材和预览在 `reference-assets/`。16 个视线槽复用中性姿态。

## 2. 制作与局部修订

1. 保留原图集和受影响状态的预览作为对照。以本套待机和相邻动作核对头身比、发色、勾线、衣料阴影、配饰侧别和道具。重绘时先验证候选帧，记录实际采用的输入、提示词和修订范围。
2. 用一致的等比缩放对齐躯干或脚底基线。左右走路按屏幕方向检查脸、视线、鞋尖和换脚，按角色自身左右检查非对称衣装和持物。保留小步行走的节奏。按本套说明区分等待、工作和复核，基建的 `Interact` 用于工作。
3. `jumping` 槽位在本合集用于悬停回应，保持双脚落地、轻轻抬眼并复位。视线修订先核对上、右、下、左四个基准方向，再看相邻方向是否顺滑，尤其是 `157.5° → 180°` 和 `337.5° → 0°` 两处接缝。
4. 优先复用 `scripts/` 内适合本次动作的 Python/Pillow 脚本。先看参数和写入路径，`--skill-scripts` 指向实际包含对应导入和校验脚本的辅助目录。有输出目录参数时先生成候选。运行会原地覆盖成品的 `scripts/update_hover.py` 时，将副本作为项目参数。

## 3. 图集与验收

图集为 Codex v2 无损 RGBA WebP，尺寸 1536 × 2288，8 列 × 11 行，每格 192 × 208。保持现有行序及帧时长。下表按零起始行号排列，空槽保持全透明。

| 行 | 状态 | 使用槽位数 |
| --- | --- | --- |
| 0 | `idle`，第 7 格用于中性视线 | 7 |
| 1–2 | `running-right`、`running-left` | 各 8 |
| 3 | `waving` | 4 |
| 4 | `jumping` | 5 |
| 5 | `failed` | 8 |
| 6–8 | `waiting`、`running`、`review` | 各 6 |
| 9–10 | 从屏幕正上方起，顺时针每格 22.5° | 各 8 |

- 重新解码导出的 WebP，核对尺寸、Alpha、槽位、裁切和底色残留，更新该套 `validation.json`。局部修改逐格比较修改前后的 RGBA 像素，确认范围外的槽位一致。
- 从最终图集重生成受影响的公开预览和对应验收图。按实际展示大小检查循环、首尾衔接和状态切换。GIF 可能合并连续相同的帧，分别核对图集槽位与预览总时长。
- 审查记录写明造型、状态、帧号或角度及可见证据。交付时给出成品和预览路径，分别列明实际完成的结构检查、视觉检查和客户端实测，标记未核实项。

## 4. 打包、安装与发布

- 打包时生成 `scene-codex-pets-<version>.zip`，按用户指定的发布范围收录各套以宠物 ID 命名的目录、安装文件、公开预览、说明和图集校验记录。对照根目录 `README.md` 的安装说明，解包核对路径和文件字节，并生成 `SHA256SUMS.txt`。`release-assets/` 用于本地发布产物，已被 Git 忽略。
- 安装、更新账户云端图集和切换当前宠物均按用户授权执行。替换前按 ID 核对目标并保留旧版，替换后回读验证。核对当前使用的版本来自本地还是账户云端。
- 仅在用户明确要求对应操作时，才向 GitHub 推送代码或上传文件、创建或发布 Release。用户只要求本地修改、验证或打包时，在本地交付。执行已授权的发布操作前，核对目标仓库、版本和发布脚本的实际副作用，并按 `NOTICE.md` 核实素材权利和平台要求。
