# 应用设计

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/app-design-0000002353509845
- 抓取时间：2026-04-04T08:24:40.932Z
应用窗口的内容区作为展示信息的空间，需要根据业务类型合理选择布局、控件元素和响应式布局。

## 应用布局

目前电脑端上常见的应用布局，可以分为以下三种。

<table id="ZH-CN_TOPIC_0000002353509845__Xd4d75dd0789fb448a42685b7d00b54f669eb050" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002353509845__row108mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p110mcpsimp"><span><img originheight="2304" originwidth="3456" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110428.80196564736451634734092656682047:50001231000000:2800:2A618069DD10E1C6C7283E022E21BE0989FD0DCD0A66737D31A2385E346C426A.png" title="点击放大" width="162.33333333333331" height="108.2222222222222"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p112mcpsimp"><span><img originheight="2304" originwidth="3456" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110428.86211930122521164743238578441405:50001231000000:2800:6CD310AA6A2C3C70F633A507C7F16E34E47DF1A89473B6E19F01858CD26B6341.png" title="点击放大" width="162.33333333333331" height="108.2222222222222"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p114mcpsimp"><span><img originheight="2304" originwidth="3456" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110428.31870208964303500725606100890017:50001231000000:2800:7CC678F7A020C0D63AF22A600BA1038F3220BD5432AEFC14322AE969BA7EEFA7.png" title="点击放大" width="162.33333333333331" height="108.2222222222222"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row115mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p117mcpsimp">通栏</p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p119mcpsimp">双分栏</p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p121mcpsimp">三分栏</p></td></tr></tbody></table>

### 通栏布局

通栏布局适用于层级关系简单，注重内容呈现效率的应用。应用可在窗口顶部区域添加菜单栏、工具栏，收纳复杂操作，使用户将注意力集中在更大的主要任务区上。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110428.99444222399670491086685925859274:50001231000000:2800:1EC2940952466E477C361E3C0C100BA0F382B9414056A0E1682B5BE7AB61169B.png "点击放大")

### 双分栏布局

适用于具备父子层级结构，以左侧列表 + 右侧内容的形式高效呈现信息。

<table id="ZH-CN_TOPIC_0000002353509845__Xf38470b82d28859a95d7b6d8bda2eac8718071d" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002353509845__row241mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p243mcpsimp"><span><img originheight="1708" originwidth="2444" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110428.17920008481428817087594106958517:50001231000000:2800:91153A2006A9EC41E00CDA4286A8A5BBF59FB0DDC6B030B0B46A65355C856214.png" title="点击放大" width="268.5" height="187.64238952536826"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p245mcpsimp"><span><img originheight="1708" originwidth="2444" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110429.45688326983303826804739267556684:50001231000000:2800:DABD04291A4B420A705E85CAD133B12C28B2E865A8B87221FB76915A53FCEEE6.png" title="点击放大" width="268.5" height="187.64238952536826"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row246mcpsimp"><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002353509845__p248mcpsimp">内容区为一级界面时，标题栏与通栏平级呈现</p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002353509845__p250mcpsimp">内容区为非一级界面时，返回按钮与标题栏结合呈现</p></td></tr></tbody></table>

双分栏结构也适用于大多数移动端适配到大屏设备上的应用，适配时通常将底部 tab 适配为侧边导航，右侧内容区占比较大，所承载的内容及控件元素更为丰富、自由。

<table id="ZH-CN_TOPIC_0000002353509845__Xaf00661c5983d721f66ecf64ec51226b97b85d2" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002353509845__row257mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p259mcpsimp"><span><img originheight="1708" originwidth="2444" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110429.09188989728868356819598059091806:50001231000000:2800:B5CD907E62BF72F83D8A3284F8E902BF50C85AA434DFC22B33A5D5EC1490FC47.png" title="点击放大" width="162.33333333333331" height="113.44735406437533"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p261mcpsimp"><span><img originheight="1708" originwidth="2444" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110429.33370058388668121965027077513935:50001231000000:2800:E3EEF2E11E77D4DB2D385FE483545645B3FC63A2E8129CB7E5B34688F442094F.png" title="点击放大" width="162.33333333333331" height="113.44735406437533"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p263mcpsimp"><span><img originheight="1708" originwidth="2444" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110429.21721705330543613473836687376232:50001231000000:2800:39E481CCC3EDEDA5DDDD12EA8AB8F73E983F7BCF815398811DE26D4A5190FAF1.png" title="点击放大" width="162.33333333333331" height="113.44735406437533"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row264mcpsimp"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p266mcpsimp">示例: 左侧抽屉按钮 + 右侧工具栏</p></td><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p268mcpsimp">示例: 右侧工具栏 + 搜索框的复杂构成</p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p270mcpsimp">示例: 内容区内居中呈现的分段按钮</p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__X2f4e432ac97cbb45f1184ba70bfd47578f2c911"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p272mcpsimp"><span><img originheight="1704" originwidth="2556" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110429.05099641394609987389132627259952:50001231000000:2800:337C1042658E67BC0FA70C15CC03AB2565B6C673764BD3CDF1E32A7000507768.png" title="点击放大" width="162.33333333333331" height="108.22222222222221"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p274mcpsimp"><span><img originheight="3102" originwidth="4500" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110429.14840221242667947677764942073479:50001231000000:2800:D40F6096FB6ACE1F34C03A7B11E827B67E6211936089BBF38105670682981003.png" title="点击放大" width="162.33333333333331" height="111.90177777777777"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p276mcpsimp"><span><img originheight="1808" originwidth="2558" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110430.34727764489716008741733419011992:50001231000000:2800:AA4737647BE63C94C033CCE8531B0B2000C6F994D0F6C5235A5448E6A674C349.png" title="点击放大" width="162.33333333333331" height="114.73755538180868"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row277mcpsimp"><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p279mcpsimp">天气</p></td><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p281mcpsimp">应用市场</p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000002353509845__p283mcpsimp">日历</p></td></tr></tbody></table>

当应用适配电脑端窗口时，建议优先选择侧边导航栏。导航栏可以承载更多的信息，提升信息呈现效率，更符合效率型设备的使用场景。

### 三分栏布局

适用于具备递进式导航的、层级结构较复杂的应用，常见于办公类应用及 IM 社交类应用。

**构成**

<table id="ZH-CN_TOPIC_0000002353509845__Xe5bcc8e1815c6802c8c08f1d2c6596061534fca" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002353509845__row153mcpsimp"><td class="cellrowborder" valign="top" width="7.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p155mcpsimp">序号</p></td><td class="cellrowborder" valign="top" width="13.000000000000004%"><p id="ZH-CN_TOPIC_0000002353509845__p157mcpsimp">元素名称</p></td><td class="cellrowborder" valign="top" width="69%"><p id="ZH-CN_TOPIC_0000002353509845__p159mcpsimp">描述</p></td><td class="cellrowborder" valign="top" width="11.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p161mcpsimp">显示区域</p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row162mcpsimp"><td class="cellrowborder" valign="top" width="7.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p164mcpsimp"><strong>1</strong></p></td><td class="cellrowborder" valign="top" width="13.000000000000004%"><p id="ZH-CN_TOPIC_0000002353509845__p167mcpsimp">抽屉按钮</p></td><td class="cellrowborder" valign="top" width="69%"><ul id="ZH-CN_TOPIC_0000002353509845__ul169mcpsimp"><li id="ZH-CN_TOPIC_0000002353509845__li170mcpsimp">用于收起侧边导航栏，业务根据需要选配</li></ul></td><td class="cellrowborder" valign="top" width="11.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p172mcpsimp">B 栏列表区</p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row173mcpsimp"><td class="cellrowborder" valign="top" width="7.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p175mcpsimp"><strong>2</strong></p></td><td class="cellrowborder" valign="top" width="13.000000000000004%"><p id="ZH-CN_TOPIC_0000002353509845__p178mcpsimp">标题栏按钮</p></td><td class="cellrowborder" valign="top" width="69%"><ul id="ZH-CN_TOPIC_0000002353509845__ul180mcpsimp"><li id="ZH-CN_TOPIC_0000002353509845__li181mcpsimp">内容区默认不呈现左侧标题栏，仅呈现右侧图标按钮；</li><li id="ZH-CN_TOPIC_0000002353509845__li182mcpsimp">最多支持 3 个图标按钮，超出数量的图标收入最后 1 个[更多]图标里</li></ul></td><td class="cellrowborder" valign="top" width="11.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p184mcpsimp">B 栏列表区</p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row185mcpsimp"><td class="cellrowborder" valign="top" width="7.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p187mcpsimp"><strong>3</strong></p></td><td class="cellrowborder" valign="top" width="13.000000000000004%"><p id="ZH-CN_TOPIC_0000002353509845__p190mcpsimp">放大按钮</p></td><td class="cellrowborder" valign="top" width="69%"><ul id="ZH-CN_TOPIC_0000002353509845__ul192mcpsimp"><li id="ZH-CN_TOPIC_0000002353509845__li193mcpsimp">当非一级界面支持扩大至窗口整屏时，可配置此按钮</li></ul></td><td class="cellrowborder" valign="top" width="11.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p195mcpsimp">C 栏内容区</p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row196mcpsimp"><td class="cellrowborder" valign="top" width="7.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p198mcpsimp"><strong>4</strong></p></td><td class="cellrowborder" valign="top" width="13.000000000000004%"><p id="ZH-CN_TOPIC_0000002353509845__p201mcpsimp">工具栏</p></td><td class="cellrowborder" valign="top" width="69%"><ul id="ZH-CN_TOPIC_0000002353509845__ul203mcpsimp"><li id="ZH-CN_TOPIC_0000002353509845__li204mcpsimp">最多支持 6 个图标按钮，超出数量的图标收入最后 1 个[更多]图标里</li></ul></td><td class="cellrowborder" valign="top" width="11.000000000000002%"><p id="ZH-CN_TOPIC_0000002353509845__p206mcpsimp">C 栏内容区</p></td></tr></tbody></table>

-   常规三分栏窗口，包含 A 栏侧边导航栏，B 栏列表区及 C 栏内容区。
-   窗口中的其他控件元素，从通栏下方开始，贴边往下排布。例如：

-   B 栏的搜索入口，C 栏的标题栏等。

<table id="ZH-CN_TOPIC_0000002353509845__Xb9a931a7f843625f90de5ccb073c2937f4fe961" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002353509845__row216mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p218mcpsimp"><span><img originheight="1708" originwidth="2444" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110430.24140887833044235965362578894440:50001231000000:2800:93EFF6DC5D68616EBA863A2E46E5E6E2B1F59D3026813384292086503EC41C63.png" title="点击放大" width="268.5" height="187.64238952536826"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p220mcpsimp"><span><img originheight="1708" originwidth="2444" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110430.24632830882417922260632035185327:50001231000000:2800:289BDA7536EF448E70414F80777CA4F170816C11834CF2CE9418D61A4C5BA288.png" title="点击放大" width="268.5" height="187.64238952536826"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row221mcpsimp"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002353509845__p223mcpsimp">窗口通栏元素说明</p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002353509845__p225mcpsimp">其他窗口控件元素示例</p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__X560139d22d0072dfb5e7576cdf9c03fe2b39172"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p227mcpsimp"><span><img originheight="1794" originwidth="2556" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110430.78683068854537697989912453984536:50001231000000:2800:902B9B0F7A7FB3DD868AFD6290D18082AFA1CD59B0176CC1A4ED813CC4DF06D9.png" title="点击放大" width="268.5" height="188.45422535211267"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002353509845__p229mcpsimp"><span><img originheight="1564" originwidth="2424" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110430.33237191311301082368172316963333:50001231000000:2800:BF3646BCA9D4B3ED08F0E7DB0EE99B5E890D41F2A9A2E758B76CD45A582AC6C2.png" title="点击放大" width="268.5" height="173.240099009901"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002353509845__row230mcpsimp"><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002353509845__p232mcpsimp">邮件</p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002353509845__p234mcpsimp">备忘录</p></td></tr></tbody></table>

### 布局转换

-   应用使用侧边导航栏时，可提供抽屉按钮，方便用户进行收起和展开，提供用户更灵活的任务操作区域。
-   为了清晰指引窗口收起后的界面层级，可在收起的 B 栏呈现标题栏，其内容与 A 栏中所属列表的名称保持一致。
-   应用也可直接拖拽分栏边缘，对布局进行切换，请参阅“[断点系统](https://developer.huawei.com/consumer/cn/doc/design-guides/design-layout-basics-0000001795579413#section525952492)”。

Video Player is loading.

Current Time 0:00

Loaded: 0%

0:00

Duration \-:-

1x

-   2x
-   1.8x
-   1.5x
-   1.2x
-   1x, selected

This is a modal window.

The media could not be loaded, either because the server or network failed or because the format is not supported.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-Transparent

Text BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparent

Caption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%

Text Edge StyleNoneRaisedDepressedUniformDrop shadow

Font FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

End of dialog window.

257

## 使用多态控件

电脑控件与手机控件为同一个控件，是对手机控件的继承和新增，针对键鼠与触控场景进行补充与改造，以满足多设备需求。例如，在电脑上，可考虑利用光标悬停态增加控件说明。具体控件使用，请参阅“[控件](https://developer.huawei.com/consumer/cn/doc/design-guides/general_overview-0000001929599380)”章节里对电脑控件的差异化介绍。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110431.41257752544890841645619588038677:50001231000000:2800:6B44A598B21BBE92F374E1ED96A5226A7C69371F1BBD07A940CCBEBB71D20CB8.png "点击放大")

## 多窗口协同

电脑拥有更大的显示空间，更精准的交互操作。在设计过程中，可充分利用多窗口能力，增强应用并行任务能力。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110431.90223584996142981180319205062671:50001231000000:2800:A1BF4388BD00C97CF9377A0C75841748E3098D123498105E5DEC14756F60E610.png "点击放大")
