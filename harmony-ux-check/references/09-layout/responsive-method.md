# 响应式布局方法

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/design-responsive-layout-method-0000001795698449
- 抓取时间：2026-04-04T08:22:30.600Z
当窗口容器大小发生变化时，界面元素需要自动变化以适应容器大小的变化。

根据使用场景，提供了以下 8 种不同的布局方法，在面向多端应用设计过程中不同的方法可以叠加使用。

## 自适应拉伸

某单个内容或某组内容的显示宽度不是固定值，而是通过相对参照物的方式来确定其显示宽度。当参照物的宽度发生变化时，内容或内容间距的宽度随之发生自适应拉伸。

**左右拉伸**

<table id="ZH-CN_TOPIC_0000001795698449__X00c34c2c695afb844a9200fe3dd0eb891f50a38" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row113mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795698449__p115mcpsimp">容器组件尺寸发生变化时，增加或减小的空间全部分配给容器组件内指定区域。</p><p id="ZH-CN_TOPIC_0000001795698449__p116mcpsimp">例如，列表开关组合中，在窗口宽度变化时，开关控件固定宽度并相对列表的右边缘位置固定，整个组合与文本宽度均自适应变化。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001795698449__p119mcpsimp"><span><img originheight="455" originwidth="1200" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104006.55695246776357569832480940279633:50001231000000:2800:C16803B6110DADA726602D3088B3F6954AC814D2AA1CAC40E5DDACBADE196226.gif" title="点击放大" width="268.5" height="101.80625"></span></p></td></tr></tbody></table>

**均分拉伸**

<table id="ZH-CN_TOPIC_0000001795698449__X671444cf28d2a97c4d00bd58d1fe0740b871bb7" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row126mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795698449__p128mcpsimp">容器组件尺寸发生变化时，增加或减小的空间均匀分配给容器组件内所有空白区域。</p><p id="ZH-CN_TOPIC_0000001795698449__p129mcpsimp">自适应拉伸适用于文字、普通按钮、间距等展示宽度灵活，对宽高比不敏感的内容和内容组合。</p><p id="ZH-CN_TOPIC_0000001795698449__p130mcpsimp">例如，在图标型网格中，当窗口宽度变化时，入口图标间距与图标离左右边缘间距同时均等变化。</p><p id="ZH-CN_TOPIC_0000001795698449__p131mcpsimp">当可能出现的拉伸宽度不足以显示默认内容时，应根据场景选择优先保证内容完整或者优先保证其他内容的屏效，并进行截断或换行等组合适配。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001795698449__p134mcpsimp"><span><img originheight="1077" originwidth="1701" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104006.30030482289348364474009339472308:50001231000000:2800:2E31C1B33E3E07423D6CE992826A80B0C10F12003EB963BA8B34F8D797F48B62.gif" title="点击放大" width="268.5" height="170.0026455026455"></span></p></td></tr></tbody></table>

## 自适应缩放

组件的显示大小是固定比例，通过相对参照物的方式来确定其宽或高。当参照物的大小发生变化时，元素的大小随之发生自适应缩放。

**等比缩放**

<table id="ZH-CN_TOPIC_0000001795698449__X431666b9474e29c39702918c655d04d09ca8780" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row143mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795698449__p145mcpsimp">子组件的宽或高按照预设的比例，随容器组件发生变化。</p><p id="ZH-CN_TOPIC_0000001795698449__p146mcpsimp">例如，在宽度或高度变化时，时钟始终保证表盘完整展示并根据较短边决定宽高。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001795698449__p149mcpsimp"><span><img originheight="262" originwidth="501" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104007.56243572143738935185794610073244:50001231000000:2800:5118075EA1F4927607204FA8829E6F54832427E7B5F3CF76935A8C0C6F4FFA57.gif" title="点击放大" width="268.5" height="140.4131736526946"></span></p></td></tr></tbody></table>

**占比缩放**

<table id="ZH-CN_TOPIC_0000001795698449__X3413b5ad24816917a2cc294b04de27020b43639" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row156mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="51.019999999999996%"><p id="ZH-CN_TOPIC_0000001795698449__p158mcpsimp">子组件的宽高按照预设的比例，随容器组件发生变化，且变化过程中子组件的宽高比不变。</p><p id="ZH-CN_TOPIC_0000001795698449__p159mcpsimp">自适应缩放适用于图片、圆形按钮、banner、反应真实物体形状的图像等必须保证宽高比的内容。</p><p id="ZH-CN_TOPIC_0000001795698449__p160mcpsimp">例如，带主体和背景的插画，画面内容根据宽度变化裁切，根据高度变化按 50% 比例缩放。</p><p id="ZH-CN_TOPIC_0000001795698449__p161mcpsimp">不推荐将所有元素同时缩放、或某内容放大过大超过屏幕 50%。这将导致获取信息量不增反减，不符合用户预期。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="48.980000000000004%"><p class="msonormal" id="ZH-CN_TOPIC_0000001795698449__p164mcpsimp"><span><img originheight="1077" originwidth="1710" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104007.51940617033297537820196763443493:50001231000000:2800:51D745FD60BFE2887C392751458BE841EE9C7F3B2245BA8B9930EA202E49216A.gif" title="点击放大" width="262.00260000000003" height="165.01567263157898"></span></p></td></tr></tbody></table>

## 自适应延伸

组件的显示数量不是固定的，而是通过相对参照物的方式来确定其显示数量。当参照物的宽度发生变化时，组件随之发生自适应延伸显示更多数量。

**自适应延伸**

<table id="ZH-CN_TOPIC_0000001795698449__Xeeee9920e420fa46b2fb14a566aad2d30365811" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row173mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795698449__p175mcpsimp">容器组件内的子组件，按照其在容器中的先后顺序，随容器组件尺寸变化显示或隐藏。</p><p id="ZH-CN_TOPIC_0000001795698449__p176mcpsimp">例如，子页签和可滑动宫格在默认宽度下通过露出最后内容，提示右方有更多入口，在宽度变化时，可在每个元素宽度不变、保持滑动交互时显示更多数量。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001795698449__p179mcpsimp"><span><img originheight="1077" originwidth="2097" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104007.62855977818674154171638216653664:50001231000000:2800:9799AD11F878EC01DF0B483DC8DC54D34F080BF08A69119B2F0E4440A93F882E.gif" title="点击放大" width="268.5" height="137.89914163090128"></span></p></td></tr></tbody></table>

**自适应隐藏**

<table id="ZH-CN_TOPIC_0000001795698449__X5c550dbb0b883fba0efa70bdf82c340731b3f4c" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row186mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795698449__p188mcpsimp">容器组件内的子组件，按照其预设的显示优先级，随容器组件尺寸变化显示或隐藏。相同显示优先级的子组件同时显示或隐藏。</p><p id="ZH-CN_TOPIC_0000001795698449__p189mcpsimp">自适应延伸/隐藏适用于页签、操作块、推荐栏目等具有相同交互层级且有更多数据可以填充的内容。</p><p id="ZH-CN_TOPIC_0000001795698449__p190mcpsimp">例如，默认处于同一排的不同音乐播放按钮优先级不同，在宽度变化时可延伸或隐藏低优先级的按钮，最大化适应不同窗口尺寸。</p><p id="ZH-CN_TOPIC_0000001795698449__p191mcpsimp">需要判断因隐藏而不展示的内容对功能完整性是否有影响，并考虑通过滑动或“更多”按钮提供查看使用该内容的方式。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001795698449__p194mcpsimp"><span><img originheight="1077" originwidth="1998" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104007.32733331650800577417598945641149:50001231000000:2800:7699AC1BC3D3C05F22DD1527C09B2BDAEB44A12565C31B87881EF3FDD76AD209.gif" title="点击放大" width="268.5" height="144.731981981982"></span></p></td></tr></tbody></table>

## 自适应折行

<table id="ZH-CN_TOPIC_0000001795698449__Xc3168aec9cf73d072d4f04e8e8f478e8d3bfdac" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row201mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795698449__p203mcpsimp">容器组件尺寸发生变化，当布局方向尺寸不足以显示完整内容时自动换行。</p><p id="ZH-CN_TOPIC_0000001795698449__p204mcpsimp">自适应折行适用于操作块、内容流等具有相同交互层级，且希望保证类型和数量完整性的内容。</p><p id="ZH-CN_TOPIC_0000001795698449__p205mcpsimp">例如，在宽度足够时，操作块位于同一行，在宽度变小时，可根据内容能显示的宽度纵向排布。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001795698449__p208mcpsimp"><span><img originheight="1077" originwidth="2097" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104007.01431930086046362606423279494717:50001231000000:2800:9FEBC6FA09F91D4BCD0DDDCDF1DA3B330BB208E8A90209FB53D61168A87DBE95.gif" title="点击放大" width="268.5" height="137.89914163090128"></span></p></td></tr></tbody></table>

## 缩进布局

为了在宽屏上内容显示有更好的效果，在不同宽度的设备上进行不同缩进效果。

缩进布局适用于纯段落文本/上图下段落文本/卡片的布局结构的场景，在其对应的栅格规格下，缩进的规则占用栅格数量进行布局。

<table id="ZH-CN_TOPIC_0000001795698449__table771613231293" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795698449__row107171223096"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001795698449__p471714239917"><span><img originheight="4396" originwidth="10560" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104007.71782998979394926376363718319276:50001231000000:2800:5B9E336ECF576128CBA9FCF4512802B9E398D448D0864E7F21D3D126BAC5AAA5.png" title="点击放大" width="587" height="244.36098484848486"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001795698449__row137177231198"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001795698449__p939545572">当栅格为 8 column 或 12 column 时可以使用 6 column 和 8 column 的缩进布局。</p></td></tr></tbody></table>

## 挪移布局

利用屏幕的宽度优势，将原先的上下布局切换成左右布局。

挪移布局适用于横竖屏切换，以及类似的宽高比明显变化 (大于 200%) 同时希望保证内容完整的场景。

例如上下布局的插画和文字，横屏后左右布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104007.20093972806210132861640183459739:50001231000000:2800:C90D3660833A5795C2E5767B0142EE152F59613DBDECC4A5E8558F3BDC9AA97E.png "点击放大")

## 重复布局

利用屏幕的宽度优势，将相同属性的组件横向并列排布。

重复布局适用于对宽高比敏感的图片和及组合内容，当内容放大以后导致原图放大超过 150% 的场景。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104008.61983768578555522136612007742204:50001231000000:2800:CB2EC15CCB450C3354F7586276E7729EF214AEB360FF0B07420C854422A679BA.png "点击放大")

## 分栏布局

利用屏幕的宽度优势，将有上下级层级的界面同时左右显示。

当同时满足水平 vp 大于等于 600，可以响应分栏布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251121104008.48755554162608382590454406714061:50001231000000:2800:E039850BC1DB7B8EBFB0F03EC058CD5E9465F4D6BB68BA1A6D5D96DBFE681842.png "点击放大")

## 开发文档

[响应式布局能力](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout)
