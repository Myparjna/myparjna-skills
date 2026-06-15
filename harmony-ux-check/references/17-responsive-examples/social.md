# 社交通讯类

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/responsive-design-examples2-0000001793536901
- 抓取时间：2026-04-04T08:24:54.986Z
社交通讯类场景主要包括社交动态、IM 对话、通话、会议等类型的应用和场景。此类场景旨在让用户享受高效的浏览和互动交互。需要避免因为部分元素显示过大，导致大屏幕上交互效率降低。建议重点关注首页、详情页、对话页、通话页等，有针对性地适配以提高用户体验。

## 分栏布局的 IM 对话

<table id="ZH-CN_TOPIC_0000002364842717__table104mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002364842717__row108mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364842717__X1b80652a09f908414f2ada435ad452ae819b5de">IM 对话建议使用分栏布局，左侧消息列表，右侧消息详情。分栏布局时，左侧列表不变，右侧可切换显示下一层级内容。</p><p id="ZH-CN_TOPIC_0000002364842717__p19564191810334"><span><img originheight="1080" originwidth="4131" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140402.07041073996997358438025696985507:50001231000000:2800:6E18108B7CDBC41C39FC2511D9EADF249AF0B2072A98C65F9C8264FBD70A319A.png" title="点击放大" width="587" height="153.4640522875817"></span></p><p id="ZH-CN_TOPIC_0000002364842717__p1454384112347"><span><img originheight="1080" originwidth="4131" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140402.39687565904787996805754575782978:50001231000000:2800:739421A94703EF7A3C59C5A5C0909226AD79DE6ED7E70CA3E23546F6B0C7C923.png" title="点击放大" width="587" height="153.4640522875817"></span></p></td></tr></tbody></table>

IM 对话场景的多端设计示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140402.71303790408587688108049279550168:50001231000000:2800:BD7D4CA007D54574CD04C7C772E9A9FA6C1ABC550AD2AC4762958EB523870D71.png "点击放大")

分栏的开发指南，请参阅[一多开发实例 (即时通讯)。](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-communication-app#section18771832172516)

## 应用内分屏

在应用内打开元服务、网页、文档、视频通话等内容，可以提供应用内分屏入口，实现边聊边买、边聊边看等任务并行的体验。IM 对话时打开元服务，提供应用内分屏的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140403.43819922600052930411515823220628:50001231000000:2800:845085D1D0E61965E9F6F4EE56ACF6BC0B6FCB13A558BE64590EDD6A1C62EC94.png "点击放大")

IM 对话时打开文档，提供应用内分屏的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140403.80179499670400633932680301066550:50001231000000:2800:A1F5C711BC42C612505CBC003E043504A64F6D536E72F0F27276199F1D0D5ECA.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140403.02976445967216610002455578840265:50001231000000:2800:CA5B2D25F202E725CA8BA3CE2A82DB16AAF6CDF29F0978B5261E8A1FDB77C9C0.png "点击放大")

视频通话时露出分屏按钮，点击按钮后提供应用内分屏的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140403.86722415708009719939324909305531:50001231000000:2800:FCDFEC2BCA2CFD5E74F04CD2609E662E4B165303DAE641914FE0047689B79E85.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.22164806982665364625323624442800:50001231000000:2800:4FC003292EB41AB967FADB6C67B3BF9B723CD398CCBE34C80486F615E2C8456F.png "点击放大")

在折叠屏、平板、电脑上，都可以使用应用内分屏的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.18602533631659832307654725906920:50001231000000:2800:27D0A4F16D2BE25511B94DB3FADBB7155929CC37128639977BDA6D73D91A89C3.png "点击放大")

## 视频通话

### 双人视频通话

<table id="ZH-CN_TOPIC_0000002364842717__table118mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002364842717__row141mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364842717__p145mcpsimp">视频通话场景，尽可能提供全屏沉浸的视频画面。</p><p id="ZH-CN_TOPIC_0000002364842717__p7910744163312"><span><img originheight="1456" originwidth="4000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.71806992836895248010443183122836:50001231000000:2800:01EEE3156D3A5CC733774E7F71EBDB1C4B5ACA8CEE44B81C83E09C238C598117.png" title="点击放大" width="587" height="213.66799999999998"></span></p></td></tr></tbody></table>

视频通话需要适配悬停态，避免在中间折痕区域显示画面或操作按钮。上半屏显示视频画面，下半屏显示操作。需要避免视频通话悬停态时对方的取景画面被横过来。

范式一：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.14618649182888362823196394990283:50001231000000:2800:077A1A38CEF39E58CEFB7EFE1B4D8EC6E0C6590673CE21F4A5574B6EFF6F2CE9.jpg "点击放大")

也可以在悬停时尽量提供沉浸式通话效果

范式二：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.36562478640787572307719886490731:50001231000000:2800:8A7F6585D1291144E87D2B4FB80C345D4AD091D78E254DDE6BCA6C1565C54B6E.jpg "点击放大")

### 多人视频通话

<table id="ZH-CN_TOPIC_0000002364842717__table45231841192411" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002364842717__row257584111245"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364842717__p19575184114243">多人通话时取景框可根据设备的物理尺寸进行响应式的布局设计，尽可能提供最大屏占比的舒适布局。</p><p id="ZH-CN_TOPIC_0000002364842717__p1544420716345"><span><img originheight="1456" originwidth="4000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.67806403136848947828297096012918:50001231000000:2800:2579DB2DD4C04EB9EC4B2F12AB9F32AFD5ED86809F3FC03840233DB01E1BD166.png" title="点击放大" width="587" height="213.66799999999998"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002364842717__row557674115247"><td class="cell-norowborder" style="border: none;" valign="top" width="100%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000002364842717__row8576741122418"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364842717__X75cb57428fb5f9354bc831472f234ef6f83c98c">取景框响应式布局的开发指南，请参阅<a href="https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-responsive-layout" target="_blank">响应式布局。</a></p><p id="ZH-CN_TOPIC_0000002364842717__p12230171213810"></p><p id="ZH-CN_TOPIC_0000002364842717__p35761441182415">更多人的视频通话响应式布局示例：</p><p id="ZH-CN_TOPIC_0000002364842717__p85451536133412"><span><img originheight="1456" originwidth="4000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.40894115400059540977807901561692:50001231000000:2800:86367A33B1920C7B2C47E9561C5B0EC8F23A620880698A3C5CBA24073F7C733E.png" title="点击放大" width="587" height="213.66799999999998"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002364842717__row857674152411"><td class="cell-norowborder" style="border: none;" valign="top" width="100%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000002364842717__row0576204172419"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364842717__p17576174172418">同一设备上取景画面，大小布局和均分布局的示例：</p></td></tr><tr id="ZH-CN_TOPIC_0000002364842717__row105761641202417"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364842717__p5900610160"><span><img originheight="1080" originwidth="2160" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.66539179342794266511817561609304:50001231000000:2800:AE91EE794D788E22D4727B93F1D554ED23C1DE0FCE3EB84442EC87BF38AD4E78.jpg" title="点击放大" width="587" height="293.5"></span></p></td></tr></tbody></table>

## 会议

### 会议的自适应布局

<table id="ZH-CN_TOPIC_0000002364842717__table170mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002364842717__row174mcpsimp"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002364842717__p177mcpsimp">会议界面根据设备的屏幕宽度进行投屏画面和参会人信息的自适应布局。</p><p id="ZH-CN_TOPIC_0000002364842717__p1163919589341"><span><img originheight="1456" originwidth="4000" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.07249778929507603361172586014824:50001231000000:2800:BD4EF3679A5E3B5A5DE298751FC897C70F27C37724FA92A1E9831D535CC1CD3E.png" title="点击放大" width="587" height="213.66799999999998"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002364842717__row178mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%">&nbsp;&nbsp;</td></tr></tbody></table>

在同一尺寸的设备上，根据投屏内容的比例进行自适应布局的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140404.53231864439599217280685905222907:50001231000000:2800:5C991A0F947C089AF1B2B6ACDD520F9D82854DB213740E5FAD0C82E8B798B322.png "点击放大")

本场景的开发指南，请参阅[典型场景布局。](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-page-layout)

### 会议的悬停适配

会议场景的悬停态设计。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.71496146999223476916782208242568:50001231000000:2800:6688BF15B16C97816B1D0289A8002667B5AC407426682CFD02F77F80D3597DC1.png "点击放大")

## 社交动态的图片布局

社交动态和新闻资讯类场景的图文布局比较类似，通常采用上文下图的布局。

### 单张图片/视频

在单张图片的场景下，图片与文字靠左对齐，采用上文下图的布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.93279007109624159889046917111774:50001231000000:2800:495A1CEBF5B775DAF19523612832B4A5E8365FF90925FADCC7EFBDB5D47DE016.png "点击放大")

### 多张图片/视频延伸布局

有 3 张以上数量的图片时，采用延伸布局，可以横向滑动，查看更多图片。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.36129102036737467838183662442039:50001231000000:2800:8E01CCFBD1D06653DC6BD1E8433C8C7AB31C2276C4224A9B168C1385E4B31A36.png "点击放大")

### 多张图片聚合宫格布局

多张图片聚合到一起显示，在宽屏设备上整体聚合图片的高度不要超过屏幕高度的 80% ，约 55% 高度为最佳。

多张图片聚合时，在宽屏设备上接受部分的留白或者通过图片的自适应裁剪减少留白。

6 张图片聚合的宫格布局，范式一：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.67510458782686362240318029093101:50001231000000:2800:F26F249B81FDAAFC46A69198263AD2A371DFC784E7245FA9DA461A68CCCABD33.png "点击放大")

6 张图片聚合的宫格布局，范式二：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.43858215859408688975796067350427:50001231000000:2800:90740676A194F9C6A47D8F3E72C357FBC08AB3FD48C80E1C761983263A30D441.png "点击放大")

5 张或 7 张图片聚合，不可避免的会出现部分留白，如下图：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.47075698467451253145802665887153:50001231000000:2800:770664169E60A20122C7315B38C7F3978F4C5CC4A23C6BE19E801C97D2E399E8.png "点击放大")

### 多张图片杂志化自适应布局

通过图片的自适应布局和基于设备宽度的智能裁剪能力，可以实现一种图片的杂志化自适应布局。

该布局下，优先让每张图片按照相同比例相同大小排布显示，当无法避免有留白情况时，允许部分图片放大显示，若依然无法避免有留白情况，则允许部分图片自适应形变裁剪，从而确保在宽屏设备上没有留白，尽可能利用宽屏设备空间。

需要注意整体图片的高度不要超过设备高度的 80%，约 55% 高度为最佳。

3 张图片杂志化布局的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.30923591031102743306297151619928:50001231000000:2800:6BE8E381C83903ED9FCDB6070CA107B466D7D9F5C48D13C3A05A26A69CA12DE0.png "点击放大")

4 张图片杂志化布局的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.82790666867581100125224861354728:50001231000000:2800:0520F6C6D52FDABA2D5918F07A278DE86C0D50050DB089B1B6E71347EA88F8B2.png "点击放大")

5 张图片杂志化布局的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.50708813585860873157029107672490:50001231000000:2800:FCD471B39E7DA30ECD0CC99B3D53F9FA86C6DBB566A5869FACB5F78DE0CF6D50.png "点击放大")

6 张图片杂志化布局的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140405.10627123464752212889239574999143:50001231000000:2800:E32E6469873FC30169256ADC34AE592BC240660A405A5BCB6BB4C1040F22C08A.png "点击放大")

7 张图片杂志化布局的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140406.08107115691568158485185925544070:50001231000000:2800:96211F4AA7DBA736604F347FBA5B90ACD546ED5F7E7DACAE5F039DF4710BD1C0.png "点击放大")

## 社交动态的卡片布局

### 动态卡片首页

**单列卡片变宽**

手机上的单列动态卡片，在宽屏设备上可露出更多辅助信息变成更宽的动态卡片。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140406.67856069437650151124748536435577:50001231000000:2800:47DAEE79EC3626503C28DD0FD9F1977D3C055158FD6906B0E8A22217A08320A7.png "点击放大")

**单列卡片变分栏 + 瀑布流布局**

手机上的顶部关注列表和动态卡片，在宽屏设备上挪移布局并形成分栏，在更宽的平板和更大尺寸的屏幕设备上可露出更多列的动态卡片，成为分栏加瀑布流布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140406.89840767178873387600328524199950:50001231000000:2800:5B403A0DB9D76D851569B39D56E1BB456EA241189AE5CCB15E97600A9E16F9F2.png "点击放大")

分栏的开发指南，请参阅[一多开发实例 (即时通讯)。](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-communication-app#section133771713132818)

**单列卡片变瀑布流布局**

也可以直接从手机的单列卡片到宽屏设备的瀑布流结构，随着屏幕宽度的增加显示更多列数内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140407.72637617691285371189840416612044:50001231000000:2800:AFD09E41F31B7204B772F8E2216D8463F830CF1BC3245E8FAC6BD940365C5974.png "点击放大")

瀑布流组件的开发指南，请参阅 [API 参考 (WaterFlow)。](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)

### 社交详情

在宽屏设备上可利用屏幕宽度通过挪移布局将上下结构的内容变为左右结构。例如在折叠屏、平板上通过挪移布局实现边看边评的体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140408.90596561517047666437453350101461:50001231000000:2800:950EEB0986A0B6AB08B444AF19389F68593E2F254BF786506F50BEE9B566E1EF.png "点击放大")

自适应能力的开发指南，请参阅[典型场景布局。](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-page-layout)

折叠屏这种接近 1:1 的方形设备，可提供布局切换按钮，允许用户切换布局样式的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140409.78723347526455198634664867479486:50001231000000:2800:7E29D0974C343A64ADEC4D690DE18B14DDEE7A8ACBF55878B03A7D720A5F7427.png "点击放大")

往上滑动浏览内容时自动隐藏标题栏、工具栏，提供沉浸浏览体验的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140409.76109084219617316512786349855385:50001231000000:2800:7A66D19DA7A35F3617591F8623645C1144AE0E75B97BF8E76C48816F11431F14.png "点击放大")

### 查看图片详情

多设备场景下，点击图片查看详情时，同样适用于边看边评的体验，即：点击评论按钮，在右侧的侧边面板显示评论内容；边看边评时也支持横向滑动切换下一张图片。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140409.35710509358518576091118938207572:50001231000000:2800:545A3A36AF1814F03BF57592B3446313BFB4ED92C96894FA1986181C0CAB480A.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260109140409.84459449587463215413372770022950:50001231000000:2800:211754D2590664F45548BCFCDD76B967DC1865ABC3586B9B563FE70FE9DC315D.png "点击放大")
