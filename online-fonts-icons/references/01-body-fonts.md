# ① Body Fonts / 正文字体（2 款）

适合长文阅读、界面正文、数据展示等需要高易读性的场景。

---

## 阿里巴巴普惠体 3 — Medium

- **font-family**: `AlibabaPuHuiTi-3-Medium`
- **来源**: 阿里巴巴官方出品
- **官网**: https://fonts.alibabagroup.com/
- **iconfont**: https://www.iconfont.cn/fonts/detail?cnid=adI1E7HF7yme

### CDN 引入

```html
<style>
@font-face {
    font-family: 'AlibabaPuHuiTi-3-Medium';
    src: url('https://cdn.jsdelivr.net/npm/alibabapuhuiti-3-65-medium@1.0.0/AlibabaPuHuiTi-3-65-Medium.woff2') format('woff2');
    font-weight: 500;
    font-display: swap;
}
</style>
```

### 使用

```css
body { font-family: 'AlibabaPuHuiTi-3-Medium', sans-serif; }
```

---

## HarmonyOS Sans SC

- **font-family**: `HarmonySans SC`
- **来源**: 华为 HarmonyOS 系统字体
- **官网**: https://developer.huawei.com/consumer/cn/design/resource/

### CDN 引入

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@ayahub/webfont-harmony-sans-sc@1.0.0/css/index.min.css">
```

### 使用

```css
body { font-family: 'HarmonySans SC', sans-serif; }
```
