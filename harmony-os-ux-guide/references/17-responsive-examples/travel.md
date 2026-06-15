# 出行导航类

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/travel-and-navigation-0000001957391017
- 抓取时间：2026-04-04T08:25:06.888Z
<table id="ZH-CN_TOPIC_0000002364802841__table103mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002364802841__row107mcpsimp"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364802841__p110mcpsimp">出行导航类场景通常包含查询地点信息，路线建议，导航，打车等核心功能，用户可以通过悬浮面板体验到面板与底层地图间的交互，围绕此核心场景，此类应用有如下特点：</p><ul id="ZH-CN_TOPIC_0000002364802841__ul111mcpsimp"><li id="ZH-CN_TOPIC_0000002364802841__li112mcpsimp">手机使用底部半模态面板，其他设备上使用侧边半模态面板</li><li id="ZH-CN_TOPIC_0000002364802841__li113mcpsimp">面板支持多档位高度滑动调节</li><li id="ZH-CN_TOPIC_0000002364802841__li114mcpsimp">面板默认高度，需要依据屏幕尺寸的不同而有所区分，充分发挥屏幕尺寸优势</li><li id="ZH-CN_TOPIC_0000002364802841__li115mcpsimp">折叠屏&amp;平板上侧边的半模态面板支持用户自行拖拽至左侧或右侧位置</li><li id="ZH-CN_TOPIC_0000002364802841__li116mcpsimp">建议折叠屏和平板等宽屏设备上，Tab 放置在半模态面板内</li></ul></td></tr><tr id="ZH-CN_TOPIC_0000002364802841__row120mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%">&nbsp;&nbsp;</td></tr></tbody></table>

## 首页

1.  直板机上使用底板的半模态面板。在折叠屏、平板等宽屏设备上，使用侧边的半模态面板而非全屏拉伸的底板面板，减少面板对地图的遮挡。
2.  面板默认高度，依据屏幕尺寸的不同而有所区分：手机和折叠屏设备使用「中」高度的面板高度，减少对地图的遮挡。宽屏端设备因为屏幕空间足够，面板默认以最高高度展示。
    
    ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105600.43470811677647225666278871564316:50001231000000:2800:29192A6E580DC6F3BA20AD495898AF62B12F88BB7471FBE7072ED154216C04B2.png "点击放大")
    

半模态面板的开发指南，请参阅 [API 参考 (bindsheet)。](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition)

### 面板支持多档位高度滑动调节

面板默认以「中」高度展示，露出快捷功能和常用地点，方便用户快捷操作；面板下拉可收起，仅保留露出搜索，释放更多的屏幕空间给地图；面板上滑可以进入最大高度档位，可为展示更多内容信息；点击地图可以完全隐藏/显示面板。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105600.65629160597669235686630784246367:50001231000000:2800:493430E4BBBA452E733C151BA422D37DDFB0789A88009670976B32CAE8C79DEA.png "点击放大")

**面板高度：低**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105600.89510693191650623797771779363362:50001231000000:2800:5601C2B9D77D283ADB98E611DE65F75C6A08E1AADB315B5277EE7BC92042489D.png "点击放大")

**面板高度：中**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105600.34292346978502886221408011060862:50001231000000:2800:8F30AC8CF95BA756ABCE9283D62BFACD100C13DC9A3BDEB7AC151F81A48AAA78.png "点击放大")

**面板高度：高**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105601.42442992769542706087265164531432:50001231000000:2800:FFC9F14E2D3CF9236B2E2A9A99379C0BB5FE1221A8DCFE893C56CA05A4CE4F84.png "点击放大")

**面板隐藏**

面板隐藏时，可以达到沉浸式浏览地图的体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105601.59880312023166926748372934303212:50001231000000:2800:1153C5F87652A788493EEFA7628261BCBEC3DEACF4EC9EBA79E4073D2969D408.png "点击放大")

**多档位高度滑动调节面板高度**

点击地图空白处可以隐藏面板，再次点击可以显示面板。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105601.39774611894176868467548186138973:50001231000000:2800:CCB3DE99AB6DFD483DFBC1A306D91D88788BC3220374CDFA1A854E33405AD1F2.png "点击放大")

### 创新布局

考虑到用户体验，以及左利手/右利手不同的操作习惯，面板在折叠屏和平板设备上可以拖动至屏幕右侧。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105601.09838701592246450992360162925955:50001231000000:2800:3F42A35D8EAB72BE93BF1C3AAD9EB06D428835B04BF0291A6D20216DAAC7A161.png "点击放大")

**侧边面板可拖动**

在折叠屏和平板设备上，半模态面板默认固定在屏幕左侧，可通过面板上方 bar 来拖动至屏幕右侧。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105601.55988968625633881286997420713867:50001231000000:2800:1AEE59E92BDBF922D6AD849B13A058C41845C09D84408C2C045D00873ED3FEC7.png "点击放大")

### 地点详情信息

**范式一**

地图选点后，多端设备地点详情在原有面板上覆盖展示 (以确保足够的运营类商业露出)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105601.02160051767395217304949576308335:50001231000000:2800:5C800F11CA007D414933E2BDCA4970387B0AF6C5751CB1ECFDED57AB77F661B4.png "点击放大")

**范式二**

地图选点后，手机和折叠屏设备上无变化，平板和电脑设备上地点详情在位置点附近以 Popover 形式展示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105602.60011077110439265896812977712441:50001231000000:2800:25C45F568DDA8CD6E9EABB809B92A8EDE5B29640C0519F93DBEB8CEF47F19C37.png "点击放大")

**上滑查看更多地点信息**

在手机和折叠屏上滑面板可查看更多地点详情信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105602.64404211459620311940319717460353:50001231000000:2800:52DD990CA29AB8E5C2CE90EBC63392983E66E8EE93DC4F42581554930B8EF035.png "点击放大")

在平板上 Popover 区域内上滑查看更多内容，在电脑上 Popover 区域内使用鼠标滚轮滑动查看更多内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105602.78510240361204276297255291239100:50001231000000:2800:0BD62E298B7B8DC2A54403CECC0117B9A1639043EBDB66EECE31C2C104A39889.png "点击放大")

## 搜索

搜索场景是地图类应用核心功能之一，点击搜索可以拉起面板，以面板最大高度显示，搜索结果以列表结构显示。建议在手机和折叠屏上，搜索框限制在面板内。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105603.30056058871237356440517780125423:50001231000000:2800:6E2379045B33BCB7706DC1B890782729E131E4FF94B220D126DBD2C7B5DCE63E.png "点击放大")

### 下滑面板地图与面板范式一

在手机和折叠屏设备上，下滑面板可以直接以卡片形式展示结果选点详情；在平板和电脑设备上，搜索列表和 Popover 同时展示，充分利用屏幕尺寸优势，方便查看地点信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105603.86654047166040144043201418342022:50001231000000:2800:AAC2A8B712E37ABA87CF6DCE6622B80ED9E3555379EB411750FA9A994A9B8FC7.png "点击放大")

### 范式二

在手机和折叠屏设备上，搜索结果面板下滑，仍显示结果列表与地图多点定位；在平板和电脑设备上，搜索列表和 Popover 同时展示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105603.80105994166730367674204494460129:50001231000000:2800:0252175252A0FF8A19F7ABE19C6587F68E617F6DEB933A105AF71D158A43D7D1.png "点击放大")

## 路线

在多设备上，点击面板内的起点/终点输入框可以拉起面板，以面板最大高度显示，搜索结果以列表结构显示。建议在手机和折叠屏上，输入框限制在面板内。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105603.63401269085440719145433075462041:50001231000000:2800:A0F98AFCEEDDA93D6CB1AB69D541B42328EDE27C054A171F97F534B44E2E4720.png "点击放大")

### 路线建议

在手机、折叠屏和平板设备上，路线搜索结果默认以面板中高度显示，同时展示面板内的路线建议和地图中的路线展示，可以达到更好的使用体验；在电脑设备上，路线结果使用列表结构。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105604.52244855244451515728377680195058:50001231000000:2800:078A03B7076ED50C9EE595231F5CCEB21345A6A1D2376345E5B798FB37D0F643.png "点击放大")

**自适应布局**

在折叠屏和平板设备上，面板内的路线结果使用小卡片样式显示，在上滑至最大高度后，路线推荐方案布局自适应变化，可以提升在大屏设备上的使用体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105604.54538550877464219893983372228500:50001231000000:2800:53FC9C296850845EE1F6E92CB367FD3CA9878C3CA53EBACBDC26F5981D4B7365.png "点击放大")

### 导航

导航功能作为出行导航的核心场景之一，建议多端设备上统一设计方案。在手机设备上，顶部背景面板与底部半模态面板使用沉浸式的设计，与设备边框不留间距；在折叠屏和平板设备上，沿用悬浮面板的设计，部分内容在大屏上通过自适应布局带来更好使用体验；在电脑设备上，无导航功能，可以通过点击路线结果，展示具体的出行方案。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105604.81243653207791288609575329582507:50001231000000:2800:44F74BEC9CE40A6DB1B32269A5351E5D78F767A2F8D2276216B89C6B51EC1727.png "点击放大")

### 打车

打车功能在出行导航场景中经常用到，因此在面板首页有固定的打车入口。进入打车页面时，多端设备上面板高度默认中档位高度显示，展示打车目的地搜索框和常用功能区域，地图上显示打车起点定位。在手机上，同时展示半模态面板和地图选点；在大屏设备上，露出更多地图，提升使用体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105605.12226112119599919707313436901947:50001231000000:2800:C2A6C71447EA74E9069C8716415B61048F7A93E55FCFC4D25BCD53A9A5E16C32.png "点击放大")

**选择车型**

选择起点和终点后，进入车型选择列表，在多端设备上，车型列表在半模态面板上展示，打车路线在地图上展示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105605.44360188518953890745439419414679:50001231000000:2800:B5B130D6F3819111EDAD645DCF54F69C7ABD64FF6BE42812690F10AB35728866.png "点击放大")

**便捷打车**

另一种打车方式通常是在搜索地点结果后，在推荐路线页面，侧边面板上横向选择出行方式为打车，可直接打车。在多设备上，侧边面板的内容一致，在大屏设备上有更大的地图体验效果更好。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105605.15906862603690240694056503078702:50001231000000:2800:58A8D7B8B69A2DD9B4E45E5090DCB624DEDC0DA5CCC528BDEBEFBDA25BC1C1C4.png "点击放大")

## 实况窗

实况通知是一种帮助用户聚焦进行中任务、方便快速查看和即时处理的消息提醒，包含胶囊态、卡片态。在地图导航场景中，导航和打车时都可在实况通知中展示重要信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105605.85457899945309461921958469356128:50001231000000:2800:513A72779B8770D8CD6889B7D494BE738DFDDE6CABC9F3F0E1D020169AEF70B1.png "点击放大")

### 多种状态

1.  同一个事件活动在不同场景下仅出现一个形态，如当前事件所承载的落地页在前台，则当前无胶囊；如当前为通知中心/锁屏，则不显示胶囊。
2.  通知中心的实况通知卡片会默认显示在顶部，避免滥用对用户造成打扰。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105605.95681467909079759649886248218588:50001231000000:2800:8133A998E4C4AF7E745AE34E0BEE37286B9C8E986C1120A0CBE5AA76E7B463A8.png "点击放大")

实况窗的开发指南，请参阅 [Live View Kit。](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/live-view-kit-guide)

## 服务卡片

1.  在地图导航场景中，将此类应用的重要信息或操作指令以卡片的形式展示在桌面，通过点击可以直达对应的功能界面，从而直达服务，减少体验层级。
2.  用户在桌面服务长按卡片即可发现编辑选项，点击后进入编辑界面。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105605.96505121187887757311772927477990:50001231000000:2800:6C2B4A9C4A97F50BE446A397126B67BDC677E44EFB387BD7A8761FA671D13F95.png "点击放大")
