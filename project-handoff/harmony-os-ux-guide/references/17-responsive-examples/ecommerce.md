# 电商购物类

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/responsive-design-examples5-0000001930419478
- 抓取时间：2026-04-04T08:25:00.087Z
购物、买菜等服务类型的应用或业务场景，旨在让用户享受高效的浏览和互动。这类场景的核心是浏览商品、商品比价、直播购，因此，在大屏设备上可以向用户展示更多的商品选择，提供更轻便高效的交互体验。此类应用有如下特点：

-   界面布局舒适美观
-   展示更多的商品信息
-   高效的详情对比
-   快捷流畅的界面交互
-   关键信息无干扰

## 首页

### 首页的沉浸广告

<table id="ZH-CN_TOPIC_0000002330924390__table110mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924390__row114mcpsimp"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924390__p118mcpsimp">在电商购物应用中，首页通常会有入口图标和商品卡片等丰富的商品信息。通过对入口图标进行挪移或延展，商品卡片增加列数的方式高效适配多端设备尺寸，从而提升大屏设备上界面布局的舒适性、美观性和浏览效率。</p></td></tr><tr id="ZH-CN_TOPIC_0000002330924390__row119mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924390__p13531164812146"><span><img originheight="1521" originwidth="4178" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110525.09439168414604868726773130167256:50001231000000:2800:00E3E9556C0E5A6B6ABA579B6B0DDADDDBAE55CF85EBEFE77E9114E952B5E9EE.png" title="点击放大" width="587" height="213.69722355193872"></span></p></td></tr></tbody></table>

### 首页的卡片响应式布局

有多张卡片时，在宽屏设备上采用延伸布局以露出更多卡片。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110526.17067360035967039306378780090075:50001231000000:2800:0E343C651185D229223464D60F2FD80DAF5AB13CA6D87E09FB1ADFCFC31982D6.png "点击放大")

只有两张卡片时，在更宽的设备上卡片自适应形变。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110526.58616269093545698861352803288264:50001231000000:2800:07571EA1C96C0AA00CD0CB6A3A05049742E75420A95961C1DB3D07A72FB1E165.png "点击放大")

只有一张卡片时，在宽屏设备上卡片自适应形变 + 挪移布局范式一：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110526.29782734631111628221315725298915:50001231000000:2800:F467CD046571C5D62164760F8F7B0D0ABCBCAFEF27E192A3C133173C1AA7D44D.png "点击放大")

只有一张卡片时，在宽屏设备上卡片自适应形变 + 挪移布局范式二：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110527.21408571793685053661178327367062:50001231000000:2800:ECDF4F40D8F4DB95411732F17D97A56269379E84A2F4404D5C7B570FF9EEB397.png "点击放大")

本场景的开发指南，请参阅[一多开发实例（购物比价）-首页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section1976644133811)。

## 商品分类

商品分类页主要用于快速查找目标商品，在大屏设备上建议通过分栏布局提升查找效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110527.53736473324195108601361617144512:50001231000000:2800:3326117C1015DBFE7B7F588AA4FD270370BB0A0643A7944791CEE7740AE57709.png "点击放大")

本场景的开发指南，请参阅[一多开发实例 (购物比价)-商品分类页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section1048762514385)。

## 商品搜索

为了避免进入整屏搜索界面时产生的大面积跳转，同时也为了规避搜索联想词列表的留白问题，在折叠屏/平板上建议采用轻量化搜索体验。当用户点击搜索框/搜索按钮时，原地激活搜索框，使用搜索面板承载推荐内容和搜索联想词，保持界面布局的整体稳定性。

说明

**注：应用根据自身业务属性决策是否在首页使用，推荐运用于二级频道页。**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110527.43232684134139199996927866255711:50001231000000:2800:BC7918588C806C1233138C4ABA577762B5A0314A1F72D0800602433D71C62F27.png "点击放大")

## 商品详情

商品详情页中通常有顶部的商品图片，在折叠屏上建议通过延伸布局露出更多商品图片，在平板上建议从商品列表到进入商品详情时，提供分栏体验，帮助用户更高效的查找商品。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110528.52047756912545903132503002170375:50001231000000:2800:80C6CF12BAE2FAEED7ECE52B9A512397070881A6CFF6917ABE3CCC53FD512CA5.png "点击放大")

平板上分栏布局时，点击全屏按钮，进入全屏，显示全屏的挪移布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110528.75440819516485560123665224608089:50001231000000:2800:4A39AEC7D2046FB9F763C2AED0E4B32DC96D83C328B544AFACB8694B331C4F89.png "点击放大")

也可以为平板提供默认的全屏体验，点击商品卡片直接进入商品详情。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110528.22902595004714488665700579086705:50001231000000:2800:DA2222EA898E24EA8E9C627A875D4B3A90AD52B2FE9B345A5E157A4D994B498E.png "点击放大")

本场景的开发指南，请参阅[一多开发实例 (购物比价)-商品详情页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section112893356386)。

平板上挪移布局显示商品详情时，查看下一层级内容时，建议使用以下两种范式。

范式一：在商品详情页，点击评论等功能进入下一层级页面时，通过侧边面板显示下一层级内容：

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

114

范式二：在商品详情页，点击评论等功能进入下一层级页面时，原来的全屏界面被缩窄，右侧露出的面板上显示下一层级内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110529.92106990740899030583837856744300:50001231000000:2800:8A329D1938B9EF4CEDB19D29A51A25CD0424931B02C9C44C8BE8C38D0219C44B.png "点击放大")

本场景的开发指南，请参阅[一多开发实例 (购物比价)-商品详情侧边面板页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section8305102524814)。

## 分屏购物比价

查看商品详情时，在宽屏设备上，可点击应用内“分屏”按钮进行分屏，可满足同时查看两个商品的详细参数进行购物比价的诉求。

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

101

形成分屏后，“分屏”按钮自动切换为“全屏”按钮，可再次点击“全屏”按钮回到当前获焦窗口的全屏，退出另一侧的分屏任务。

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

85

多端的应用内分屏购物比价效果：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110529.55851152801797099793466215647284:50001231000000:2800:A7BBE56FA831550044C67D812F6D94683073678216E64EC9D787D7BAF8918E20.png "点击放大")

## 侧边面板咨询客服

在查看商品详情时，经常会有咨询客服的诉求，可采用侧边辅助面板显示客服对话等辅助信息，从而提升浏览效率，实现边看商品详情边聊天咨询的体验。

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

79

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

67

侧边面板同样可用于更多场景，例如在商品详情页临时打开购物车、查看评论、查看店铺信息等。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110529.80260734069653432853643241909726:50001231000000:2800:D94B23CECCD87E5748EF4E6F86D79755D8F223DF16A713F7F808C05469665ED3.png "点击放大")

## 购物车

购物车页面通常用于快速查看并支付待购买的商品。折叠上可全屏适配显示更多关键参数信息，平板和更大尺寸的屏幕设备的显示区域较大，为避免界面留白较多信息过疏，建议采用重复布局、露出辅助信息等方式确保页面的使用效率。

范式一：重复布局

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110530.64386357156779617032329772251840:50001231000000:2800:7DE90513050231783ABF0DEF0AAABC657B9CD651082D0AB6B3F2832AA2F38D65.png "点击放大")

范式二：右侧露出辅助信息

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110530.56537251171027215070397499706789:50001231000000:2800:047955A2244A67D3734ACB3BB16FC280F08931289E3DA923572D48C131B3A267.png "点击放大")

本场景的开发指南，请参阅[一多开发实例 (购物比价)-购物车页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section49871612174810)。

<table id="ZH-CN_TOPIC_0000002330924390__table225mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002330924390__row229mcpsimp"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002330924390__p232mcpsimp">范式三：从列表变卡片</p><p id="ZH-CN_TOPIC_0000002330924390__p233mcpsimp">查看商品详情时，有需要临时查看购物车内待支付商品的诉求，可利用侧边辅助面板显示购物车页面，提升浏览效率。</p><p id="ZH-CN_TOPIC_0000002330924390__p959813815109"><span><img originheight="1521" originwidth="4178" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110530.40306487405069695515372766778184:50001231000000:2800:6B144419A789A17935CBBBC98E95E7C564B025F0777EB014B4E1F94BC38536FA.png" title="点击放大" width="587" height="213.69722355193872"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002330924390__row235mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%">&nbsp;&nbsp;</td></tr></tbody></table>

## 浅层窗口支付

全屏商品详情支付时，采用浅层窗口可以有效避免大面积的页面跳转带来的体验中断。平板和折叠屏上调用居中的半模态控件；手机上调用底部半模态控件，来实现浅层窗口体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110530.27925335048809563863682635253697:50001231000000:2800:6C567BCC840214B7B3A67EC6A480080F871F73B46624407407CF5E7FCCEFF47F.png "点击放大")

本场景的开发指南，请参阅[一多开发实例 (购物比价)-商品支付页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section1965713469388)。

## 直播购物

直播购物在电商购物场景中很常见。

### 全屏直播间

直播画面和推荐的商品信息，在多端基于设备屏幕尺寸进行响应式适配。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110531.40591283685212623494856482730097:50001231000000:2800:760244AD95F9594BB4523468F3EC18149F00188DB7BFC7DD3003D9DBAE58B872.png "点击放大")

同一设备上，可根据直播画面比例进行自适应的布局适配。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110531.82599537518804603813996942797048:50001231000000:2800:D1FBA78B5BE540F60861529A1B04F77BC95ACE4459034A935B449B423DDC4BA7.png "点击放大")

本场景的开发指南，请参阅[一多开发实例 (购物比价)-直播间页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section838561613490)。

### 边看边买

**直播 + 商品详情**

在看直播时，经常需要一边听商品讲解一边浏览商品信息，可利用侧边辅助面板查看商品详情，提升购买决策效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110531.97187473215833794200820871336827:50001231000000:2800:9DA215CF4C4C1FCC2444ADD163E4D62010EB5EAA84E449CE5036E035491B7AB6.png "点击放大")

**直播 + 直播间购物袋**

看直播时，会有临时查看直播间中直播商品的诉求，通过侧边辅助面板可快速查看直播间购物袋直播商品，提高浏览效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110532.35425886299602994351625394548143:50001231000000:2800:4DEBFABDEEE96B042D0163D4611E523977F613DBC67EDB8642F86E374BC76FA2.png "点击放大")

**直播 + 支付**

看直播时，可以通过侧边辅助面板直接进行支付，确保任务不会被中断和支付效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110532.02175597273092606830877836777025:50001231000000:2800:42B47FADF97BD6CDCFB24C2D76E85AF767DE981AFD1F187D4208F022ED79F5AC.png "点击放大")

本场景的开发指南，请参阅[一多开发实例 (购物比价)-直播侧边面板页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-shopping-price-comparison#section972591693910)。
