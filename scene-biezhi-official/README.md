# 稀音·别枝（官方素材版）

[返回项目总览](../README.md)

采用 PRTS「稀音 → 别枝 → 基建」的游戏小人素材，保留原始待机、移动和交互动作，并补足其余桌宠状态。桌宠 ID 为 `scene-biezhi-official`，可与插画版 `scene-biezhi` 同时安装。

[九种状态动图](preview/animation-overview.gif) · [招手](preview/waving.webp) · [悬停](preview/jumping.webp) · [等待](preview/waiting.webp) · [失败](preview/failed.webp) · [复核](preview/review.webp) · [逐格检查图](preview/contact-sheet.png)

| 桌宠状态 | 素材或动作 |
| --- | --- |
| 待机 | `Relax` 闲置 |
| 左右移动 | `Move` 原朝向和 PRTS 翻转朝向 |
| 招手 | 保持原伞面、脸和站姿，只用空手招手 |
| 悬停 | 取自 `Relax` 的原始眨眼，双脚站定，闭眼后重新睁开 |
| 失败 | 保持站姿，低头垂肩，停一拍后恢复 |
| 等待 | 双脚站定，短暂张望后回到原站姿 |
| 工作 | `Interact` 交互 |
| 复核 | 保留原伞面，低头查看伞柄，再抬眼 |
| 视线 | 16 个方向复用 `Default` 中性姿态，视线保持固定 |

本地安装时，将 `pet.json` 和 `spritesheet.webp` 放入 `~/.codex/pets/scene-biezhi-official/`，重新打开 Codex，选择「稀音·别枝（官方素材版）」。已检查图集结构和逐格画面，客户端触发待实测。

[结构校验](validation.json)

本套为非官方桌宠适配。《明日方舟》角色和原始动画素材权利归原权利人所有。 [素材来源](https://prts.wiki/w/Scene#干员模型) · [权利声明](NOTICE.md)
