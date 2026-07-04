# 即时操作

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/component_snackbar-0000002340726169
- 抓取时间：2026-04-04T08:23:04.778Z
即时操作组件位于屏幕底部或固定位置，用于提供操作结果反馈、状态变更提示或轻量级通知。该组件支持自动关闭或手动关闭功能，确保不影响页面其他操作。

开发文档请参阅 [HDS SnackBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssnackbar) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165643.76299400403243205843469377771036:50001231000000:2800:4E8A965654D2507A8E0272B0897E65650FB2536322DD7D936C38255BE1E984B7.png "点击放大")

## 如何使用

**即时操作是一种轻量的弹出类组件。**用于向用户显示即时信息的同时，提供简单的操作，如“撤销”“重试”。它通常会在屏幕的底部，不随页面滚动，不影响用户对页面的操作。

**根据配置类型可分为两种模式：定时关闭模式和常驻模式。**定时关闭模式支持配置5~10秒自动消失，为了减少对用户的干扰，应做到滑动屏幕时自动关闭即时操作组件。常驻模式通常用于提示登录、获取权限等对用户操作体验更重要的信息，需要提供关闭按钮。

<table id="ZH-CN_TOPIC_0000002340726169__table6512144719537" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002340726169__row17543114745313"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p512945216496"><span><img originheight="320" originwidth="508" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165643.97694138343426215683212370672282:50001231000000:2800:46F3C92352A7B444B2FBD76ACC6620332EDEEC1B8859D6A79C4383CB5221C304.png" width="268.5" height="169.1338582677165"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p68571035509"><span><img originheight="320" originwidth="508" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165643.66383615584969441156259732188441:50001231000000:2800:2BD29FC2A949F662DAD256B8AACB8A03BC398D4F5F2AFD28CDF486BD49EE2800.png" width="268.5" height="169.1338582677165"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002340726169__row1154314716533"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p125431447135311">定时关闭模式</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p05441147155314">常驻模式</p></td></tr></tbody></table>

**视觉规则**

**视觉效果**

**使用材质提升组件的沉浸感。**使用半透明材质能够在保障前景元素可读性的基础上，提升应用的沉浸感体验，避免过于突出的背景颜色影响页面的视觉感受。

**采用投影增强组件的空间感****。**即时操作组件以悬浮态存在时，通常使用投影强调信息层级，避免与页面过度融合。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165643.73046316631755026522703072760396:50001231000000:2800:51D9568240F826C6D24B5D39F0738AB58338BD0C412E9ECF3F9D9E48C0873F31.png "点击放大")

**跟随系统色彩模式**

即时操作元素颜色支持系统深浅模式配置，同时前景元素支持配置主题色。

<table id="ZH-CN_TOPIC_0000002340726169__table029717316593" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002340726169__row1829816316595"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p347714432013"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165644.35021213643243738487149133264520:50001231000000:2800:4B9F979037F04E926D37BF41E0CC978BDFA98BD3F0BD7B82F1393F7FB1FBCF12.png" title="点击放大" width="268.5" height="151.03125"></span></p><p id="ZH-CN_TOPIC_0000002340726169__p1393518125019">系统浅色模式</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p138101091903"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165644.31140138774396113972719568879818:50001231000000:2800:11F5FE4B09A9E74B4FBC4A35A90E36701EB67872EA383C7F2CEAC6388A47B2B3.png" title="点击放大" width="268.5" height="151.03125"></span></p><p id="ZH-CN_TOPIC_0000002340726169__p17850192315013">系统深色模式</p></td></tr></tbody></table>

**布局规则**

**手机****竖屏**

默认情况下，即时操作宽度为基于宽度设备差异适应窗口宽度，最大宽度按照“窗口或屏幕宽度 - 两侧 Margin”来计算，当控件最大拉伸到400vp 宽度时不再跟随放大。

<table id="ZH-CN_TOPIC_0000002340726169__table49541817111019" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002340726169__row69558179108"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p1197924621016"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165644.64893603350636881882756770283370:50001231000000:2800:452B2E5BCE6119B757C902B8BC84B72DF66E88D37C6B458A44FB51A3E020002C.png" title="点击放大" width="268.5" height="151.03125"></span></p><p id="ZH-CN_TOPIC_0000002340726169__p354031216114">弹出位置距离底部导航条 92 vp</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p19892599105"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165644.29235012538451219013830296721180:50001231000000:2800:AD273589FFFBF786BB9B1C9320BE88DEEF3AD91BD08A35CF2B9EC1461F9135F1.png" title="点击放大" width="268.5" height="151.03125"></span></p><p id="ZH-CN_TOPIC_0000002340726169__p7156105219563">存在底部页签的场景建议弹出位置距离底部页签 16 vp</p></td></tr></tbody></table>

**手机横屏**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165644.29904108347422065316023114659420:50001231000000:2800:774232E46E6D66F3F014AF4E8A1F7C79303B6EA6051F456472C57F14BE23EED8.png "点击放大")

手机横屏情况下，宽度默认最大400 vp

**平板**

平板场景下，底部避让高度与手机规则相同，默认宽度最大400vp。

<table id="ZH-CN_TOPIC_0000002340726169__table13461938141318" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002340726169__row534610383137"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p8694163151517"><span><img originheight="1112" originwidth="1975" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165645.90695899453402819197007554806467:50001231000000:2800:8B62A89A39AC86D7CE56FA4D4851C9928EDAA447CB9CED430745461D1D75982B.png" title="点击放大" width="268.5" height="151.17569620253164"></span></p><p id="ZH-CN_TOPIC_0000002340726169__p3550191619">平板横屏</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002340726169__p77361243181518"><span><img originheight="1112" originwidth="1975" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165645.79844896940027845195302124212462:50001231000000:2800:A76E59C99703900307A2BD221B7830058B235457CF4622581E6A8E50C7F64793.png" title="点击放大" width="268.5" height="151.17569620253164"></span></p><p id="ZH-CN_TOPIC_0000002340726169__p1699171417163">平板竖屏</p></td></tr></tbody></table>

**电脑****设备**

在电脑设备上圆角、投影规格与手机有差异，同时默认会提供一圈描边用于提升识别性。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251212165645.72990442396539925756427285484414:50001231000000:2800:E76B0317C9075324A039379C793B9EA079CB360F959E2604CDECEB8BA5ADE058.png "点击放大")

## 开发文档

[HdsSnackBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssnackbar)
