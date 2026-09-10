# 字体与图标按需选用

资源入口优先为用户的 `online-fonts-icons` 技能。下列路径均相对该技能目录，使用时先定位当前安装版本；不把本机绝对路径写入生成的页面。这里维护选用方法，CDN 代码与字体声明读取来源文件，避免复制整份库造成版本分叉。

**该技能不可用（如隔离环境）时的自包含候选**：直接使用下列已验证地址，不猜包名、不逐个试 URL——字体候选尝试不超过 2 个地址即沿回退链下行，并记录最终生效方案：

```css
/* 中文正文：阿里巴巴普惠体 3 Medium（jsDelivr，已验证 2026-09）*/
@font-face {
  font-family: 'AlibabaPuHuiTi-3-Medium';
  src: url('https://cdn.jsdelivr.net/npm/alibabapuhuiti-3-65-medium@1.0.0/AlibabaPuHuiTi-3-65-Medium.woff2') format('woff2');
  font-weight: 500;
  font-display: swap;
}
```

- 中文标题需要单独家族时：钉钉进步体等从 `references/02-headline-heiti.md` 候选中取；无明确需要时标题沿用正文家族。
- 境外网络环境中文备选：Noto Sans SC（Google Fonts）；数字与代码用 JetBrains Mono 等已验证等宽字体或 `tabular-nums`。
- 图标：Tabler / Lucide / Iconify 任选一套主库，CDN 锁版本。
- 以上均不可达时回退系统字体栈，并在交付说明中标注。

授权核对、锁版本、字形验证等下方规则不变。

| 需要 | 实际读取的参考文件 | 选用原则 |
|---|---|---|
| 中文正文、表单、表格 | `references/01-body-fonts.md` | 优先阿里巴巴普惠体3；HarmonyOS Sans可作替代，最后回退中文系统字体。字重与实际文件一致，Medium文件声明500，不冒充完整字重家族 |
| 中文标题 | `references/02-headline-heiti.md` | 按业务选择钉钉进步体、爱点风雅黑、得意黑等候选；不因收录而默认使用斜体或装饰体，常规工作台标题可沿用正文家族 |
| 文化、圆体、艺术方向 | `references/03-song-kai-calligraphy.md`、`references/04-round-cute-handwrite.md`、`references/05-art-special.md` | 仅相应题材需要时读取；装饰字体不蔓延到表格、正文和控件 |
| 特殊数字/代码字体 | `references/06-mono-pixel-tech.md` | 像素字体不自动适合高密度指标，常规指标优先清楚的数字和tabular-nums |
| 在线图标 | `references/07-icon-libraries.md` | 比较Tabler、Lucide、Font Awesome Free、Bootstrap Icons、Heroicons，选择一套主库 |
| CDN平台与加载方式 | `references/08-cdn-platforms.md` | 按所选资源核对jsDelivr、ZeoSeven等平台的实际地址与加载方式，部署环境逐项验证 |

图标选择：线性工具界面可选Tabler或Lucide；需要品牌标识时按需使用Font Awesome Free的品牌资源；需要实心/轮廓风格时逐个确认Bootstrap Icons或Heroicons的具体变体。已有项目图标库优先，不为换库增加依赖；不同库不用同一页面随机混搭。

CDN落地时：

- 将来源示例作为候选，核实所选包版本、实际文件路径和具体图标名称；不能照搬 `@latest` 或假设每个图标都有实心版本。交付采用已验证的固定版本或项目锁文件。
- 字体CSS里的font-family、字重、相对字体地址以实际响应为准；CDN能访问不等于字体或图标已经显示。字体用目标中文字形检查，图标检查实际SVG或字体字形，避免空白方框。
- 静态原型可用CDN；已有打包工程优先现有依赖和按需组件。单个图标无需整套JS，Font Awesome按实际方式选择字体CSS或SVG方案，不无条件同时加载两套。
- 颜色优先使用组件的currentColor或受控SVG样式；外部img不能直接继承页面currentColor，勿以为设置color就已着色。图标字形为装饰时对读屏隐藏，按钮另有可访问名称。
- 保留资源授权要求；“免费资源合集”不代替具体资源和版本的授权核对。CDN失效时使用已准备的本地图标或保留文字操作入口，不生成死按钮。
- 只引入本页需要的字体家族与字重。多读资源用于选对资源，不等于全部加载到网页。
