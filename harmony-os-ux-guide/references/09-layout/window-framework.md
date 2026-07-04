# 窗口框架

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/window-0000002321868010
- 抓取时间：2026-04-04T08:24:41.384Z
窗口是系统中各个应用的载体，用户通过窗口对应用内容进行查看和交互。在电脑上，窗口可作为一个单独对象进行查看和操作，通常支持打开、关闭、调整尺寸，支持最小化、最大化和分屏显示。

**主窗口**

用于显示当前使用的应用，不同应用窗口间可层叠，一般情况下，桌面上有且只有一个主窗口处于激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/QWt-Tj4NTFm28h7wSzDLXA/zh-cn_image_0000002322673226.png?HW-CC-KV=V1&HW-CC-Date=20260404T082435Z&HW-CC-Expire=86400&HW-CC-Sign=9DC1837D45436C9D738BC9ED4A863E7AFD00B43E4155AA36E849CDA6D89EAF7D "点击放大")

**子窗口**

从主窗口启动并且依赖主窗口而存在，按使用场景可分为模态、非模态两种类型，主窗口被关闭，子窗口也跟随关闭。根据应用需要，子窗口也可支持移动、响应拉伸改变尺寸。

<table id="ZH-CN_TOPIC_0000002321868010__X736e9f8802453bd4adac571bf94b5b3b8621d13" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002321868010__row176mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p178mcpsimp"><span><img originheight="1094" originwidth="1640" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/BPPf5XoBSteEB1lNdaMCTw/zh-cn_image_0000002355643361.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4948E48EB336B510E71798C07C8C6E409A25B927B4C91294D4C2CC6FACA33DB" title="点击放大" width="268.5" height="179.10914634146343"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p180mcpsimp"><span><img originheight="1094" originwidth="1640" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/EHKwSjgmTNGp3Dggyy4yAg/zh-cn_image_0000002321724690.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E0F84F53BBF0F0C8CAA348757950271FF76A3DA46653E366492A9FE696EE8F6" title="点击放大" width="268.5" height="179.10914634146343"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321868010__row181mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321868010__p680810242430"><strong>模态窗口</strong></p><p id="ZH-CN_TOPIC_0000002321868010__p184mcpsimp">模态子窗消失之前，无法对下方应用进行操作。</p><p id="ZH-CN_TOPIC_0000002321868010__p1323914113414">模态子窗建议在窗口居中出现，出现时，下方主窗口有黑色蒙层。</p><p id="ZH-CN_TOPIC_0000002321868010__p1350882912342">模态子窗跟随主窗口的移动而相对移动，最小化主窗口时也跟随最小化。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="start(2)" id="ZH-CN_TOPIC_0000002321868010__p10370182719438"><strong>非模态窗口</strong></p><p id="ZH-CN_TOPIC_0000002321868010__p189mcpsimp">更为独立的子窗，可和主窗口应用协同操作。</p><p id="ZH-CN_TOPIC_0000002321868010__p935718143354">非模态子窗建议在操作处跟手出现，出现时，下方主窗口无黑色蒙层。</p><p id="ZH-CN_TOPIC_0000002321868010__p05971928123516">非模态子窗不跟随主窗口移动和最小化。</p></td></tr></tbody></table>

## 窗口构成

窗口由容器层和内容区构成。

容器层用于展示应用品牌和控制整体窗口，通常包含标题、最小化、最大化、关闭等按钮，支持窗口操作；

内容区是用于用户与应用内容交互的部分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/aG9dzP2zQlqWmvCH0W6U_w/zh-cn_image_0000002355803273.png?HW-CC-KV=V1&HW-CC-Date=20260404T082435Z&HW-CC-Expire=86400&HW-CC-Sign=E8029C62E3D9CC74002D5EF8C514FF39E44599EC8BE06D29CA256A58FAF818B8 "点击放大")

### 容器层

必选元素：窗口控制 (最大化、最小化、关闭)

可选元素：应用图标、窗口名称

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/D8Sc7tv9Q5amAm5NwqiF9w/zh-cn_image_0000002321728150.png?HW-CC-KV=V1&HW-CC-Date=20260404T082435Z&HW-CC-Expire=86400&HW-CC-Sign=B386EEA2DA7AEEC579CE55FE4285D0E5F6B1A3FB8143F1C2588F868D94D8694B "点击放大")

窗口标题栏高度支持应用自定义。推荐在设计电脑应用时，将应用工具栏与窗口标题栏结合，减少窗口顶部层级，从而让内容区可以更高效地容纳和呈现信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/aGEHYrofSUCmwpPmbzB2jA/zh-cn_image_0000002355806689.png?HW-CC-KV=V1&HW-CC-Date=20260404T082435Z&HW-CC-Expire=86400&HW-CC-Sign=5ACF2A475056695BB02184F2160284C867FF93105E6433B36BF111509CA10C84 "点击放大")

Compact 40vp：无需工具栏、搜索等控件时，应用自定义内容

Default 56vp：适用于标题栏、工具栏、搜索栏等通用控件

Medium 64vp：适用于图标 + 文字呈现的工具栏。当用户切换工具栏显示类型时，通栏高度跟随切换

Large 72vp：应用有需求时，可扩展到最大值

**应用示例：**

<table id="ZH-CN_TOPIC_0000002321868010__table9467112012487" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002321868010__row1047516206481"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000002321868010__p154757207489"><span><img originheight="2188" originwidth="3284" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/X5kefPxwSXSw1-wk918EiA/zh-cn_image_0000002357939333.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86BD84A8D111CFEC4926242A469ADD1E70E47F7B51587F362C8544A55D3E0052" title="点击放大" width="162.33333333333337" height="108.15631343889568"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000002321868010__p1247542084818"><span><img originheight="2188" originwidth="3284" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/cQqIfC5cQ_mx0N37oYS4Ew/zh-cn_image_0000002323940766.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6BF9E047B04E1CD781DEB0806D00CC6473B2044133CCD7CC0B65B32E56A7DD0" title="点击放大" width="162.33333333333337" height="108.15631343889568"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000002321868010__p647562015489"><span><img originheight="2188" originwidth="3284" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/6sFPRzveTr260XwhhzLUlA/zh-cn_image_0000002357859225.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=033F68AE045C25099AE60F5F545B793D063438986D0A46DF153A90D80E6EF7D3" title="点击放大" width="162.33333333333337" height="108.15631343889568"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321868010__row547582010486"><td class="row-nocellborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000002321868010__p11100201194619">浏览器：使用 Compact 标题栏，节省顶部空间</p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000002321868010__p1342183864613">备忘录：使用 Default 标题栏，容纳常用编辑工具</p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000002321868010__p670918349474">天气：应用背景铺满窗口，沉浸感更强</p></td></tr></tbody></table>

当应用未做适配时，窗口提供默认的标题区背景、应用图标、应用名称以及窗口控制按钮。请结合应用场景设计顶部区域，避免仅使用基础标题栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/asZIPWDtQuCtCxUdTnb1Lw/zh-cn_image_0000002355646849.png?HW-CC-KV=V1&HW-CC-Date=20260404T082435Z&HW-CC-Expire=86400&HW-CC-Sign=CDF47FF55C2E44890CC1F58EC499290E04A8C5EEDDA3719E291FC9459B1A467D "点击放大")

### 内容区

内容区是应用展示信息的空间，应用需重点关注窗口大小改变带来的布局变化，合理利用响应式规则，确保以最佳的布局来显示内容。

应用常见的内容区布局包括通栏、双分栏和三分栏结构。详细的布局适配和响应式规则，请参阅[应用布局](https://developer.huawei.com/consumer/cn/doc/design-guides/app-design-0000002353509845#section195431623181117)。

## 交互规则

窗口标题栏提供了最大化、最小化和关闭按钮，用户也可通过双击标题栏进行最大化，或还原窗口尺寸。

窗口最大化时，默认保留状态栏和快捷栏，用户可在设置中修改为自动隐藏。应用如有需要，如视频、游戏类应用，也可配置进入沉浸式全屏。

<table id="ZH-CN_TOPIC_0000002321868010__X593f785443e214999f5b81449e53f95a9a16a8e" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002321868010__row241mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p243mcpsimp"><span><img originheight="2188" originwidth="3284" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/AJhbv023TLiZ8grzcMdnsw/zh-cn_image_0000002321887998.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D74808A7D48CE6DC12F89007C41A97173120C096144B118C2B6E666588D9AE5" title="点击放大" width="268.5" height="178.89098660170524"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p245mcpsimp"><span><img originheight="2188" originwidth="3284" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/8ewhTpXQQTed_q7Gt5J4bA/zh-cn_image_0000002323814804.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9E27597A26FA3557F8DC6F60EF3E8679CE6086C4B509B0AA46B26F88D596608" title="点击放大" width="268.5" height="178.89098660170524"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321868010__row246mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321868010__p248mcpsimp">默认最大化</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321868010__p250mcpsimp">全屏</p></td></tr></tbody></table>

## 视觉规则

### 窗口尺寸

每个窗口初次启动时按默认尺寸显示，支持拉伸为任意尺寸的窗口，支持最大化、分屏。在设计过程中，除了默认尺寸，还应结合响应式规则，兼顾最大化、分屏、最小尺寸时的窗口显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/rfmHGhz8R9SbuZWaUUlpCg/zh-cn_image_0000002355806697.png?HW-CC-KV=V1&HW-CC-Date=20260404T082435Z&HW-CC-Expire=86400&HW-CC-Sign=51755C6B7910CB9FD40AB11E9E828DA17BDC580A0F31AC130F0EAA6E60493DA1 "点击放大")

默认尺寸：参考值为 1200\*800vp

最小尺寸：360\*240vp，应用可根据情况设定大于此尺寸的最小数值

### 窗口三键

窗口三键按照最大化、最小化、关闭的顺序，从左至右排列。

<table id="ZH-CN_TOPIC_0000002321868010__Xb3d633f39dabb7bc6b4c57540f53fc0340f6d45" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002321868010__row113mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p115mcpsimp"><span><img originheight="800" originwidth="800" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/lF3-IVI5RB-p8pto2SDFPQ/zh-cn_image_0000002355646853.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C32D3AA977CD9AD41D691A5070F5BF53203639D8442A6ABEB705A5BB3950C3F" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p117mcpsimp"><span><img originheight="800" originwidth="800" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/GyJ52WCoTV20JGQ3hoxZuw/zh-cn_image_0000002321888002.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02D36EDF6757B96AF5D79303107604DD86C9C78F815934777C6725FA22B72358" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p119mcpsimp"><span><img originheight="800" originwidth="800" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/JrEB7bh6RgGMyTLPi6coag/zh-cn_image_0000002321728162.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B602D127B953C0C958A50078D491144AB8CDD5C2D56FDD0B38596E1FD10734AD" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321868010__row120mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002321868010__p122mcpsimp">默认状态</p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002321868010__p126mcpsimp">Hover</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002321868010__p129mcpsimp">Click</p></td></tr><tr id="ZH-CN_TOPIC_0000002321868010__row0656112795015"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p10654162765015"><span><img originheight="800" originwidth="800" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/OSR5qmnSR1C5UCTQrUzq-w/zh-cn_image_0000002355807493.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4EB14A556B439A3F71C0FB5EB93BBE09C9E99EB697F0293175AD909026B324A" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p126541927175013"><span><img originheight="800" originwidth="800" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/XpPmvnyYSQemxuESrA86vw/zh-cn_image_0000002355647653.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73481E79DD220E1A303A4F91E291220FEE76A5F25568E5504D25845601653D7D" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p11654152718505"><span><img originheight="800" originwidth="800" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/um_4HvVPQkGhUv4pNFePgQ/zh-cn_image_0000002321888818.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C4E198F67EA8D254C723B0AFE8ABA30A43EE336B347E3A4370325E918CEC4A6" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321868010__row10656152765011"><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002321868010__p96541727175017">默认状态</p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002321868010__p1265472716501">Hover</p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002321868010__p196541527145014">Click</p></td></tr></tbody></table>

### 深浅模式

应用需随系统深浅模式，适配对应效果。

<table id="ZH-CN_TOPIC_0000002321868010__X4261421e94dccbd1cbcfb1088b272cd560c5b59" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002321868010__row159mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p161mcpsimp"><span><img originheight="1600" originwidth="2400" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/fx4dkcp0Q1ORYxrLZY71FQ/zh-cn_image_0000002321729182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7571FD052FF6DA96DB71E252453CC41754FBACBAF9CD3A3E4970DB664FBEE0E9" title="点击放大" width="268.5" height="179"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002321868010__p163mcpsimp"><span><img originheight="1600" originwidth="2400" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/w12fo622T8GqIdwSBiHlkw/zh-cn_image_0000002355807725.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082435Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C381D8B9D794FC0D4ADA833CDDC7BDF566C9B92659935F91D00057AD7D1FAE3F" title="点击放大" width="268.5" height="179"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002321868010__row164mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321868010__p166mcpsimp">浅色模式</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002321868010__p168mcpsimp">深色模式</p></td></tr></tbody></table>
