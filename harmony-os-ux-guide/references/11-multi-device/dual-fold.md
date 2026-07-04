# 双折叠

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-0000002352875141
- 抓取时间：2026-04-04T08:24:43.001Z
## 概述

<table id="ZH-CN_TOPIC_0000002352875141__table212mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row216mcpsimp"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p219mcpsimp">折叠屏设备的三种形态分别为<strong>折叠态、展开态和悬停态</strong>。</p><p id="ZH-CN_TOPIC_0000002352875141__p221mcpsimp">折叠态便于随身携带和单手操作，适合移动场景下的便捷使用；展开态屏幕变宽，能够充分展示应用内容，适合多任务处理和沉浸式体验；悬停态则处于完全展开和折叠的中间状态，设备可稳定放置，让用户解放双手。</p></td></tr></tbody></table>

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163706.54572201873476280781068139868112:50001231000000:2800:A69915E768105AB004F20E2A6F02CFDB5751C60576A4AAF9EC7D1417FBC5A9FF.png "点击放大")

## 基础要求

为了保证以上体验，需要满足以下基础体验要求：

### 信息完整

-   图片、视频等视觉元素不应发生变形、裁剪、显示不全等信息缺失。
-   一般情况下，展开态不应出现页面内的内容元素数量减少，或图形化元素模糊、分辨率下降或视觉体量减小等损失，确保展开态的内容元素不少于折叠态内容元素信息量的3/4。

<table id="ZH-CN_TOPIC_0000002352875141__table499mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row504mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p1493917187447"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163707.46546813818163655087136629399673:50001231000000:2800:B83A6BD14BB210FB13A77FCAFE8388198D8FF9D6C358F5EBCAD27AB3FBEECFEB.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1544852212339"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163707.84545237085439172475132378271940:50001231000000:2800:6381D9310BFE63886D82E038228797BC359B320A82E63FF2284E64607C09A912.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p508mcpsimp">推荐</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p572402219455"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163707.20135992288344562475928557938014:50001231000000:2800:5585A13EB1552B83D1E9CBCBDDB7632C1C560AB3FB4321AFBFCFEB2E74F912C1.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1173031012483"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163707.19243485236026661989372778282466:50001231000000:2800:3AF04D26F8FD1C5A49C6FD553ECCF5BA920F688E215AAE7E2AEF6A0A8A2B3351.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p510mcpsimp">不推荐（图片过大导致一屏信息显示过少）</p></td></tr><tr id="ZH-CN_TOPIC_0000002352875141__row511mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p7760947104518"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163707.13692784211938920495655287989859:50001231000000:2800:E8A618A980685371F2C518ABE6029C232F03CC457752897B91620EF6E692C320.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p20423123611489"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163707.28846787199796187156503539788523:50001231000000:2800:AA4B84CF7D38BF7A391526A038EF1173D9BFB0312709602572221C6FA1F24AEF.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p515mcpsimp">推荐</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p28851134619"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163707.20335480708687299858022350879346:50001231000000:2800:4C2F51D941CEDDF0C13767F0A64CFB1C35B2CF40FC8EC8FA50748216E79CE432.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p142615218346"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163708.04798769249471571565163429048145:50001231000000:2800:0698F39A32565D0EF65FD6B8871246748265D42727075059C302B7CD38F26793.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p517mcpsimp">不推荐（内容放大导致一屏信息显示过少）</p></td></tr></tbody></table>

### 交互跟手

折叠屏展开态屏幕尺寸较大，弹出框上的操作按钮不易触达。建议针对折叠屏展开态、平板等大尺寸的设备，提供跟手的弹出框。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163708.85574344005197032449972445872067:50001231000000:2800:5EFE553308178BC4FB338659713FCDEAB2E984005117C276504B20C8FB0B19D4.png "点击放大")

### 横屏适配

折叠屏在展开态下的屏幕显示比例接近正方形，基于此特征，应用设计和开发时需要做如下考虑：

-   支持展开态横屏显示。
-   展开态横竖屏布局一致。除部分特殊界面外，建议应用在横屏和竖屏下保持一样的布局。
-   横竖屏旋转时，需要适配摄像头的挖孔区域，重要信息需要避开挖孔区显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163708.11034171862196533363031368382976:50001231000000:2800:F2765B8B573859185C9264993F48733A933A65C28F606128F2F55638C5BC345F.png "点击放大")

### 挖孔适配

在设计界面布局时，应确保其适应摄像头挖孔区域，以确保重要信息不会在挖孔区域内显示。

当设备处于竖向显示时，状态栏应避让挖孔区域；而在设备横向显示时，建议整列避让挖孔，对于一些固定且不会对内容产生影响的元素，如底部的标签栏，可以不进行避让。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163708.93801774026520928188696438605936:50001231000000:2800:806749C2974048E1C682AEDAE8C3958FB182AFD170FBC5B518A0F94CD523D2D3.png "点击放大")

### 文字适配

在折叠屏设备的展开态，图标和字体大小应保持与折叠态一致，以确保良好的可读性和用户体验。若确需调整，建议控制在1.2倍以内。单屏文本长度建议控制在36字左右，最长不超过40字。

<table id="ZH-CN_TOPIC_0000002352875141__table433mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row438mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p14816195274714"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163708.65190185857739574351821108067099:50001231000000:2800:28B34974215B6E64EDFF5DCB4DE5CB25FCC3B52A0ED6BC080609EB0F8730F2AE.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1618501712351"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.00574252075932607714427599202641:50001231000000:2800:3098BE640338FA82FA5CD29D31931EE199A62C6BC72855CA8443B33C56B08207.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p4181314448">推荐</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p82754484913"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.40582822553608800913493528785377:50001231000000:2800:18B6838842BF0D061680DAD439BE44F2009ECF0AF7A594A0692D00CB41AAC537.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p11646112153613"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.91667498191780160419374115456539:50001231000000:2800:2F9401C12C0E2D25931A0824D597A883A2C1C2337E625645DB19C5A488E1110D.png" title="点击放大" width="268.5" height="1.124607329842932"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p14337122012415">不推荐（字体过大导致一屏幕显示的信息太少）</p></td></tr></tbody></table>

### 图标适配

展开态图标大小不应发生明显变化，建议保持跟折叠态一样的大小。若一定要发生大小变化，则最大不要超过1.2倍。

折叠屏展开态入口图标显示主要有相对拉伸、挪移布局、延伸布局、相对拉伸&挪移布局四种方式。

(1) 相对拉伸：折叠屏展开后，入口图标数量不变、大小不变、布局不变，图标间距均匀变宽。但需要避免图标左右边距过大或图标之间间距过大。

<table id="ZH-CN_TOPIC_0000002352875141__table234465310355" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row33441353133517"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p173441538357"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.71819278660762066046025928756871:50001231000000:2800:4B06C4D2BEE7C2036623EFE4D552E0BFA1FF60B51C7AC2EB0D3DC422B33E7928.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p452531462010"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.31294650395097671088363346578937:50001231000000:2800:F6EB30CE46B0A91878EB13B82A9C33DFF8FE806E51F36F6A50BB4217C23C714C.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p912917491416">推荐（图标相对拉伸）</p></td></tr></tbody></table>

(2) 挪移布局：折叠屏展开后，图标使用挪移布局，入口图标3行变2行，横向平铺。

<table id="ZH-CN_TOPIC_0000002352875141__table0502161893716" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1950291813377"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p7502518103715"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.38234438338844927709689443243388:50001231000000:2800:22CDDBD30E3AC8241067FA5AF02DB07EE15845A56EB96721703A7F6591175BC1.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p650219185370"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.51674773327693536104131346211592:50001231000000:2800:0597EE839560F1780DBEEB80E5A3191A38E28CD99E4B1FFA54DB8C2494B2C198.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p2936102511519">推荐（图标挪移布局且适当调整间距）</p></td></tr></tbody></table>

(3) 延伸布局：折叠屏展开后，图标使用延伸布局，一屏内显示更多图标数量，用户可以横滑显示更多。

<table id="ZH-CN_TOPIC_0000002352875141__table599336153812" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row109931266380"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p59939663818"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.26172623602779362807081791326209:50001231000000:2800:E67305DD34409A7D6EA2A89F62820C996853C14ACE78C8C0389C2ECE88EA83B5.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p7993126153819"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.21024820013777184502155350125783:50001231000000:2800:A004FEFECF18FBAB0E616C65FBAF6EC2C06D9E616A613536673443E06E0BA2C5.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p887314519516">推荐（图标延伸布局且适当调整间距）</p></td></tr></tbody></table>

(4) 相对拉伸&挪移布局：折叠态图标数量固定时，折叠屏展开后图标间距相对拉伸，大小不变，建议文字部分进行挪移布局，图标在左，文字在右，以避免图标信息过疏。

<table id="ZH-CN_TOPIC_0000002352875141__table101071579394" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1010707183915"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p8107197113913"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163709.88775846802686710241887487362005:50001231000000:2800:E3D12624EB7DDF858DEB0D388437F89E6E1B59CA73FFDC9936C1E0DD81BECD74.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p9107972397"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.22321727696654173237316575505473:50001231000000:2800:F5550B752971E2B979653BED3DEF247735E00B2C1AE05746DB81FA97E67E565A.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p17776513664">推荐（图标相对拉伸&amp;挪移布局）</p></td></tr></tbody></table>

(5) 以下3种为图标适配中常见的显示效果不佳的案例。

<table id="ZH-CN_TOPIC_0000002352875141__table159781842143913" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row19781842153916"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1797854263910"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.11097927709641251215881678591256:50001231000000:2800:8C5637CB41CD6FEAE0864BF02312CC377CBFB89A10C8FE975C206616F6EC2D49.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p13304758133914"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.63209491255809234300999044645254:50001231000000:2800:273471C673E76A3E1CAA73AD5F0A3ADC8B843782CFABAEBA414E7730CCC01F71.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p129326301620">不推荐（左右边距过大）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table1450052164010" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row165055234018"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p350205254015"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.25971379285631412766299552857115:50001231000000:2800:9F172BFBBF40B04FC209FD08168BA7EEC46A3DC6C1D9BFD0FCB8AD4E39BF8155.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p165014523404"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.55954396083090630855283827761909:50001231000000:2800:FAC1962D8F4F54A1CF77BA14004B60CE97644DAF2E8054F110CD82CA8F77C73A.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1229155215612">不推荐（信息过密）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table20526183324118" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row175263339418"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p16526133134117"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.42088802809015421939331379387520:50001231000000:2800:D8621CC24073AC7C0797387EC10EDA69DAFD08124545D7F38CDCB543017093D4.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p145261633104113"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.47757290487554008972880744065074:50001231000000:2800:59BD560DBE1CBF53B033C38F0113CB670D36D919B52DBD7EED4B52CAE80EB767.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p17724137715">不推荐（图标过大）</p></td></tr></tbody></table>

## 组件适配

### 列表

(1) 相对拉伸：折叠屏展开后，控件元素大小不变，列表横向拉伸。

<table id="ZH-CN_TOPIC_0000002352875141__table5731519104210" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row127316199423"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p3738198421"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.92712641270295921286605056772878:50001231000000:2800:0C2D56553B6EAC85B74F941A90BEFF376A607C1FFB775180746E8F1818CC9405.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p53291444144211"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.29394350504373550268666030685236:50001231000000:2800:208E6DE7C3BF879574A51226CC4D691CB6BB8BD1A6642C0BF77E9BAD01C7AEC9.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p565933317715">推荐（列表内容相对拉伸）</p></td></tr></tbody></table>

(2) 重复布局：折叠屏展开后，控件元素大小不变，内容从单列变为双列。

<table id="ZH-CN_TOPIC_0000002352875141__table141841611114318" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1718451164318"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p71847110435"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.50361046739115009362088755910074:50001231000000:2800:FF9DCB64CA965DA4269E51CBC14461A82C4B12A4E98FBCCFFDCFE721065DF40A.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p418401116436"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.60018279101541420464558844354053:50001231000000:2800:AD1DC37C21ECA8F3B6C72919476313DB67684551FD6E490983E4598FA2B31479.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p20127756883">推荐（列表重复布局，单列变双列）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table059414508437" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row75941850154314"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p35941150144316"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163710.60882127149147029398887595735078:50001231000000:2800:527FD3FE7C5832738284C8BF8EA92C8200AA1B5B77A1A8E6CF2101867DC4996A.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p551965574914"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.80297596543633907140058668856210:50001231000000:2800:42D0307718542592B66E7BE0E1C4C66DD6E172530897EB2628F3AF080D19A9D0.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p159811151090">不推荐（边距过大）</p></td></tr></tbody></table>

### 组合控件

**顶部搜索框+子页签/其他控件**

(1) 相对拉伸：折叠屏展开后，按钮、图标等元素大小不变，间距横向均匀变宽。

<table id="ZH-CN_TOPIC_0000002352875141__table1554132124517" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row2554821104515"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p25541212452"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.39097960377093744282376387034215:50001231000000:2800:456AB0CD7134F8A167C48F520ABBB5448F10988549934244BFEB429BB53C442F.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p2554421114515"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.10503663833270873997837515984898:50001231000000:2800:AC11B19898698840F45682383079040E9D535CE96FAF22A7FFFA86B1E429B5D5.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p134711411390">推荐（相对拉伸）</p></td></tr></tbody></table>

(2) 延伸布局：折叠屏展开后，控件元素的大小不变，间距均匀变宽，可显示的页签数量增多。

<table id="ZH-CN_TOPIC_0000002352875141__table131061953154513" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row12106053164511"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p10106185313451"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.47350772006075376695664977949191:50001231000000:2800:700024B2993E0CEA8486DFB63BD9204D66B64C9220EA20E51ECE08A5090E468A.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1510695384519"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.54881982582453081240756917160954:50001231000000:2800:2995F457F940CD14A3949F2E69BA662BFB163B0D97BA57AF6D52E6A37190D902.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p3717111101012">推荐（延伸布局）</p></td></tr></tbody></table>

(3) 挪移布局：折叠屏展开后，由于横向空间明显增加，组合控件内的元素由原来上下排布的两行变为左右排布的一行。变为一行后，可根据优先级对内容进行先后排序。

<table id="ZH-CN_TOPIC_0000002352875141__table195649188465" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row75647183463"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1056441814462"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.26540156205265871471638154461661:50001231000000:2800:B7D09CF6879A7DAE1AE58EC0A04F68204678A224D2944B4C1E9B7C2FD64B85EB.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1856417185469"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.20735071303506624535743309680017:50001231000000:2800:CE954336F5E360B18087F0B480FABF985181CE247EBE9A6C397EBC9A9B2AD3DC.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1857232116107">推荐（挪移布局）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table34811451124617" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row18481195124617"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p15481251154616"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.77870714005212466476344601973453:50001231000000:2800:D366697CFD7CCE95CC127C500097C8144315C01702D5762547B4AC8ED999F112.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p4473126113113"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.49197828234437886517010158715361:50001231000000:2800:950E68C6CCECBE1C46AC050A7DA4C7BB047BFE6075DCFA2ED131442BCACB0781.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p117391639111012">不推荐（内容过大）</p></td></tr></tbody></table>

### 底部工具栏

延伸布局+相对拉伸：在折叠屏展开后，通过相对拉伸让图标间距均匀变宽，同时通过延伸布局来显示更多工具按钮。二级工具栏，同样适用于以上规则。

<table id="ZH-CN_TOPIC_0000002352875141__table37631037144718" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row476393784716"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p37631337184718"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163711.79723751071201643564817814174321:50001231000000:2800:AC16F4D3DE9F9CAC995BD1F6944B3619637F8D96A38CE3738A414FF76F3243B3.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p7763143704717"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.92893048470789684053400255848071:50001231000000:2800:EFD4A0F88784D893DFC6A6192B33D7E1F0F11C3D0E598919820C120D7C0AA1BC.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1285013209111">推荐（延伸布局&amp;相对拉伸）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table1155265810475" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row15552195819478"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1055211583477"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.60382051024177025542555923101600:50001231000000:2800:37C25BD0E754AFC3FA70A59A2720977CA3F86BFDB723B4F571DAC7B7A273181F.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1155216586474"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.75713906342361074061525770753080:50001231000000:2800:C6CFC995BC7D5E4961D07EA40B6B515964F247CD00740B8A21C39DCB950A6DCD.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p445220441117">推荐（一级和二级工具栏同时延伸布局且相对拉伸）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table1673810254487" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row8738725134814"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p173842515489"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.11198847781102039339301110991134:50001231000000:2800:ED534CBAA80EDB6B826A9D2672A31D79BDF5C72359401D11EB9AC3FF735E9012.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p4890184914311"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.22227233449423730719797420422523:50001231000000:2800:9187872EEDBD6B8C9D1BD31954DE8B7C115BA1368E2C5FA6B66EDF393AB8574D.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p843517211121">不推荐（信息过密）</p></td></tr></tbody></table>

### 运营类图片/视频/卡片

运营类的图片/视频等，通常有卡片和沉浸式两种样式。

展开态的图片/视频/卡片应适应页面的宽度、间距、列数等因素进行适配显示，不能造成信息量的明显减少或信息密度过大。

**居中的运营类图片/视频/卡片**

-   折叠态显示单张居中的卡片，折叠屏展开后，可横向延伸显示两张或三张运营卡片。

<table id="ZH-CN_TOPIC_0000002352875141__table21811732135012" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row3181153215501"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p19181133219503"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.50089669523978368905332852336594:50001231000000:2800:45AB6F982981F2AB342D0F99090EF44A8EB548096AA1DEA507EDB8055354DB0E.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p18181732105019"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.32635313599732622158580267788961:50001231000000:2800:EDC6FF240ACD3150AA53D51026B9B38EA3EACE2E789670649CB908A545228E39.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p148672165126">推荐（展开态显示两张运营卡片）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table14446183125119" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row154461316511"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p3446183195110"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.49978324789616288174244200528270:50001231000000:2800:809AB348FDAE87C96479FE8E5F7A6A637DA91166BD3058FB21B2B9A9F6C3C944.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p2044619385115"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163712.69322010154444162572844474405606:50001231000000:2800:7EBF341C24498C79A942480E2F0BDC5288D0241B6CD622203F51E476221C736B.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p6141135191219">推荐（展开态显示四张运营卡片）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table12575174118513" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row3575104115114"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p20575114185116"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163713.37192531612305218553691668316368:50001231000000:2800:AE03D977A39C127FDD3B7DC31BA839A1D8E43A25B1FFE72B12524B51B82D966E.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p4575104115514"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163713.66707967662484826828414088731042:50001231000000:2800:AC5E23F7205B4ADE74FA25696D074F0B7C173D37F41AE86CFCA84A731FD9FEEC.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1913195501210">推荐（展开态显示三张运营卡片）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table12232014115216" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1023221455210"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p9232101455219"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163713.94088300126019554532604693310597:50001231000000:2800:724D9DDA04005F12258C28A89A06717A40D8BDD0F7F61AA72BE436F4B36B23C4.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p10232114115219"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163713.61419078694566860618424946388437:50001231000000:2800:34A08B0243BF08648A8C59464BD1164C2760D7AAB426996AF4B5A6454EE70C9F.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p28041552131617">推荐（展开态显示三张运营卡片的创新样式）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table4405174455214" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row114051144105219"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p14051744105218"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163713.65951308706012605472863523660006:50001231000000:2800:B7ED7BE18F344AB64BC84D4C1569A406274CFE2173057B796FD1150A4E42499A.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p7405114411525"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163713.05968143470244455925609864717857:50001231000000:2800:4610B5D25DE578F07D9C67FCABF36D9B69BFA93BCBABBE46897A7920D14E447C.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1810291371715">不推荐（展开态运营卡片等比放大，且超过1/2屏幕高度）</p></td></tr></tbody></table>

**首页的沉浸式运营类图片/视频/卡片**

应用首页的沉浸式的图片/视频/卡片在展开态显示过大，是折叠屏适配中较为常见的问题。

（1）针对有多张沉浸广告图的，展开后，横向平铺显示多张广告图。

<table id="ZH-CN_TOPIC_0000002352875141__table13971323175313" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row097102314538"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p14979232534"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163713.79557273516691563324577233562340:50001231000000:2800:BF8ED537006D97E0EA1DD9AB10DB03847C74F4A19764482F5409E2C1BCFF3CD6.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p398162365313"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.50265401506747593290194287084073:50001231000000:2800:EE123CA2DBAE3C3F67EB35D8A0A57151A3D444EA54D11A3749458AEAF54C0DCE.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p5625132991715">推荐（一排平铺显示多张沉浸式广告图）</p></td></tr></tbody></table>

（2）针对只有单张沉浸广告图的，宽高比大于2∶1的沉浸式广告，折叠屏展开后，整体内容等比放大。

<table id="ZH-CN_TOPIC_0000002352875141__table12297153195315" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row16297115315531"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1929725312537"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.39756765471390443024948317094517:50001231000000:2800:AE5B7BEF24BC04E56D269A43DA1E831E9697C57EB424E7492FE2BD1A43E1CA4A.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1629795345310"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.84681259784514168107683449718496:50001231000000:2800:F3465D21C74B6FD4A93F0FD02D19CC3F9286E86D0BA2D03CD599F96FADF788E6.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p13309947151712">推荐（宽高比大于2∶1且只有单张沉浸式广告图，展开态等比放大广告图，确保不超过屏幕的1/2高度）</p></td></tr></tbody></table>

（3）针对只有单张沉浸广告图的，宽高比小于2∶1的沉浸式广告，建议将背景图和广告内容元素分层。折叠屏展开后，背景图等比放大的同时顶部和底部适当裁剪。避免裁剪到核心信息，同时确保广告背景图的高度不超过屏幕高度的1/2，广告内容的核心元素可适当放大。

<table id="ZH-CN_TOPIC_0000002352875141__table1656915319220" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row135697312026"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p756915311212"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.70331878911600093262863535702541:50001231000000:2800:A68C5CF54758F5C1D107D406213A2524F9FCCE53C5AF86D332654AC84BD03FB5.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p135691311521"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.87695918442453821278120611319872:50001231000000:2800:DC55DBAE44BEED88CDC1777DE2C13947F505C9714B61BA4EE2C7B0E9391E83A4.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p6722328181810">推荐（宽高比小于2∶1且只有单张沉浸式广告图，背景图进行智能裁剪，核心元素适当放大，确保不超过屏幕的1/2高度）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table2036181217318" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row2361151217313"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p43618124316"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.34880248357207357090493220745176:50001231000000:2800:1D81D8572B7B2C4C3F33E0E3371C6EFC082B6D367157702CD7EA4104D00C4D3C.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1347113485388"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.30190951881684165028478192885397:50001231000000:2800:1093B4F458791D6A7B4798BB10F3B25FC8875BD554C6F5E2CF539D36ADD7F415.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p111981049131817">不推荐（宽高比大于2/4且只有单张的沉浸式广告图，直接放大显示，展开态太大）</p></td></tr></tbody></table>

（4）针对有按钮、页签等控件的沉浸广告图，建议将背景图和广告内容元素分层。展开后，背景图横向撑满且高度不变，按原来布局基于响应式规则调整内容元素的大小。

<table id="ZH-CN_TOPIC_0000002352875141__table122181116419" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row62181411144"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p6218619413"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.68950741762167942114512987009916:50001231000000:2800:51B9AFBF4C6F2DE2EAA0EA7AA94045DCCCF68433F8246F0CB2AAED945088DDDE.png" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p4275178183912"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163714.09721004267933491683725099533795:50001231000000:2800:731C4FF93560DB6786C0D72A733269AC7B25BC16AD5C711D0CD714DA6BAC3E28.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p2742711111915">推荐（背景图高度不变横向撑满，广告元素自适应布局）</p></td></tr></tbody></table>

**详情页的沉浸式运营类图片/视频/卡片**

部分应用详情页使用较大的沉浸式图片/视频/卡片展示商品详情，用于吸引用户。在该页面，需要确保展开态时，广告内容能显示完全，且商品的核心信息不被裁剪。通常建议在展开态通过显示多张广告图来解决宽屏适配问题。

<table id="ZH-CN_TOPIC_0000002352875141__table1271172012511" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row5271320758"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1627122012513"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163715.48460188323396707573027154236962:50001231000000:2800:E97788241696F18E1229A14DAB7F163EF6FC8230AED55252B91CCA553D1EE363.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p22710201856"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163715.10750977008854266097694604539318:50001231000000:2800:5DF65BD6C9309DDE2B8F3FFE7F2DE01182E0D081FF19EA93454406121BFC97EF.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1865122916191">推荐（详情页的沉浸式大图，展开态显示两张沉浸式大图）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table66501753258" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row565110531510"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p265155310520"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163715.81036409366663757660091320655388:50001231000000:2800:8D9DE128A53899695B6EBF37FC059D540F076677BF5927FE8FB7B35D158ABD82.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p86571132103912"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163716.19719531303047583899434669231706:50001231000000:2800:D0A3CC4FD46C71AD91125337D2975DBF4251BD6F0038EC1EE5FA0D4DB9C433BE.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p177874916194">不推荐（详情页的沉浸式大图，展开态直接放大，图片显示不完全）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table4856142815613" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row185616281065"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p108561284610"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163716.40913497692091897767528140279063:50001231000000:2800:12C9B3EB345CC6462AFA51ACC672D8950DF5E1405DE4035A032E943582E755CC.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p28568281769"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163716.61197123133816424447959919839598:50001231000000:2800:F436949597B093DC5CAA9A37008A903528F50385EC67A21DC7535270C1EC597B.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p11276984203">不推荐（详情页的沉浸式大图，展开态直接放大，导致商品的核心信息显示不完全）</p></td></tr></tbody></table>

### 内容类图片/视频/卡片

折叠屏展开态内容的显示主要有瀑布流或宫格布局、信息流布局两种形式。

**瀑布流或宫格布局的图片/视频/卡片**

-   横向的图片/视频/卡片，在展开态建议增加1列。
-   竖向的图片/视频/卡片，在展开态建议增加1列或2列。
-   瀑布流或宫格布局的图片/视频/卡片，在展开态的列数至少不低于2列，至多不超过6列。
-   若该瀑布流或宫格布局的内容，在展开态不增加列数，则需要确保单个图片/视频/卡片的高度不超过1/2屏幕高度。

<table id="ZH-CN_TOPIC_0000002352875141__table6126151815106" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row121261118201015"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p14126918171011"><span><img originheight="1512" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163716.54188416311277834333135609620237:50001231000000:2800:2C15E50FF95D0801DDEA49050D94591AE09AEBCB25AE1C341C1A5C5C15B9EBA6.png" title="点击放大" width="587" height="240.39653304442035"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p186821012164016"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163717.98997786078712632614091596857461:50001231000000:2800:2EF38F3487253BF5A3E29F91E043F80E15FF0390A0805E92FBF9F279A7A36648.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p10831421202114">推荐（横向图片，1列变2列）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table15561251181012" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row175625181018"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p85617518106"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163717.54235042318999416592851788569916:50001231000000:2800:39DB8F5E5E15D37067C0505D6FF72C75A2F231BF64ACC7838EF9F8D9DA967851.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1956751121016"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163717.68677286113720765592383238689963:50001231000000:2800:2D906F9A1AD33D1D656A25E9C88F796BE0BB20EA43A0C8250B179DC6512D7F2F.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p15652036202118">推荐（横向图片，2列变3列）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table3583114751118" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row75831847201110"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p758334791120"><span><img originheight="1512" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163717.62851729341734386579529259387190:50001231000000:2800:C5ECE4029E2DBE81B6B8D59DE1DFCAD5D5BFF07AF9556B8F88657DC79351C915.png" title="点击放大" width="587" height="240.39653304442035"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p185831047131118"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163717.03275594415359721106885481742708:50001231000000:2800:68A8B96070B026A225667B9697609A6780B37394F04A73A97CC10503C6481720.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1296115022116">推荐（竖向图片，2列变3列或4列）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table17865104015125" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1886544011124"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1865184010124"><span><img originheight="1240" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163717.94431483617511424064435143582741:50001231000000:2800:CDE7E30A7D9DB58CC35F6B1044A8DFCD49AE729448ACCB6B24D446E3CB271B66.png" title="点击放大" width="587" height="197.15059588299025"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p148651409125"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163718.76920614322923630931194649883668:50001231000000:2800:CB736582906469B250272C48DB409F6F9AA0787B29828BD71E70AEFDAEC1358A.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p4382989225">推荐（横向图片，3列展开后还是3列）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table12240123817130" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row11240203816135"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p17240538131316"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163718.34083291114923351660752867953409:50001231000000:2800:C60DDDE1A04C1CD7A3AAA6D71C3BE4C4C7E050386C015DF7F14310FC94EC5FDA.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p116951939417"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163718.71360393255231242327557039430574:50001231000000:2800:40397C30E0D6B7B8548D9740C8A13F1DC5314BFC029BEA5718E4651BB5776CD3.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1170122311228">不推荐（单列展开后还是单列，单张图片高度过大）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table1634310172145" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row123436178147"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1334341771416"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163718.01862139177109003956283740427997:50001231000000:2800:3DB32FF8C5CA97F94327B0041FA03DC223880D03CC1949592C0AC8C878C4BF8C.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p103431917201415"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163718.40833918993084174680890690351016:50001231000000:2800:E611831694C421B3A54EF80A80B23A10BCDCAFBC221B6D00544ABCEB2EE54E4D.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1932412426225">不推荐（3列展开后还是3列，单张图片高度过大）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table17534164014143" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row16534940121411"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p15341440171419"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163718.95191896011519309986825245249095:50001231000000:2800:6B59B13B2B47EEB74DC4FE92C5C06F968052C1B4F8221BE37750A3FF0A8CD710.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p145341540111417"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163719.31820171460637693743378308628998:50001231000000:2800:A7FA3000D1B8F028DC7131A0DA156756434E251E8B981F9C7630157F2C8CBFD1.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1375917223">不推荐（4列展开后变成7列，信息过密）</p></td></tr></tbody></table>

**社交类信息流布局的图片/视频/卡片**

此类信息流布局，从折叠到展开需要重点考虑图片/视频/卡片的适配，并区分首页和详情页两种情况。

首页或该页面有多条信息流的：

（1）9宫格聚合图片/视频/卡片，建议不低于1/2屏幕高度，不超过60%屏幕高度，约为55%屏幕高度最佳；

（2）单张横向或方形图片/视频/卡片，建议不低于1/3屏幕高度，不超过40%屏幕高度；

（3）单张竖向图片/视频/卡片，建议不低于1/3屏幕高度，不超过60%屏幕高度，约为50%屏幕高度最佳；

详情页或该页面仅极少条信息流内容的，信息流中的单张图片/视频/卡片或多张聚合的图片，高度建议不超过屏幕高度的60%。

<table id="ZH-CN_TOPIC_0000002352875141__table87072532152" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1370716533151"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p67071853121519"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163719.49793323650610719705098749910354:50001231000000:2800:AA79416A0F8489A120CB43977F44E0FD01539D6D14F64034BC8FC37F734E2662.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p18973104194118"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163719.84532039765962699932244059147326:50001231000000:2800:E618C440A4485692AD3F47400A0031F86FAB7286FB59182852D4075BA3AF3BE8.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p14295823102317">推荐（首页聚合图，不低于1/2屏幕高度，不超过60%屏幕高度，约为55%屏幕高度最佳)</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table17455521615" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row274535211615"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p5745552266"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163719.39971866393146799169444907299164:50001231000000:2800:11C39BDD161CD67A852D4B3590C85BF9D1F05CC6F782B663DE866A940CD4419A.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p12745125214617"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163719.25708569443416091700740116017633:50001231000000:2800:FA4093000D954F1B569A4650DD95E59AD181725FC4D82E9C91CCCDF5499906F1.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p203248571535">推荐（详情页聚合图，不超过60%屏幕高度，动态的完整内容一屏幕显示完整效果最佳）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table1761115252168" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1611192551616"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1061192571614"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163719.11551386423519696217835770992749:50001231000000:2800:BE421B89AFE07CE4A19D39CB42EC0ABAA1466DBFA535EAE79D244FC32EB53C66.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1461262581617"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163720.89289460755296227673875358376955:50001231000000:2800:37EDE891D1CDDDFEC3E6264D42A71F29D19B2D0F79F1BBA535E4121844AAB9ED.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p716923842311">推荐（首页横向图，不低于1/3屏幕高度，不超过40%屏幕高度）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table5457713171719" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1345715132176"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1545731312177"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163720.69467250434128459251003889710760:50001231000000:2800:A3C728BDCB69CA815DC34CDD4F8180DC499FFBB17659A240454E060081D7A0B2.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p8457413201714"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163720.68537993050062861581228959900088:50001231000000:2800:92A776BC79F1F2347A0ACFFADA08BBC5746ECD44446D7505C2F8A3D9708351DC.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1425314132411">推荐（详情页横向图，不超过60%屏幕高度，一屏幕显示完整效果最佳）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table51903381073" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row18190538678"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p16190113815716"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163720.79509079417519261902138373828173:50001231000000:2800:8587012FBE9F0A1048951327A2A645BD0DABF15AB8172BFCA731A3AFA57C0986.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p101907388714"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163720.71138529654508476642867707161644:50001231000000:2800:907671828DD3EA957F387F58A2B482BEE1A2A2F83ACBC69E4DAD34EC5FA5739F.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p16315447153015">推荐（首页竖向图，不低于1/3屏幕高度，不超过60%屏幕高度，约为50%屏幕高度最佳)</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table185418581184" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row6854165818189"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1485420583185"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163720.62545151951623442334778780546221:50001231000000:2800:D7D3EE533026FA146520ED1467B8A91DBF6814B76D7348C68C8C2D47FCF6E18C.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p2085455881818"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163720.87495860227825112037083066593530:50001231000000:2800:BED2C03221A8B2EBCDAA32D5193F4605E9B30E1BC53809448F631F0966763EE8.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p56711219242">推荐（详情页竖向图，不超过60%屏幕高度，一屏幕显示完全效果最佳）</p></td></tr></tbody></table>

**新闻资讯类信息流布局的图片/视频/卡片**

此类信息流布局，从折叠到展开需要重点考虑图片/视频/卡片的适配，并区分首页和详情页两种情况。

首页或该页面有多条信息流的：

（1）单张方形或竖向图片/视频/卡片，建议不超过60%屏幕高度；

（2）单张横向图片/视频/卡片，建议不超过40%屏幕高度；

（3）有多张图片/视频/卡片时，建议平铺显示。

详情页信息流中的图片/视频/卡片，建议不超过60%屏幕高度，有多张连续的图片/视频/卡片时，建议其横向平铺。

点击图片/视频/卡片后，全屏显示图片/视频时，需要确保默认一屏幕内显示完整的图片/视频内容。特殊的超长广告图除外。

<table id="ZH-CN_TOPIC_0000002352875141__table15238112531915" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1123852511195"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p12381125161917"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163721.06742563473302580187706509145288:50001231000000:2800:398947FD6480BA24CA59AAE9347B668C0A269848712115FA5976781DC07372B1.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1523852541916"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163721.05710945276639758297082506160375:50001231000000:2800:39C3E607477A965B7E1B718969DCA7B0AF04AC2E844C7FF5F0908CFD090EF6FB.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p13823972414">推荐（信息流首页，横向平铺显示更多图片）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table1811705314198" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1511814536193"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1111818531197"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163721.10096236272971822584237541199428:50001231000000:2800:3D006423C79DB12E2B5760C4CC894CB89A47248AD424C1E5A05BB4882167CAF7.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p411855321920"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163721.53889114594963815665525794520250:50001231000000:2800:AE8A80F6F4B7DA35FD44BD39D9F631B749AA92B65416D48511BABAAA7F91F0DE.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p2044965613245">推荐（信息流首页，图片文字分离，进行挪移布局）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table19728112322017" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row19728023102012"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p172892342017"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163721.44506433900468895173237872731053:50001231000000:2800:C0D68D1BF8BE3B1D02910873495D728B47E495FCC16A8E4A7C6FEE2E34BAECE5.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p3957459194220"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163721.54308807186705470678894312437828:50001231000000:2800:1394C5D54123E286473A068177B256C20D20A26CF3FC8B655CD4D123966124B6.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1217419151252">不推荐（信息流首页，图片直接放大显示，超过40%屏幕高度）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table1578255912012" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row278245912015"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p177821459102012"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163721.62899191961395976290398006599786:50001231000000:2800:C55DD3B8467BB0E809194850F67A0D90CFA21C76C60D03EBDCBAAE418C9AE835.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1422083073919"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163722.64060414227456113734160461113165:50001231000000:2800:C0E249F60272B9DC3A360959E08179435BE035843524F7CE5BEEE86BB827DE9B.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1074963114259">推荐（详情页，横向平铺显示更多图片）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table846033412211" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row16461434142111"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p046110347210"><span><img originheight="2040" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163722.42787498161394386516367827565999:50001231000000:2800:10DB06BDC9746FBDB6A98D3610C6C14C749B172E97ECD7F4C8F48A2C0966BD09.png" title="点击放大" width="587" height="324.34452871072585"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p15251192534313"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163722.44828665791218766719213310058401:50001231000000:2800:32C97339F2DD827E0DA91DA427F3BD5A49F5FDEDDB97F2D5AEA3594515EC4896.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p15757655152518">不推荐（详情页，图片直接放大显示，超过60%屏幕高度）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table147191050229" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row12719859224"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p97191452222"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163722.25753757236514070846097210301333:50001231000000:2800:609D4831EBE59E1F7E3AC760E6A1966B8D30B35AF6BAB775551164EFEC8A60EF.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p6719554224"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163722.60702896398603175400421488304111:50001231000000:2800:28C4064EA1F393B255C6B3413F13C7B2383DBE2949688673EC34E79C0EE0D97C.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p6613171420266">推荐（点击查看具体单张大图时，默认图片不超过一屏幕高度）</p></td></tr></tbody></table>

### 弹出框

弹出框在应用设计中较为常见，例如红包、广告等，建议展开态和折叠态弹出框保持相同的大小，或大小变化最大不超过1.2倍。

<table id="ZH-CN_TOPIC_0000002352875141__table1251465882212" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row105141258162215"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1051416586229"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163722.24635926030940816047055379857624:50001231000000:2800:CF80D46DD0B269A1FBA30B3BE503B9C2DCF992990F36F43E92EDBFF935E10AD9.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1951405802213"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163723.01567987346198878443040195049483:50001231000000:2800:A3C5BA50D28339547488F309118BC92C22B01B7B2C2ED90C9A883AD69B851BD7.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p9115930202612">推荐（弹窗大小不变）</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table5220163022318" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row1622013017236"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p15220183015237"><span><img originheight="2134" originwidth="3692" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163723.42380830397081708211055025783296:50001231000000:2800:C3E5FB87E5451DBD90C1618EE1FFA5A35A657A19B766907BD9B2D9EE11765240.png" title="点击放大" width="587" height="339.2898158179848"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p11388111994415"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163723.53233801047982283565003996108263:50001231000000:2800:1DC8A6C1925F3967A5743281D5C6011A6A250B05BD420FC363F95327DE0328B2.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p1598145019268">不推荐（展开态弹出框过大，导致显示不全或无法交互）</p></td></tr></tbody></table>

### 其他控件

页面中的其他界面元素，例如按钮、输入框等，建议展开折叠时高度按照字体大小的缩放比例进行缩放，或大小变化最大不超过1.2倍，宽度根据元素本身的响应式规则进行设计，部分元素（例如按钮）保持等比缩放，部分元素（例如列表、输入框）对宽度进行适当延伸，最宽不超过整个窗口的宽度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163723.22683890871340845382777366422114:50001231000000:2800:DF536F07BDC266589D48907ED4CF23C6B44C52E1379581EE92E0495EEB09D66D.png "点击放大")

## 开合接续

在折叠态和展开态切换时，应确保页面不发生跳转，焦点不发生偏移。

### 页面不跳转

展开态不应出现页面跳转、操作步骤增加，操作更复杂等体验下降的情况。

不应破坏应用内原有的沉浸式体验，避免仅仅为了扩充内容，或强制应用分屏而过度改变用户体验和用户习惯。

在折叠态和展开态之间切换时，需要保证当前任务的连续性。切换前的任务和相关状态应能够保存、延续或快速恢复，以提供连续的用户体验，避免出现闪退、重启等异常情况。

-   页面内容，均需要支持开合接续；
-   弹出层控件，且点击周边空白区域自动关闭的，可以开合不接续，例如弹出框、toast 等；
-   半模态控件需要支持开合接续。

<table id="ZH-CN_TOPIC_0000002352875141__table19734191382410" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row67341113182411"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p16734151319247"><span><img originheight="2160" originwidth="4320" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163723.44051743327785399314817177183780:50001231000000:2800:1F9041CFF015142DDE8A13A60C11C833BC5036BF6B98D79370AE3D4F1B8226E3.png" title="点击放大" width="587" height="293.5"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p153221933184412"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163724.59187926127222169253436034407501:50001231000000:2800:4137C9F60AB07306036A388673A2EFB0475C11487D72C888C92E699DCBE038DB.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p2761913142717">推荐 (拍摄状态和参数不变)</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table3599103312249" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row115991833202413"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p1559918334245"><span><img originheight="2160" originwidth="4320" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163724.80693444245227976405455197843368:50001231000000:2800:B6A862C396289CAD77D63128B5492F19192AC536651715040DA1F6E3633BC017.png" title="点击放大" width="587" height="293.5"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p16599233182418"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163724.76374605265337466152223127448471:50001231000000:2800:4334DCEBAB74B906046A378CDB08A316BEAE4524A1777936C40E4B4C3D1329A0.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p5496729132717">推荐 (阅读的焦点不偏移)</p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000002352875141__table35658532511" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row115659582517"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000002352875141__p65651253252"><span><img originheight="2160" originwidth="4320" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163724.21823882826860707479220821683647:50001231000000:2800:8626E49C982972B96B9314609596B020BE1A078FB12EBA3C58E751EC8F823A0F.png" title="点击放大" width="587" height="293.5"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p4259498456"><span><img originheight="8" originwidth="1910" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163724.90795199213035487275854696911778:50001231000000:2800:47FA67485556DF268583BB85D08A6D6C40D0C82182A30CBBA70A8951A44BE046.png" title="点击放大" width="587" height="2.4586387434554973"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p866017444276">不推荐 (页面跳转，任务中断)</p></td></tr></tbody></table>

### 焦点不偏移

当有足够多的显示内容时，第一个完整的信息作为接续的起始位置，例如下图的卡片 7 作为接续的起始位置。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163724.64528298025484992154250687038666:50001231000000:2800:B74350F964BF8CB1737441349C50BA774D89814D033251737F57F9ADA8310C9E.png "点击放大")

当显示的内容不足一排时，以当前态看到的第一个内容，作为另一个状态的起始行内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163725.47562678799112482265886384300972:50001231000000:2800:9DDC1B93481B9D5B70F83BF805FF1192BC1EC7D7410C87181D143A0A37C88FF1.png "点击放大")

支持左右横滑的内容，开合接续时，左侧第一个完整的内容作为另一个状态的起始位置。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163725.77193133627866602297507025195469:50001231000000:2800:F39E12698791A6F18C91545EF698F2A64CD97F13B8E7C3ED739891872D33B591.png "点击放大")

当支持左右横滑的内容，在另外一个状态遇到末尾数据时，右侧内容填满。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163725.77045611955694213062193947949129:50001231000000:2800:82D617441B7E73EE5209606FD2067BA4BF628C67875D290E5FDB45AB3550D60E.png "点击放大")

## 交互架构

在大屏幕设备上，双页面同时显示为用户提供了创新的操作体验。当应用程序中的两个页面存在关联关系时，可以考虑采用组合页面的方式。根据不同的场景需求，选择合适的页面组合关系至关重要。组合页面主要包括以下三种类型：层级关系、主从关系和并列关系。

### 层级关系

层级关系可以分为多层级和单一层级两种类型。层级关系的双窗口展示方式通常被称为分栏。

**多层级分栏**

在多层级分栏结构中，存在一个完整的多层结构，例如复杂的系统设置菜单、海量内容（如综合电商的商品、视频、图片或音乐的媒体资源、新闻网站的海量新闻）的门户及多级分类子页面。

这种交互方式的特点如下：

第一级的基础分类通常以列表形式呈现，以便用户能够快速了解整个结构的概览。

末级列表页面中的元素为最小内容元素，例如单个商品、单个媒体素材、单条新闻等。这使得用户能够更方便地访问和操作具体的信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163725.44295030034686512834720968384409:50001231000000:2800:7C50F2C4C84D8287B0A1BEE90EE69CA1ADD2291A4B1C85FA183E1EC8F0A419D8.png "点击放大")

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

245

有多个层级递进关系的场景示例

**单一层级分栏**

单一层级结构通常采用“列表+详情”的形式展示，其中列表中的每个元素均为末端元素，不包含二级分类列表。这种结构适用于邮件、信息、备忘录等类型的内容元素列表。此类交互的特点如下：

列表中仅包含独立的元素，无子列表，左右两侧内容属性固定，有助于减少用户迷失。

用户点击左侧列表中的某个条目时，右侧将显示对应的详情内容。

用户可通过在左侧列表中点击任意一个条目，快速在右侧打开对应的详情内容，实现内容的快速切换。

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

202

### 主从关系

在主从关系类型中，一侧的主导页面为沉浸式场景，而另一侧的辅助页面则呈现评论、互动讨论、参考信息等相关内容。根据沉浸内容的情况，主从关系可以分为左右或上下的组合页面结构。

主从关系的交互逻辑特点如下：

两部分之间相互独立，且具有明显的主从关系。

辅助侧依赖主导侧存在，若主导侧关闭或切换，辅助侧页面不能单独存在，需同步关闭或切换。

主导侧的内容呈现不受打扰和中断，持续保持最佳的沉浸状态。

辅助侧的内容用户可以进行滚动浏览，适合于信息流数据，用户可参与互动。

主从关系的信息架构样式主要有以下几种，应用可根据具体场景进行选择：

**悬浮面板**

从属信息默认以悬浮面板的形式显示，通过特定按钮或特定手势交互触发，一般用于作为主要信息的筛选项或更多菜单项，不影响主要信息的展示。

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

208

短视频应用使用悬浮面板的示例

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

172

导航应用悬浮面板的示例（折叠屏展开后，悬浮面板不拉伸，不遮挡底部主要信息）

**侧边栏**

从属信息默认以边栏形式显示，通过界面比例和视觉效果表现从属关系，不影响主要信息的展示，同时能快速浏览或操作从属信息。

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

194

短视频应用使用侧边栏的示例

### 并列关系

在并列关系中，界面中的两侧内容具有同等的重要性。这些内容可以是同类型的内容，也可以是不同类型的内容。

例如，在购物应用中，下单前对两个相似商品进行详细对比的页面属于同类型内容的并列；而购物应用中一侧窗口显示商品信息，另一侧显示与商家的对话界面，则属于不同类型内容的并列。

并列关系有助于用户更详细地比较两个商品的信息，或进行更高效的交互操作。在这种组合页面中，左右两页面之间不存在主次和从属关系，页面分割比例应为1:1。

<table id="ZH-CN_TOPIC_0000002352875141__table386mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row391mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="49%"><p id="ZH-CN_TOPIC_0000002352875141__p1935453912218"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163726.34885716547627298387071032352280:50001231000000:2800:1ECE6E97D994EB2AEF85E66D6291D01AF29C3958F6CB587000E129E642233C01.png" title="点击放大" width="262.13" height="196.5975"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="51%"><p id="ZH-CN_TOPIC_0000002352875141__p65801158132120"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163726.62549897028544865472969742286861:50001231000000:2800:CFC57006FBD2693C3576EEAD68B32AB4DA5A056A6DC17C42D4B9BAF731A2EFC4.png" title="点击放大" width="274.87" height="206.1525"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002352875141__row393mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="49%"><p id="ZH-CN_TOPIC_0000002352875141__p395mcpsimp"><strong>相同类型内容的页面并列</strong></p><p id="ZH-CN_TOPIC_0000002352875141__p397mcpsimp">两边有相同的页面布局、各段信息相互对应</p></td><td class="cellrowborder" style="border: none;" valign="top" width="51%"><p id="ZH-CN_TOPIC_0000002352875141__p399mcpsimp"><strong>不同类型内容的页面并列</strong></p><p id="ZH-CN_TOPIC_0000002352875141__p401mcpsimp">两边页面布局和内容不同，但相互间有关联性</p></td></tr></tbody></table>

## 响应式布局

随着屏幕设备规格的变化，界面中所呈现的信息量有增加，常见的响应式布局的表现形式为：相对拉伸、相对缩放、延伸布局、挪移布局、重复布局、瀑布布局等。

### 相对拉伸

布局特点：页面内元素的显示宽度不是固定值，而是通过相对参照物的方式来确定其开始和结束的位置。当布局的显示大小发生变化时，元素的显示宽度随之发生改变。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163726.86814094477442340841720815146942:50001231000000:2800:BE9E2199D0B4B0FE0B95295C6198883C4CC76F42EC486A3A7D5BCDFE1EBD06F9.png "点击放大")

### 相对缩放

布局特点：布局内元素的显示大小不是固定值，而是通过相对参照物的方式来确定其宽或者高的参数。当布局的显示大小发生变化时，元素的大小随之发生缩放。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163726.84317398953584389629979052074073:50001231000000:2800:5CA5C4E5F75A7ABBFC488497C51271369D6EC78303D53B4A88131F01720FA05F.png "点击放大")

### 延伸布局

布局特点：组件内元素横向布局，元素间的距离固定，可显示元素的数量可随着显示宽度的改变而变化。

适用场景：内容呈现型界面，单页面内信息架构扁平，内容元素为单层列表或分组列表结构，例如内容门户网站首页面。

适配规则：保持页面元素尺寸或间距不变，随着屏幕宽度的增加，在横向显示更多元素。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163727.81375864106694497059558599800267:50001231000000:2800:491B246AACA7F3A1A9CBA31EE96E173D5B3C2FF36A16512E6E5F71B862E7665C.png "点击放大")

### 挪移布局

布局特点：布局内的元素根据布局的宽度来选择是上下排布还是左右排布。

适用场景：页面内信息架构层级少的，例如门户网站首页面、内容详情页面等。

适配规则：首先判断布局区域是否有明显的“宽高特征”，即横纵比是否大于4:3；其次判断横向宽度，是否能容得下若干个元素，如果容得下就左右排布，容不下就上下排布。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163727.82286691200789971954515933902617:50001231000000:2800:7366029B61232FB95679C19ED92C30371B8757DB7436616CE2C6BCC0F80CA3CE.png "点击放大")

### 重复布局

布局特点：利用屏幕的宽度优势，将相同属性的布局组件横向并列同时排布。

适用场景：内容运营类列表信息，例如歌单列表、应用列表等。

适配规则：可以定义单个元素的宽度规则，随着屏幕宽度的变化，⾃动计算可以重复的元素的个数，满足宽度条件时横向重复排列。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163727.37046773350892814053654434985096:50001231000000:2800:C9F314C9301BFF22C57A4D900E16EC82B7ACA5134D4BFCC7E1DF0A64743E5B85.png "点击放大")

### 瀑布布局

布局特点：利用屏幕的宽度优势，将原来单列纵向布局，拓展为两列或多列的纵向布局。

适用场景：适合用卡片呈现内容的场景，通过卡片的横纵扩展在⼤屏上展示更多内容。

适配规则：可以定义单个组件的宽度规则，随着页面宽度的变化，⾃动计算可以重复的卡片个数，满足条件时横向排列更多卡片。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163727.10221490335576602995185650255407:50001231000000:2800:FE66962F5AF6295DA0A6AE2DEE1BC456179A6B7D734FC87758F2E5CA1CB9A37E.png "点击放大")

## 布局&交互创新

结合六种动态布局规则，三种双页面交互架构规则以及多窗交互规则，在折叠屏上可以进行多种布局样式和交互的创新设计，以下为一些参考范式。

-   分栏布局
-   挪移布局
-   重复布局
-   瀑布流&宫格布局
-   临时双窗

### 分栏布局

分栏布局是一种具有层级关系的左右分窗口设计，其主要目的是在宽屏设备上实现良好的视觉效果，从而提高用户的任务处理效率。这种布局方式特别适用于文件管理、联系人、设置、备忘录等应用程序的展开状态。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163728.36871135856356688558897773412900:50001231000000:2800:ECD2930177645CDCA018EC407B2110F4859D41EC4B669281AD3A63568F500C3F.png "点击放大")

备忘录的分栏布局示例

### 挪移布局

通过调整折叠屏设备的布局，从折叠状态到展开状态，可以实现布局的挪移变化，从而提高阅读舒适度和浏览效率。以下是四种常见的挪移布局用法。

**范式1：将不同页面的内容整合到同一页的布局调整。**

**边看边评**

在阅读时，展开状态下同时显示文章详情和评论列表，满足用户在阅读文章的同时查看评论的需求。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163728.33818097825956786735390495831748:50001231000000:2800:C727CFE13F1AF6E465372F3A742003942F45126A634760A22C2B5D329D0E5498.png "点击放大")

边看新闻边看评论的示例

**范式2：同一页面的上下结构内容，变成左右结构的挪移布局。**

**杂志排版**

本范式常用于阅读场景的图片和文本之间的挪移布局。不仅能解决图片过大的问题，还能通过杂志化布局带来更好的视觉效果。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163728.09640829229675528027651039374972:50001231000000:2800:10159BE6FCEDD03F315090A7D3668E69D00364622BD892C192245D17BC73CA5A.png "点击放大")

同一页面的新闻，从上下图文变成左右图文的挪移布局示例

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163728.48120649937404214181524534390787:50001231000000:2800:1F31805023D93B7949F701EF0AFAAE189866C958690E818DA24E4421DEB3F557.png "点击放大")

同一页面的生活服务信息，从上下图文变成左右图文的挪移布局示例

**范式3：有层级结构的图文内容，变成左右结构的挪移布局。**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163729.87099931399352789186713337108625:50001231000000:2800:D845339C7F92D0ADD08013091B2B0E9C1D42ED7B95EA0DCCD866FEE1B262B9D8.png "点击放大")

首页的图文内容，从层叠变成左右图文的挪移布局示例

**范式4：通过挪移布局，在展开态上减少次要信息对核心信息的干扰。**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163729.37194327366828832535941140954428:50001231000000:2800:0F93389CDA6B9745005B0B1D9673947ABC44FCF6BD504416CE13BB9FA099E0DF.png "点击放大")

看视频时，弹幕和操作按钮挪移布局到周边空闲区域的示例

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163729.80023601802258043174872288039504:50001231000000:2800:E3FE9D0DFF9556281C77A39EC4991DAD405D334FC2514EC279CB36DD15424790.png "点击放大")

多人视频通话时，参会人信息从底部挪移到展开态的侧边，减少对视频通话画面遮挡的示例

### 重复布局

折叠屏设备，从折叠到展开，页面内的列表、卡片等均可通过重复布局，横向展示更多信息，提升页面的浏览效率，同时避免信息过疏。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163730.88142941885525075912319935363062:50001231000000:2800:688728428337179DB3FB7D468C780197B9EE591A4963E557C52F7F91DAE3ADEB.png "点击放大")

列表在展开态重复布局的示例

从折叠态到展开态，使用重复布局时，通常内容按照从左到右的Z字形排布。

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

139

卡片在展开态重复布局的视频示例

### 瀑布流&宫格布局

瀑布流布局适用于卡片式结构。折叠态的单列卡片，到展开态显示双列卡片，不同高度的卡片形成错落有致的瀑布流布局。可以有效提升页面的浏览效率和可视化效果。

新闻首页卡片瀑布流布局示例

瀑布流布局和卡片的重复布局比较相似，内容也按照从左到右的Z字形排布，卡片的高度可以不同。

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

147

视频卡片从折叠到展开态的瀑布流布局示例

宫格布局的应用，从折叠到展开建议显示更多列数。一般在展开态横向显示3列效果最佳。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163730.94816582636859563668623156843043:50001231000000:2800:E99670000427F871BAECFF2B7D684A8440EB6F31F3C8BF07636A5E5F53CD9BC9.png "点击放大")

从折叠到展开态增加列数的宫格布局示例

瀑布流布局或宫格布局的页面，建议可通过双指缩放进行布局调整，从而满足不同用户的高效浏览或大图浏览等不同诉求。

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

114

双指缩放进行宫格布局调整的视频示例

### 临时双窗

播放视频或购物类场景，通常使用临时双窗口来实现“边看边评”或“边看边买”的体验。

**边看边评**

播放视频时，点击评论按钮，在不影响视频播放等核心任务的前提下，为评论留出足够的空间，从而实现一边看视频一边看评论或边看边写评论的体验。

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

149

看视频时，点击“查看评论”按钮，核心内容被向左推挤，在右侧窗口显示评论信息的示例

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

117

播放视频时，点击“评论”按钮，核心内容被向上推挤并缩小，在下方的临时窗口进行评论输入的示例

在同时显示视频和评论的视频详情页面，建议通过上下拖动进一步调节评论区域的大小。

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

109

向上拖动评论标题区域，视频内容被向上推挤并缩小，留出更大区域显示评论的示例

**边看边买**

在电商或生活服务类应用中，经常需要一边浏览商品信息一边和商家进行沟通，可通过临时双窗口实现一边浏览商品信息一边和商家交流的体验。

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

131

购物时通过临时双窗口和商家对话的示例

在播放视频或阅读文本等信息时，遇到需要购物的场景，可通过临时双窗口完成购物过程，确保主任务不会被中断。

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

87

看直播时通过临时双窗口完成购物及支付的示例

## 多窗口交互

折叠屏设备因其大屏特性，天然具备多窗口适配的优势。这种多窗口交互方式能够显著提高信息处理效率，特别适用于需要同时处理多个任务的场景。通过充分利用屏幕空间，用户可以实现多任务的高效协同，从而显著提升工作效率。

### 悬浮窗

可通过悬浮窗显示需要临时使用的任务，全屏显示需要长时间使用的任务，从而实现任务的短暂并行或快速处理。实现临时任务处理。

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

162

示例：调出支付悬浮窗快速完成支付，避免页面跳转

### 分屏

分屏功能适用于需要同时运行两个应用的多任务场景，支持左右分屏和上下分屏两种样式，在大尺寸设备上可提供无遮挡的高效任务并行体验。例如，用户可以边逛商品边比价、边看视频边聊天、边学视频边记笔记。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163730.29938562515444780958579540272752:50001231000000:2800:9C8B86B1099B131C8DC364708A23FD2AA7F18C79B3CC4A392468D1B3DAB3DFC3.png "点击放大")

示例：边看视频边聊天

### 跨屏拖拽

在形成分屏或打开悬浮窗后，用户可以从一个窗口内拖拽内容到另一个窗口。这个功能支持内容的跨应用传递，例如将文字、图片、视频或链接从一个窗口拖拽到另一个窗口，从而实现高效的内容交互，进一步提升多任务处理的效率和灵活性。

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

137

## 悬停态

折叠屏产品支持独特的悬停态，即产品半折后立于桌面，实现免手持的便捷体验。悬停态适用于无需频繁交互的场景，如观看视频、视频通话、拍照及听歌等。

### 悬停态适配

悬停态时，持握和放置状态下，手指最舒适的操作热区均集中在下半屏，而上半屏的可视角度更加友好。

悬停状态下，屏幕按照交互的难易程度，可分为以下四个部分：

1 易操作区：在此区域内，手指交互操作稳定舒适，一般在此区域放置关键交互操作，例如按钮、拖动条等；

2 不易操作区：在此区域内，手指交互时不太容易直接触达，需要更多地伸展手指或发生持握方式的变化

3 难操作区或显示区：在此区域内，执行触屏交互容易导致设备不稳定，一般不在此区域呈现交互类控件，或将此区域作为显示区，呈现浏览型内容，例如图片、视频等；

4 无法操作区：该区域一般为设备的悬停夹角区域。该区域操作精准度低，且显示内容容易变形，应尽量避免在此区域放置交互操作或显示重要信息；建议在上下半屏分别预留一定的空白区域。

<table id="ZH-CN_TOPIC_0000002352875141__table416mcpsimp" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002352875141__row421mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p7761154917406"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163731.14607146261060290724348734909241:50001231000000:2800:3185055BB9983934D8DD0211536C44F37071ED8529F9BDD0B16C63FB9B42C40B.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p422mcpsimp">悬停态双手持握</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002352875141__p167314224112"><span><img originheight="2160" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163731.96860471353505801493789286605733:50001231000000:2800:789288A9BC55053C1928267271A35EE10C1FD73F3332F6A108388A3769F0F26E.png" title="点击放大" width="268.5" height="201.375"></span></p><p id="ZH-CN_TOPIC_0000002352875141__p424mcpsimp">悬停态半折平放</p></td></tr></tbody></table>

### 悬停态折痕避让规格

悬停态时，中间弯折区域难以操作且显示内容会变形，因此建议页面内容进行折痕区避让适配。建议上半屏内容由中线向上避让16vp（3毫米）、下半屏内容由中线向下避让40vp（7毫米）。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163731.26071983891805280993098854282826:50001231000000:2800:E10E29316D9C3028CFE743CF1B1B4B8FF244FD2F6303D563EE765D238D175AA4.png "点击放大")

### 典型悬停适配案例

悬停状态下，界面布局应自动调整。即将浏览型内容上移，在上半屏显示；将操作类控件元素下沉，在下半屏显示。提供更舒适和高效的使用体验。

**视频通话**

悬停时，上半屏显示通话界面，下半屏显示通话相关的操作按钮。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163731.10862842494926056564991190740698:50001231000000:2800:55695F425B6BC65653381009CD25E6E551D93BC623FA2CFB4C93188F984FCE3D.png "点击放大")

**视频**

悬停时，上半屏显示视频画面，下半屏显示视频相关的操作按钮或周边信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163731.76743956651805709142132678901907:50001231000000:2800:ADCE3BE81F6D4AFBBBDDE3EBB71DA540702C43343FAD70C58375C28FFFF30FEE.png "点击放大")

**短视频**

短视频悬停时，头像、评论、视频画面等显示的内容在上半屏展示，输入框等操作在下半屏显示。短视频类应用进行需要手势操作快速切换视频内容。建议下半屏支持横向滑动切换视频。

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

117

悬停态看短视频示例

**健身视频**

悬停时，上半屏显示动作跟练视频内容、进度，下半屏显示播放及切换功能。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163732.71132577403372217784458398812438:50001231000000:2800:81DFE705BF1E8E102C18B93D0A0C1FF9B64FA8AA5DD01C5DE9E1A6A185F6E92F.png "点击放大")

悬停态看健身视频示例

**拍摄**

悬停时，上半屏显示取景画面，下半屏显示取景模式、拍摄参数控制按钮等操作类功能。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163732.45757364095431897912467985572367:50001231000000:2800:3A3A911801D712E0B09B449E11AA30046E2DD66CF943E1182BC04EBD78CD10FA.png "点击放大")

悬停态拍摄示例

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163732.16289950324784179335966188425368:50001231000000:2800:801C8D6FECE63B4DCDB07B7EA1B49B395E4EF92941F0C9A4782BCD3002884D0B.png "点击放大")

悬停态录制视频示例

**音频播放**

悬停时，上半屏显示专辑封面或歌词、音乐MV，下半屏显示音频播控功能。

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

116

悬停态播放音乐示例

**控件适配-弹出框**

悬停态若触发应用内的弹出框等操作型控件，建议在下半屏显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163733.88465719839325864009197950658463:50001231000000:2800:48EA25D86D5F8E12435CC7447717A7CA0EFE647899BEF0125F83B8639708161A.png "点击放大")

**菜单**

悬停时菜单跟随触发按钮位置，菜单高度自动适配屏幕高度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163733.54346348008541210301042542359632:50001231000000:2800:AB2DF6613D09D30E9580DAD62A1FD8B700F84A743DE25AB332A5D9325DB464E9.png "点击放大")

**输入**

悬停时输入，避免在中间折痕区域显示输入框。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163733.81282827219589071722435311076287:50001231000000:2800:1524D7AF59007B59CE5CD1502424EB1BC65732A82DC15FE97C84580D68FA42CA.png "点击放大")
