# 概述

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/practices-overview-0000001746498066
- 抓取时间：2026-04-04T08:24:53.558Z
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185316.91668645367313560741300840893812:50001231000000:2800:8E5C66E490998572B457D60650994FD1D1038085BB6C126BB3049DC8C95C14B0.png "点击放大")

随着终端设备形态日益多样化，应用设计需要考虑界面能适配不同的屏幕尺寸、屏幕方向和设备类型。同时还需要保持多设备体验的连续性，改善多端独立的设计、尽可能降低开发者的工作量和维护成本。基于此 Harmony OS 为设计师提供了面向多设备的设计指南，让设计师在进行多端设计时有一套科学的方法，最大限度地减少设计的工作量，保障多端设计在一定程度的一致性。同时 Harmony OS 也提供了对应的技术能力，帮助开发者快速地进行多端应用设计。

本指南结合用户在多端设备上的历史交互习惯、各场景下的使用诉求等，进行了一些设计方法的总结，主要包括如下几个部分：

-   基础要求：在多设备应用设计中需要遵守的基础体验要求，如果不满足基础要求，则会极大损害用户的使用体验。
-   响应式布局：针对部分常见的界面元素提出了宽屏设备上的响应式布局设计范式，避免简单拉伸、放大等导致的一些体验问题。
-   增值体验：在多设备应用设计中可以考虑更多体验上的变化，在合适的场景下提供增值的体验
-   场景化设计参考：针对具体垂类场景应用给出了场景内典型页面的设计建议，方便设计师进行更有针对性的参考和选用。

## 基础要求

-   导航适配
-   横竖屏&挖孔适配
-   多窗适配
-   弹出框适配
-   键鼠适配
-   体验评估标准

### 导航适配

**底部导航&侧边导航**

通常手机和折叠屏使用底部页签导航；平板及其他宽屏设备使用侧边页签或侧边栏导航。调用鸿蒙系统提供的控件可自动适配该导航规则。

底部导航&侧边导航的详细设计规范，请参阅[典型布局场景 - 页签栏](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-page-layout)。

<table id="ZH-CN_TOPIC_0000002330924398__table282mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row286mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p179392411710"><span><img originheight="2160" originwidth="5404" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185316.89597529443604232538073512870263:50001231000000:2800:D823EFC2557E0E299A5E28C1613A92E4D5594E59E1D706CFE45F041EEE8BDDF7.jpg" title="点击放大" width="587" height="234.62620281273132"></span></p></td></tr></tbody></table>

**底部导航条适配**

移动端设备应用内的底部页签、底部工具栏、底部文本，或底部悬浮按钮需要自动抬高避让底部导航条。应用内的可滚动内容，可直接显示在导航条下方，仅当滚动到内容的最底部时需要向上抬高避免被底部导航条遮挡。调用鸿蒙控件，可自动实现以上导航条的避让规格。

沉浸式页面，例如全屏播放视频、游戏、阅读等场景下，超过 2 秒自动隐藏底部导航条，从底部上滑或从顶部下滑可触发恢复显示底部导航条。导航条适配规范&开发指南，请参阅 [系统特性 - 导航条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185316.75094477088483557055697098432219:50001231000000:2800:8DCA7B55AA6331212DBF7ED03D8BC6502DE59571E0FA9611137EC1A0B46A7C10.png "点击放大")

### 横竖屏&挖孔适配

手机和折叠屏折叠态的应用通常需要适配竖屏布局。仅部分特殊场景例如横屏游戏、长视频需要适配横屏布局。

折叠屏展开态、平板上，应用需要同时适配横屏和竖屏布局。

当设备尺寸比例接近 1:1 时，建议横竖屏使用相同或相近的布局；

当设备尺寸比例差异大时，横竖屏可以使用不同的布局，从而提供更好的使用体验，例如横屏后自动分栏或横屏后自动露出右侧的辅助信息等。

横竖屏适配过程中，需要考虑核心内容或重要交互不要被挖孔区遮挡，如果被遮挡则进行局部内容等避让；可滚动内容或非核心信息无需专门避让挖孔区；要避免因为避让挖孔导致左右侧留白不一致。

<table id="ZH-CN_TOPIC_0000002330924398__table297mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row301mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p13805781616"><span><img originheight="1588" originwidth="4420" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185316.60924163720165018709650924985037:50001231000000:2800:FDF1823A2C833E92BB2DB02519B29CB965FC389086D3999AB88F44A7061D59ED.png" title="点击放大" width="587" height="210.89502262443438"></span></p></td></tr></tbody></table>

### 多窗适配

手机和折叠屏折叠态，应用需要适配竖向悬浮窗、上下分屏。仅部分特殊场景例如横屏游戏、长视频，需要适配横向悬浮窗。折叠屏展开态，在以上基础外还需要适配上下分屏。

平板及更宽的设备上 ，应用需要适配自由窗口 (即可任意拖大、拖小、拖宽、拖窄) ，横屏时支持左右分屏，竖屏时支持上下分屏，且支持分屏比例的自由调节。

在多端设备上，长视频、直播、会议、通话等场景，需要支持画中画。多窗的适配设计规范，请参阅[智慧多窗应用适配指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-guide)。

<table id="ZH-CN_TOPIC_0000002330924398__table306mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row310mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p69312030151714"><span><img originheight="1165" originwidth="4096" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185317.64844434467792911244696448406447:50001231000000:2800:ABF985CE968BE0331028A0C19816E7C8DB541EC0B7F2ED87C8CA6A9053791AD3.png" title="点击放大" width="587" height="166.956787109375"></span></p></td></tr></tbody></table>

### 弹出框适配

建议调用系统的弹出框控件，避免在宽屏设备上弹出框过宽或过高的问题。

若应用自定义弹出框尺寸，则建议在 8 栅格及以上的设备上，弹出框最宽不超过400vp ；宽屏设备上弹出框的物理高度不超过手机上的该弹出框高度的 1.5 倍。

### 键鼠适配

平板及更宽的设备上的应用需要进行基础的鼠标、键盘等适配。详细的人机交互要求和适配规则，请参阅 [人机交互](https://developer.huawei.com/consumer/cn/doc/design-guides/hmi-overview-0000001795410269)。

### 体验评估标准

UX 体验的基础要求和评估标准，请参阅 [应用UX体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-overview-0000001760867048)。

## 响应式布局

应用内的页签、搜索、入口图标、广告图、列表、卡片、图片、内容模块等可以灵活地通过形变、延伸布局、重复布局、挪移布局、宫格布局、瀑布流布局等进行宽屏设备上的响应式适配，以达到最佳的信息量和舒适的浏览体验。

布局相关的设计规则，请参阅[响应式布局](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout)。

-   子页签&搜索
-   入口图标
-   广告图
-   列表
-   卡片
-   详情大图
-   内容模块

### 子页签&搜索

手机和折叠屏折叠态，搜索和子页签分两排显示。

折叠屏展开态、平板及更宽的设备上 等 ，子页签和搜索可以同一排显示，搜索框根据子页签数量的多少而自适应调整长度。

<table id="ZH-CN_TOPIC_0000002330924398__table104mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row108mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p18181142501812"><span><img originheight="1624" originwidth="10808" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185317.89412439297160594542437820462867:50001231000000:2800:76A4214A4903BF294222CCC6CBB61A687AF93478EE45F78F67F56A6262A1CB43.png" title="点击放大" width="587" height="88.20207253886011"></span></p></td></tr></tbody></table>

### 入口图标

在多端设备上，建议 1 行显示的入口图标数量限制在一定范围内。例如在折叠屏和平板竖屏上一排图标不超过 8 个，在平板横屏上一排图标不超过 13 个，要避免一排图标过多导致信息过密。

<table id="ZH-CN_TOPIC_0000002330924398__table112mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row116mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p1610452191818"><span><img originheight="752" originwidth="4096" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185317.78267215667693011070649996290019:50001231000000:2800:B63E87486954257DBD9AB3EBF377E000A733E052C481CB49CBE3476EB447FCE0.png" title="点击放大" width="587" height="107.76953125"></span></p></td></tr></tbody></table>

### 广告图

**卡片广告**

在宽屏设备上建议使用延伸布局和形变进行卡片广告的响应式适配。

例如手机上一张广告卡片，在折叠屏可显示两张广告卡片，在平板显示三张广告卡片。同时基于各端的物理尺寸可进行广告卡片的自适应形变，在宽屏设备上广告卡片更长，在窄屏设备上广告卡片更高。

<table id="ZH-CN_TOPIC_0000002330924398__table122mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row126mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p18669441181911"><span><img originheight="2156" originwidth="10808" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185317.22253590805195297077345728595833:50001231000000:2800:521BB3B82C8032E7CBE7AF33621CC76C1E198813D23D0C3560A2CA8490D33318.png" title="点击放大" width="587" height="117.0958549222798"></span></p></td></tr></tbody></table>

**沉浸广告**

音视频等应用，为提供更沉浸的影音娱乐体验，可使用沉浸广告图效果。

应用使用沉浸广告时，建议沉浸广告的背景和广告内容元素分为多个图层，且为宽屏设备提供更长的背景图，或通过智能裁剪为不同宽度的设备裁剪出合适高度的背景图。保持背景图横向铺满整个设备宽度，且要避免背景图过高。广告的图片、文本等内容元素在宽屏设备上响应式布局。

<table id="ZH-CN_TOPIC_0000002330924398__table131mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row135mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p4429172219201"><span><img originheight="1600" originwidth="5656" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185318.52327345814896740235364291225858:50001231000000:2800:C6B8F2AC16DA5CD115C8281C4D245D374C00D6BFD8653383BAC1B62784DD13AA.png" title="点击放大" width="587" height="166.05374823196607"></span></p></td></tr></tbody></table>

金融理财、生活服务等类型的应用也经常使用沉浸广告图打造更好的营销氛围。需要考虑为多端提供一个适宜的沉浸广告高度，避免在宽屏设备上等比放大导致整个广告过高，导致首屏的信息量过少。

折叠屏和平板横屏时，建议沉浸广告图不超过 0.5 倍的屏幕高度，平板竖屏时建议沉浸广告图不超过 0.4 倍的屏幕高度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185318.48440120038509189457145638299904:50001231000000:2800:523E229C2D348040791B1864BE077A1D25DA2523E9F74B61DCE01340E57101EE.png "点击放大")

### 列表

**列表的重复布局**

在宽屏设备上，为避免结构过于单调且信息量过少，可通过重复布局来改善页面的浏览舒适度和使用效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185319.86644496647741098054355293046203:50001231000000:2800:635F8CCF3149CFA198500FED823B59325A8C41951B2ADA8F8E54292E23E5CA98.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185319.97218168182434887522198132036662:50001231000000:2800:834848DDB4636C233B6375F3B7C4E0A104F9D1B2D7826BD3A90B30AEA34ABEF9.png "点击放大")

**列表的挪移布局**

列表结构中的大视频或单张大图片，在宽屏设备上也可以通过图文挪移布局来避免视频或图片显示过大。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185319.76202823370858719814208584384716:50001231000000:2800:E5A0B4FF1CD11E9EB139D8BE7A4AF2A7D9EF3214D7A0A9232090E8EA2E0AF88E.png "点击放大")

**列表变瀑布流或宫格**

可以通过从列表到宫格或瀑布流的布局变化，带来宽屏设备上更舒适的增值阅读体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185319.93526189370550497902323432378353:50001231000000:2800:05C7F2C8BC4845CAD0322A14E76255DA4A9107FCFFBDC80F51EB71B035E951ED.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185319.16133939246712879873707299620570:50001231000000:2800:C3BF64EAFFDF80821A4AEC01FA6ADE583B0896BB018D9CFD44A44A86CEB1E968.png "点击放大")

### 卡片

手机上的单列的卡片，在宽屏设备上，通过分栏 + 瀑布流/宫格布局的方式进行显示适配，提升浏览效率且提供舒适布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185320.69279842095994590506834929151786:50001231000000:2800:2FDDA8F6AF888B3CA4A11D5892C3A68D43ADA399B3A96190D54D8376B7440643.png "点击放大")

### 详情大图

在宽屏设备上，页面内的大图可以通过延伸布局或挪移布局进行适配。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185320.83900716369291460539364269307695:50001231000000:2800:8EED8A873D572C5DE3BC18D1FF839FD06D5EFD31B6BD48C70DED30EEA06E4ABA.png "点击放大")

### 内容模块

同一个设备上，也可以根据多个模块的内容尺寸进行自适应的挪移布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185320.96048735115542789082591743137389:50001231000000:2800:A741A77C75EA61B1B10F27E7B4652050FBF1D749440D1D7F18249BC43F351685.png "点击放大")

## 增值体验

1.  沉浸体验：沉浸广告、沉浸浏览、沉浸观影
2.  高效体验：分栏、应用内分屏、缩放
3.  轻交互：浅层窗口、临时双窗、长按预览
4.  跟手交互：跟手弹框、跟手输入
5.  悬停体验：悬停适配、悬停创新

### 沉浸体验

**沉浸广告**

音视频等应用，为提供更沉浸的影音娱乐体验，或电商购物、金融理财、生活服务等应用为营造营销氛围感，可使用沉浸广告图效果。使用沉浸广告图时，广告图的背景和广告内容元素需要分层，并根据设备的屏幕宽度进行自适应布局。

<table id="ZH-CN_TOPIC_0000002330924398__table156mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row160mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p018104017249"><span><img originheight="1600" originwidth="5656" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185321.05645054894604633014548651331431:50001231000000:2800:93E8B06533FF8CEC519F84109D5DA5D2BA6E29B2459EA2B50DA567FCDCF4E4E2.png" title="点击放大" width="587" height="166.05374823196607"></span></p></td></tr></tbody></table>

**沉浸浏览**

新闻阅读、社交资讯、生活服务、电商、办公等类型的内容，在详情页浏览内容时，可以通过上滑隐藏标题栏、工具栏，下滑或停留超过一定时长恢复显示标题栏、工具栏的方式，提供更沉浸的浏览体验。

<table id="ZH-CN_TOPIC_0000002330924398__table165mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row169mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p161704817305"><span><img originheight="2160" originwidth="4320" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185321.34616026495524712064326111065996:50001231000000:2800:3D17A48CBE9FAD4612DDBB6983FF5730E3E0E1D07B287839DD50FB3A39576A9A.png" title="点击放大" width="587" height="293.5"></span></p></td></tr></tbody></table>

**沉浸观影**

全屏播放视频时，建议提供以下两种体验。

1 ) 减少屏幕旋转。例如在接近方形的折叠屏上，点击全屏播放按钮时，需要避免屏幕旋转导致的观影体验中断。

2 ) 减少弹幕对视频内容的遮挡。例如当屏幕内有黑边时，尽量在上方的黑边显示弹幕，当屏幕内没有黑边时，需要避免弹幕显示过多导致严重影响观影体验。

<table id="ZH-CN_TOPIC_0000002330924398__table178mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row182mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p2015872012186"><span><img originheight="1521" originwidth="4606" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185321.52531925171829256547323309797143:50001231000000:2800:16346E0CEAD209DC20327491AF68A597E060D0BA85FF26932A1B18AA683231B0.png" title="点击放大" width="587" height="193.83999131567518"></span></p></td></tr></tbody></table>

### 高效体验

**分栏**

8 栅格以上的设备可支持分栏，适用的设备包括手机横屏、折叠屏、平板及更宽的设备上 等。

办公类、效率型、IM 社交类应用适用于分栏布局，例如自研应用中的邮件、日历、备忘录、文件管理、设置、短信、畅连、联系人等。金融类、电商购物类部分页面，也可以通过分栏提升宽屏上的使用效率。

分栏布局时，允许应用内通过点击“全屏”按钮，从分栏切换至临时全屏或点击“缩小”按钮，从临时全屏恢复分栏。

分栏设计规范，请参阅[响应式应用架构](https://developer.huawei.com/consumer/cn/doc/design-guides/design-responsive-layout-structure-0000001748539684)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185321.90600836745451109044448479756606:50001231000000:2800:B08D91E57EBCE55AEDE05FE802A74AFAEFA1FDC2B74C10E9BC48E5B63641618D.png "点击放大")

**应用内分屏**

文档编辑、阅读、购物、IM 对话、通话等场景，通常需要进行多个内容对比或多个任务协同。

此类场景下，建议通过页面内的“分屏”按钮触发任务分屏。形成分屏后，“分屏”按钮自动切换为“全屏”按钮，点击“全屏”按钮，即退出另一侧的分屏任务，让当前焦点所在的任务回到全屏。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185322.54843916603432159877896067026826:50001231000000:2800:DAA93B9ADB6FD011EDD794B496664D90AE046094E871182D272953C46135777A.png "点击放大")

**缩放**

瀑布流或宫格布局，建议支持通过双指缩放进行布局列数的调整，从而满足效率型和大图浏览型的不同用户诉求。

新闻详情、网页详情、笔记、文档等图文阅读类页面，建议支持通过双指缩放调整文字大小。

双指缩放的设计规范，请参阅[人机交互 - 手势](https://developer.huawei.com/consumer/cn/doc/design-guides/hmi-touchscreen-0000001928273206)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185322.11749954975039205811572541773515:50001231000000:2800:6CC35AEE8F2119BD9E621CDE6AE27DE70FBD2C2AECFCB72B2B9F6D0964DD2E6B.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185323.54335293130074416264986370607529:50001231000000:2800:1F8C75971272D712626296CD540D5180E4445E8A0CE47BF8EACACF0E7C2D8C7C.png "点击放大")

### 轻交互

**浅层窗口**

简单的新建、筛选、添加、浏览，或临时的支付、登录、设置等页面，可以通过浅层窗口避免在宽屏设备上大幅度的页面跳转带来的体验中断。应用可根据自身业务诉求考虑需要调用半模态控件的场景，并选择适合的半模态控件，从而达到浅层窗口的体验。可根据业务特性，采用以下三种浅层窗口样式中的一种。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185323.74772643027129727741931136127172:50001231000000:2800:2CA203A2C326AEBCA7CDCD9691422CF0D4F3F206218AAA8F1B3DBC84F964C093.png "点击放大")

<table id="ZH-CN_TOPIC_0000002330924398__table220mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row224mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p3867134412245"><span><img originheight="1521" originwidth="4178" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185323.57832994749663984096416308467615:50001231000000:2800:94674B34C96D13D35B9FF42513444F990A059A7DBB7A349B7E269064F3985C86.png" title="点击放大" width="587" height="213.69722355193872"></span></p></td></tr></tbody></table>

**侧边面板**

除浅层窗口外，在购物、浏览图片、浏览短视频、查看长视频等场景，可通过侧边面板实现边看边评、边看边买等便捷任务处理的轻交互体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185323.68151631988491165844060119607881:50001231000000:2800:772B3E9895F27092C02AC5C013AF0E5B90595E370F174AB923985B0E02843788.png "点击放大")

**长按预览**

系统提供了长按预览的控件能力，接入控件后可以针对视频、附件等卡片实现长按预览播放、长按预览查看详情的体验，且可以在菜单中加入常用功能。

长按预览菜单的设计规范，请参阅[人机交互 - 手势](https://developer.huawei.com/consumer/cn/doc/design-guides/hmi-touchscreen-0000001928273206)。

<table id="ZH-CN_TOPIC_0000002330924398__table236mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924398__row240mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924398__p15481111924215"><span><img originheight="2160" originwidth="4320" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185323.34508405248165385151189148087600:50001231000000:2800:11074CE2D19374EC943AFEDB4AE2316D7DBA195D63DA1370BEE3C483F89A4D9A.png" title="点击放大" width="587" height="293.5"></span></p></td></tr></tbody></table>

### 跟手交互

**跟手弹框**

折叠屏展开态和平板的屏幕尺寸较大，弹出框上的操作按钮不易触达。建议针对折叠屏展开态、平板等大尺寸的设备，提供跟手的弹出框。

跟手弹出框需要满足以下条件：

1 ) 仅适用于宽度和高度均>= 8 栅格的设备。

2 ) 是点击顶部，或底部的标题栏/工具栏上的图标/按钮等触发的弹出框，则使用该跟手弹出框样式。

3 ) 跟手的弹框默认和触发按钮左右居中对齐，无法居中对齐时靠近边缘对齐。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185323.40632291032657602571618645733001:50001231000000:2800:2F90F53357CDDD9715E48F345B4ADED3ED441419C87187CCBEB41895EE46FD6E.png "点击放大")

### 折叠屏悬停

折叠屏产品具有独特的悬停态，即用户可以将产品半折后立在桌面上，实现免手持的体验。悬停态场景非常适合不需要频繁进行交互的任务，例如视频通话、播放视频、拍照、听歌等。

悬停态时，中间弯折区域难以操作且显示内容会变形，因此建议页面内容进行折痕区避让适配。建议上半屏内容由中线向上避让 16vp (3 毫米)、下半屏内容由中线向下避让 40vp (7 毫米)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030185324.12110028286169755793750507502350:50001231000000:2800:8409AE69DD43F9012D83232FCDDF50DDC7D5BF77A5BC2D7D78C8B4629B27B312.png "点击放大")

悬停态若触发应用内的弹出框、半模态等操作型控件，建议交互型控件在下半屏显示；若触发跟随上下文的控件，例如菜单等，建议跟随触发元素的位置显示。控件高度需要根据悬停态的屏幕尺寸进行最大高度的适配。

悬停态价值场景&适配规范，请参阅[悬停态](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-0000002352875141#section183378919119)。
