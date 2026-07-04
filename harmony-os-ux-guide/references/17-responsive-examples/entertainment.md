# 影音娱乐类

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/responsive-design-examples1-0000001957369849
- 抓取时间：2026-04-04T08:24:53.276Z
长视频、短视频、直播、音乐等类型的应用或业务场景很常见。这类场景的核心都是沉浸式的视频播放和互动，围绕此核心场景，此类应用有如下特点：

-   海量视频内容资源 (一应俱全)
-   沉浸式视频播放状态 (持续粘性)
-   简单的信息架构，层级扁平 (适合做特殊设计优化)
-   快捷的手势交互，易学，沉浸感强 (操作流)
-   注重作者与观赏者的互动 (社交因素)
-   探索延展相关业务：多方同台直播、视频内商品推广 (商业机会)

## 长视频

### 沉浸式广告

在视频应用中，首页顶部往往会有广告内容。针对影音场景，使用沉浸式广告图可以达到更好的沉浸式体验效果。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102202.27458468740214386871230682529589:50001231000000:2800:9EC88A6E4012044A8E9C66F63D645E4DE8AA1B26EFF18B1228C12AC0B2C4A0E1.png "点击放大")

### 自适应广告卡片

也可以使用卡片样式的广告图，在宽屏设备上广告卡片延伸布局，同时结合设备的物理尺寸适当进行广告卡片的形变，广告图内容自适应裁剪。需要确保卡片样式的广告图在多端都有较好的显示效果。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102202.22724414466111552718292173863328:50001231000000:2800:DEFCC0D8352F6590A2417D6BF2552AC695F5437B2BE6BC3FCEB22030FDE226AD.png "点击放大")

除了广告卡片的自适应形变外，还可以基于设备物理尺寸进行广告卡片的布局创新。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102202.60406442583539049914933798681678:50001231000000:2800:8FB7A4EF2F1460095FFCB5781527EC98648F542077765F8D6EE1423CBEC83E5C.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(长视频)-首页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-video-app#section109591922155720)。

### 可缩放宫格卡片

视频应用首页通常会有宫格卡片，通常折叠屏和平板竖屏最佳 3 列卡片，平板横屏最佳 5 列卡片。为满足不同用户群体对于卡片大小和浏览效率的诉求，宫格或瀑布流的布局建议支持通过双指缩放进行卡片列数的调整。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102202.49844305676860315856818697118668:50001231000000:2800:75F63F8024DE1BA3A0FE7CCD4D588D10A25D381FC6BFD0272EB00230A0815CD8.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(长视频)-首页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-video-app#section109591922155720)。

### 长按播放预览

长按视频卡片后，可进行视频内容的播放预览，并针对该视频内容提供一些快捷操作菜单。应用根据业务诉求自定义长按后的菜单项内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102202.41921344830327990269984361163267:50001231000000:2800:A4FA313FD70A31AA41C83815A141A856E541D189AFB495379361227C3441E099.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(长视频)-首页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-video-app#section109591922155720)。

### 浅层级搜索

在应用内进行搜索时，建议原页面内容和搜索页面的层级不切换，搜索框一镜到底的变化，提供更轻的搜索体验。同时充分利用搜索推荐页、搜索结果页在宽屏设备上显示面积大的优势，提升搜索效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102202.77507548597660473488006925875289:50001231000000:2800:C02D668EB8C52AC23DD93772428B491EA10C9036AB86D88453F37FE6D33AF1A3.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102202.63693267422755836571734816279825:50001231000000:2800:BABFBF3508AF56D06318039E4C989021DD7F45F4F7941D0A7B803C9B5E7AD07A.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(长视频)-搜索页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-video-app#section1932711221013)。

### 边看边评

看视频时，经常会有同时看评论的诉求。在折叠屏上，可向上拖动调整评论区高度，提供更大的评论区域；在平板横屏时默认右侧显示评论区域，可向左拖动调整评论区宽度，提供更大的评论区域；在电脑设备上可自由调节视频应用窗口尺寸，视频和评论区域的布局跟随窗口尺寸自适应调整。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102203.52066033111312141579756378295231:50001231000000:2800:5C934F3D1B437CD0785ED32377A98D9368843E768F9F484F4AA88E09688BF15D.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(长视频)-视频详情页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-video-app#section9259381113)。

### 沉浸全屏播放

全屏播放视频，上下有黑边时，弹幕仅在上方黑边区域内显示；上下没有黑边时，建议在视频画面内显示的弹幕不要太多。电脑设备上播放视频时，建议支持沉浸式窗口样式。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102203.73401664610545685388870108731445:50001231000000:2800:1E77B99285BE069D91FC9C9FC4CEBCE96634115120370D1B845E5B1E08AF284E.png "点击放大")

全屏播放视频时，点击选集、倍数等操作，通过侧边或底部面板的方式来呈现临时的操作内容。

在手机横屏、折叠屏折叠态横屏、平板和电脑上，从屏幕右侧触发侧边面板；在折叠屏展开态从屏幕底部触发底部面板，展开态和悬停态的体验一致。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102203.24070179336116168238252971175546:50001231000000:2800:35E56F7C18C886569D2CE06B6558C34DD2FFE9B3D7606D2D8079EA38EF0C8984.png "点击放大")

在类似折叠屏展开态这种方形尺寸屏幕的设备上，点击“全屏播放”按钮，视频画面不旋转。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102203.05968241289194583272933373248901:50001231000000:2800:87CC6AD662EF6459C582CE16B6A7A299ECF1F6A7F72C2DE716CC2D111F984729.png "点击放大")

### 视频悬停播放

在折叠屏展开态，全屏播放视频或在视频详情页播放视频时，将设备折叠，以上两种情况均自动切换至悬停态的沉浸播放视频体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102203.91894198019186739210745339066236:50001231000000:2800:CB521AADA1BAB6B79FA5385402BFD8940F0D368793D66CFDBA9EC835F7D8DC84.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(长视频)-全屏播放页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-video-app#section2899145416113)。

## 短视频

### 侧边面板边看边评

浏览短视频同时看评论是常见的操作，在宽屏设备上可以通过侧边面板为用户提供更好的边看边评体验。

在手机和折叠屏上，默认全屏显示短视频内容，点击评论按钮后分别在底部或侧边展开评论面板。在平板和电脑上由于屏幕足够宽，可直接显示短视频的评论内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.53358042364382860783811190081266:50001231000000:2800:85AA1BBB3E9DC88DDD9E4F237C560B5B72D82FC4305EF67347364F91CB41EDDB.png "点击放大")

在手机或折叠屏上，点击评论按钮展开评论面板：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.32857698430892256898145325411414:50001231000000:2800:EA9397811014F635E9B9A37C5081029BC6C3DFCDE349BA3E23C1AF542339ED42.png "点击放大")

查看横向短视频时，点击展开评论：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.88928120661740626746873669560052:50001231000000:2800:7EC74F427FCD1C52157B9185DD1B1705149ADCC00FA13079A0412DF86CE403C3.png "点击放大")

同时显示短视频和评论时，建议支持继续上滑切换短视频内容：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.65314295524572127124674651659978:50001231000000:2800:A2609EF3C14A29EA74C579457FB47459B40941CDF88B356DC4C5EE673F869FB8.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(短视频)](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-short-video-app#section093743919159)[\-](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-short-video-app#section093743919159)[评论页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-short-video-app#section093743919159)。

### 侧边面板个人详情

还可以在侧边面板显示个人详情页，提供快速切换视频的体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.63075403807559228175492205066632:50001231000000:2800:F8BFA0412DE08AEF8C2149E59AE1BB2A8EFC2091CD4CBEF3D345B9CC7EECE8B4.png "点击放大")

多端的个人详情页面：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.92756625098075110047895157413201:50001231000000:2800:033C7AA879237ABD88C568EFCF68DCF89A42D998B214C5CA993C81052BA0BE52.png "点击放大")

本场景的开发指南，请参阅[一多开发实例(短视频)](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-short-video-app#section1911216483325)[\-](https://developer.huawei.com/consumer/cn/doc/design-guides/responsive-design-examples1-0000001957369849)[个人作品页](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-short-video-app#section1911216483325)。

### 侧边面板快捷手势

在通过宫格瀑布流界面点击进入的视频播放页中，可以提供全局滑动手势，帮助用户实现更浅层的浏览、筛选体验。

-   在屏内右滑，调出左侧侧边面板，呈现上一级的宫格瀑布流，切换其他视频播放；
-   在屏内左滑，调出右侧侧边面板，呈现下一级的个人详情页，挑选该博主的其他视频播放。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.11835733801838993292121892575258:50001231000000:2800:F07D5A18AA6C6C026DD46CD9BEF2398EFDAAAF56A19C7CE436A46044324AFCE7.png "点击放大")

需注意，应用在划分快捷手势热区时，需避开全局系统返回手势热区。

系统返回手势在屏幕两侧的热区宽度均为 16vp，多端保持一致。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.16105693926553597755710851665579:50001231000000:2800:B09D4CB5FBFE4E67700A8795AA5E8ECE5DAD8D62F991A6A75447BB3C5ABDE6BB.png "点击放大")

多端的宫格瀑布流页面：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.49233274140747536493361630597253:50001231000000:2800:A1C523C645A3F5354CBF40F5CF3635ACE871C8485715DCBE925BF8B6EC3992D9.png "点击放大")

### 画中画体验

建议支持画中画能力，用户可在浏览其他内容的同时通过悬浮小窗继续观看视频。

-   开启方式一：点击视频播放页的画中画按钮，调起悬浮小窗；
-   开启方式二：点击返回键或使用全局返回手势，在返回上一级界面的同时调起悬浮小窗。
-   首次使用时，建议直接调起授权弹窗，引导用户开启画中画权限。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.68145190904149096606826236111962:50001231000000:2800:2A450A7E213A5E6D673325B68625114258C2198D58A4F425FC7595A0C35EF778.png "点击放大")

### 半模态窗口分享

在应用内进行分享等快捷操作时，可以通过系统的半模态控件，实现更轻的分享体验，避免大面积的页面跳转，也可以直接调用系统提供的分享能力。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102204.36382198764865890210663583656278:50001231000000:2800:7AD5B97D937B60446A43920E46659F9788360745A3F58DA30B815FA629C1924F.png "点击放大")

### 短视频悬停

短视频场景需要适配悬停体验，在上半屏显示短视频内容和相关的文本信息，下半屏显示操作类功能。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102205.13120401675842604020223261527262:50001231000000:2800:343D6EA9F4798C88FFC2DA0701F507CDF551B231716BE7996C3BF357EDB39E0F.png "点击放大")

## 音乐听书

### 沉浸广告

音乐听书类应用中，比如音乐厅页面，顶部沉浸式广告，建议在直板机和折叠屏上可保持沉浸体验，在平板和电脑上可变为自适应卡片创新布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102205.84848895539776580128537240481537:50001231000000:2800:9B6F173107143B76B6C7D025B66AB257207CE255661A35A774779F157EFC90E3.png "点击放大")

### 浅层级搜索

搜索页是音乐听书类应用的典型页面，建议在直板机和折叠屏上全屏显示，平板和电脑上可考虑在搜索框下方以浅层窗口的样式出现。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102205.21154222229786082235609133386195:50001231000000:2800:C8DB966B167061118CD460B90F8ADFA696074A602E9D9AA221693952A7AE5E89.png "点击放大")

搜索后结果列表，在直板机上单列呈现，在折叠屏、平板和电脑上双列，可呈现更多信息，提升用户获取信息的效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102206.21665240593764646093587834515040:50001231000000:2800:D1CDB798A67274E1F456FF819064E8D9CB358C4B598D2EBF27088B812201532C.png "点击放大")

### 左右布局播放

播放页面，在折叠屏、平板和电脑上左右布局，左侧歌曲配图和播放按钮右侧歌词（或音频正文内容），提高屏幕的使用效率，避免图片或留白过大。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102206.90365364910728338106279596207493:50001231000000:2800:0DF1A6BF7F6CFE0A5D1564EFF58D16642BE2632B3C6992868C0C1978BBFB2DC1.png "点击放大")

### 浅层窗口列表

在播放页切换歌曲的场景直板机上半模态列表，在折叠屏、平板和电脑上可调用半模态窗口，实现更轻的歌曲切换，避免页面大面积跳转。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102206.02955304839017268505058663807562:50001231000000:2800:6D13C6591D9631A70CA047D2C78B827B61EFE757106EA2CA078D69AD59753619.png "点击放大")

### 排行榜

排行榜页面，在直板机上一般单列，建议在折叠屏、平板和电脑上重复布局，单列变为双列。宽屏显示更多的内容，提升用户获取信息效率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260107102207.66133388150073291773988012727765:50001231000000:2800:B74AB0EDB38FDF0E78ABFE43409AC2D3B5C4075A02D9D31A3E730F67EA0B7231.png "点击放大")
