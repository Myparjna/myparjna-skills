# 三折叠

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/trifold-0000002352915021
- 抓取时间：2026-04-04T08:24:30.901Z
## 概览

三折叠手机是一种具有特殊形态的终端设备，支持单屏态、双屏态、三屏态等多种形态，适应不同应用场景，打破终端场景边界，实现一机多能。三折叠手机具备更大的屏幕尺寸和更灵活的形态，给用户带来更极致、高效的使用体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160054.85945810505872380263866130620570:50001231000000:2800:2C50E9C571DB8E0C32BE1D2409DD4D7C0FDB909A62DE5AAE92DA85565D232714.png "点击放大")

## 基础要求

### 横竖屏适配

三折叠手机在三屏态下的横竖屏比例存在差异，为了确保流畅的使用体验，建议应用适配横屏和竖屏布局，实现不同屏幕方向间的无缝接续。适配过程中，应注意避免应用界面撑不满屏幕、强制竖屏、留白、页面元素比例失调等情况的出现。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160054.39332382608838405094975481076306:50001231000000:2800:2B698F718EAB1D7C1FC3E2CEBC1887D95BA25D833CB46FBE1ED9F344E43EDE6D.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160055.46699883700139280783911807865831:50001231000000:2800:9CC5A4695C11221158F981E2B8365594F0B227B88677135667B81D3E3759F478.png "点击放大")

推荐：不同形态横竖屏的响应式布局

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160055.17632981585300252791035254511912:50001231000000:2800:449EBC0B96FDBBFCF55E19E531446625534F3756B1B7253300DB35C18EC923C2.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160055.11603200831425147145826868000794:50001231000000:2800:56E45B9260235AE7BD338986FCB9C3B1210ABDC46414D4FD64864C0454EA20E7.png "点击放大")

不推荐

### 交互跟手

**跟手弹框**

为了减少用户操作路径过长的情况，在双屏态和三屏态可通过跟手弹窗进行展示，弹出框的弹出位置离手更近，以便用户能够快速操作。跟手弹框详细规格，请参阅[弹出框比例与界面布局](https://developer.huawei.com/consumer/cn/doc/design-guides/dialog-0000001957012569#section5639104752013)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160055.32899014405917281467450104955873:50001231000000:2800:4FB92C19A36560C0F29ECF12307B673C93031E2DD6A3A45155DC5159903C1A46.png "点击放大")

**跟手半模态**

在单屏态，半模态窗口通常从屏幕底部弹出；在双屏态，建议窗口居中显示；而在三屏态，可以考虑跟手半模态窗口或者居中半模态窗口显示，具体根据业务需要选择。

跟手半模态详细规格，请参阅[半模态比例与显示布局](https://developer.huawei.com/consumer/cn/doc/design-guides/bindsheet-0000001956852753)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.18921722243724569168174068908358:50001231000000:2800:B0D3691B47D8B6AC4431FC5657435206420D797F6B6C2684356EF25E6FBFBC40.png "点击放大")

## 开合接续

在单屏态、双屏态和三屏态切换时，应确保页面不发生跳转，焦点不发生偏移。

### 页面不跳转

在三折叠设备折叠开合过程中，需要保证当前任务的连续性。不应出现页面跳转、操作步骤增加，操作更复杂等体验下降的情况，同时确保任务状态的保存和快速恢复。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.13121199221811665050568891500505:50001231000000:2800:445D6F0DE7E7941B2ABE7A6DF8F800A3BA6D9821C54547D59445A4EAB46F643A.png "点击放大")

### 焦点不偏移

确保用户当前浏览内容、图片等焦点区域保持视觉稳定，焦点不发生偏移。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.00218655478958073107031159246719:50001231000000:2800:7DD88412BE09C74A5D13220BD2B9628DBC210EF3916107996602E59EA4FBD237.png "点击放大")

## 应用架构

### 导航栏

为提高大屏幕状态下设备的交互易用性，建议在三屏态横屏使用侧边Tab，将底部Tab结合挪移布局的方法，挪移到左侧。侧边tab的导航选项继承底部 Tab ，适用于导航结构简单的内容型应用。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.41947917521494298946052262900802:50001231000000:2800:4FD9D0C24E80E3A15153DC217BA6A619C62448A9C86CAF14CD0A6497555CBABC.png "点击放大")

### 两分栏

分栏布局可以帮助用户在宽屏设备上更高效地处理任务。三折叠设备分栏布局在折叠展开过程中保持分栏样式，分栏后两侧窗口分别基于栅格进行窗口内的布局。三屏态屏幕较宽，建议统一按照屏幕宽度减掉侧边导航后再计算内容区域的宽度。详情请参阅[分栏规范](https://developer.huawei.com/consumer/cn/doc/design-guides/design-responsive-layout-structure-0000001748539684#section194871434192212)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.73219728568719929482276061379637:50001231000000:2800:4CF2ABD4C8A261A5BA386EA49AA946BF2AB7C5D1A9DE477ACDCB0F5B4E19A8BD.png "点击放大")

### 三分栏

三屏态下可支持三分栏布局，原来父子关系的层级页面可拆分后平行显示，使侧边导航抽屉完全展开，充分利用屏幕空间。在双屏态和单屏态下，导航抽屉收起至导航按钮，点击后展开为悬浮导航面板。详情请参阅[响应式应用架构](https://developer.huawei.com/consumer/cn/doc/design-guides/design-responsive-layout-structure-0000001748539684)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.10741764325471244321335897236944:50001231000000:2800:9662593FABFEB4744BF5F3C580776C830EEA59D039BCCB1C69E0443D1B765348.png "点击放大")

## 响应式布局

### 重复布局

为避免结构过于单调且信息量过少，可通过重复布局来改善页面的浏览舒适度和使用效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.33922482747106091131316668714342:50001231000000:2800:C6687F08577707ACB6408707893E9F9ACBB81A72D539D8D4487A9FFB94A0EA44.png "点击放大")

### 延伸布局

在宽屏设备上可以使用延伸布局，同时结合设备的物理尺寸适当进行形变、自适应裁剪，确保更好的显示效果。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.88008423144824274412283802408907:50001231000000:2800:647C8654C38F9F61087E4832F20B1D2662A40E81274A1B326EC8CB9A983E0EEA.png "点击放大")

### 挪移布局

为利用屏幕宽度优势，避免在宽屏设备上内容仅横向延伸过于单调，在宽屏设备上可使用挪移布局，将上下结构变为左右结构。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.54689329986382317856617628885286:50001231000000:2800:330134CD7F525FCD3C760A9CF5D6711B5EF0279FF9357F6119F8FEA73BDE3A6C.png "点击放大")

详情请参阅[响应式布局方法](https://developer.huawei.com/consumer/cn/doc/design-guides/design-responsive-layout-method-0000001795698449)。

## 价值场景

### 边看边评

为了更有效地利用三折叠屏幕空间，在带有评论的页面场景中，我们建议在双屏态和三屏态下将评论区挪移到右侧，以实现边浏览观看边评论的效果。这种布局适用于影音娱乐、新闻阅读和图文笔记等场景。

**影音娱乐类**

观看短视频时，在单屏态下，评论区从屏幕底部弹出；而在双屏态和三屏态下，建议将评论区从右侧展开，以实现边观看边评论的效果，从而不影响视频观看体验，提高用户体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160056.70950621299221165362693478398530:50001231000000:2800:1D874C22842EBEE38B86392898621BB79033043AEA8B4516131CD35C0365A95C.png "点击放大")

**新闻阅读类**

当用户阅读新闻详情时，为确保沉浸式阅读体验，默认全屏图文显示。同时允许用户手动切换布局，将评论区挪移到右侧，实现边看边评的效果。详情请参阅[应用设计最佳实践-新闻阅读类](https://developer.huawei.com/consumer/cn/doc/design-guides/responsive-design-examples4-0000001746657290)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160057.42589258875376775354927064703262:50001231000000:2800:EEB4749E2C0B5CA43DD3C6929394B1A35CFE1A7A18AA8E5E8ED7E63290F17989.png "点击放大")

**图文笔记**

在阅读笔记详情时，随着屏幕变宽，在双屏态和三屏态建议采用挪移布局：将文字挪移到图片右侧，以实现左图右文的图文对照效果。在双屏态中，我们建议按照6:4的图文区域宽度比例进行布局；而在三屏态中，建议该比例为1:1。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160057.19585553826349076381168895795338:50001231000000:2800:17CAB6AC54FC61F308BDAD47A5DA0ACAA096E6006746D3783A4DC80AFE097302.png "点击放大")

## 增值体验

**自由多窗**

三折叠设备在三屏态时可开启自由多窗模式，支持同时开启多个应用窗口，允许用户自由调整尺寸、位置及堆叠层级，实现高效的多任务操作。应用窗口可在最小档位与全屏之间无极调节。详情请参阅[平板自由窗口](https://developer.huawei.com/consumer/cn/doc/design-guides/pad-0000001823654157#section1768267204717)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251110160057.24746334805846106472269024029051:50001231000000:2800:DD9346911DA58365167656A3FB36345D3096742A23FE8262C9B1E0D32914B57B.png "点击放大")
