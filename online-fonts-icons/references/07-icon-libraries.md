# 图标库 CDN 集成指南（5 套）

---

## 1. Tabler Icons — 4500+ 线性 SVG 图标

**特点**: 纯线性风格、无需 JS、SVG 天然支持任意颜色/渐变
**官网**: https://tabler.io/icons
**GitHub**: https://github.com/tabler/tabler-icons

### 方式 A：`<img>` 标签直接引用（最简单，零依赖）

```html
<img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/home.svg" width="24" height="24" alt="首页">
<img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/search.svg" width="24" height="24" alt="搜索">
<img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/heart.svg" width="24" height="24" alt="收藏">
```

URL 格式：`https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/{图标名}.svg`
图标名全小写，用连字符连接。

### 方式 B：fetch 动态加载 + 自定义颜色

```html
<div id="my-icon" style="display:inline-block;width:24px;height:24px;"></div>
<script>
const res = await fetch('https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/heart.svg');
let svg = await res.text();
svg = svg.replace(/stroke="(?!none)[^"]*"/g, 'stroke="#ef4444"');
svg = svg.replace(/<svg/, '<svg width="24" height="24"');
document.getElementById('my-icon').innerHTML = svg;
</script>
```

### 方式 C：`<img>` + CSS filter 着色

```html
<img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/star.svg"
     style="filter:brightness(0) saturate(100%) invert(65%) sepia(95%) saturate(800%) hue-rotate(10deg);width:24px;">
<!-- 常用 filter 值：
     红色: invert(30%) sepia(98%) saturate(2000%) hue-rotate(330deg)
     金色: invert(65%) sepia(95%) saturate(800%) hue-rotate(10deg)
     绿色: invert(50%) sepia(90%) saturate(500%) hue-rotate(130deg)
     蓝色: invert(70%) sepia(95%) saturate(600%) hue-rotate(190deg)
-->
```

### 方式 D：fetch + 渐变 stroke

```html
<svg width="0" height="0" style="position:absolute;">
  <defs>
    <linearGradient id="my-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f093fb"/>
      <stop offset="100%" stop-color="#667eea"/>
    </linearGradient>
  </defs>
</svg>
<script>
const res = await fetch('https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/sparkles.svg');
let svg = await res.text();
svg = svg.replace(/stroke="[^"]*"/g, 'stroke="url(#my-gradient)"');
svg = svg.replace(/<svg/, '<svg width="24" height="24"');
document.getElementById('my-icon').innerHTML = svg;
</script>
```

---

## 2. Lucide Icons — 1200+ Feather 分支图标

**特点**: Feather Icons 的官方续作，默认线性描边，支持一键切换为面性填充
**官网**: https://lucide.dev/icons/
**GitHub**: https://github.com/lucide-icons/lucide

### 引入 + 使用

```html
<!-- Step 1: 引入 JS -->
<script src="https://cdn.jsdelivr.net/npm/lucide@latest/dist/umd/lucide.js"></script>

<!-- Step 2: 使用图标 -->
<i data-lucide="home"></i>
<i data-lucide="user"></i>
<i data-lucide="settings"></i>

<!-- 面性模式（加 fill 即可） -->
<i data-lucide="home" style="color:#f093fb;fill:currentColor;"></i>

<!-- Step 3: 页面加载后初始化（必须！） -->
<script>lucide.createIcons();</script>
```

### 样式控制

```css
i[data-lucide] { color: #667eea; width: 24px; height: 24px; stroke-width: 2; }
i[data-lucide].filled { fill: currentColor; }
```

---

## 3. Font Awesome — 2000+ 最流行图标库

**特点**: 生态最大，品牌图标最丰富（GitHub、微信、支付宝等）
**官网**: https://fontawesome.com/icons
**GitHub**: https://github.com/FortAwesome/Font-Awesome

### 引入 + 使用

```html
<!-- Step 1: 引入 CSS + JS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@latest/css/all.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@latest/js/all.min.js"></script>

<!-- Step 2: 使用 -->
<!-- Solid（实心面性） -->
<i class="fa-solid fa-house" style="color:#667eea;font-size:24px;"></i>
<i class="fa-solid fa-heart" style="color:red;"></i>

<!-- Regular（线性描边） -->
<i class="fa-regular fa-heart"></i>
<i class="fa-regular fa-star"></i>

<!-- Brands（品牌 logo） -->
<i class="fa-brands fa-github"></i>
<i class="fa-brands fa-weixin"></i>
<i class="fa-brands fa-alipay"></i>
```

---

## 4. Bootstrap Icons — ~1500 开源图标

**特点**: Bootstrap 官方出品，每款图标都有 Linear 和 Filled 两种变体
**官网**: https://icons.getbootstrap.com/
**GitHub**: https://github.com/twbs/icons

### 方式 A：fetch 动态加载（推荐，按需加载）

```html
<span data-b-icon="house-fill" style="display:inline-block;width:24px;height:24px;"></span>
<span data-b-icon="person" style="display:inline-block;width:24px;height:24px;"></span>

<script>
document.querySelectorAll('[data-b-icon]').forEach(async el => {
    const iconName = el.dataset.bIcon;
    const url = `https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/icons/${iconName}.svg`;
    try {
        const res = await fetch(url);
        if (res.ok) {
            el.innerHTML = await res.text();
            const svg = el.querySelector('svg');
            if (svg) { svg.setAttribute('width','24'); svg.setAttribute('height','24'); svg.style.color = '#667eea'; }
        }
    } catch(e) { el.innerHTML = '✗'; }
});
</script>
```

### 方式 B：一次性引入全部图标 CSS

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/font/bootstrap-icons.css">
<i class="bi bi-house-door-fill"></i>
<i class="bi bi-person"></i>
<i class="bi bi-gear-fill"></i>
```

---

## 5. Heroicons — 300+ Tailwind 出品

**特点**: Tailwind CSS 团队设计，风格圆润现代，分 outline 和 solid 两套
**官网**: https://heroicons.com/
**GitHub**: https://github.com/tailwindlabs/heroicons

### fetch API 动态加载

```html
<i data-heroicon="home" data-style="outline" style="display:inline-block;"></i>
<i data-heroicon="home" data-style="solid" style="display:inline-block;"></i>
<i data-heroicon="user" data-style="outline" style="display:inline-block;"></i>

<script>
document.querySelectorAll('[data-heroicon]').forEach(async el => {
    const name = el.dataset.heroicon;
    const style = el.dataset.style || 'outline';
    const url = `https://cdn.jsdelivr.net/npm/heroicons@2/24/${style}/${name}.svg`;
    try {
        const res = await fetch(url);
        if (res.ok) {
            el.innerHTML = await res.text();
            const svg = el.querySelector('svg');
            if (svg) { svg.setAttribute('width','24'); svg.setAttribute('height','24'); svg.style.color = style==='solid'?'#f093fb':'#667eea'; }
        }
    } catch(e) { el.innerHTML = '✗'; }
});
</script>
```

---

## 选型建议

| 需求 | 推荐 |
|------|------|
| 彩色/渐变图标 | Tabler Icons（唯一原生 SVG 支持渐变） |
| 品牌 Logo（GitHub/微信等） | Font Awesome |
| 通用后台管理系统 | Lucide（轻量、风格统一） |
| Bootstrap 项目 | Bootstrap Icons |
| Tailwind 项目 | Heroicons |
| 最小化依赖 | Tabler Icons（零 JS/CSS，直接 `<img>`） |
