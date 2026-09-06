# 布局基础

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/design-layout-basics-0000001795579413
- 抓取时间：2026-04-04T08:22:26.486Z
布局不是静态固定的，当显示环境发生变化时，如横竖屏切换、调节字体大小、应用分屏，要及时调整内容的布局方式以适应变化。

通过调用断点系统、栅格系统、媒体查询、自适应布局和响应式布局能力就可以让内容更好地适配显示环境的变化。综合运用布局基础能力，可实现常用页面结构的多设备适配。

随着终端设备形态日益多样化，应用设计需要考虑界面安全区及避让区的属性，适配不同的屏幕尺寸、屏幕方向和设备类型。HarmonyOS在设计之初就面向全场景、全设备进行定义。系统整合了手势、基础交互、视效等维度的基础能力，确保不同终端（手机、平板、手表、IoT 设备等）的交互逻辑和视觉风格高度统一，用户无需重复学习，保证体验最优解。

**布局完整**。设备在折叠/展开或横竖屏切换时，应用窗口的组件、图片、视频等元素应避免出现错位、截断、变形、模糊等问题。

**响应式设计。**避免使用固定像素来作为界面布局或元素尺寸的定义，对于留白空间可以使用弹性布局或增加 Blank 等组件来实现动态伸缩。配合媒体查询、宽度及高度断点来进行动态判断，尽量使用流式排版来进行布局定义。

**移动优先**。将应用需要适配的设备类型或断点区间进行汇总，按照最小到最大的比例进行优先级适配，先保证最小屏幕的内容、功能及界面布局完整性后，再逐步向更大比例设备进行延展和功能适配。极端情况下，需要牺牲部分功能体验，确保最小集的完整呈现。

## 窗口状态

在 UX 设计中需要针对不同类型设备，或同一类型设备的不同状态来改变布局样式等。状态感知 (媒体查询能力) 提供了丰富的媒体特征监听能力，可以监听应用显示区域变化、横竖屏、深浅色、设备类型等等，状态感知为系统底层能力， UX 设计时只需定义在不同场景下对应的设计表现。

根据响应式布局的场景需要，支持以下四种查询类型：

### 设备类型

支持手机、平板、电脑、智慧屏、手表多设备类型查询。

在进行多端设计时需要对于一些特殊设备的布局和控件特殊定义，例如智慧屏上的按钮和 Pad 按钮的视觉样式不同，利用设备查询能力能判断当前处于什么设备，以调用对应样式的组件。

### 窗口宽度/高度

支持设备屏幕宽高查询，对于应用窗口支持自由缩放的设备，也支持应用窗口宽高的实时变换监听。

屏幕、窗口的宽高查询能力将帮助应用判断当前处于什么断点和栅格，从而判断应用架构和界面布局响应何种变化。

### 折叠屏窗口状态

支持以下折叠屏窗口状态的查询：

-   折叠方式 (内外折/上下折)
-   折痕位置
-   折叠状态 (折叠/开合)
-   悬停状态 (内折悬停/外折悬停)

### 横竖屏状态

支持横竖屏切换查询。

## 虚拟像素单位：vp

虚拟像素 (virtual pixel) 是一台设备针对应用而言所具有的虚拟尺寸 (区别于屏幕硬件本身的像素单位)。vp 是灵活的单位，它可在任何屏幕上缩放以具有统一的尺寸体量。它提供了一种灵活的方式来适应不同屏幕密度的显示效果。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150016.91935573363271092828366871224951:50001231000000:2800:4B4C132EEED4C0A881C64AD8C695FADFAEAA0D0B7E780F94AF654FB75A925444.png "点击放大")

使用虚拟像素，使 UI 元素在不同密度的设备上具有一致性大小视觉感受

## 字体像素单位：fp

字体像素 (font pixel)默认情况下与 vp 相同，即默认情况下 1 fp = 1vp。如果用户在设置中选择了更大的字体，字体的实际显示大小就会在 vp 的基础上乘以 scale 系数，即 1 fp = 1 vp \* scale。

## 8vp 网格系统

基于 8vp 为网格的基本单位可以对 UI 界面上元素的大小，位置，对齐方式进行更好的规划，可以构建更有层次感、秩序感，以及多设备上一致的布局效果。一些更小的控件，例如图标大小也可以对齐 4vp 的网格大小。

## 断点系统

断点以应用窗口宽度和宽高比信息为参照，在宽度和宽高比的维度上分成了几个不同区间 (即不同的断点)。当窗口宽度和宽高比从一个断点变化到另一个断点时，可根据 UX 设计方案实现不同的页面布局效果 (如将页面内容从单列排布调整为双列排布甚至三列排布等) ，以获得更好的显示效果。

在应用进入分屏或多窗模式时，窗口尺寸应为分屏或多窗后的窗口尺寸。

**断点的设计原理**

提升全场景体验，需考虑多种窗口变化连续性。应用页面布局设计时推荐遵循以下原则：

-   原则一：两个宽度相近的窗口，页面布局应相同。
-   原则二：高度相对宽度较小的窗口，可根据宽高比信息来进行横向窗口或类方形窗口的页面布局差异化设计。

因此，系统设计了横向和纵向断点分别代表窗口的不同特征，作为判断页面布局和交互体验的条件：

-   横向断点以窗口宽度值区分，代表窗口宽度实际大小，会影响用户使用和观看的物理尺寸。
-   纵向断点以窗口宽高比区分，代表窗口相对高度，表示横向比例、方形或纵向比例窗口。

**窗口断点**

根据断点系统划分了几种不同的窗口形态范围。通过窗口的宽度及宽高比可以判断当前在哪个断点区间，并切换相对应的应用架构或布局以符合当前窗口交互特征。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150016.09143976312650241893659728445436:50001231000000:2800:3C5772DFCF0AC73843E75C59059DDDCF14CCA5427DE07A3410F40D439641CE37.png "点击放大")

## 栅格系统

栅格系统是一个多设备下通用的辅助定位系统，栅格给布局提供一种可循的规律，解决多尺寸多设备的动态布局问题。保证各模块各设备的布局一致性。栅格会跟随屏幕尺寸、窗口尺寸、子容器尺寸的变化而动态变化。

**栅格构成**

栅格系统有 Margins (边距) ，Gutters (间距) ， Columns (栅格) 三个属性。

**Margins (边距)：**

Margin 是元素相对窗口左右边缘的距离，决定了内容可展示的整体宽度，是用来控制元素距离屏幕最边缘的距离关系，可以根据不同的窗口容器尺寸定义不同的 Margin 值。

**Gutters (间距)：**

Gutter 是每个 Column 的间距，控制元素和元素之间的距离关系，决定内容间的紧密程度，可以根据不同的窗口容器尺寸定义不同的 Gutters 值，为了保证较好的视觉效果，Gutters 通常的取值不会大于 Margins 的取值。

**Columns (栅格)：**

Column 是内容的占位元素，其数量决定了内容的布局复杂度，Columns 的宽度在保证 Margins 和 Gutters 符合规范的情况下，根据实际窗口的宽度和 Columns 数量自动计算每一个 Columns 的宽度。不同的窗口容器尺寸匹配不同的 Columns 数量来辅助布局定位。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150016.16067892736761985923190070186897:50001231000000:2800:B66AC97BD370F0DD745CDEDEA514309F826FB58E4C0B4685BB0E6A9D6FBEF423.jpg "点击放大")

**窗口栅格**

窗口栅格系统是系统提供的一种面向多设备高效适配的辅助布局的定位工具。系统将根据窗口容器的水平宽度自动匹配最佳的栅格数量，以达到内容布局的最佳适应。

0 <= 水平 vp < 600 时：4 Columns 栅格；

600 <= 水平 vp < 840 时：8 Columns 栅格；

840 <= 水平 vp 时：12 Columns 栅格；

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150017.46376187342308981032553041940743:50001231000000:2800:346638C12C7F81C10914305299A5B5F3BC4E0871926E82477E59AD2D0C09C622.png "点击放大")

栅格定义：

1.  通用型：margin= 16vp，gutter=8vp，column=4 ；宽松型：margin= 16vp，gutter=16vp，column=4
2.  margin=24vp，gutter=12vp，column=8
3.  margin=32vp，gutter=16vp，column=12
4.  margin=32vp，gutter=20vp，column=12

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150018.87542798436103292031802041598598:50001231000000:2800:2326F8A8802E65A8CBA8B26473AB74A3185FD4C67F49CA8ADFED534BC204790E.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150018.17098067290514887761656363174589:50001231000000:2800:F5CC55B2A98A093121C398F8615484F443688F80E1A1CD470E4820DF2D7B9D8D.png "点击放大")

栅格最大使用宽度：

最大使用宽度为 2220vp，当窗口不断拉宽大于 2220vp 时，栅格内的内容区范围不再变化，多出的区域左右留白。

## 系统安全区

安全区定义了界面可完整显示的区域，确保在安全区内的内容不会被硬件挖孔、圆角等因素截断或遮盖。

### 手机

基于默认布局规则，手机上需避让顶部信号栏、底部导航条安全区、与两侧margin，有需要时预留键盘占据的空间，考虑安全区的嵌入后能最大化信息的展示效率，使用户感知到应用界面为一个整体。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150018.29602768400193925670126995892794:50001231000000:2800:B47D396A48BCA802B1DF35543F3231629BD106DFD6D6B7B9FA15140761070F6B.png "点击放大")

当屏幕中包含多个窗口时，如图示窗口高度比例2:1、1:1、与存在悬浮窗的场景，用户难以看清靠近边缘的内容，应考虑在窗口内居中放置主要内容，并避免过于紧凑的界面布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150018.28662707507046876021261656551691:50001231000000:2800:DAFB8938FD1F91383716B6A5AE72D886DAA43AB74748F21C82EF2CA8CB89FBE3.png "点击放大")

### 折叠设备

除顶部信号栏与底部导航条以外，需避免将关键信息放置在折叠设备的转轴区（即折痕处），便于悬停态适配，详情请参阅[悬停态](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-0000002352875141#section183378919119)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150019.34727756857697737914005890105283:50001231000000:2800:D2A015F6298394602153120C0DE8123D5BB3CE31BE7CA3F548F2F36561376EE7.png "点击放大")

折叠设备呈展开态并存在多个窗口时，需考虑分屏布局，使关键信息易识别，核心操作易于使用。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150019.57195584212464545176004409475606:50001231000000:2800:F3B04C2949932EA89848B7EEC169DA647A30600E4152F2B2A853B2F7A03C5B39.png "点击放大")

### 平板

平板基础布局需避让顶部信号栏、底部导航条安全区、与两侧margin（根据断点规则计算）。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150019.58202166918295067096728917640120:50001231000000:2800:44DE4512790D2813153F65EB032703010E87C50A6F6D7FB1DE72A390F106D1EF.png "点击放大")

平板布局应额外考虑横排状态下窗口宽度比例1:2，1:1，与2:1分屏浏览的情况。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150019.78170294729432049513188167517118:50001231000000:2800:0B81DC79DF4280F1B236C333687DC172F784D11DC77A2678F27CDC35ABDAFB2C.png "点击放大")

### 智能穿戴

智能穿戴产品的信息布局需要根据设备为圆表或方表，以及当前应用的实际内容进行设计。避让水平屏幕边缘间距的同时，在不同的界面架构中，需要考量垂直布局额外进行避让，详情请见[间隔参数](https://developer.huawei.com/consumer/cn/doc/design-guides/spacing-parameters-0000002202912577)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150020.15676961539119628085179087195140:50001231000000:2800:E8C766022AE58837062E708DCCFAB763C0E3F258EDEE9B1068E097F070A15FFB.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250926150020.14815216439246750921426283482623:50001231000000:2800:17ED640A46201B5E3FE0A776D42EF63E28E997EA61A396EFCA559289253AA992.png "点击放大")

## HarmonyOS 设备屏幕尺寸

**手机**

<table id="ZH-CN_TOPIC_0000001795579413__table123221533125611" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795579413__row203882336566"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p138811332561"><strong>机型</strong></p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p8388183315566"><strong>尺寸px</strong></p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p1238833365611"><strong>尺寸vp</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row2388833135616"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p1038819337564">Mate 60</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p23881933195614">1216x2688</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p138873312569">374x826</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row53881533185619"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p1738893315613">Mate 60 Pro</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p1638823318564">1260x2720</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p938893313566">388x836</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row11388153335620"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p8388033145613">Mate 70</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p1738813355610">1216x2688</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p7388143375613">374x826</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row1838873310566"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p18388833105615">Mate 70 Pro</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p138817336569">1316x2832</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p638843314561">376x810</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row1038810336567"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p1338963385619">Pura 60</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p138933315615">1220x2700</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p103899335566">376x830</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row1738953319565"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p17389143317566">Pura 60 Pro</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p5389033165617">1220x2700</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p183891533135615">376x830</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row11389133145611"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p4389103325611">Pura 70</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p18389633165611">1256x2760</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p16389183318567">358x788</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row538953385618"><td class="cellrowborder" valign="top" width="32.910000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p538933395617">Pura 70 Pro</p></td><td class="cellrowborder" valign="top" width="33.97%"><p id="ZH-CN_TOPIC_0000001795579413__p143899334566">1260x2844</p></td><td class="cellrowborder" valign="top" width="33.12%"><p id="ZH-CN_TOPIC_0000001795579413__p153891033155612">360x812</p></td></tr></tbody></table>

**折叠屏**

<table id="ZH-CN_TOPIC_0000001795579413__table1330113311565" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795579413__row19389153319566"><td class="cellrowborder" valign="top" width="32.41675832416758%"><p id="ZH-CN_TOPIC_0000001795579413__p8389163310566"><strong>机型</strong></p></td><td class="cellrowborder" valign="top" width="33.896610338966106%"><p id="ZH-CN_TOPIC_0000001795579413__p4389113315563"><strong>尺寸px</strong></p></td><td class="cellrowborder" valign="top" width="33.68663133686631%"><p id="ZH-CN_TOPIC_0000001795579413__p1038963325620"><strong>尺寸vp</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row123891233195617"><td class="cellrowborder" valign="top" width="32.41675832416758%"><p id="ZH-CN_TOPIC_0000001795579413__p638963375610">Mate X5</p></td><td class="cellrowborder" valign="top" width="33.896610338966106%"><p id="ZH-CN_TOPIC_0000001795579413__p03899331566">1080x2504</p></td><td class="cellrowborder" valign="top" width="33.68663133686631%"><p id="ZH-CN_TOPIC_0000001795579413__p1338933365618">346x802</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row1538914339566"><td class="cellrowborder" valign="top" width="32.41675832416758%"><p id="ZH-CN_TOPIC_0000001795579413__p193899332566">Mate X5-展开</p></td><td class="cellrowborder" valign="top" width="33.896610338966106%"><p id="ZH-CN_TOPIC_0000001795579413__p138943335620">2224x2496</p></td><td class="cellrowborder" valign="top" width="33.68663133686631%"><p id="ZH-CN_TOPIC_0000001795579413__p20389123315617">712x798</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row73891733205616"><td class="cellrowborder" valign="top" width="32.41675832416758%"><p id="ZH-CN_TOPIC_0000001795579413__p238963320564">Mate XT</p></td><td class="cellrowborder" valign="top" width="33.896610338966106%"><p id="ZH-CN_TOPIC_0000001795579413__p2038913312567">1008x2232</p></td><td class="cellrowborder" valign="top" width="33.68663133686631%"><p id="ZH-CN_TOPIC_0000001795579413__p93891433145615">350x776</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row123891733105618"><td class="cellrowborder" valign="top" width="32.41675832416758%"><p id="ZH-CN_TOPIC_0000001795579413__p11389133310569">Mate XT-双折展开</p></td><td class="cellrowborder" valign="top" width="33.896610338966106%"><p id="ZH-CN_TOPIC_0000001795579413__p10389123315615">2048x2232</p></td><td class="cellrowborder" valign="top" width="33.68663133686631%"><p id="ZH-CN_TOPIC_0000001795579413__p15389163317560">712x776</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row1538963318567"><td class="cellrowborder" valign="top" width="32.41675832416758%"><p id="ZH-CN_TOPIC_0000001795579413__p2389833105615">Mate XT-三折展开</p></td><td class="cellrowborder" valign="top" width="33.896610338966106%"><p id="ZH-CN_TOPIC_0000001795579413__p23891133195617">3184x2232</p></td><td class="cellrowborder" valign="top" width="33.68663133686631%"><p id="ZH-CN_TOPIC_0000001795579413__p1389233195616">1108x776</p></td></tr></tbody></table>

**小折叠**

<table id="ZH-CN_TOPIC_0000001795579413__table183342330562" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795579413__row1539073317567"><td class="cellrowborder" valign="top" width="32.42%"><p id="ZH-CN_TOPIC_0000001795579413__p539011336566"><strong>机型</strong></p></td><td class="cellrowborder" valign="top" width="34.11%"><p id="ZH-CN_TOPIC_0000001795579413__p5390163315568"><strong>尺寸px</strong></p></td><td class="cellrowborder" valign="top" width="33.47%"><p id="ZH-CN_TOPIC_0000001795579413__p539013345615"><strong>尺寸vp</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row439023335619"><td class="cellrowborder" valign="top" width="32.42%"><p id="ZH-CN_TOPIC_0000001795579413__p1139083335611">Pura X</p></td><td class="cellrowborder" valign="top" width="34.11%"><p id="ZH-CN_TOPIC_0000001795579413__p139053320562">980x980</p></td><td class="cellrowborder" valign="top" width="33.47%"><p id="ZH-CN_TOPIC_0000001795579413__p1439063317567">326x326</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row183901633135611"><td class="cellrowborder" valign="top" width="32.42%"><p id="ZH-CN_TOPIC_0000001795579413__p53903336563">Pura X-展开</p></td><td class="cellrowborder" valign="top" width="34.11%"><p id="ZH-CN_TOPIC_0000001795579413__p11390133155620">1320x2120</p></td><td class="cellrowborder" valign="top" width="33.47%"><p id="ZH-CN_TOPIC_0000001795579413__p143907333568">440x706</p></td></tr></tbody></table>

**平板**

<table id="ZH-CN_TOPIC_0000001795579413__table8336203365611" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795579413__row539023395616"><td class="cellrowborder" valign="top" width="33.050000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p143906338561"><strong>机型</strong></p></td><td class="cellrowborder" valign="top" width="33.69%"><p id="ZH-CN_TOPIC_0000001795579413__p2390183313569"><strong>尺寸px</strong></p></td><td class="cellrowborder" valign="top" width="33.26%"><p id="ZH-CN_TOPIC_0000001795579413__p17390143395612"><strong>尺寸vp</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row839016335569"><td class="cellrowborder" valign="top" width="33.050000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p173901533185618">MatePad</p></td><td class="cellrowborder" valign="top" width="33.69%"><p id="ZH-CN_TOPIC_0000001795579413__p1639083315610">2560*1600</p></td><td class="cellrowborder" valign="top" width="33.26%"><p id="ZH-CN_TOPIC_0000001795579413__p1939053375615">1280x800</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row439033335618"><td class="cellrowborder" valign="top" width="33.050000000000004%"><p id="ZH-CN_TOPIC_0000001795579413__p73901833195614">MatePad Pro</p></td><td class="cellrowborder" valign="top" width="33.69%"><p id="ZH-CN_TOPIC_0000001795579413__p14390143365616">2880*1920</p></td><td class="cellrowborder" valign="top" width="33.26%"><p id="ZH-CN_TOPIC_0000001795579413__p19390153335612">1440x960</p></td></tr></tbody></table>

**PC**

<table id="ZH-CN_TOPIC_0000001795579413__table163381533165619" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795579413__row1139073385618"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p5390193375619"><strong>机型</strong></p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p1039013315565"><strong>尺寸px</strong></p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p133901433105619"><strong>尺寸vp</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row6390143305613"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p1390133155620">MateBook Pro</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p19390133115616">2080x3120</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p133907333567">1094x1642</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row8390123375620"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p23904331561">MateBook Fold</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p0390193316567">1648x2472</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p839073315569">916x1374</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row639013318563"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p1539033395615">MateBook Fold-展开</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p1839193313563">3296x2472</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001795579413__p339113318565">1832x1374</p></td></tr></tbody></table>

**穿戴**

<table id="ZH-CN_TOPIC_0000001795579413__table1034015338564" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795579413__row13391133185616"><td class="cellrowborder" valign="top" width="32.2%"><p id="ZH-CN_TOPIC_0000001795579413__p203911332569"><strong>机型</strong></p></td><td class="cellrowborder" valign="top" width="33.900000000000006%"><p id="ZH-CN_TOPIC_0000001795579413__p539183365619"><strong>尺寸px</strong></p></td><td class="cellrowborder" valign="top" width="33.900000000000006%"><p id="ZH-CN_TOPIC_0000001795579413__p1391143335614"><strong>尺寸vp</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row839110335565"><td class="cellrowborder" valign="top" width="32.2%"><p id="ZH-CN_TOPIC_0000001795579413__p1339193315568">圆表</p></td><td class="cellrowborder" valign="top" width="33.900000000000006%"><p id="ZH-CN_TOPIC_0000001795579413__p639133315566">466x466</p></td><td class="cellrowborder" valign="top" width="33.900000000000006%"><p id="ZH-CN_TOPIC_0000001795579413__p2391233195614">233x233</p></td></tr><tr id="ZH-CN_TOPIC_0000001795579413__row939193318562"><td class="cellrowborder" valign="top" width="32.2%"><p id="ZH-CN_TOPIC_0000001795579413__p1939123313564">方表</p></td><td class="cellrowborder" valign="top" width="33.900000000000006%"><p id="ZH-CN_TOPIC_0000001795579413__p1039173375616">408x480</p></td><td class="cellrowborder" valign="top" width="33.900000000000006%"><p id="ZH-CN_TOPIC_0000001795579413__p11391133319566">204x240</p></td></tr></tbody></table>
