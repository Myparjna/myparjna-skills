# 画中画

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/pip-0000001927422624
- 抓取时间：2026-04-04T08:24:05.803Z
画中画是一种视频内容或视频通话的显示方式，利用“画中画”可以在使用其他应用的同时，观看视频内容或使用视频通话，覆盖场景包括视频播放、直播、视频通话、视频会议等。

## 基础方式

画中画有多种触发方式，业务可根据具体场景需要进行选择。

固定入口：通过应用内的固定入口触发，点击按钮开启画中画。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224850.52635807724630664149609816668687:50001231000000:2800:5931B37F25DF5543B2C895E070650054E24CB57A849EB39EA8A4D736A57C4868.png "点击放大")

应用返回：通过应用内点击"返回"按钮或手势返回，返回至应用上一级，开启画中画。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224851.53623521406024992613898630668989:50001231000000:2800:88F697115264CD9419F00700F80FE8155C56430D0044755105F36C70C37CD667.png "点击放大")

注：使用本方式，需先在系统设置中开启“自动开启画中画”

返回桌面：在应用内返回桌面，开启画中画。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224851.49799478558763647938137067335196:50001231000000:2800:60C7F662114CBD146F758BC51E92311AA4EFB392365F124C3578CCF724C6A0BB.png "点击放大")

注：使用本方式，需先在系统设置中开启“自动开启画中画”

### 窗口大小调节

可以通过以下方式调节窗口大小：

1、双击窗口放大。

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

866

2、拖拽窗口左下角或右下角，窗口等比例大小缩放。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224851.05148750721607813522340116301874:50001231000000:2800:97A6BB46F7530DC71B62156BEC1B9DD2BB1140A6D4BB5EE7EA5B77AF820E2DB3.png "点击放大")

3、手指捏合或张开，在最大和最小尺寸之间等比例缩放窗口。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224852.02618799226303426136556572147852:50001231000000:2800:7D9EC7DE25DB3BEDA062D61173CBFF2E78998F088516F88B9560D1FB90F54753.png "点击放大")

### 窗口最小化

拖动画中画窗口到屏幕边缘，画中画收起到侧边悬浮条，任务不中断。点击侧边条，可从侧边条中恢复画中画窗口。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224852.72776840228461072240980257596628:50001231000000:2800:756B8F232A23D470CE8D8514A1984EF0A2BDF8D5BCDB8184EC65BFD08331A23A.png "点击放大")

### 窗口控制面板

系统提供根据业务场景提供统一的控制面板。

**【控制面板结构**】

系统定义画中画窗口显示区域、按钮数量和功能，针对不同业务场景提供对应的控制模版。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224852.21809307810511660835983628053333:50001231000000:2800:754F315A55C4427D54AE2FBEF36225A7B5C2A63A4C0530390E2B4D82144A7720.png "点击放大")

不同业务场景的窗口模版：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224852.52245501201865803031900832423831:50001231000000:2800:45280282678589D367994A4A05F54B41532E0F8EB593A1362FA84F8EA2EDEF37.png "点击放大")

**【控制面板交互**】

默认小窗启动，显示控制面板，控制面板 3 秒不操作，自动隐藏。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224852.51515050111611787589763185542463:50001231000000:2800:4ED703C2F3F2E0D55B025172BA790F48692304099629636AF031E7A34752A8A3.png "点击放大")

控制面板隐藏，单击窗口控制面板显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224852.01885323776536568141947384838691:50001231000000:2800:599A1D1FB9B30D9A293D106D3AEE149B1156CA2E20D8EF64FBAD170B45DCB7C7.png "点击放大")

2 in 1端鼠标移动到画中画窗口上悬停，控制面板显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224853.64073415097597640028119062027565:50001231000000:2800:C71AA17E86AAB2C50831355E8357C0F47D9FBD8D3BDC5A63C416A53CC53C327C.png "点击放大")

不同业务场景的控制按钮支持可配置，可根据场景需要配置显示不同的功能按钮。

<table id="ZH-CN_TOPIC_0000001927422624__X6c0e9c47321db83833fe7f946308f25925baaef" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001927422624__row150mcpsimp"><td class="cellrowborder" valign="top" width="8.450845084508451%"><p id="ZH-CN_TOPIC_0000001927422624__p152mcpsimp"><strong>业务场景</strong></p></td><td class="cellrowborder" valign="top" width="13.77137713771377%"><p id="ZH-CN_TOPIC_0000001927422624__p155mcpsimp"><strong>窗口控制区</strong></p></td><td class="cellrowborder" valign="top" width="17.17171717171717%"><p id="ZH-CN_TOPIC_0000001927422624__p158mcpsimp"><strong>内容控制</strong></p></td><td class="cellrowborder" valign="top" width="21.21212121212121%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="39.39393939393939%"><p id="ZH-CN_TOPIC_0000001927422624__p162mcpsimp"><strong>备注</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row164mcpsimp"><td class="cellrowborder" valign="top" width="8.450845084508451%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="13.77137713771377%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="17.17171717171717%"><p id="ZH-CN_TOPIC_0000001927422624__p168mcpsimp">必选</p></td><td class="cellrowborder" valign="top" width="21.21212121212121%"><p id="ZH-CN_TOPIC_0000001927422624__p170mcpsimp">可选</p></td><td class="cellrowborder" valign="top" width="39.39393939393939%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row172mcpsimp"><td class="cellrowborder" valign="top" width="8.450845084508451%"><p id="ZH-CN_TOPIC_0000001927422624__p174mcpsimp"><strong>视频播放</strong></p></td><td class="cellrowborder" valign="top" width="13.77137713771377%"><p id="ZH-CN_TOPIC_0000001927422624__p177mcpsimp">关闭、还原</p></td><td class="cellrowborder" valign="top" width="17.17171717171717%"><p id="ZH-CN_TOPIC_0000001927422624__p179mcpsimp">播放/暂停</p></td><td class="cellrowborder" valign="top" width="21.21212121212121%"><p id="ZH-CN_TOPIC_0000001927422624__p181mcpsimp">上一个&amp;下一个、快进&amp;快退</p></td><td class="cellrowborder" valign="top" width="39.39393939393939%"><p id="ZH-CN_TOPIC_0000001927422624__p183mcpsimp">可选控件只能成对出现，不支持拆分；上一个&amp;下一个与“快进&amp;快退”仅可配置一对，不可同时出现。</p></td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row184mcpsimp"><td class="cellrowborder" valign="top" width="8.450845084508451%"><p id="ZH-CN_TOPIC_0000001927422624__p186mcpsimp"><strong>直播</strong></p></td><td class="cellrowborder" valign="top" width="13.77137713771377%"><p id="ZH-CN_TOPIC_0000001927422624__p189mcpsimp">关闭、还原</p></td><td class="cellrowborder" valign="top" width="17.17171717171717%"><p id="ZH-CN_TOPIC_0000001927422624__p191mcpsimp">无</p></td><td class="cellrowborder" valign="top" width="21.21212121212121%"><p id="ZH-CN_TOPIC_0000001927422624__p193mcpsimp">外放静音、播放/暂停</p></td><td class="cellrowborder" valign="top" width="39.39393939393939%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row195mcpsimp"><td class="cellrowborder" valign="top" width="8.450845084508451%"><p id="ZH-CN_TOPIC_0000001927422624__p197mcpsimp"><strong>视频通话</strong></p></td><td class="cellrowborder" valign="top" width="13.77137713771377%"><p id="ZH-CN_TOPIC_0000001927422624__p200mcpsimp">关闭、还原</p><p id="ZH-CN_TOPIC_0000001927422624__p201mcpsimp">(配置任意可选按钮后显示)</p></td><td class="cellrowborder" valign="top" width="17.17171717171717%"><p id="ZH-CN_TOPIC_0000001927422624__p203mcpsimp">无</p></td><td class="cellrowborder" valign="top" width="21.21212121212121%"><p id="ZH-CN_TOPIC_0000001927422624__p205mcpsimp">打开/关闭麦克风、挂断、打开/关闭摄像头、外放静音</p></td><td class="cellrowborder" valign="top" width="39.39393939393939%"><p id="ZH-CN_TOPIC_0000001927422624__p207mcpsimp">1、默认无按钮，点击画中画窗口任意位置还原；</p><p id="ZH-CN_TOPIC_0000001927422624__p208mcpsimp">2、选择任意可选按钮，“还原”和“关闭”按钮自动显示。</p></td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row209mcpsimp"><td class="cellrowborder" valign="top" width="8.450845084508451%"><p id="ZH-CN_TOPIC_0000001927422624__p211mcpsimp"><strong>视频会议</strong></p></td><td class="cellrowborder" valign="top" width="13.77137713771377%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="17.17171717171717%"><p id="ZH-CN_TOPIC_0000001927422624__p215mcpsimp">关闭、还原</p><p id="ZH-CN_TOPIC_0000001927422624__p216mcpsimp">(配置任意可选按钮后显示)</p></td><td class="cellrowborder" valign="top" width="21.21212121212121%"><p id="ZH-CN_TOPIC_0000001927422624__p218mcpsimp">无</p></td><td class="cellrowborder" valign="top" width="39.39393939393939%"><p id="ZH-CN_TOPIC_0000001927422624__p220mcpsimp">打开/关闭麦克风、挂断、打开/关闭摄像头、外放静音</p></td></tr></tbody></table>

## 视觉规格

### 窗口默认大小、位置

画中画默认显示最小窗口尺寸，手机端、折叠屏和平板端默认显示在屏幕右上角，2 in1 端默认显示在屏幕左上角。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224853.72359768977699059081663802340930:50001231000000:2800:4220E39873561C1409D13192D752C4CFE2CE848B8FCAF164FA5AA6FAAAB117C9.png "点击放大")

### 画中画窗口尺寸

系统定义了竖向和横向两种比例的的画中画窗口，两种比例的窗口在不同设备上分别有最小（默认）和最大两个尺寸，应用可设定画中画窗口的显示比例，系统根据设定比例自动适配画中画的窗口大小。

<table id="ZH-CN_TOPIC_0000001927422624__X7ad163e3846ec33568bd6711f6a6ccc4b93175a" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001927422624__row233mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p235mcpsimp"><strong>设备状态</strong></p></td><td class="cellrowborder" valign="top" width="28.999999999999996%"><p id="ZH-CN_TOPIC_0000001927422624__p238mcpsimp"><strong>竖向画中画窗口</strong></p></td><td class="cellrowborder" valign="top" width="15%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="26%"><p id="ZH-CN_TOPIC_0000001927422624__p242mcpsimp"><strong>横向画中画窗口</strong></p></td><td class="cellrowborder" valign="top" width="15%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row245mcpsimp"><td class="cellrowborder" valign="top" width="15%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="28.999999999999996%"><p id="ZH-CN_TOPIC_0000001927422624__p248mcpsimp">默认尺寸</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p250mcpsimp">最大尺寸</p></td><td class="cellrowborder" valign="top" width="26%"><p id="ZH-CN_TOPIC_0000001927422624__p252mcpsimp">默认尺寸</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p254mcpsimp">最大尺寸</p></td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row255mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p257mcpsimp"><strong>直板机/折叠屏折叠态</strong></p></td><td class="cellrowborder" valign="top" width="28.999999999999996%"><p id="ZH-CN_TOPIC_0000001927422624__p260mcpsimp">窗口短边为屏幕短边的 30%</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p262mcpsimp">窗口宽度占 3 栅格</p></td><td class="cellrowborder" valign="top" width="26%"><p id="ZH-CN_TOPIC_0000001927422624__p264mcpsimp">窗口短边为屏幕短边的 30%</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p266mcpsimp">窗口宽度占 4 栅格</p></td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row267mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p269mcpsimp"><strong>折叠屏展开态</strong></p></td><td class="cellrowborder" valign="top" width="28.999999999999996%"><p id="ZH-CN_TOPIC_0000001927422624__p272mcpsimp">窗口短边为屏幕折叠态短边的 30%</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p274mcpsimp">窗口宽度占 3 栅格</p></td><td class="cellrowborder" valign="top" width="26%"><p id="ZH-CN_TOPIC_0000001927422624__p276mcpsimp">窗口短边为屏幕折叠态短边的 30%</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p278mcpsimp">窗口宽度占 5 栅格</p></td></tr><tr id="ZH-CN_TOPIC_0000001927422624__row279mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p281mcpsimp"><strong>平板</strong></p></td><td class="cellrowborder" valign="top" width="28.999999999999996%"><p id="ZH-CN_TOPIC_0000001927422624__p284mcpsimp">窗口尺寸为默认悬浮窗窗口大小的 30%</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p286mcpsimp">窗口宽度占 4 栅格</p></td><td class="cellrowborder" valign="top" width="26%"><p id="ZH-CN_TOPIC_0000001927422624__p288mcpsimp">窗口宽度为屏幕短边的 30%</p></td><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001927422624__p290mcpsimp">窗口宽度占 5 栅格</p></td></tr></tbody></table>
