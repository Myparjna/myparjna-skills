---
name: online-fonts-icons
description: This skill should be used when the user needs to integrate online Chinese fonts or icon libraries into web projects via CDN. It provides ready-to-use CDN URLs, font-family declarations, and HTML/CSS code snippets for 46 curated Chinese fonts (6 categories) and 5 icon libraries. Includes font usage principles (decorative fonts ONLY for headlines/titles, NOT for body text) and icon color selection logic (white icons on colored backgrounds, deep theme-colored icons on light backgrounds). Trigger when: user mentions fonts, Chinese web fonts, icon libraries, CDN fonts, Google Fonts alternatives for Chinese, typography guidance for web pages/dashboards/presentations, or needs to choose icon colors that match background colors.
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
| HarmonyOS Sans SC | `HarmonySans SC` | jsDelivr CSS | Fallback / system-like |

→ Full code: `references/01-body-fonts.md`

### ② Headline Heiti (标题黑体, 7 fonts) — HEADLINES/TITLES ONLY
**Top picks by scenario:**
- **后台系统/科技产品标题** → `DingTalk JinBuTi`（钉钉进步体）
- **企业官网/正式报告** → `爱点风雅黑`
- **品牌LOGO/国风海报** → `WSQuanXing`（万事全兴体）
- **新闻媒体/运动品牌** → `快看世界体`
- **年轻化/社交产品** → `Douyin Sans`（抖音美好体 Bold）
- **创意社区/开源项目** → `Smiley Sans Oblique`（得意黑）
- **活动/音乐/潮流** → `摇醒青年黑`

→ Full code: `references/02-headline-heiti.md`

### ③ Song/Kai/Calligraphy (宋体楷体书法, 11 fonts) — CULTURAL/ARTISTIC TITLES
Top picks: `LXGW WenKai GB Screen`（霞鹜文楷, 可做正文）, `Source Han Serif CN`（思源屏显臻宋）

→ Full code: `references/03-song-kai-calligraphy.md`

### ④ Round/Cute/Handwrite (圆体可爱手写, 15 fonts) — CUTE/UI/KIDS APPS
Top picks: `寒蝉半圆体`（通用UI首选）, `江城圆体`（不出错通用型）, `975 Maru Sc Medium`（日系）

→ Full code: `references/04-round-cute-handwrite.md`

### ⑤ Art/Special (艺术特殊, 4 fonts) — LOGO/POSTER ONLY, USE SPARINGLY
`xiaowei`（站酷小薇）, `站酷文艺体`, `JUNJUN`, `zihunbiantaoti`

→ Full code: `references/05-art-special.md`

### ⑥ Mono/Pixel/Tech (等宽像素科技, 5 fonts) — CODE/LOGS/DATA TABLES
**First choice:** `Maple Mono CN` Regular（日志/代码/数据表格）
Also: Thin（轻量展示）, Bold（高亮关键词）, 像素字体（游戏/复古装饰）

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

| Platform | URL Pattern | Fonts | Speed (CN) |
|----------|-------------|-------|-----------|
| jsDelivr | `cdn.jsdelivr.net/npm/...` | ~5 | ⭐⭐⭐ Fast |
| chinese-fonts-cdn | `chinese-fonts-cdn.deno.dev` | ~18 | ⭐⭐ Good |
| cn-fontsource | `cdn.jsdelivr.net/npm/cn-fontsource-xxx` | ~12 | ⭐⭐ Good |
| ZeoSeven | `fontsapi.zeoseven.com/{id}/main/result.css` | 31 | ⭐⭐⭐ Fast |

→ Details: `references/08-cdn-platforms.md`

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
