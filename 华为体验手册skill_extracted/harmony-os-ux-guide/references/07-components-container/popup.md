# 气泡提示

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/popup-0000001956975269
- 抓取时间：2026-04-04T08:23:05.553Z
通过临时弹出指向性气泡提示用户当前如何操作。开发相关能力请参考 [Popup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213440.96615023935176868880872388206653:50001231000000:2800:2E57CAB91CF174CE4678FD30A4BD120C46E82B34AF4671CEDB3445FA52A15932.jpg "点击放大")

## 如何使用

**气泡提示是一种临时性的、非模态的小型弹出框，用于向用户显示简短的提示信息或补充说明。**通常由一个小三角形指示器和一个矩形框构成，矩形框内包含文字或图标。

**气泡提示常用于对某个对象进行简短描述或补充说明。**气泡提示的指向对象通常是链接文字或图标，用于那些不太被用户所关注的元素场景。在 电脑设备上，当鼠标悬停在某个控件上时，也可能会显示该控件的功能说明。

**气泡提示分为带操作和不带操作两种类型。**不带操作主要以文本提示为主，这类气泡出现时间有最大限制，或是点击界面空白区域即可消失。带操作的需要常驻显示，用户只能通过执行关闭按钮或者其他功能键跳转入口才可关闭。

<table id="ZH-CN_TOPIC_0000001956975269__table1279732619584" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975269__row197972026145813"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p379711261589"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213440.51438171165960667399161725166807:50001231000000:2800:2703F451CAAAD411387A164E5EBB9C974C2F7F81D7BEE4F7A8145711124471A6.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p1679792625812"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213440.49574184306478465519502002161998:50001231000000:2800:1AE8BAD61477A77E6971A71D503A40E3F5FE669CFB2B098BB8FD7CB352CB4DF3.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row1579722645816"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p107878421580">不带操作的气泡提示</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p1323034019584">带操作的气泡提示</p></td></tr></tbody></table>

## 视觉规则

**手机**

**气泡内默认元素规格**

在气泡提示中提供了一些默认布局样式，开发者可以通过 [PopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup) 中提供的接口类型实现 HarmonyOS NEXT 默认效果。其中包含规定样式的默认布局和接口能力。默认样式需要绑定 [bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup) 进行使用。

<table id="ZH-CN_TOPIC_0000001956975269__table1234410553570" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975269__row1234411557575"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p18718116195818"><strong>对应元素接口名</strong></p><p id="ZH-CN_TOPIC_0000001956975269__p1471811611588">1.icon</p><p id="ZH-CN_TOPIC_0000001956975269__p13718146195815">2.title</p><p id="ZH-CN_TOPIC_0000001956975269__p1171816145810">3.message</p><p id="ZH-CN_TOPIC_0000001956975269__p87189685820">4.showClose</p><p id="ZH-CN_TOPIC_0000001956975269__p3718369587">5.button</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p2637125193411"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213440.11718994033438449542314125355622:50001231000000:2800:DE961F311BD8F836B9A493FC6B39536CB4DE6B1C874DF7EB9F226DBC799BC2E6.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

**可选择默认样式**

通过以上接口内容可以搭配出以下布局样式。

<table id="ZH-CN_TOPIC_0000001956975269__X34aa17d9f5196349a2cc4a02de20f0e53fb79ee" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975269__row149mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975269__p151mcpsimp"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213440.95956515623032993834030842351777:50001231000000:2800:76186A1ED5A1554E8E2F982D1F9CDDD0B8CAAE2184C5B4F2FFD9CAC83B90118F.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975269__p153mcpsimp"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213440.30626162995439028930639194395029:50001231000000:2800:B47B57D5B55E06F8E74503258EEE225610E5DB505D41843A627D2434B2F75003.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row154mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p156mcpsimp">Message</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p159mcpsimp">Message + showClose</p></td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row104015651111"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row161mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975269__p163mcpsimp"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213440.44939922790719243620561346818830:50001231000000:2800:6C6C3EB79AAA8BEB5FB86172D452A460FD35F24EBB6353A85091CC1BAEEAE297.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p0971121011352"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.85849165487265494297601055715834:50001231000000:2800:F947D05F05BC6412612025BDC2C3E88DB62A711F95FF7634AA48905370383309.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row166mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p168mcpsimp">Message + showClose + title</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p171mcpsimp">Message + showClose + title + button</p></td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row1567718583112"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row173mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p966718015352"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.12736138786107195768219691461266:50001231000000:2800:AE166F1F0F741E8FE6C8AFC48B6B98965B1DDD8D936BF34FAB2AA12814FB3F82.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row177mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p179mcpsimp">Message + showClose + title+ button + icon</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>

**指向型气泡**

指向型气泡默认最大宽度为“窗口或屏幕宽度-两侧 Margin”来计算，当控件最大拉伸到 400vp 宽度 时不再跟随放大。可以指定气泡距离界面边缘最小宽度，气泡到屏幕边缘最小可以到 6vp，以保证尖角与点击元素可以对齐。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.09434181222358684272102451603565:50001231000000:2800:5629B226C0731BCF51263472B8CE6A0A3E419C7518190348E879936E4756930F.png "点击放大")

**嵌入型气泡**

嵌入型气泡主要用于同界面元素混排，在界面发生滑动等操作时，可跟随界面内容一同响应。

在界面布局和适配上，嵌入型气泡应该跟随界面适配规则进行拉伸等适配。

**折叠屏**

**指向型气泡**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.75840511142526394034476151440664:50001231000000:2800:17084CE4F4D52CA90EB3871B6E7DD9AD36B452BCA7FA5C68D7A226FD8E2F3FC5.png "点击放大")

**嵌入型气泡**

跟随界面布局规则进行适配，若界面整体以拉伸为主，则跟随拉伸。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.13477179453475363810556134829562:50001231000000:2800:B02538D778641B38E4E03D5836A0EEC2048E80ABFBAA5FD423CCA6E4F13CC388.png "点击放大")

**平板**

**指向型气泡**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.85464034792678474486508031484560:50001231000000:2800:9CCC40C425F35C0739AB372E1B240CDF9BE5216B2840B9808D06CC47A02095E3.png "点击放大")

**嵌入型气泡**

分栏场景下，基于气泡所在分栏区域内容宽度进行适配，同内容区最大宽度、拉伸等规则。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.19454487378630618013901833631398:50001231000000:2800:7BD902CA6904146F62C6F7B0A6DA49D4E6F68429B8BA35CF6C86AE58565CAD0B.png "点击放大")

**电脑设备**

在电脑设备上圆角规格与手机有差异，同时会默认提供一圈描边色用于提升识别性。

宽度比例拉伸规则遵从通用规格。

<table id="ZH-CN_TOPIC_0000001956975269__Xa63f3957142a410e17cc045c8b43b44feb74e3d" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975269__row210mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975269__p212mcpsimp"><span><img originheight="480" originwidth="936" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.76137732513373452565118056899825:50001231000000:2800:3245BB63F8ECAB0B3BD15CB2BE9449B668D789E45681411C774EBC9CB8ECBD27.png" title="点击放大" width="268.5" height="137.69230769230768"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975269__p214mcpsimp"><span><img originheight="480" originwidth="936" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.77445521749246358187662551700041:50001231000000:2800:E2D443B5D7C2EEEC6E82756D289B81C68C5CF540A5537D7C9456952DD31F118D.png" title="点击放大" width="268.5" height="137.69230769230768"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row215mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p217mcpsimp">指向性气泡</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p219mcpsimp">非指向性气泡</p></td></tr></tbody></table>

**气泡箭头适配规则**

**气泡箭头可根据指向诉求，在一定范围内自定义偏移属性。箭头的边缘距离气泡边缘的默认间距为** 20vp，通过 arrowPointPosition 可以配置箭头的垂直和水平方向上的位置，有“Start”、“Center”、“End”三个位置点可以配置。以上所有位置点均位于父组件区域的范围内，不会超出父组件的边界范围。

**在极限场景下可以指定箭头指向的样式**。界面布局中某些特殊位置的极端场景可能导致尖角无法完全对齐的情况，这时可以考虑使用边缘角度进行对齐处理，提供上下对齐和左右对齐两种规格。通过 arrowOffset 来指定偏移位置，当数值为 0 时则可以指定箭头布局在气泡的边缘。以上规格可以通过 [CustomPopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#custompopupoptions8类型说明) 内的属性来支持。

<table id="ZH-CN_TOPIC_0000001956975269__X3ba12bc043f00f6ca1783807d9c96c1dcdba2a1" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975269__row234mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p717181073914"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.12232213350453636815455014174006:50001231000000:2800:1DC3F9CCC253FCCC56459B1E378E0B44170941289FE11F3CCB709FEF62660FD3.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p4889021113910"><span><img originheight="860" originwidth="1720" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213441.17394045420048089711112657254578:50001231000000:2800:1C878857EA1BE6B06DC5B4373AADCDDBBF70166E111681E4C42BEE1CCD3AA894.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956975269__row239mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p241mcpsimp">上下结构边缘尖角对齐</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975269__p243mcpsimp">左右结构边缘尖角对齐</p></td></tr></tbody></table>

## 开发文档

[Popup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup)

[Advance.Popup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup)
