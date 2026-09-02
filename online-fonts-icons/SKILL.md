---
name: online-fonts-icons
description: "用户提到 中文字体、网页字体、在线字体、图标库、CDN 字体、图标颜色 时必须使用本技能。提供 35 款中文字体与 5 套图标库的 CDN 引入代码、字体声明与配色建议。"
---

# Online Fonts & Icons Skill

CDN-based Chinese font and icon library integration guide. All resources verified, free-to-use (mostly OFL-1.1), loadable via CDN without local files.

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

**Core rule**: Icon color depends entirely on background lightness.

**Case A — Colored/Dark Background → White Icon**
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
1. Contrast first: WCAG AA ≥ 4.5:1 ratio required
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

### ② Headline Heiti (标题黑体, 6 fonts) — HEADLINES/TITLES ONLY
**Top picks by scenario:**
- **后台系统/科技产品标题** → `DingTalk JinBuTi`（钉钉进步体）
- **企业官网/正式报告** → `Aidian FengYaHei`（爱点风雅黑）
- **品牌LOGO/国风海报** → `WSQuanXing`（万事全兴体）
- **年轻化/社交产品** → `DouyinSans`（抖音美好体 Bold）
- **创意社区/开源项目** → `Smiley Sans Oblique`（得意黑）
- **活动/音乐/潮流** → `摇醒青年黑1.0`

→ Full code: `references/02-headline-heiti.md`

### ③ Song/Kai/Calligraphy (宋体楷体书法, 10 fonts) — CULTURAL/ARTISTIC TITLES
Top picks: `LXGW WenKai GB Screen`（霞鹜文楷, 可做正文）, `STDongGuanTi`（上图东观体）

→ Full code: `references/03-song-kai-calligraphy.md`

### ④ Round/Cute/Handwrite (圆体可爱手写, 13 fonts) — CUTE/UI/KIDS APPS
Top picks: `寒蝉半圆体`（通用UI首选）, `JiangChengYuanTi`（江城圆体，不出错通用型）, `975Maru SC Medium`（日系）

→ Full code: `references/04-round-cute-handwrite.md`

### ⑤ Art/Special (艺术特殊, 2 fonts) — LOGO/POSTER ONLY, USE SPARINGLY
`zcoolwenyiti`（站酷文艺体）, `zihunbiantaoti`（字魂扁桃体）

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

| Platform | URL Pattern | Fonts | Status |
|----------|-------------|-------|--------|
| jsDelivr | `cdn.jsdelivr.net/npm/...` | ~5 | ✅ Stable |
| ZeoSeven | `fontsapi.zeoseven.com/{id}/main/result.css` | 31 | ✅ Stable (Recommended) |
| chinese-fonts-cdn | `chinese-fonts-cdn.deno.dev` | ~18 | ❌ DEPRECATED (403 Forbidden) |
| cn-fontsource | `cdn.jsdelivr.net/npm/cn-fontsource-xxx` | ~12 | ✅ Stable |

→ Details: `references/08-cdn-platforms.md`

## ⚠️ IMPORTANT: Deprecated Fonts

The following fonts have **NO working CDN** and are excluded from this skill:
- 快看世界体 (kksjt) — No CDN found
- 思源屏显臻宋 — No CDN found
- 鲨鱼菲特健康体 — No CDN found
- 荆南俊俊体 — No CDN found
- 站酷小薇 LOGO 体 — No CDN found
- 目哉像素体 — No CDN found
- 寒蝉全圆体 Bold — ZeoSeven 只提供 Regular 字重，无 Bold 切片
- Maple Mono CN (Thin/Regular/Bold) — Not a pixel font, use for code only

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

**验证方法**：浏览器 DevTools → Network → 加载 CSS → 查看 `@font-face { font-family: "..." }`，或用 `document.fonts.load('20px "family名"')` 检查是否真能加载到 FontFace。**family 名写错时，CSS 即使 200 也会静默回退到系统字体，肉眼看不出但字体没生效。**

## Workflow

1. Identify user's need: font category or icon library
2. Check usage context — if it's body text, recommend Category ①; if it's a title/logo, recommend appropriate decorative font
3. Load the corresponding reference file from `references/`
4. Provide copy-paste code (`<link>` or `@font-face`)
5. Include `font-family` CSS with fallback
6. For icons: determine background color → apply correct coloring method (white vs filter)
7. Remind about `font-display: swap` and fallback fonts

## Important Notes

- Free commercial use (OFL-1.1), verify before production
- Chinese fonts are 2MB+ woff2; CDN uses subsetting optimization
- Always set English fallback: `sans-serif`, `serif`, `monospace`
- ZeoSeven URLs must include `/main/result.css` suffix
- Tabler Icons is recommended as default icon choice (zero dependency)
- Avoid fonts marked as DEPRECATED — they have no working CDN
