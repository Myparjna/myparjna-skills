# CDN 平台总览

| 平台 | URL 格式 | 官网 | 说明 |
|------|----------|------|------|
| ZeoSeven（推荐） | `fontsapi.zeoseven.com/{id}/main/result.css` | https://fonts.zeoseven.com/ | 中文字体 CSS 切片加载 |
| jsDelivr | `cdn.jsdelivr.net/npm/...` | https://www.jsdelivr.com/ | npm 包 CDN，国内访问良好 |
| cn-fontsource | `cdn.jsdelivr.net/npm/cn-fontsource-xxx` | https://gitee.com/zhfjyq/cn-fontsource | 中文 FontSource 社区包，经 jsDelivr 分发 |

chinese-fonts-cdn（`chinese-fonts-cdn.deno.dev`）已停用，返回 403，请勿使用。

## 注意事项

1. ZeoSeven 地址必须带完整路径 `/main/result.css`，仅访问数字 ID 会返回 404。
2. 脚本请求 ZeoSeven 需携带浏览器 User-Agent 与 Accept 请求头，否则返回 HTTP 204 空响应。
3. `@font-face` 中设置 `font-display: swap`，避免字体加载阻塞渲染。
4. 中文字体通常超过 2MB，CDN 已做切片与子集化。
5. 务必设置英文 fallback，如 `sans-serif`、`serif`、`monospace`。
6. 商用前逐款核对字体授权。
