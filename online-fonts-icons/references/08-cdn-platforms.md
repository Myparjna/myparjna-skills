# CDN 平台总览

## 四大 CDN 来源

### 1. jsDelivr

- **URL 格式**: `cdn.jsdelivr.net/npm/...`
- **官网**: https://www.jsdelivr.com/
- **说明**: 全球加速 npm 包 CDN，稳定性高，国内访问良好
- **覆盖字体**: ~5 款（阿里巴巴普惠体系列等）
- **适用**: 所有通过 npm 发布的包

### 2. chinese-fonts-cdn（中文网字计划）

- **URL 格式**: `chinese-fonts-cdn.deno.dev`
- **官网**: https://chinese-font.netlify.app/zh-cn/
- **说明**: 基于 Deno Deploy 的中文字体专用 CDN，封装 @fontsource 包
- **覆盖字体**: ~18 款
- **适用**: 大量中文开源字体

### 3. cn-fontsource

- **URL 格式**: `cdn.jsdelivr.net/npm/cn-fontsource-xxx`
- **Gitee**: https://gitee.com/zhfjyq/cn-fontsource
- **说明**: 中文 FontSource 社区 npm 包，通过 jsDelivr 分发
- **覆盖字体**: ~12 款
- **适用**: 中文字体 npm 包

### 4. ZeoSeven

- **URL 格式**: `fontsapi.zeoseven.com/{id}/main/result.css`
- **官网**: https://fonts.zeoseven.com/
- **说明**: 国内中文字体 CDN 服务商，提供 CSS 切片加载
- **覆盖字体**: 31 款
- **适用**: 最丰富的中文字体 CDN

## 注意事项

1. **ZeoSeven 地址必须带完整路径**: `/main/result.css`，仅访问数字 ID（如 `/354`）会返回 404
2. **font-display: swap**: 使用 `@font-face` 时建议加上，避免字体加载阻塞渲染
3. **中文字体文件较大**: 通常 2MB+（woff2），首次加载可能较慢。CDN 已做切片/子集化优化
4. **fallback 字体**: 务必设置英文 fallback（如 `sans-serif`、`serif`、`monospace`），在 CDN 不可用时优雅降级
5. **授权协议**: 以上字体大多遵循 OFL-1.1 或类似开源协议，允许免费商用。商用前建议确认具体授权
