<p align="center">
  <a href="#宠物展示"><img src="scene/source/frames/idle/00.png" alt="稀音原版服装" width="112"></a>
  <a href="#宠物展示"><img src="scene-biezhi/source/frames/idle/00.png" alt="稀音·别枝" width="112"></a>
  <a href="#宠物展示"><img src="scene-new-terrain/source/frames/idle/00.png" alt="稀音·新地形" width="112"></a>
</p>

<h1 align="center">scene-codex-pets</h1>

<p align="center">《明日方舟》稀音的 Codex 桌面宠物合集</p>

收录原版、别枝和新地形三套造型。每套提供 9 种状态动画和 16 个注视方向，可单独安装，也可同时放入宠物列表。

**[下载 v1.2.4 完整合集](https://github.com/scenesuki/scene-codex-pets/releases/download/v1.2.4/scene-codex-pets-v1.2.4.zip)** · [SHA-256 校验](https://github.com/scenesuki/scene-codex-pets/releases/download/v1.2.4/SHA256SUMS.txt) · [更新记录](https://github.com/scenesuki/scene-codex-pets/releases) · [提交 Issue](https://github.com/scenesuki/scene-codex-pets/issues/new)

**下载范围**：v1.2.4 将三套稀音桌宠合为一个 ZIP，内附安装文件、动画预览与图集校验记录。解压后可按需选装。

[浏览造型](#宠物展示) · [安装方法](#三步安装) · [版本记录](#版本与历史下载)

## 宠物展示

点击小图查看造型说明。全动作预览用九宫格同时播放九种状态，16 个注视方向见各套视线检查图。

| 原版服装 | 别枝 | 新地形 |
| :---: | :---: | :---: |
| <a href="scene/README.md"><img src="scene/source/frames/idle/00.png" alt="稀音原版服装" width="144"></a> | <a href="scene-biezhi/README.md"><img src="scene-biezhi/source/frames/idle/00.png" alt="稀音·别枝" width="144"></a> | <a href="scene-new-terrain/README.md"><img src="scene-new-terrain/source/frames/idle/00.png" alt="稀音·新地形" width="144"></a> |
| **服饰要素**：浅色外套、深浅不对称的腿部搭配、相机和橄榄绿腰包 | **服饰要素**：红裙、浅色花纹袖摆、花形发饰和折叠伞 | **服饰要素**：棕色帽子、橄榄绿披肩、胸前相机和棕色短靴 |
| **画风**：Q 版日系插画 | **画风**：Q 版日系插画 | **画风**：Q 版日系插画 |
| **参考造型**：《明日方舟》稀音原版服装 | **参考造型**：EPOQUE 时装「别枝」 | **参考造型**：生命之地时装「新地形」 |
| **[全动作预览](scene/preview/animation-overview.gif)** | **[全动作预览](scene-biezhi/preview/animation-overview.gif)** | **[全动作预览](scene-new-terrain/preview/animation-overview.gif)** |
| [造型说明](scene/README.md) · [悬停](scene/preview/hover-calm.gif) · [走路](scene/source/qa/previews/running-right.gif) · [视线](scene/preview/look-directions.png) | [造型说明](scene-biezhi/README.md) · [悬停](scene-biezhi/preview/hover-calm.gif) · [走路](scene-biezhi/source/qa/previews/running-right.gif) · [视线](scene-biezhi/preview/look-directions.png) | [造型说明](scene-new-terrain/README.md) · [悬停](scene-new-terrain/preview/hover-calm.gif) · [走路](scene-new-terrain/source/qa/previews/running-right.gif) · [视线](scene-new-terrain/preview/look-directions.png) |

## 三步安装

1. 打开 [v1.2.4 下载页](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.2.4)，下载完整合集 ZIP。可使用同版 `SHA256SUMS.txt` 核对下载内容。
2. 解压并将想安装的宠物目录复制到 `~/.codex/pets/`。确认目录内直接包含 `pet.json` 与 `spritesheet.webp`。Windows 默认位置为 `%USERPROFILE%\.codex\pets\`。
3. 重新打开 Codex，在宠物设置中选择「稀音」「稀音·别枝」或「稀音·新地形」。

| 显示名称 | 安装目录 |
| --- | --- |
| 稀音 | `~/.codex/pets/scene/` |
| 稀音·别枝 | `~/.codex/pets/scene-biezhi/` |
| 稀音·新地形 | `~/.codex/pets/scene-new-terrain/` |

> **更新提示**：如果原有宠物已迁移到 Codex 账户云端，仅覆盖本地文件不会更新正在使用的云端图集。更新账户中对应的宠物图集后，再刷新或重新打开 Codex。

<details>
<summary>规格与验证范围</summary>

- 每套采用 Codex v2 无损透明 WebP 图集。图集为 1536 × 2288 像素，由 8 列 × 11 行、每格 192 × 208 像素组成。
- [原版校验](scene/validation.json)、[别枝校验](scene-biezhi/validation.json)、[新地形校验](scene-new-terrain/validation.json) 记录图集结构检查结果。各造型目录也保留动作预览、视线检查和制作素材。
- 图集提供 16 个注视方向。客户端如何触发和显示视线跟随，取决于应用版本与运行状态。文件和预览检查不等同于客户端实测。

</details>

<a name="版本与历史下载"></a>

<details>
<summary>版本与历史下载</summary>

| 版本 | 更新内容 |
| --- | --- |
| [v1.2.4](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.2.4) | 稀音原版、别枝、新地形三套完整合集，附动画预览、安装说明和图集校验记录。 |
| [v1.0.1](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.0.1) | 将悬停时的跳跃改成双脚落地的轻微回应。 |
| [v1.0.0](https://github.com/scenesuki/scene-codex-pets/releases/tag/v1.0.0) | 首次发布三套稀音桌宠。 |

历史安装包以对应 Release 的附件为准。

</details>

<details>
<summary>项目结构</summary>

每套造型有独立目录，顶层的 `spritesheet.webp` 和 `validation.json` 是正式图集与结构校验结果。`preview/` 提供公开预览，`source/` 保留制作素材、布局元数据和验收记录。`scripts/` 存放图集整理脚本。

```text
scene/              稀音原版
scene-biezhi/       稀音·别枝
scene-new-terrain/  稀音·新地形
```

</details>

---

本项目是《明日方舟》的非官方同人作品。角色及参考素材的权利归原权利人所有，详见 [NOTICE.md](NOTICE.md)。
