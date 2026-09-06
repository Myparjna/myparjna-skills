# 智感握姿

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/smart-reachability-0000002556657823
- 抓取时间：2026-04-04T08:24:14.190Z
## 概述

智感握姿综合多种传感器信息和人因信息，通过先进的 AI 算法，实时识别出手机握持姿势，动态调整界面上交互组件的位置，旨在解决顶部与侧边操作不易触达的问题，让单手操作更易用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/KcbBGPEvRLOWkVcb2cSmUA/zh-cn_image_0000002557715109.png?HW-CC-KV=V1&HW-CC-Date=20260404T082411Z&HW-CC-Expire=86400&HW-CC-Sign=5937931607B504E428843CE772A071B624294BB5483E530EFB9E0FCAD88BFE0E "点击放大")

## 典型场景

### 保留已有交互

针对交互组件在难触达区域且用户已有心智的操作，建议保留原有位置的交互，在此基础上在单手易操作区域新复制一组交互组件方便用户操作，两者距离不宜过近，示例如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/TwcR0pndQ5SgCm-9JiXBXQ/zh-cn_image_0000002526561930.png?HW-CC-KV=V1&HW-CC-Date=20260404T082411Z&HW-CC-Expire=86400&HW-CC-Sign=283F0DB3F5FBDBDA31A2E51963016AEBA2DEC62C1FD102BDA0C55BFC4DF765E7 "点击放大")

### 移动已有交互

针对交互组件在难触达区域，也可将原有交互区域直接移动至当前单手易操作区域，示例如下。同时需避免过于频繁移动带来不稳定和干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/AODhTUm1S5eXbl_9pc24Uw/zh-cn_image_0000002557721759.png?HW-CC-KV=V1&HW-CC-Date=20260404T082411Z&HW-CC-Expire=86400&HW-CC-Sign=0195BCCA21D1D9E409425F6924786395B07962AA84DB242C68A43DBB43F35745 "点击放大")

## 接入原则

为确保此能力服务于广泛且准确的用户体验，建议满足以下条件：

**仅针对单手难触达的必要组件。**推荐用户必须操作的组件接入智感握姿，例如来电横幅接听/挂断按钮、侧边悬浮按钮等。避免应用于悬浮广告等营销场景，诱导用户点击。

**不可改变已有的交互逻辑。**在难触达交互组件移动/复制至易操作区域时，避免增加或遗漏功能，并保持与原有交互一致。

**用户可自由关闭此功能。**应用应有此功能的开关设置，在用户不需要时可自行关闭。

**统一术语。**“智感握姿”为 HarmonyOS 独有能力，应用若露出相关介绍，必须准确使用“智感握姿”，避免使用其他类似用词混淆用户心智。

## 交互规则

智感握姿旨在将让单手操作更易用，不限制特定的交互手势，点击、滑动、长按、拖拽等系统常见基础手势均可接入。

1\. 在保留已有交互的场景下，两组交互需同步联动，保证两侧反馈一致，示例如下。同时建议将原本的难触达操作按钮弱化，引导用户关注侧边易用按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/9T4_QQa_T3K-LrsS00Af7A/zh-cn_image_0000002526721904.png?HW-CC-KV=V1&HW-CC-Date=20260404T082411Z&HW-CC-Expire=86400&HW-CC-Sign=2E3051CCE0EAB955E436B9BDDB8C8FC15EF4D36A6C4B533CD3491B4BE904BB70 "点击放大")

2\. 新增的交互组件避免与已有的系统组件冲突，注意避让键盘、横幅通知、侧边导航栏、画中画、中转站等，示例如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Np017fDdTLevoVhssWq1sQ/zh-cn_image_0000002526562056.png?HW-CC-KV=V1&HW-CC-Date=20260404T082411Z&HW-CC-Expire=86400&HW-CC-Sign=823749C7E4C855ADBBD2131F58320C522EA7D8364E87F820FBB5C6CF5A810458 "点击放大")

## 动效规则

组件出场位移动画使用曲线 interpolatingSpring (velocity 0；mass 1；stiffness 200 ; damping17) 。

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

17

组件换位位移建议从屏幕外移动，尽量避免频繁在屏幕内移动，干扰用户视线 。动画使用曲线 interpolatingSpring (velocity 0；mass 1；stiffness 170 ; damping17)。

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

10

智感握姿开发文档请参阅：[获取用户动作开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/motion-guidelines)
