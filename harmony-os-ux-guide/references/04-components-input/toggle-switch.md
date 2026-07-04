# 开关

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/toggleswitch-0000001956852745
- 抓取时间：2026-04-04T08:23:26.016Z
通过开关，开启或关闭某个功能。开发相关描述请参考 [Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle#toggletype枚举说明) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213508.62479834172573419079347052786837:50001231000000:2800:92D440C58826EA94622EA0FA7821680497E0D755A14200DAACB329608CEA5BDA.jpg "点击放大")

## 如何使用

开关控件属于 Toggle 类控件中的一个类型样式，是一种用于打开或关闭某个功能和设置状态的控件，通过在 [ToggleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle#toggletype枚举说明) 中选择 Switch 样式使用。

**呈现明确的开关状态。**开关控件通常由一个手柄和一段滑块区域组成，通过点击可以改变手柄的位置，并在滑块区域给出明显的色彩反馈，用来表明当前已开启状态。即使在自定义场景下，也需要明确区分开与关的状态反馈。

**强化操作认知和风险规避。**如果开关控件控制的是重要功能或会产生重大影响的设置，可以在切换时增加确认弹出框让用户进行二次确认。

**开关控件的交互应该简单直观，避免过多的步骤或复杂的操作。**开关控件一般情况下搭配列表使用，在基础交互场景下一般用于打开某一项功能，也可以关联并绑定其他组件的交互事件，例如通过打开操作，允许用户操作另外几个列表选项。当列表项之间有关联关系时，那些未激活的列表需要变为不可用状态。

**开关控件的交互应该简单直观，避免过多的步骤或复杂的操作。**通过点击或者滑动开关来开启或关闭功能项，点击列表其他区域则不响应开关操作。

**自定义开关样式。**开发者可以使用系统默认的风格样式，基础样式可以直接修改其色彩。若对其他元素仍然有自定义诉求，例如尺寸、圆角、手柄半径等等，可以通过对 [SwitchStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle#switchstyle12) 配置不同参数来实现。

<table id="ZH-CN_TOPIC_0000001956852745__X73016c6b68801e0205738f72edd0955d925bf2e" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956852745__row126mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956852745__p128mcpsimp"><span><img originheight="360" originwidth="640" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213508.86274873743911073962481700210175:50001231000000:2800:4AEE8C074845BBC5DD2A83D5D6CED3A0D4B857FE58C945A6928B9F3B3D7C9600.png" title="点击放大" width="268.5" height="151.03125"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001956852745__p131mcpsimp"><span><img originheight="360" originwidth="640" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213508.07527315823975804021645369157583:50001231000000:2800:79A7D17670B1B8515122680B3399CDCFFA97DF6D54BE6E742DE4564F7E0247BB.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956852745__row1367445012720"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852745__p1067595042714"><strong>默认开启状态</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852745__p132mcpsimp"><strong>默认关闭状态</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001956852745__row129394002813"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001956852745__X3f5b19718d1737a0ab810afe4bb93a3b4a93a74"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852745__p19669525174715"><span><img originheight="1920" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213508.47923264748249318650324213753893:50001231000000:2800:27DE56B07778D6FEADA3485AED09E8EEEE553DD30E9AD687326E158B4D99EC5E.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852745__p977583594713"><span><img originheight="1920" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213508.91799946532782808009944882695462:50001231000000:2800:BFA8431AB8AD587C4D5D942E9EB12828B177DA54A35179065BD07237C4C87CD1.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956852745__row6508113132813"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852745__p135mcpsimp"><strong>自定义圆角和颜色等参数</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852745__p138mcpsimp"><strong>自定义尺寸和颜色等参数</strong></p></td></tr></tbody></table>

**穿戴设备开关**

通过开关，开启或关闭某个功能。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213508.09562935425300183636418248257245:50001231000000:2800:BC47232515D995606BB96A9B36175B0BC1AED8688410B59F9E39F01ABAA3F43C.png "点击放大")

**视觉规则**

圆形表：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.06342506360927819522866682891036:50001231000000:2800:40E7C1DAAFA67E8CA51DD5062724AA5A90BDCAFFAE2EC5D49F74B3E334985C39.png "点击放大")

方形表：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213509.64605428159284021149634007419172:50001231000000:2800:F842A9519B7B5D515C7ED3C17FDF2144459D12F76032AC2B5116EF3D0BE387C4.png "点击放大")

## 开发文档

[Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle#toggletype枚举说明)
