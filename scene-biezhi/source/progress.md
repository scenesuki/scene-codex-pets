# 稀音·别枝 pet 制作进度

- [x] 准备时装参考与外观设定
- [x] 制作主形象
- [x] 制作标准动作与视线方向
- [x] 检查动画并打包安装

参考：

- https://wiki.biligame.com/arknights/别枝-稀音
- https://prts.wiki/w/稀音/spine

本项目为 AI 绘制的基建小人风格适配，不直接导出或复用游戏 Spine 帧。

## 2026-10-10：悬停动作调整

按用户要求，将第 5 行 jumping 替换为双脚落地的安静眨眼与轻微点头。保留原生五帧及时长，其余十行像素完全相同。生成提示词、合成脚本和本轮校验见 source/prompts/rows/hover-calm.md、仓库 scripts/update_hover.py 和 source/qa/hover-calm/。
