# 评分条

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/rating-0000001929853906
- 抓取时间：2026-04-04T08:23:29.604Z
表示用户使用感受的衡量标准条。开发相关描述请参考 [Rating](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.96002098259440425656270120206859:50001231000000:2800:E2151CE701016BBAE397CC5BD9C5935CD3B4345838D5E7832C5B5E301AE443BD.jpg "点击放大")

## 如何使用

**明确使用场景和评分规格。**评分条控件是一种允许用户对某个对象进行星级评分的交互控件。通过一组五个元素让用户进行选择，通过激活元素数量来提供对应分数的映射。主要使用场景为：电商应用中对商品进行评分；在线服务评价中对服务质量进行评分；内容分享平台中对内容质量进行评分、游戏、应用，或软件评分等等。

**评分等级的图形元素应该具有明确的视觉区分，避免用户混淆。**评分后应该有明确的反馈，让用户知道评分是否成功提交。开发者考虑是否需要为评分添加文字说明的输入框，以便用户补充评论。

**为了提高可用性，评分条控件应该支持点击或滑动等多种交互方式。**控件提供了基础的点击交互，用户可以直接点击想要选择的等级进行评分。也可以通过滑动多个元素进行交互，选择想要的评分等级。明确评分反馈，评分成功后，应该有视觉或文字反馈来确认评分已提交。

**根据使用场景设定滑动步幅。**评分反馈的分数与选择元素的数量有直接关系，在默认规格中，评分步幅按照 0.5 为基础值为一个单位，即每一次滑动元素递增的

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.27704107136083296838395277334838:50001231000000:2800:BAA95260D0E77249E7C60F0108C799BFBAB34A09872C28325DDE16F887A5FA74.png "点击放大")

<table id="ZH-CN_TOPIC_0000001929853906__table86669183311" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853906__row120mcpsimp"><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p122mcpsimp">序号</p></td><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p124mcpsimp">标题</p></td><td class="cellrowborder" colspan="2" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p126mcpsimp">描述</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853906__row127mcpsimp"><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p129mcpsimp">1</p></td><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p131mcpsimp">已选中星星</p></td><td class="cellrowborder" colspan="2" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p133mcpsimp">必选。可配置默认状态是否为选中。</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853906__row134mcpsimp"><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p136mcpsimp">2</p></td><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p138mcpsimp">未选中星星</p></td><td class="cellrowborder" colspan="2" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p140mcpsimp">必选。可配置默认状态是否为全部未选中。</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853906__row141mcpsimp"><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p143mcpsimp">3</p></td><td class="cellrowborder" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p145mcpsimp">评价文字</p></td><td class="cellrowborder" colspan="2" valign="top"><p id="ZH-CN_TOPIC_0000001929853906__p147mcpsimp">可选。不同评价等级为不同文字。</p></td></tr></tbody></table>

展开

| 
**可操作评分条**

 | 

**不可操作评分条**

 |
| :-- | :-- |
| 

用于如应用商店、购物场景、应用/功能的评分。也可以横向滑动对内容进行评分，跟手滑动状态变化，支持步长为整颗星星。

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

135

 | 

不可操作评分条仅用于评价量化展示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213510.13013900069659435263510513544483:50001231000000:2800:3B236083893CDA64F62185F5765742E79027CC89B5568C484A410992CEBE914C.png "点击放大")

 |

## 开发文档

[Rating](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating)
