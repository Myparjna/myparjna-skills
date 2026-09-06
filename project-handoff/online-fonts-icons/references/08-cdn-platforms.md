# CDN 平台总览

## 四大 CDN 来源

### 1. jsDelivr

- **URL 格式**: `cdn.jsdelivr.net/npm/...`
- **官网**: https://www.jsdelivr.com/
- **说明**: 全球加速 npm 包 CDN，稳定性高，国内访问良好
- **覆盖字体**: ~5 款（阿里巴巴普惠体系列等）
- **适用**: 所有通过 npm 发布的包
- **状态**: ✅ 稳定

### 2. chinese-fonts-cdn（中文网字计划）

- **URL 格式**: `chinese-fonts-cdn.deno.dev`
- **官网**: https://chinese-font.netlify.app/zh-cn/
- **说明**: 基于 Deno Deploy 的中文字体专用 CDN，封装 @fontsource 包
- **覆盖字体**: ~18 款
- **状态**: ❌ **已废弃** — 2024年底开始返回 403 Forbidden，重定向到 `cn-font.claude-code-best.win` 也被拒绝

### 3. cn-fontsource

- **URL 格式**: `cdn.jsdelivr.net/npm/cn-fontsource-xxx`
- **Gitee**: https://gitee.com/zhfjyq/cn-fontsource
- **说明**: 中文 FontSource 社区 npm 包，通过 jsDelivr 分发
- **覆盖字��**: ~12 款
- **状态**: ✅ 稳定

### 4. ZeoSeven（推荐）

- **URL 格式**: `fontsapi.zeoseven.com/{id}/main/result.css`
- **官网**: https://fonts.zeoseven.com/
- **说明**: 国内中文字体 CDN 服务商，提供 CSS 切片加载
- **覆盖字体**: 31 款
- **状态**: ✅ 稳定（推荐使用）

## 已废弃的字体（无替代 CDN）

以下字体原本使用 chinese-fonts-cdn.deno.dev，目前没有找到可用的替代 CDN：
- 快看世界体 (kksjt)
- 思源屏显臻宋 (sypxzs)
- 寒蝉全圆体 Regular → **已找到 ZeoSeven 替代**（仅 Regular 字重）
- 寒蝉全圆体 Bold → **ZeoSeven 无 Bold 字重，已移除**
- 鲨鱼菲特健康体 (syftjkt)
- 荆南俊俊体 (jnjj)
- 字魂扁桃体 (zhbtt) → **已找到 ZeoSeven 替代**
- 站酷小薇 LOGO 体 (zkxw)
- 上图东观体（粗体）(stdgt) → **已找到 ZeoSeven 替代**
- 目哉像素体 (mzxst)
- Maple Mono CN 系列

## 注意事项

1. **ZeoSeven 地址必须带完整路径**: `/main/result.css`，仅访问数字 ID（如 `/354`）会返回 404
2. **font-display: swap**: 使用 `@font-face` 时建议加上，避免字体加载阻塞渲染
3. **中文字体文件较大**: 通常 2MB+（woff2），首次加载可能较慢。CDN 已做切片/子集化优化
4. **fallback 字体**: 务必设置英文 fallback（如 `sans-serif`、`serif`、`monospace`），在 CDN 不可用时优雅降级
5. **授权协议**: 以上字体大多遵循 OFL-1.1 或类似开源协议，允许免费商用。商用前建议确认具体授权
6. **避免 chinese-fonts-cdn**: 该 CDN 已废弃，所有使用该源的字体都需要更换为 ZeoSeven 或从列表中移除