---
name: online-fonts-icons
description: "用户提到 中文字体、网页字体、在线字体、图标库、CDN 字体、图标颜色 时必须使用本技能。提供 45 款中文字体与 5 套图标库的 CDN 引入代码、字体声明与配色建议。"
---

# Online Fonts & Icons Skill

CDN-based Chinese font and icon library integration guide. Availability is URL-, time- and network-specific; a successful HTTP response is not proof of a usable font. License terms must be checked per font and version; this guide does not certify all fonts as free for commercial use.

核验依据（2026-09-10 全量复核）：只读用户 `C:/Users/mypra/Desktop/VibeCoding指南/免费资源合集/免费字体预览/app.js` 中的全部 45 款字体配置（family、cdn、cdnType），逐款核验 CSS 与字体文件。**45/45 全部可用**：CSS 返回 200，字体文件返回 200 且魔数校验通过（woff2/wOFF 等），各款 `@font-face` 声明的 font-family 与清单一致。核验明细见 `new-frontend-design/TempFiles/0910-字体全量核验/results.json`。

**ZeoSeven（fontsapi.zeoseven.com）反爬提醒**：用脚本裸请求（无浏览器 User-Agent）会得到 HTTP 204 空响应，这不代表字体失效。判活必须带浏览器请求头（User-Agent + Accept），或直接在浏览器/页面中验证；不得凭脚本 204 断定字体停用。

## When to Use

- User needs Chinese web fonts for HTML pages, dashboards, presentations
- User asks about icon libraries (Tabler, Lucide, Font Awesome, Bootstrap Icons, Heroicons)
- User wants font style guidance by category
- User asks about **icon color selection** based on background colors
- User needs copy-paste CDN code for fonts or icons

## ⚠️ Critical Design Principles

### Font Usage Rule: Decorative Fonts Are Only For Headlines

| Use Case | Recommended Font Type | Anti-Pattern |
|----------|----------------------|-------------|
| Body text / paragraphs / lists | System default OR body fonts (Category ①) | ❌ NEVER use decorative fonts here |
| Table content / form labels | System sans-serif | ❌ No round/calligraphy fonts |
| Code / logs / terminal output | Mono/tech fonts (Category ⑥) | ❌ No non-monospace fonts |
| Page H1 title / brand logo / poster headline | ✅ Headline/Art/Song fonts (②③④⑤) | THIS is their purpose |
| Card titles / section headings | ✅ Light decorative fonts OK | Keep to 1-2 levels max |
| Button text / nav items | System default is fine | ❌ Don't over-decorate globally |

### Icon Color Selection Logic (MUST follow this)

**Core rule**: Choose icon colors using measured contrast against adjacent colors, plus semantics and interaction states. Background lightness alone is insufficient; colored backgrounds do not automatically require white icons.

**Case A — Dark Background → White Icon, only if measured contrast passes**
```html
<img src="icon.svg" style="filter:brightness(0) invert(1);">
```
Use on: colored buttons, logo containers, active toolbar states, dark panels.

**Case B — Light/White Background → Deep Theme-Colored Icon**
Use CSS filter with hue-rotate:
```html
<!-- Blue -->
filter:brightness(0)saturate(100%)invert(70%)sepia(95%)saturate(600%)hue-rotate(190deg)
<!-- Green → hue-rotate(130deg), Red → hue-rotate(330deg), Gold → hue-rotate(10deg) -->
```
Use on: quick-action cards, stat cards, list items, light toolbars, empty states.

**Design rules:**
1. Contrast first: WCAG AA requires essential non-text icons/controls ≥ 3:1 against adjacent colors; normal text ≥ 4.5:1; large text ≥ 3:1 (18pt or 14pt bold). Decorative icons/inactive controls are exceptions. Measure final colors including alpha/filter/gradient; see `references/07-icon-libraries.md`.
2. Color semantics: red=error, green=success, yellow=warning, blue=info
3. Max 3 icon colors per page — don't over-color
4. Neutral areas use gray icons — data-dense zones shouldn't compete for attention
5. Interactive feedback: deepen color or add glow on hover

## Font Categories & Quick Reference

### ① Body Fonts (正文无衬线, 2 fonts) — FOR BODY TEXT ONLY
| Font | font-family | CDN | Best For |
|------|-------------|-----|---------|
| 阿里巴巴普惠体 3 Medium | `AlibabaPuHuiTi-3-Medium` | jsDelivr woff2 | Site-wide base font |
| HarmonyOS Sans SC | `HarmonyOS Sans SC` | jsDelivr CSS | Fallback / system-like |

→ Full code: `references/01-body-fonts.md`

### ② Headline Heiti (标题黑体, 14 fonts) — HEADLINES/TITLES ONLY
**Top picks by scenario:**
- **后台系统/科技产品标题** → `DingTalk JinBuTi`（钉钉进步体）
- **企业官网/正式报告** → `Aidian FengYaHei`（爱点风雅黑）
- **品牌LOGO/国风海报** → `WSQuanXing`（万事全兴体）
- **年轻化/社交产品** → `DouyinSans`（抖音美好体 Bold）⭐
- **创意社区/开源项目** → `Smiley Sans Oblique`（得意黑）
- **活动/音乐/潮流** → `摇醒青年黑1.0`
- **高端文化/禅意标题** → `Kingnamype Yuanmo SC`（荆南缘默体）
- **科技品牌/概念标题** → `Unbounded Sans`（无界黑）、`NanoByongGyeHei`（纳米扁界黑）⭐
- **产品标签/短标题** → `JinzisheBianzheng`（金字社扁正体）⭐
- **社交/生活方式** → `JinzisheZhenhao`（金字社真好体）⭐
- **自然有机风格** → `寒蝉有机体` ⭐
- **文化/艺术海报** → `Monu YueDong`（典迹悦动）⭐、`ZT YueDongHei`（卓特悦动黑）⭐

→ Full code: `references/02-headline-heiti.md`

### ③ Song/Kai/Calligraphy (宋体楷体书法, 9 fonts) — CULTURAL/ARTISTIC TITLES
Top picks: `LXGW WenKai GB Screen`（霞鹜文楷, 可做正文）, `STDongGuanTi`（上图东观体）

→ Full code: `references/03-song-kai-calligraphy.md`

### ④ Round/Cute/Handwrite (圆体可爱手写, 14 fonts) — CUTE/UI/KIDS APPS
Top picks: `寒蝉半圆体`（通用UI首选）, `JiangChengYuanTi`（江城圆体，不出错通用型）, `975Maru SC Medium`（日系）, `荆南波波黑`（社区/儿童/活动）, `Kingnammm Maiyuan 2`（荆南麦圆体，生活方式）

→ Full code: `references/04-round-cute-handwrite.md`

### ⑤ Art/Special (艺术特殊, 4 fonts) — LOGO/POSTER ONLY, USE SPARINGLY
`zcoolwenyiti`（站酷文艺体）, `LXGW Marker Gothic`（霞鹜漫黑）, `WD-XL Lubrifont SC`（WD-XL 滑油字）, `JiangChengJieXingTi`（江城解星体）

→ Full code: `references/05-art-special.md`

### ⑥ Mono/Pixel/Tech (等宽像素科技, 2 fonts) — CODE/LOGS/DATA TABLES
**First choice:** `点点像素体-方形`（复古像素游戏风格）
Also: `x12y16pxMaruMonica`（莫妮卡像素圆体）

→ Full code: `references/06-mono-pixel-tech.md`

## Icon Libraries (5 sets)

| Library | Count | Best For | Integration | Official |
|---------|-------|----------|------------|----------|
| **Tabler Icons** ⭐推荐 | 4500+ | Zero-dependency, color/gradient | `<img>` tag only, no JS/CSS needed | https://tabler.io/icons |
| Lucide Icons | 1200+ | General admin UI | JS init required | https://lucide.dev/icons/ |
| Font Awesome | 2000+ | Brand logos, quick dev | CSS + class names | https://fontawesome.com/icons |
| Bootstrap Icons | ~1500 | Bootstrap projects | CSS or fetch | https://icons.getbootstrap.com/ |
| Heroicons | 300+ | Tailwind projects | fetch dynamic load | https://heroicons.com/ |

→ Full integration + filter color codes: `references/07-icon-libraries.md`

## CDN Platforms

以下平台数量和状态为旧版记录，未在本次全量复核；具体地址以本页带日期的抽样及目标环境测试为准，“稳定”不构成持续可用保证。

| Platform | URL Pattern | Fonts | Historical status |
|----------|-------------|-------|--------|
| jsDelivr | `cdn.jsdelivr.net/npm/...` | ~5 | ✅ Stable |
| ZeoSeven | `fontsapi.zeoseven.com/{id}/main/result.css` | 31 | ✅ Stable (Recommended) |
| chinese-fonts-cdn | `chinese-fonts-cdn.deno.dev` | ~18 | ❌ DEPRECATED (403 Forbidden) |
| cn-fontsource | `cdn.jsdelivr.net/npm/cn-fontsource-xxx` | ~12 | ✅ Stable |

→ Details: `references/08-cdn-platforms.md`

## ⚠️ IMPORTANT: Deprecated Fonts

以下为旧版未收录或曾未找到 CDN 的历史记录，不代表现时没有可用源。遇到用户近期实测 URL，应优先核对，不直接否定或删除该字体：
- 快看世界体 (kksjt) — No CDN found
- 思源屏显臻宋 — No CDN found
- 鲨鱼菲特健康体 — No CDN found
- 荆南俊俊体 — No CDN found
- 站酷小薇 LOGO 体 — No CDN found
- 目哉像素体 — No CDN found
- 寒蝉全圆体 Bold — ZeoSeven 只提供 Regular 字重，无 Bold 切片
- Maple Mono CN (Thin/Regular/Bold) — Not a pixel font, use for code only
- 字魂扁桃体 (zihunbiantaoti) — 有 ZeoSeven 源（405），但 2026-09-10 未收录于最新实测清单，用前先实测

## ⚠️ CRITICAL: font-family 命名陷阱（实测得出）

**font-family 名必须以 CDN CSS 里 `@font-face` 实际声明的为准，不能凭字体中文名猜。**

常见陷阱（已全部实测修正）：
| 字体中文名 | ❌ 错误 family | ✅ 正确 family（CSS 实测） |
|-----------|---------------|-------------------------|
| 抖音美好体 Bold | `Douyin Sans` | `DouyinSans`（无空格） |
| 爱点风雅黑 | `爱点风雅黑` | `Aidian FengYaHei` |
| 摇醒青年黑 | `摇醒青年黑` | `摇醒青年黑1.0`（带版本后缀） |
| 阿里妈妈东方大楷 | `MaShanZheng` | `Alimama DongFangDaKai` |
| 极影毁片辉宋 | `极影毁片辉宋` | `极影毁片辉宋 Bold` |
| 香萃端庄宋体 | `香萃端庄宋体` | `XCDUANZHUANGSONG` |
| 寒蝉活宋体 | `寒蝉活宋体` | `ChillHuoSong_F` |
| 猫啃网风雅宋 | `猫啃网风雅宋` | `MaoKenWangFengYaSong` |
| 荆南缘默体 | `荆南缘默体` | `Kingnamype Yuanmo SC` |
| 江西拙楷 | `江西拙楷` | `jiangxizhuokai` |
| 女书梧桐 | `女书梧桐` | `Nyushu Firmia` |
| 江城圆体 | `江城圆体` | `JiangChengYuanTi` |
| 莫妮卡像素圆体 | `X12Y16PX Maru Monica` | `x12y16pxMaruMonica` |
| 猫啃珠圆体 | `Maoken Zhuyuan Ti` | `MaokenZhuyuanTi` |
| 悠哉字体 | `Yozai` | `Yozai Medium` |
| 站酷文艺体 | `站酷文艺体` | `zcoolwenyiti` |
| 点点像素体-方形 | `点点像素 方` | `点点像素体-方形` |
| 无界黑 | `无界黑` | `Unbounded Sans` |
| 金字社扁正体 | `金字社扁正体` | `JinzisheBianzheng` |
| 金字社真好体 | `金字社真好体` | `JinzisheZhenhao` |
| 纳米扁界黑 | `纳米扁界黑` | `NanoByongGyeHei` |
| 典迹悦动 | `典迹悦动` | `Monu YueDong` |
| 卓特悦动黑 | `卓特悦动黑` | `ZT YueDongHei` |
| 写意体 | `写意体` | `YShi-Written` |
| 荆南麦圆体 | `荆南麦圆体` | `Kingnammm Maiyuan 2` |
| WD-XL 滑油字 | `WD-XL 滑油字` | `WD-XL Lubrifont SC` |
| 江城解星体 | `江城解星体` | `JiangChengJieXingTi` |

**验证方法**：浏览器 DevTools → Network → 加载 CSS → 查看 `@font-face { font-family: "..." }`，或用 `document.fonts.load('20px "family名"', '实际目标文字')` 检查返回的 FontFace 数组非空且各项 status 为 loaded，再在 DevTools 的 Rendered Fonts 检查实际文字使用的字体。仅 Promise 成功或 `document.fonts.check()` 为 true 不足以证明目标字体已生效。**family 名写错时，CSS 即使 200 也会静默回退到系统字体，肉眼看不出但字体没生效。**

## Workflow

1. Identify user's need: font category or icon library
2. Check usage context — if it's body text, recommend Category ①; if it's a title/logo, recommend appropriate decorative font
3. Load the corresponding reference file from `references/`
4. Provide copy-paste code (`<link>` or `@font-face`)
5. Include `font-family` CSS with fallback
6. For icons: determine background color → apply correct coloring method (white vs filter)
7. Remind about `font-display: swap` and fallback fonts

## Important Notes

- 商用前逐款核对作者/发行方的具体授权与字体版本；CDN 可下载、项目名含“免费”、或其他字体采用 OFL 均不构成本字体授权证明。
- Chinese fonts are 2MB+ woff2; CDN uses subsetting optimization
- Always set English fallback: `sans-serif`, `serif`, `monospace`
- ZeoSeven URLs must include `/main/result.css` suffix
- Tabler Icons is recommended as default icon choice (zero dependency)
- DEPRECATED 是历史源状态标记，不等于字体本身不可用；有近期实测源时按具体 URL 重新核验。
