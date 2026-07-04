# 索引条

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/alphabetindexer-0000001956975265
- 抓取时间：2026-04-04T08:22:59.955Z
索引条主要针对按字母顺序排序的列表进行快速定位。用于快速精确定位，如：联系人列表 (查找联系人)、天气、世界时钟 (添加城市)。开发相关描述请参考 [AlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154036.25842478444930449232575501536593:50001231000000:2800:D8324E1945AE067065D5953678EC076022E37596F8067BD8A403D8B063BEEA47.png "点击放大")

## 如何使用

**索引条作为快速检索类型组件，需要充分适配设备尺寸。**例如在手机竖屏情况下时，能够完整展示索引条内容；若将手机旋转成横屏显示，由于屏幕高度限制，优先显示对应的字母索引；如果字母仍然显示不全，则使用缩略的方式展示关键字母条目。索引条可以通过 [usingPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer#usingpopup) 接口显示浮层窗口，用于展示索引内容的首字母，可以配置仅展示英文，或展示对应该条目下的所有同类型字母前缀，主要适用于中文场景。

<table id="ZH-CN_TOPIC_0000001956975265__X9bdff94261ae022c35688b5a1f4fc22fd36af80" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975265__row112mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975265__p114mcpsimp"><span><img originheight="2160" originwidth="2560" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154037.71739272743718063944261099458502:50001231000000:2800:B66AADED63802C3CE09C535FF67A5FD08D8541629366DAF948832A30321DB544.png" title="点击放大" width="268.5" height="226.546875"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975265__p116mcpsimp"><span><img originheight="2160" originwidth="2560" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154037.73481736470440761371151366823874:50001231000000:2800:2EE4376D270885E9D29FB1BA9809C40D02DCCCB9B86393AC8DFEDD2FAB8AD50C.png" title="点击放大" width="268.5" height="226.546875"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956975265__row117mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975265__p119mcpsimp">纯首字母索引浮层</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975265__p121mcpsimp">多项索引浮层</p></td></tr></tbody></table>

## 组件规则

### 控件构成

索引条控件主要由索引项、索引浮层和检索内容区域为主。其中索引项一般为英文字母，用来进行选择，切换对应选后会对内容区进行筛选，做到快速定位。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154038.29226008062089406479169171638705:50001231000000:2800:68A5AF371463ED09205D38344304099688921033D86D98319D8A2A67993A04B1.png "点击放大")

<table id="ZH-CN_TOPIC_0000001956975265__Xe60f3bf4e0daaa676da8b9a95dca060c4258b17" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975265__row129mcpsimp"><td class="cellrowborder" valign="top" width="9%"><p id="ZH-CN_TOPIC_0000001956975265__p131mcpsimp">序号</p></td><td class="cellrowborder" valign="top" width="16%"><p id="ZH-CN_TOPIC_0000001956975265__p133mcpsimp">元素名称</p></td><td class="cellrowborder" valign="top" width="75%"><p id="ZH-CN_TOPIC_0000001956975265__p135mcpsimp">描述</p></td></tr><tr id="ZH-CN_TOPIC_0000001956975265__row136mcpsimp"><td class="cellrowborder" valign="top" width="9%"><p id="ZH-CN_TOPIC_0000001956975265__p138mcpsimp">1</p></td><td class="cellrowborder" valign="top" width="16%"><p id="ZH-CN_TOPIC_0000001956975265__p140mcpsimp">当前索引项</p></td><td class="cellrowborder" valign="top" width="75%"><p id="ZH-CN_TOPIC_0000001956975265__p142mcpsimp">表示内容区域正显示由此索引项对应的内容</p></td></tr><tr id="ZH-CN_TOPIC_0000001956975265__row143mcpsimp"><td class="cellrowborder" valign="top" width="9%"><p id="ZH-CN_TOPIC_0000001956975265__p145mcpsimp">2</p></td><td class="cellrowborder" valign="top" width="16%"><p id="ZH-CN_TOPIC_0000001956975265__p147mcpsimp">快捷操作浮层</p></td><td class="cellrowborder" valign="top" width="75%"><p id="ZH-CN_TOPIC_0000001956975265__p149mcpsimp">用户在索引项列表上滑动时出现，支持点击操作，如无操作显示 3 秒后自动隐藏</p></td></tr><tr id="ZH-CN_TOPIC_0000001956975265__row150mcpsimp"><td class="cellrowborder" valign="top" width="9%"><p id="ZH-CN_TOPIC_0000001956975265__p152mcpsimp">3</p></td><td class="cellrowborder" valign="top" width="16%"><p id="ZH-CN_TOPIC_0000001956975265__p154mcpsimp">索引项列表</p></td><td class="cellrowborder" valign="top" width="75%"><p id="ZH-CN_TOPIC_0000001956975265__p156mcpsimp">展示所有可操作的索引项</p></td></tr><tr id="ZH-CN_TOPIC_0000001956975265__row157mcpsimp"><td class="cellrowborder" valign="top" width="9%"><p id="ZH-CN_TOPIC_0000001956975265__p159mcpsimp">4</p></td><td class="cellrowborder" valign="top" width="16%"><p id="ZH-CN_TOPIC_0000001956975265__p161mcpsimp">内容区域</p></td><td class="cellrowborder" valign="top" width="75%"><p id="ZH-CN_TOPIC_0000001956975265__p163mcpsimp">跟随索引项操作变化内容显示</p></td></tr></tbody></table>

### 动态布局

当设备处于横屏下时，例如手机设备，或是当应用窗口处于分屏场景时，由于可展示的应用高度不够，字母索引可以以间隔方式显示字母。 通过使用 [autoCollapse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer#autocollapse11) 接口能力可以实现动态判断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154038.41348510724153305976193380817585:50001231000000:2800:9D8CED52E2F35373DCBFB709510895418A673886EBBBB2B42F3DE2D81E6C66C9.png "点击放大")

## 设备差异

### 手机设备

<table id="ZH-CN_TOPIC_0000001956975265__X96cca9f53df389a3ab88eda9e353a81ab815e38" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956975265__row171mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975265__p173mcpsimp"><span><img originheight="2480" originwidth="2480" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154038.73478932511872552776055759514888:50001231000000:2800:79D5541022515BFCE43E5AAB067140A6C3EE7E021B4AA83B6DC28CF9330B91B7.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956975265__p175mcpsimp"><span><img originheight="2480" originwidth="2480" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154039.26776883270065889583090129222780:50001231000000:2800:ACAD9E8EF3102A03C0CDFBF1699C906EF4C279B3675ED584786603F58DCC30D9.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956975265__row176mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975265__p178mcpsimp">索引条的位置需要在界面中可以自由布局，通常情况下建议在界面中保持居中位置。在 HarmonyOS 应用中通常会将界面中的信号栏和底部工具栏/底部页签高度去除掉，然后居中展示。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956975265__p180mcpsimp">若顶部的内容还包含子页签等其他组合组件，字母索引起始位置可以考虑基于顶部组件高度提供一个默认间距，固定显示。</p></td></tr></tbody></table>

### 穿戴设备

索引条是快速定位列表内容的操作条。用于快速精确定位，如联系人列表查找联系人。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154039.03564988249737032526518892122795:50001231000000:2800:BEC5353C834ABD9AA24DC3E9716E34EAE07021CAD5EDFCFE968AD09B910DD236.png "点击放大")

**使用规则**

-   索引条最少显示 2 个索引；当索引数在索引条上量超过 4 个时，可通过点击折叠箭头> 展开或折叠索引条。
-   未展开状态下，用户可以在索引条上通过滑动交互和点击交互来获取精确定位。当用户手指滑动或点击至某一字母位置时，界面顶部有气泡提示当前字母，用户在非索引条区域滚动或点击时，此气泡消失；若用户没有操作，则 3.5s 后气泡自动消失。
-   展开状态的索引条，点击或用滑动索引条，均可进行焦点选择，此时界面有气泡提示当前字母，消失规则与未展开时相同； 滑动列表中的内容或点击箭头，可将索引条折叠。
-   展开状态的索引条弧长根据数量增长，最长可形成整圆。方形表为胶囊形。
-   多语言情况下，整圆状态下超过 30 个字符时，可隐藏一些字符并以“.”显示，焦点处于此位置时，气泡显示被隐藏的多个字符。
-   多语言情况下，一些语言需要切换至字母索引时，本地语言末尾有一个字母，点击或滑动可切换至字母语言；切换至字母索引时，字母索引上方有一个本地语言字符，点击或获得可切换至本地语言。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154039.27873024023250969274011340249419:50001231000000:2800:EF52B17B1DE7DAE55F7C1AB29CDC8597FA37A9812923ED86986C77C42F126006.png "点击放大")

方形表：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154039.67268550598073372930919706726257:50001231000000:2800:84F5E8678F08F0748740B1EBC6249DC1DBBF9E8C2B2DE724C01B9E4681461BED.png "点击放大")

**视觉规则**

圆形表：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154039.94929275212021017057366220879359:50001231000000:2800:BF30BF768432DEFA8E045279A2A45CF6C72621DFA32FA835628F1911A63DDF10.png "点击放大")

方形表：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250825154039.40780039721518042331648636050351:50001231000000:2800:BD02ABCFC72F323CC92073F5948DB59693B66E2D02420F81020F7379CEAFB6B7.png "点击放大")

## 开发文档

[AlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer)
