# 即时反馈

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/toast-0000001929656648
- 抓取时间：2026-04-04T08:23:03.738Z
用于在屏幕底部或中部显示一个操作的轻量级反馈。开发相关能力请参照 [PromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#showtoast) 文档中的 showToast 用法。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170634.05680488513036251454507841810260:50001231000000:2800:D70CD811A109BCAF6A2957248CE18262FDF8F927531FF0527AD3250F60702E95.jpg "点击放大")

## 如何使用

**即时反馈是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。**它通常会在屏幕的底部或顶部短暂地弹出，并在一段时间后自动消失。即时反馈的主要目的是提供简洁、不打扰的信息反馈，而不会干扰用户当前的操作流程。

**合理使用弹出场景，而不是频繁的提醒用户。**可以针对以下常用场景使用即时反馈操作，例如，当用户执行某个操作时及时结果反馈，用来提示用户操作是否成功或失败；或是当应用程序的状态发生变化时提供状态更新等。

**注意文本的信息密度，即时反馈展示时间有限，应当避免长文本的出现。**Toast 控件的文本应该清晰可读，字体大小和颜色应该与应用程序的主题相符。除此之外，即时反馈控件本身不应该包含任何可交互的元素，如按钮或链接。

**杜绝强制占位和密集弹出的提示。**即时反馈作为应用内的轻量通知，应当避免内容布局占用界面内的其他元素信息，如遮盖弹出框的展示内容，从而迷惑用户弹出的内容是否属于弹出框。再或者频繁性的弹出信息内容，且每次弹出之间无时间间隔，影响用户的正常使用。也不要在短时间内频繁弹出新的即时反馈替代上一个。即时反馈的单次显示时长不要超过 3 秒钟，避免影响用户正常的行为操作。

**遵从系统默认弹出位置。**即时反馈在系统中默认从界面底部弹出，距离底部有一定的安全间距，作为系统性的应用内提示反馈，请遵守系统默认效果，避免与其他弹出类组件内容重叠。特殊场景下可对内容布局进行规避。

<table id="ZH-CN_TOPIC_0000001929656648__table544950135418" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929656648__row1144920015419"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p44490018544"><span><img originheight="1776" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170634.40304700091091321397135475217676:50001231000000:2800:EB2F3F9ED868F4A27FB6E1DA6127336B16267B2DF2E0671FA58394389490CE9C.png" title="点击放大" width="268.5" height="248.36249999999998"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p11449170165417"><span><img originheight="1776" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170634.19688989560073471485774793077389:50001231000000:2800:99F99B881CC157E25508FAFA18D9069B86396320D232C413EB4DAA4D250A8497.png" title="点击放大" width="268.5" height="248.36249999999998"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929656648__row6449120185411"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p8540111613540">底部提示</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p1661415149544">指定位置提示</p></td></tr></tbody></table>

## 布局规则

**手机**

**响应式布局**

即时反馈默认宽度跟随文本宽度展示，基于设备宽度差异，最大宽度按照"窗口或屏幕宽度-两侧 Margin"来计算，当控件最大拉伸到 400 vp 宽度 时不再跟随放大。

<table id="ZH-CN_TOPIC_0000001929656648__table1849212212710" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929656648__row1149322171"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p1349302876"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170634.99516615787513482481378363697569:50001231000000:2800:424663AC7AA74A3E4F7B32141409588C5941FFF168936E4CB1A87EFCC997DDD3.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p14493523716"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170634.48814469327543995067521431394753:50001231000000:2800:2A30E75889468D3A23364FCD85FF81252384A0C2DC10F1A6565590B4ADEA09BE.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929656648__row24931214712"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p133000131771"><strong>手机竖屏</strong></p><p id="ZH-CN_TOPIC_0000001929656648__p12300413879">默认宽度：基于文本宽度自适应</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p15452166717"><strong>手机竖屏</strong></p><p id="ZH-CN_TOPIC_0000001929656648__p205453161718">最大宽度：屏幕宽度-两侧 Margin</p></td></tr></tbody></table>

**跟随系统色彩模式**

<table id="ZH-CN_TOPIC_0000001929656648__table7184204011819" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929656648__row918419402816"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p1612485818812"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.97446629775785633374283080108776:50001231000000:2800:05AFB3B192EC46B8FEC8AF32414557537FFC8A14F87EE18136E60DE0BDCC5472.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p178717713919"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.28772751884703206814552801254611:50001231000000:2800:67827C1039F6E46BB93CC4A7B729D6F9E4AD29B8B0957B040E43CED53A3C881C.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929656648__row218419401186"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p2298926593"><strong>浅色模式</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p175013356916"><strong>深色模式</strong></p></td></tr></tbody></table>

**距离窗口底部默认高度**

<table id="ZH-CN_TOPIC_0000001929656648__table13937152693" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929656648__row293715213910"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p1636815184118"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.43160761193321724367973317846073:50001231000000:2800:58A8140F9D86B6DC7773E8B54B705591A03466313A8EEB7645CB7E4397FD196B.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p710018268119"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.07263155379623456286757804899497:50001231000000:2800:DB7FDA943158AF93ED4F8F49AD3DBB7AB78BB78032C20B191E2A70B58C6363BB.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929656648__row9937152399"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p955918851019">弹出位置距离底部 80vp</p><p id="ZH-CN_TOPIC_0000001929656648__p1655915861015">单行情况高度为 36vp</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p1748113125102">当底部有导航条时</p><p id="ZH-CN_TOPIC_0000001929656648__p164815129107">弹出位置距离虚拟导航栏顶部 80vp</p></td></tr></tbody></table>

**手机横屏规格**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.45527814818105839999193344562090:50001231000000:2800:A8E85B71B6C5D00836B7A536AB9DF8E0BED02FDD009153C42AD6C810976AA314.png "点击放大")

**平板**

**平板竖屏**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.05762806581451707062456604571805:50001231000000:2800:3B64641BF8EE6527320AB2BB620253544A640B21144774213F6518C53D14B967.png "点击放大")

**平板横屏**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.22433662226541372751284683709506:50001231000000:2800:F21B5729BA0943A8EE9C1363E520B54756BF1D03617F2ED0A089FC5B85D2C866.png "点击放大")

**电脑设备**

在电脑设备上圆角规格与手机有差异，同时会默认提供一圈描边色用于提升识别性。

宽度比例拉伸规则遵从通用规格。

<table id="ZH-CN_TOPIC_0000001929656648__X90c5a0be2d1048648a4300e190deb44f3cdc376" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929656648__row191mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929656648__p193mcpsimp"><span><img originheight="480" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.25470553222036082952298621502017:50001231000000:2800:BB914C4A1F5A5838D5A2CF0301A097931EC5C3BE0B5C8E3EC0000CA2F6B9B3A4.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929656648__p195mcpsimp"><span><img originheight="480" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.28713731642268203322218336557305:50001231000000:2800:62081D100A4CDE26E4584025E4FB296A3CBEA17752B22368396181E8B774C52A.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929656648__row196mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p198mcpsimp">浅色模式</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929656648__p200mcpsimp">深色模式</p></td></tr></tbody></table>

**智能穿戴即时反馈**

用于在屏幕中部显示一个操作的轻量级反馈。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.01822451860059679534672954645314:50001231000000:2800:8334EC6236EFE6BB54E991F8BFF7904B01B72B3D6E0DB1A98D78DD82DBA026C1.png "点击放大")

**视觉规则**

· 文本上下左右安全距离：10vp

· 文本超长规则：先换行，默认最多3行（特殊情况可更多行）；放不下则缩小3级，再放不下则用“...”截断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260210170635.75222026778059629916209058826893:50001231000000:2800:6424604B6E14514D5EB4D964C3D91A9B4543FDAA0326054FEE4F6AB891E6D6DE.jpg "点击放大")

## 开发文档

[PromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#showtoast)
