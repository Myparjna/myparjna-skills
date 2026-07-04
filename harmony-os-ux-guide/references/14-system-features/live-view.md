# 实况窗

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-live-view-0000001955186861
- 抓取时间：2026-04-04T08:23:54.388Z
实况窗是一种帮助用户聚焦进行中任务、方便快速查看和即时处理的消息提醒。包含卡片态、胶囊态、沉浸态。

实况窗具有时效性、时段性、变化性、可视性（锁屏沉浸态）的特点。

**时效性**

实况窗的内容为正在进行或即时发生的进程，在特定时间段内，信息对用户有价值。例如，通话中、计时中等正在进行的用户活动，属于实况窗；权限调用、功能待机等系统状态，不属于实况窗；2 天后的机票，在购买后不立即提醒，而在出发前提示，具体提醒时间根据业务实际情况确定。

**时段性**

该事件或服务需要持续一段时间，有明确的开始和结束，而非单点的提醒或信息。例如，打车、外卖等从事件开始到结束需要经历一段时间，属于实况窗；天气提示、电影票等单点提醒，则不属于实况窗。

**变化性**

实况窗展示内容应当保持动态更新，确保用户获取实时状态信息。例如，航班登机口变更、打车时司机取消订单等突发情况，都需要在实况窗中及时告知用户。

**可视性（锁屏沉浸态）**

锁屏沉浸态支持在锁屏以可视化形式表现更多数据情况，并进行动态刷新，帮助用户在锁屏聚焦进行中的任务。例如打车时车辆当前的位置情况、点外卖时外卖员的派送情况、播放歌曲时专辑封面更新等，便于用户快速获取关键信息并执行关键操作。

## 提醒方式

实况窗能够在锁屏、通知中心等位置显示卡片。除此之外，还支持：

1.  在状态栏显示胶囊状态，以及在状态栏点击胶囊后展开悬浮卡片；
2.  在锁屏显示胶囊状态和卡片态，以及长按或点击卡片头图进入锁屏沉浸态。

多种显示方式能够将信息即时触达到用户，避免用户反复进出应用或服务的页面。在不同的显示位置中，通知中心顶部会显示全量实况窗，其他显示位置则根据用户的设置及业务的重要程度进行呈现。

1.  同一个事件活动在不同场景下仅出现一个形态，如当前事件所承载的落地页在前台，则当前无胶囊；如当前为通知中心/锁屏，则不显示状态栏胶囊。
2.  通知中心的实况卡片会默认显示在顶部，需避免滥用对用户造成打扰。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153428.54877920396127334502904591744394:50001231000000:2800:69B33CCE6CB62850EB20F05FB2CD19E722E03F042E4A5590E10A2263BD69A1D8.png "点击放大")

## 适用场景

1.  用户在特定时段内非常关注该活动，且需要即时查看或快捷操作。
2.  该活动有明确的开始和结束时间，且总时长较短。
3.  用户对于接收到该活动的实况信息有明确的预期，通常为用户主动行为触发。
4.  需要确保展示内容对用户有足够的价值。

## 设计原则

**内容设计**

-   展示价值信息：提供当前事件的重要信息，在胶囊显示最精简的重要内容，在卡片上显示用户关注的关键内容。
-   避免重复发送：展示实况窗后，避免对同一事件发送内容重复的普通通知。
-   隐私信息脱敏：避免在实况窗上展示涉及用户隐私的信息，如必须展示，建议进行脱敏处理。
-   避免广告营销：避免将实况窗用于营销、广告等场景。

**交互设计**

-   自动清理信息：为每个实况窗活动设定明确的结束事件，并在用户进程结束后一个合理的时间内自动清理消息。
-   提供快捷操作：必要时，为用户提供快捷操作按钮，满足便捷操作的诉求。

**视觉设计**

-   兼容深浅模式：图片、强调色需要考虑其深色模式和浅色模式下的显示效果，确保两个模式下用户能清晰看到关键信息。
-   统一强调色值：在各个显示界面中采用相同的强调色，推荐使用应用的品牌色，若出现品牌色不适合文本阅读的场景可提供相近的色值，确保用户能够快速抓取应用特征记忆。

## 基础交互

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.46673195753210251771535975293550:50001231000000:2800:4C23827F2AFF70A3EE296739859B1370B3F78C354E2519958BA10A2D29F1AB2E.png "点击放大")

点击单个胶囊，呼出悬浮卡片，胶囊消失；点击卡片空白处，进入对应详情页。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.99418864274476366008422453109336:50001231000000:2800:34F3A22708742E88DE5B8A6DDB71428F9E780F2892571505C6E35F7C8B490B38.png "点击放大")

进入沉浸态：锁屏后默认进入；点击锁屏卡片态头图；点击锁屏胶囊态。

退出沉浸态：侧边back手势退出，返回至展开前状态；下拉收起至胶囊态；上滑进入锁屏卡片态。

## 通用卡片模板

为了帮助用户聚焦进行中任务、方便快速查看和即时处理，实况窗提供了更丰富的卡片模板，可以显示更可视化的进程信息以及简要操作。

-   卡片内需满足绝大部分用户使用需要，提供详细进程信息及高频操作。
-   卡片用于悬浮状态、锁屏、通知中心的显示。

### 模板结构

卡片支持固定区、辅助区、扩展区三个板块，其中固定区为必选，辅助区和扩展区为可选。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.40259316852267517488680083080441:50001231000000:2800:D0858E1805BE9DDDB357A9F9141E0F4B583048C0F2172BA25517C7E1C011D0A9.png "点击放大")

<table id="ZH-CN_TOPIC_0000001955186861__X308bc046567a59c0f5e3141167112ebcad95ca6" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001955186861__row169mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="61.79%"><p id="ZH-CN_TOPIC_0000001955186861__p32833191659"><strong>固定区</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol7817152915125"><li id="ZH-CN_TOPIC_0000001955186861__li181742991212">左侧应用图标：表示实况窗来源，系统将直接展示应用桌面图标</li><li id="ZH-CN_TOPIC_0000001955186861__li947673218123">主文本：简要概述当前进展</li><li id="ZH-CN_TOPIC_0000001955186861__li183964317123">副文本：描述当前进展的详情或信息补充</li><li id="ZH-CN_TOPIC_0000001955186861__li08170375121">主副文本超长会截断显示，不支持跑马灯，合理控制字数</li></ol></td><td class="cell-norowborder" style="border: none;" valign="top" width="38.21%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p177mcpsimp"><span><img originheight="833" originwidth="1583" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.22458272107899037904386685103946:50001231000000:2800:C0222F57689D9BE5BF6BADDE3F20957A609F838383D9C538BE4A7924513135C7.png" title="点击放大" width="193.39770000000001" height="101.76897289955781"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001955186861__row178mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="61.79%"><p class="start(2)" id="ZH-CN_TOPIC_0000001955186861__p835316551964"><strong>辅助区</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol54111271888"><li id="ZH-CN_TOPIC_0000001955186861__li17417271288">辅助区区域：44*44vp，支持展示：图片、胶囊带文字、icon &amp; logo、纯文本</li><li id="ZH-CN_TOPIC_0000001955186861__li25941434487">支持应用在规定区域内，上传自定义元素大小、对齐方式的资源；不推荐截断显示</li><li id="ZH-CN_TOPIC_0000001955186861__li0155541884">文本大小推荐：8-12vp (默认 10vp)</li><li id="ZH-CN_TOPIC_0000001955186861__li1716816276918">拓展按钮位: 44vp*70vp(宽度)；要求按钮在区域内右对齐；<p id="ZH-CN_TOPIC_0000001955186861__p1312674920131">系统默认: 10vp字体(可选择8-12vp)，胶囊高度22vp &amp; 纯色背景</p></li><li id="ZH-CN_TOPIC_0000001955186861__li7718162171414">若选择辅助区，则会挤占固定区宽度，可根据需求自选。请注意确保深浅模式效果。</li></ol></td><td class="cell-norowborder" style="border: none;" valign="top" width="38.21%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p190mcpsimp"><span><img originheight="1268" originwidth="2100" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.50014510125207058410565414993358:50001231000000:2800:4C7F1FFABDB9C836D544E1F52DB813C75E5D6980CC76F870BAF9750AF9683E1D.png" title="点击放大" width="193.39770000000001" height="116.77537314285715"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001955186861__row191mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="61.79%"><p class="start(3)" id="ZH-CN_TOPIC_0000001955186861__p85427348143"><strong>扩展区</strong></p><p id="ZH-CN_TOPIC_0000001955186861__p194mcpsimp">支持进度可视化、强调文本、左右文本、赛事比分样式，具体根据业务类型和诉求进行详细设计。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="38.21%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p196mcpsimp"><span><img originheight="832" originwidth="1561" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.18861655721952293089100134511975:50001231000000:2800:293245B5D6CF1B59E82A99AEFAF2BFFE1458F14851B65E60F2A2DD36B65E69D9.png" title="点击放大" width="193.39770000000001" height="103.07936348494556"></span></p></td></tr></tbody></table>

### 模板类型

卡片模板类型目前包括基础模板、进度可视化模板、强调文本模板、左右文本模板、赛事比分模板、导航等。

\*以下“应用色”均指代应用侧上传、可代表该应用品牌辨识度的色值。

<table id="ZH-CN_TOPIC_0000001955186861__X9aed93bb2791e80e374212fa39f376aae020e9e" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001955186861__row108171830181912"><td class="nocellnorowborder" style="border: none;" valign="top" width="52.98350298350299%"><p id="ZH-CN_TOPIC_0000001955186861__p2017917419202"><strong>基础模板</strong></p><p id="ZH-CN_TOPIC_0000001955186861__p2179174202015"><strong>适用于不需要扩展区的内容较少、简易操作场景</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol151796422020"><li id="ZH-CN_TOPIC_0000001955186861__li191791546207">当不填充扩展区内容时，仅显示1*4的卡片大小。图标、文本、辅助区规则与2*4一致。</li><li id="ZH-CN_TOPIC_0000001955186861__li171792472018">使用1*4时，请注意在辅助区提供必要的功能操作和引导。</li></ol></td><td class="nocellnorowborder" style="border: none;" valign="top" width="32.678132678132684%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p381233010199"><span><img originheight="1424" originwidth="2360" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.18555269979982475355756239788211:50001231000000:2800:B8BD50FA1748E102980BD99999596DD946CFDD61E597A1FF39474E0E9F5106FB.png" title="点击放大" width="158.1597051597052" height="95.43195768958483"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="14.338364338364338%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001955186861__row1681783014197"><td class="row-nocellborder" style="border: none;" valign="top" width="52.98350298350299%"><p id="ZH-CN_TOPIC_0000001955186861__p1439115811713"><strong>进度可视化模板</strong></p><p id="ZH-CN_TOPIC_0000001955186861__p216mcpsimp"><strong>适用于打车、外卖等需要呈现完整进程及当前节点的场景</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol14845122941811"><li id="ZH-CN_TOPIC_0000001955186861__li148451129191814">图标：支持表示来源的应用/服务图标</li><li id="ZH-CN_TOPIC_0000001955186861__li143218330234">文本：支持双行主副文本，显示当前节点阶段和详细信息，其中副文本可选关键词采用强调色，支持一种强调色，且需要与胶囊底色等其他自定义颜色一致；</li><li id="ZH-CN_TOPIC_0000001955186861__li17518113802310">辅助区：支持添加辅助信息，如商品/商家图片等，挤占文本区域</li><li id="ZH-CN_TOPIC_0000001955186861__li18537450202317">扩展区：支持进度和节点的可视化显示，节点数支持 2-5 个，进度条支持 3 个样式可选，并组合不同的图片展示样式。进度条可定义高亮色，建议与文本强调色、胶囊底色等保持一致。</li></ol></td><td class="row-nocellborder" style="border: none;" valign="top" width="32.678132678132684%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p13812830171912"><span><img originheight="768" originwidth="1496" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153429.83544687809449887051269907021546:50001231000000:2800:F9F48A796C9CFF80C342AFFE707EB53CD34F22BC1B2300007F56306DB147D685.png" title="点击放大" width="158.1597051597052" height="81.19428714081123"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="14.338364338364338%">&nbsp;&nbsp;</td></tr></tbody></table>

**进度样式说明**

1\. 应用可自定义活动进程节点个数 (最多 5 个)、节点 icon 和进度条搭配样式，进度条指示器 (pic 区域) 可在限定区域内展示派送员、车、派送物品等直观视觉样式。

2\. 考虑卡片底板具有一定透明度及模糊材质，卡片内容会受到底部页面影响。应用设计时推荐使用圆形底板以增加对比度，节点底板颜色建议自定义高亮色。如未上传高亮色，已完成进度默认系统高亮蓝色 #317AF7，未完成进度显示系统黑白样式 (10% 黑/白)。若不需要圆形底板，也可选择设计有足够显色度、识别度的图标，展示在规定的图标区域内。已完成进度条和已完成进度节点背景色一致，未完成进度条和未完成进度节点背景色一致。

-   请注意使用系统圆形底板需上传 svg 格式图标；若自定义底板，需上传 png 格式。不推荐无底板的样式，会造成进度条连接处显示异常。

3\. 使用样式二时，支持在固定区域内展示骑手等插画图形短暂覆盖进度条节点位置，但不可直接显示进度条头尾无节点。

-   pic 可等比缩放，pic 区仅有最大高度限制，宽度根据需求自定义。不推荐扁而长的插画资源，会导致进度移动缓慢、比例失衡等问题。

样式一：采用圆点进度，已完成的进度条及节点底板推荐使用应用色

样式二：采用条状进度，已完成的进度条推荐使用应用色

样式三：采用较粗条状进度，已完成的进度条推荐使用应用色，也可搭配无 pic 场景突出进度条样式

图片类型：

1、气泡遮罩类：系统提供固定大小气泡，应用可替换裁切的为居中正圆区域，实际大小32\*32vp。

2、自定义覆盖类：系统限制长宽区域，最大高度56vp，应用根据设计所需诉求提供对应资源。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.72625546695859418068329507146015:50001231000000:2800:E53995545F46B19B9225708132B3DFA8B9447B6963A081B68AD71786CF3CC6E6.png "点击放大")

<table id="ZH-CN_TOPIC_0000001955186861__table125786375334" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001955186861__row1957819372337"><td class="nocellnorowborder" style="border: none;" valign="top" width="42.93611793611793%"><p id="ZH-CN_TOPIC_0000001955186861__p122761150103318"><strong>强调文本模板</strong></p><p id="ZH-CN_TOPIC_0000001955186861__p3276195003319"><strong>适用于取餐、排队等需要强调部分文本信息的场景</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol102763502336"><li id="ZH-CN_TOPIC_0000001955186861__li17276250133317">图标：支持表示来源的应用/服务图标</li><li id="ZH-CN_TOPIC_0000001955186861__li1327685063319">文本：支持双行主副文本，显示当前节点阶段和详细信息，其中副文本可选关键词采用强调色，支持一种强调色，且需要与胶囊底色等其他自定义颜色一致</li><li id="ZH-CN_TOPIC_0000001955186861__li8276105043312">辅助区：支持添加辅助信息，如商家图片等，挤占文本区域</li><li id="ZH-CN_TOPIC_0000001955186861__li8276175018339">扩展区：支持强调文本 (例：72988；请注意此处文本较大，为保证协调性更推荐英文字母和数字) 和标记辅助文本 (例：取餐码)；强调文本下划线可自定义颜色以及是否显示，右侧支持显示相关详情图；强调文本区和图片区共用卡片宽度<p id="ZH-CN_TOPIC_0000001955186861__p19276105019337">a. 下划线的颜色：建议使用应用色，若出现应用色不易浏览的场景可提供相近的色值，确保用户能够快速抓取应用特征记忆。下划线长度略长于文本</p><p id="ZH-CN_TOPIC_0000001955186861__p17276175016334">b. pic 区域内：可提供通知相关的图片或矢量插画等，应用可选择在区域内展示位置 (如居中或居右等)</p></li></ol></td><td class="nocellnorowborder" style="border: none;" valign="top" width="50.92137592137592%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p657883711335"><span><img originheight="760" originwidth="1496" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.62915734673187685840435186974875:50001231000000:2800:F32FF06BD98324F9853D960A4E26D807CB0909D4355761AE5A8389B7228B22D1.png" title="点击放大" width="274.3691646191646" height="139.38540448567187"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="6.142506142506142%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001955186861__row1457813379330"><td class="nocellnorowborder" style="border: none;" valign="top" width="42.93611793611793%"><p id="ZH-CN_TOPIC_0000001955186861__p16427153463416"><strong>左右文本模板</strong></p><p id="ZH-CN_TOPIC_0000001955186861__p265mcpsimp"><strong>适用于高铁、航班等左右信息对称的场景</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol1552110391342"><li id="ZH-CN_TOPIC_0000001955186861__li15521539163413">图标：支持表示来源的应用/服务图标</li><li id="ZH-CN_TOPIC_0000001955186861__li1579745103414">文本：支持双行主副文本，显示当前节点阶段&amp;对应节点的重要信息，其中副文本可选关键词采用强调色，支持一种强调色，且需要与胶囊底色等其他自定义颜色一致</li><li id="ZH-CN_TOPIC_0000001955186861__li12656134983413">辅助区：支持添加辅助信息，如高铁/航班号，选择后会挤占文本区宽度</li><li id="ZH-CN_TOPIC_0000001955186861__li936251103514">扩展区：支持行程出发地/出发时间，目的地/到达时间；可根据业务类型替换居中图形样式 (如飞机、高铁等)。<p id="ZH-CN_TOPIC_0000001955186861__p9267125163517">a. 传递矢量图类型，会默认显示 18*18vp 的大小，左右会分别显示 3 个小圆点。</p><p id="ZH-CN_TOPIC_0000001955186861__p16510973358">b. 传递非矢量图类型，则直接按应用传递的图片大小进行居中显示，最高不超过 32vp，否则按最大高度对图片进行等比缩放。</p><p id="ZH-CN_TOPIC_0000001955186861__p113149220353">c. 请注意图形区域有最大高度限制，且需验证在深浅模式的卡片上的易读性，不推荐与卡片颜色相近的较白或黑灰。</p><p id="ZH-CN_TOPIC_0000001955186861__p151431543163313"></p><p id="ZH-CN_TOPIC_0000001955186861__p335011674019">*拓展区支持强调型和均衡型两种样式，区别在于文本使用组合的大小不同，强调型主体字号更大能够突出内容，均衡型字号相对小一些能够展示相对更多文本。</p><p id="ZH-CN_TOPIC_0000001955186861__p57911044203315">可通过<a href="https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-liveviewmanager#section1181383342218" target="_blank">左右文本样式类型</a>字段设置子样式类型，默认为强调型子样式。</p></li></ol></td><td class="nocellnorowborder" style="border: none;" valign="top" width="50.92137592137592%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p1657893720332"><span><img originheight="768" originwidth="1496" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.45856108843251485540277288260328:50001231000000:2800:751E40D393106ED03A8A2116D74FD65C908BA9CC7F407D5B6B83D3BABF63C7F0.png" title="点击放大" width="274.3691646191646" height="140.85261926973158"></span></p><p id="ZH-CN_TOPIC_0000001955186861__p7970296329">强调型</p><p id="ZH-CN_TOPIC_0000001955186861__p144381955183212"></p><p id="ZH-CN_TOPIC_0000001955186861__p112118713332"><span><img originheight="768" originwidth="1496" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.32949549317148670667446055876602:50001231000000:2800:29298982B69C6CF5ECC2B569DA2E8F4633D06880153923074BF1E0961E3564A9.png" title="点击放大" width="274.3691646191646" height="140.85261926973158"></span></p><p id="ZH-CN_TOPIC_0000001955186861__p14959181693210">均衡型</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="6.142506142506142%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001955186861__row68953497351"><td class="nocellnorowborder" style="border: none;" valign="top" width="42.93611793611793%"><p id="ZH-CN_TOPIC_0000001955186861__p593017910371"><strong>赛事比分模板</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol42351714103714"><li id="ZH-CN_TOPIC_0000001955186861__li14235101416374">图标：支持表示来源的应用/服务图标</li><li id="ZH-CN_TOPIC_0000001955186861__li366215518218">文本：支持双行主副文本，显示比赛的当前节点&amp;详细信息</li><li id="ZH-CN_TOPIC_0000001955186861__li1176181743719">扩展区：支持队名/队徽图片，比分显示，中间可选择显示当前比赛辅助信息或“VS”<p id="ZH-CN_TOPIC_0000001955186861__p7301142843720">a.pic 队徽：推荐使用无底板 png 图片</p><p id="ZH-CN_TOPIC_0000001955186861__p943133011375">b.中间元素 (小节、时间、赛名等) 由赛事自定义</p><p id="ZH-CN_TOPIC_0000001955186861__p1496832583713">c.队伍名称可采用简写等方式，长度不可超出限制区域，超过后会直接截断</p></li></ol></td><td class="nocellnorowborder" style="border: none;" valign="top" width="50.92137592137592%"><p id="ZH-CN_TOPIC_0000001955186861__p289614915353"><span><img originheight="760" originwidth="1496" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.60671748800116528631675832757516:50001231000000:2800:E6ED3662F7FB6BA3B157DDE2795285481736D3719356DDBC01530EABBD7234EC.png" title="点击放大" width="274.3691646191646" height="139.38540448567187"></span></p><p id="ZH-CN_TOPIC_0000001955186861__p2061510388304"></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="6.142506142506142%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001955186861__row421013183613"><td class="row-nocellborder" style="border: none;" valign="top" width="42.93611793611793%"><p id="ZH-CN_TOPIC_0000001955186861__p410710431374"><strong>导航定制模板</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol36251349153718"><li id="ZH-CN_TOPIC_0000001955186861__li116251449113710">左侧大图：显示当前导航主要引导方向。</li><li id="ZH-CN_TOPIC_0000001955186861__li1691219516375">右侧辅助区56*36vp：默认展示该应用的logo图标，位置如右图(默认)；也可选择传入其他资源，默认居中右对齐，或通过透明边框等形式控制资源效果(ex.1-2)</li><li id="ZH-CN_TOPIC_0000001955186861__li203121554173710">扩展区：支持1-11个车道信息，间距将根据车道个数均等分。请注意提供的资源区分主次车道颜色，便于用户理解。</li><li id="ZH-CN_TOPIC_0000001955186861__li2019334032815">为确保系统深浅模式显示效果，系统将对资源做赋色能力。1）提供车道信息资源时尽量使用png、svg格式，若上传jpg等其他格式则保留原样显示不支持赋色。2）资源输出时: 主要路径与次要路径的需使用同色不同透明度，不支持双色，否则易造成图标资源信息丢失等问题。</li></ol></td><td class="row-nocellborder" style="border: none;" valign="top" width="50.92137592137592%"><p id="ZH-CN_TOPIC_0000001955186861__p1521013143610"><span><img originheight="1092" originwidth="2304" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.90884078150684581201449719383811:50001231000000:2800:4767B8AD1C669FA3B9E6BD9941CAD9523C14106517BD0C257E4429024C5F2133.png" title="点击放大" width="274.3691646191646" height="130.03955198095824"></span></p><p id="ZH-CN_TOPIC_0000001955186861__p1515012819233"><span><img originheight="1092" originwidth="1544" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.41634314212490224891258911469613:50001231000000:2800:12940DB26CFF17DBD3932BCE4C33F46B56135129DDEA051E8B3968CA9C174215.png" title="点击放大" width="274.3691646191646" height="194.0486578783211"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="6.142506142506142%">&nbsp;&nbsp;</td></tr></tbody></table>

### 通用卡片模板使用说明

业务可以基于任务的不同节点，在上述模板中选择最适合展示的样式。

示例：打车场景，业务可使用强调文本类模板展示车牌号信息，待乘客上车后再以进度可视化模板展示距离终点的进度变化；

同样地，业务也可以全程使用进度可视化模板来展示。

示例一：对于不同时段的信息获取侧重不同，则可使用不同模板

司机接驾时突出：车辆颜色、车牌

行程开始后突出：距离目的地路程、时间

示例二：将信息整合，在同一卡片内刷新替换

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.00723877100148202980653614289980:50001231000000:2800:1EDE8BC5603573AC6AE90C0E662D38E4F499EEEA270F1C0BE1DCDE81C722A403.png "点击放大")

## 通用胶囊模板

实况窗将在挖孔居中的设备上进行软硬结合的显示。与状态栏固定元素（时间、信号、电池等）共存，产生联动与挤压。

胶囊内需显示最精简、最重要的内容，保证用户一瞥即得。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.07882686322623846598307317293202:50001231000000:2800:74569CCCB50C092EFB2625425512CFF44AC4D827EB0EAB042FD3F90901CA923E.png "点击放大")

**胶囊场景类型**

胶囊与居中挖孔的设备软硬结合居中展示，在侧边挖孔或无孔场景下则居左展示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153430.34664635787131821718467848568860:50001231000000:2800:3639B155A33A48BA47994042BC0EA10B15C956267C269320B04DA715A8075694.png "点击放大")

**通用胶囊****组成元素**

1、胶囊：由系统提供默认黑色微渐变 / 纯黑透明度样式（#000000），根据场景自适应

2、图标：用于表示业务来源，需传入业务定制图标或应用logo，提升胶囊的易读性和辨识度

3、文本：支持传入1-2段文本内容，尽量精简避免冗余和超长跑马灯；颜色为#FFFFFF，不支持定制

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153431.63904733992762197425377309491655:50001231000000:2800:951994706D9C01BD9E66B234A526B0F0D9B5FFE94D3623BECE0AE6F3237559ED.png "点击放大")

4、辅助图标区：提供右侧圆形槽位（系统裁切），支持例如红绿灯倒计时等其他可视化次要信息。

\* 需注意挤占关系：副文本会被右侧槽位挤压，可用空间不足时文本则渐隐展示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153431.82600950117102592210657062774162:50001231000000:2800:382EBBD0348C033A0BA17B49964523C70EC3386C79EB8EC04C7727E7C0B7F7B2.png "点击放大")

**图标规则**

1、为确保胶囊一致性及美观性，系统将裁切图标形成同心圆效果，具体资源要求及裁切效果如下：

矢量图标资源：需预留裁切安全边距，避免出现关键图形被裁切；

应用图标：不预留额外边距，保证完整填充，避免裁切出成多边形

2、默认将传入的品牌色生成圆形底板置于图标下方，如有其他色彩展示诉求，需导出在图标资源中

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153431.42771289769547545519030177715300:50001231000000:2800:FDD1E336E9427F5F045179D586648B08E893A52753CA559AC7F14795EA24E0B7.png "点击放大")

**文本布局规则**

单文本时，图标单独显示在左侧，文本单独显示在右侧；双文本时，图标和主文本显示在左侧，副文本显示在右侧。

为确保胶囊整体美观性、信息效率等综合体验：

1、建议接入双文本

2、建议将单段超长文本拆解为双文本

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153431.02545071003142714442862801567212:50001231000000:2800:AF2D2F6647F87BB21CCAC2B196018298B85BA7AD9EDC5D0D81E1B5882A3A110B.png "点击放大")

**文本长度规则**

考虑到多设备场景适配（包含单孔、多孔屏上的显示）

1、推荐 主文本：1-3个中文字符；副文本：1-6个中文字符

2、如传入超长文本，在不同设备可用空间上，用渐隐效果展示，支持跑马灯

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153431.15804282071590802719570323520854:50001231000000:2800:AA4795F97DF29DD53531CDE4F64ECB96561C3398CD2148832411FCFDBD9222D6.png "点击放大")

**跑马灯规则**

1、为避免两端文本同时跑马造成使用困扰，仅支持胶囊右侧文本跑马灯

2、双文本时若主文本过长，有概率无机会完整显示；副文本超长则支持跑马灯两遍

综上所述：推荐主文本精简 + 副文本较长的字符组合方式，注意避免文本超长

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153432.68278810859988819787785846797122:50001231000000:2800:E183C6D4340573AEC1EBAC34985159DFD7F96D013A8C7A80C692187B5FBB8DDC.png "点击放大")

## 锁屏模板

为了帮助用户聚焦进行中任务、方便快速查看和即时处理，实况窗提供了更丰富的卡片模板，可以显示更可视化的进程信息以及简要操作。

### 锁屏胶囊态

锁屏胶囊态需显示最重要的内容和操作，用户可快速获取信息和操作关键任务。

显示固定区和辅助区内容，与实况窗卡片态的固定区和辅助区内容保持一致。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153432.51421580300705873338426709271003:50001231000000:2800:B67D3CA8D2E6E90FA5E6E6767E84D9E09A41B715D78E67CEF86B5DD842DBB211.jpg "点击放大")

<table id="ZH-CN_TOPIC_0000001955186861__table11706131974813" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001955186861__row1170631934817"><td class="nocellnorowborder" style="border: none;" valign="top" width="61.67%"><p id="ZH-CN_TOPIC_0000001955186861__p16591203616486"><strong>固定区</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol698284012484"><li id="ZH-CN_TOPIC_0000001955186861__li2982940144817">左侧应用图标：表示实况窗来源或业务定制图标，如为来源，系统将直接展示应用桌面图标；如为定制图标（例如导航箭头），需上传 36*36vp，避免被圆形遮罩裁切</li><li id="ZH-CN_TOPIC_0000001955186861__li561924314810">主文本：简要概述当前进展</li><li id="ZH-CN_TOPIC_0000001955186861__li7529154812489">副文本：描述当前进展的详情或信息补充</li><li id="ZH-CN_TOPIC_0000001955186861__li1122017518485">主副文本超长渐隐截断显示，支持跑马灯</li></ol></td><td class="cell-norowborder" style="border: none;" valign="top" width="38.33%"><p class="msonormal" id="ZH-CN_TOPIC_0000001955186861__p1870718192489"><span><img originheight="484" originwidth="1120" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153432.38881670312356208901237582007472:50001231000000:2800:A70BAF9EB83A05346B0D0C8D4EDEEF330AFD43B707DAD8D49B691B26D7E27C05.jpg" title="点击放大" width="194.16209999999998" height="83.90576464285714"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001955186861__row164103110493"><td class="row-nocellborder" style="border: none;" valign="top" width="61.67%"><p id="ZH-CN_TOPIC_0000001955186861__p1660431115014"><strong>辅助区</strong></p><ol id="ZH-CN_TOPIC_0000001955186861__ol1297415735011"><li id="ZH-CN_TOPIC_0000001955186861__li8765110155019">辅助区区域：36*36vp<p id="ZH-CN_TOPIC_0000001955186861__p9349411115017"><a name="ZH-CN_TOPIC_0000001955186861__li8765110155019"></a><a name="li8765110155019"></a>支持展示：图片、胶囊带文字、icon &amp; logo、纯文本</p></li><li id="ZH-CN_TOPIC_0000001955186861__li27019161504">支持应用在规定区域内，上传自定义元素大小、对齐方式的资源；不推荐显示截断</li><li id="ZH-CN_TOPIC_0000001955186861__li18141022205011">文本大小推荐：8-12vp (默认 10vp)</li><li id="ZH-CN_TOPIC_0000001955186861__li588192518506">若选择辅助区，则会挤占固定区宽度，可根据需求自选</li><li id="ZH-CN_TOPIC_0000001955186861__li821723275010">拓展按钮位: 36vp～70vp（宽度）；要求按钮在区域内右对齐<p id="ZH-CN_TOPIC_0000001955186861__p1033783435019"><a name="ZH-CN_TOPIC_0000001955186861__li821723275010"></a><a name="li821723275010"></a>a. 系统默认: 10vp字体（可选择8-12vp），胶囊高度22vp &amp; 纯色背景；</p><p id="ZH-CN_TOPIC_0000001955186861__p2084593235011">b. 也可自定义背景颜色和透明度，请确保深浅壁纸模式效果</p></li></ol></td><td class="cellrowborder" style="border: none;" valign="top" width="38.33%"><p id="ZH-CN_TOPIC_0000001955186861__p764173174910"><span><img originheight="1384" originwidth="2092" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153432.47620531339565267334868753903888:50001231000000:2800:DE75B8A014AEC1BEC80C0FCF10D18D2ADF5DD8FDBDE21D7A2203D08A72AA22D4.jpg" title="点击放大" width="194.16209999999998" height="128.4514084130019"></span></p></td></tr></tbody></table>

### 锁屏沉浸态

为了帮助用户在锁屏快速查看任务情况和快速操作，实况窗在锁屏状态以可视化形式呈现更多的数据情况以及提供更多快速操作。

锁屏沉浸大卡片支持可视化区、固定区、辅助区、扩展区四个板块，其中固定区、辅助区和扩展区与实况窗卡片数据情况保持一致，可视化区为锁屏沉浸大卡片必选板块。

**可视化区**

支持在锁屏实时更新进程。若不展示扩展区，可视化区域比例增大。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153432.66269281529069029814677750414752:50001231000000:2800:D6158FE0DF1D6E070E20ED2BFB3DD1567C9A9FB04CA4E29017A8ED2AC38E70B7.jpg "点击放大")

目前支持接入地图和静态图。地图类可视化区域支持地图拖动、缩放等交互操作，适用于导航、打车、外卖等场景；静态图类支持图片展示和刷新，适用于音乐、赛事等场景。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153432.87333483654596791254904685805578:50001231000000:2800:AD8EA9C94419CCAF821F6C32D8C447D9449E8F331F4338F552F7AD432E804C96.png "点击放大")

## 文本超长显示规则

根据卡片、胶囊的可用宽度及推荐文本长度，进行文本内容设计。

1.  建议完整显示字串，合理控制字数。
2.  不支持跑马灯，不支持换行，超过 1 行“…”截断。
3.  如有辅助区，则固定区文本可显示区域被挤占，显示文字变少。

### 卡片固定区

无辅助区：主文本最多显示 23 个英文字符，或 16 个中文字。副文本最多显示 28 个英文字符，或 19 个中文字。

有辅助区：主文本最多显示 18 个英文字符，或 13 个中文字。副文本最多显示 22 个英文字符，或 15 个中文字。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153433.89248922552274087451071456210066:50001231000000:2800:E17E3672A6D13F7F46113B868537131881423291DB74E3A32E8E9543FD9A9181.png "点击放大")

### 卡片扩展区

强调文本模板：辅助文本最多显示 20 个英文字符，或 13 个中文字。强调文本最多显示 7 个英文字符，或 9 个数字。

左右文本模板：主文本显示时间 HH:MM。辅助文本最多显示 8 个英文字符，或 5 个中文字。

赛事比分模板：辅助文本最多显示 8 个英文字符，或 5 个中文字。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153433.28748296538673456327900010219217:50001231000000:2800:7CB5A9A164D81F9E8ECDC3FF823FC1DB8E58943AE92FD0E4420DD191D5BE2FF7.png "点击放大")

### 锁屏模板

**锁屏胶囊态**

无辅助区：主文本最多显示15个英文字符，或10个中文字，辅助文本最多显示18个英文字符，或12个中文字；支持跑马灯，超过后渐隐截断。

有辅助区：主文本最多显示11个英文字符，或8个中文字，辅助文本最多显示14个英文字符，或9个中文字；支持跑马灯，超过后渐隐截断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153433.66517217056649693480689044757344:50001231000000:2800:D5BF655C5DA564117326AC4B849138C61D5DD3584521500D759B541E38DA0AAA.png "点击放大")

**锁屏沉浸态**

1）卡片固定区

无辅助区：主文本最多显示 19 个英文字符，或 14个中文字。副文本最多显示 26个英文字符，或 17个中文字。

有辅助区：主文本最多显示 15 个英文字符，或 11 个中文字。副文本最多显示 21 个英文字符，或 14 个中文字。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153433.52328713066286072732002491188615:50001231000000:2800:AE93F3EC9E8CFB303677F2B8C4BA1E4D9466C0C586FF321BFB734E903AA8C4B5.jpg "点击放大")

2）卡片扩展区

强调文本模板：辅助文本最多显示 20 个英文字符，或 13 个中文字。强调文本最多显示 7 个英文字符，或 9 个数字。

左右文本模板：主文本显示时间 HH:MM。辅助文本最多显示 8 个英文字符，或 5 个中文字。

赛事比分模板：辅助文本最多显示 8 个英文字符，或 5 个中文字。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153433.68467772247710700006991839600837:50001231000000:2800:B75357CDA77D9084CF661DD3DB3164B7F37A1691F73F966387CDBBAFE7CA4260.png "点击放大")

## 设计模版和资源

应用可以基于实况窗通知样式模版自行更改符合应用自身场景的相关内容。

[HarmonyOS+实况通知样式模板.zip](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251229153433.31315489748446269967504159871423:50001231000000:2800:B98719E298C84871CA7173004D8F15979187C9261DA4A7ACF7F9D678CDF58115.zip?needInitFileName=true)（.sketch）
