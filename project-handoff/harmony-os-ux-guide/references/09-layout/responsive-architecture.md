# 响应式应用架构

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/design-responsive-layout-structure-0000001748539684
- 抓取时间：2026-04-04T08:22:29.667Z
响应式布局方法也用于应用导航，当应用窗口发生变化时，应用导航方式也会随着窗口达到对应断点值而发生变化，通过导航方式的调整提高交互的易用性。

## 侧边Tab

当窗口宽度达到对应的断点值，底部 Tab 可以结合挪移布局的方法，把 Tab 组件挪移到左侧。在大尺寸设备上提高交互易用性。

适用于导航结构简单的内容型应用，例如音乐、视频等。

窗口宽度 ≥ 840vp，建议使用侧边 Tab，侧边 Tab 的导航选项继承底部 Tab 。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214027.43232854655177609843019506566548:50001231000000:2800:6A2DD0FF797C06ECD6E0EBB98834CBB1C5C2BD3DC0526F53C82DB212FDA3FE8F.png "点击放大")

## 分栏

当窗口宽度达到对应的断点值，原来父子关系的层级页面可拆分后平行显示，在大尺寸设备上充分发挥屏幕的显示优势，例如设置、短信等。

窗口宽度 ≥ 600vp，建议使用分栏布局。默认两栏宽度比例为 4:6，特定场景下可支持配置为 5:5 或 6:4

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214028.93181758599155067459379261030342:50001231000000:2800:229F13D7098923FB5041AE19E95F49A6EF58EB912A883AB392644E19350B45D7.png "点击放大")

## 侧边导航栏

侧边导航栏是大屏设备上常用的一种导航方式，使用侧边导航栏，通过切换导航页签或入口提高操作效率。

-   **底部 Tab 切换侧边导航栏**

窗口宽度≥840 底部 Tab 可切换为侧边导航栏，默认侧边导航栏在窗口容器内嵌入显示。

底部 Tab 可切换为侧边导航栏必须针对导航栏做一定的拓展，例如拓展导航的层级、增加导航的选项、增加高频功能等，若导航选项保持不变仅位置变化则使用侧边 Tab。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214028.19688116316395076141051702004088:50001231000000:2800:4A5384BA8655EC1B866037215D8C7CC7DFC8CA4411A53C0E2A2BFF4267FA3371.png "点击放大")

-   **侧边导航栏显示与收起**

侧边导航栏默认显示，点击导航栏上的图标可临时收起侧边导航栏，在大尺寸设备上通过收起导航栏可以获得更多的内容显示空间。

特殊场景下可选择侧边导航栏固定显示，固定显示时侧边导航栏固定显示在页面左侧，导航栏不显示收起图标，固定显示方式不支持悬浮显示，需要满足窗口最小宽度 ≥ 840。

<table id="ZH-CN_TOPIC_0000001748539684__table122mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001748539684__row127mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539684__p74712001488"><span><img originheight="4568" originwidth="5276" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214029.99591896775661652697934208522218:50001231000000:2800:4F7FAD9AEEEC12324FD9921C4584B37BA6B9EE9D6CF1D416C283DE05AF569211.png" title="点击放大" width="268.5" height="232.46929492039425"></span></p><p id="ZH-CN_TOPIC_0000001748539684__p129mcpsimp">侧边导航栏显示</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539684__p61946376489"><span><img originheight="4568" originwidth="5276" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214029.59178330438358952209362706717358:50001231000000:2800:095E5FA60B54DA4EF6FB52FBCF77373060D1EE2AC34C9CEE5FD095BE2269B582.png" title="点击放大" width="268.5" height="232.46929492039425"></span></p><p id="ZH-CN_TOPIC_0000001748539684__p132mcpsimp">侧边导航栏收起</p></td></tr></tbody></table>

-   **侧边导航栏嵌入和悬浮**

侧边导航栏支持嵌入和悬浮两种显示方式，在支持窗口自由缩放的大尺寸设备上，根据窗口的宽度变化在达到对应断点值后切换显示方式。

<table id="ZH-CN_TOPIC_0000001748539684__table135mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001748539684__row140mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539684__p20133181920508"><span><img originheight="4568" originwidth="5276" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214029.28729369140158512397000969138965:50001231000000:2800:100D0C585C4D33ACDB4CF674EE3CF8777A9CBD2E5DC0AB8261D9E00E5F5288C0.png" title="点击放大" width="268.5" height="232.46929492039425"></span></p><p id="ZH-CN_TOPIC_0000001748539684__p142mcpsimp">窗口宽度 ≥ 840</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539684__p144mcpsimp"><span><img originheight="4568" originwidth="5276" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214030.58027729736961087401853917467044:50001231000000:2800:65C42154FA721F6E7080D5539C1C2872C37FD405BABE4E1E0BA8FD359B3DB162.png" title="点击放大" width="268.5" height="232.46929492039425"></span></p><p id="ZH-CN_TOPIC_0000001748539684__p145mcpsimp">窗口宽度 ≤ 840</p></td></tr></tbody></table>
