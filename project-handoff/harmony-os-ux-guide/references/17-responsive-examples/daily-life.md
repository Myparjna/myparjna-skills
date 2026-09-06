# 便捷生活类

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/convenient-life-0000001957252465
- 抓取时间：2026-04-04T08:25:08.166Z
便捷生活类场景主要包括点餐、观影、看攻略等。此类场景在宽屏上可以让用户拥有更高效和流畅的使用体验。

开发指南，请参阅[一多开发实例(便捷生活)](https://developer.huawei.com/consumer/cn/doc/best-practices/multi-convenient-life)。

## 首页的自适应布局

首页采用自适应布局进行适配，在宽屏上，建议一排显示更多图标数量，但折叠屏不超过一排8个，平板横屏不超过一排12个。折叠屏展开态上3列宫格布局最佳，平板横屏默认5列宫格布局最佳。在更宽的屏幕上也可以通过挪移布局进行更多体验创新。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110536.16843622358757583956481571601455:50001231000000:2800:0D1C17138E1F9198313E94735A27F4884A7B0222E92E06208C8502AFA814C5F0.jpg "点击放大")

## 美食页面

### 搜索列表

在搜索结果的显示上，建议宽屏设备上通过重复布局展示更多内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110536.16401514372612336138577628545350:50001231000000:2800:FB23C73EDBFD090A5F8F2FF634730456A57D19A4517749052B96BEC0DE6BED66.jpg "点击放大")

### 店铺页

在店铺页进行宽屏适配时，建议默认使用分栏布局来提高交互效率。分栏形成后，左侧内容固定不变，新页面始终在右侧区域替换，以实现“列表+详情”快速切换的效果。在折叠屏上通常建议分栏比例为1:1，在平板上为4:6。

支持分栏、全屏切换：在折叠屏/平板上，该场景形成分栏后，支持用户手动切换为全屏，交互更自由。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110537.50800827265588543065457369046753:50001231000000:2800:7BE33D4736DE2AEA523AF5B17659858288B0F592ED408C28E7871788AB6CF01D.jpg "点击放大")

### 详情页

从店铺页分栏进入美食详情页后，依然保持分栏显示，同时也支持手动切换成全屏。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110537.60066734654493570242654743799843:50001231000000:2800:5D062B57F42E547B4BE05273C1CA636898D12069382D61F73856DFFE028909FC.jpg "点击放大")

顶部单张大图适配：在8栅格和4栅格的设备上，如果顶部商品图片数量只有1张时，建议保证图片高度不超过0.5倍屏高，若图片超过则上下智能裁剪，同时图片支持向下滑动展开，以查看完整图片内容。

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

### 选规格

当用户选择美食的具体规格时，建议调用半模态窗口显示：在手机态为置底的悬浮面板，折叠屏上为窗口居中显示，平板上为窗口跟手显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110538.65119173182397305717305794622068:50001231000000:2800:93761138E74FDED961A45FE5170F3E5F9AA0DAC24B5BB234EB294CDA74B3A4A7.jpg "点击放大")

窗口高度动态变化：半模态窗口的高度跟随规格的内容动态变化，最低不低于320vp，最高不超过90%屏幕短边宽度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110539.06753806795291202885467212654029:50001231000000:2800:98EAC9A45FACCEC470E66C1377C34611AEBE39F368A8BB9B18811C3C9FB04CC6.jpg "点击放大")

## 电影

在电影购票流程的页面上，建议在宽屏上进行适当的布局调整，让内容显示更多，同时保证沉浸感。

### 选电影

随着屏幕的宽度的变化，建议采用挪移布局，上下结构变成左右结构；另外，原本列表显示的内容，也可以考虑变成宫格/瀑布流显示，以获得更佳的使用体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110539.54525011249906202318913819214210:50001231000000:2800:403B6D5D00E43F6BAB4EB864254B54BCF04EAC4F8D1DD5860CA0AF03152D2EB8.jpg "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110539.65971434277187287045741171553565:50001231000000:2800:A30738507317D01867F62BFCEE486748B46E37C3C730EA92D9F4EA9F7E2A8827.jpg "点击放大")

### 电影简介

在手机和折叠屏上，建议使用自适应布局。在平板等更大屏幕设备上，建议采用挪移布局，上下结构变成左右结构，左侧固定显示电影的基本信息。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110540.17261847917633915584215931018851:50001231000000:2800:285A713B2C51F0AFFAC5A159115343F2AFD7BE98CDB5403E0140777C33600DC3.jpg "点击放大")

### 选影院

在折叠屏上，可以考虑挪移布局，上下变左右结构，横滑变竖滑。在平板上，建议在左右布局的基础上，可以考虑展示当前选中影片的预告片等。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110540.81417687087688453975580349451089:50001231000000:2800:AD5FC5ABD4A149B5DAD67E6AD56484BA966876BBEE66E93BC4E4ABE2089A6713.jpg "点击放大")

## 实况窗

实况窗是一种帮助用户聚焦进行中任务、方便快速查看和即时处理的消息提醒，包含胶囊态、卡片态。在点外卖和电影开场提醒等场景中十分实用：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110541.79200429487354139708033592881538:50001231000000:2800:D630454ECBEDF057C0A8662F83AB5BC3AD3F7F220B462B9FFF222DD73EC13D22.jpg "点击放大")

点击卡片空白处，进入对应详情页。其他实况通知详细内容，请查看实况通知章节。

## 推荐

推荐页经常使用宫格或瀑布流布局。在宽屏设备上，通常显示更多列数，且宫格和瀑布流布局支持双指缩放。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110541.34957767757152749126365482194297:50001231000000:2800:CD0F18534DC18320AF2B26D59426859003A37E6101F089478B451CBCE4489FD3.jpg "点击放大")

## 短视频

### 视频详情看评论

短视频详情页宽屏适配时，折叠屏上点击评论按钮后显示评论列表，平板默认展开评论列表。宽屏背景使用毛玻璃效果可提升页面沉浸感。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110542.61768175337910998770788477538527:50001231000000:2800:D3038DEA8C55E44EB378A2A13BD4E0E92739DD560AB73C1BCEADC8CA3DF2BC21.jpg "点击放大")

点击评论按钮后，手机端底部向上展开评论面板的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110542.44288186441013946124895758576857:50001231000000:2800:167E787E81AE6B4622F0D38BBEDAC81D68C97D15089E09165A2EE62745647DE3.jpg "点击放大")

### 查看更多辅助信息

点击视频下方的标签文字按钮或卡片、链接等，可通过右侧的面板呈现打开的内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110543.96233823567211075720450182803645:50001231000000:2800:E9980FF8550C41FE2B791177CE5B96EFEFD9D3D57D681D078B82C71B66903DCC.jpg "点击放大")

多端查看辅助信息的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110543.90760926254467601300160813631586:50001231000000:2800:2BCB506D23F3204E9E7B3AEA3CBF46DEC2F5DC1C354A28EB013834BFF14FB1D2.jpg "点击放大")

返回或关闭右侧辅助面板时，恢复全屏浏览视频。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110544.80082913788860589933862853170121:50001231000000:2800:808B026A85F0C940A2AAA14E599EF09488781FBEE69ACD54AE6ABB594996D076.jpg "点击放大")

### 视频悬停

短视频场景需要适配悬停体验，在上半屏显示短视频内容和相关的文本信息，下半屏显示操作类功能；视频播完后自动播放下一个视频，智能优先筛选横向视频。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110544.93709159761085407488093583893831:50001231000000:2800:73A0BFD9527982D83814EE8BF6B9D5DAA8B69900D66132C7B0B43D4C3ECC6CC5.jpg "点击放大")

## 直播间

在直播时，经常会有聊天互动的诉求，手机上默认全屏显示直播内容，在折叠屏、平板、电脑上将聊天面板在侧边展开，在看直播的同时也能享受聊天的乐趣，增加互动性。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110545.83462729013091667762714587653327:50001231000000:2800:0957A82B5BA0AD1BB8B0E74F75E1360B7C85D2E0E5E8C349DA1CA8E7214B1BD4.jpg "点击放大")

## 笔记详情

### 图文笔记

在阅读笔记详情时，为确保更好的阅读体验，折叠屏、平板以及电脑 建议采用挪移布局：将文字挪移到图片右侧，实现图文对照阅读效果。折叠屏尺寸接近方形，建议允许用户手动切换布局，提供更自由的阅读体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110545.54732561757248135482793594123225:50001231000000:2800:44304B80D4C23A845D7FD0CA96A6D6FD99917CFC9241E925058859E059FE624E.jpg "点击放大")

折叠屏上建议按照约3:2的图文区域宽度比例，平板和电脑上建议按照1:1的图文区域宽度比例。

折叠屏图文详情：

在折叠屏上的图文占比为 6:4,图片右侧贴合文字区域，且与左侧页边距应尽量缩小，保证图片最大化显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110546.53406507506931310938741635014715:50001231000000:2800:CE7F7C9204EBF0D5906BA41FDACCC6FFADC80B3BCF549A85B43D27DF08B97177.jpg "点击放大")

通过按钮切换布局的示例：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110546.79423139049618450851440502148957:50001231000000:2800:3BC039EF8C24800B98513DB75E2F2EF01110BE18726F41585E6B75DF84F98D74.jpg "点击放大")

折叠屏的图文详情页，上下布局的三种范式：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110546.50298226634848726692489164624380:50001231000000:2800:0A6E48FF1AE92D8CD51A7E11E1B5182158A2C844C88BAAC0EE6B15E0D302458D.jpg "点击放大")

在平板上，点商品链接进入下一层级页面时，商品详情面板右侧推挤显示：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110547.79398830570579833045038399337660:50001231000000:2800:432A6D0776E815950E978710F4C66FC2549F29DD900E89A1D776BE1D84C72E7C.jpg "点击放大")

多端键盘输入：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110547.42190428865418422628841870398538:50001231000000:2800:4DC0BDCC5DAB5A0EDABE5B30567EAE76E535AE5C714451D61E72C84D7D361380.jpg "点击放大")

### 图文浏览效果

图片点击放大：

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

73

双指滑动放大：

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

61

沉浸式图文同看：

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

62

横图缩小浏览：

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

51

## 个人主页

在笔记详情里面，点击用户头像，折叠屏、平板侧边面板覆盖在原界面中显示该用户的个人主页。

折叠屏：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110547.87880258003752649235646172944521:50001231000000:2800:615040C3A51687E0BB97A1C08FED590216A35DA9EAD2441E13EBA1C9955EFCE3.jpg "点击放大")

平板：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110548.87042371220614873239476586096845:50001231000000:2800:59F0A2C6F6409873472C7994D845E0E7A77DFBDDA6370D2667389ABCAB9F2454.jpg "点击放大")

个人主页侧边面板支持手动切换成全屏显示：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110548.50950562711530953783278335857187:50001231000000:2800:476AD28FC948593F9FC70B7FE5DCB6CF9A7E8CF61F839EC0166B9F815D0F2620.jpg "点击放大")

不同设备的屏幕宽度不同，建议在宽屏设备上采用挪移布局，上下结构变成左右结构；列表内容显示可以考虑宫格/瀑布流形式。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110548.19262619586039804887944013716578:50001231000000:2800:3A436E1FB50EE3B46E7258AEAA1B6D3227160805C57EFE240CC1F0FAD9F398F7.jpg "点击放大")

## 关注动态

### 范式一：单列卡片变分栏+宫格/瀑布流布局

手机上的顶部关注列表和动态卡片，在宽屏设备上挪移布局并形成分栏，在更宽的平板和电脑上可露出更多列的动态卡片，成为分栏加宫格/瀑布流布局。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110549.16296656896363699352083853336012:50001231000000:2800:4A24C3DF09CBBE7F54A857CE892648ADA1BC1738AD299FCF1000DF3017E997D0.jpg "点击放大")

### 范式二：单列卡片变宫格/瀑布流布局

也可以直接从手机的单列卡片到宽屏设备的宫格/瀑布流结构，随着屏幕宽度的增加显示更多列数内容。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110549.60493904022943244386817905766718:50001231000000:2800:5E33B0DBA5A85DBC0E65DDF7348B7F80BCDCA57D38E462097ACDCE4389B3C49F.jpg "点击放大")

### 范式三：单列卡片变宽

手机上的单列动态卡片，在宽屏设备上可露出更多辅助信息变成更宽的动态卡片。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250701110550.60350693361790562545393351490944:50001231000000:2800:23BEF3AF082073B179C096DC529CD2373FDEA37025A2043DB1C3CC3942683148.jpg "点击放大")
