# 稀音 Codex Pets

本仓库收录三个以《明日方舟》干员“稀音”为原型制作的 Codex v2 动画宠物。三个项目彼此独立，可单独安装，也可同时使用。

## 项目

| 造型 | 显示名称 | 宠物 ID | 项目说明 |
| --- | --- | --- | --- |
| 原版服装 | 稀音 | `scene` | [`scene/`](scene/) |
| EPOQUE 时装“别枝” | 稀音·别枝 | `scene-biezhi` | [`scene-biezhi/`](scene-biezhi/) |
| 生命之地时装“新地形” | 稀音·新地形 | `scene-new-terrain` | [`scene-new-terrain/`](scene-new-terrain/) |

## 安装

1. 进入需要安装的项目目录。
2. 创建与 `pet.json` 中 `id` 相同的宠物目录。
3. 将该项目的 `pet.json` 和 `spritesheet.webp` 一起复制到宠物目录。
4. 重新打开 Codex。

三个项目对应的安装位置为：

```text
~/.codex/pets/scene/
~/.codex/pets/scene-biezhi/
~/.codex/pets/scene-new-terrain/
```

## 兼容性与验证

三个项目均使用 Codex `spriteVersionNumber: 2`，图集尺寸为 `1536 × 2288`，由 `8 × 11` 个 `192 × 208` 单元格组成。最终图集均为带透明通道的 WebP，并已通过各自 `validation.json` 中的结构检查，结果为 `ok: true`，无错误或警告。

每个项目还包含动作预览、视线方向检查图和完整制作工程，详情见对应目录中的 README。

## 仓库结构

```text
.
├── README.md
├── NOTICE.md
├── scene/              # 稀音原版服装
├── scene-biezhi/       # 稀音·别枝时装
└── scene-new-terrain/  # 稀音·新地形时装
```

## 声明

本仓库为非官方同人项目。角色设计、《明日方舟》及相关素材的权利归上海鹰角网络科技有限公司及其关联方所有。详见 [`NOTICE.md`](NOTICE.md)。
