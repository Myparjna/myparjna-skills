# 框选

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/hmi-scenes-selection-0000001957005521
- 抓取时间：2026-04-04T08:23:45.851Z
框选是指通过使用指针拖动选择框，使被框到的文本、文件等被选中。框选对象后，内容支持键鼠操作如拖拽、弹出菜单、加减选等。框选的对象可以为单个控件也可以为多个控件，可以为同类型的对象也可以为不同类型的对象。

框选的控件分为两类，内容类和文本类。内容类的控件主要是容器类控件如列表、宫格，文本类的控件则包含单行文本、多行文本、搜索框、富文本等。

<table id="ZH-CN_TOPIC_0000001957005521__X5c363658a37c78edbf04a7baeef5a45f7daba83" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957005521__row108mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957005521__p110mcpsimp"><span><img originheight="450" originwidth="1028" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619215619.37386263884354749123500909746134:50001231000000:2800:72AF116D9E16B302B88FE86A5EBB398D68E021720D5B8F7E91422E0A443F82D3.png" title="点击放大" width="268.5" height="117.534046692607"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957005521__p112mcpsimp"><span><img originheight="214" originwidth="1204" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619215619.51835429267026855348798532846292:50001231000000:2800:AC3C8C723C17B1F281C26A7393B153527BB21B12259A928EF3D27B823C36CDC9.png" title="点击放大" width="268.5" height="47.7234219269103"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001957005521__row113mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957005521__p115mcpsimp">内容类控件</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001957005521__p117mcpsimp">文本类控件</p></td></tr></tbody></table>

## 发起框选

按下并移动可发起框选，抬手后完成选择。多种输入方式都能发起拖拽，鼠标和触控板交互为精细化操作，适用于内容类和文本类控件。

鼠标

鼠标按下并移动发起框选，抬手后结束框选。框选内容类对象时都会出现选框，框选文本类对象不会出现选框。

内容类对象框选

内容类对象可以从空白处发起框选，即发起框选的初始位置不在对象上。热区较大的对象可以分区处理框选热区，如 List 较长时右侧较为空白的区域为框选热区，图标和标题区为拖拽热区。

文本类对象框选

当鼠标悬浮在文本类可以框选的对象上时会变成工字形指针样式。文本类对象发起框选后没有选框，文本会呈现选中态。

## 加减选

在键鼠操作中，通常会使用 Ctrl 键和 Shift 键实现加减选，该操作也支持触屏/触控板 + 键盘的协同操作。

### 间序加减选

间序加减选即通过组合操作可以实现对象的不连续的跳选。

内容类对象

按住 Ctrl 键加上鼠标左键点选或者鼠标左键框选，间序加减选。

文本类对象

按住 Ctrl 键加上鼠标左键框选，间序加减选。

### 连续加减选

内容类对象

按住 Shift 键加上鼠标左键点选或者鼠标左键框选，连续加减选。

文本类对象

-   已有选择文本，按住 Shift ，点击或滑动文本中其他位置，可连续加减选。
-   点击：点击文本外部，已选中的文本到点击位置之间的文本被加选。点击文本内部，已选中的文本靠近点击位置的端点到点击位置之间的文本都被减选。
-   滑动：左键拖动指针在文本上滑动。滑到文本外部时，根据滑到的位置动态加选，滑到文本内部时，根据滑到的位置动态减选。

<table id="ZH-CN_TOPIC_0000001957005521__Xac0dd46da0ccb739ef7fc6b2b62974f61829c41" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001957005521__row140mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957005521__p142mcpsimp"><span><img originheight="134" originwidth="1676" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619215619.99523563340621568734554048541551:50001231000000:2800:E0463C3940568D2E6912210F2EB934B819C340DF313A9B4A8FCEEF14228749D0.png" title="点击放大" width="268.5" height="21.467183770883057"></span></p><p id="ZH-CN_TOPIC_0000001957005521__p143mcpsimp">加选</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957005521__p145mcpsimp"><span><img originheight="140" originwidth="1676" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619215620.45974444274531603143844091256365:50001231000000:2800:3CD7A42B283E62DF60A445FC2C93CDCB1422BF6424FC58C4F41E25578E802063.png" title="点击放大" width="268.5" height="22.428400954653938"></span></p><p id="ZH-CN_TOPIC_0000001957005521__p146mcpsimp">加选完成</p></td></tr><tr id="ZH-CN_TOPIC_0000001957005521__row147mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957005521__p149mcpsimp"><span><img originheight="134" originwidth="1676" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619215620.66045030649783391823615256060152:50001231000000:2800:768238AE13385C3284FE3097725E3FBAE2AD3F3C58F42F89E50E3B5E193528AD.png" title="点击放大" width="268.5" height="21.467183770883057"></span></p><p id="ZH-CN_TOPIC_0000001957005521__p150mcpsimp">减选</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001957005521__p152mcpsimp"><span><img originheight="134" originwidth="1676" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619215620.78437624846433203511547968943107:50001231000000:2800:0BE8CF1CB36EF7089B9959D759F6F2A157A75A9D4355BF2BCF9A0FE656213B5B.png" title="点击放大" width="268.5" height="21.467183770883057"></span></p><p id="ZH-CN_TOPIC_0000001957005521__p153mcpsimp">减选完成</p></td></tr></tbody></table>

### 走焦加减选

已有选中内容，按住 Shift 和键盘方向键。从列表对应方向的最后一个项开始加选。

## 视觉规则

### 鼠标框选底板色

选框填充颜色：

引用 ohos\_id\_color\_component\_normal (#000000) 叠加 ohos\_id\_alpha\_normal\_bg

选框描边颜色：

引用 ohos\_id\_color\_foreground\_contrary 叠加 ohos\_id\_alpha\_highlight\_bg

选框描边宽度：1vp

文本选中底板颜色：

引用 ohos\_id\_color\_text\_highlight\_bg (#0A59F7)

叠加 ohos\_id\_alpha\_highlight\_bg

### 框选底板位置

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619215620.44941061212315043831707717810004:50001231000000:2800:01553F809A2021D29247D20469CBB41684B1C2E02CD763BE0BDB5ADE260A3BA3.png "点击放大")

与光标上边缘，左边缘各留 1 vp

与光标下边缘、左边缘各留 1 vp

与光标上边缘、右边缘各留 1 vp

与光标下边缘、右边缘各留 1 vp
