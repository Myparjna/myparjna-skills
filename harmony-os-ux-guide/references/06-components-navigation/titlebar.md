# 标题栏

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/titlebar-0000001929628982
- 抓取时间：2026-04-04T08:22:53.231Z
标题栏是布局在界面顶部的导航类控件，用于呈现界面名称和操作入口。开发相关描述请参考 [Navigation/Title](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#title) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101813.65145448095507534555588519316028:50001231000000:2800:1A15D4D3D5AC8C8F0D5B51C023E979A7C0DB5A0EBF5CEBEBB80843E9736FBE8B.jpg "点击放大")

## 如何使用

**标题栏用于展示当前页面的标题和状态信息。**使用标题栏显示当前界面的名称和操作入口，标题栏的样式会极大影响内容首屏显示的效率，不同类型的界面可以匹配不同的风格，具体可参考下方控件构成相关内容。

**明确当前标题的导航层级，给予用户重要提示。**系统导航的基础逻辑应当明确一级目录的唯一性，非一级页面要有明确返回导航或者关闭操作，防止用户在使用应用的过程中丢失导航路线。

**合理使用右侧可操作区域，适当提供可操作选项。**放置与当前页面相关的操作按钮，如搜索、分享、设置等，操作按钮应与当前页面内容密切相关，避免提供与应用不相关的操作内容。如果应用的操作项过多，请不要全部展示出来，可以通过展示“更多”图标来提供菜单选项，简化界面复杂度，详情可参考 [menus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu) 能力规格。

**标题栏的高度应保持一致，以确保良好的交互体验。**标题栏控件在 HarmonyOS NEXT 上默认单行高度为 56vp，强调型标题栏为 112vp，开发者需要根据自身业务需要选择不同类型的标题栏，可以通过 NavigationTitleMode 来进行配置，其中 Free 样式为动态布局，标题栏会根据手势滑动动态缩小高度，Mini 与 Full 均为固定样式。

**标题栏文本的呈现应简洁明了。**标题的描述应准确反映当前页面的内容和状态，不要用过长的字符串来展示标题信息，标题展示的文本信息应该是当前页面的概述和分类。文本过长不仅影响布局和美观度，也会在阅读体验上产生影响。除此之外，标题文字应使用醒目的字体大小和颜色，与背景形成足够对比，在系统默认风格的标题栏中使用加粗字体来展示其重要性。

## 组件规则

### 组件构成

**一级页标题**

标题栏一般由标题和右侧功能图标组成，在一级标题栏下左侧不可以出现返回标题，若在 Mini 样式下默认带上返回图标，需要通过 [hideBackButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidebackbutton) 隐藏其显示。标题栏的使用通常与系统信号栏的布局相邻，在默认情况下标题栏的背景色会延伸至信号栏区域，通过 [expandSafeArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea) 接口可以实现安全区的避让。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101813.85815108842637333731297087397805:50001231000000:2800:06AF8AE79F1FC8AAD6CA8BBE5C20F94234CEB209F992643B3EF7CCF2334448C0.png "点击放大")

强调型标题栏

主要用于一级界面突出标题区域，在没有特殊要求的情况下，模块的一级界面应该使用强调型标题栏。

支持显示单行标题、双行标题、强调型标题样式。

<table id="ZH-CN_TOPIC_0000001929628982__X3034304dc56ed4b8f5bebf16288672957c5f057" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row130mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p132mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.62254942247264485492710259387954:50001231000000:2800:746B84D660C723F1AA4DAC7F103B8C09EB6F8DD8DAF83942B1C39639DE6E6582.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p134mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.74633169269530959505882556825958:50001231000000:2800:06A4DEB5133E70C74CBF18845F31E86ECD97536B4F99A4A2BE997A9E38E78A94.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

普通型标题栏

用于不需要突出标题的场景。当界面上方主要区域为图形化展示时，应该使用普通标题栏。

支持单行标题和双行标题两种样式。

<table id="ZH-CN_TOPIC_0000001929628982__Xb0169c78e277b65290bf3cd1cc1ec98c8d68beb" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row143mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p145mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.71164914531911168789478762211509:50001231000000:2800:67161644D75138576CE0E3A0E3EC30AA2266CDFBD0D085FF644E467B46988CAC.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p147mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.59534925266239866739505731983544:50001231000000:2800:1A9145A2273C1CFF3F93C10E197BD77381B7CE132C6B6E69DFD4C833CE28AF74.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

抽屉型标题栏

用于展示不同的分类，可以快捷地进行切换、查找。抽屉型在不同尺寸设备上呈现的效果略有差异，手机端为侧边遮罩层，平板端等大屏设备为分栏界面布局。通常效率型、办公类及内容型应用较为常用。抽屉标题栏需要配合 [SideBarContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer) 结合使用。

<table id="ZH-CN_TOPIC_0000001929628982__X8f626e9e1a5b795ebf8de5854ef32cc3e16ce0c" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row156mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p158mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.55500334102159430158185621178761:50001231000000:2800:DF1536FF511DCADA78C0C76377A8D4E0C360097963F0A221F83545B0DBE55E3F.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p10247102314199"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.34941656342600935387653748463095:50001231000000:2800:DF6E1AFF549645019F5E0595F6CB56A00B5E2B4E3A6C4D7651944EDFC6933584.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

**二级页标题**

除一级界面、编辑界面和选择界面外，所有其他界面都展示二级页标题。二级标题栏通常使用 [NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination) 控件组合使用，NavDestination 是子页面的根容器控件，用于显示 Navigation 的内容区。

<table id="ZH-CN_TOPIC_0000001929628982__Xbe1818bdec4b8b305bc909d8c96ff812d244b8e" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row169mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p171mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.62382165400805378358196641656217:50001231000000:2800:A6B86633C808E27A1230D320F6D512AE18305D57DED81B0C9DD91DB00E69FBD2.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>

编辑界面

当需要对界面内容进行编辑时，使用编辑界面标题栏。详情能力可参考 [EditableTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-editabletitlebar) 控件相关能力。

编辑界面标题栏一般使用左侧关闭右侧确认的布局形式，在一些需要大量编辑文本的场景下可以使用返回按钮。

<table id="ZH-CN_TOPIC_0000001929628982__Xffa4a7e8f6935583f96e2a3f03a649ce78a91cd" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row182mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p184mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.16878238076281812310279870685602:50001231000000:2800:1F25444DD2744137A95D71199315F5701F072DDA5408B308691B0DDD98B2482E.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929628982__p186mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.21917339007596764395781200632147:50001231000000:2800:0BB1708EF85B6AC2CD927E220CD4E1C37989E1A920D488E8971AE27C5CEE5ED0.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

### 视觉规则

**模糊材质**

标题栏可以通过模糊材质实现更高级的视觉效果，HDS 标题栏控件默认背板带有模糊材质。同时，该控件提供了两种模糊类型：

-   通用模糊：组件对标题栏的背景进行均匀的模糊处理，模糊强度一致，边界清晰，用于强调控件与内容的层级分隔。
-   渐变模糊：模糊效果在空间维度上呈现渐强/渐弱的变化，模糊边界柔和，用于增强页面沉浸感。

HDS 标题栏控件开发相关描述请参阅 [HDS Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation) 文档。

**直接模糊**

在标题栏中，通用模糊作为独立视觉层级存在，与内容层形成悬浮空间关系，适用于页面内容与标题栏产生交叠的场景。

标题栏的通用模糊默认带有提亮压暗属性，能够激发色彩活力，提高背板通透度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101814.64870278553046553947832279385588:50001231000000:2800:CDCC734763923215BF888984344BA8F139CFDADCF459EADEF51FC67C3A0DDBBD.png "点击放大")

为提高内容边界可识别性，避免视觉认知障碍问题，默认情况下，模糊背板下边缘带有一条 1 px 的分割线。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101815.80982651655298455698995498852096:50001231000000:2800:049FF36FDE47CE9B7909B8FED592309DEEBE1C658718D822C330C7F0B417454A.png "点击放大")

半模态标题栏在满足内容与标题区产生重叠关系时，采用通用模糊类型，提升半模态页面质感。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101815.35814009790382718566238769638198:50001231000000:2800:4A816CC9B31F14549A9DA8AB71B0CF7D41DF03288D5A11791486195379ABAD98.png "点击放大")

**渐变模糊**

渐变模糊与页面内容的融合度更高，通过弱化视觉边界，以延展页面空间，但渐变模糊会增高页签占用面积、降低页签内容可读性，因此仅适用于部分特定场景。

渐变模糊默认带有黑色渐变蒙层，用于提高标题栏可识别度。

渐变的颜色蒙层支持自定义修改颜色，在不同场景下，可通过匹配背景颜色增强页面沉浸感。

标题栏支持添加自定义组件，如添加自定义内容，模糊背板会随着标题栏高度变化而变化，分割线始终位于模糊背板下边缘。

**跟手与反馈**

直接模糊和渐变模糊类型都具备两种模糊跟手生效的方式：

-   直接生效
-   过渡生效

**直接生效**

滑动内容进入/离开标题栏区域过程中，模糊背板和分割线透明渐变出现/消失。此方式适用于非沉浸式场景。

当页面内容进入/离开标题栏区域时，默认触发模糊 & 分割线渐变显示/隐藏，增强触顶操作的心理暗示。

**过渡生效**

滑动前后标题栏内容发生颜色/状态变化，滑动过程中，线性跟手变化。此方式仅适用于沉浸式到非沉浸式相互切换的场景。

**堆叠与模糊材质**

使用ark UI的标题栏组件，除了通用的布局规格以外，也提供了可堆叠样式，开发者可以通过 [BarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#barstyle12枚举说明) 配置其属性为 STACK 来改变标题栏的布局层级。使用了堆叠样式后，界面中的内容便可以穿透到组件下方。在 [NavigationTitleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigationtitleoptions11) 中将标题栏背景色设置为透明度，同时使用 backgroundBlurStyle 属性配置其[模糊样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#blurstyle9)的枚举，结合堆叠样式和模糊属性实现标题栏的整体模糊效果。

<table id="ZH-CN_TOPIC_0000001929628982__table130184019198" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row1230118402192"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p2301640101920"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101815.84120051174778314715080985042249:50001231000000:2800:1A38CBA489DEEBDACA1AA18315D3B3852DB124B76F582DB1EB71A6C9AFC983DC.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p123018405197"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101815.46650698300176661272452773591085:50001231000000:2800:0FD0F4CF5C3D4876B2CA791C10EE6C2715B514C05E14A40ECC574EE615FE4AEF.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929628982__row19301040191916"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p28157491199">普通深浅模式下，模糊按照整个控件区域呈现，可以扩展至信号栏区域。</p><p id="ZH-CN_TOPIC_0000001929628982__p158155495199">模糊生效时，在标题栏底部会有一条分割线投影，用于明确区分布局边界。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p73011340191913">当模糊效果不生效时，背景色与界面融为一体。需确保模糊材质内的填充色与界面背景色一致。</p></td></tr></tbody></table>

## 设备差异

### 手机设备

**横屏**

标题栏布局与竖屏一致，右侧图标为竖屏下 Toolbar + Appbar 上所有功能图标的集合。

手机端除 Launcher 模块，信号栏默认不显示，标题栏紧贴屏幕开始显示，高度为 56 vp。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101815.80390303286457773068278969509686:50001231000000:2800:C9FB557D396F5BBBE0705A690E12722A7BFBD95A3ED07905B2BB12313C1708F7.png "点击放大")

**分栏**

标题栏在其可用区域内，按照竖屏规则布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101815.49991790585421209133392653025031:50001231000000:2800:E8E3B7AEF93E9E7B209BDB4D0D314304086A3247BD7831CFA897F174D0C3CC03.png "点击放大")

### 平板设备

**平板竖屏布局**

规则与手机一致，在标题栏使用上没有特殊规则，适配主要以拉伸适配为主，充满整个容器宽度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101815.12665494203634683029353699943140:50001231000000:2800:5430FF17CDC0CDEF39347B5AE0F942A3FD948D9EF16394D671F3712846E54424.png "点击放大")

**平板横屏分栏布局**

在一些效率型应用中，开发者为了呈现更多内容，需要对界面布局进行分栏处理。分栏布局可以通过 [NavigationMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigationmode9枚举说明) 接口能力，并配置 Split 样式属性。开发者也可以使用 Auto 属性样式来动态布局分栏规格，当窗口宽度大于等于 600vp 时，采用Split模式显示；窗口宽度小于600vp时，采用Stack模式显示。在 HarmonyOS NEXT 版本中定义了跨设备的断点式布局规格，详情可以阅读视觉规范中布局章节了解详情。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.50941458951206421543471169686404:50001231000000:2800:30947F968A73443DA5FC9EB4659AFD639D7A9D883493793BE47BDE7541777E7F.png "点击放大")

### 电脑设备

在电脑场景下，标题栏使用更小的字体提高界面信息密度，同时去掉了圆形底板。

**强调型标题栏**

主要用于一级界面突出标题区域

支持显示单行标题、双行标题

<table id="ZH-CN_TOPIC_0000001929628982__table1471675417223" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row177161354102220"><td class="row-nocellborder" style="border: none;" valign="top" width="49.94%"><p id="ZH-CN_TOPIC_0000001929628982__p18716185452215"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.29625521040167587046127130735839:50001231000000:2800:476F065429C84F6CA25819A3EB95E710D651C59DFDDEB4A8E6D5D93F8B798D3C.png" title="点击放大" width="268.1178" height="134.0589"></span>单行标题</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50.06%"><p id="ZH-CN_TOPIC_0000001929628982__p471618547223"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.36098086047336241920316965591981:50001231000000:2800:2CE196FEEBE8EE619078B8D4235823CC78501B1232F479043D51420EB6044752.png" title="点击放大" width="268.8822" height="134.4411"></span>双行标题</p></td></tr></tbody></table>

**普通型标题栏**

用于不需要突出标题的场景。当界面上方主要区域为图形化展示时，应该使用普通标题栏。

支持单行标题和双行标题两种样式。

<table id="ZH-CN_TOPIC_0000001929628982__table1417210322227" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row01721532162212"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p2172173212223"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.02492182885499441669861285182430:50001231000000:2800:39F03F84C807132C5E33D6C2CDD1E10AEFAB392D0FAEF5C05A26FD77B940A1F5.png" title="点击放大" width="268.5" height="134.25"></span>单行标题</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p7172932132219"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.80335123787314670822132514642783:50001231000000:2800:F078F201FCF85D85CE844A808B8D597F639CD2D244665655887BEE5D6BD43E1F.png" title="点击放大" width="268.5" height="134.25"></span>双行标题</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000001929628982__table101724012217" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929628982__row19181340122118"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p218mcpsimp"><strong>抽屉型标题栏</strong></p><p id="ZH-CN_TOPIC_0000001929628982__p97845505215">用于展示不同的分类，可以快捷地进行切换、查找。抽屉型在不同尺寸设备上呈现的效果略有差异，手机端为侧边遮罩层，平板端等大屏设备为分栏界面布局。通常效率型、办公类及内容型应用较为常用。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p518154011215"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.95632697058601500669545418840213:50001231000000:2800:154DA3CE7ED0B554DFA7F6210B9213C87D543FBAEBDF2CF95386D844224BE1D7.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929628982__row131819409215"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p234mcpsimp"><strong>二级页标题</strong></p><p id="ZH-CN_TOPIC_0000001929628982__p236mcpsimp">除一级界面、编辑界面和选择界面外，所有其他界面都展示二级页标题。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p1818140202117"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.70481727093125554996291274672364:50001231000000:2800:86AF9EB76A56CE4B748E80CFC0A2BD7AE1724BF6101533B10EB78F36F432B6BB.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929628982__row8181440182110"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p244mcpsimp"><strong>编辑界面</strong></p><p id="ZH-CN_TOPIC_0000001929628982__p12500181117227">当需要对界面内容进行编辑时，使用编辑界面标题栏。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929628982__p1918440202117"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.67605328641106826059047850235667:50001231000000:2800:F125B876F9F9E29FD5418A292AB2AABD12F2D088F3CD49A5318E57096464A13D.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

**普通标题栏：左侧元素**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.84456887993487229104406287439422:50001231000000:2800:4126FE87D46C392A42638B8EE49F8721B374E8C7F3893770664CE2794CB4C9C0.png "点击放大")

**普通标题栏：右侧元素**

最多同时支持 3 个图标 (含菜单)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.49024415116636288395724726621494:50001231000000:2800:6C9D084FBB0BCF6E7F62F27076FBF29D592D8E83CC88C570542FE209AEEA5486.png "点击放大")

**普通标题栏：中间元素**

支持放置工具栏、分段按钮等控件

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.75287540822630116022996564348635:50001231000000:2800:D86FC4C25037B2DCE9122D1414CD9011C3D0B5E0806101C68BB34E1E96F3CB4C.png "点击放大")

**强调型标题栏**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.61817526651913504126462768801632:50001231000000:2800:F02C5F572863EFF5CBBDD6AC08AC8EDD1C9983379186879E713BC5FA94FCF7F4.png "点击放大")

### 穿戴设备

标题栏用于指示当前页面的位置。在方表上，标题栏存在如一/二级标题栏的区分。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101816.94414729794749123615692095606049:50001231000000:2800:6D9CED84DD6595326F21925D1D3A4E8729D30FCD84E444EB4DFF2164B337C7A1.png "点击放大")

**圆形表**

**单行标题**：文字19vp，可换2行（特殊场景可不换行或换更多行），放不下则缩小字号至 18vp、15vp，还放不下则用“...”截断。

**双行标题：**文字19vp，不支持换行，文本超长则先缩小字号至18vp、15vp，最后考虑最大区域内跑马灯显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101817.23566671054958507577375073545244:50001231000000:2800:ABDEAE0DD60F7611544149AACDA2F37EDD08A0810EE63EB6ABB88F12B60B3888.png "点击放大")

**方形表**

**居中大标题栏：**适用于功能明确且内容少的首屏页面。文字24vp，可换2行（特殊场景可不换行或换更多行），放不下则缩小字号至 19vp、18vp，还放不下则用“...”截断。

**居中小标题栏：**适用于内容较多的页面。文字15vp，不可换行，放不下则缩小字号至 13vp，还放不下跑马灯显示。

**标题+时间戳：**适用于具有时效性的图表/数据页面。文字15vp，不可换行，放不下则缩小字号至 13vp，还放不下跑马灯显示。

**对称型标题栏：**适用于高频功能的分发。文字15vp，不可换行（无辅助文本可换2行），放不下则缩小字号至 13vp还放不下则用“...”截断。

**二级标题栏：**适用于二/三级页面。文字15vp，可换2行（有辅助文本不可换行），放不下则缩小字号至 13vp还放不下则用“...”截断

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250919101817.06304920715763606857899100088574:50001231000000:2800:6E87801F138A36BE571230B912896D8DDC56D70814276964463594A946A31D0D.png "点击放大")

## 开发文档

[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)

[HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation)

[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)

[HdsNavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavdestination)

[SideBarContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer)

[HdsSideBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssidebar)

[EditableTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-editabletitlebar)
