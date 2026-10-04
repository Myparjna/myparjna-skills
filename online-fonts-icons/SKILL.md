---
name: online-fonts-icons
description: "用户提到 中文字体、网页字体、在线字体、图标库、CDN 字体、图标颜色 时使用本技能。提供 45 款中文字体与 5 套图标库的 CDN 引入代码、字体声明与配色建议。"
---

# 在线中文字体与图标库

## 字体使用原则

装饰字体仅用于标题。

| 场景 | 推荐字体 |
|------|----------|
| 正文、列表、表格、表单 | 系统默认或 ① 正文字体 |
| 代码、日志、终端 | ⑥ 等宽字体 |
| 页面 H1、品牌 LOGO、海报标题 | ②③④⑤ 装饰字体 |
| 卡片标题、分区标题 | 轻装饰字体，最多 1–2 级 |
| 按钮、导航 | 系统默认 |

## 字体分类索引

| 分类 | 数量 | 首选 | 参考文件 |
|------|------|------|----------|
| ① 正文无衬线 | 2 | `AlibabaPuHuiTi-3-Medium`、`HarmonyOS Sans SC` | `references/01-body-fonts.md` |
| ② 标题黑体 | 14 | 后台 `DingTalk JinBuTi`，官网 `Aidian FengYaHei`，年轻化 `DouyinSans`，创意 `Smiley Sans Oblique` | `references/02-headline-heiti.md` |
| ③ 宋楷书法 | 9 | `LXGW WenKai GB Screen`（可做正文）、`STDongGuanTi` | `references/03-song-kai-calligraphy.md` |
| ④ 圆体手写 | 14 | 通用 UI `寒蝉半圆体`、`JiangChengYuanTi` | `references/04-round-cute-handwrite.md` |
| ⑤ 艺术特殊 | 4 | `zcoolwenyiti`、`LXGW Marker Gothic` | `references/05-art-special.md` |
| ⑥ 等宽像素 | 2 | `点点像素体-方形`、`x12y16pxMaruMonica` | `references/06-mono-pixel-tech.md` |

font-family 必须以 CDN CSS 中 `@font-face` 实际声明的名称为准，写错会静默回退到系统字体。对照表见 `references/09-font-family-names.md`。

## 图标库

| 图标库 | 数量 | 适用 | 引入方式 |
|--------|------|------|----------|
| Tabler Icons（默认） | 4500+ | 零依赖、可着色 | `<img>` 标签 |
| Lucide | 1200+ | 通用后台 | JS 初始化 |
| Font Awesome | 2000+ | 品牌图标 | CSS 类名 |
| Bootstrap Icons | ~1500 | Bootstrap 项目 | CSS 或 fetch |
| Heroicons | 300+ | Tailwind 项目 | fetch 动态加载 |

完整引入代码与滤镜着色见 `references/07-icon-libraries.md`。

## 图标配色规则

1. 以实测对比度选色：必要图标与控件对相邻颜色 ≥ 3:1，正文 ≥ 4.5:1，大字 ≥ 3:1。
2. 深色背景且对比度达标时使用白色图标：`filter:brightness(0) invert(1)`。
3. 浅色背景使用深主题色图标，通过 `hue-rotate` 滤镜调色。
4. 语义色：红为错误，绿为成功，黄为警告，蓝为信息。
5. 单页图标颜色不超过 3 种，数据密集区域使用灰色。
6. 悬停时加深颜色或增加光晕。

## 工作流

1. 判断需求属于字体还是图标，以及使用场景（正文或标题）。
2. 读取对应的 `references/` 文件。
3. 提供 `<link>` 或 `@font-face` 代码，设置 `font-display: swap` 与英文 fallback。
4. 图标先确定背景色，再按配色规则着色。
5. 验证字体：`document.fonts.load('20px "family"', '目标文字')` 返回非空且状态为 loaded，并在 DevTools 的 Rendered Fonts 中确认。

CDN 平台说明见 `references/08-cdn-platforms.md`。
