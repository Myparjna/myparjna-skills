# 深色模式

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/dark-mode-0000001823255497
- 抓取时间：2026-04-04T08:23:58.342Z
深色模式满足更多个性化的需求，基于人因研究设计了深色模式下舒适的颜色范围。深色模式开启后，浅色主题应用界面背景会变成深色，而文字、图标等前景会变成浅色。深色模式的界面上内容更加突出、在 OLED 屏幕的设备上更加省电、能够给用户带来视觉舒适感和沉浸式体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224853.21723442826560907611178096320403:50001231000000:2800:A7374705D0E0DE02D9DE268E9CAD4834F6FA25D3BE21132E47979DC15BC8EDBA.png "点击放大")

## 设计原则

由于深色模式下屏幕总发光量更少，部分用户倾向于在暗环境使用深色模式；但同时，也有相当比例的用户出于对深色风格的喜爱或出于节能省电的需求（深色模式下OLED屏幕功耗更低）而全天开启深色模式。

因此，在深色模式的设计中需要考虑在全天不同环境下清晰易读，同时特别关注在暗环境的使用舒适性，另外还需要保持与浅色模式在层级感知、色彩语义方面的一致性。

### 易读性

深色模式下为了保证清晰易读，文本、图标等前景与深色背景之间仍需要满足最小对比度要求。根据WCAG（Web Content Accessibility Guidelines）的要求和华为人因团队研究结果，文字、图标满足最低的对比度要求，分级标准如下：

展开

| 
**场景**

 | 

**推荐（优秀）**

 | 

**一般**

 | 

**不建议**

 |
| :-- | :-- | :-- | :-- |
| 

大字号（17fp或15fp以上粗体）、辅助文本（如列表二级文本，或其他对识别效率要求不高的场景）、功能性图标

 | 

大于3:1

 | 

1.9:1 – 3:1

 | 

小于1.9:1

 |
| 

非大字号主要文本（如长文本正文、列表一级文本）

 | 

浅色模式大于4.5:1

深色模式大于5:1

 | 

浅色模式3:1-4.5:1

深色模式大于3:1-5:1

 | 

小于3:1

 |
| 

建议表示活动状态的可交互控件

 | 

控件背板与背景之间对比度不小于2.2:1

 | 

\\

 | 

\\

 |

注：装饰性文本、表示disable状态的文本、logo等特殊场景不需要满足以上要求

<table id="ZH-CN_TOPIC_0000001823255497__table155mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001823255497__row160mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p162mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224853.71651994154110677305606061260834:50001231000000:2800:29BD6D3AA3C361F036DACF0696C117F6C571370CE2A9007E0DF9C131BB1EFBE0.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p163mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.83400998912867119281281406853961:50001231000000:2800:29655023C944B1282E03A2EF1F05AB9ECC545C41706A355FD3056A86F7157F0F.png" width="268.5" height="2.6531620553359687"></span></p><p id="ZH-CN_TOPIC_0000001823255497__p16872121652414">正文与背景对比度不低于5:1</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p166mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.63534770295896193485743347130030:50001231000000:2800:3AE3A0B9CE28C20A50FCE67D95C37A70E947905302250522175EDAD91F7B7368.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p167mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.29874717300992470675476941749443:50001231000000:2800:B9F6E2D171F626F92F759F34539E7E749F132A9C4CA1F95588E8262636B1AF5A.png" width="268.5" height="2.6531620553359687"></span></p><p class="start(2)" id="ZH-CN_TOPIC_0000001823255497__p136922142417">正文与背景对比度低于5:1</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000001823255497__table169mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001823255497__row174mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p176mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.39226411043530825585882609456991:50001231000000:2800:AD16AB6C9169B86FB71C70E169E7B33BAEEA1CE63C8495912707088FC6604763.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p177mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.90992911262230409332395424126215:50001231000000:2800:9675B0772E4B129C0B5B2EB6497E275F48BB507A4DF29D77F8574021F6CFE02E.png" width="268.5" height="2.6531620553359687"></span></p><p class="start(3)" id="ZH-CN_TOPIC_0000001823255497__p5926194512216">辅助文本与背景对比度不低于5:1</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p180mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.21706102676128537722234296163492:50001231000000:2800:AFD45D93FCC571B5325B5191153417AD17AC74B621CD6914FC57DF0A7068838D.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p181mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.81861900514243016796226443196949:50001231000000:2800:64DE47385BBED81C6C5D5E2C6ADB7226143D5BC06B022F21EC4E357733208ADE.png" width="268.5" height="2.6531620553359687"></span></p><p class="start(4)" id="ZH-CN_TOPIC_0000001823255497__p1155224819220">辅助文本与背景对比度低于1.9:1</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000001823255497__table183mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001823255497__row188mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p190mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.21673560223704400386904240258238:50001231000000:2800:5CF5DA1E1E4240D38AC6833983822023F7734DE5F7A821C7DD70E5DF147B89B0.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p191mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.01882325672757457719821500422515:50001231000000:2800:D5E5AEB21D4B918BD1E6B4234A8D8BD4D5A33855FF8AB6ED3A1AF12C347159B5.png" width="268.5" height="2.6531620553359687"></span></p><p class="start(5)" id="ZH-CN_TOPIC_0000001823255497__p1636905110223">可点击控件背景填充色与页面背景对比度不低于2.2:1</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p194mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.48762073029280817442995718271467:50001231000000:2800:50B22154E317CC75DD5C80BD6ED513C8474F5636660156BF7536CCC0B12CEDFA.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p195mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.74997310543575303867204708784924:50001231000000:2800:B4AC1EE3799C8C0F319EBACF6E2BE5052303FB8E508A890ED628B462B2046DB9.png" width="268.5" height="2.6531620553359687"></span></p><p class="start(6)" id="ZH-CN_TOPIC_0000001823255497__p1246175417223">可点击控件背景填充色与页面背景对比度低于2.2:1</p></td></tr></tbody></table>

对于同时使用多个多彩色用于表示不同状态或用于相邻位置时，在适应对比度要求的基础上，还需要满足色彩差异要求：

展开

| 
**场景**

 | 

**要求**

 |
| :-- | :-- |
| 

一般要求

 | 

两个需要区分的颜色或相邻颜色，色彩差异△Euv >= 20 ；

 |
| 

无障碍要求

 | 

考虑色盲群体无障碍需要，使用色盲模拟器后，两个要区分的颜色或相邻颜色，色彩差异△Euv >= 20

 |

<table id="ZH-CN_TOPIC_0000001823255497__table217mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001823255497__row222mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p224mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.47600182147980793268493848877217:50001231000000:2800:04D4254AD43BB8CBAF01FA909C5C99B62EB00AC54CA773B20EFF216B162AAF5C.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p225mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.97514768551149663478468019992917:50001231000000:2800:6192894989C633AA63285D4EBF2C614DD93B18E3673EF13087FC3C7A1B648CEE.png" width="268.5" height="2.6531620553359687"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p227mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.79225471367670334747030271464992:50001231000000:2800:7978956679AF23CA91821790B797F1A7D40B993081A63374F6FAD0BF23524352.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p228mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224854.34744180210198906623485819589705:50001231000000:2800:C04E943EED99E31A32E8B3A7DE948DF502F3620AA242E4B658552BB984F70AD4.png" width="268.5" height="2.6531620553359687"></span></p></td></tr></tbody></table>

### 舒适性

由于部分用户时常在暗环境选择使用深色模式，深色模式建议遵从以下原则以尽量避免刺眼等舒适性问题。

展开

| 
**要求**

 | 

**推荐（优秀）**

 | 

**一般**

 | 

**不合格**

 |
| :-- | :-- | :-- | :-- |
| 

文字对比度上限

 | 

文字需要谨慎使用大于17.6:1的高对比度

 | 

15.7:1-17.6:1

 | 

大于17.6:1

 |
| 

小图片、图标背板

 | 

对比度建议不大于15.7:1

 | 

\\

 | 

\\

 |
| 

浅色控件使用与适配

 | 

同时满足以下三条要求：

\-深色模式下应用应切换为深色背景

\-应用内避免黑白跳转的页面

\-页面上不建议使用大面积白色图片或背景

 | 

深色模式下应用切换为深色背景，但存在黑白跳转的页面或大面积白色图片

 | 

深色模式下应用仍为浅色界面

 |

<table id="ZH-CN_TOPIC_0000001823255497__table277mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001823255497__row282mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p284mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.11399489669318397719148941388003:50001231000000:2800:81F3F67AB7BC6BC043544E36C1EC8267E75349D06370081E5D1DAAC5283FA16E.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p285mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.72886904135329939156678329180527:50001231000000:2800:D22BE7EAE287C70FD9549A4110C0C1A697BFC4BE44598E3AA8351E50B50258EC.png" width="268.5" height="2.6531620553359687"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p287mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.91524674497146223900060204086675:50001231000000:2800:25F8AD4E12144A5B0EE16238B198F2A95356C57CAC2D4B6FF816AE9234B99E70.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p288mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.79661235850222298187973228219092:50001231000000:2800:A6A04FB276E55DC248CD4A6487A5FE8EC3DD58C1F5C9DE101FC466D97A1EE3DF.png" width="268.5" height="2.6531620553359687"></span></p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000001823255497__table289mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001823255497__row294mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p296mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.62753742886166650317580104997524:50001231000000:2800:CF0B8075A1624A75E00EFC224C035841A41A917F1BBA0FC92D6F3D2BC6EDF6FE.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p297mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.03219684911259163408536347150032:50001231000000:2800:B7199F382888163DE4707387DF63D3DA4C81E958D317CA3973516891207B3E0E.png" width="268.5" height="2.6531620553359687"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p299mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.01360244746143639761494818748294:50001231000000:2800:F2F6510251C29D47B17A6ACD0E5AB1280A66135AA0417325DBD4E23479716217.png" title="点击放大" width="268.5" height="204.515350877193"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p300mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.00218074507723357231700464777034:50001231000000:2800:F2E74B778C3E0DA84D7271DA4751CE8541DC91FDC08AEC15E7A60A289DDF8EEA.png" width="268.5" height="2.6531620553359687"></span></p></td></tr></tbody></table>

### 一致性

由于多数应用设计以及用户使用的默认模式为浅色模式，建议在深色模式的设计中需要注意与浅色模式保持一致性，主要包括以下几方面

-   **层级的一致性** 浅色模式下明度不是唯一的表达层级的视觉线索，而在深色模式尤其是在黑色背景上，用户对投影的感知程度降低，通常使用明度表达层级，因此不同层级之间需要有一定的明度区分，并与浅色模式感知一致
-   **色彩语义的一致性** 深色模式下，表示警示、通话等具有语义信息的颜色需要保持一致，可以在保持色相一致的前提下对明度进行调整
-   **同类控件风格一致性** 深色模式下，在用应用或不同页面中的同类控件，视觉风格（颜色、形状等）保持一致

<table id="ZH-CN_TOPIC_0000001823255497__table310mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001823255497__row316mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p318mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.95493531063984279852927873939084:50001231000000:2800:D6E3F3D99FBE5FDA3005FAECF0BFC786DA9B67558CEAAB1348E9A50AB04089AE.png" title="点击放大" width="162.33333333333331" height="123.64863547758283"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p320mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.33627668795962366263314931193157:50001231000000:2800:6FC44D23CE50EA88A0F7E1FA74D5D07E35DFFB05EB2AB801FBB1A186C177C07B.png" title="点击放大" width="162.33333333333331" height="123.64863547758283"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p321mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.74247160113873289664140300813649:50001231000000:2800:C9E05EF9EE241429D9C6A71A9ABD7EBDECA07788F7EB921E6FE03F78E513584B.png" width="162.33333333333331" height="1.6040843214756255"></span></p><p id="ZH-CN_TOPIC_0000001823255497__p322mcpsimp">正确示例</p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p324mcpsimp"><span><img originheight="1042" originwidth="1368" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.10615208087742698921729897937248:50001231000000:2800:7B737B0038C4A3249BC3A5824B07DFB1E51A68089F15813233A4B5BC162FAFD3.png" title="点击放大" width="162.33333333333331" height="123.64863547758283"></span></p><p class="msonormal" id="ZH-CN_TOPIC_0000001823255497__p325mcpsimp"><span><img originheight="5" originwidth="506" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224855.31665194127435524356543621889441:50001231000000:2800:E1765F1F6BE147FAA0B9EA88D9620BA4E0E377532404E4AD740F5E79B0296271.png" width="162.33333333333331" height="1.6040843214756255"></span></p><p id="ZH-CN_TOPIC_0000001823255497__p326mcpsimp">错误示例：色彩语义不一致</p></td></tr></tbody></table>
