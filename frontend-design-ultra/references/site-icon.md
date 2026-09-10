# 站点图标 favicon

新建完整网页或站点时检查 favicon 与页面 title；只交付局部组件时不修改宿主页元数据。

1. 优先复用已有品牌图标，保留项目的图标与框架元数据约定。
2. 没有品牌素材时，直接生成一个本地 SVG：方形 viewBox、简单业务符号、项目强调色与清楚对比。可从 `online-fonts-icons` 推荐图标库选择已核实授权的图形，保留必要许可；也可用简单几何图形组合。无需调用图片生成服务。
3. 图形应在16px和32px仍可识别。不用完整产品名、复杂细线、emoji、外部字体或远程图片；字母方案转成路径，避免字体缺失。不要给所有产品复制同一个图标。
4. 放到框架静态资源目录，例如 `public/favicon.svg`，通过框架元数据或 `<link rel="icon" type="image/svg+xml" href="…">` 引用。地址遵守实际部署基础路径，嵌套部署不盲用根路径。
5. 只允许单文件 HTML 时，可把完整 SVG 用 `encodeURIComponent` 编码后嵌入 `data:image/svg+xml,` 链接；检查 CSP 是否允许，禁止粘贴含未编码 `#` 的 data URL。常规项目优先本地文件。
6. 目标浏览器需要时从同一图形导出 PNG/ICO；主屏幕安装图标按实际需求单独配置，不把 SVG favicon 当作所有平台的安装图标。

例如，检索工具可用以下简单图形作为起点，颜色按项目改写。这是候选图形，不是全站通用品牌模板：

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="#176B59"/>
  <circle cx="13" cy="13" r="6" fill="none" stroke="white" stroke-width="3"/>
  <path d="M18 18L25 25" stroke="white" stroke-width="3" stroke-linecap="round"/>
</svg>
```

交付前检查资源实际返回图像而非404或HTML回退、浏览器标签图标可见、浅深浏览器标签背景均可识别，以及刷新后无旧图标缓存干扰。校验目标页面 title 可区分多个项目。不把配置了 link 当成已经验证显示。

参考：[MDN rel="icon"](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#icon)。
