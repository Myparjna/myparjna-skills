# 元服务 UX 体验标准

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/ux-standard-overview-0000002019655177
- 抓取时间：2026-04-04T08:25:19.512Z
## 概述（全量检测范围）

元服务和 APP 是 HarmonyOS 生态的“一体两面”，相比较 APP，元服务即开即用、纯净轻量、高效触达特征尤为明显。元服务在体验管控方面强调“一进一出"丝滑流畅无拦截、“一上一下”导航清晰无遮挡，在自动化检测维度上包含通用应用、大屏应用、折叠屏应用、电脑应用 UX 体验标准，全量指标如下：

<table><tbody><tr><td><p>标准类型</p></td><td><p>标准子类型</p></td><td><p>标准编号</p></td><td><p>标准项名称</p></td><td><p>标准项描述</p></td><td><p>是否必须遵守</p></td></tr><tr><td rowspan="41"><p>通用应用 UX 体验标准</p></td><td rowspan="34"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-general-0000001760708152#section11938161416124">基础体验</a></p></td><td><p>2.1.1.1</p></td><td><p>系统返回</p></td><td><p>所有界面响应系统返回操作，全屏界面提供返回/关闭/取消按钮</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.2.1</p></td><td><p>布局基础要求</p></td><td><p>应用支持在不同屏幕尺寸的设备上良好显示</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.2.2</p></td><td><p>挖孔区适配</p></td><td><p>界面布局适配摄像头的挖孔区域</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.2.3</p></td><td><p>元素排布对齐</p></td><td><p>元素排布对齐</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.4</p></td><td><p>文本排版对齐</p></td><td><p>中西文排版对齐</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.5</p></td><td><p>留白率达标</p></td><td><p>留白率</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.6</p></td><td><p>元素图形平衡</p></td><td><p>元素图形平衡</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.7</p></td><td><p>页面视觉平衡</p></td><td><p>页面视觉平衡</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.8</p></td><td><p>深度层级合理</p></td><td><p>卡片/控件背景明度层级</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.9</p></td><td><p>平面层级合理</p></td><td><p>平面层级</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.10</p></td><td><p>分组线索清晰</p></td><td><p>分组线索清晰</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.11</p></td><td><p>同组元素整体</p></td><td><p>同组元素整体</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.12</p></td><td><p>元素排布规律性</p></td><td><p>元素排布规律性</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.2.13</p></td><td><p>页面布局规律性</p></td><td><p>页面布局规律性</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.3.1</p></td><td><p>避免与手势系统冲突</p></td><td><p>应用/元服务自定义手势与系统手势无冲突</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.3.2</p></td><td><p>典型手势时长设计</p></td><td><p>应用/元服务使用的典型手势时长合理</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.3.3</p></td><td><p>点击热区</p></td><td><p>点击热区不得小于 40vp×40vp</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.4.1</p></td><td><p>色彩对比度</p></td><td><p>应用/元服务使用的色彩满足最小对比度要求</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.4.2</p></td><td><p>字体大小</p></td><td><p>应用/元服务的文字大小满足最小字号要求</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.4.3.1</p></td><td><p>应用图标</p></td><td><p>应用图标资源需分层，尺寸需满足规范要求</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.4.3.2</p></td><td><p>界面图标</p></td><td><p>应用/元服务的界面图标大小满足最小尺寸要求</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.4.3.3</p></td><td><p>图标清晰度</p></td><td><p>应用/元服务的图标清晰度</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.5.1.1</p></td><td><p>层级转场</p></td><td><p>层级转场采用左右位移的运动方式</p></td><td><p>强烈推荐</p></td></tr><tr><td><p>2.1.5.1.2</p></td><td><p>搜索转场</p></td><td><p>搜索转场采用共享元素的转场方式</p></td><td><p>强烈推荐</p></td></tr><tr><td><p>2.1.5.1.3</p></td><td><p>新建转场</p></td><td><p>新建转场采用上下位移的运动方式</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.5.1.4</p></td><td><p>编辑转场</p></td><td><p>编辑转场采用淡入淡出的过渡方式</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.5.1.5</p></td><td><p>共享元素转场</p></td><td><p>对于转场前后持续存续的的元素</p></td><td><p>强烈推荐</p></td></tr><tr><td><p>2.1.5.1.6</p></td><td><p>秩序感元素转场</p></td><td><p>对于有明显成组排列的布局，建议进入页面时，成组排列的布局有节奏的使用时间差</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.5.2.1</p></td><td><p>动效无缺失</p></td><td><p>存在转场动效过渡检查</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.5.2.2</p></td><td><p>转场动效时长下限</p></td><td><p>全屏页面的转场动效时长满足要求</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.5.3.1</p></td><td><p>启动页动效时长</p></td><td><p>有内容填充的启动页在全屏状态停留时长不建议超过3s</p></td><td><p>强烈推荐</p></td></tr><tr><td><p>2.1.5.3.2</p></td><td><p>滑动跟手反馈动效一致性</p></td><td><p>滑动跟手反馈动效一致性</p></td><td><p>必须</p></td></tr><tr><td><p>2.1.5.3.3</p></td><td><p>滑动过界反馈动效一致性</p></td><td><p>界面滑动到边界位置存在反馈动效</p></td><td><p>推荐</p></td></tr><tr><td><p>2.1.5.3.4</p></td><td><p>离手减速动效一致性</p></td><td><p>离手减速动效检查</p></td><td><p>必须</p></td></tr><tr><td rowspan="7"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-general-0000001760708152#section15603108141517">系统特性</a></p></td><td><p>2.2.1</p></td><td><p>底部导航条适配</p></td><td><p>界面布局适配底部导航条</p></td><td><p>必须</p></td></tr><tr><td><p>2.2.2</p></td><td><p>通知</p></td><td><p>应用/元服务通知设计需遵循通知规范</p></td><td><p>涉及则必须</p></td></tr><tr><td><p>2.2.3</p></td><td><p>实况窗</p></td><td><p>实况窗通知样式需符合设计规范</p></td><td><p>必须</p></td></tr><tr><td><p>2.2.4.1</p></td><td><p>悬浮窗适配</p></td><td><p>应用支持以悬浮窗模式运行</p></td><td><p>必须</p></td></tr><tr><td><p>2.2.4.2</p></td><td><p>分屏适配</p></td><td><p>应用支持上下分屏和左右分屏</p></td><td><p>必须</p></td></tr><tr><td><p>2.2.5</p></td><td><p>深色模式</p></td><td><p>应用需支持深色模式显示</p></td><td><p>必须</p></td></tr><tr><td><p>2.2.6</p></td><td><p>状态栏</p></td><td><p>应用需要对状态栏进行适配显示</p></td><td><p>必须</p></td></tr><tr><td rowspan="34"><p>大屏应用 UX 体验标准</p></td><td rowspan="2"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-large-screen-0000001807707561#section12976125418475">功能完整</a></p></td><td><p>3.1.1</p></td><td><p>横竖屏适配</p></td><td><p>横竖屏适配检查</p></td><td><p>必须</p></td></tr><tr><td><p>3.1.2</p></td><td><p>多窗适配</p></td><td><p>多窗适配检查</p></td><td><p>必须</p></td></tr><tr><td rowspan="12"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-large-screen-0000001807707561#section146787220496">布局合理美观</a></p></td><td><p>3.2.1.1</p></td><td><p>布局基础要求(大屏)</p></td><td><p>折叠屏在各个形态下显示正常</p></td><td><p>必须</p></td></tr><tr><td><p>3.2.1.2</p></td><td><p>图标文字大小适中</p></td><td><p>折叠屏图标文字大小符合要求</p></td><td><p>必须</p></td></tr><tr><td><p>3.2.1.3</p></td><td><p>弹出框大小适中</p></td><td><p>折叠屏展开态弹出框高度符合要求</p></td><td><p>必须</p></td></tr><tr><td><p>3.2.1.4</p></td><td><p>宫格图片信息量适中</p></td><td><p>宫格图片控件占比符合要求</p></td><td><p>必须</p></td></tr><tr><td><p>3.2.1.5</p></td><td><p>广告图信息量适中</p></td><td><p>广告图控件占比符合要求</p></td><td><p>必须</p></td></tr><tr><td><p>3.2.1.6</p></td><td><p>上下图文信息量适中</p></td><td><p>上下图文信息量符合要求</p></td><td><p>必须</p></td></tr><tr><td><p>3.2.1.7</p></td><td><p>单行文本</p></td><td><p>单行文本字数检查</p></td><td><p>推荐</p></td></tr><tr><td><p>3.2.1.8</p></td><td><p>边距适中</p></td><td><p>应用/元服务左右边距符合要求</p></td><td><p>必须</p></td></tr><tr><td><p>3.2.1.9</p></td><td><p>效率型布局</p></td><td><p>效率型应用/元服务应使用分栏布局</p></td><td><p>推荐</p></td></tr><tr><td><p>3.2.1.10</p></td><td><p>浏览型布局</p></td><td><p>浏览型应用/元服务应使用宫格/瀑布流等布局</p></td><td><p>推荐</p></td></tr><tr><td><p>3.2.2.1</p></td><td><p>布局创新</p></td><td><p>折叠屏应在布局视觉提升的创新</p></td><td><p>推荐</p></td></tr><tr><td><p>3.2.2.2</p></td><td><p>侧边导航栏</p></td><td><p>应用窗口宽度 ≥840vp 时底部导航栏切换为侧边导航栏</p></td><td><p>推荐</p></td></tr><tr><td rowspan="5"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-large-screen-0000001807707561#section192433105012">交互易用</a></p></td><td><p>3.3.1.1</p></td><td><p>按钮易点击</p></td><td><p>按钮应避开难交互区域</p></td><td><p>推荐</p></td></tr><tr><td><p>3.3.1.2</p></td><td><p>键盘易操作</p></td><td><p>键盘按键应避开难交互区域</p></td><td><p>推荐</p></td></tr><tr><td><p>3.3.1.3</p></td><td><p>弹框易操作</p></td><td><p>弹出框位置易操作</p></td><td><p>推荐</p></td></tr><tr><td><p>3.3.2.1</p></td><td><p>临时悬浮窗</p></td><td><p>应用内启动临时的需要跨应用或跨实例跳转的任务应使用临时悬浮窗</p></td><td><p>推荐</p></td></tr><tr><td><p>3.3.2.2</p></td><td><p>临时双窗</p></td><td><p>应用内启动的临时的辅助任务应使用临时双窗</p></td><td><p>推荐</p></td></tr><tr><td rowspan="15"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-large-screen-0000001807707561#section65561444209">鼠标、触控板和键盘交互</a></p></td><td><p>3.4.1</p></td><td><p>可交互控件响应光标悬浮</p></td><td><p>当光标悬浮在应用/元服务的可交互控件上，控件或者光标需要提供对应的视觉反馈</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.2</p></td><td><p>目标单选</p></td><td><p>对于界面中支持选中态的目标，可使用鼠标或触控板对其进行选择</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.3</p></td><td><p>多目标框选</p></td><td><p>当需要选择多个目标时，可通过框选操作进行选择</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.4</p></td><td><p>多目标连选</p></td><td><p>当需要选择多个目标时，可通过连选操作进行选择</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.5</p></td><td><p>多目标点选</p></td><td><p>当需要选择多个目标时，可通过点选操作进行选择</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.6</p></td><td><p>目标点击</p></td><td><p>对于应用界面中可点击的控件，通过光标进行点击</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.7</p></td><td><p>滑动页面内容</p></td><td><p>当显示的内容超出应用窗口，可通过滑动页面浏览未显示的内容</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.8</p></td><td><p>文本选择</p></td><td><p>在文本内容区域，可对文本进行多选操作</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.9</p></td><td><p>旋转</p></td><td><p>对于界面中支持旋转的目标，可使用鼠标或触控板对其进行旋转</p></td><td><p>推荐</p></td></tr><tr><td><p>3.4.10</p></td><td><p>缩放</p></td><td><p>对于界面中支持缩放的目标，可使用鼠标或触控板对其进行缩放</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.11</p></td><td><p>拖移</p></td><td><p>对于界面中支持拖移的目标，可使用鼠标或触控板对其进行拖移</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.12</p></td><td><p>显示上下文菜单</p></td><td><p>对于界面中支持显示上下文菜单的目标，可使用鼠标或触控板打开上下文菜单</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.13</p></td><td><p>支持使用外接键盘键入</p></td><td><p>应用支持使用外接键盘键入文本</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.14</p></td><td><p>支持全键盘操作</p></td><td><p>应用/元服务中的主要任务流支持键盘的焦点导航</p></td><td><p>必须</p></td></tr><tr><td><p>3.4.15</p></td><td><p>支持常用功能的通用快捷键</p></td><td><p>支持常用功能的通用快捷键</p></td><td><p>必须</p></td></tr><tr><td rowspan="4"><p>折叠屏应用 UX 体验标准</p></td><td rowspan="4"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-foldable-screen-0000001807866557#section1519516555910">基础体验</a></p></td><td><p>4.1</p></td><td><p>开合连续性</p></td><td><p>应用/元服务在开合过程中体验连续</p></td><td><p>涉及则必须</p></td></tr><tr><td><p>4.2</p></td><td><p>开合流畅</p></td><td><p>应用/元服务在开合过程中动效流畅</p></td><td><p>推荐</p></td></tr><tr><td><p>4.3</p></td><td><p>悬停适配</p></td><td><p>应用/元服务在悬停态时布局满足要求</p></td><td><p>推荐</p></td></tr><tr><td><p>4.4</p></td><td><p>折痕避让</p></td><td><p>应用/元服务在悬停态时应避开折痕</p></td><td><p>推荐</p></td></tr><tr><td rowspan="5"><p>电脑应用UX体验标准</p></td><td rowspan="5"><p><a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-2in1-0000001777895636#section4545182215262">窗口响应式</a></p></td><td><p>5.1.1</p></td><td><p>支持窗口化运行</p></td><td><p>应用/元服务支持窗口化运行</p></td><td><p>推荐</p></td></tr><tr><td><p>5.1.2</p></td><td><p>支持窗口形态转换</p></td><td><p>应用/元服务支持通过窗口控制器转换窗口形态</p></td><td><p>推荐</p></td></tr><tr><td><p>5.1.3</p></td><td><p>支持窗口尺寸调节</p></td><td><p>应用/元服务支持在可调范围内任意调节窗口大小</p></td><td><p>推荐</p></td></tr><tr><td><p>5.1.4</p></td><td><p>支持分屏和比例调节</p></td><td><p>应用/元服务支持分屏和比例调节</p></td><td><p>推荐</p></td></tr><tr><td><p>5.1.5</p></td><td><p>窗口内容状态保持</p></td><td><p>应用/元服务窗口在调节时内容保持</p></td><td><p>涉及则必须</p></td></tr><tr><td rowspan="9"><p>元服务 UX 特征体验标准</p></td><td rowspan="9"><p><a href="/consumer/cn/doc/design-guides/ux-standard-overview-0000002019655177#ZH-CN_TOPIC_0000002019655177__section392114613448">特征体验</a></p></td><td><p>7.1.1</p></td><td><p><span>图标设计规范</span></p></td><td><p>详情如下</p></td><td><p>必须</p></td></tr><tr><td><p>7.1.2</p></td><td><p><span>元服务启动过程无自定义动画</span></p></td><td><p>详情如下</p></td><td><p>必须</p></td></tr><tr><td><p>7.1.3</p></td><td><p><span>启动无开屏、无扑脸广告</span></p></td><td><p>详情如下</p></td><td><p>必须</p></td></tr><tr><td><p>7.1.4</p></td><td><p><span>退出时无拦截</span></p></td><td><p>详情如下</p></td><td><p>必须</p></td></tr><tr><td><p>7.1.5</p></td><td><p>头部导航栏</p></td><td><p>详情如下</p></td><td><p>必须</p></td></tr><tr><td><p>7.1.6</p></td><td><p><span>元服务胶囊</span></p></td><td><p>详情如下</p></td><td><p>必须</p></td></tr><tr><td><p>7.1.7</p></td><td><p><span>底部导航栏</span></p></td><td><p>详情如下</p></td><td><p>必须</p></td></tr><tr><td><p>7.1.8</p></td><td><p>沉浸式设计</p></td><td><p>详情如下</p></td><td><p>推荐</p></td></tr><tr><td><p>7.1.9</p></td><td><p><span>基本转场过程无多余加载过渡</span></p></td><td><p>详情如下</p></td><td><p>推荐</p></td></tr></tbody></table>

## 特征体验

7.1.1 图标设计规范

<table><tbody><tr><td><p>标准编号</p></td><td><p>7.1.1</p></td><td><p>图标设计规范</p></td></tr><tr><td colspan="2"><p>标准描述</p></td><td><p>1.元服务图标与应用图标有明显区别，它继承了 HarmonyOS 的设计语言体系，内部圆形表示完整独立，外圈装饰线表示可分可合可流转的特点。</p><p>2.元服务图标生成需提供尺寸为 1024 x 1024 px 的静态图片资源（参考<a href="https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-overview-0000001900384976#section158386422413" target="_blank">图标设计规范</a>），并使用元服务图标工具（<a href="https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-icon-generation" target="_blank">生成元服务图标</a>）生成相应的规范图标。</p><p>3.元服务图标外圈线请勿使用纯白或纯黑，以避免在纯白/纯黑页面背景上无法清晰辨识其轮廓形态。当中心圆背景为纯白/纯黑时，需给中心圆增加描边，以确保图标中心圆轮廓清晰可见。</p></td></tr><tr><td colspan="2"><p>测试方法</p></td><td><p>规范图标需满足：</p><p>1）内环圆形、外形点状轮廓需符合元服务装饰特征。</p><p>2）生成的元服务图标统一为 PNG 格式资源。</p><p>3）元服务图标在黑白背景下清晰无锯齿、无拉伸。</p><p>4）元服务工程文件中的图标尺寸满足 512*512 px。</p><p>5）AppGallery Connect 上架元服务时，<a href="https://developer.huawei.com/consumer/cn/doc/app/agc-help-harmonyos-releaseservice-0000001946273965#section94111352985" target="_blank">“应用信息”页面</a>上传的图标满足相应要求。</p></td></tr><tr><td colspan="2"><p>判定标准</p></td><td><p>所有元服务图标透出场景均需满足图标显示要求</p></td></tr><tr><td colspan="2"><p>标准等级</p></td><td><p>必须</p></td></tr><tr><td colspan="2"><p>适用设备类型</p></td><td><p>手机、折叠屏、平板、电脑</p></td></tr><tr><td colspan="2"><p>需考虑的特殊事项</p></td><td><p>无</p></td></tr><tr><td colspan="2"><p>系统能力</p></td><td><p>请参阅：<a href="https://developer.huawei.com/consumer/cn/doc/atomic-guides/atomic-service-icon-generation" target="_blank">生成元服务图标</a></p></td></tr></tbody></table>

7.1.2 元服务启动过程无自定义动画

展开

| 
标准编号

 | 

7.1.2

 | 

元服务启动过程无自定义动画

 |
| :-- | :-- | :-- |
| 

标准描述

 |    | 

平台针对元服务启动过程提供了系统原生启动动效，不可在系统启动动效的基础上叠加使用其他自定义加载效果。

 |
| 

Video Player is loading.

Current Time 0:00

Loaded: 0%

0:00

Duration \-:-

1x

-   2x
-   1.8x
-   1.5x
-   1.2x
-   1x, selected

This is a modal window.

The media could not be loaded, either because the server or network failed or because the format is not supported.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-Transparent

Text BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparent

Caption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%

Text Edge StyleNoneRaisedDepressedUniformDrop shadow

Font FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

End of dialog window.

252

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092035.26880760547005204988087587556257:50001231000000:2800:AC99B435DB0F120A05CEE017F5D6B7BA35B3DE609CCC81C983754DF212D70771.png "点击放大")

Do

 | 

Video Player is loading.

Current Time 0:00

Loaded: 0%

0:00

Duration \-:-

1x

-   2x
-   1.8x
-   1.5x
-   1.2x
-   1x, selected

This is a modal window.

The media could not be loaded, either because the server or network failed or because the format is not supported.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-Transparent

Text BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparent

Caption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%

Text Edge StyleNoneRaisedDepressedUniformDrop shadow

Font FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

End of dialog window.

175

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092035.07740540005971996333474470215966:50001231000000:2800:D2CB15EC39471757DDBB4B4937D2C56941DD3A5A8F798E8DAA323BE39431B5CA.png "点击放大")

Don't（使用非系统原生动效）

 | 

Video Player is loading.

Current Time 0:00

Loaded: 0%

0:00

Duration \-:-

1x

-   2x
-   1.8x
-   1.5x
-   1.2x
-   1x, selected

This is a modal window.

The media could not be loaded, either because the server or network failed or because the format is not supported.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-Transparent

Text BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparent

Caption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%

Text Edge StyleNoneRaisedDepressedUniformDrop shadow

Font FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

End of dialog window.

124

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092035.70049108862184485720854893063790:50001231000000:2800:B79EA0559A9626F0D25AD42BAC491E82603AF3FA0D441A5500E5C46CE0C945A7.png "点击放大")

Don't（在原生动效上叠加其他加载效果）

 |
| 

测试方法

 | 

启动元服务，检查元服务启动过程中，无系统加载动效外的其他自定义加载效果。

 |
| 

判定标准

 | 

进入元服务时，展示元服务系统原生启动动效，动效完成后直接进入首页，过程中无其他动效。

 |
| 

标准等级

 | 

必须

 |
| 

适用设备类型

 | 

手机、折叠屏、平板、电脑

 |
| 

需考虑的特殊事项

 | 

无

 |
| 

系统能力

 | 

设计规则

 |

7.1.3 启动无开屏、无扑脸广告

展开

| 
标准编号

 | 

7.1.3

 | 

启动无开屏、无扑脸广告

 |
| :-- | :-- | :-- |
| 

标准描述

 |    | 

通过元服务图标、服务卡片、场景调用等方式打开元服务，无开屏界面。非用户主动操作，应避免出现扑脸弹框（系统隐私提醒除外）干扰用户。

 |
| 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.22725857108298706281708708983031:50001231000000:2800:DEF628C3BB6348315D47A5927967AA1D1D657EBCB338E1345A49536FE9BB0C4E.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.78754923236728548003195363927793:50001231000000:2800:CA8D82635BE6A379A415B88003FB75148C3F3D3094CF93D1D64CA148AE08E52F.png "点击放大")

Do

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.12450765472752677000868120929655:50001231000000:2800:2F868E3278C77DC2E92C91D0CABE503D59F616FC4FB46FF7DD56AB34DF0C742B.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.95335675213387119339451062222578:50001231000000:2800:51035C1E62D422A0887ADFAED0A2C63923050316C5CF8B314EF772A8E185429C.png "点击放大")

Don't

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.89565938577378538822346290625738:50001231000000:2800:2BB472B47F1E6A48F7D679B1AE12CE4F355BAA11DA8D20BFC80DEE2DE4754E3E.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.97986449052405204239891758045420:50001231000000:2800:AE7D15048214A65ABAA5DFBA4A45068F7BE5EF29B96E7632D0EC7481490A6CD5.png "点击放大")

Don't

 |
| 

测试方法

 | 

启动元服务，元服务系统加载完后，直接进入首页。

 |
| 

判定标准

 | 

元服务加载完后，直接进入首页，无其他开屏、弹窗等广告信息干扰。

 |
| 

标准等级

 | 

必须

 |
| 

适用设备类型

 | 

手机、折叠屏、平板、电脑

 |
| 

需考虑的特殊事项

 | 

无

 |
| 

系统能力

 | 

官方提供底部悬浮窗样式，请参阅：[InterstitialDialogAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-interstitialdialogaction)

其他按照设计规则

 |

7.1.4 退出时无拦截

展开

| 
标准编号

 | 

7.1.4

 | 

退出时无拦截

 |
| :-- | :-- | :-- |
| 

标准描述

 | 

系统返回手势需一键关闭元服务、一键返回上一级页面，不允许二次弹框等形式打断用户行为。

 |
|    | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.04863389088153929500145811062105:50001231000000:2800:D94B4CBF499C7EF91776A53B41297CA14E06B023A9539D485A075C8620566DB3.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.58836273641077324546334442373488:50001231000000:2800:814FEF107A48A2819EC39CE9FA606CDB879F3D6268B38E5B9E6D8D1ABF0A4A79.png "点击放大")

Don't

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092036.97228433611810680290889787814458:50001231000000:2800:61287F45A6A7DB9164977EE638A342027CD864785080E60C6200233266E8AA50.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.78640582978497215289651273057563:50001231000000:2800:0E5DA3664D86C54E1A16ABA955058BCEE3F9E3347D8BF33A57390B685FD9D931.png "点击放大")

Don't

 |
| 

测试方法

 | 

启动元服务，在元服务内使用侧滑返回手势，检查手势响应效果。

 |
| 

判定标准

 | 

遵循元服务轻量高效规范

 |
| 

标准等级

 | 

必须

 |
| 

适用设备类型

 | 

手机、折叠屏、平板、电脑

 |
| 

需考虑的特殊事项

 | 

无

 |
| 

系统能力

 | 

设计规则

 |

7.1.5 头部导航栏

<table><tbody><tr><td><p>标准编号</p></td><td><p>7.1.5</p></td><td colspan="2"><p>头部导航栏</p></td></tr><tr><td rowspan="5"><p>标准描述</p></td><td rowspan="5">&nbsp;&nbsp;</td><td colspan="2"><p>如开发者需使用头部导航栏，建议开发者直接调用元服务官方提供的导航栏 (<a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation" target="_blank">AtomicServiceNavigation</a>) 控件。</p><p>若开发者选择自行设计开发导航样式，请遵循：</p><p>1）为确保头部导航简洁清晰，一级标题栏范围内有且仅最多显示 2 个元素（含文本、图片标识、功能操作），非一级标题栏范围内有且仅最多显示 3 个元素。（必须）</p><ul><li>合理利用头部空间，避免使用双行竖排标题。</li><li>为适应头部 banner 运营需求，一级标题栏标题元素非强制显示。</li></ul><p>2）合理设置标题栏高度，避免过低（低于44vp）出现元服务胶囊与标题栏、底部内容信息重叠问题。（必须）</p><p>3）为确保标题栏左右信息对称，标题元素均需与元服务胶囊水平中心对齐。（必须）</p><p>4）标题栏范围仅有一个元素时，需要保证左对齐。（必须）</p><ul><li>手机左侧第一个元素距离左侧屏幕边缘不超过 16vp（建议 16vp）。</li><li>折叠屏左侧第一个元素距离左侧屏幕边缘不超过 24vp（建议 24vp）。</li><li>平板左侧第一个元素距离左侧屏幕边缘不超过 32vp（建议 32vp）。</li></ul><p>5）合理设置标题文本字号，一级标题建议加粗，默认字号不小于 20fp，非一级标题默认字号不小于 18fp 。（推荐）</p><p>6）明确一级界面和非一级界面关系，非一级界面的标题栏必须提供返回或关闭按钮。（必须）</p></td></tr><tr><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.33816793877158515999989562120729:50001231000000:2800:DEB7717A91C4D7848969D72F8449ABC9D221E028EE77E345A735B0A317EB3C60.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.15425026140887590850337887897149:50001231000000:2800:69AC10890394BD5113764559E1D9643BBC35F6453D40C3C51932C006213E413B.png" title="点击放大" height="5"></span></p><p>Do（标题栏高度显示合理）</p></td><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.83485451851486140576866625329602:50001231000000:2800:964B78387C9A8D62842374D1E244D96E3CB2ECE44EDB0111395D1959E224F347.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.41163284752518966349180320446530:50001231000000:2800:2632A3D9A63AC872E6B25D7D6E5198A8DF0F647209D4ADAEF8C3D554D1C81B5B.png" title="点击放大" height="5"></span></p><p>Don't（标题栏过低）</p></td></tr><tr><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.11290979360702976750493343030459:50001231000000:2800:78B3578FE41B27CD74A6A3683EB15A029BB0BF46E01C50A639AF370F9EBAE61A.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.76561616423746460472133920359108:50001231000000:2800:1A3081DE720CEBE011D7B23E1FB9C77BC8768BD8B2F1DE546AC37E4244F6FAC8.png" title="点击放大" height="5"></span></p><p>Do（一级标题显示元素数量适中）</p></td><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.97799110573458580315590869886170:50001231000000:2800:7151A004F944335061390F0E2683CE92FDDA06A5E70CFADB47ABCEA25CCE94A2.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.72927316649793346131402631279297:50001231000000:2800:6814E51B96402C2E5B162F41470BF6DF564EEB86D0A8A82C8721824113190107.png" title="点击放大" height="5"></span></p><p>Don't（一级标题显示元素数量过密）</p></td></tr><tr><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.68112306721079538253583125121272:50001231000000:2800:6769905C02B878E8586ACB7117C858353CAC2F8330C1E175A2095484752ADBC2.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.25293114067304362913885439156339:50001231000000:2800:AE1156A482F97C6A700FDA1AFAEADF6E497ABC484EAD372BD0BC3F3C4D90AD24.png" title="点击放大" height="5"></span></p><p>Do（标题与胶囊水平中心对齐）</p></td><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.08874413213023774494789219070894:50001231000000:2800:A45809A60D73151D4C903799F2F82DDC489CD99A8CB66E8B5D3A81A4D195D090.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.60440401349812190854965396024458:50001231000000:2800:20D3E87FBE41834825CCEE63871E8AE67D12AB079F1E03BF9F7624B8C3A1CEEE.png" title="点击放大" height="5"></span></p><p>Don't（标题元素靠上）</p></td></tr><tr><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.71503477084811167445815713045967:50001231000000:2800:3A8EF05604BD86AF2F552F0D49BB5CDCC7384BBF6BD74EA7E4615A6C270F7CC7.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.86876161677089600917135910515275:50001231000000:2800:F80E7AE3014AFEB5A0E1124227F6E39D470643463866A1C2710CFA3F172FE4EC.png" title="点击放大" height="5"></span></p><p>Do（单元素标题左对齐）</p></td><td><p><span><img originheight="356" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092037.94108065134882304498190326511942:50001231000000:2800:ED16444A65FF8591BD037E355641A7B3119975EB93E0C489BDCBEE8F54814796.png" title="点击放大" height="226.772"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.50712332439735209078736482665762:50001231000000:2800:07F9A25EE153A34F7E755566CC369DFFDD6C6F148AAB9599ACE604476527CC8E.png" title="点击放大" height="5"></span></p><p>Don't（单元素标题未保持左对齐）</p></td></tr><tr><td colspan="2"><p>测试方法</p></td><td colspan="2"><p>启动元服务，检查界面各级页面头部导航栏。</p></td></tr><tr><td colspan="2"><p>判定标准</p></td><td colspan="2"><p>元服务所有头部导航栏信息构成、显示高度、标题字号、标题显示位置满足元服务规范要求。</p></td></tr><tr><td colspan="2"><p>标准等级</p></td><td colspan="2"><p>必须</p></td></tr><tr><td colspan="2"><p>适用设备类型</p></td><td colspan="2"><p>手机、折叠屏、平板、电脑</p></td></tr><tr><td colspan="2"><p>需考虑的特殊事项</p></td><td colspan="2"><p>无</p></td></tr><tr><td colspan="2"><p>系统能力</p></td><td colspan="2"><p>请参阅：<a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation" target="_blank">AtomicServiceNavigation</a></p></td></tr></tbody></table>

7.1.6 元服务胶囊（Menubar）

<table><tbody><tr><td><p>标准编号</p></td><td><p>7.1.6</p></td><td colspan="3"><p>元服务胶囊（Menubar）</p></td></tr><tr><td rowspan="2"><p>标准描述</p></td><td rowspan="2">&nbsp;&nbsp;</td><td colspan="3"><p>元服务胶囊在静态或第一屏界面显示时，胶囊区域无文本信息或功能控件遮挡，无热区冲突。</p></td></tr><tr><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.16077634602645033205625569011057:50001231000000:2800:847C7834C034081A796950CCC65ECABCEEBE208F8BB1349D082473082415CD94.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.60145578396962381229561590364367:50001231000000:2800:0C521D2A17949976A16F3F622773FBF0763A4CD8C65E2CFCC01EAA0B7B8A3C9D.png" title="点击放大" height="5"></span></p><p>Do</p></td><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.73123845957211955673798658384130:50001231000000:2800:0D0D7EC2F302F0056A353FA98277E17A911CFE7ED8C6A075ABB874632BE996F7.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.52225088859146847201446529352614:50001231000000:2800:2103443BC6AA46112F26D339422F6ADF5F061BF4006F7089C02143895D3471F5.png" title="点击放大" height="5"></span></p><p>Don't（操作热区冲突）</p></td><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.09890804562765070251540607703399:50001231000000:2800:CFEC4E935A87A7D7110FE1725A2F0821970E2ABF7923C9556BFD7CFF1A4B9B2F.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.34265007020640850638220829422643:50001231000000:2800:BF88851E95C1011EB80E95F0640F6A3533065B59B0CDD1F6CEAF0ABACFB8CFE1.png" title="点击放大" height="5"></span></p><p>Don't（标题栏过低，信息遮挡）</p></td></tr><tr><td colspan="2"><p>测试方法</p></td><td colspan="3"><p>元服务胶囊在静态或第一屏界面显示时，胶囊区域无文本信息或功能控件遮挡，无热区冲突。</p></td></tr><tr><td colspan="2"><p>判定标准</p></td><td colspan="3"><p>除全屏模态弹窗场景，其他静态或第一屏界面显示时，元服务胶囊需保证显示清晰且可操作，胶囊区域无文本信息或功能控件遮挡，无热区冲突。</p></td></tr><tr><td colspan="2"><p>标准等级</p></td><td colspan="3"><p>必须</p></td></tr><tr><td colspan="2"><p>适用设备类型</p></td><td colspan="3"><p>手机、折叠屏、平板、电脑</p></td></tr><tr><td colspan="2"><p>需考虑的特殊事项</p></td><td colspan="3"><p>无</p></td></tr><tr><td colspan="2"><p>系统能力</p></td><td colspan="3"><p>设计规则</p></td></tr></tbody></table>

7.1.7 底部导航栏

<table><tbody><tr><td><p>标准编号</p></td><td><p>7.1.7</p></td><td colspan="3"><p>底部导航栏</p></td></tr><tr><td rowspan="2"><p>标准描述</p></td><td rowspan="2">&nbsp;&nbsp;</td><td colspan="3"><p>如开发者需使用底部导航栏，建议开发者直接调用元服务官方提供的底部页签 (<a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicetabs" target="_blank">AtomicServiceTabs</a>) 控件。</p><p>若开发者选择自行设计开发导航样式，请确保导航简洁清晰，并遵循：</p><p>1）页签数量配置最多不超过 5 个，最少不少于 2 个。</p><p>2）合理设置底部导航栏高度，除去导航条固定高度（28vp），底部页签栏（此处仅涉及手机、折叠屏）在设计时应避免过高（超过70vp）或过低（低于 40vp）。</p></td></tr><tr><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.57560851799202287420731336574944:50001231000000:2800:F453C433772F3494E11ED97AF4A79BF916FF247412DCB550D812B09660B84E6E.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.32650562689340030934473619181224:50001231000000:2800:8882510F44BDB528EF44B1BA1F3A4CD0E22BB610E432259AC4966FA684A5B2A8.png" title="点击放大" height="5"></span></p><p>Do</p></td><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.13305368587880336517666674968323:50001231000000:2800:235BC6710CF775BC53F268B43D85580529DEC247E3C0DD566C1303E8EBAC04D2.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.55565895783807286180850934797558:50001231000000:2800:BC56A8B572B74357440FB7543CA0927C9D31B0DC5818CDB233873A2130CF2526.png" title="点击放大" height="5"></span></p><p>Don't</p></td><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.43468514186283714161117692223446:50001231000000:2800:6774A1E075768EBE50ECDC771435B74D6B3BB89B300E5DD9052D272217D1B168.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092038.31495168253492004455631109158249:50001231000000:2800:3F172E7CBD6D6C66995309B2D81CFB21A30E0E90761FC8F6F268125BC553F062.png" title="点击放大" height="5"></span></p><p>Don't</p></td></tr><tr><td colspan="2"><p>测试方法</p></td><td colspan="3"><p>启动元服务，检查元服务底部导航栏。</p></td></tr><tr><td colspan="2"><p>判定标准</p></td><td colspan="3"><p>元服务底部导航栏显示高度、页签数量、与导航条避让间距满足元服务规范要求。</p></td></tr><tr><td colspan="2"><p>标准等级</p></td><td colspan="3"><p>必须</p></td></tr><tr><td colspan="2"><p>适用设备类</p></td><td colspan="3"><p>手机、折叠屏、平板、电脑</p></td></tr><tr><td colspan="2"><p>需考虑的特殊项</p></td><td colspan="3"><p>无</p></td></tr><tr><td colspan="2"><p>系统能力</p></td><td colspan="3"><p>请参阅：<a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicetabs" target="_blank">AtomicServiceTabs</a></p></td></tr></tbody></table>

7.1.8 沉浸式设计

<table><tbody><tr><td><p>标准编号</p></td><td><p>7.1.8</p></td><td colspan="3"><p>沉浸式设计</p></td></tr><tr><td rowspan="2"><p>标准描述</p></td><td rowspan="2">&nbsp;&nbsp;</td><td colspan="3"><p>元服务头部标题栏满足沉浸一体式设计：</p><p>1）避免标题栏底部背景色与服务内底部背景色（含状态栏背景色）差异过大，确保自然过渡。</p><p>2）融合背景的同时，需要确保标题栏信息清晰可阅读。字体和背景的对比度至少 3:1。</p></td></tr><tr><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092039.89967687335876287211745264135012:50001231000000:2800:C84D405EE60952E407AA1E51380F8D75023082B3E7E55337986A8802D39C4486.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092039.38588392477851298262667715976026:50001231000000:2800:A103D562C6C1B17F97D3CCA2AB416A568C34AE1239ED1EDD37FD8DB569B7A826.png" title="点击放大" height="5"></span></p><p>Do</p></td><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092039.43573976010065166911377289777916:50001231000000:2800:15BBDA96F22E477271F2EE1F14C1FB51A55ECD93ACE46C5E73C72708E286D1C8.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092039.44635771110897413497813167572547:50001231000000:2800:0FBB5149040553E19C325B9ED9B2A5FBFB17B49DC3906BDB1A29C2A4698C4606.png" title="点击放大" height="5"></span></p><p>Don't（背景色分割块面多）</p></td><td><p><span><img originheight="1771" originwidth="1000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092039.16145408117709163360973743435987:50001231000000:2800:A4B48844987F78A85401DA2193CA3272EC460C9DF8B8843ADC2BE2BC1B744418.png" title="点击放大" height="1128.127"></span></p><p><span><img originheight="5" originwidth="303" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250625092039.39194299360006929806086559564473:50001231000000:2800:723D6603B62E1FFCA4E46A0AA6B80B8D354DAF6F0593B7D850335CCFF4C08C7D.png" title="点击放大" height="5"></span></p><p>Don't（标题信息模糊）</p></td></tr><tr><td colspan="2"><p>测试方法</p></td><td colspan="3"><p>启动元服务时，检查标题栏背景色沉浸式效果。</p></td></tr><tr><td colspan="2"><p>判定标准</p></td><td colspan="3"><p>元服务所有头部标题栏满足沉浸一体式设计</p></td></tr><tr><td colspan="2"><p>标准等级</p></td><td colspan="3"><p>推荐</p></td></tr><tr><td colspan="2"><p>适用设备类型</p></td><td colspan="3"><p>手机、折叠屏、平板、电脑</p></td></tr><tr><td colspan="2"><p>需考虑的特殊事项</p></td><td colspan="3"><p>无</p></td></tr><tr><td colspan="2"><p>系统能力</p></td><td colspan="3"><p>设计规则</p></td></tr></tbody></table>

7.1.9 基本转场过程无多余加载过渡

<table><tbody><tr><td><p>标准编号</p></td><td><p>7.1.9</p></td><td><p>基本转场过程无多余加载过渡</p></td></tr><tr><td colspan="2"><p>标准描述</p></td><td><p>检查元服务一二级界面切换效果，保证元服务转场切换沉浸无干扰，页面跳转遵循元服务动效规范，切换过程中无须动画/文字加载状态。</p><p>动效设计满足：</p><p>1）父子层级转场流畅，无多余动画/文字加载提示。</p><p>2）搜索、新建、编辑场景转场流畅，无多余动画/文字加载提示。</p><p>3）卡片（列表、网格、按钮、图片、视频）打开转场流畅，无多余动画/文字加载提示。</p><p>4）左右翻页滑动流畅，无多余动画/文字加载提示。</p></td></tr><tr><td colspan="2"><p>测试方法</p></td><td><p>检查元服务一二级界面切换效果。</p></td></tr><tr><td colspan="2"><p>判定标准</p></td><td><p>遵循元服务加载状态规范</p></td></tr><tr><td colspan="2"><p>标准等级</p></td><td><p>推荐</p></td></tr><tr><td colspan="2"><p>适用设备类型</p></td><td><p>手机、折叠屏、平板、电脑</p></td></tr><tr><td colspan="2"><p>需考虑的特殊事项</p></td><td><p>无</p></td></tr><tr><td colspan="2"><p>系统能力</p></td><td><p>请参阅<a href="https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-page-transition#section92341720171119" target="_blank">合理使用页面间转场-转场场景</a></p></td></tr></tbody></table>
