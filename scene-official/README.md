# 稀音（官方素材版）

[返回项目总览](../README.md)

采用 PRTS「稀音 → 默认 → 基建」的游戏小人素材，保留原始待机、移动和交互动作，并补足其余桌宠状态。桌宠 ID 为 `scene-official`，可与插画版 `scene` 同时安装。

[九种状态动图](preview/animation-overview.gif) · [招手](preview/waving.webp) · [悬停](preview/jumping.webp) · [等待](preview/waiting.webp) · [失败](preview/failed.webp) · [复核](preview/review.webp) · [逐格检查图](preview/contact-sheet.png) · [结构校验](validation.json)

| 桌宠状态 | 取用素材 |
| --- | --- |
| 待机 | `Relax` 闲置 |
| 左右移动 | `Move` 原朝向与翻转朝向 |
| 招手 | 从站姿抬手，向外摆掌，回到站姿 |
| 悬停 | 半合眼、抬眼、回到站姿，保留原站姿的身体和脚底 |
| 失败 | 双脚站定，闭眼时头和肩一起轻微下沉，再恢复原站姿 |
| 等待 | 双脚站定，向右略微侧头观察，再回正 |
| 工作 | `Interact` 的完整交互节奏 |
| 复核 | 相机保持胸前，低头检查、拨动相机，再抬眼 |
| 视线 | `Default` 中性姿态填充 16 个方向槽 |

16 个方向显示同一姿态，鼠标移动时视线保持固定。

本地安装时，将 `scene-official` 目录中的 `pet.json` 和 `spritesheet.webp` 放到 `~/.codex/pets/scene-official/`，再打开 Codex 选择「稀音（官方素材版）」。图集结构和逐格画面已检查，客户端触发待实测。

《明日方舟》角色与原始动画素材权利归原权利人所有。本套为非官方桌宠适配。 [素材来源](https://prts.wiki/w/Scene#干员模型) · [权利声明](NOTICE.md)
