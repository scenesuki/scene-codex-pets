<p align="center">
  <a href="#插画版"><img src="scene/preview/idle.png" alt="稀音（插画版）" width="80"></a>
  <a href="#插画版"><img src="scene-biezhi/preview/idle.png" alt="稀音·别枝（插画版）" width="80"></a>
  <a href="#插画版"><img src="scene-new-terrain/preview/idle.png" alt="稀音·新地形（插画版）" width="80"></a>
  <a href="#官方素材版"><img src="scene-official/preview/idle.png" alt="稀音（官方素材版）" width="80"></a>
  <a href="#官方素材版"><img src="scene-biezhi-official/preview/idle.png" alt="稀音·别枝（官方素材版）" width="80"></a>
  <a href="#官方素材版"><img src="scene-new-terrain-official/preview/idle.png" alt="稀音·新地形（官方素材版）" width="80"></a>
</p>

<h1 align="center">scene-codex-pets</h1>

<p align="center">《明日方舟》稀音的 Codex 桌面宠物合集</p>

收录原版、别枝和新地形三种造型，各有插画版和官方素材版，共六套桌宠。每套提供 9 种状态动画，使用独立宠物 ID，可同时安装到宠物列表。

**[下载 v1.3.0 六套合集](https://github.com/scenesuki/scene-codex-pets/releases/download/v1.3.0/scene-codex-pets-v1.3.0.zip)** · [SHA-256 校验](https://github.com/scenesuki/scene-codex-pets/releases/download/v1.3.0/SHA256SUMS.txt) · [更新记录](https://github.com/scenesuki/scene-codex-pets/releases) · [提交 Issue](https://github.com/scenesuki/scene-codex-pets/issues/new)

**下载范围**　v1.3.0 ZIP 收录三套插画版和三套官方素材版，内附安装文件、动画预览和图集校验记录。解压后可按需选装。

[浏览造型](#宠物展示) · [安装方法](#三步安装) · [版本记录](#版本与历史下载)

## 宠物展示

点击小图查看造型说明。全动作动图用九宫格同时展示九种状态。

### 插画版

以游戏服装和基建小人比例为参考制作的 Q 版插画。每套包含 9 种状态动画和 16 个不同的注视方向。

| 原版 | 别枝 | 新地形 |
| :---: | :---: | :---: |
| <a href="scene/README.md"><img src="scene/preview/idle.png" alt="稀音（插画版）" width="144"></a> | <a href="scene-biezhi/README.md"><img src="scene-biezhi/preview/idle.png" alt="稀音·别枝（插画版）" width="144"></a> | <a href="scene-new-terrain/README.md"><img src="scene-new-terrain/preview/idle.png" alt="稀音·新地形（插画版）" width="144"></a> |
| 浅色外套、相机与橄榄绿腰包 | EPOQUE 时装，红裙、花纹袖摆与折叠伞 | 生命之地时装，棕色帽子、橄榄绿披肩与胸前相机 |
| **[全动作预览](scene/preview/animation-overview.gif)** | **[全动作预览](scene-biezhi/preview/animation-overview.gif)** | **[全动作预览](scene-new-terrain/preview/animation-overview.gif)** |
| [造型说明](scene/README.md) · [悬停](scene/preview/jumping.gif) · [逐格检查](scene/preview/contact-sheet.png) | [造型说明](scene-biezhi/README.md) · [悬停](scene-biezhi/preview/jumping.gif) · [逐格检查](scene-biezhi/preview/contact-sheet.png) | [造型说明](scene-new-terrain/README.md) · [悬停](scene-new-terrain/preview/jumping.gif) · [逐格检查](scene-new-terrain/preview/contact-sheet.png) |



### 官方素材版

以游戏原始基建小人素材为基础的非官方桌宠适配。每套保留待机、移动和交互等原始动作，并补足其余状态，共 9 种状态动画。16 个视线槽复用中性姿态。

| 原版 | 别枝 | 新地形 |
| :---: | :---: | :---: |
| <a href="scene-official/README.md"><img src="scene-official/preview/idle.png" alt="稀音（官方素材版）" width="144"></a> | <a href="scene-biezhi-official/README.md"><img src="scene-biezhi-official/preview/idle.png" alt="稀音·别枝（官方素材版）" width="144"></a> | <a href="scene-new-terrain-official/README.md"><img src="scene-new-terrain-official/preview/idle.png" alt="稀音·新地形（官方素材版）" width="144"></a> |
| 浅色外套、相机与橄榄绿腰包 | EPOQUE 时装，红裙、花纹袖摆与撑开的纸伞 | 生命之地时装，棕色帽子、橄榄绿披肩与手持相机 |
| **[全动作预览](scene-official/preview/animation-overview.gif)** | **[全动作预览](scene-biezhi-official/preview/animation-overview.gif)** | **[全动作预览](scene-new-terrain-official/preview/animation-overview.gif)** |
| [造型说明](scene-official/README.md) · [悬停](scene-official/preview/jumping.webp) · [逐格检查](scene-official/preview/contact-sheet.png) | [造型说明](scene-biezhi-official/README.md) · [悬停](scene-biezhi-official/preview/jumping.webp) · [逐格检查](scene-biezhi-official/preview/contact-sheet.png) | [造型说明](scene-new-terrain-official/README.md) · [悬停](scene-new-terrain-official/preview/jumping.webp) · [逐格检查](scene-new-terrain-official/preview/contact-sheet.png) |

## 三步安装

1. 从 [v1.3.0 下载页](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.3.0) 下载 ZIP，用同版 `SHA256SUMS.txt` 核对后解压。也可直接从本项目选择所需造型目录。
2. 在 `~/.codex/pets/` 下建立与宠物 ID 同名的目录，将所选套装的 `pet.json` 与 `spritesheet.webp` 直接放入其中。Windows 默认位置为 `%USERPROFILE%\.codex\pets\`。
3. 重新打开 Codex，在宠物设置中按下表的显示名称选择。

| 显示名称 | 安装目录 |
| --- | --- |
| 稀音（插画版） | `~/.codex/pets/scene/` |
| 稀音·别枝（插画版） | `~/.codex/pets/scene-biezhi/` |
| 稀音·新地形（插画版） | `~/.codex/pets/scene-new-terrain/` |
| 稀音（官方素材版） | `~/.codex/pets/scene-official/` |
| 稀音·别枝（官方素材版） | `~/.codex/pets/scene-biezhi-official/` |
| 稀音·新地形（官方素材版） | `~/.codex/pets/scene-new-terrain-official/` |

> v1.2.4 ZIP 中的三套宠物沿用发布时的显示名称。
>
> **更新提示**：如果原有宠物已迁移到 Codex 账户云端，仅覆盖本地文件不会更新正在使用的云端图集。更新账户中对应的宠物图集后，再刷新或重新打开 Codex。

<details>
<summary>规格与验证范围</summary>

- 每套采用 Codex v2 无损透明 WebP 图集。图集为 1536 × 2288 像素，由 8 列 × 11 行、每格 192 × 208 像素组成。
- 插画版校验包括[原版](scene/validation.json)、[别枝](scene-biezhi/validation.json)和[新地形](scene-new-terrain/validation.json)。官方素材版校验包括[原版](scene-official/validation.json)、[别枝](scene-biezhi-official/validation.json)和[新地形](scene-new-terrain-official/validation.json)。
- 插画版的 16 向视线触发取决于客户端版本与运行状态。官方素材版的客户端触发仍待实测。

</details>

<a name="版本与历史下载"></a>

<details>
<summary>版本与历史下载</summary>

| 版本 | 更新内容 |
| --- | --- |
| [v1.3.0](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.3.0) | 新增原版、别枝、新地形三套官方素材版，统一六套显示名称、预览和安装说明。 |
| [v1.2.4](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.2.4) | 稀音原版、别枝、新地形三套插画版合集，附动画预览、安装说明和图集校验记录。 |
| [v1.0.1](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.0.1) | 将悬停时的跳跃改成双脚落地的轻微回应。 |
| [v1.0.0](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.0.0) | 首次发布三套稀音桌宠。 |

历史安装包以对应 Release 的附件为准。

</details>

<details>
<summary>项目结构</summary>

每套使用相同入口。`pet.json` 与 `spritesheet.webp` 用于安装，`validation.json` 记录图集检查，`README.md` 与 `NOTICE.md` 说明套装与素材权利。`preview/` 提供待机展示图、动作预览和逐格检查图。官方素材版的原始素材与制作记录保留在本地工作区。

```text
scene/                       原版插画版
scene-biezhi/                别枝插画版
scene-new-terrain/           新地形插画版
scene-official/              原版官方素材版
scene-biezhi-official/        别枝官方素材版
scene-new-terrain-official/   新地形官方素材版
reference-assets/            本地基建原始素材和来源记录
scripts/                     图集整理脚本
release-assets/              本地发布产物
```

</details>

---

本项目是《明日方舟》的非官方同人作品。角色及参考素材的权利归原权利人所有，详见 [NOTICE.md](NOTICE.md)。
