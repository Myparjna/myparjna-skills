# 勾选

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/checkbox-0000001957012561
- 抓取时间：2026-04-04T08:23:25.833Z
勾选用于表示用户同意该项的描述，明确接受该选项被选中。常见的场景如：USB 连接界面的“不再提示”，图片发送时的选中状态等。单个选项独自使用时请参考 [Checkbox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox) 文档，多个选项之间有父子级关系请参考 [CheckboxGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkboxgroup) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213507.97418536195917044558451795958303:50001231000000:2800:091ED9E2518DD414D367955E7EBE9E876968D0ED3EB6DE7F1A30689531AFF1E8.jpg "点击放大")

## 如何使用

**勾选控件允许用户从一组选项中选择一个或者多个选项。**一般情况下由一个勾选图形搭配一段文本进行展示使用，也可以将勾选布局在图片、宫格或者列表中使用。

**在宫格类场景下使用多个勾选布局时，需要考虑其点击热区带来的影响。**结合人因确保勾选的热区比例足够用户可点击，且不发生热区冲突。

**合理展示选择内容的优先级别。**勾选控件建议以逻辑顺序排列选项，例如，被选择可能性的从高到低、从小到大、操作难度从简单到复杂、风险程度从低到高等。

**勾选项是界面中主要内容或操作的一个附加选项。**勾选项是否默认开启，需考虑勾选项对用户所带来的影响，默认状态不应该对用户带来负面影响。不要通过默认勾选这种方式，诱导用户或趁用户不注意时开启或关闭某个功能，如果与用户意愿违背则会带来强烈的欺骗感。

**基础样式**

勾选的样式可自定义选择，在 HarmonyOS 中使用圆形背板代替传统的圆角矩形，开发者可以通过 [CheckBoxShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox#shape11) 中的属性配置其形状，常用的有 CIRCLE 和 ROUNDED\_SQUARE，也可以使用 path 路径进行自定义绘制。

<table id="ZH-CN_TOPIC_0000001957012561__X1b53d0fe4fb4c8d13316227d4c7666575bf825f" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012561__row120mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012561__p122mcpsimp"><span><img originheight="360" originwidth="640" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213507.27282313452397289976432822296530:50001231000000:2800:17DCB2BD6C5E44F03B99FCE648E2336DF2531AA3007BF4703AF3BB92C1504B04.png" title="点击放大" width="268.5" height="151.03125"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012561__p125mcpsimp"><span><img originheight="360" originwidth="640" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213507.81212149514285240617156042896946:50001231000000:2800:43A4C6CD5B7E76391F46E47EEF52E183B3C8B4CF7C358ACAADFE9919BA8856F2.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012561__row1339414286277"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012561__p123mcpsimp"><strong>勾选状态</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012561__p126mcpsimp"><strong>未勾选状态</strong></p></td></tr></tbody></table>

**成组勾选**

<table id="ZH-CN_TOPIC_0000001957012561__Xee1c9f00565eb5cab04256823938392be0f6213" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012561__row131mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001957012561__p133mcpsimp">多选的默认选中状态为勾号，若在成组勾选中使用，当子选项有多一项或多项未被选中，则父选项会从勾号变成一条横线。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="56.00000000000001%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012561__p135mcpsimp"><span><img originheight="540" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213507.43595690611514392165556006572411:50001231000000:2800:BDAA91932CC3152C002FD7AA698862DC63D6FDAABA14F6D3CCE21A35C0C34837.png" title="点击放大" width="306.7200000000001" height="172.53000000000003"></span></p></td></tr></tbody></table>

在 电脑 设备上，多选使用小圆角形式，以体现设备风格。

<table id="ZH-CN_TOPIC_0000001957012561__开发文档" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012561__row106mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012561__X2ce36d4e6510caa3c8d6ce21d9bbd7d49f6da25"><span><img originheight="480" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213507.99045972543071746195204161018708:50001231000000:2800:CE551A9206418CF6BDC7AD4B382FA4306627CB233AF2570ACEDEE68220D82413.png" title="点击放大" width="268.5" height="134.25"></span></p><p id="ZH-CN_TOPIC_0000001957012561__p149411889423">勾选状态</p></td><td class="cellrowborder" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012561__p294178154216"><span><img originheight="480" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213507.62864689493338276659535089832351:50001231000000:2800:FEA7E5F3ED7B0DD24C19233DAF4EEFF72F41614F8FB6E601AE57125DD5389A9A.png" title="点击放大" width="268.5" height="134.25"></span></p><p id="ZH-CN_TOPIC_0000001957012561__p111mcpsimp">未勾选状态</p></td></tr></tbody></table>

**智能穿戴勾选**

勾选用于表示用户同意该项的描述。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213507.71870769277119965251615991679693:50001231000000:2800:6D9914A27302DEF05441D6316D2BED26E4337DD62CF664A0CD9A768E65300966.png "点击放大")

**界面用语超长处理规则**

超长文本状态下，字号不变，图标与文本上下居中。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213508.54403710290603632909330034319688:50001231000000:2800:CBC0325C9ACE439F9AC4D8806A329AE5F1F5F7E28156FBC88665CCEAB417960F.png "点击放大")

## 开发文档

[CheckBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox)

[CheckBoxGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkboxgroup)

[Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio)

[Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle)
