# 列表

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/list-0000001929853910
- 抓取时间：2026-04-04T08:23:32.936Z
列表是展示重复性内容的常用界面元素，良好的列表设计可以提高用户的浏览和查找效率。列表的通用组件能力可以参阅 [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list) 控件规格，关于列表的布局能力以及组合能力可以参阅 [ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem) 以及 [ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163649.71961805601674394348112349893252:50001231000000:2800:FA6B698B34254E6101FEAD34394BEC053941DAA3DEA6147B4560D49DD6AF7D4B.jpg "点击放大")

列表控件包含一系列相同宽度的列表项，适合连续、多行呈现同类数据，例如图片和文本。列表作为可以按组展示信息的控件，也提供多种交互的能力，例如长按出菜单 (可参考 [bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu12) 开发文档) 或可以滑动列表进行删除、置顶、收藏等功能。

## 如何使用

优秀的列表设计需要在内容展示、视觉美感和交互体验之间寻求平衡，以满足不同场景和设备的需求。因此，开发者需要更多注意列表内容的结构是否清晰，能否帮助用户轻松识别到核心内容。

**清晰的列表结构**

当列表出现在同一界面或是同一分组时，请使用一致的视觉样式，如间距、对齐方式等。通过文本大小、颜色对比来区分不同层级的列表项，从而达到突出核心内容的目的，除此之外，可以在列表右侧提供一些交互选项，确保每个列表的内容与交互事件是独立分区的。当内容条目或种类过多时，适当使用分组或分类有助于用户快速定位内容，可以使用[子标题](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheader)展示分组标题。

**易于阅读和识别**

在复杂的界面结构和列表信息中，突出显示关键信息才能使用户能够快速获取核心内容。首先要精简列表的文本数量，若文本内容较长，可以提炼核心文本作为一级文本，其他的文本用较淡的颜色和更小的字体展示在下方。对于较长的列表项可考虑使用多行布局，如果有一段描述文本可以拆分成多个列表项，请务必将这些列表成组显示。

**明确的选择反馈**

用户对于列表操作需要提供明确的反馈状态，因此开发需要定义列表的点击态、选中态以及激活态等事件。不同的状态要有明显的视觉变化，如颜色变化、勾选状态等。

交互状态

<table id="ZH-CN_TOPIC_0000001929853910__table515042516226" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row615082572220"><td class="nocellnorowborder" style="border: none;" valign="top"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p130mcpsimp"><span><img originheight="492" originwidth="988" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163649.67706304803666321905128338785000:50001231000000:2800:020FCCDBBBC228972538E998BB46FACA31E24C07056D62D413EF967A3A38981E.png" title="点击放大" width="637" height="317.2105263157895"></span></p></td><td class="nocellnorowborder" colspan="2" style="border: none;" valign="top"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p132mcpsimp"><span><img originheight="492" originwidth="988" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163649.45965776890867654946528041365459:50001231000000:2800:CAFCF1AA71C16776A0C5E2334A6E5D7A296D640A98AAF43C761D5BD24D2DB9DD.png" title="点击放大" width="637" height="317.2105263157895"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p134mcpsimp"><span><img originheight="492" originwidth="988" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163649.71894923699854182603150082549724:50001231000000:2800:2B41FACE21B41BEBE8B2A82FE8BFBDE7FB7732F6E05C3A2A67981AE19EE2558A.png" title="点击放大" width="637" height="317.2105263157895"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p136mcpsimp"><span><img originheight="492" originwidth="988" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163649.11377882644320616455216117030608:50001231000000:2800:A6BAF0077EF57B95CDFB05A5FE920CBE62DD7D20DE95C63FEEEB2A64A274D339.png" title="点击放大" width="637" height="317.2105263157895"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p138mcpsimp"><span><img originheight="492" originwidth="988" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163649.18101513045652990989788283902779:50001231000000:2800:7903FBD4C3AB409FDC3A5AE63E25E089D486E98DB12B4DC5D65437B7E6C918B7.png" title="点击放大" width="637" height="317.2105263157895"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929853910__row1150192532218"><td class="row-nocellborder" style="border: none;" valign="top"><p id="ZH-CN_TOPIC_0000001929853910__p141mcpsimp"><strong>悬浮态</strong></p></td><td class="row-nocellborder" colspan="2" style="border: none;" valign="top"><p id="ZH-CN_TOPIC_0000001929853910__p143mcpsimp"><strong>点击态</strong></p></td><td class="row-nocellborder" style="border: none;" valign="top"><p id="ZH-CN_TOPIC_0000001929853910__p145mcpsimp"><strong>选中态</strong></p></td><td class="row-nocellborder" style="border: none;" valign="top"><p id="ZH-CN_TOPIC_0000001929853910__p147mcpsimp"><strong>不可用态</strong></p></td><td class="cellrowborder" style="border: none;" valign="top"><p id="ZH-CN_TOPIC_0000001929853910__p149mcpsimp"><strong>获焦态</strong></p></td></tr></tbody></table>

## 组件规则

### 视觉规则

优先显示列表中的文本，文本作为列表类组件和核心传递内容，是重要组成部分，因此，在文本的布局、排列、色彩以及内容自适应上，都需要着重关注。

文本的描述应当简洁、精炼，这可以大幅度的减少因为文本描述而导致的换行、布局调整等问题，同时保持界面的整洁度。如果列表中的内容由大量文本组成，需要考虑文本的展示结构是否可以分级显示，或是作为辅助文本出现在列表的下方，而不是整体都展示在列表内。

**信息层次**

根据信息的重要性，使用不同的字体大小、颜色和粗细来区分。详细可以参考[视觉](https://developer.huawei.com/consumer/cn/doc/design-guides/color-0000001776857164)规范中对于文本色的使用，分别使用一级文本、二级文本和三级文本来对内容做段落的区分。

次要信息可使用较小的字体或灰色字体，同时，如果应用中的列表有明确的分类规格，可以使用[子标题](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheader)来对列表内容进行分组，这样是有效的对界面布局进行划分，提高用户的阅读效率和界面信息展示的密集程度。

**适度的装饰与布局**

适量使用图标、缩略图等装饰元素，有助于快速识别和理解。对于大部分的效率型应用，列表的展示更多是作为信息入口提供给用户，用户看见的应该是明确表意的文本信息，而不是各式各样用于表意的图标或者插画。

对于其他大部分内容应用来说，列表内的装饰很大程度上可以为界面的美观度增光添彩，但需避免过度装饰，从而影响内容的可读性。配图的选择和尺寸占比与列表的宽高有直接关系，开发者需要在界面展示信息密度和设计效果中做取舍。

内容密度越高、结构越复杂，列表之间所需要的间距就需要越大，因此列表的行高需要根据内容的复杂程度进行一定的处理。为了保障视觉感受的一致性，不要将不同结构和布局的列表强制放在同一个分组中，这种行为会造成视觉上内容的不对齐，影响正常的阅读效率。

**响应式布局**

开发者需要根据不同屏幕尺寸动态调整列表的布局，在较小屏幕上可考虑使用单列布局或隐藏次要信息，当屏幕占比较大时，可以选择分栏布局展示。同时，针对屏幕拉伸场景下，列表内的左右元素也需要进行对应的适配，确保文本和元素的对齐方式不发生变化。

### 可横滑列表

对于列表内容的更多交互行为可以通过横滑列表触发，开发者可以将删除、转发、收藏等行为展示在滑动后的列表布局中，请参考开发者文档中关于 [SwipeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#swipeaction9) 的相关描述进行布局规格的自定义。

横滑后的布局中建议使用表意明确的图标进行展示，避免用户的主观猜测。同时，请克制滑出的内容数量，一般情况滑动后出现的操作数量宽度不大于列表宽度的一半，最多不超过三至四个选项，选项过多会造成滑动触发困难，滑动所需的距离阈值通常为操作区宽度的二分之一，因此，请选择核心且重要的列表行为作为操作项。

**列表式**

<table id="ZH-CN_TOPIC_0000001929853910__X0c1e21711c58d799f96652edfcba32b3347ebba" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row275mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p277mcpsimp"><span><img originheight="1440" originwidth="1482" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.10511778711910539895018627068163:50001231000000:2800:BF327F585137F245B42F705B31CD403BD46B0F8B54379835ADB406A5F3A5DD79.png" title="点击放大" width="268.5" height="260.8906882591093"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p279mcpsimp"><span><img originheight="1440" originwidth="1482" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.15834671285182018750240835151412:50001231000000:2800:99E0D3272E632CC636CF56DD411B82F47D4B03398B3F2E6A65A1A429B7A9E96B.png" title="点击放大" width="268.5" height="260.8906882591093"></span></p></td></tr></tbody></table>

**卡片式**

<table id="ZH-CN_TOPIC_0000001929853910__X1525ef0df9f3e7b946135974a86fddb0fe81a21" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row286mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p288mcpsimp"><span><img originheight="1440" originwidth="1482" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.30829576509260593047959240709490:50001231000000:2800:02AEA0994165498E12D5D7DBACF40384CBC546235A16A34FD5010515E70521B5.png" title="点击放大" width="268.5" height="260.8906882591093"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p290mcpsimp"><span><img originheight="1440" originwidth="1482" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.03102469362104383029450276080750:50001231000000:2800:69E363D728CAD8BBE7362FC05C03237C1E756A069407B7FED5D6D77CB08F5769.png" title="点击放大" width="268.5" height="260.8906882591093"></span></p></td></tr></tbody></table>

## 设备差异

### 手机设备

**左侧元素**

<table id="ZH-CN_TOPIC_0000001929853910__X2df2b374b15058dadd658b96578b0c8d1d322b9" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row180mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p182mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.51115498458555806713400162244784:50001231000000:2800:1AA900A96E14952B191ABCF340470CACA53BD3F9392D0D33DFB0791FD1CED9BB.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p183mcpsimp">Badge</p><p id="ZH-CN_TOPIC_0000001929853910__p184mcpsimp">8×8vp</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p186mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.79897169770847054677371431201601:50001231000000:2800:0B31EF1F19F5A22ADBDF632295708632B94BA03AED541ED4498FA001453EF6E9.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p187mcpsimp">系统图标</p><p id="ZH-CN_TOPIC_0000001929853910__p188mcpsimp">支持 16x16、24x24vp</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p190mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.97612162455235544076265841254302:50001231000000:2800:C716B784DF08F2AC83CA5F4663E52F0D71E733064AB16AD750D092C44229D40C.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p191mcpsimp">头像</p><p id="ZH-CN_TOPIC_0000001929853910__p192mcpsimp">支持 40、48、56vp</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p194mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.69015303091561141830646855556335:50001231000000:2800:B6A20D871903C4D5B72B4C99FE663B7D36A9E22B344C5D54879B4BF0A53DEC66.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p195mcpsimp">1:1 预览图</p><p id="ZH-CN_TOPIC_0000001929853910__p196mcpsimp">支持 48、56、72、96vp</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853910__row197mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p199mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.13911240522383344068862188081721:50001231000000:2800:38138A4052F96375754360B7A04E1DFCE31EA4AD9E2172970A96215B5A842D6E.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p200mcpsimp">应用图标</p><p id="ZH-CN_TOPIC_0000001929853910__p201mcpsimp">支持 48、56、64vp</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p203mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.19774117733838266326667506661042:50001231000000:2800:A422D6120FB2AFB9507FE68A480C596A4B48C76C5BDEBFE0D9330C2C471294D7.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p204mcpsimp">16:9 预览图</p><p id="ZH-CN_TOPIC_0000001929853910__p205mcpsimp">保持最长边 96vp</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p207mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163650.10396342880657714106649923114330:50001231000000:2800:968FDC695435346995C8336E2B8AEBB64F15381DA3CF426EFDD7AC39A9C69E6A.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p208mcpsimp">13:18 预览图</p><p id="ZH-CN_TOPIC_0000001929853910__p209mcpsimp">小尺寸：默认高度 64vp</p><p id="ZH-CN_TOPIC_0000001929853910__p210mcpsimp">大尺寸：默认高度 96vp</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p212mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.69484040734188123910424072682340:50001231000000:2800:D03C0BE90D994BD4F4ED1B53DEE1B131657002CDC7A0B6BF276A7626ECED50AB.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p213mcpsimp">3:4 预览图</p><p id="ZH-CN_TOPIC_0000001929853910__p214mcpsimp">小尺寸：默认高度 64vp</p><p id="ZH-CN_TOPIC_0000001929853910__p215mcpsimp">大尺寸：默认高度 96vp</p></td></tr></tbody></table>

**右侧元素**

右侧支持功能图标或文本或图标 + 文本的组合。常见样式见右侧。

右侧元素与中间列表内容保持 12vp 间隔。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.97177243721914162935011090652574:50001231000000:2800:608D9DCA78D83C4EBB8F1580368C01051562CCF085EA36FFD3B981A8A74FE8B8.png "点击放大")

**效率型列表**

效率型列表主要以“纯文本”以及“纯文本 + 图标”的样式呈现，右侧元素可按需组合。

效率型列表在默认参数下通用高度为 48vp、56vp、64vp、72vp 和 96vp，特殊场景可按需增减。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.15624036112256561716478061346914:50001231000000:2800:05A2D098E93180741A3A99EEE6D9476EBA77C3E48F8081E57A09B5A89D439189.png "点击放大")

**内容型列表**

内容型列表主要以图片资源与文本混排的形式呈现，右侧元素可按需组合。

内容型列表由于展示图片所需高度更多，因此通用高度为 64vp、72vp、80vp、96vp 和 120vp，特殊场景可按需增减。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.73818376557257297846068450196200:50001231000000:2800:0064C575C5FC350C77B74EA98AF66EE72410317014DB83E6B06704713EFF03A1.png "点击放大")

### 电脑设备

**左侧元素**

<table id="ZH-CN_TOPIC_0000001929853910__X96922d86a6d5b54c92dbfc6e3f59bd8672e812c" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row234mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p236mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.23342796255945070331922224393514:50001231000000:2800:0935D74088AC48EDFEB13B8D40152566F7CBAC2FF8B15C9514AF06645F817B87.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p237mcpsimp">Badge</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p239mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.35866308320069936317081109143244:50001231000000:2800:FB34F814C549B2E6A2FD6BFF4E2F0799FDFCE55AFC2F1EB802AF8730693B9616.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p240mcpsimp">系统图标</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p242mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.93247930057466258088604759130345:50001231000000:2800:CAA85E63322CA7F241502CC72B7A0D89459573789AF452002B6EB447ABEB1726.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p243mcpsimp">头像</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p245mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.34936454124379563947834258396331:50001231000000:2800:3C57F44407CA1CF41D3F50E5C9A8C66ADC0A9C48CEBB726EB08DDFA3C731A64D.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p246mcpsimp">1:1 预览图</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853910__row247mcpsimp"><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p249mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.85720414130271174832981588974530:50001231000000:2800:17F29A87FD808FEF36529165087FCED72608AFE59F33D08DF744BD3D29D5DC7B.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p250mcpsimp">应用图标</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p252mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.35280915603948108960917524510715:50001231000000:2800:432D350ADA87C7FFB36B3EA2DDABD57F0C032D4DC0EE0FD32A27A83F8C4952B3.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p253mcpsimp">16:9 预览图</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p255mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.68145646895963931147139283466297:50001231000000:2800:970BD4D58C99655A772AE380D095E4D46AD0BF43CCEBC3340B10BA41DB4A33EE.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p256mcpsimp">13:18 预览图</p></td><td class="cellrowborder" valign="top" width="25%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853910__p258mcpsimp"><span><img originheight="592" originwidth="592" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.24698562234389857671273165481916:50001231000000:2800:05464889D9271DD6281B333C92BC39F8892525FF186AAE68D8CE35F998767CC0.png" title="点击放大" width="109.25" height="109.25"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p259mcpsimp">3:4 预览图</p></td></tr></tbody></table>

**右侧元素**

右侧支持功能图标或文本或图标 + 文本的组合。常见样式见右侧。

<table id="ZH-CN_TOPIC_0000001929853910__table250016503191" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row125001450191913"><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p1850075051918"><span><img originheight="600" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.51496311070061271157696348915101:50001231000000:2800:AA2C40A448BC476E8CB80C98D1807A9C253055DBC1FEDAA6A691CACF9BD91D97.png" title="点击放大" width="162.33333333333331" height="101.45833333333333"></span></p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p19500125019190"><span><img originheight="600" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.86452866560106127058205708353531:50001231000000:2800:429C18C59644AAC00CEA474BB5220A29F7554DAD9C300978EAAD46D21075686D.png" title="点击放大" width="162.33333333333331" height="101.45833333333333"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p1750012507193"><span><img originheight="600" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163651.29918467374078158970970484519762:50001231000000:2800:329806BA9E42C23700D79052AD9D04F59EEF4EF3455BB958B88D5E61B08E5AFF.png" title="点击放大" width="162.33333333333331" height="101.45833333333333"></span></p></td></tr></tbody></table>

### 穿戴设备

用于展示重复性内容的常用界面元素。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.21816556673244447157482541915725:50001231000000:2800:34E78F67B66C06DC1177779F6D8D3C701E645BB07A22D6C5DD3E031640CE1DD4.png "点击放大")

**圆形表：**

**左侧元素**

<table id="ZH-CN_TOPIC_0000001929853910__table84143563579" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row74151956105716"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p577735616276"><span><img originheight="400" originwidth="400" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.03104443670366611112129807200667:50001231000000:2800:170D394EC4EFEF25FD3D4F10E9C9768DF68C181B357EDEB2A13FAD9A826DD0D7.png" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p741565611573">Badge</p><p id="ZH-CN_TOPIC_0000001929853910__p1963417901512">尺寸：8*8vp，与图标右上对齐</p><p id="ZH-CN_TOPIC_0000001929853910__p15505191191510">颜色：引用 warning（#E84026）</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p179284172816"><span><img originheight="400" originwidth="400" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.88359253183760038717866001488380:50001231000000:2800:A6241B775638B4A57B92BCC5FAF51F5C7E286D6911C5CB4D37FD1E8EDA568C3F.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p84157564579">大图标、应用图标、头像、封面</p><p id="ZH-CN_TOPIC_0000001929853910__p144094621515">46*46vp，圆形</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p911814559199"><span><img originheight="400" originwidth="400" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.79482695812190930451390364665700:50001231000000:2800:7EF8E9172C69789370A17F5B984B49E009DE9B7A1D5122746CA14EA320F04155.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p16415195655717">可操作图标</p><p id="ZH-CN_TOPIC_0000001929853910__p2060942261418">图标大小：28*28vp</p><p id="ZH-CN_TOPIC_0000001929853910__p747418258142">热区大小：46*46vp</p><p id="ZH-CN_TOPIC_0000001929853910__p4571181017149">图标颜色：引用 icon_secondary（#FFFFFF，66%）</p></td></tr></tbody></table>

**右侧元素**

<table id="ZH-CN_TOPIC_0000001929853910__table496361517585" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row3963215115815"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p34291544172815"><span><img originheight="400" originwidth="400" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.66752806829698433283536666963605:50001231000000:2800:F2D6129191F2CE794C7405F7E9993344CC2681A5479284B2A1D7AE77EB95377D.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p2963415155811">指示图标</p><p id="ZH-CN_TOPIC_0000001929853910__p205721354123416">图标大小：28*28vp</p><p id="ZH-CN_TOPIC_0000001929853910__p1045841616351">热区大小：整行响应</p><p id="ZH-CN_TOPIC_0000001929853910__p1825882316353">图标颜色：引用 icon_secondary（#FFFFFF，66%）</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p15688115316284"><span><img originheight="400" originwidth="400" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.00630261362857935195421888627040:50001231000000:2800:33655ED6531537D42D8DC48AAC6CA68E764DEAE61077C98C724159CDB210BCAB.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p189631015135810">选择类图标</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p812411149295"><span><img originheight="400" originwidth="400" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.21356393924304180264423761054156:50001231000000:2800:535731BBCBBA1FE89766288D1F3605B6E49E62B8F144329201E97AB17B05B562.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p1796391513589">操作图标</p><p id="ZH-CN_TOPIC_0000001929853910__p144401441183616">图标大小：28*28vp</p><p id="ZH-CN_TOPIC_0000001929853910__p35671547123610">热区大小：46*46vp</p><p id="ZH-CN_TOPIC_0000001929853910__p1971118323715">图标颜色：引用 icon_primary（#FFFFFF，100%）</p></td></tr></tbody></table>

单行列表

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.02945550271757993814183959656508:50001231000000:2800:EFC80366163104A72A65548A4CF07F46A0B09D4F1486A71BB20F6057C0668D50.png "点击放大")

双行列表

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.04932574527329970923347684520698:50001231000000:2800:FA60F287BBC1659340200FF6F79CB4D0C70545966631E4268C6E185976C076C0.png "点击放大")

三行列表

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.89500197185854813001767413296294:50001231000000:2800:F7BC876D4C8D605BC14C7FD9EDC5889FD11C1F2D752A68A78E1EF5FB84E77DE8.png "点击放大")

**方形表：**

**左侧元素**

<table id="ZH-CN_TOPIC_0000001929853910__table1447919513190" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row10479451171917"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p1047911515190"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.83311587265435252129623336747683:50001231000000:2800:9F9D4B3F40906FD9B85B7DCD2260EDF1B1CCFA72447442C59D4F97D9B5065FB9.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p19480551171911">Badge</p><p id="ZH-CN_TOPIC_0000001929853910__p1480251161919">尺寸：6*6vp，与图标右上对齐</p><p id="ZH-CN_TOPIC_0000001929853910__p15480115141911">颜色：引用 warning（#E84026）</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p048055151917"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.94373910391421576597556274905503:50001231000000:2800:98FF08427E23267BABD1F29D7B64EF8D522976BEB6F29D4DB2CEFF833ABA2686.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p174802515194">大图标、应用图标、头像、封面</p><p id="ZH-CN_TOPIC_0000001929853910__p134801514195">35*35vp，圆形</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p9480185161917"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.88277299282511164669849106016245:50001231000000:2800:F2FEE6186D010E36319892CEB13D2D523F009E391B6A354BA32EA0EDC536621A.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p13480551171911">可操作图标</p><p id="ZH-CN_TOPIC_0000001929853910__p19480251101919">图标大小：28*28vp</p><p id="ZH-CN_TOPIC_0000001929853910__p7480125111199">热区大小：40*40vp</p><p id="ZH-CN_TOPIC_0000001929853910__p848065116199">图标颜色：引用 icon_secondary（#FFFFFF，66%）</p></td></tr></tbody></table>

**右侧元素**

<table id="ZH-CN_TOPIC_0000001929853910__table1248045121912" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853910__row1648085114194"><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p1248085111195"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.01443015687997738563566676961635:50001231000000:2800:7A95028F61D309FE424C6078595C10EAA2A34C28181AD91AF593983BF0A0D3F3.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p17480551161917">指示图标</p><p id="ZH-CN_TOPIC_0000001929853910__p848015101917">图标大小：28*28vp</p><p id="ZH-CN_TOPIC_0000001929853910__p14480175141920">热区大小：整行响应</p><p id="ZH-CN_TOPIC_0000001929853910__p248035110199">图标颜色：引用 icon_secondary（#FFFFFF，66%）</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p1848110518192"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.90584919950237083706929952705514:50001231000000:2800:E8B8E6562266D664B003D90B8D75CFD30BA712022C8280363A101D42D4B28A3D.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p84816512194">选择类图标</p></td><td class="cellrowborder" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853910__p1248145110192"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.58582725684278502701718941866279:50001231000000:2800:C753B1EFF62453560AC3C659578C197C5692D12398CF1D793C04A217A5D9B679.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p><p id="ZH-CN_TOPIC_0000001929853910__p8481145131912">操作图标</p><p id="ZH-CN_TOPIC_0000001929853910__p7481451191913">图标大小：28*28vp</p><p id="ZH-CN_TOPIC_0000001929853910__p1848185111918">热区大小：40*40vp</p><p id="ZH-CN_TOPIC_0000001929853910__p44812515193">图标颜色：引用 icon_primary（#FFFFFF，100%）</p></td></tr></tbody></table>

单行列表

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163652.22261818887031346928584502200427:50001231000000:2800:6DD5767B65A4A5B14E4347BE55EA370ABF962838343EC02EC7E3AE90FB5A025A.png "点击放大")

双行列表

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163653.15648567775559614835843038128277:50001231000000:2800:4E6A81928BDC91E3500E3D7E1B60B0EE5ADD5E8B49BCCF9D6E888A02C980A927.png "点击放大")

三行列表

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163653.17181608654518731671712715234516:50001231000000:2800:5A849285D00DBF7E0E6FD01EF3FC1CFFD9D6C54F0F6665F2F2A12D6D12D8C39C.png "点击放大")

## 开发文档

[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)

[ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem)

[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)

[Subheader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheader)

[HdsListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitem)

[HdsListItemCard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitemcard)
