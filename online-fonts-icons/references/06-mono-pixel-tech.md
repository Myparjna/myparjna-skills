# ⑥ Mono / Pixel / Tech / 等宽像素科技风格（2 款）

适合代码编辑器、终端界面、游戏 UI、复古终端风格等场景。

---

## 点点像素体-方形

- **font-family**: `点点像素体-方形` （⚠️ 注意：原 skill 误写为点点像素 方）
- **风格**: 标准像素风格字体，复古游戏感，方块颗粒均匀
- **来源**: ZeoSeven
- **原址**: https://fonts.zeoseven.com/items/110/

### CDN

```html
<link rel="stylesheet" href="https://fontsapi.zeoseven.com/110/main/result.css">
```

```css
.pixel { font-family: '点点像素体-方形', monospace; }
```

---

## 莫妮卡像素圆体

- **font-family**: `x12y16pxMaruMonica` （⚠️ 实测：CSS 实际声明为连写无空格，不是 X12Y16PX Maru Monica）
- **风格**: 像素风格+圆角结合，8-bit 复古感但笔画圆润
- **来源**: cn-fontsource (jsDelivr)
- **原址**: https://fonts.zeoseven.com/

### CDN

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/cn-fontsource-x-12-y-16-px-maru-monica-regular/font.css">
```

```css
.retro { font-family: 'x12y16pxMaruMonica', monospace; }
```

---

## 已移除（Not Pixel Fonts / No CDN）

### Maple Mono CN 系列 (Thin / Regular / Bold)

- **⚠️ 注意**: 这不是像素字体！是等宽代码字体 (Monospace Code Font)
- 适合代码编辑器、终端、日志展示
- 原 CDN 已失效
- 如需代码字体，推荐使用系统内置 monospace 或 Nerd Font 方案
- 已从像素分类中移除

### 目哉像素体

- 原 CDN 已失效
- 暂未找到可替代 WebFont CDN
- 已从 skill 中移除