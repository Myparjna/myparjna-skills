# 阔折叠

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/flip-0000002321233974
- 抓取时间：2026-04-04T08:24:38.306Z
阔折叠手机是折叠手机的一种，展开时为直板机，折叠后尺寸为展开态大小的一半，携带更加便捷。相较于内屏，外屏幕尺寸较小，对应用的显示和操作要求更高，需要进行针对性设计。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160058.94663358456304864335934365050747:50001231000000:2800:2EB510DC2049559463CE1DDCE30EA670D2DC364F67B9899EC6F4EBFB3CACEA50.png "点击放大")

## 通用基础体验设计

### 布局完整

设备在折叠、展开或横竖屏切换时，应用窗口中的图片、视频等界面元素应避免出现错位、截断、变形模糊等问题。

<table id="ZH-CN_TOPIC_0000002321233974__table117mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002321233974__row122mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321233974__Xecaa724e6d938c29445cc7fa59385bebd0d9a57"><span><img originheight="2904" originwidth="4578" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160058.47853171611718718543106986432348:50001231000000:2800:7A5A96D220C3C7B4498D018F6403354E5BB0A25844951A37D5F2E6C0DF93367D.png" title="点击放大" width="268.5" height="170.31979030144169"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321233974__p125mcpsimp"><span><img originheight="2904" originwidth="4578" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160058.97333092190952622477146074935125:50001231000000:2800:DA1750CBFDB19E8D701C00206DA1EAA1608B76A393AA28356E6A28F462B8A149.png" title="点击放大" width="268.5" height="170.31979030144169"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321233974__row126mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321233974__p13990104185620"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160059.98927587939349313753054657850709:50001231000000:2800:E9FD31FE1B2A0D7FA9F6692B2A36E13975FB07CB7A7166D2C566078FBD7927B6.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002321233974__p128mcpsimp">不推荐（弹框截断）</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321233974__p1353242495720"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160059.74649866821634230918089523552803:50001231000000:2800:E06D38FF365A8B4AD6760BCFC8FDAB4C37B3E5A55F17CFACA24C6AB3FD71FBE8.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002321233974__p130mcpsimp">不推荐（视频截断、元素重叠）</p></td></tr></tbody></table>

外屏文字、图标大小应与内屏保持一致。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160059.32084154449015017210680723886203:50001231000000:2800:30608DA742FA140F6CC94C961F27BA08F3A19623A6124CFE5AA2516E78471AC9.png "点击放大")

### 导航条适配

外屏无需显示导航条，同时不显示导航条所占的纵向空间。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160059.61434830476342853784094387445600:50001231000000:2800:7EB979D1CE6A94B76AEE1151892CBF5B217D1C0D650E4EE9C48D585D7C2AA7E4.png "点击放大")

### 状态栏适配

外屏状态栏应隐藏，释放其所占用的纵向空间，增加内容显示区域。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160059.47980323440953580708052089074985:50001231000000:2800:B2893EA7FFD77D6A296757116E1A58055E1EBD3AE639BC3C9ED4C67144EA9E3A.png "点击放大")

### 多窗适配

外屏不支持悬浮窗、分屏功能，内屏已经形成的悬浮窗或分屏，设备折叠后焦点窗口外屏全屏打开，非焦点窗口退后台。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160100.12104310564571702210308195016515:50001231000000:2800:B3E502C297443507522108C06D980F10DAEF95AABC554AD80C73F169D3C40AC5.png "点击放大")

### 画中画适配

外屏支持画中画功能，通过点击画中画按钮、视频详情上滑退出应用等方式可启动画中画。

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

147

内屏已经打开画中画，设备折叠进入外屏画中画接续不中断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160100.47250940522082019179330015200760:50001231000000:2800:A748BF76613C9A94375BC731A0C6E7C7C6B23CE4ECEC81BDC03AFF3B70146562.png "点击放大")

### 通用应用架构

应用的基础布局结构一般为：

-   标题区：大标题、子页签、搜索图标等都在顶部标题区域显示。
-   内容区：内容区显示页面的主要内容，常见的内容区有列表、宫格、瀑布流等布局。
-   底部区 (可选)：底部操作区域，常见为底 tab、工具栏，底部区域为可选区域。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160101.81110688954288420167090020198463:50001231000000:2800:8CF70D020AF4EC88CF2C21BF78DD741FA9FDC30F4D301E000B16AF053F33D1D1.png "点击放大")

(内屏通用架构)

外屏应与内屏保持一致的应用架构，保证功能和显示完整可交互。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160101.97355335008225024265540584844045:50001231000000:2800:490922E9903AECED9AF759D49828C2EB9E231ED91D516A275ABBA00296260283.png "点击放大")

(外屏通用架构)

**瀑布流布局**

-   设备折叠，应用界面遵循基础的布局结构不变，确保功能正常操作。
-   窗口高度发生变化，界面上可滑动的内容溢出到屏幕外，滚动页面查看。滑动过程中，顶部与底部结构如标题栏、底部导航栏可临时隐藏。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160101.23961002791593623352473996410057:50001231000000:2800:3E271F8509CC14B2C8CECB0FBCC82CAC2DF493AC144D9AEE4A391B9E5F3E5199.png "点击放大")

**固定布局**

外屏固定布局应用，界面内元素需支持一定的压缩和变形，在确保功能完整、可交互的前提下保证内容完整显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160102.21558059960367932807689788658588:50001231000000:2800:738554451EBED843B98F884DA8AF13D532939E6316DA24E70C66F8A456C0375A.png "点击放大")

### 滑动沉浸

外屏屏幕尺寸较小，为便于浏览和获取信息，可采用滑动或点击的方式，将顶部和底部的标题栏、导航栏等控件隐藏，以提供更大的信息显示量。

**全部隐藏**

滑动应用内容区，同时隐藏顶部和底部的控件，以帮助用户更加专注于页面内容。

本场景的开发指南，请参阅[滑动沉浸式浏览](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-purax-guide)。

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

176

**局部隐藏**

滑动应用内容区，隐藏部分顶部栏和底部栏，以增加内容区域可视空间，同时保留轻量级内容，以确保必要的功能操作得以实现。

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

151

### 横幅 Banner 适配

应用横幅 Banner 区域在屏幕顶部沉浸式显示，外屏应用横幅 Banner 尺寸需要进行一定的压缩，最大高度不超过屏幕高度的 60% ，压缩后需要确保图片、文字不变形，核心内容在窗口完整显示，例如视频应用。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160102.34215882486321178354459528053861:50001231000000:2800:F4BF0CCBDD26C7C4E3A49978A192E2721B92FBFD091620842E99257DCDCD3616.png "点击放大")

## 组件适配

### 标题栏

外屏应用大标题切为小标题显示，以减少留白区域，增加核心内容显示空间。

本场景的开发指南，请参阅[标题栏外屏适配](https://gitee.com/harmonyos_samples/SmallWindowScene)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160102.74076461179026881684285261435228:50001231000000:2800:6C9E371B6D9134557038AB12E6D33AE9E7E1CD57BB0B6E16552240FE5715099C.png "点击放大")

### 搜索框

外屏应用搜索框切换为搜索图标，与标题栏同行显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160103.66732507056127530561056658041878:50001231000000:2800:7209A1E5A5A7607C95EE9F97AE374270F9EA4C39F5371128FE92EBE82B69BC81.png "点击放大")

### 索引条

外屏采用分段式索引条，长按指定分段可滑动选取具体字母进行索引。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160103.55399424425512997176333784845616:50001231000000:2800:7E81EA608018B4C61A5221304F6187E3B71D73F122BEFEDC62AC045680A4A5D8.png "点击放大")

### 弹出框

建议调用系统的弹出框控件，以便更好地适配不同的屏幕尺寸，保持体验的一致性。

弹出框包括系统弹窗、隐私声明、权限弹窗、提示弹窗、Toast、运营类弹窗等。

外屏弹出框需在屏幕内完整显示，包括弹框主体及弹框主体外的交互对象 (按钮等)，弹出框在外屏显示的最大高度不超过屏幕高度的 90% 。

本场景的开发指南，请参阅[弹出框适配](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-purax-guide)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160103.16057786860646262734262092486846:50001231000000:2800:660D78BE61B415044B7B0F0F1560FC135C448E35CEB5E3881DA6827A784360DA.png "点击放大")

### 半模态

半模态控件在外屏需要保持功能完整，超出窗口的内容支持可滑动，最大尺寸为距离窗口顶部 8vp。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160104.67410848190757614286526494503830:50001231000000:2800:E58C946A19A184C6D981235279C6A7606351DD8F02C89BC0EED6B43612BD9A6F.png "点击放大")

## 典型场景

### 图文详情页

**单图**

外屏上图下文形式的内容详情类页面，图片等比缩放，高度不超过窗口高度的 60% ，确保图片和文本详情都在窗口内显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160105.27880303379718701004087433073497:50001231000000:2800:3C7A5F8D1F3A151193814F2534863DE7BF5BC3A3A67883D385168B765FC874EA.png "点击放大")

**多图**

使用外屏时，多图的上图下文形式的内容详情类页面图片等比缩放后，原滑动显示的图片采用延展布局显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160105.93928455833833379421580093899251:50001231000000:2800:C57774D1804290641DEF1AEFBB3EFCE3E3D9BFECAFD464FA17EA8474A3EBD276.png "点击放大")

### 长视频

**视频播放详情**

-   外屏视频类应用视频画面区域在窗口内完整显示，顶部设置固定冻结区域
-   上滑页面时顶部冻结区域可等比缩放至屏幕高度的 40% ，下滑恢复

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160106.08437645650525681884183709328098:50001231000000:2800:A2C7A35E44DEC4C9DBF719499FE7DBA80C9121F30715656F4108347D2DDFC7F4.png "点击放大")

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

74

**视频全屏播放不旋转**

外屏视频全屏播放，窗口不旋转，保持当前方向播放。

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

75

### 短视频

**短视频播放详情**

-   短视频、直播等视频画面区域在屏幕内完整，画面不被截断
-   横向比例的视频窗口 (16:9、21:9、4:3) 确保宽度占满屏幕，自适应缩放高度
-   纵向比例的视频窗口 (9:16) 确保高度占满纵向内容区自适应缩放宽度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160106.69924679429567808542776608996530:50001231000000:2800:A7BE144F405AF68BA8006249C637151A9E5A9B4B71FC9E1726B87DABDD8C2393.png "点击放大")

**侧边控件**

外屏应用侧边控件应避免显示截断或重叠，并支持滑动显示。

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

73

**直播弹幕**

外屏直播类应用底部弹幕最大高度不超过窗口高度的 50% 。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160106.84253454981368090538306898857058:50001231000000:2800:C4E04F27CE620BF5D4AD0799720C7441F6CE9877B056F38FA6A773089279707D.png "点击放大")

**评论区页面**

-   外屏应用的评论区默认高度最小为屏幕高度 40%
-   评论输入框需完整显示
-   评论区上拉占满全屏，下拉恢复

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160107.84413784976857487668230363940564:50001231000000:2800:3BC969E7E36CF793C2543E0CF1C8132895918D074DF8A0642E3DDFB922C94A1E.png "点击放大")

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

21

**登录页**

-   压缩留白区域
-   顶部和底部操作区固定显示
-   内容显示不全，需支持滑动查看

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160107.14434288351289844460284542536682:50001231000000:2800:A39796299EAC78BAE43D2C8F95980892A64821B5D899469257BEC2B625651D7F.png "点击放大")

<table id="ZH-CN_TOPIC_0000002321233974__table3700132414468" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002321233974__row37011824194615"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321233974__p3610173914293"><span><img originheight="1104" originwidth="1456" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160107.47250509901458612440343857954417:50001231000000:2800:96FDABA96F7D0BE237AF4A3E4A7C04F6C1C5E731CDB59083EB5ADE9379FD8672.png" title="点击放大" width="268.5" height="203.5879120879121"></span><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160107.62854746760761463547172904564580:50001231000000:2800:306704D3DD2FD2A185EA1E5660C7F32329A2FEFF8C00ECE4476660215FAB0D57.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002321233974__p1557104412483"><span style="color: rgb(127,127,127);">不推荐（元素重叠）</span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321233974__p121411543122913"><span><img originheight="1104" originwidth="1456" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160107.96031453784000670733236984788095:50001231000000:2800:52A1FF9B198186ABD0277D8AE94B1F5BAFA5FC1F8310EEA14C310E535E95B617.png" title="点击放大" width="268.5" height="203.5879120879121"></span><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160107.53219454219235824382918390479709:50001231000000:2800:AF9CF034773914E33E94D6190DC8F0743B2540358426FE241ED9AB156C5AA504.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002321233974__p544381174714"><span style="color: rgb(127,127,127);">不推荐（页面固定布局且不支持滚动，导致截断）</span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321233974__row27013243467"><td class="row-nocellborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>
