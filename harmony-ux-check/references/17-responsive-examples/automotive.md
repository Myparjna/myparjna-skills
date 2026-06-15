# 汽车类

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/cars-0000001930233436
- 抓取时间：2026-04-04T08:25:10.608Z
汽车类应用主要包括首页、汽车详情、3D 看车、车辆对比等核心的应用场景。在此类场景中，用户能够选择其感兴趣的汽车品牌和其车型，在页面中观看各种参数、配件、功能等，甚至还能看 3D 汽车模型或者是更换喜欢的配色进行观察。此类应用旨在让用户在选车看车时，使用大屏设备有更优的体验。

## 首页

首页 banner 在手机上使用轮播图的形式展示，在宽屏设备上使用延伸布局同时展示更多 banner 卡片。功能区入口图标通过延伸布局在宽屏上露出更多。卡片内容使用瀑布流布局，在宽屏显示更多列数，并支持双指缩放调整列数。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110609.50202197690642396134199207071630:50001231000000:2800:CBB533CFE7EB0BFA87AABB5E3F1C43ECDB988E23654C53356322172D5F5B239B.jpg "点击放大")

同时，建议在设备上支持 banner 沉浸式无边距的设计，为汽车类的营销头图广告带来更强冲击力，提升使用体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110609.54250097556283445919351875806049:50001231000000:2800:2EC056E2B0DE594127AA1B2AF68690833D3213822743D49739D48818782B1A21.jpg "点击放大")

## 选车

选车场景主要用于快速查找目标品牌与感兴趣的汽车。

范式一：在宽屏设备上，使用自适应布局，推荐区域可以展示更多的汽车品牌，提升浏览效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110610.44905478014288520627728861740623:50001231000000:2800:1948546E081CEC65A07D3705423FB08493AA52F5C1BEEEEE4469C8A8C704234D.jpg "点击放大")

范式二：在宽屏设备上，建议分栏布局，提升效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110610.68905800344909330500484486200791:50001231000000:2800:EA2D350D264CA24865BE987AAF2DA7890B0F7732C51A3D8C116361819B28BA6C.jpg "点击放大")

## 车辆详情

车辆详情场景中，通常有顶部的商品图片，在平板上从选车列表到进入车辆详情时，可以展示更多商品信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110610.22319372739235419258543149202120:50001231000000:2800:E526C8A307BDF7D02034C10AAE52015DE5041875EA6A46476868C376F1422214.jpg "点击放大")

### 全屏3D看车

在折叠屏上，建议使用沉浸式布局，提升全屏看车的使用体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110610.72842721993008339817476738421181:50001231000000:2800:C2328B5BF35FC6DA36B5E8EEBDA4DA95D12E242E92A40FF50F196E9E30EB2E74.png "点击放大")

在平板设备上，可以显示更大的汽车 3D 模型图，视觉效果更佳。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110610.75985026750821730071976277752626:50001231000000:2800:38A0EECDF92F608E405E169BA92AD3C9CDE5B942BE2FE49AA3434DB88C25B521.png "点击放大")

3D 沉浸式看车时，旋转车身可以从不同的视角欣赏汽车。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110611.26623105679836939954033961954364:50001231000000:2800:649D7970AE2F411A77046A2EDE7C332757EF356B2F3E11949D7FF847AAF6DF63.png "点击放大")

### 询底价半模态

点击底部查询底价按钮时，使用半模态控件展示页面内容，在手机上使用底部向上的半模态面板，在宽屏设备上使用居中半模态面板。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110611.47279125030185679651767243451059:50001231000000:2800:4E796301C9E09709A01AAC5C946BD37427B2ADA81085A0CE2C81EBFF35B45FC3.jpg "点击放大")

半模态面板的开发指南，请参阅 [API 参考 (bindsheet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition)。

### 汽车评分

进入评分页面，建议整体使用沉浸式背景，减少可视化的评分区域和用户评论区域的视觉割裂感，对比车型数据使用可视化展示，提升使用体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110611.39876417289311681692698486842195:50001231000000:2800:BB0EFFD18968DCD32DB9DFD23DF8EB68883B35A99CF7E5D9C997393EB1B0B962.jpg "点击放大")

### 汽车PK

汽车 pk 场景，多端设备上页面可以使用重复布局，手机上最多显示两个车辆的对比信息，建议在更宽的折叠屏及平板上能同时显示更多列内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110611.04906484289402908829393081133869:50001231000000:2800:2263C62ADD5C824287FAE17CE096EFDE95580DDCBE23721027D6CC328696F484.jpg "点击放大")

## 视频购车

营销页面，在浏览文章/视频的同时，推送文章相关车辆，可以直接查询该车型的底价等。在手机上，使用底部半模态面板；在折叠屏上，建议使用 1:1 侧边面板展示推荐车型；在平板上，建议使用 3:2 的侧边面板展示推荐车型。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110611.53848911392599284411527079502968:50001231000000:2800:6F855ACA7C12537B54DE005D1AC88C57E01E9460DB5578195849649B8B87DDC5.jpg "点击放大")

侧边面板可以关闭，或通过底部 icon 打开。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110611.20710777159194266351222565910461:50001231000000:2800:4522B65830C7CDAD6B6B9CA258202D3CCF97604B8B226804266FC48EAA3E8944.png "点击放大")
