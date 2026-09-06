# 新事件标记

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/badge-0000001929816016
- 抓取时间：2026-04-04T08:23:01.996Z
应用中可能有需用户关注的新事件提醒，需要采用新事件标记来标识。开发能力相关请参考 [Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213435.76589287513069038169005809315233:50001231000000:2800:DDCFB4FE0C50C504785EC5D487E3136192C80C33EF94062519288DFBA550240F.png "点击放大")

## 如何使用

**在关键时刻提醒用户，而不是始终出现打扰。**新事件标记通常用于显示未读消息数量或通知数量，包括指示新功能或内容更新，以及标记任务或进程的完成状态。新事件标记的使用一定伴随有效的信息通知，而不是任何更新都需要告知用户，否则会对用户造成信息获取的困扰。

**聚类内容，不要在界面中频繁且多次的出现。**仅在必要时使用提醒，避免界面中过度使用导致视觉混乱，确保新事件标记的使用与其所在控件或内容区域有明确的关联性。可以将需要传递的内容聚类在一个列表项或者页签中，通过一个传递入口来统一告知用户。

**减少文本的展示。**新事件标记内的文本信息应简洁明了，一般使用数字直接表达数据信息的数量。特殊情况下可以用于其他运营，例如在运营内容上新时会使用“NEW”来提示用户。如果使用文本则需要控制其展示的字符数量，中文一般不超过 3 个字，英文尽量使用一个单词。

**明确使用类型。**新事件标记分为数字标记和圆点标记两个样式，其传递信息的区别主要在于是否展示具体的数据参数。圆点标记的使用更为轻量，占用面积和展示信息都较少，对用户的打扰相对较低。

**数字标记**

数字标记只显示应用中的主要事件。例如应用市场中有应用更新、活动推广等多种类型的事件。数字标记中的文本显示建议控制在 1-99 数字，超过 99 用 99 + 表示。

<table id="ZH-CN_TOPIC_0000001929816016__X416bafa0ed0d1c1bad7337aa390a25c5335f54a" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929816016__row118mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929816016__p120mcpsimp"><span><img originheight="960" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213435.05732008458698839190069537854340:50001231000000:2800:4C60912DACC477EE521304FD18CB9688CCFF3F9521ED85F22B49A8C2F6B98441.png" title="点击放大" width="268.5" height="179"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929816016__p122mcpsimp"><span><img originheight="960" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213435.96180850447177049602226307456416:50001231000000:2800:75C222884C8198B1EC4B33948FA630E057F85530120FCC995EB9A9E8DDD630F5.png" title="点击放大" width="268.5" height="179"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929816016__row123mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p125mcpsimp">数字标记展示多个文本信息</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p127mcpsimp">数字标记在列表中展示</p></td></tr><tr id="ZH-CN_TOPIC_0000001929816016__row16679143213614"><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001929816016__row128mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001929816016__row131mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p133mcpsimp"><strong>数字标记除了使用默认红色以外，结合业务场景也可以作为非警示性信息使用，例如邮件业务中可以使用新事件标题作为当前未读数据的展示。</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p1170151920121"><span><img originheight="960" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213436.29481748368579273504936098985177:50001231000000:2800:6B9A7D0BD5E30B043442FD94E7F62C7831806ADB61B37929ACA512330A4316AB.png" title="点击放大" width="268.5" height="179"></span></p></td></tr></tbody></table>

**圆点标记**

圆点标记适用于标识应用中的次要事件，通常出现在底部页签、列表项中的文本后方等。当用户点击对应内容后，圆点标记则会消失。

<table id="ZH-CN_TOPIC_0000001929816016__Xd3e9d943a67fe97db9bc9cf33c654bf23ff590c" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929816016__row141mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p19741101573310"><span><img originheight="960" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213436.20352697648626866804342878322634:50001231000000:2800:CF717AE5BE113CBA8F28B52BE516516B1B4668BC833A13C9786C775D21CD883E.png" title="点击放大" width="268.5" height="179"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p1385910031813"><span><img originheight="960" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213436.63232981552765650037843658488774:50001231000000:2800:6E530F4A71D3B3301FE040DF7A689A516C2B7FCAAD527942EF77D11D598449E8.jpg" title="点击放大" width="268.5" height="179"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929816016__row146mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p148mcpsimp">圆点标记展示在底部页签</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929816016__p150mcpsimp">圆点标记展示在文本之后</p></td></tr></tbody></table>

## 开发文档

[Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge)
