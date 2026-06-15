# 色彩

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/color-0000001776857164
- 抓取时间：2026-04-04T08:22:21.263Z
在 HarmonyOS NEXT的色彩设计中，强调品牌色的特征性展示以及系统色彩的对比关系，通过色彩的层次结构传递视觉的连续性和界面的关联性。HarmonyOS NEXT 的色彩系统的体验目标是为所有人群而设计，体现更加包容性的设计，以不同用户群体的视角思考问题。

HarmonyOS NEXT 的系统色调继承了“鸿蒙宇宙”世界观中回归本源的主旨思想，结合宇宙宏观之势与回归自然本源之力，吸收并呈现纯净与和谐的虚拟世界色彩空间体验。宇宙蓝与雪域灰作为 HarmonyOS NEXT 系统中色彩的构成基础，奠定了整体色系的体验趋势，象征着苍穹与大地，两者相配合，使得整个用户界面更加干净、和谐。

<table id="ZH-CN_TOPIC_0000001776857164__X31cd9040e265ac719ca43fbe825905de58bd377" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row108mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p110mcpsimp"><span><img originheight="1128" originwidth="2002" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102604.34406156523298211697571746259261:50001231000000:2800:93134C94302395F7DDC396A8305E877C87779999CE3B8A7059B5CF2D85EDC0B7.png" title="点击放大" width="268.5" height="151.2827172827173"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p112mcpsimp"><span><img originheight="1126" originwidth="2004" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102605.41984565496338995251754553387633:50001231000000:2800:F7BC47A38F8CC8FAE7E8CBE4A33AA361B4B848B5E4F97604566AD8C8A3F0B5A1.png" title="点击放大" width="268.5" height="150.86377245508982"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row113mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p115mcpsimp"><strong>宇宙蓝</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p117mcpsimp">我们选择更为深邃广阔的宇宙蓝，无边无垠的蓝深邃如宇宙，为系统带来宇宙初开的纯净与宁静。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p119mcpsimp"><strong>雪域灰</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p121mcpsimp">自然里面，没有绝对的黑也没有绝对的白，以带有淡蓝色相的雪域灰作为卡片界面的背景颜色来烘托界面的纯净感。</p></td></tr></tbody></table>

创建属于应用自身的品牌色，可以让用户时刻注意并了解当前所属的应用进程，便于用户理解和发现关键性事件。一套舒适有特征的配色方案，结合层次分明的参数信息和组件结构，可以更加高效的帮助开发者与设计师投入到应用开发与设计中。

## 如何分层构建色彩

色彩分层的核心在于构建不同使用场景下的对比关系，每一个颜色都有属于自己的 ID，用于处理不同层级之间的对比差异和保持同层级色彩一致的关键作用。

**映射正确的色彩关系**

系统组件会默认对应一套分层参数，这些参数在默认情况下满足使用场景。如果应用需要自定义组件规格，则需要重新梳理正确的映射关系到这些组件的背景、文本等色彩。

**保障色彩的可阅读性**

色彩的搭配使用需要满足常规阅读对比度，系统默认颜色保障了最小 3:1 对比度，在深色模式下色彩的映射关系会发生部分变化，这些变化在情理之中。

**最小化的色彩管理**

在 HarmonyOS 的色彩体系中，可以最小化的管理系统色彩数量，基于常规色四件套便可搭建系统整体的色彩风格。

## 如何运作 Token 参数

在系统参数中可以找到名称前缀包括 “primary”、“on\_primary”、“brand”、“container”的颜色，在浅色与深色模式中均使用相同的 Token 名称，但他们可能对应不同的数值。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102605.47142485696284763556240876350036:50001231000000:2800:98BD35F9135D0B0BB3942A8A7B372668E95081BBD6B584A8C252651BCE6B9B00.png "点击放大")

在系统参数设计中，会将参数类型划分为三个层级关系，自上而下为控件私有参数、通用语义参数和通用基础参数。

-   **基础 Token**：基础色彩包含 primary、on\_primary、brand、container、background 等色彩，基础色会通过一定的计算方式延伸成一定数量的对比度色彩，用于展示在用户界面的不同元素中，通过对比度关系构建界面效果。基础色可以被直接引用，或是被引用后重新定义语义，用于界面中同类型和显示层级的元素中。
-   **语义 Token**：语义色彩有用于固定场景 Token 名称，这些名称定义了自身的使用场景且不可随意更改。语义 Token 分为文本类、图标类、组件类和交互事件类。这些类别定义了系统中大部分的使用场景，每个 Token 参数都与基础 Token 具备一定的引用关系，应用自定义的参数也可基于使用场景自定义引用链路。
-   **控件 Token**：用于指定控件内某一元素所对应的参数信息，具有唯一性且不可复用。控件 Token 属于组件内部的元素名称，应用自定义控件可以参考这类 Token 的使用关系。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102605.55128314379940838525798130704961:50001231000000:2800:F171FC7533BD312862F1F0DB65E589D590B20BC6DC87065BF8DEFEDA1488DC0A.png "点击放大")

<table id="ZH-CN_TOPIC_0000001776857164__table16751155618716" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row1075145618720"><td class="nocellnorowborder" rowspan="2" style="border: none;" valign="top" width="50%"><ul id="ZH-CN_TOPIC_0000001776857164__ul1114710158819"><li id="ZH-CN_TOPIC_0000001776857164__li10147215389"><strong>Primary</strong></li></ul><p id="ZH-CN_TOPIC_0000001776857164__p11147215487">用于最上层文本、图标的填充和显示，低对比度可用于其他层级显示，例如二级文本色、三级文本色等。</p><ul id="ZH-CN_TOPIC_0000001776857164__ul1114717156820"><li id="ZH-CN_TOPIC_0000001776857164__li31478151187"><strong>onPrimary</strong></li></ul><p id="ZH-CN_TOPIC_0000001776857164__p61476151182">用于显示在强调色、图片之上显示的文本、图标，不可在常规界面中使用。例如，不可在一级背景色 backgroundColorPrimary 基础上直接使用 onPrimary 颜色。</p><ul id="ZH-CN_TOPIC_0000001776857164__ul101471915782"><li id="ZH-CN_TOPIC_0000001776857164__li1814781519815"><strong>Brand</strong></li></ul><p id="ZH-CN_TOPIC_0000001776857164__p7147215986">系统主题色、高亮色，用于突出核心组件信息。应用可定制主题色，主题色影响系统默认组件，同时可用于应用自定义组件。所有引用 brand 色彩的组件都会受到此影响。</p><ul id="ZH-CN_TOPIC_0000001776857164__ul131478157811"><li id="ZH-CN_TOPIC_0000001776857164__li314701513813"><strong>Container</strong></li></ul><p id="ZH-CN_TOPIC_0000001776857164__p1314771515810">系统组件容器色，用于展示组件背景填充色。例如普通按钮背景色、搜索框组件背景色等。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p975195613718"><span><img originheight="1080" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102605.88629815212926775657086401964316:50001231000000:2800:699E652377A24D636042F70AF98C2DBC5C56B6257444FA41AC2515F749DAC962.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1775125613711"><td class="cell-norowborder" style="border: none;" valign="top"><p id="ZH-CN_TOPIC_0000001776857164__p47513560716"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102605.18872781449202096943744897346556:50001231000000:2800:422AD0B1FA6C12B424E23723E9F89264BEBBE297178E137E6A6F801761600DD6.png" title="点击放大" width="637" height="318.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1175116561173"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1075125619719"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p1532212255813"><strong>定制主题及色彩</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p13221225389">基础色中的 Primary、onPrimary、Brand 以及 Container 均可单独定义色彩，系统默认色彩中 Primary 和 Container 使用同级配色，设计师可以通过配置不同明暗对比的色彩丰富界面视觉效果。</p><p id="ZH-CN_TOPIC_0000001776857164__p532213251083">如何自定义应用品牌色，可以参阅<a href="https://gitee.com/openharmony/docs/blob/master/zh-cn/application-dev/ui/theme_skinning.md#%25E8%25AE%25BE%25E7%25BD%25AE%25E5%25BA%2594%25E7%2594%25A8%25E7%25BA%25A7%25E8%2587%25AA%25E5%25AE%259A%25E4%25B9%2589%25E5%2593%2581%25E7%2589%258C%25E8%2589%25B2" target="_blank">主题换肤</a>中的相关能力。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p175185611715"><span><img originheight="1080" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102605.80203034845751335944957252346924:50001231000000:2800:54DE80FAB781F563023B44D251F2FBE01182284E0E72D867D606B851C98AB948.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row12290291813"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row155442271386"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p954462713810"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102605.23532458074777561601649357698276:50001231000000:2800:2131F55ACD75C8907E6BB7F295A7561446AC262C2CCCDD7705443FF307488467.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p15453276815"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.73878052854849554874143702660748:50001231000000:2800:32BA190375672B968858F7BCFC50A2BF5B2053016014722E0C346F35A8645B81.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row6234238581"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p121078471384"><strong>系统默认主题色</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p1910794716810">系统默认色以宇宙蓝为高亮色，雪域灰为基础背景搭建</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p9107147687"><strong>应用定制主题色</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p121071547281">应用可定制属于自己品牌色色调，并应用于整个界面</p></td></tr></tbody></table>

## 如何使用 Token 参数

**计算与理解基础 Token 参数关系**

基础 Token 中的颜色会基于透明度系数分别映射出 12 个不同的色彩参数，默认规则直接将透明度与色彩参数值叠加使用。设计师与开发者只需指定基础色的原色参数，通过带入不同透明度值实现整体映射。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.70459823365539906863957877143133:50001231000000:2800:C7C55CDE7D132EFEA5249B18164D27E0F0B71F9D303F350A818339F53C670F23.png "点击放大")

开发者也可以将主题色指定为其他的颜色。系统通用的基础色彩数量是不变的，修改映射关系可能带来控件默认引用 Token 链路发生变化，开发者需要同步考虑控件的默认参数引用逻辑和关系。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.26653905780961302718827286831073:50001231000000:2800:CD2A8130D2592D681CD83397ABB38660067E02FD0F109B122B73686ACD629BF6.png "点击放大")

**正确使用 Token 进行界面搭配**

为了保障在应用中所有的图层色彩信息保持一定对比度和色彩关系，请参考左侧进行合理的搭配关系。

不正确地组合颜色可能会破坏组件和界面的对比关系和美观度，特别是在自定义场景下，错误的组合可能会对应用界面带来极大的异常体验。

<table id="ZH-CN_TOPIC_0000001776857164__X3245e057cb8e68bfa97bde053777e524bd1503f" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row216mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p218mcpsimp"><span><img originheight="750" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.47017556279509221637604592992529:50001231000000:2800:8F253F2DCBD6B1F1D44305442425E7E95E6599651DBC3B1647AFC58FC7BFE1CA.png" title="点击放大" width="268.5" height="209.76562499999997"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p220mcpsimp"><span><img originheight="750" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.99912728130970294477309460711535:50001231000000:2800:32B1ECD378E6A7701CF0026B8DB4FCE52F11DEF6670EBB6C405927CDD2A566E3.png" title="点击放大" width="268.5" height="209.76562499999997"></span></p></td></tr></tbody></table>

## 文本色与图标色

<table id="ZH-CN_TOPIC_0000001776857164__X3905a9db2e0b41b8fd706c4d18b50eed09d255b" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row226mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="51%"><p id="ZH-CN_TOPIC_0000001776857164__p228mcpsimp"><strong>色彩分级</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p230mcpsimp">文本与图标在界面使用中要根据信息优先级选择合适的色彩透明度使用，在 HarmonyOS 中我们划分默认四个基础层级和一个高亮色层级进行展示文本和图标。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="49%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p232mcpsimp"><span><img originheight="1000" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.38121927111531453826815805649360:50001231000000:2800:110097DB92D5261DF27572261777C87B90734A8E09A0F7A8BBDCD3E576E3659E.png" title="点击放大" width="262.13" height="136.52604166666666"></span></p></td></tr></tbody></table>

文本与图标基于基础 Token-Primary 引用，常规使用分为四个层级，font\_primary、font\_secondary、font\_tertiary 和 font\_fourth，这四个层级依照由高到低依次透明度变化，用于表达界面中核心内容与辅助内容的区别。除此以外文本与图标还有对应反色场景，在 Token name 的表达上使用 font\_on 和 icon\_on 为开头展示，这些内容通常用于展示高亮色容器之上或图片之上的文本与图标，反色内容无论深浅色模式都是用高亮度色彩。

文本与图标的高亮色场景默认引用系统 Brand 颜色，当主题中的 Brand 颜色发生变化，或应用自定义了主题色后，与之对应关联的高亮文本与图标都会发生对应变化。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.65338587552141555114750506959013:50001231000000:2800:A5D6EECB5A6A618B5C09992E61BCA4A15725DBF993F0F7A80244FAEA5B13D923.png "点击放大")

## **组件容器色**

<table id="ZH-CN_TOPIC_0000001776857164__table791340201013" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row109220409108"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p250mcpsimp"><strong>区分组件背景层级</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p252mcpsimp">用于区分组件背景色的层级关系，在系统组件中存在诸多通用背景色，例如普通按钮、搜索框、文本框等组件。同时，部分组件的背景有特殊含义，例如强调按钮使用系统品牌色，子页签有中性高亮色等。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p149264019109"><span><img originheight="1000" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.44940749698767501945608711113760:50001231000000:2800:5095501F22AB98B3348766A0910D8B1B76290095B07B6AAF2A1D7C146D841325.png" title="点击放大" width="268.5" height="139.84375"></span></p></td></tr></tbody></table>

控件容器色以 comp 开头的控件专用色主要用于各类控件容器背景色，容器背景基于组件的布局层级分为容器类和展示类，容器类组件的色彩通常跟随系统深浅模式变化，例如：列表背景色、弹出框背景色、半模态背景色；展示类一般为基础功能组件，主要是用品牌色或低透明度背景色，例如：按钮背景色、搜索框背景色、索引条选中色等等。

<table id="ZH-CN_TOPIC_0000001776857164__X9c4bfb9654a6d542fb274d88119584369599ba0" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row259mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p261mcpsimp"><strong>控件高亮背景色</strong></p><ol id="ZH-CN_TOPIC_0000001776857164__ol12470235155615"><li id="ZH-CN_TOPIC_0000001776857164__li447073565610">comp_background_emphasize，控件高亮背景色</li><li id="ZH-CN_TOPIC_0000001776857164__li2470235185610">comp_emphasize_secondary，控件高亮二级背景色</li><li id="ZH-CN_TOPIC_0000001776857164__li1147043555614">comp_emphasize_tertiary，控件高亮三级背景色</li></ol></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p267mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.91805349429411532144492580442130:50001231000000:2800:BC72D4892FF65317B6A7F27AB1130CF40472394CDAE95E091843D371CB33E21E.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row268mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row271mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p273mcpsimp"><strong>控件基础背景色</strong></p><ol id="ZH-CN_TOPIC_0000001776857164__ol049914412568"><li id="ZH-CN_TOPIC_0000001776857164__li8499104117569">comp_background_primary，控件一级背景色</li><li id="ZH-CN_TOPIC_0000001776857164__li12499541115613">comp_background_primary_contrary，控件一级背景色反色</li><li id="ZH-CN_TOPIC_0000001776857164__li4499541155614">comp_background_secondary，控件二级背景色</li><li id="ZH-CN_TOPIC_0000001776857164__li9499154112565">comp_background_tertiary，控件三级背景色</li><li id="ZH-CN_TOPIC_0000001776857164__li10499184125614">comp_background_list_card，控件列表卡片色</li></ol></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p281mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.51556425022607555821042800849623:50001231000000:2800:2A7F3398F223FE503DCA75CF5F14A5FF8445029D9F182B683CEDE076044F7439.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row282mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row285mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p287mcpsimp"><strong>控件交互事件色</strong></p><ol id="ZH-CN_TOPIC_0000001776857164__ol13940114612562"><li id="ZH-CN_TOPIC_0000001776857164__li19940114635611">interactive_hover，悬浮事件色</li><li id="ZH-CN_TOPIC_0000001776857164__li79401946175612">interactive_pressed，点击事件色</li><li id="ZH-CN_TOPIC_0000001776857164__li159409462569">interactive_focus，获焦事件色</li><li id="ZH-CN_TOPIC_0000001776857164__li18940164685615">interactive_disable，禁用事件色</li><li id="ZH-CN_TOPIC_0000001776857164__li1194018462567">interactive_select，选中事件色</li><li id="ZH-CN_TOPIC_0000001776857164__li994011467560">interactive_active，激活事件色</li></ol></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p296mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.58030465499689019342776627029395:50001231000000:2800:144F5D37E315EA2B74238EDFFEDFE3327C55DECA5ACAD187F1F0CC564B03907C.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

## 界面背景色

<table id="ZH-CN_TOPIC_0000001776857164__Xf54223d5f2efa73cb1234e984d1cd207622a8b6" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row302mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p304mcpsimp"><strong>背景色原理</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p306mcpsimp">界面背景色主要用于窗口分层处理使用，在多屏及悬浮窗场景下，动态替换背景色的灰阶层级，避免相同背景在不同窗口层级下出现色彩融合的情况。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p308mcpsimp"><span><img originheight="1000" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102606.44396062298073214549048530060810:50001231000000:2800:E24DF540CAC1064B02AE4CF736DCC5A7BABC7F466AC017E1FD188B237F81F55C.png" title="点击放大" width="268.5" height="139.84375"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row309mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row312mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001776857164__p314mcpsimp"><strong>背景色分层</strong></p><p id="ZH-CN_TOPIC_0000001776857164__p316mcpsimp">在通用界面背景下，浅色模式的通用白色背景和雪域灰对应的深色模式都是黑色，这两种背景色作为浅色模式下的基础色，对应深色模式不区分界面色彩的差异化。</p><p id="ZH-CN_TOPIC_0000001776857164__p317mcpsimp">从 gray_02 灰阶色开始，无论深色还是浅色，都对应现显示层级逐级提高或降低灰阶对比度。</p><p id="ZH-CN_TOPIC_0000001776857164__p318mcpsimp">界面背景色不可为透明度颜色，在某些特殊情况可作为其他组件背景色使用，跟界面的层级关系依照灰阶对比度逐级选择使用。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p320mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.22725206714379336175074535272650:50001231000000:2800:EC96D886838532CE6A13DD9F72261B32F71C093ECE71EB9A84C6C427ABC9F0FB.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row321mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row324mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p326mcpsimp"><span><img originheight="1180" originwidth="2360" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.22331285431331799743853053787725:50001231000000:2800:84908182AEAA2D59D12D6DF0BF4050A78FA63E9C69F69F9A3237E83D9C7C01E5.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001776857164__p328mcpsimp"><span><img originheight="1180" originwidth="2360" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.34945184755984331129314670111566:50001231000000:2800:E16D684D7EDBE776B38CFD7012739CB3EA32E6DA0643B0F9E61698CD11A74330.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row329mcpsimp"><td class="cellrowborder" colspan="2" style="border: none;" valign="top"><p id="ZH-CN_TOPIC_0000001776857164__p331mcpsimp"><strong>界面通用背景色</strong></p><ol id="ZH-CN_TOPIC_0000001776857164__ol738411558568"><li id="ZH-CN_TOPIC_0000001776857164__li9384185575616">background_primary，界面一级背景色</li><li id="ZH-CN_TOPIC_0000001776857164__li13384155516569">background_secondary，界面二级背景色</li></ol><p id="ZH-CN_TOPIC_0000001776857164__p335mcpsimp">深色模式下，Primary 与 Secondary 对应的背景色默认都为黑色（background_primary的Dark资源）。</p><p id="ZH-CN_TOPIC_0000001776857164__entry336mcpsimpp0"></p></td></tr></tbody></table>

## **系统基础与语义 Token 全量表**

以下颜色参数为ARGB格式呈现，前两位为透明度参数。

展开

| 
Token

 | 

场景类别

 | 

Light

 |    | 

Dark

 |    |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

brand

 | 

品牌色

 | 

#ff0a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.96150303366307860946180096893540:50001231000000:2800:4692BD2879A14E802D198EB8E501F94C0C13BF0887CE2E30C07865AB6AF2DA01.png)

 | 

#ff317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.64133447243588411345310486637930:50001231000000:2800:1860A9534AF59B6DDE4AFEE6195D4D84B5187B484857B9BB39E9CB041FFA0D6A.png)

 |
| 

warning

 | 

一级警示色

 | 

#ffe84026

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.62746235581158972792335805116696:50001231000000:2800:182994C40212ACE6A03A54A9C610563BE06FABB76B765EA78DE382A513D9445E.png)

 | 

#ffd94838

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.98350425693361280314891610991631:50001231000000:2800:8AC844CD7B8E3FA4D8721333EDFC2BBA95E6F6291E4A799D317D05905CD7B516.png)

 |
| 

alert

 | 

二级警示色

 | 

#ffed6f21

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.80104447062302677012029793336521:50001231000000:2800:7343D4BE28B1D303C6674510902ABCA1109FA711529840AF2E43E65F7222D66D.png)

 | 

#ffdb6b42

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.89944247793138178118358863046101:50001231000000:2800:6B5305D168BDB45474810264158B5228339C8755F03AF02F957D8CE58863F4D8.png)

 |
| 

confirm

 | 

确认色

 | 

#ff64bb5c

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.51334772270320608693084681194705:50001231000000:2800:307276B1BC55AB94814796148A58C32ACA57C254E8193CE0447D540C0826C081.png)

 | 

#ff5ba854

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.13666399243883116724907327737120:50001231000000:2800:5883A6F96C3125AB26821B82F857AC7B1DF25BD865682BED935A9070AD6B12A1.png)

 |
| 

font\_primary

 | 

一级文本

 | 

#e5000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.27103453317614164114481958128082:50001231000000:2800:3E8006BF71B7CE51FF4A345D92A61D2BB9274B1026D84EF6903CC9EC2E9C59A6.png)

 | 

#e5ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.05876086478271331417105479261332:50001231000000:2800:329B70E5CEADB3ED7F6AB975C30FDA3D291894279B52A9A571858CAE93846234.png)

 |
| 

font\_secondary

 | 

二级文本

 | 

#99000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.15014361530937805083781658585805:50001231000000:2800:100551C87CA0256E1A67078C060E2DF1CF79CAAB822C802316B79D2ADE946E6B.png)

 | 

#99ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.02843700462269405181770761411481:50001231000000:2800:734138F477D037F8CC76A78066676938517B97D1B80E3613C8162F770AA513E6.png)

 |
| 

font\_tertiary

 | 

三级文本

 | 

#66000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102607.48542567703483731606759084158081:50001231000000:2800:3A0005869ECE7682FB7E87D93E33B2C2E67675281FDD09B57FC910E61F3307F3.png)

 | 

#66ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.35253134846737889337052776251145:50001231000000:2800:CD7461927D7A1E488CEE90832416B0F756F84A01049A36AE6E88E148FDC9F3BF.png)

 |
| 

font\_fourth

 | 

四级文本

 | 

#33000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.89874736592709239194948483036807:50001231000000:2800:0C30DEC7130EB2070DEC7F71C8DB0CFBBF5798A5F414B0384AEC7242DB1DC506.png)

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.55454830495595867924811513188856:50001231000000:2800:65D615A8D994CFA422013099EBA42DDDBE6A80F0BC00CB13B568BA221180B918.png)

 |
| 

font\_emphasize

 | 

高亮文本

 | 

#ff0a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.08411318833158465120108670394565:50001231000000:2800:CCD9B311C5F7A1B0A208A884EAAEA1FE4657DA8C786BB2D9B1B9936E8137EE97.png)

 | 

#ff317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.26618204483192970548846914219559:50001231000000:2800:A89F5AB4F5099F9AF021A709E4E261A07BFA913309659DED3EAB54D4F00C147F.png)

 |
| 

font\_on\_primary

 | 

一级文本反色

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.25155765544799676979326789909827:50001231000000:2800:8B9884A3220A2CE12CFBF42230F0954893F5A49D90DAF4140914A652FB447AC7.png)

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.19501624233751036225662190871293:50001231000000:2800:BEB0C1FF2F396993B1FADB3A9208FCB1FD61CD210F5D7E249B3AEA99D4039CB1.png)

 |
| 

font\_on\_secondary

 | 

二级文本反色

 | 

#99ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.76215300606987509850521095840378:50001231000000:2800:88FB04FC8F217FF4B6BB2FE4B095B2C187A4D725F18CCB48BC1665751F78ED91.png)

 | 

#99ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.53877506246474221478623373057544:50001231000000:2800:BF5A6C68F365AFDD80BEC212D244C43503E2AEEB4E0BEF6DF38A2B186A0A3027.png)

 |
| 

font\_on\_tertiary

 | 

三级文本反色

 | 

#66ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.51277188937688963001569383923906:50001231000000:2800:65831A9C19E396ADDB3C4808258D4A1077B64669C1FF42B3300DA7050CE71E42.png)

 | 

#66ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.79158148531808088459042870082895:50001231000000:2800:B6DBC0CBAB4F193BA57F45FBC626644417AF51313D30C8260F753873C6FA4FBB.png)

 |
| 

font\_on\_fourth

 | 

四级文本反色

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.52082965447094575781473699884373:50001231000000:2800:FC3B382CB9F9862ED017041722CB250FA892BEC7E80D7A059C6101C179F3035E.png)

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.32151565213396949709565716578121:50001231000000:2800:616C55669DC0CC06CDEE7D4DAFAEC2DFDF34E54D832D620644A6FD5287843FCD.png)

 |
| 

icon\_primary

 | 

一级图标

 | 

#e5000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.07792378342729029018686140210294:50001231000000:2800:4D6722898ED2ED1E1D1C58668118FE14B6B361246D52E486B3581F7D59C6EC8C.png)

 | 

#e5ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.24167680326994571184981640001149:50001231000000:2800:ABA0359F72BC1CA84BE85B31A3527297AC882EC3014B5226F21E9FD7CA240291.png)

 |
| 

icon\_secondary

 | 

二级图标

 | 

#99000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102608.79241377579792888847430074437586:50001231000000:2800:3575C0A980E97888B9B76697DC992E653815D6F1AE28A5E92240E17BA01ECC73.png)

 | 

#99ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.98839630459875852255558016703038:50001231000000:2800:6E83B4AA21A0CF089AC15FEA0CD0CDAFC4C0B68C2ED39F528B6959A887B39FE8.png)

 |
| 

icon\_tertiary

 | 

三级图标

 | 

#66000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.61936275156682357105841578101636:50001231000000:2800:46CC249BFB385300D2B26D889692156ED3CFA868D5F54CC3EEEFACEF87453A2A.png)

 | 

#66ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.90455153769579700214460596220793:50001231000000:2800:1334B00C128FCEB0E7BF65D43CB10975FFF808150FBFAB5F1A1ABCE7B6C964F5.png)

 |
| 

icon\_fourth

 | 

四级图标

 | 

#33000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.66550011477321257078718840221762:50001231000000:2800:A5FA585EEBD7875ADDF7D46009990B369036ECBA133E7A45B0632F419DA76CCB.png)

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.43949630751862546063543382233020:50001231000000:2800:44DD6EF791CDE9E35174768E555F45AD35CE78A1A0D951D188E166FC508A47EF.png)

 |
| 

icon\_emphasize

 | 

高亮图标

 | 

#ff0a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.53119069105110810952756571616711:50001231000000:2800:606F298EC30E26E1BFCF0B57BEC5A6A3FEF275B4DE641900E4BCA3D6CB7D8203.png)

 | 

#ff317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.04494920341474649580180870238045:50001231000000:2800:EE313EBD44D502E5C84AC41C087233462AD1016E9A1933C976B964553B7580BC.png)

 |
| 

icon\_sub\_emphasize

 | 

高亮辅助图标

 | 

#660a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.83890471565934628944101666768104:50001231000000:2800:F94A3512B0A423A8022030C934B68D255D6277F9BEC37039F5535E478E6EE255.png)

 | 

#66317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.55828616954235059669710621818604:50001231000000:2800:E54E48F34CB7B714EFAA0C61B9652A36B4B46D62ADACCBBB97A4DE220E07F0F7.png)

 |
| 

icon\_on\_primary

 | 

一级图标反色

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.56880354969383742620325863543654:50001231000000:2800:79B45AFDD1559FDDC7112F7AEE1E3E0C188C6535BED9DCBD990C7294752DA823.png)

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.99936592280652592260292895849752:50001231000000:2800:70D23A8D50F8B075295DB7E28C2DDD96FFD6F99D841160B339043291F2D9AEA2.png)

 |
| 

icon\_on\_secondary

 | 

二级图标反色

 | 

#99ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.64346378707431096492034163896374:50001231000000:2800:C578875C017055AF2442D5F581F318C132A417BD6BFD0E3CA94E5CEEC7D0FDEA.png)

 | 

#99ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.00753381946110703286172821027908:50001231000000:2800:4994D9AD6A8A49FA7851667B6FB32BC206A7F543DEE6CA15098D03C4913F9388.png)

 |
| 

icon\_on\_tertiary

 | 

三级图标反色

 | 

#66ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.61322404209146897503622479289921:50001231000000:2800:78E1175CA7BBAAE91F0E338E3EAD2273765B33052AFB9112417B00C3AFDBC196.png)

 | 

#66ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.24799274400660154069705006277224:50001231000000:2800:7FAD2A799DCD4EEA0AA25986581215092CB59088A93D517AD3092CD8F98550D2.png)

 |
| 

icon\_on\_fourth

 | 

四级图标反色

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.80022743621634499788150479154319:50001231000000:2800:5E634F4F260D85FC142447AE5F74ACA02C4A35524C12BF325BD7893D279B8A9A.png)

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102609.64761873778686831888734778244747:50001231000000:2800:0A1348A956117A03ECD74798E3275297AA20118C90BD6C9168465AD49AFC2AE8.png)

 |
| 

background\_primary

 | 

一级背景（实色/不透明色）

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.43646773305270685081032725576287:50001231000000:2800:758ACE3AF43D3DA59DAB4038DFBA690D630D38ED56CF1CAA18F3AE5B2E29DF44.png)

 | 

#ffe5e5e5

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.99674217304881714197433428456860:50001231000000:2800:5FFACA6C8FBE2D9F6F5A48192309D17E8F15FE4836C42DFC2D3835EE31702762.png)

 |
| 

background\_secondary

 | 

二级背景（实色/不透明色）

 | 

#fff1f3f5

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.93409488654590277812425004950671:50001231000000:2800:2DAF6665B56DF7256195EC31E6B1AE29BC158E7DEF6CDE226D061E7365145BBC.png)

 | 

#ff191a1c

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.60280123920383031279640369692485:50001231000000:2800:5A61465350A02A6116883010ECA9DADE35EC1E35323F5D011BA91CD392B0DE0F.png)

 |
| 

background\_tertiary

 | 

三级背景（实色/不透明色）

 | 

#ffe5e5ea

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.90769598052778254704743228911031:50001231000000:2800:354FF34859B7DF04A36045C11EB437B480E8040107894A05947923462340257B.png)

 | 

#ff202224

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.13700208512462390675557836844939:50001231000000:2800:5ADE5C8DF25857ABA228313F578CCD0AAA00091048B566B38177E5B345C60076.png)

 |
| 

background\_fourth

 | 

四级背景（实色/不透明色）

 | 

#ffd1d1d6

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.27672810370904199476911520277731:50001231000000:2800:03ABE31C9FCA6267726CECE6A18D59394D0DE9CA7CE054461D2E90AC3C571695.png)

 | 

#ff2e3033

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.10288516479267049149923113683176:50001231000000:2800:52FAAE50F291EEA2AAAB17213F26D987C03152E158F1104DCB3ECB752D995357.png)

 |
| 

background\_emphasize

 | 

高亮背景（实色/不透明色）

 | 

#ff0a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.16122001522736610981102494173609:50001231000000:2800:BDE749C4D9DA33C354F69EB936E81E8ABF13B956F8C16EBC5FE729EF515C566A.png)

 | 

#ff317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.07712102549939814506333639371205:50001231000000:2800:AA2ADED587A5C5D432EFC16637FEA6500BF3914475821DCE64997017471200D1.png)

 |
| 

comp\_foreground\_primary

 | 

前背景

 | 

#ff000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.86604623938605648084583663620707:50001231000000:2800:A00162726813A62C7225063D3661DED85F0DC18AEE66F383F887193FE85F15E6.png)

 | 

#ffe5e5e5

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.78750783094334838804653496488670:50001231000000:2800:2123EDF14FE37063ECD83ABB6016AE384DA998FBE52CA7B91BF7342540A6E33F.png)

 |
| 

comp\_background\_primary

 | 

白色背景

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.02170242241166886681564617053913:50001231000000:2800:AFB6D3C8B58EDCFD6EE296F38FFDD86F4B054AB84C02166D43B6D3F0DCC860AA.png)

 | 

#ff202224

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.49661313008938981235753391320855:50001231000000:2800:9CFAD3B2B14E8B0F1E793E7CF76C70EE4B606AE7078FA243272B136FFE75AC8B.png)

 |
| 

comp\_background\_primary\_contrary

 | 

常亮背景

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.29218011220354626284746102467743:50001231000000:2800:EEDE39C31FF233D2B2004669A3E944FAC86C4515A4D7CF51E0C6F95728DC0D74.png)

 | 

#ffe5e5e5

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.84385864359708444976557280728769:50001231000000:2800:E31056D4C1A67550A6A6188D40DF2C707C33E0EB4BB40F2CEBC392FCC3CB0DC0.png)

 |
| 

comp\_background\_gray

 | 

灰色背景

 | 

#fff1f3f5

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.54982310996865566269516224093851:50001231000000:2800:98C0A52885A7ED8C5F7B464991C08DD9B480A75BB2F5F71EB53F0074EE923DF9.png)

 | 

#ffe5e5ea

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102610.08113907090801786017323101470701:50001231000000:2800:00C06169762BBF29BD34D4AB8977DDECDD3A6AA71240C50B7F9E3F53C2ABE288.png)

 |
| 

comp\_background\_secondary

 | 

二级背景

 | 

#19000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.83543259843328227580594690621703:50001231000000:2800:54D68ECF4511AA0C6E60BF0EF724F8A773BD4E09814C5C4E34DF845931F1C3A8.png)

 | 

#19ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.13429369540051585371407109170327:50001231000000:2800:E5AB1296CB1AD0E16CDC99E57E61E7C79E74E682BA08C54FBF45B4341AEA1048.png)

 |
| 

comp\_background\_tertiary

 | 

三级背景

 | 

#0c000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.52635455573688363781775449822237:50001231000000:2800:AF46B4B4427FBD249BF606D1ECBEE3DCD158FFDDEB850DFDB96E688BC8447705.png)

 | 

#0cffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.69157502452277507902362042861239:50001231000000:2800:2BE86D59BBF0AADE66889A646F2FD2F55EE83C899E08EEF09CA89BE71EF2C060.png)

 |
| 

comp\_background\_emphasize

 | 

高亮背景

 | 

#ff0a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.15450258501449677798640959251178:50001231000000:2800:33AA98B14B7FD0F1B544B25CB4FBD30B55F197102C4738A861D626B80AD75751.png)

 | 

#ff317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.43110128374015968164560848094419:50001231000000:2800:D6621D0D0495129B3CBAA9178361D7553A22506E0948E7700C0BB5E7E9373314.png)

 |
| 

comp\_background\_neutral

 | 

黑色中性高亮背景

 | 

#ff000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.99104184689136375560656358663322:50001231000000:2800:D02908C25A439FC4898A557B356874751F064A844198E28B858A87D6EB152AAD.png)

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.50203389546962864613252746381102:50001231000000:2800:E1126C5AF89D77B57BCA4893D9CF6D32FC3ACD95F2CA3FE6957329EC09F23666.png)

 |
| 

comp\_emphasize\_secondary

 | 

20%高亮背景

 | 

#330a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.76585266439363136184462671853266:50001231000000:2800:C9AC779BF029F5ABD58D909A0A50C6BB90062BA947960DC21B72585460A1055E.png)

 | 

#33317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.00506629295749599724125462186315:50001231000000:2800:30CAA757375811581F3086D8BDBF0EF919A2F58D054EB5999ED1F2E3B1C6DCE8.png)

 |
| 

comp\_emphasize\_tertiary

 | 

10%高亮背景

 | 

#190a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.80758453006705787516124899843979:50001231000000:2800:13A1AE6F6461ED7EBE2AD9D9C22279B9D4F975B9D12B54E9852D2482C5B56265.png)

 | 

#19317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.73677408361747478272819965458282:50001231000000:2800:FC6C4D56C1FD2AFF244E263E9741C8559965F68230057EDD0988C174A8DF5A2E.png)

 |
| 

comp\_divider

 | 

分割线颜色

 | 

#33000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.85896358151701422099063062499876:50001231000000:2800:7272FD4DDDBFFCF1DC603DCE2B482331A382A58DE6AAD74B00F8DFD3AB23FDD6.png)

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.58862349457577132354858650367689:50001231000000:2800:C1CB5D053FA5699C02FF433AEAEE36EB7562AB6901A2AED68EE98FFF4BE05212.png)

 |
| 

comp\_common\_contrary

 | 

通用反色

 | 

#ffffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.79970056263621032006797014480721:50001231000000:2800:EB335D1F0E59E28DBBC6B82B423D696A7263C7C79F7D9C816AA7AF5BDD5DF510.png)

 | 

#ff000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.66907482428790312113116393362121:50001231000000:2800:96722EA10079650C953DFD7F68DD97F63B146C63C67299FB5F2F1AC67399EBE3.png)

 |
| 

comp\_background\_focus

 | 

获焦态背景色

 | 

#fff1f3f5

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.55424301305635965464189774419578:50001231000000:2800:13DA53B5DA6204A2BC75A46DF3DF79419E96CF96696DBF63F5794651071FAB08.png)

 | 

#ff000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.56235271080995681796995161467125:50001231000000:2800:59D7D71AEBEC6F2F978F349D031A6B796C21071BC4B299A45981F49D4AE68F8E.png)

 |
| 

comp\_focused\_primary

 | 

获焦态一级反色

 | 

#e5000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102611.59408890491824479331405111034282:50001231000000:2800:B89FBBB9A0D57A600DAF36812B24949751A696BAFC77BA92CFA6B43BF1328378.png)

 | 

#e5ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.26889273286777698670330125535653:50001231000000:2800:44964ACEBB7E5BEA475BBAD24BA95FFD68C5B92873DEB4DBD3E9D9F7568CEAC6.png)

 |
| 

comp\_focused\_secondary

 | 

获焦态二级反色

 | 

#99000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.24242788330747773332541520801668:50001231000000:2800:FAAE53C3C7E9A5CDD9931CAFE9DEF3DC6000DC8F11B6A3FB0CC740E67CD1E4EA.png)

 | 

#99ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.91133171591619975783293004132018:50001231000000:2800:B0A478733289E5B031E1EA3C031F61CBA560958AE839A262A27CADFB54A006EB.png)

 |
| 

comp\_focused\_tertiary

 | 

获焦态三级反色

 | 

#66000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.03268579488169088802399086829621:50001231000000:2800:3D922331C3BF0E841C37C7FD434C6365CFBC8E88DD9D7BB191D0A2E112845F1B.png)

 | 

#66ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.39851923214207872429866134966053:50001231000000:2800:6284656AA3C92F90A94122AC660DEC25785DAB2652EA046DFC9AC9FA891E1F45.png)

 |
| 

interactive\_hover

 | 

通用悬停交互式颜色

 | 

#0c000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.28095629623376798611470034544683:50001231000000:2800:A98638B98E2058FF6D7FD89F5FCB89FFCD1056DAEEA0123890C53F47091B413B.png)

 | 

#0cffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.49250942068330798120177435847902:50001231000000:2800:4C12FD82091E179DBE4A970F25C668E1B6C14F7B95EDE610212E889F58179160.png)

 |
| 

interactive\_pressed

 | 

通用按压交互式颜色

 | 

#19000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.49554003283345458312392868639641:50001231000000:2800:019FEC126477A07656F4200F09E07EE6884AF8268DE747DDA3CF5BB4551018F2.png)

 | 

#19ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.35658997772830161363352004741886:50001231000000:2800:4EE6D6C2A9D261B72AC83567313E484EFFDE48CE0DDA62F8388675EF10107F8D.png)

 |
| 

interactive\_focus

 | 

通用获焦交互式颜色

 | 

#ff0a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.04236250482771238310173085589910:50001231000000:2800:E032340D2276EFAF8613798FDE51BA01548E10D47F6BFDD5E2D27DB359EA5178.png)

 | 

#ff317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.76889158821179852371825102689018:50001231000000:2800:58859E3A214E89C5CBA0D93F4184D4BF88891406CBB542226B331F46A4E8A7F8.png)

 |
| 

interactive\_active

 | 

通用激活交互式颜色

 | 

#ff0a59f7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.74793726327943865974030504836153:50001231000000:2800:EB1826990CBD5B2E130A1AEF49CDC3C732279AC2E4DD2B6017FCC178A6F20AC4.png)

 | 

#ff317af7

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.88286579971373888886947720409371:50001231000000:2800:A8C44F8C2970AC46223B8B258857CA790E75BE1E709390C051329A1A17A16B6C.png)

 |
| 

interactive\_select

 | 

通用选择交互式颜色

 | 

#33000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.47135514380042010008599785669587:50001231000000:2800:EB93C1CE53D2474FD86B9DFB4638FEA9E5818291BAE26755C0929B6D7C7ED9DD.png)

 | 

#33ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.50017268436212132646881449132236:50001231000000:2800:54A4A5AA33527ACAFA96BC35C222A9705499EDA83C834E695CFF2E70E0649751.png)

 |
| 

interactive\_click

 | 

通用点击交互式颜色

 | 

#19000000

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.78307491601587875523502157816196:50001231000000:2800:4F93CD7EB00A4AE5981CEF18862FFD6970A6ABEE3C66E889827295BB161B6CA8.png)

 | 

#19ffffff

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.58760470839543984200379919977043:50001231000000:2800:5EEF0182C67A1AA7132946585BF351F6ADD048C013A213B58714B9619E34A727.png)

 |

## 智能穿戴 Token 全量表

<table id="ZH-CN_TOPIC_0000001776857164__table1855185910304" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776857164__row17551115973018"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p165511591306"><strong>Token</strong></p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p95511459153014"><strong>场景类别</strong></p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p455120592306"><strong>Light</strong></p></td><td class="cellrowborder" valign="top" width="12.48124812481248%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p17551259193010"><strong>Dark</strong></p></td><td class="cellrowborder" valign="top" width="12.161216121612162%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row155275912301"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p14552125916305">brand</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1955255914307">品牌色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p655210595308">#ff0a59f7</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p3259152810594"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102612.26551893607832015814742477748144:50001231000000:2800:002A412109FB63B6CC13FB0620D5FD8C2919E4E01A346F4B94A9574FE8EA3542.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p355214598304">#ff1f71ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p9997239105912"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.17149818264736115667961419954866:50001231000000:2800:0237ED88DB11E19F79DEEDF3A334AF77319975CD0E81E076474B7D96B6638B0D.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row25521659103012"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p165521659133013">warning</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1955212599304">一级警示色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p7552115918304">#ffe84026</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p1766885045919"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.15095784507781722637374459316099:50001231000000:2800:F644452D39982C84378E341A73FB8180C0CB1FF5320A9A2C0F7B755AFCF58C77.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p655245919302">#ffe84026</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p13292059135917"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.16339777926952092349227468423122:50001231000000:2800:175715B693FE7D69EFE6C0D63BD39309D1624543EE018730180784FB25F9F137.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row113215447388"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1532184419383">alert</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1832044173816">二级警示色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p33254453811">#ffed6f21</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p15230135528"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.80701599031450404190903740089733:50001231000000:2800:F4BB934FA5D0B3FB4ADD8C8CA7D27429049A67415EEBF50F412315531A518473.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1432144411384">#ffed6f21</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p1986914501624"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.32531589501916184747622894625836:50001231000000:2800:A5DB2CE49F43C51AFA51B9CB6A4AAE1C656F0FFDD325E087012DCA9B1F5AC8D7.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row15879124563814"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p4879545163818">confirm</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p11879945143814">确认色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p158793452389">#ff64bb5c</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p11884101437"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.28152757604092354293971954445921:50001231000000:2800:D288BB1003078524DD890E71E912801C567A5FD49E5063E25E952BB64DF10497.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1187920451380">#ff64bb5c</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p105492077319"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.22635993457249266010448017712625:50001231000000:2800:5FFF8102F22CFA35DB8B1DA1E3AE6B309BC9198E14E0A5F69D9896417D267558.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row18319946123815"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p93191646133814">font_primary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1319104623818">一级文本</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p93191246153811">#E5000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p16386124215418"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.77304615600200827803814435783876:50001231000000:2800:04C267ED8EBC369AFC01550D1089558ECC83F436E6D719C432C423D1662D7A5E.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p231911463389">#ffffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p1362514588415"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.61847514415557534599392276692179:50001231000000:2800:F1CC003AF645AF4CF4459DAE7357F899CE04B98D7E5AC4CC3462D603B7F51658.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1654916461385"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p165497469382">font_secondary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1549144617385">二级文本</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p115498465382">#99000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p389714509417"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.16110716299013652146699396951285:50001231000000:2800:C52EF3CBF9663424F4628C387094FB177590856A4D8E042B442844F38F54392C.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p654913467386">#A9ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p2041513111254"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.29847493649811528470328726583616:50001231000000:2800:3A79DF2FDAB491EA14A264E3601ED188B666EB02B0AC81FF9C938F35030728A3.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row197541546153819"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1755144633810">font_tertiary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p9755114623811">三级文本</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p0755104617382">#66000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p73745302613"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.77795679680878304772423506936324:50001231000000:2800:09ED1590B08035CC552FAE630A912E9A80C1D990AD00B3811CEE3914903CCA00.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1755194619380">#66ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p19125451164"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.40564034241955743622911614703888:50001231000000:2800:91A8AAEC7C08CE74158D58B1920EED40439641F88D93255DC62BE2B4D90D8AD4.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row179741527113714"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1097432718372">font_fourth</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p09748273372">四级文本</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p79741275375">#33000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p23223374617"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.06516331438593818911314123957684:50001231000000:2800:59606BD4096077D872987B150BFE13AE9F129073818B3DE7906BF774CCB2C99E.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p16974172714379">#33ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p16932115119619"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.42538195888453613046391689532181:50001231000000:2800:AC4081014B3E8A26BE857DF7C2A4EDA393FF2FA4B1A765B46C3A7E191BBA147B.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1699024633817"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p179907463389">font_emphasize</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p2990124693819">高亮文本</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p1899054673815">#ff0a59f7</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p48432311109"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.41745316308420531578142034205208:50001231000000:2800:EF5BE4705D28AE1603751DD899EE384BBFA62C32B7EC0DDB88B1E72D4DD0CE1D.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p10990946103818">#ff5ea1ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p126410336116"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.80002908174866989683278642774131:50001231000000:2800:E8ADD28C8AA7306B5DE503F55CE958D9D4F00F5DA2789FE617161A21EC6BB3BC.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row48018192715"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p48015191679">font_on_primary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p10801819777">一级文本反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p108017195714">#ffffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p2059543814101"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.13580062698001084336260908428931:50001231000000:2800:7661AD108FDAEB33FF7FA9AB4D782DE5E5308B3047CEC02FB99FE85B44A77BEB.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p280181911710">#ffffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p762113910112"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102613.07303107943261824761021948878353:50001231000000:2800:CC7C877F3D696DD38BFC476B90DCE312597BE89EB15588A3A799781F729996A8.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1153111910716"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p6531019271">font_on_secondary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1153110191079">二级文本反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p453116199714">#99ffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p468334441013"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.32710148707577520917360411443865:50001231000000:2800:5892164CEF8FDBBBE75227D039651188A95C9945DCED33C7B400BECC783C047B.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p4532419273">#A9ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p0332134621112"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.28147836856731684882488909951188:50001231000000:2800:4D969E051465CA6A0E20879354043965008594355FBBBDD0D3B14D925B9778F0.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row6903181919718"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p990381919718">font_on_tertiary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p17903161911711">三级文本反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p39031219775">#66ffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p118799508108"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.14505357101436157942224610957766:50001231000000:2800:38B87D361F5C8FA7881E40F028623D7BFD525595064D5B3400D2857C4A76B8E7.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1190381917718">#66ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p1964610536113"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.41647888114291579430437677947415:50001231000000:2800:523782FB0EA20884780FDC02342B723EC15E5DCD6DFD762557E3BB0E5AFE268B.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row42341145193613"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p2023418458360">font_on_fourth</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p62344453365">四级文本反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p122341345193611">#33ffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p56031580102"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.76162031733215440259193014850156:50001231000000:2800:A21B45B5C48FF43E8CB2D84D06204CFB4276546EAD4C8354C22686203993ADBA.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p32347453363">#33ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p13264191111215"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.43534360389489365106930632806183:50001231000000:2800:88CB56D046090FAFC3CAD0333F5D19A3FB03ACEFFF5DE190712FE23D76A41A28.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row5499132017719"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p204997206718">icon_primary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p104991201676">一级图标</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p134991820678">#e5000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p114518524173"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.87179940570441238538265543689776:50001231000000:2800:B521AC7F8DCA9C8D3238AC342BE7E1F4F642EF06CD22C6F1CE236434C90331A1.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p249916203714">#ffffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p965323851811"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.94758325052556402318352684243945:50001231000000:2800:2AF38C8A6D9337453C1AE4F702C220F42C71332CD6239B9D6ACD706D1E9FC0A5.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row119281459229"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p6928165102216">icon_secondary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p3928115162213">二级图标</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p139281953223">#a9000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p395141111812"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.84861047386901742668983480020620:50001231000000:2800:0351D09631668EC18E18FFE7DA314FDE603808BA1B129BB706EAFA1FB9401FD7.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1592816582215">#a9ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p162869456182"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.55715608258985730097381192490639:50001231000000:2800:443981E7D804162E0B8C0AF77590EB39F1C874490B402F43F4C992A79568F9E6.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row73732682219"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p173734642211">icon_tertiary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p237366182217">三级图标</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p1437419617221">#66000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p22951374181"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.05115141484137410330898743572626:50001231000000:2800:FC0FB73A135AD2406628BF99CB807DCD7D7D96E1654558BB9E2CA800287D8F83.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p7374196192218">#66ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p11698950151816"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.66739074057112236261998002354748:50001231000000:2800:949EA09EBD1A2E2C847E429B4881437BBA387F8C6EF35082F761B2637AE5F585.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row08330588371"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p12833115813718">icon_fourth</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p4834105820372">四级图标</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p1983417584372">#33000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p7942191312182"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.33348386086794286742134724350149:50001231000000:2800:B6EAB6D8ED78DDAE36D7303E114AAE53B563662C6C6DF070FED270BB5FB0ACFC.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1183420589376">#33ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p328395791815"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.79239929088400028077518883530224:50001231000000:2800:7CC3787DA8D1BE6E47DCC338C0D9AB83F2E59CD93E0D5B1092484B08FED9DE6A.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1060617622216"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1160611618223">icon_emphasize</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p960619616222">高亮图标</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p16061615225">#ff0a59f7</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p1368010132011"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.00222284803812104886602789195174:50001231000000:2800:E73CB60AB7D20F5BA43A42BFDD55C9BDD362FB913C4C20A66D2F65BC4D86900A.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p86074632213">#ff5ea1ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p176191716202017"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.41682263499453393146811024547116:50001231000000:2800:5B0E03B325A51DA6AB18B3A41EFB13CB1EFEEB0EDE2B8A8E01DEED810EED7002.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row45571988229"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1155768172212">icon_sub_emphasize</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p4557687228">高亮辅助图标</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p135587814224">#660a597f</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p1451314972016"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.14548290536974365578485392121025:50001231000000:2800:61C80C79B05C3913B172BC7FBA331EE0F9C7A23AB7035DB7D4CF60555FC3DF64.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p2558984222">#665ea1ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p19149122319203"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102614.00791031229985378693941148658161:50001231000000:2800:15CFDAAB3E95F9D1BC7D9CA7CAEBD9F932F927FA47C9D25053422D56B87F3E22.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row15274143010221"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p92751230152216">icon_on_primary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p152750309221">一级图标反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p12751130192217">#ffffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p2125111913228"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.33666177575374737161963586313011:50001231000000:2800:5EA3B21D3145920D8629838A60C780CAC9C8D038CC45969516AFE677F1429F4F.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p102751230102211">#ffffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p1946894811224"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.59648150171544026220807262038080:50001231000000:2800:577BCA3A9676EFC14E35A643EEC3D0D2BCA4E8C05713D2F8B73F00DFCAD0DD4A.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row18538153042218"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1539630142217">icon_on_secondary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p55391030162214">二级图标反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p453923012214">#a9ffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p12992624142218"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.02267793125942426097497739409842:50001231000000:2800:80DF4C5BC66F3C024B755D2340367A40F2219FEBF8BEF71BD3D012251560A221.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p115392030142210">#a9ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p1131645519228"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.53656803455042307535775372272779:50001231000000:2800:380B8651C604F38F1BD1A1D9877FFAE022FC841AD8945A5139741E0C45993F8D.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1974663013221"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p47470302226">icon_on_tertiary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p19747193017221">三级图标反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p197477308229">#66ffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p185753016221"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.05207778340674702136226933168983:50001231000000:2800:F5100A4732824780E12B34B51D1F7FB453A25DB58A4C1F33357C76B1C667C4A7.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1974717307224">#66ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p685071142310"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.07524575305254513719636141248485:50001231000000:2800:F48A25E1316A4F72A3D506CBDC4A9BD2E3E8A524A9F3FB680503750C00472F7F.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row31682811383"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p101715284389">icon_on_fourth</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p181719283389">四级图标反色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p101782813816">#33ffffff</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p151169374227"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.88231905513732324042050947295607:50001231000000:2800:0B5CE139A03AD983B68D1D00ECB768475FB973EC84C2AA13B233AF85930B5D51.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p10174285381">#33ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p168593842311"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.10496851337525664421289999713218:50001231000000:2800:F2DE719C5EFF6EBF1FFD6CF297973109CE16D7E93AD6F9C20CB1A60A06913043.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row1392723042214"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p3927153062219">background_emphasize</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1992753002211">高亮背景（实色/不透明色）</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p09271230152214">#ff0a59f7</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p54538408241"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.76350495014878750452719233991076:50001231000000:2800:E90063B29C7454841C0A37A040BB84C6CB3F296205F60BDD73FDB0CBE2EC6774.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p18927163012220">#ff1f71ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p625113282514"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.45704307145595971787241297437490:50001231000000:2800:24D279D3E2E7538E7ACAE0B4D3CBBC6F6599DD35DE6EC65B68BC13CABE19FC5C.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row171079315226"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p910713114220">comp_background_emphasize</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p16107731142219">高亮背景</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p101071031192216">#ff0a59f7</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p19850124512416"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.34571062684159746834051541565398:50001231000000:2800:7779CE256636DDFAE4915ABE7400C9CFE89ECF8D7B6962534A02864F2270402D.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p16107731112216">#ff1f71ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p67211552613"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.25075676031424501212578452509506:50001231000000:2800:F5B2DE80FD77E6917BCE06B7AD2C4D0043C09FD2904E575271A9E9AAACDD1845.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row52744310228"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p42751231142212">comp_emphasize_secondary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p127583116221">20%高亮背景</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p19275831142216">#330a59f7</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p135881751152417"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.02514389969117071602507860277246:50001231000000:2800:B72B9566D326CE38934A3356E95F61F04B951D9E9822F2F6CA1087E9D674807F.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p17275123122211">#331f71ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p18268141132617"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.10609434348005196092457434423940:50001231000000:2800:777C9FAEE6152F61DAA015A26669FAD63178F64ED04AC4FB37FF7103946D9539.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row16447103142217"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1444773152218">comp_emphasize_tertiary</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p16447183162217">10%高亮背景</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p194471131182210">#190a59f7</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p920845782415"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.00281091978910302115480467973822:50001231000000:2800:EE2AA30AC6B3434B0B5ED93B1DFA9E3DA02418256DF4A0772BADCA71873DDEED.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p184471831192211">#191f71ff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p12891717152612"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.39995731202517407492687277689930:50001231000000:2800:F08466DD9EF5A887A75DE3848713A266B1366C9619757244277623F3DDAE1005.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001776857164__row10310192711263"><td class="cellrowborder" valign="top" width="19.99199919991999%"><p id="ZH-CN_TOPIC_0000001776857164__p1631092792617">comp_divider</p></td><td class="cellrowborder" valign="top" width="27.202720272027204%"><p id="ZH-CN_TOPIC_0000001776857164__p1310132782619">分割线颜色</p></td><td class="cellrowborder" valign="top" width="14.24142414241424%"><p id="ZH-CN_TOPIC_0000001776857164__p173103277261">#33000000</p></td><td class="cellrowborder" valign="top" width="12.48124812481248%"><p id="ZH-CN_TOPIC_0000001776857164__p28571842254"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.56571520498503234837139127157728:50001231000000:2800:49B9747E30EA824F0BF8B8A781772C0A94023FB77B763B1861D3308C096F666F.png" class="notEnlarge" width="29.505550555055493" height="11.802220222022196"></span></p></td><td class="cellrowborder" valign="top" width="13.92139213921392%"><p id="ZH-CN_TOPIC_0000001776857164__p1631182719266">#33ffffff</p></td><td class="cellrowborder" valign="top" width="12.161216121612162%"><p id="ZH-CN_TOPIC_0000001776857164__p16889223182610"><span><img originheight="20" originwidth="50" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251111102615.14640093476281726428201223623677:50001231000000:2800:A12C9E595BC419E67CB92946369D6A4A2107A8CEB9D23581BFFE87F70F2ADC95.png" class="notEnlarge" width="27.466946694669474" height="10.98677867786779"></span></p></td></tr></tbody></table>
