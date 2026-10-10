# 稀音 pet 制作记录

用户选择：原版服装，贴近游戏基建小人。

- [x] 准备角色参考与外观设定
- [x] 制作主形象
- [x] 制作动作与视线方向
- [x] 检查动画并打包

参考：
- https://wiki.biligame.com/arknights/%E7%A8%80%E9%9F%B3 （原版角色图已取得）
- https://prts.wiki/w/%E7%A8%80%E9%9F%B3/spine （基建模型索引已确认；本地访问 TLS 失败，尚未取得渲染帧）

本轮为 AI 绘制的基建小人风格适配，不是从原游戏 Spine 动画直接导出的帧。
绘图：imagegen 内置工具。
保留左右不对称特征；不镜像右跑生成左跑。
暂不加入独立摄影车，以保持单个 pet 的紧凑轮廓。


## 2026-10-10：悬停动作调整

按用户要求，将第 5 行 jumping 替换为双脚落地的安静眨眼与轻微点头。保留原生五帧及时长，其余十行像素完全相同。生成提示词、合成脚本和本轮校验见 source/prompts/rows/hover-calm.md、仓库 scripts/update_hover.py 和 source/qa/hover-calm/。
