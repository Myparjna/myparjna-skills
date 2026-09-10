# 字体与图标按需选用

资源入口优先为用户的 `online-fonts-icons` 技能。下列路径均相对该技能目录，使用时先定位当前安装版本；不把本机绝对路径写入生成的页面。这里维护选用方法，CDN 代码与字体声明读取来源文件，避免复制整份库造成版本分叉。

**中文字体默认策略：正文用系统字体栈，不下载网页字体。** 一份中文 woff2 字重约 5MB，正文全量引入会拖慢首屏并挤占同期网络请求（实测冷加载案例：四档中文字体加若干大图，整页 load 事件被推到 18 秒）。只有当标题、主视觉、品牌位等少量文字确需设计感，或用户明确要求指定字体时，才经 CDN 引入，且只作用于这些元素。

正文系统栈（直接复制使用，无需任何资源请求）：

```css
font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "HarmonyOS Sans SC",
             "Microsoft YaHei", "Noto Sans SC", "Source Han Sans SC", sans-serif;
```

**需要设计感字体时的自包含候选**（该技能不可用时直接取用，不猜包名、不逐个试 URL；候选尝试不超过 2 个地址即回退系统栈，并记录最终生效方案）——只声明页面上真正用到的那 1–2 档：

```css
/* 标题/品牌位：阿里巴巴普惠体 3（jsDelivr，多字重同族声明，已验证 2026-09）*/
@font-face{font-family:'AlibabaPuHuiTi-3';src:url('https://cdn.jsdelivr.net/npm/alibabapuhuiti-3-55-regular@1.0.0/AlibabaPuHuiTi-3-55-Regular.woff2') format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'AlibabaPuHuiTi-3';src:url('https://cdn.jsdelivr.net/npm/alibabapuhuiti-3-65-medium@1.0.0/AlibabaPuHuiTi-3-65-Medium.woff2') format('woff2');font-weight:500;font-display:swap}
@font-face{font-family:'AlibabaPuHuiTi-3';src:url('https://cdn.jsdelivr.net/npm/alibabapuhuiti-3-85-bold@1.0.0/AlibabaPuHuiTi-3-85-Bold.woff2') format('woff2');font-weight:700;font-display:swap}
```

- **同族多字重声明**：一个家族名（如 `AlibabaPuHuiTi-3`）下按 `font-weight: 400 / 500 / 700` 分别声明文件，页面直接用 `font-weight` 取值；不把字重写进家族名（如 `AlibabaPuHuiTi-3-Medium`），那会让其它字重落到别处。
- **只用已声明的字重**：页面里写 `font-weight:600` 却只声明了 500，浏览器会拿 Medium 合成粗体，效果是过粗、发虚、边缘发糊，属于常见显丑来源。需要更粗时补声明对应文件（普惠体 3：`75-semibold`→600、`85-bold`→700），或把用到的字重收在已声明范围内。标题优先级通常 500 已足够，不默认拉满 700。
- 每个字重 woff2 约 5MB：默认不引；确需引入时只声明实际用到的档位，正文元素不继承这个家族，不能让整页文本都去等字体下载。
- 中文标题需要单独家族时：钉钉进步体等从 `references/02-headline-heiti.md` 候选中取；无明确需要时标题沿用正文家族（系统栈）。
- 数字与代码用 JetBrains Mono 等已验证等宽字体或 `tabular-nums`；西文数字体积小，可按需引入，也可直接用系统等宽栈。
- 图标：Tabler / Lucide / Iconify 任选一套主库，经 CDN 加载使用；不从本地取图标文件，不手写、不手绘、不凭几何印象拼 SVG 图形，不把别处看到的 path 手工抄进页面，也不用 `<symbol>`+`<use>` 自建精灵图。用下面两种加载式方案之一（2026-09 实测可达）：
  1. **Tabler 图标字体**（最省事，推荐）：引入 `https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.31.0/dist/tabler-icons.min.css`，用 `<i class="ti ti-search" aria-hidden="true"></i>`；`ti-` 后的名称即 Tabler 官方图标名。
  2. **Lucide 运行时**：引入 `https://unpkg.com/lucide@0.462.0/dist/umd/lucide.min.js`，写 `<i data-lucide="search" aria-hidden="true"></i>`，脚本末尾调用 `lucide.createIcons()`；动态插入 DOM 后需再次调用。
  只有确实需要零运行时依赖、且项目明确要求时，才改用 Iconify 官方接口（`https://api.iconify.design/tabler.json?icons=...`）取原样 body，同样是把库的产出原样使用，不是自己画；此路仅在项目提出该要求时启用。
- 图标名逐项核对：`https://api.iconify.design/tabler.json?icons=<名称>` 返回该名称即存在，返回空 `icons` 就换名。
- 以上均不可达时回退系统字体栈与文字标签（图标位保留文字或语义缩写），并在交付说明中标注。

授权核对、锁版本、字形验证等下方规则不变。

| 需要 | 实际读取的参考文件 | 选用原则 |
|---|---|---|
| 中文正文、表单、表格 | 无需读取 | 默认系统字体栈完成，不下载网页字体 |
| 标题、主视觉、品牌位等少量需设计感的文字 | `references/01-body-fonts.md`、`references/02-headline-heiti.md` | 按业务选阿里巴巴普惠体3或钉钉进步体、爱点风雅黑、得意黑等候选；只声明实际用到的 1–2 档字重，只作用于这些元素，可先读 `references/01-body-fonts.md` 确认候选；不因收录而默认使用斜体或装饰体 |
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
- 只引入本页需要的字体家族与字重。多读资源用于选对资源，不等于全部加载到网页。中文正文默认系统栈，零请求；确需引入中文字体时，先评估该字体文件体积是否值得为首屏等待（单档约 5MB），并限定作用元素。
- 页面中同时存在的所有外部资源互相争抢带宽：中文字体、大图、地图瓦片、脚本会一起排队。控制同期总字节数，首屏不引非必要资源，比事后调超时更有效。
