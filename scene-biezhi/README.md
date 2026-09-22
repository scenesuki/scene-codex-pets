# 稀音·别枝 Codex Pet

以《明日方舟》干员“稀音”的 EPOQUE 时装“别枝”和基建小人比例为参考制作的 Codex v2 动画宠物。

![动作总览](preview/contact-sheet.png)

## 安装

将本目录的 `pet.json` 和 `spritesheet.webp` 一起复制到：

```text
~/.codex/pets/scene-biezhi/
```

重新打开 Codex 后，宠物名称显示为“稀音·别枝”。

## 文件结构

```text
.
├── pet.json
├── spritesheet.webp
├── validation.json
├── preview/
│   ├── contact-sheet.png
│   └── look-directions.png
└── source/
    ├── decoded/
    ├── frames/
    ├── final/
    ├── prompts/
    ├── qa/
    ├── references/
    ├── imagegen-jobs.json
    ├── pet_request.json
    └── progress.md
```

## 技术规格

- Codex `spriteVersionNumber: 2`
- 图集尺寸：`1536 × 2288`
- 单格尺寸：`192 × 208`
- 布局：8 列 × 11 行
- 9 组标准动作
- 16 个顺时针注视方向
- WebP RGBA 透明背景

最终图集通过 v2 结构验证、透明通道检查、三份隔离方向盲测、逐方向语义复核和独立视觉 QA。

## 参考与声明

角色设计、《明日方舟》及相关素材的权利归上海鹰角网络科技有限公司及其关联方所有。本项目是非官方同人制作，不代表或隶属于官方。由于内容包含第三方角色的衍生图像，本目录不附带开源许可证；上传、公开和再分发前，请自行确认适用平台规则及权利要求。
