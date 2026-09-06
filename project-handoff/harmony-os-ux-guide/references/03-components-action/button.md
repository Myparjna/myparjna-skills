# 按钮

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/button-0000001929683228
- 抓取时间：2026-04-04T08:23:12.027Z
一种常用控件，点击可触发对应操作。开发相关描述请参考 [Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213449.40999747680680629940462818315923:50001231000000:2800:AAA4C809B5DD637CF9025A91AC98A2CAE3514605B2858FE875AE3217DF218615.jpg "点击放大")

## 如何使用

视按钮重要程度、屏幕空间大小、整体布局选择按钮类型。按钮重要程度：强调按钮>填充按钮>文字按钮。

含状态的按钮：上传、下载类的按钮可以包含一系列状态：下载，等待，下载中，暂停，重试，完成。

若用户触发将产生严重后果的不可逆操作，如“删除”，“重置”，“取消编辑”，“停止”等，使用红色警告色。

强调按钮是一种常见的按钮形式，点击执行操作。在界面上很突出，用于强调当前操作。典型场景：弹出框、界面底部按钮。例如：保存、支付、订阅、安装。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213449.63182668872608367564185794196835:50001231000000:2800:4B5F0303D67AE96660626846F4960D7931CC3A3C0EC32536F3AD49DAB37A4591.png "点击放大")

**普通按钮用于一般界面操作。**清晰的背板可以明确的指示用户可操作的区域。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.56872354634388404460386523569296:50001231000000:2800:0A953D34B4B55706CE49ED116E441512197841AB73F33A35D6C72F9B31E56768.png "点击放大")

**文本按钮为纯文本按钮，点击执行操作，可最大限度减少按钮对内容的干扰。**界面内容区 (跟随内容)、弹出框的操作按钮：需使用强调色蓝色，以便用户找到。

<table id="ZH-CN_TOPIC_0000001929683228__Xa416228e42b4658a56f23a529a709598cee1c40" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row121mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p123mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.87391560041600022088354683341326:50001231000000:2800:2BA03BBA6692B28A699713254BD5B10C28050E257F6472C94ADF958EAB0D5FB6.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p125mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.42951079195053213039930846962301:50001231000000:2800:6A5DAAAB6669E375FAC3FF2D7C27B95DAA37414EDAE7A18B89A088E8100DB2FA.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

**在显示区域受到限制时，使用图标按钮可以节省空间，让用户对当前界面内容执行快速操作。**在以下场景较为常见：标题栏/工具栏、控制中心、悬浮显示在内容上

<table id="ZH-CN_TOPIC_0000001929683228__table1349111217157" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row12491120152"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p154901241516"><span><img originheight="1440" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.15133823496548542232000979453352:50001231000000:2800:0DEBE33331D86E846A1DF2BE12713A478D312BD32DEA5A50A2C1548046D06626.jpg" title="点击放大" width="268.5" height="201.37499999999997"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p154931213152"><span><img originheight="1440" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.10909929399913231150968412514544:50001231000000:2800:0631FF9502578189452E9B17B605B54D453A44BAC6BAAF29B718786ECA6AF900.jpg" title="点击放大" width="268.5" height="201.37499999999997"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row154931261518"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p18491212141514"><strong>带容器的图标按钮</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p54921271516"><strong>普通图标按钮</strong></p></td></tr></tbody></table>

**强调按钮、普通按钮、文字按钮都可以使用等待状态。等待状态用于表达正在执行或加载的过程，操作执行完成或加载完成，则进入下一界面。**

以下使用场景用等待状态按钮替换正在加载弹出框：1. 弹出框闪现的情况。在加载极快的情况下，会出现闪现情况。2. 多个连续跳转的场景。用加载按钮减少复杂度。

## 视觉规则

**手机**

按钮样式请使用控件子样式来书写，不要直接给控件写参数，以下参数均已落地在控件中，子样式接口能力参照 [ButtonStyleMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttonstylemode11枚举说明) **和** [ButtonRole](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttonrole12枚举说明) 介绍文档。可通过接口能力实现不同的按钮风格。例如：可通过修改[通用属性 borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius) 实现电脑中的小圆角风格，详见电脑 部分。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.96472848702687042777203750383028:50001231000000:2800:9CC632E930343F209E2C97CFB645AE33976232E4CD20289F32B8EFA5F4F07C80.png "点击放大")

**所有按钮都支持两种尺寸。**按钮控件提供了两种尺寸接口，NORMAL 和 SMALL，分别对应设计规范普通按钮和小按钮，尺寸接口能力参照 [controlSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#controlsize11枚举说明) 介绍文档。

**强调按钮**

<table id="ZH-CN_TOPIC_0000001929683228__table761195218155" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row161185241512"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p3611952171517"><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.50135051400654797130129729163570:50001231000000:2800:D3238C71F458BBFDF8FE8942C0CDBC4CCF5CE5058A97BE8055FA26636973E45C.png" title="点击放大" width="268.5" height="267.38589211618256"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p36175215151"><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.84833414773803507418538552450287:50001231000000:2800:DAAC84B46834C1342C5E95044404DB6D7ADA32614006FAF8AE9030F953AD860E.png" title="点击放大" width="268.5" height="267.38589211618256"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row1761552191514"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p193488315167">默认样式</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p36175261518">多态</p></td></tr></tbody></table>

**普通按钮**

<table id="ZH-CN_TOPIC_0000001929683228__table11138202010166" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row1713902021610"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p1913919201165"><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213450.97540853465383794462468041204418:50001231000000:2800:5EB47A37C5979FA1E321CC5640567881B184D8FD8E289943C3A05E0810D36B3F.png" title="点击放大" width="268.5" height="267.38589211618256"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p12139820181611"><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.23962062670055649145317137195333:50001231000000:2800:651D211BFB997AD39DA2AB31AA3B024AE83083D59C24BD7504D473019E09A3A1.png" title="点击放大" width="268.5" height="267.38589211618256"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row113916207164"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p1571519327167"><strong>默认样式</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p39283355168"><strong>多态</strong></p></td></tr></tbody></table>

**文字按钮**

<table id="ZH-CN_TOPIC_0000001929683228__table164941146141618" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row249424671613"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p74941946111620"><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.62927392515186096477539401107783:50001231000000:2800:615836374652814496A671D37D4E7E797F88C7B915612BE7645DE8B97618DB7C.png" title="点击放大" width="268.5" height="267.38589211618256"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p3495646171614"><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.51705610029136183822756521504126:50001231000000:2800:E1D445F952AAB064DFDA6C163E8CA6EFAA6EFD7B67543075CC8ADAE6F1E16CEF.png" title="点击放大" width="268.5" height="267.38589211618256"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row1149564681616"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p104951946151611">默认样式</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p124959463161">多态</p></td></tr></tbody></table>

**圆形按钮**

<table id="ZH-CN_TOPIC_0000001929683228__table6259101281718" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row2025931218175"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p102592124172"><span><img originheight="944" originwidth="1312" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.94901198243603729456716115764129:50001231000000:2800:CFE6D9DD2CAEDD07D9AC5F3FE1713064DE7BAF90E82B4DA0070B97F89C67AD32.png" title="点击放大" width="268.5" height="193.1890243902439"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p725911211713"><span><img originheight="1464" originwidth="2036" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.00759558342976481287557334207581:50001231000000:2800:A60505B06DA593A2D76662FDB55E14A7F52203AE030EE7FF41A504A7AE26F719.png" title="点击放大" width="268.5" height="193.06679764243614"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row725918126174"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p150472210170"><strong>默认样式</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p77162518171"><strong>多态</strong></p></td></tr></tbody></table>

**电脑设备**

**在电脑设备中，使用更小的按钮圆角体现设备风格。**

**强调按钮**

<table id="ZH-CN_TOPIC_0000001929683228__X0013f6d6789cd53ffeeae86f8beee8df2006757" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row214mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p216mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.21624241396290215318524000515788:50001231000000:2800:82501C188E31D0B02A97BCAF132E9BC61003079EBC87C603D36695A79CB3388B.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p218mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.02841653464920352272909220015485:50001231000000:2800:C4B0E25E0D18029C3CEB632D1F335447A4A78468C3281C83592354EB0482C2C4.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p220mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.97923212010486211349260293368435:50001231000000:2800:ACD615D1563E5CC694ADB33A8E40363D9ED7173296F3DA18EE584644F49E0377.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td></tr></tbody></table>

**普通按钮**

支持普通按钮和小按钮两种尺寸。

<table id="ZH-CN_TOPIC_0000001929683228__X2f91c3ad9994ff3bb2a0eac7f6687743fba81ca" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row229mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p231mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.36751765738696424062700165608822:50001231000000:2800:23D4B6006AA5CFA8A0CBF1CFFE87BF004A8813B619495BB225BB18C92C7C7C12.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p233mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.53900432673427794496024282690952:50001231000000:2800:6DF56B64BECF1026F2CF15FC844B94EEAC156E269B9F52B9F235D34F1897B603.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p235mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.99027916388673212190256872013855:50001231000000:2800:4FDE1EE14BF157E32EC9B7F2C86C4C81470F957A03AC439226607D66C92E0811.png" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td></tr></tbody></table>

**文字按钮**

<table id="ZH-CN_TOPIC_0000001929683228__Xe9100d4575425991f2833578e0fb24aecfb4eb5" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row242mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p244mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213451.50685623633946708667734566577175:50001231000000:2800:F96B3D1D5AB133FCEF9460B8059663224797C8DE903C61AAE2F3FA1BAD4A15D9.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929683228__p246mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.51262965031534696633554246765726:50001231000000:2800:7CE5490B69E9551293056FB693392DCFCE2246B7B71315BDB36E2BF6D25E271E.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr></tbody></table>

**智能穿戴**

在穿戴设备中，除了圆形、胶囊、文本按钮，常用的还有弧形按钮（仅圆表），它是贴合了圆形设备的边缘而适配的常用按钮。

弧形按钮一般悬浮在界面下方，有两个弧形按钮时另一个在上方；按钮背板有背景高斯模糊效果。

**强调按钮**

文本超长则缩小2级，还放不下则跑马灯。

<table id="ZH-CN_TOPIC_0000001929683228__table4982732142615" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row1982173214267"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p1438634145715"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.84759645521127702707364303560621:50001231000000:2800:80F7BB2AE54451C0083B5666C9DCCFA63EC459BAA0A5E592380D8EAFADF76D37.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p1608138527"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.81144800737222809037967537088454:50001231000000:2800:9F3F78DB446328757AB76C1A446B45FC9BEC11CA91C680731AE03CD1FCE53D13.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr></tbody></table>

**普通按钮**

<table id="ZH-CN_TOPIC_0000001929683228__table6130034152820" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row16130133414287"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p159321652182817"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.42950783512663672802378142174320:50001231000000:2800:BC728331790227DE0B83073447DD05E6ACC5E964C1E2EDE57F1885D2825192F1.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p444417166524"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.79888648956002973424169471702769:50001231000000:2800:83E2EE930CC82680C2E7DFDE2F8C28C2FFA0FD34C67ECAF73D7DCF49C1720055.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row9131134102820"><td class="row-nocellborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p0131173432813">不可用状态，背板不变，仅文本不透明度变为 40%。</p></td></tr></tbody></table>

**胶囊、文本、圆形按钮**

胶囊按钮、圆形按钮的 3 种状态变化，与“弧形按钮”相同。

<table id="ZH-CN_TOPIC_0000001929683228__table15802174114112" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row15802184151118"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p16600541121319"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.24307996056933181135441131365235:50001231000000:2800:C6101CFC062F40F6EBF5C9066C5241D2FAFB91EBD7B46749B8C2839701B97BE2.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p1389935111418"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.10323859882803719007232349292948:50001231000000:2800:9865C1B5FD7E972B085FF24C3A36416218202E774030BDB7D636E9E83C94E064.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row4803164181111"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p2342716191417"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.94729217017975238436300586675048:50001231000000:2800:B13F572751A63F3E2F48CB893E90A21FB52B587DBF7901CD90D2FA13E5798DF8.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p18761938191814"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.59716029755885724996622715640979:50001231000000:2800:5D7700BB252E80D0CFD35B40A5CA7A2AEB1C625871806E46F842CAE6817B9152.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row14803164111116"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p134481139101413"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.32698891788421090965063284620654:50001231000000:2800:CE263635F128DE0A81E5001D22664EBC3C239C27CA78A1A87C1C69C86D25A8F4.png" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p1020224815147"><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.27979566358094413357528420183780:50001231000000:2800:26218F4B29D16156A608FC930C7438E803453328B17EB530C1FA558332FF1E78.png" title="点击放大" width="268.5" height="268.5"></span></p></td></tr></tbody></table>

## 响应式布局

**手机**

**手机竖屏**

<table id="ZH-CN_TOPIC_0000001929683228__table2040355815178" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row2403158121715"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p17403158151716"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.13297305222874533967657209820915:50001231000000:2800:A643D9C946A58C4CAA7B91CC44FA6B372CA504508897BA686788254867B52E5F.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p6403145817178"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.89616603544346018986762334785241:50001231000000:2800:67757572BB038F9DA25018DDF997015FD9753381802ADFB8A630408925701EA0.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row13403145891718"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p083915102185"><strong>单按钮&amp;双按钮布局</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p13960181211812"><strong>三个以上按钮布局</strong></p></td></tr></tbody></table>

**手机横屏**

<table id="ZH-CN_TOPIC_0000001929683228__table14777121116472" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929683228__row19777711114715"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p67771611144712"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.16511064746893520944804817594896:50001231000000:2800:570B7CCCAC4BE934E40E3CD56A806091ED45620D93F7C2C71F62C36C62BF49A0.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p57774117471"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213452.72365149591379928125937784384384:50001231000000:2800:C4BD02323515B2420D39D0B1DE8D5C6C234F1DD9A306BBA52B60AF813035BE06.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929683228__row1577701111476"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p97541145194718">单个按钮在横竖屏切换时最大扩展到 448vp</p><p id="ZH-CN_TOPIC_0000001929683228__p2075420453473">双按钮，左右布局，两者间距 12vp，总体宽度与 448vp 齐平</p><p id="ZH-CN_TOPIC_0000001929683228__p2754174574717">3 个以上按钮上下排列，按钮上下间隔与竖屏一致，间距保持 12vp</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929683228__p1977175614719">在半模态中使用遵循同样规格</p><p id="ZH-CN_TOPIC_0000001929683228__p1477656204714">半模态最大宽度 480vp 的场景下，按钮两边距离半模态保留左右各 16vp 间距，使按钮宽度与全屏显示宽度保持一致手机竖屏</p></td></tr></tbody></table>

**折叠屏及平板**

在更大屏幕上，按钮保持最大 448vp 的宽度，不再跟随屏幕伸缩而改变宽度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213453.13124339061770018917366504070013:50001231000000:2800:CBBD83832801A3230B98DC2DDCE05D70323015BC32BBCDD560C4D8E172280B69.png "点击放大")

在半模态等窗口化场景下保持同样规则，基于容器的宽度减去两侧 16vp 间距，保持最大 448vp 按钮宽度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213453.33825236966492366563314370185744:50001231000000:2800:BDA23311875BCD297BF0C6E38CADE8FBC5EEFD89A27236F08AE74623D38BB372.png "点击放大")

**智能穿戴**

单个按钮优先使用圆形按钮，如需悬浮或更清晰表达按钮含义时，用弧形按钮。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213453.89483036276418882903493570182771:50001231000000:2800:04161F52FE52EE72DA01B46264650A4448AF6D1FA12884AA6071D7FA5CE3F9E0.png "点击放大")

多个按钮可使用胶囊按钮，按钮根据内容在最大、最小宽度内自适应。（多个按钮时，按钮长度需相等）

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213453.63850371220681847504514739352038:50001231000000:2800:385D1ADB5F22E2DCFB49E6782455C65099F655D0FAFFD17C4FCEC14EF35CA7C7.png "点击放大")

文本按钮（混排）

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213453.46644864397796324451624858436711:50001231000000:2800:7CDB1EA35B8A32A0FED70D4D10343FAF605CFC3A9154869F8FA812B54EF4FC2D.png "点击放大")

通用弹出框布局

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213453.82297390712097085971569359906425:50001231000000:2800:D758E7C4DDD9B5BE565C948CF326B4157C3D3CEDE8034B47878009625D142D7B.png "点击放大")

## 开发文档

[Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button)
