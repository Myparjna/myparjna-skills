# 弹出框

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/dialog-0000001957012569
- 抓取时间：2026-04-04T08:23:35.488Z
弹出框是一种模态窗口，在弹出框消失之前，用户无法操作其他界面内容，是一种对用户在进行界面交互过程中干扰性比较强的控件。通常弹出框用来展示用户当前需要执行的操作或必须关注的信息，其他情况不建议使用弹出框，可考虑应用内通知等其他非模态窗口控件。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150815.10068659158986972253949226062603:50001231000000:2800:7BFEBC4DE3026738B970AA906D2C76EE0AC810EAEB1729E1B546A53E71932526.jpg "点击放大")

弹出框的内容通常是不同控件进行组合布局。如：文本 (可带格式，如缩进，链接，粗体等)、列表、输入框、网格、图标或图片。HarmonyOS NEXT 中提供了系统默认风格的通用弹出框控件，布局样式可参考 [AdvancedDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog) 组件，开发者也可以完全自定义弹出框，可参考 [CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box) 控件。

## 如何使用

弹出框内容样式的划分上主要分为选择类和确认类，选择类多为不同组件样式的合集，使用场景为提供多个可选项内容让用户进行选择，可能是列表形式或是宫格形式，内容一般以开发自定义为主。确认类多为提示类内容，多为文本的组合，通过文本描述当前的使用场景让用户判断是否允许执行某一项命令。

<table id="ZH-CN_TOPIC_0000001957012569__X466aa8ded3aa5e2ab58f2a1c7d8d71d988c0fec" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row114mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="55.00000000000001%"><p id="ZH-CN_TOPIC_0000001957012569__p116mcpsimp"><strong>选择类弹出框</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p118mcpsimp">弹框中以列表或网格的形式提供可选择的内容，选择一项或多项。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="45%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p120mcpsimp"><span><img originheight="1080" originwidth="2160" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150816.83470677600364209679237755110518:50001231000000:2800:24A6791ADDB7C51B5DDD239D5AE98651C085735FEB16B9CE7233D97DF155B906.png" title="点击放大" width="236.64999999999998" height="118.32499999999999"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row124mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="55.00000000000001%"><p id="ZH-CN_TOPIC_0000001957012569__p126mcpsimp"><strong>带图形弹出框</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p128mcpsimp">必要时可通过图形化方式展现确认框，以便用户更好理解或认同确认内容。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="45%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p130mcpsimp"><span><img originheight="1539" originwidth="2160" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150816.20148177975614353610524103235901:50001231000000:2800:8CF887567871B57C02B37C3C13A474CDAA9DA6C37B0623B534788AA14CD063E1.png" title="点击放大" width="236.64999999999998" height="168.613125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row134mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="55.00000000000001%"><p id="ZH-CN_TOPIC_0000001957012569__p136mcpsimp"><strong>带输入弹出框</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p138mcpsimp">需要用户输入内容时使用。无输入内容时，确认按钮置灰。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="45%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p140mcpsimp"><span><img originheight="1080" originwidth="2160" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150816.81936690146512286290315946996865:50001231000000:2800:07EA7DFADCD5F5CE4500309A30CCD92FAF1A840CAC7E07EC76AE46479D0DE5BC.png" title="点击放大" width="236.64999999999998" height="118.32499999999999"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row144mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="55.00000000000001%"><p id="ZH-CN_TOPIC_0000001957012569__p146mcpsimp"><strong>信息弹出框</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p148mcpsimp">操作未正确执行 (如网络错误、电池电量过低)，或未正确操作时 (如指纹录入)，反馈的错误或提示信息。尽量在弹框中给出解决问题的选项、入口或帮助链接。选择查看内容详情时，如查看文件详情。或是需要在继续操作前了解的信息，如权限提示框。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="45%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p150mcpsimp"><span><img originheight="1080" originwidth="2160" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150816.92958481776249512556714258070428:50001231000000:2800:AB2481D0D137053B137D70B2CA23256C9018F807528211160E325FA099229079.png" title="点击放大" width="236.64999999999998" height="118.32499999999999"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row154mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="55.00000000000001%"><p id="ZH-CN_TOPIC_0000001957012569__p156mcpsimp"><strong>操作确认弹出框</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p158mcpsimp">触发一个将产生严重后果的不可逆操作时。如删除、重置、取消编辑、停止等。</p><p id="ZH-CN_TOPIC_0000001957012569__p159mcpsimp">触发的操作包含一些需用户知道的影响，或关联设置项状态会产生变化时。如允许开发设置、允许 USB 调试、设置无密码锁屏会关闭指纹校验等。触发的操作需满足某些前提条件时，显示解决前提条件的推荐确认框。如开启应用锁才能关联指纹、先安装某应用才能进行操作等。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="45%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p161mcpsimp"><span><img originheight="1080" originwidth="2160" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150816.62999275147547718671820686973411:50001231000000:2800:517FF49238E8245E09D653E9190B34E905F0A29A42763E83DD44151A44385BA4.png" title="点击放大" width="236.64999999999998" height="118.32499999999999"></span></p></td></tr></tbody></table>

## 组件规则

### 控件构成

<table id="ZH-CN_TOPIC_0000001957012569__Xdf35aa42bcf261251ba408087984833fac5e1a2" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row185mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47%"><p id="ZH-CN_TOPIC_0000001957012569__p187mcpsimp">基<strong>础构成</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p189mcpsimp">弹出框由三部分区域构成：标题区、操作按钮区以及内容区。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="53%"><p id="ZH-CN_TOPIC_0000001957012569__p1227078113216"><span><img originheight="2700" originwidth="5400" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150816.01855509989009459878450729190604:50001231000000:2800:CC41A0E651158E6CB7E936EC2815AC83B38013F46E7DB677A19039F3664F8801.png" title="点击放大" width="287.61" height="143.805"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row195mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47%"><p id="ZH-CN_TOPIC_0000001957012569__p197mcpsimp"><strong>标题区</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p199mcpsimp">纯标题 (单/双行标题）</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="53%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p201mcpsimp"><span><img originheight="2103" originwidth="3624" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150816.29123549200478664530820687032575:50001231000000:2800:A79A8F2CBADE00A92629A907B211886889A7A36176276D4DC5F0948AD32B72CC.png" title="点击放大" width="287.61" height="166.89951158940397"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row205mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="47%"><p id="ZH-CN_TOPIC_0000001957012569__p207mcpsimp"><strong>按钮操作区</strong></p><p id="ZH-CN_TOPIC_0000001957012569__p209mcpsimp">默认按钮宽度不超过弹框宽度，按钮左右布局。按钮组合数量超过三个及以上时，按钮改为上下布局，布局顺序由左至右修改为从下至上。</p><p id="ZH-CN_TOPIC_0000001957012569__p210mcpsimp">在需要强调的场景下，按钮可使用带蓝色背景填充的效果，强调按钮支持模块自定义。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="53%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p212mcpsimp"><span><img originheight="2103" originwidth="3624" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150817.91875963233253775438542214618871:50001231000000:2800:D3369DD26503B383AB297B88726EF2E6BB03199FCC60D925F297BED93B458236.png" title="点击放大" width="287.61" height="166.89951158940397"></span></p></td></tr></tbody></table>

### 视觉规则

弹出框的结构主要分为标题区、内容区、按钮区三个部分，其中内容区属于必选项，在一定可视范围内允许开发者自定义要展示的内容和复杂布局。

内容区通常是不同控件进行组合布局，例如：文本、列表、输入框或图片，常用于选择或确认信息。内容区的描述一般为需要用户确认的内容，让用户明确操作弹窗后可能会产生的影响、效果、影响范围等。

标题与按钮操作区虽然作为可选项，但通常使用场景中，都需要给用户提供明确的可操作指示。

**布局和层次**

中心显示：弹出框作为窗口类容器，对用户操作的打断性较强，为了保障在多设备场景下的体验一致，通常居中显示在屏幕或窗口容器中，确保用户注意力集中。在一些特殊场景下，例如在较大屏幕中，为了减少用户操作路径过长，可通过跟手弹窗进行展示，弹出框的弹出位置需要与目标物本身的相对位置有关联性。

层次分明：在移动端设备中，通常使用全屏蒙层或窗口蒙层来解决弹出框与界面背景的层级差异，在电脑设备上，为了避免蒙层面积过大带来的视觉突兀感，通常使用阴影、边框等视觉效果区分弹出框与界面内容。

**尺寸和比例**

节制的自适应规格：弹出框的内容应根据设备屏幕的比例自适应，避免过大或过小。开发者通常需要注意弹出框内容的布局规格，通常是两端对齐、居中对齐或者是文本的换行对齐。

最大以及最小尺寸：设置合理的最大和最小尺寸，确保内容可读且不溢出。通常情况弹出框应该有一个固定的计算规则，同时应当定义其在较大屏幕或窗口中的最大比例，避免弹出框无节制的跟随变大。

**视觉一致性**

品牌风格：弹出框中的颜色、字体、按钮样式应与整体品牌风格一致。鼓励开发者与设计师进行有品牌调性的风格化设计，点缀性的使用品牌色对高亮文本、按钮进行填充，避免大面积的使用。

一致布局：保持应用内的弹出框在界面布局上的一致性，如标题、内容、按钮的排列方式。避免在同一应用内使用不同风格、布局、结构的弹出框类型，结构以及样式上的差异容易误导用户是否仍然在操作属于应用内的界面，减少体验上的割裂。

### 模糊材质

弹窗默认附带模糊材质效果，使用 COMPONENT\_ULTRA\_THICK，可参考 [backgroundBlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#blurstyle9) 接口枚举类型。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150817.88508905234000770082800759964942:50001231000000:2800:BC2E07600074A8581EB41A12723767F00D4B36C71D1402B3A0A4CA7B4857B708.png "点击放大")

## 设备差异

**电脑设备**

电脑设备的控件整体设计风格相较于移动端，使用更小的圆角。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150817.48628469592793908060176500215072:50001231000000:2800:E8B789EA8124E6D81911F1F9B90DC7743829F4C319F5B57615A77533D972B3CF.png "点击放大")

在 电脑设备中弹出框会自带阴影，分为获焦态与失焦态，用来区分当前操作的窗口层级。

<table id="ZH-CN_TOPIC_0000001957012569__X40de80cf53a56323c6c2a446e5dd0f072c59728" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row220mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p222mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150817.99051778715281303867538281084065:50001231000000:2800:E36DC8C61812658763434721CCE1AF12AEA9AF3F4468EEF6775203B8A24ACC14.png" title="点击放大" width="268.5" height="268.5"></span><strong>获焦弹出框</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p224mcpsimp"><span><img originheight="960" originwidth="960" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150818.19396551042338245652398498202607:50001231000000:2800:0ABEC6807A12B4B2EC003320AE922C5C7D349D9B23609432704D551A01157E4A.png" title="点击放大" width="268.5" height="268.5"></span><strong>失焦弹出框</strong></p></td></tr></tbody></table>

## 布局规则

弹出框的宽度默认通用计算方式为：屏幕/窗口宽度-两侧 Margin = 弹出框宽度。

当屏幕设备基于默认手机 360vp 宽度缩小或拉伸时，同样基于上述计算规则进行自适应，当最大宽度达到 400vp 时不再继续响应伸缩。

弹出框最大高度= 0.9\*(屏幕高度-信号栏-导航栏)，在电脑设备场景下高度按照子窗口的整体高度计算。

### 手机设备

<table id="ZH-CN_TOPIC_0000001957012569__X529f7e26812965fe547a96bd6bcec220df39b35" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row237mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p239mcpsimp"><strong>手机竖屏效果</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p681935515336"><span><img originheight="1776" originwidth="3084" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150818.62517624193371149780926701189635:50001231000000:2800:A880D2B35158C8235551694183A7659C314D85056EC9151E3570CAC4652E89C0.png" title="点击放大" width="268.5" height="154.6225680933852"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row243mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row246mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p248mcpsimp"><strong>手机横屏效果</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p251mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150818.17014455759738257231418537854268:50001231000000:2800:11DCE3A3AAEDC15462BDF6787EA1735138086F056E830D708B949519CBB72CF4.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

### 折叠设备

<table id="ZH-CN_TOPIC_0000001957012569__X4cf9ad10fb4122d4ae24340a6f042264d5755ec" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row256mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p258mcpsimp"><strong>折叠屏竖屏效果</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p19465532193412"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150818.05449350207830244746877813187729:50001231000000:2800:29B8F6C21E3253AE894109ADAC27F262FEB4AA62D2B2FD033722A36CB9505BBB.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row262mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row265mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p267mcpsimp"><strong>折叠屏横屏效果</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p11712184215341"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150818.17256414695520705361915928555244:50001231000000:2800:6984B47BB38E36C186706E3079D5A428EB81AD1B45E8BB94772AE40F60A85911.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr></tbody></table>

### 平板设备

<table id="ZH-CN_TOPIC_0000001957012569__X775c69f5448a60fc2c4adffa8ae40eaa88e083b" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row275mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p277mcpsimp"><strong>平板竖屏效果</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p280mcpsimp"><span><img originheight="2912" originwidth="5116" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150818.85299451474622189004238443784729:50001231000000:2800:8F184568766D90742052E3F96410FC131B6A2AF46CA79DA46FE9F1639C3641F1.png" title="点击放大" width="268.5" height="152.82877247849882"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row281mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row284mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p286mcpsimp"><strong>平板横屏效果</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957012569__p289mcpsimp"><span><img originheight="2160" originwidth="3840" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150818.15542049946991100957918658893202:50001231000000:2800:B87267E60DB00D5AD47ECF07C831BDC3DB0EBC9D02CE59E5996D1360653E05B4.png" title="点击放大" width="268.5" height="151.03125"></span></p></td></tr></tbody></table>

### 电脑设备

<table id="ZH-CN_TOPIC_0000001957012569__X87c9d1397b4d3b58025010fecf19cba00f44c7a" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row294mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p296mcpsimp">弹出框最大高度= 0.9*窗口内容层</p><p id="ZH-CN_TOPIC_0000001957012569__p297mcpsimp">应用弹出框位置在窗口内容层区域居中显示</p><p id="ZH-CN_TOPIC_0000001957012569__p298mcpsimp">桌面弹出框位置在桌面区域居中显示</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p3744338191814"><span><img originheight="2304" originwidth="3456" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150819.71298356010062707430243736995381:50001231000000:2800:1FF5C642B62E221C017C6F24601643C2FFD8BD3920CBCEDD6CE18536E52B7766.png" title="点击放大" width="268.5" height="179"></span></p></td></tr></tbody></table>

### 穿戴设备

<table id="ZH-CN_TOPIC_0000001957012569__table1174542915257" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957012569__row674542912511"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p187451729132510">智能穿戴的弹出框是一种全屏模态窗口，对用户在进行界面交互过程中干扰性比较强。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p177452293255"><span><img originheight="962" originwidth="1924" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150819.69184168295540885974165580758289:50001231000000:2800:594D83D7EEB295258947E2E3777FDB3DF349BE74AFC4AB461E4B4C13D3E75CAA.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957012569__row4745132952514"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p147453292250">弹出框支持三种布局样式，包括仅描述文本、标题+描述文本及图标+描述文本。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957012569__p1374542920255"><span><img originheight="962" originwidth="1924" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150819.29542715335012601510108572194086:50001231000000:2800:46FDD33DFBF6740549BBDCD38473A63C85F19C357FD2B56E24699E042D95FE23.png" title="点击放大" width="268.5" height="134.25"></span><span><img originheight="1924" originwidth="3848" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150819.32677232203902551265303986687369:50001231000000:2800:3C12CCD7A1DC57C21C98A131202BFF499B42243E70BA73555146826042046EA3.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr></tbody></table>

### 响应式布局

弹出框按照屏幕宽度断点规格进行不同屏幕大小设备上自适应适配。

**手机****设备**

全屏显示弹窗

默认计算方式为：屏幕宽度-两侧 Margin = 弹窗宽度

当屏幕设备基于默认手机 360vp 宽度缩小或拉伸时，同样基于上述计算规则进行自适应，当最大宽度达到 400vp 时不再继续响应伸缩

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150819.71483378957224838146047429344677:50001231000000:2800:F009F8ED62E35EA20B7DDCD7236F8E7CBC84103BA64B3E8389A84A643FC1DB99.png "点击放大")

分屏显示弹窗

当弹窗出现在分屏场景下时，弹窗默认以当前窗口总体宽度减去当前设备两侧 Margin 为显示宽度

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150820.99646213471132875364276615028108:50001231000000:2800:4154DBB46D0823B9EEBE4690E1D91F642235E2E5986D79ADBA71BCCCC3AD73EB.png "点击放大")

**电脑设备**

电脑弹出框宽度固定，不跟随父窗口变化而改变尺寸。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250820150820.85467496682129173878498255173967:50001231000000:2800:998699C43D4F9AE85955C2EC4972E3C82BE44EFA32A4938CE001FEEF6DBF8D45.png "点击放大")

## 开发文档

[CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)

[advanced.Dialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog)

[PromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction)
