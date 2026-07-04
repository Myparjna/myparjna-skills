# 状态按钮

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/togglebutton-0000001956842045
- 抓取时间：2026-04-04T08:23:14.663Z
状态按钮用于从一组选项中进行选择，并可能在界面上实时显示选择后的结果。通常这一组选项都是由状态按钮构成。开发相关描述请参考 [Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle)文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213454.19105635166193772066846687201277:50001231000000:2800:3EB43BFED727A525DD701EE35F11DF7A760F80009BB9E35DFEDFE7708657F1A4.jpg "点击放大")

## 如何使用

状态按钮有已选择和未选择两种状态。

状态按钮不单独使用，通常由多个状态按钮组成一组选择项。

多个状态按钮作为单选选择时，只能有一个状态按钮处于选择状态，并作为当前的选择。

多个状态按钮也可以组成多选选项，每个状态按钮都可以被选择，根据业务的需求，也可以设定其中某些状态按钮为互斥状态，即选择一个后，另一个状态按钮就自动设置为未选择状态。

## 视觉规则

**手机**

<table id="ZH-CN_TOPIC_0000001956842045__Xb557c2644ed0a8c0682488c7cf983f79271a558" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956842045__row116mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956842045__p118mcpsimp"><span><img originheight="1616" originwidth="1616" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213455.05177342935126538347342865066321:50001231000000:2800:459CBC229EF9AA42BA29DB4B03F8454A99F3EF2A0664B4FA966BEC441CD6C171.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956842045__p120mcpsimp"><span><img originheight="1616" originwidth="1616" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213455.20438646619946725391083853190485:50001231000000:2800:58F43BB1A85727261A5228BCF06EB37221C8D2C24894063E3B67D536EC6CD22D.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956842045__row121mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956842045__p123mcpsimp"><strong>未选择状态</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956842045__p125mcpsimp"><strong>选择状态</strong></p></td></tr></tbody></table>

**电脑设备**

在电脑设备上圆角规格与手机有圆角参数差异

<table id="ZH-CN_TOPIC_0000001956842045__Xffdcd298c51d672a990500b6eba6926a69f562d" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956842045__row131mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956842045__p133mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213455.61113905923173800092816902502682:50001231000000:2800:17646ACA71E039E834B024880D846606F4D39995F24E9C9AC0827B9F8E8AAC00.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956842045__p135mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213455.47330347536667480167720919094379:50001231000000:2800:2718AD9993C0C6720A1D5EA41F809A23BB4AB4A54DE62D7579F1C7DA7596EEE5.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956842045__row136mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956842045__p138mcpsimp"><strong>未选择状态</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956842045__p140mcpsimp"><strong>选择状态</strong></p></td></tr></tbody></table>

## 开发文档

[Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle)
