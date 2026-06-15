# 分段按钮

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/segmentbutton-0000001929853292
- 抓取时间：2026-04-04T08:23:31.654Z
分段按钮用于对内容进行组别分类。也可以在多个选项中激活一个或多个按钮的控件。开发相关描述请参考 [SegmentButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150836.63825219545610399200125976810377:50001231000000:2800:1B8696D8D0D8D7C338A7E757115B2D63834F2153B9264F7B7B9E39652ADCF05E.jpg "点击放大")

## 如何使用

**分段按钮控件允许用户从一组选项中进行单选或多选。**通常情况下，在手机设备上分段按钮的选项不会超过 5 个，在更大屏幕设备上一般不超过 7 个，若应用的分类条目较多，建议使用[子页签](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#subtabbarstyle9)来代替。

**分段按钮虽然每一个选项都可以激活使用，但请不要用于编辑类场景。**例如，不要将删除、添加、多选等功能放置在分段按钮中使用。也不要使用于一级导航场景，界面级别的切换仍然需要使用[底部页签](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#bottomtabbarstyle9)。

**分段按钮通常放置在应用的界面布局内，可显示在标题栏下方或底部页签上方。**默认情况下，控件会撑满容器宽度，开发者也可以在需要时自定义控件的宽度以适配业务场景诉求。

**每个选项可显示文本或图标。**为了便于用户阅读和理解，同一控件内应使用统一的内容形式，都使用纯文本或者图标与文本结合的形式。同时，应当精简文本内容，由于展示空间有限，文本应当避免被隐藏或过长截断。

## 类型

分段按照使用场景可以分为页签型、单选型和多选型。在 [SegmentButtonOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton#segmentbuttonoptions) 选项中，开发者需要先通过 type 指定分段按钮的样式类型，如果是可滑动的页签形态，则需要使用 [tab](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton#tab) 类型，如果是可激活的按钮形态，则需要使用 [capsule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton#capsule) 样式。若开发者使用了 capsule 类型，还需要定义 multiply 是否生效来决定分段按钮的操作类型属于是否可以多选。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150836.38127321144391264189466146593622:50001231000000:2800:51F070B103AC88390D2F351437CC2BB5937D76D6C58072A6F947665538E980E1.png "点击放大")

页签类单选默认为白色背板，关联页面切换；单选类 & 多选类默认为蓝色背板，仅作为选项切换。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150836.13424430393818382315303363049280:50001231000000:2800:5F70D1FF095C537BCCEDC5563F425A3C05CD8D208FEC153B504814CC77FFBC71.png "点击放大")

也可以组合图标与文本的单独样式和组合样式。通过配置 [SegmentButtonIconItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton#segmentbuttonitemoptionsarray) 的相关属性进行自定义。

<table id="ZH-CN_TOPIC_0000001929853292__X692f963933e01f72bb1fea30cc6b909092bac83" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853292__row129mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853292__p209791905549"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150836.95400551997436047756194792928467:50001231000000:2800:69F83008C7C90F10F32F8FA5A97D36FBBB9986B0D2001386E288649791B4058C.png" title="点击放大" width="162.33333333333331" height="81.16666666666666"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853292__p133mcpsimp"><span><img originheight="1440" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150836.56669672360384627979069981218207:50001231000000:2800:5F50BE792D5EE1B144FC061D53C253CB5C18EC5D4392A9EF5C5EB09AFE3E90FF.png" title="点击放大" width="162.33333333333331" height="81.16666666666666"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929853292__p135mcpsimp"><span><img originheight="1440" originwidth="2880" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150836.38447383896714028640373944990629:50001231000000:2800:EE99171778F229964EFBD9B09A7550B5C5E10D252CF8851E3759FC3440614668.png" title="点击放大" width="162.33333333333331" height="81.16666666666666"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929853292__row136mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853292__p138mcpsimp"><strong>页签分段按钮</strong></p><p id="ZH-CN_TOPIC_0000001929853292__p140mcpsimp">用于页面快速切换选项。</p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853292__p142mcpsimp"><strong>单选分段按钮</strong></p><p id="ZH-CN_TOPIC_0000001929853292__p144mcpsimp">用于表单的选项选择。有文字、图标、图标 + 文字、图片 + 文字类型。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001929853292__p146mcpsimp"><strong>多选分段按钮</strong></p><p id="ZH-CN_TOPIC_0000001929853292__p148mcpsimp">一组同类功能的按钮布局使用分段多选按钮，如选择文本样式场景。</p></td></tr></tbody></table>

## 布局规则

**手机**

**竖屏**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150836.39368522246508397599223036548281:50001231000000:2800:32A7E6C513A4F05ECCED5086A846F2359ABE98CFAC8F1CB0611C1DD8D889C5D9.png "点击放大")

**横屏**

横屏时最大扩展到 448vp。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150837.00237973602944629881014399917241:50001231000000:2800:9A3D394C7C5182B2F3EE41FEBCE5D2A958A36222C9E5B0F2F46BB9E3A8DB58BB.png "点击放大")

在半模态中使用遵循同样规格。

半模态最大宽度 480vp 的场景下，分段按钮两边距离半模态保留左右各 16vp 间距，使分段按钮宽度与全屏显示宽度保持一致。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150837.19827644041925051517193960941808:50001231000000:2800:F0E808858F14B5199760185F41789B22CA598EF82C6D31D4D6D338A3FF1CA402.png "点击放大")

**平板**

**平板设备适配**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150837.68738410609885908032489799651533:50001231000000:2800:5B3968E47AF197D5FBF67B775329502A84AC56AAF69CBF6165A85C5F3EA1B45B.png "点击放大")

在更大屏幕上，按钮保持最大 448vp 的宽度，不再跟随屏幕伸缩而改变宽度。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150837.51861635553543240191791307294702:50001231000000:2800:3CD0BD9C4AD7F7B3892A822E35710101A7AEF87C88B34E4A6E9FF94C65C732E4.png "点击放大")

在半模态等窗口化场景下保持同样规则，基于容器的宽度减去两侧 16vp 间距，保持最大 448vp 按钮宽度。

**电脑**

在电脑设备上，分段按钮使用小圆角以体现设备风格。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150837.05408559053224530852017750185057:50001231000000:2800:7DFF1C2EAAFEC2A74324393937886268F36EBAAC67346EDBBF06B7951AFC1A54.png "点击放大")

页签类单选默认为白色背板，关联页面切换；单选类 & 多选类默认为蓝色背板，仅作为选项切换。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150837.36227607958396195397402930625361:50001231000000:2800:64D82C542D4C526D20E2B0FCA070A0ACAE1D91F031D1CBF6CB4FB72055E17537.png "点击放大")

同时也可以组合图标与文本的单独样式和组合样式，通过控件能力自定义配置。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250915150837.53848851984417617669543268414382:50001231000000:2800:37EB501CCB09287FC62CBED4168C56181E537238EA433E291BC6484435F8AD9E.png "点击放大")

宽度规格与多端保持一致，最大宽度 448vp。

## 开发文档

[SegmentButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton)

[ChipGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup)
