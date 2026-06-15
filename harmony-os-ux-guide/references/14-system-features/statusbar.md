# 应用状态栏接入

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/statusbar-0000002319710910
- 抓取时间：2026-04-04T08:24:44.307Z
## 状态栏

状态栏用于显示设备当前的状态信息，包括时间、WLAN、电量、音量等，也支持用户快捷使用应用功能和设置应用功能，如输入法、截屏等。状态栏默认显示在屏幕的底部区域。

## 适用场景

-   建议场景：应用长时间使用时，需提供部分重要应用功能，以便高频和快捷操作。
-   不建议场景：应用短时间使用或在应用窗口内就能更加便捷操作的功能。

<table id="ZH-CN_TOPIC_0000002319710910__X77f4ab05121e349784b964c8c98ac69357e28bb" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__row165mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p167mcpsimp"><span><img originheight="800" originwidth="3284" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/YxJfMIGwTiOHZSOpo83YBA/zh-cn_image_0000002353786401.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBBEEA450EBA8A142261666292EAC636C8632803D560D9DB2F2B528CD82AECBB" title="点击放大" width="587" height="142.99634591961023"></span></p></td></tr></tbody></table>

## 交互规则

**鼠标左键**

1.  点击应用功能图标，直接触发相对应的功能操作，如截屏。
2.  点击应用功能图标，呼出快捷功能详情面板，适用于应用提供部分高频或重要功能，同时也可通过面板跳转至应用窗口。不推荐点击应用功能图标后，直接跳转至应用窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ImGOcn-VQB6JDuK0L0cTrw/zh-cn_image_0000002564247067.jpg?HW-CC-KV=V1&HW-CC-Date=20260404T082440Z&HW-CC-Expire=86400&HW-CC-Sign=22EAF8D63E417E8BE065A885A170276645BAED0151277810DD7B26A51A3AC826 "点击放大")

<table id="ZH-CN_TOPIC_0000002319710910__X1c1e0a7205a6fbb6802105a29fde901c130af51" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__row1573311514116"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002319710910__p163711930452"><span><img originheight="8" originwidth="1910" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/uFHweQ4_Tx6tfzHSzwhjIg/zh-cn_image_0000002356034513.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B84A67ED921E0EE6763F476D49B2549A85EEA946719B21D76F108FDF701E9EE0" title="点击放大" width="587" height="2.4586387434554973"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002319710910__row793017480193"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002319710910__p861122215448"></p><p id="ZH-CN_TOPIC_0000002319710910__p11931184816196">推荐体验</p></td></tr><tr id="ZH-CN_TOPIC_0000002319710910__row182mcpsimp"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p184mcpsimp"><span><img originheight="1200" originwidth="3284" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/l3Y1JvbwSMmcTDhPy53Pgg/zh-cn_image_0000002319827652.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAE5596F54C842AB1AC792BCB1D57A524DD5258F75E2AB9DCE13C874FF55C984" title="点击放大" width="587" height="214.49451887941535"></span></p><p id="ZH-CN_TOPIC_0000002319710910__p209061858154418"><span><img originheight="8" originwidth="1910" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/YxQIVxVeTL-4V0sI5LFsVA/zh-cn_image_0000002322035866.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A71A54D75E43018EEA1B1250A34CF7373E72C12611C01BDE00681BE4A8E5507" title="点击放大" width="587" height="2.4586387434554973"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002319710910__row20536040121912"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002319710910__p553604071920">不推荐体验</p></td></tr></tbody></table>

**鼠标右键**

鼠标右键点击应用功能图标，可呼出功能管理菜单。应用可提供“退出”等菜单项。

**鼠标悬停**

鼠标悬停在应用功能图标，可显示气泡提示。应用可根据场景提供当前状态或应用功能名称。

<table id="ZH-CN_TOPIC_0000002319710910__table10499654151817" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__Xe0a19beeec432f690600d7ed33d2a9f28acda89"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p231mcpsimp"><span><img originheight="800" originwidth="1648" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/YDGadP9YR12EHjix8gpjlA/zh-cn_image_0000002353910281.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25C2A2F446A1D3B4785C09277EB63817464D6F0198E80048D69A258001C7BEBB" title="点击放大" width="268.5" height="130.3398058252427"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p233mcpsimp"><span><img originheight="800" originwidth="1648" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/DVLa5szNSMiYGXvpRgJzvQ/zh-cn_image_0000002319991532.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=917EA331DE68382A59AA925925C3420F1CD55C358FDD1C5895FA0DBDAB56D866" title="点击放大" width="268.5" height="130.3398058252427"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002319710910__row234mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002319710910__p236mcpsimp">鼠标右键</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002319710910__p238mcpsimp">鼠标悬停</p></td></tr></tbody></table>

## 详情面板

### 面板构成

功能详情面板结构：包含标题区、内容区和更多设置区，应用可根据场景按需组合。

-   标题区：应用需定义功能名称。
-   内容区：应用按需定义功能内容。
-   更多设置区：应用按需提供相对应地应用窗口跳转入口，支持点击直接打开窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/pLQlPDRbRBCj4bCP9f56nQ/zh-cn_image_0000002533247260.jpg?HW-CC-KV=V1&HW-CC-Date=20260404T082440Z&HW-CC-Expire=86400&HW-CC-Sign=9F1C50E0264C4407C90C484CF93F02C8AFCBB2A81EFF52D70E0B5F0A25E573D7 "点击放大")

<table id="ZH-CN_TOPIC_0000002319710910__table98351715224" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__row247mcpsimp"><td class="cellrowborder" colspan="2" style="border: none;" valign="top">&nbsp;&nbsp;</td></tr></tbody></table>

### 面板视觉规则

**标题文本**

文本大小：Title\_S（Bold）

文本颜色：font\_primary

**标题文本超长规则**

文本至多显示一行，逐级缩小字号至 16sp，仍然超长使用“…”截断。

**模糊材质**

状态栏菜单默认附带模糊和阴影材质，且支持深浅两套效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/KdHcdpV7REynI0Tjd5SjYQ/zh-cn_image_0000002533408280.jpg?HW-CC-KV=V1&HW-CC-Date=20260404T082440Z&HW-CC-Expire=86400&HW-CC-Sign=85DBC4E34C389D47092E4AE212B1050C7F46C0F191B33461BAA0085AC63AB42C "点击放大")

<table id="ZH-CN_TOPIC_0000002319710910__table16437153282316" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__row141mcpsimp"><td class="cellrowborder" colspan="3" style="border: none;" valign="top">&nbsp;&nbsp;</td></tr></tbody></table>

**面板最大高度**

1.  应用可根据内容配置高度。
2.  最大高度：桌面高度-dock栏高度-上下安全间距8vp\*2。
3.  超过最大面板高度后，内容区增加滚动条，通过滚动条上下滑动查看内容。

<table id="ZH-CN_TOPIC_0000002319710910__table1921545562316" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__row150mcpsimp"><td class="cellrowborder" colspan="3" style="border: none;" valign="top"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p152mcpsimp"><span><img originheight="2188" originwidth="3280" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/vKvCbxRdQBCnz_mdsjKnBQ/zh-cn_image_0000002319831764.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37ECB80C412B39AE924D7D51FC8A6FD3EE907C8815AA68F470E54695AE063377" title="点击放大" width="637" height="424.9256097560976"></span></p></td></tr></tbody></table>

## 图标样式

状态栏是桌面重要的一部分，视觉效果需要和谐美观。不推荐直接使用色彩鲜艳的应用图标，推荐上传系统图标，具体样式请参阅[HarmonyOS Symbol](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。

<table id="ZH-CN_TOPIC_0000002319710910__Xa5f0199cfb6dbd4ad43828bc0221218ac6a2949" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__row160mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p162mcpsimp"><span><img originheight="560" originwidth="1648" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/YG50iZLrTdm_kpAHBWYmyw/zh-cn_image_0000002353910333.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA68D6C712906F84BF09388B308BC7B7A9A7CE70338662E7E820B64F4657EB41" title="点击放大" width="268.5" height="91.2378640776699"></span></p><p id="ZH-CN_TOPIC_0000002319710910__p181368273454"><span><img originheight="8" originwidth="1910" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6OAF6FLzSIi56SaUewaMCQ/zh-cn_image_0000002355954377.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D3FB7DE4EEFD8E68DE1DB3D7D289B400959ABB215ADB493932FEB5DC995822D" title="点击放大" width="268.5" height="1.124607329842932"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p164mcpsimp"><span><img originheight="560" originwidth="1648" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/4nH6j0TMRNiDcAb--iqExg/zh-cn_image_0000002319991588.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2C804596191677D8B2203427B4230318FE4BFAA00F8D300A41E5C8B26DE0A16" title="点击放大" width="268.5" height="91.2378640776699"></span></p><p id="ZH-CN_TOPIC_0000002319710910__p554014420455"><span><img originheight="8" originwidth="1910" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/W67xSuTmRzWsEK1Q3ueS3A/zh-cn_image_0000002322195686.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D3AE350B77FE489E338B1CE1773564D19D5D4EF89A38E64856AB8B9EC392D1C" title="点击放大" width="268.5" height="1.124607329842932"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002319710910__row5204250122411"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002319710910__p1120455018242">推荐样式</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002319710910__p169mcpsimp">不推荐样式</p></td></tr></tbody></table>

**图标尺寸和颜色**

-   图标尺寸：20\*20vp
-   热区大小：34\*34vp
-   资源格式推荐 Symbol 与 SVG 格式，其次为 PNG 格式。

<table id="ZH-CN_TOPIC_0000002319710910__X9f63674124b6ca39c2944e23f1ce77af342ec32" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002319710910__row180mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p182mcpsimp"><span><img originheight="560" originwidth="1648" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/lfxfq_arQc6kp0qQK-OzEQ/zh-cn_image_0000002353790549.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4EF9DF74990D5B06725ED4A1400343E0FDB23EFDA7CA7B6EBF65EEC946B3275" title="点击放大" width="268.5" height="91.2378640776699"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000002319710910__p59461912257"><span><img originheight="560" originwidth="1648" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/vz1MFutSReukw_5gVbzemg/zh-cn_image_0000002319831768.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082440Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EBC36BCFBC5A41F30AC83B2EC9A2A33393C8F658F6AA559CEA20ECEE1F3D037" title="点击放大" width="268.5" height="91.2378640776699"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002319710910__row185mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002319710910__p187mcpsimp">浅色背景-图标颜色：#000000 90%不透明度</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002319710910__p189mcpsimp">深色背景-图标颜色：#FFFFFF</p></td></tr></tbody></table>

## 开发文档

应用接入状态栏请参阅开发指导[Status Bar Extension Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/status-bar-extension-kit-guide)。
