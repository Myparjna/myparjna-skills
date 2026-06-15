# 滚动条

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/scrollbar-0000001956815473
- 抓取时间：2026-04-04T08:23:00.965Z
滚动条控件用于显示当前界面视图所在位置，并提供滚动视图时动态展示位置变化进度的功能。滚动条通常出现在内容区域大于实际可视区域时，允许用户垂直或水平滚动查看其余内容的场景。开发能力相关请参考 [ScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213431.64001175794468022567377317610959:50001231000000:2800:D182D34BE7778060E9D2CEB20FDB4CCC267D373CC6900E91638C8E05CE9107F2.jpg "点击放大")

## 如何使用

**滚动条的显示需要给予用户明确预期。**当用户初次进入界面/弹框/可滚动界面，若界面内容超出显示区域，显示滚动条，无任何操作，2 秒后消失。滚动条高度为动态高度：滚动条高度反映当前可视内容占整个内容的高度比例，高度是动态变化的，内容高度越高，滚动条高度越小。

**当页面内容超出内容显示区域长度时，会显示竖向/横向的滚动条。**若用户需快速定位内容，可拖拽滚动条；在电脑设备上可点击滚动条空白区域进行快速跳转。

**在电脑设备上存在两种滚动条的展示规则。**在默认规格中，初次进入界面时出现滚动条，无操作 2 秒后滚动条消失。滚动鼠标滚轮或双指滑动触控板时，滚动条出现，无操作 2 秒后滚动条消失。另外一种则是常驻于界面中，始终保持显示。

**根据应用使用场景，使用合适的滚动条样式。**可以通过 [ScrollBarOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar#scrollbaroptions对象说明) 中的 direction 属性配置滚动条组件的滚动方向，可以配合横向界面较多的业务场景来使用。

## 布局规则

**手机**

<table id="ZH-CN_TOPIC_0000001956815473__Xca79a38f6d89f71f169e8775d8df207a4f692e6" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956815473__row118mcpsimp"><td class="cellrowborder" valign="top" width="34%"><p id="ZH-CN_TOPIC_0000001956815473__操作操作对象">操作/操作对象</p></td><td class="cellrowborder" valign="top" width="66%"><p id="ZH-CN_TOPIC_0000001956815473__滚动条">滚动条</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row121mcpsimp"><td class="cellrowborder" valign="top" width="34%"><p id="ZH-CN_TOPIC_0000001956815473__p123mcpsimp">点击</p></td><td class="cellrowborder" valign="top" width="66%"><p id="ZH-CN_TOPIC_0000001956815473__p125mcpsimp">显示 Press 效果</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row126mcpsimp"><td class="cellrowborder" valign="top" width="34%"><p id="ZH-CN_TOPIC_0000001956815473__p128mcpsimp">悬浮</p></td><td class="cellrowborder" valign="top" width="66%"><p id="ZH-CN_TOPIC_0000001956815473__p130mcpsimp">显示 Hover 效果</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row131mcpsimp"><td class="cellrowborder" valign="top" width="34%"><p id="ZH-CN_TOPIC_0000001956815473__p133mcpsimp">滑动</p></td><td class="cellrowborder" valign="top" width="66%"><p id="ZH-CN_TOPIC_0000001956815473__p135mcpsimp">内容区滑动</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row136mcpsimp"><td class="cellrowborder" valign="top" width="34%"><p id="ZH-CN_TOPIC_0000001956815473__p138mcpsimp">拖拽</p></td><td class="cellrowborder" valign="top" width="66%"><p id="ZH-CN_TOPIC_0000001956815473__p140mcpsimp">上下/左右拖拽滚动条，内容区滑动</p></td></tr></tbody></table>

**滚动条热区大小规则**

在触屏交互场景，滚动条的点击热区扩大至 32vp，以便提升交互的准确性。

<table id="ZH-CN_TOPIC_0000001956815473__table962711495411" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956815473__row19627134917420"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p66288491741"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213431.27016664546233821120569905296870:50001231000000:2800:F2BD5D91502A12566A4284BA385481969E8EEF89623CBC1ED55D3C40B1316843.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p062814497412"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213431.48854054869021872482642150040545:50001231000000:2800:7E14AB76E6634A458A8C8EBC87473E0CD17D99B4D98029A3BBFC26CD4D6D0DEA.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row1628164919416"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p29791558"><strong>未激活</strong></p><p id="ZH-CN_TOPIC_0000001956815473__p4970112510">高度随内容自动计算，最小高度 48vp</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p091213619510"><strong>激活</strong></p><p id="ZH-CN_TOPIC_0000001956815473__p19121169516">热区：32vp 宽，高度自动变化滚动条</p></td></tr></tbody></table>

当滚动条使用在较宽界面场景时，避免滚动条的展示位置在界面中过于孤立，通常布局在屏幕边缘的右侧。同理，如果在分栏或者分屏场景内，也采用同样的展示规则。

<table id="ZH-CN_TOPIC_0000001956815473__table839215224516" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956815473__row163922223517"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p1350401873212"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213431.04837173657777973351449193369062:50001231000000:2800:EA7655775F3FA12B003ADF40CC9D028F2E6E43C1C9F56B90EC56575552235DC2.png" title="点击放大" width="268.5" height="151.03125"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p144324289320"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213432.70987850457163817005815816454224:50001231000000:2800:8E3811C3E7F090A3A25EF3B0A2894377E3D9E7AB062E7123B7A5A7800CC572C0.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row193924222518"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p1939210229516">滚动条上端与内容上边缘对齐 ，滚动范围在内容边缘内。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815473__p146766401753">滚动条宽度：4vp，距离屏幕/窗口边缘 4vp。</p></td></tr></tbody></table>

**电脑设备**

**键鼠操作**

<table id="ZH-CN_TOPIC_0000001956815473__Xaf7abe626aa4994596b447915bb378a06bb4838" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956815473__row177mcpsimp"><td class="cellrowborder" valign="top" width="19%"><p id="ZH-CN_TOPIC_0000001956815473__交互输入">交互输入</p></td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__操作">操作</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__反馈">反馈</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row181mcpsimp"><td class="cellrowborder" valign="top" width="19%"><p id="ZH-CN_TOPIC_0000001956815473__p183mcpsimp">键盘</p></td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p185mcpsimp">方向键上</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p187mcpsimp">页面向上滑动</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row188mcpsimp"><td class="cellrowborder" valign="top" width="19%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p191mcpsimp">方向键下</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p193mcpsimp">页面向下滑动</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row194mcpsimp"><td class="cellrowborder" valign="top" width="19%"><p id="ZH-CN_TOPIC_0000001956815473__p196mcpsimp">鼠标</p></td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p198mcpsimp">左键悬浮</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p200mcpsimp">显示 Hover 效果</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row201mcpsimp"><td class="cellrowborder" valign="top" width="19%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p204mcpsimp">左键拖拽</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p206mcpsimp">控制页面滑动方向</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row207mcpsimp"><td class="cellrowborder" valign="top" width="19%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p210mcpsimp">左键点击滚动条空白区</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p212mcpsimp">控制页面</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row213mcpsimp"><td class="cellrowborder" valign="top" width="19%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p216mcpsimp">左键长按滚动条空白区</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p218mcpsimp">控制页面</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row219mcpsimp"><td class="cellrowborder" valign="top" width="19%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p222mcpsimp">滚轮上滑</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p224mcpsimp">页面向上滑动</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row225mcpsimp"><td class="cellrowborder" valign="top" width="19%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p228mcpsimp">滚轮下滑</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p230mcpsimp">页面向下滑动</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row231mcpsimp"><td class="cellrowborder" valign="top" width="19%"><p id="ZH-CN_TOPIC_0000001956815473__p233mcpsimp">触控板</p></td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p235mcpsimp">双指上滑</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p237mcpsimp">页面向上滑动</p></td></tr><tr id="ZH-CN_TOPIC_0000001956815473__row238mcpsimp"><td class="cellrowborder" valign="top" width="19%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="37%"><p id="ZH-CN_TOPIC_0000001956815473__p241mcpsimp">双指下滑</p></td><td class="cellrowborder" valign="top" width="44%"><p id="ZH-CN_TOPIC_0000001956815473__p243mcpsimp">页面向下滑动</p></td></tr></tbody></table>

**当显示规则为【常驻显示】时，支持光标点击交互：**

-   当光标移入滚动条区域，点击空白区时，触发一次页面滑动，内容区滚动一屏；
-   当光标停留在空白区某一点长按时，每 100ms 激活一次页面滚动，内容区持续滑动至点击位置。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213432.07893796881635653929849985929993:50001231000000:2800:10872EC97EA5B64F32F0D478A80E7FFE951CF34B7DAFA4818F3397E07BE7C8B2.png "点击放大")![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213433.45377464745941306778576576453758:50001231000000:2800:3900ADEB449D8D87AB2B9BAE5B26665A5C71D95B3F905BF10CDA9382656EE338.png "点击放大")

**智能穿戴****滚动条**

一般位于界面右侧，随页面滚动显示当前所处的位置。当前根据智能穿戴各设备硬件差异，滚动条样式也会有所区分

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213435.88201344557669288100788069970437:50001231000000:2800:B2A2AF23B7EBF04D6BAD81C1FC6C1C86B6414CCB7E88CDCA0A18EAB577EB2783.png "点击放大")

**如何使用**

· 初次进入界面/弹框/可滚动界面，若界面内容超出显示区域，显示竖向滚动条，无任何操作，2 秒后消失。

· 滚动条高度为动态高度：滚动条长度反映当前可视内容占整个内容的高度比例，高度是动态变化的，内容高度越长，滚动条高度越短。

**滚动条显示规则**

高度随内容自动计算。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213435.60129290270570761763516613854891:50001231000000:2800:747FC603E1A55EB0983898EDC1C236EBB35568A992B17041821C9544FB038CA5.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213435.17881267336095022963011499589959:50001231000000:2800:67E5FE697BB20C521C343D6C7DA1D4E77B1E796236806F665D7D283402D84954.png "点击放大")

## 开发文档

[ScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar)
