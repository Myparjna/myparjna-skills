# 旅游住宿类

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/tourist-accommodation-0000001957241545
- 抓取时间：2026-04-04T08:25:04.307Z
旅游住宿、订票类场景通常包含火车/飞机订票，订酒店，查询票务信息等核心功能，围绕此核心功能，此类场景旨在让用户拥有流畅沉浸的用户体验，提供更轻便高效的交互体验。

## 购票

### 首页

首页通常主要展示查询车票的入口、入口图标区、热门资讯和酒店预订等信息。

平板上充分利用宽屏优势，采用挪移布局，左侧查询车票的入口、入口图标区、热门资讯固定，右侧酒店卡片可以纵向滑动。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110551.65823301680616561466495988115228:50001231000000:2800:DAED2D6EB532EDDAC49901E031CE0E95DD44A1A34C431973B0AF20F2D3405C36.png "点击放大")

### 时间选择

选择查询车票的时间，折叠屏、平板和电脑通过系统的半模态控件，拉起日历控件。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110552.43314413932786668489863606141298:50001231000000:2800:F0989507E2BD9828884E9175F41A69726525ABA6B5C0624C6806168D89D15351.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（旅行订票)-时间选择页。](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation#section147288193403)

### 车票查询

查询车票结果页面展示查询日期当日的车次卡片，在折叠屏上保持原有布局，在平板、电脑上使用分栏布局提高效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110552.57892614087175384682083529465533:50001231000000:2800:74265E7E95DB16A4F09B02B61D2EF47E22FEB1CF2FB89141471692440DABF841.png "点击放大")

上滑之后日期上移至标题栏，收起上方子页签、操作块等元素和下方工具栏，以展示更多车次内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110552.20303326621874369074807048371196:50001231000000:2800:977511985E2E6E2511AE4A8357BA6CE201ECF6E13C6C0B91DB645817ADF571AF.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（旅行订票)-查询车票上滑](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation#section052546194213)。

### 信息填写

在平板、电脑上使用分栏布局提高效率，左边选择车次，右边填写用户信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110553.85689452585941531568959271574980:50001231000000:2800:5F8333CABE3174B520C8394DC033D3DA8F987D24D8EAA31A3AF733D16552CEC0.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（旅行订票)-填写购票信息页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation#section3911202734415)。

### 提交订单

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110553.72430297833642868060652436680062:50001231000000:2800:E05150FAAC403BBB538C417B909D60F5A2B61EDBE475B1022B751A6916E7CBEC.png "点击放大")

## 订单

### 查看订单

手机上使用列表布局，折叠屏、平板和电脑使用宫格布局。手机和折叠屏订单页直接露出待支付或已经预定的车票信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110553.66422077979716737558022985710789:50001231000000:2800:488BB51F13BBB64E6BCAA8E73D0A67407260AC77A522C177316F34163FF3CBA3.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110553.11923312293254795636449330771193:50001231000000:2800:47C78D1A0FC89F6A2746A14D03174F0F84C628DFC6B9586BC6527BD0519B8E34.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（旅行订票)-订单信息页。](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation#section755015294519)

### 已支付订单

在平板、电脑上使用分栏布局查看订单提高效率，左边订单列表，右边订单详情。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110554.04347408717925749506266493514840:50001231000000:2800:382DFF450B7F2A631C9EBC9F94C1A11E1DF9E26C7AD0EFE948F440F30B5D182E.png "点击放大")

## 实况通知

实况通知是一种帮助用户聚焦进行中任务、方便快速查看和即时处理的消息提醒，包含胶囊态、卡片态。在购票出行等场景中十分实用：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110554.73922336640723641698087422388156:50001231000000:2800:E5701EFDF63ABAC027FC29E8BEDCDB38377FADD420675171E4F0C7DB91FC8858.png "点击放大")

## 酒店

### 酒店首页

使用卡片样式的广告图，在宽屏设备上广告卡片延伸布局，同时结合设备的物理尺寸适当进行广告卡片的形变，广告图内容自适应裁剪。需要确保卡片样式的广告图在多端都有较好的显示效果

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110554.24649660660031717350746609199989:50001231000000:2800:6625448FBB6970E8F52E102385D6EC0AF15A2F88949082ED936DC776F2D52AD2.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（旅行订票)-酒店首页。](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation#section41871019476)

### 酒店排行榜

手机、折叠屏上使用沉浸式banner，平板、电脑上采用左大右小的布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110555.81845752805152017883601062905437:50001231000000:2800:6C0C534E49C77D0306435A8BBD78D1F86B6F04B62EBEC41A2CE0B75651F289D2.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（旅行订票)-酒店排行榜页面。](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation#section159523974711)

### 酒店详情

手机上使用可以左右滑动的上面酒店图片，下面酒店详情的布局。宽屏上使用左图右详情布局

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110555.14217311950874501807593145220758:50001231000000:2800:82D006B5B08CFBF2D57F151E56B74135F029F78C6E55BCBB0D3105D5C09D60C0.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（旅行订票)-酒店详情页。](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-travel-accommodation#section185431244812)
