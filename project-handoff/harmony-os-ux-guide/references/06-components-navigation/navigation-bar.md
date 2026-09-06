# 导航条

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/navigation-0000001957075737
- 抓取时间：2026-04-04T08:23:50.329Z
导航条是 HarmonyOS 系统的典型特征，是手势导航等重要功能的提示入口，是应用必须适配的要求。

## 设计原则

要做到导航条和应用内的底部交互不干扰，达到和谐的使用体验，需要注意以下几点：

1) 调用最新的系统控件，且窗口没有声明全屏，导航条自动抬高避让 。

2) 如果窗口声明了全屏 (适用于视频、游戏等沉浸式应用场景)，需要根据开发指南调用系统能力进行导航条避让适配。

3) 需要根据开发指南实现导航条的沉浸式背景效果。

4) 使用 Webview 或三方框架开发的应用，同样需要进行导航条的抬高避让和沉浸式背景适配

底部导航条的开发适配指南请参阅[开发应用沉浸式效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects)。

## 沉浸式背景

系统基于深色、浅色等不同背景，为导航条提供智能反色的能力。应用在进行界面设计时，需要确保为导航条底部提供沉浸式的背景和28vp高度的抬高避让。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201353.03209113402303483595751998426968:50001231000000:2800:14D767589372A91762BF9609CFE9438088899CA1108DAF48138073491E8A48E5.jpg "点击放大")

## 导航条适配

需要考虑应用内的导航条适配，避免导航条遮挡底部内容或交互

-   可滚动页面
-   底部固定控件&键盘
-   底部悬浮控件
-   半模态&弹出框
-   多窗场景
-   横屏场景
-   沉浸式场景
-   短视频场景

### 可滚动页面

可滚动页面，无需避让导航条，当滚动的内容滑到最底部时，需要进行最底部内容的抬高适配，避免被导航条遮挡。

### 可滚动列表实例

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201353.90537228157875699926420649939660:50001231000000:2800:1BE380016A9B635DBBD662C33073FD552F5D8399575944938258F3339FA1EC39.png "点击放大")

### 可滚动网页示例

网页的可滚动内容，也需要遵循以上适配要求，例如下图示例：

1) 可滚动内容，无需避让导航条；

2) 网页缩放后也遵循以上适配要求，可滚动内容无需避让导航条；

3) 可滚动内容，滑到最底部，内容需要抬高，避免被导航条遮挡；

4) 网页底部有滚动条时，滚动条和导航条要避免显示重叠。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201353.64033134068591136069056901965082:50001231000000:2800:077AC913D6E00208F6494A688364E569665D97217B4BB4B34D65C1EBD5CFEFC3.png "点击放大")

### 底部固定控件&键盘

<table id="ZH-CN_TOPIC_0000001957075737__table399211091113" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957075737__row1499219011117"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p199921909111"><span><img originheight="1090" originwidth="3120" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.39199801237937433323434626594793:50001231000000:2800:40F08384708F13D2D62CDA73B0714C34A7C368B009D7DB885B7455CC2B73E156.png" title="点击放大" width="587" height="205.07371794871796"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957075737__row599219011119"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p179931803114"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.28485927109886730932164009750939:50001231000000:2800:2C5279EEE3478852E1929F650C73111F264E9A9EC4A9F374D0CD7B8CA77C2C08.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p199310020110">推荐（底部固定控件抬高，避免和导航条互相遮挡，且提供沉浸式背景效果）</p></td></tr><tr id="ZH-CN_TOPIC_0000001957075737__row1399370171119"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p09932005117"><span><img originheight="1090" originwidth="3120" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.93451757632702560437756306731614:50001231000000:2800:E56104541BA6EB6C51D742C8D04AA106D3B002F280EC61EF54E945BCC1297AE2.png" title="点击放大" width="587" height="205.07371794871796"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957075737__row39935081119"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p8993170111112"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.68446556903096823823670561077585:50001231000000:2800:FF6A4EF083C7BA5840725C924957C685175B25A3B938D9B092046CD70A9E139E.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p099311001114">不推荐（导航条和底部控件互相遮挡；导航条没有沉浸式背景效果）</p></td></tr></tbody></table>

### 底部悬浮控件

<table id="ZH-CN_TOPIC_0000001957075737__table79938071117" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957075737__row1799319010112"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p553813542316"><span><img originheight="1314" originwidth="3742" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.11358042044854818173156136282604:50001231000000:2800:66A500AD9E1128FED0CBF5EEE5E5197904C3E6AF1756B615B44AC1C7E89BE8C9.png" title="点击放大" width="587" height="206.12453233564938"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957075737__row39932021118"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p1599390141115"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.97300610198081585326950832207853:50001231000000:2800:F67FB65B0437FE91931B2DADC8B49DDA5B1567640FD7E938C85DA6FE279199F0.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p999310011115">推荐（底部悬浮控件抬高，避免和导航条遮挡；Video控件导航条可超时不处理自动隐藏）</p></td></tr><tr id="ZH-CN_TOPIC_0000001957075737__row1699314011120"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p099310031114"><span><img originheight="1314" originwidth="3742" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.37481400950285485662076841754823:50001231000000:2800:8844680274C92E6F12151345840F3F4CE0391DBECDA09BEFD14B4E72292CA880.png" title="点击放大" width="587" height="206.12453233564938"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957075737__row16993909111"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001957075737__p12993130151119"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.44994289562090818033250290658785:50001231000000:2800:1851BC0D75D2E4A3BC632D0506DE2AF866C18E5CEB4CEAEB2430C2B144AE72F6.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p399313081117">不推荐（导航条和底部控件互相遮挡）</p></td></tr></tbody></table>

### 半模态&弹出框

半模态控件中可滚动的内容可显示在导航条下方，可滚动内容滑到最底部时需要向上抬高，避免最底部的交互被导航条遮挡；有弹出层控件时，弹出层控件与导航条要避免互相遮挡，导航条层级比弹出层控件高。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201354.87026910200795693674641605173684:50001231000000:2800:198FA40E56390038BDF17C295F9F32B6F9DFD0AD3443E05F071E1D266C802B18.jpg "点击放大")

## 多窗场景

多窗存在悬浮窗、分屏和画中画三种窗口形态。分屏时需要进行导航条的适配，悬浮窗内、画中画内都无需显示导航条也无需进行导航条适配。

### 上下分屏

下分屏应用的底部需要进行导航条适配，上分屏应用底部控件需要避免抬高过高。

<table id="ZH-CN_TOPIC_0000001957075737__table20248123151715" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957075737__row1125816231170"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957075737__p121411555195116"><span><img originheight="1776" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201355.00172931826287643183617164609585:50001231000000:2800:6C0359642F83A26F4E4A784CCA028F7DC07398BD5A57BBDCBBE3A788916D2C46.png" title="点击放大" width="268.5" height="165.57500000000002"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p1980245515215"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201355.29800190178490664803082909846569:50001231000000:2800:F264CBA7EF98539D1455AF5DDF22AB188F2E132BD719E381F221747AB38912D5.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p880225525217">推荐（下分屏应用适配导航条）</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957075737__p14286181216526"><span><img originheight="1776" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201355.25950828152530685118182374278495:50001231000000:2800:454EAFF8218909ECA3430DEC7A87C29F9E64FD9695306171B689069FE484AAF9.png" title="点击放大" width="268.5" height="165.57500000000002"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p9891141925313"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201356.33860369201271074494146066349743:50001231000000:2800:7CF78E0703CA70F404EE5EB841A396469F3E8ED45769BA1D5B0F4DDA6E063077.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p3891101917534">不推荐（上分屏应用底部抬高过高，浪费可显示空间，下分屏未适配导致显示叠加）</p></td></tr></tbody></table>

### 左右分屏

两侧分屏应用的底部均要适配导航条，避免应用底部控件与导航条相互遮挡。

<table id="ZH-CN_TOPIC_0000001957075737__table16967915557" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957075737__row571912912551"><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957075737__p8200957185514"><span><img originheight="1776" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201356.99253884839442713892666287911707:50001231000000:2800:7E70C474BBBE3539E1C9DEA4F6E6116625372F1C2D8E26BE57AAC01BD072437B.png" title="点击放大" width="268.5" height="165.57500000000002"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p171242812568"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201356.70143104324240742143395252589260:50001231000000:2800:98DF425C3D709BDAE8B6AF4928D4874AD03F8DD70B76DC1AC4690E5B2ADFF010.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p712528165615">推荐（左右分屏时，两侧应用均适配导航条）</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957075737__p1163315813569"><span><img originheight="1776" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201356.03382521037358014468705554530250:50001231000000:2800:401E098181E8B9B1772B320626E3D1518B4A3543755A36DF17D098BF290A2A01.png" title="点击放大" width="268.5" height="165.57500000000002"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p199700035715"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201356.39548754937221507185261304447008:50001231000000:2800:252639C3C04F6B73F3D833E4E5902716ED61DE9D4372D1F36F433C831264CE7B.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p1497012019574">不推荐（应用底部固定控件与导航条相互遮挡）</p></td></tr></tbody></table>

### 悬浮窗

导航条为系统特性，不会在悬浮窗内显示。当应用在悬浮窗内显示时，需要避免窗口内底部抬高过高导致浪费显示空间。

<table id="ZH-CN_TOPIC_0000001957075737__table167211710155816" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957075737__row1732151005814"><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957075737__p2068417293589"><span><img originheight="1776" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201356.11008514962885678305629648490522:50001231000000:2800:C0AF2DA3FD9347820929F6CA2176561F58C0CB2F2DB26A3B80DF86908BD56332.png" title="点击放大" width="268.5" height="165.57500000000002"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p19499125418583"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201357.19650549939867535287030798096005:50001231000000:2800:A5E9952C7F616694F46BCC3BAC5658FE199B54AAFBE4730594543926227CC9C8.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p12499155411587">推荐（窗口内应用底部固定控件正常显示）</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957075737__p236074035811"><span><img originheight="1776" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201357.84537393325811193750334108649819:50001231000000:2800:0BC3AF35B1EBD1CF0FBC15574124DCB7BA33FACF401E05DDE8F2563D83AF0383.png" title="点击放大" width="268.5" height="165.57500000000002"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p149892975919"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201357.10068729032540593784712206333819:50001231000000:2800:500B896E31DA03EA44368ED4A3D58DFE602D247CD0F70CEF3AD67425BFA5D9AA.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000001957075737__p139899919590">不推荐（窗口内应用底部控件预留了抬高，浪费空间）</p></td></tr></tbody></table>

## 横屏场景

### 普通横屏场景

适配了直板机横屏的应用内，横屏时导航条正常显示，应用需要进行导航条的适配。通常横屏场景隐藏底部控件。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201357.69041158064481756263225051994560:50001231000000:2800:34CBE018EE03F437C40F72619439E9CF70B542BD6153D8AB2947DE92D3BE3DC7.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201357.26938002433771950638002486903899:50001231000000:2800:B078AF01B9581DA013327FF5C59DA5B30498F8F91DB854BD5655CCFFE99DD290.png "点击放大")

## 沉浸式场景

典型沉浸式场景：游戏、全屏播放长视频、全屏看大图、拍摄、录像等。

沉浸式场景下，默认显示导航条，超过 2 秒不处理，自动隐藏。导航条隐藏后，从屏幕底部上滑可恢复导航条的显示。

### 长视频示例

沉浸式播放视频，默认显示导航条，2秒后自动隐藏的示例。

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

398

### 横屏沉浸式场景示例

在横屏的沉浸式场景下，导航条支持默认显示，超过2秒自动隐藏。例如，横屏查看图片详情时，默认显示，2秒后自动隐藏导航条。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201357.23010306774881358954682571354414:50001231000000:2800:33E7B2D46B8FC51197B39FE1E2855B5B972E59581DFA741CEEE4F197913EBC7B.png "点击放大")

### 图片详情示例

图片详情页查看大图，默认显示导航条，进入沉浸看图状态后，先显示导航条，2秒后自动隐藏的示例。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201358.45583551707902966512599369561917:50001231000000:2800:EFD3F2E25F77369B39CBCE2B1E26C355BCB617ACA3DF5AC272089E7CD0B6737B.png "点击放大")

宽屏设备上的沉浸式场景，建议上下或左右撑满显示，避免因为导航条影响可显示区域的大小。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201358.25829860704707360065493526459525:50001231000000:2800:EBE2E2FDE7A7C5AC75609CAD95C8669519DF9E6FEF7AB20CD44B026327587199.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201358.20049397104132387938300348122949:50001231000000:2800:1D2087D68ED933955D108E7C843656AA5E3D70ED9D8CC1A8CC08FE2B8CEF2137.png "点击放大")

推荐（全屏显示，上下高度撑满全屏）

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201358.92945445060177808240376970046060:50001231000000:2800:14A3D8F57983F119610F0CF4B4DDDCAF60C16062DDAA1D5346BFE22084F1A152.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201359.28258753403543647361427276574097:50001231000000:2800:C7E29989251E27979F5FFE8549FE69CF14CFB423F8AF21B5A7FE1C6BF7CF59A7.png "点击放大")

不推荐（导航条没有超过2秒自动隐藏，或大图高度未撑满全屏）

### 游戏示例

游戏场景默认显示导航条，超过2秒自动隐藏。从底部向上滑恢复显示导航条。游戏场景需要进行手势导航的防误触适配，所以从底部上滑两次手势导航才生效，全屏页面才会跟手缩小；其他场景从底部上滑一次即可手势导航生效，全屏页面跟手缩小。

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

357

## 短视频场景

短视频场景建议上下撑满画面，同时底部控件抬高，避免底部控件与导航条相互遮挡。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201359.01234493474493940579822557235721:50001231000000:2800:B369C2C6BDF29B021CB7D14AC9BC4D50CB3F47879E377F1DBB6AC971DD657404.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201359.04372976436341709371625998510077:50001231000000:2800:14A476CCB90CD5437A85275FBC5C90BAA756014B06FB686C746E7FB39E1E1827.png "点击放大")

推荐（视频上下撑满，更沉浸的显示效果）

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201359.51767427418617990897151808447596:50001231000000:2800:584463801309C1C6C126A060576ADC785AE74AE736F30B4D14A704A838684A62.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201359.34803345022620682136561591605793:50001231000000:2800:6BA0071FD28926D920DFE5D8DF55DADAA43D84B31E13A129BF88468E09A502AD.png "点击放大")

不推荐（底部固定控件与导航条相互遮挡，或视频画面未上下撑满全屏）
