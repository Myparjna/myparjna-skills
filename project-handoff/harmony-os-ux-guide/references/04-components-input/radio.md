# 单选框

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/radio-0000001929853288
- 抓取时间：2026-04-04T08:23:27.735Z
单选是一种只能用于在互斥选项中进行选择的控件。开发相关描述请参考 [Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.08426255387171806778120703423653:50001231000000:2800:6BCA5D2FC7E91C95B1FC079F40F44A9676E0614B33C6651DCA61436463AE151C.jpg "点击放大")

## 使用场景

**单选控件多与列表和宫格类布局组合使用，用于在多个列表或宫格选项中选择一个。**选择内容建议控制在一屏内，超出一屏的场景可能会在阅读选中项时无法直接找到被选中内容。若内容多于一屏场景可以考虑使用[下拉按钮](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select)控件。

**当有推荐选项或者是用户常用选项时，建议默认选中。**若默认项对用户选择产生干扰，则不要默认。当用于对立相反的选项且只有两个选项时，例如同意、不同意，这两个选项应该整合为一个勾选控件而不是使用单选控件。

**不要在单选的情况下使用勾选。**单选与勾选是彼此互斥的功能控件，如果需要组合使用也应在不同的组别分类内分别使用。单选控件只能选择一个选项，选择新选项时会自动取消之前选中的选项。

**合理展示选择内容的优先级别。**单选控件建议以逻辑顺序排列选项，例如，被选择可能性的从高到低、从小到大、操作难度从简单到复杂、风险程度从低到高等。

**自定义单选样式。**开发者可以默认调用勾选的系统默认效果，同时开发者可以自定义资源样式，通过传入资源的方式来匹配业务诉求和风格差异。使用 [RadioIndicatorType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio#radioindicatortype12枚举说明) 接口来配置不同的效果，TICK 代表勾号样式，DOT 代表圆点样式，也可以使用 CUSTOM 样式来自定义资源。

<table id="ZH-CN_TOPIC_0000001929853288__Xe61a7e345d215bf4d44097e78493ea868424e6c" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853288__row121mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853288__p123mcpsimp"><span><img originheight="360" originwidth="640" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.01932797110177329795218246157347:50001231000000:2800:300BF616F6860E1871633F282EFAC10B050556A411FD83A0DE155F425C382E27.png" title="点击放大" width="268.5" height="151.03125"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853288__p126mcpsimp"><span><img originheight="360" originwidth="640" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.50837018460733313680538876181917:50001231000000:2800:3D2E8D6B8C420A16D27AAB1F1D2AABA3E5754AEBF21BABBA49C51BCC93141D3C.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929853288__row14362182013286"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929853288__p33625203287"><strong>默认 TICK 选中状态</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929853288__p9362220102812"><strong>默认 TICK 未选中状态</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001929853288__row8962123372819"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001929853288__Xcb9dd5bdfd2d8468d94b86c1a6b55cbda70ea54"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929853288__p18748111911518"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.73179993840423973765742742774060:50001231000000:2800:2592546832DD2DC853972C07A1C88C2951F7394BC264D6F4CDB811227D638615.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929853288__p1770142995114"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.83908682904551881301700186914082:50001231000000:2800:ECA562E18F9B1B37AB9EF97784985D2148DED5275663C21363C49434851AD01D.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929853288__row1113113714280"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929853288__p130mcpsimp"><strong>DOT 默认样式</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929853288__p133mcpsimp"><strong>CUSTOM 自定义样式</strong></p></td></tr></tbody></table>

## 开发文档

[Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio)
