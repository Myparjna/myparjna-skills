# HarmonyOS Symbol

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962
- 抓取时间：2026-04-04T08:22:35.023Z
## HarmonyOS Symbol

HarmonyOS Symbol 代表了 HarmonyOS 系统图标设计的一次重要演进。它通过简化的图形和直观的语义表达，不仅易于识别，同时融入了更多年轻化的设计理念，使得整体的视觉风格更加年轻和时尚。同时 HarmonyOS Symbol 还具备了字体属性，使其能够与系统字体无缝对接，确保了文本与图标的排版一致性。此外，它能够根据文本的粗细变化进行智能适配，确保了在不同文本粗细下，图标能够灵活适应，保持视觉的连贯性和一致性。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163647.18315286445583975720680664461585:50001231000000:2800:5CB83B993CA7B256D365420F4D77EC2AEFE03BFCA901260D8C338F4CFE6C812C.png "点击放大")

### 字体属性

HarmonyOS Symbol 具备字体的属性，与文本混排时可以很好地与字体基线对齐。同时，它支持粗细无极变化，允许开发者根据具体的设计需求，选择适合的图标粗细，以确保图标在不同使用场景下的风格一致性和视觉协调性。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.27448705293629995342306676375873:50001231000000:2800:CBB1A1C322CA862248AACD3FC41FCA88DFA1A9B215EEA9239F3790ADDD346A7C.png "点击放大")

### 颜色渲染

HarmonyOS Symbol 的设计采用了灵活的分层结构，确保图标在不同场景下的视觉一致性。图标的每个图层都可以独立设置颜色和不透明度，提供了高度的个性化定制能力，以实现个性化的 UI 设计效果。

**渲染策略：单色 (SINGLE)**

可生效用户指定的一种颜色，当输入多个颜色时仅生效第一个颜色。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.75168504387233636609242382104449:50001231000000:2800:5A46936F356245485791E217D88962B6DCEF231FBE9C312ADDFFC58738FEA926.png "点击放大")

**渲染策略：分层 (MULTIPLE\_OPACITY)**

默认为黑色，可以设置一个颜色。当用户设置多个颜色时，仅生效第一个颜色。不透明度与图层相关，第一层 100%、第二层 50%。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.52000994286886923487153031673043:50001231000000:2800:D9F2A3B7964FC2526258435427B4B9E01883FB2FF127A23136488B468060862D.png "点击放大")

**渲染策略：多色 (MULTIPLE\_COLOR)**

可生效用户指定的两种颜色，当用户只设置一个颜色时，修改第一层颜色，其他颜色保持默认颜色。颜色设置顺序与图标分层顺序匹配，当颜色数量大于图标分层时，多余的颜色不生效。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.00002721077490796174022316584286:50001231000000:2800:997CDA6C4C854DE6C958453ABE8E70B84FE3805865661839DC8A9660BCCEB801.png "点击放大")

### 动效策略

HarmonyOS Symbol 超越了传统的静态图标功能，集成了 7 种动态效果。开发者可以将这些动画效果与用户操作紧密结合，例如点击、长按、输入和数据传输等，使 HarmonyOS Symbol 成为互动性强的组件。动画的响应性为用户提供了直观的反馈，有效增强了交互体验。

HarmonyOS Symbol 支持 7 种动效策略，分别为出现 (AppearSymbolEffect)、消失 (DisappearSymbolEffect)、弹跳 (BounceSymbolEffect)、缩放 (ScaleSymbolEffect)、替换 (ReplaceSymbolEffect)、脉冲 (PulseSymbolEffect)、可变颜色 (HierarchicalSymbolEffect)，其中默认为无动效策略。

[动效策略原始 HTML 表格（按需查看，含全部内嵌资源）](harmonyos-symbol-motion-table.html)

> 表格来源与抓取时间同本页。原始长行完整保留在独立文件；仅核对具体动效素材时用浏览器查看，不要全文读取该 HTML。

### 如何使用

HarmonyOS 图标符号是系统内置的一套图标资源库。开发者可以通过图标的资源名称，利用 Symbol 组件高效索引并使用相应的图标。使用 HarmonyOS Symbol ，开发者不仅可以轻松地通过图标名称引用图标资源，从而简化开发流程。还能够确保其应用程序在视觉上与系统的设计风格保持一致，从而提升用户界面的专业性和准确性。

### 查询图标

模块开发可以通过图标的资源名称来索引，从而从资源框架中获取相应的图标。例如，如果要使用 “加号” 图标，就需要从 Symbol 网站上找到该图标，并标注其 Symbol name ID 为 plus 。通过 Symbol 图标网站，你可以轻松查看到 Symbol 图标的资源名称。

图标的命名是依据其形状进行描述的。图标名称请查阅 [HarmonyOS Symbol 图标库](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol/)。

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

3185

### 属性标注

Symbol 图标支持与字体样式一致的属性，包括但不限于大小 (font size)、粗细 (font weight)。此外，Symbol 图标还支持自定义的颜色渲染策略和动效策略，以实现更加丰富静态和动态的视觉效果。

**SymbolGlyph**

SymbolGlyph 组件则适用于独立图标的展示。开发者可以为图标设置字号大小和字体粗细，此外，SymbolGlyph 组件还支持自定义颜色渲染策略，允许开发者根据应用的主题或用户偏好调整图标颜色。同时，组件还支持动效策略，使得图标在用户交互时能够展现出生动的动画效果。

在默认情况下，Symbol 图标的尺寸与其字号大小保持一致，例如，设定为 24vp 的字号，其图标的宽高也将为 24\*24vp。这样的设计确保了图标与字体在视觉上的和谐统一。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.38598567023902412966900263844825:50001231000000:2800:B1B67860FFAA90969295C9C016649E1241636C8E0DBF3CBEDFA21DE2C918F735.png "点击放大")

在底部页签控件中使用 SymbolGlyph 组件时，可以充分利用 Symbol 的分层颜色样式，为每个页签提供独特的视觉识别。当用户点击页签进行切换时，可以使用 Symbol 的通用动效——弹跳效果，增强用户操作的反馈和愉悦感。

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

2748

开发指南请参阅 [SymbolGlyph 开发指导文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)。

**SymbolSpan**

SymbolSpan 组件专为图标与文本混排的使用场景设计，它能够与文本共享相同的样式属性，包括基线对齐、字号大小和字体粗细。这种设计确保了图标与文本在视觉上的一致性和协调性，使得混排内容更加协调。

当图标的粗细属性设置为 “fp”(font-pixels) 时，它将自动与系统字体的大小同步调整，实现图标与文本的视觉统一，从而实现更加灵活和适应性强的界面设计。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.54228496166816585254504341992455:50001231000000:2800:05E8B6C96B3A7E1F81801AA28CA30B29750853C6EAA348278F752695E52717DB.png "点击放大")

开发指南请参阅 [SymbolSpan 开发指导文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)。

## 图标设计

HarmonyOS系统图标追求精致简约、独特考究的设计原则，主要运用几何型塑造图形，精简线条的结构，精准把握比例关系。在造型和隐喻上增加年轻化的设计语言，使整体风格更加年轻时尚。避免尖锐直角的使用，在情感表达上给用户传递出亲近、友好的视觉体验。

### 基础图标设计原则

为保障图标体量一致性，可参考标准网格布局进行绘制，确保所有图标在统一尺寸、比例和视觉风格上保持一致，同时遵循清晰的像素对齐和简洁的设计原则，以提升整体识别性和适应性。

**图标大小**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.91320545253303067822809776768681:50001231000000:2800:7B8DAD1883BCBDA37202AD41CE63EBA107963AD049B750815B5B01E81A623E57.png "点击放大")

标准图标为24\*24vp，图标主题物应保留在蓝色区间内（22\*22vp)，网格布局主要作用为体量参考，部分图标可根据图形体量感突破网格界限。

**图标形状**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.03611915567473248358418836905804:50001231000000:2800:93A9E2BE4322053629E84360A82159F18B9B7D595B3C74F754ED246B0B85ECE4.png "点击放大")

**图标细****节**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.18833470032180584106119340744712:50001231000000:2800:F03F8216DECCEA82F255594C902F0CD4C76B065418460AAD0F9FCDCA7B2DCE9E.png "点击放大")

**1\.** 描边粗细：1.5vp ； **2\.** 终点样式：圆头 ； **3\.** 断口宽度：1.3vp ； **4\.** 外圆角：3vp ；内圆角：1.5vp

**复杂形状**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.80257222345922723375236085861233:50001231000000:2800:63EFF836777E555C708967A6AD2901855A4A3B0C65E07CB424215ACE4FEC7974.png "点击放大")

描边粗细为1.3vp

如果图标需要复杂的细节，可以进行细微调整以提高其可读性。这些调整称为视觉校正。任何视觉校正都应使用所有其他图标所基于的几何形状，而不会歪曲或扭曲这些形状。

有圆形底板组合需求，因而视觉重心呼应圆形，略微偏高。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.05002801218699821927098011973626:50001231000000:2800:A765E623F494C69E3C61C6A1AB7AF6D6E7D1B0D5AC58364A96CD6AD8FDD76FEF.png "点击放大")

右图外部实线为外框线条

导出样式：1.必须包含外框线条，作为字库化的大小标准 2.必须以 SVG 的格式导出。

### 图标扩展一致性

**角标规则**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.72279223701076302229135995542238:50001231000000:2800:4F607DB7849C51BE688FE7E399F7A4DF5B890DCBA9DC5760AEC87999602E5FBD.png "点击放大")

1\. 表示物体状态，例如加、减、乘、除、对号等，通过圆形背板形式进行表达；

（角标是面性图形时，如设置、提醒铃铛、爱心等，无需添加圆形背板，但绘制标准需要遵循角标绘制规范大小8vp）

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.66003252080200276481446278005347:50001231000000:2800:A24DBAB9D2DA5C0974BE50B4ED137B1CC5A1B87D07D54EA62FBF82CCAAF608F9.png "点击放大")

2\. 用于语意组合的两个图标组合，无需使用背板；

（语意组合表达含义较丰富，要根据主标与角标之间的关系进行绘制，无固定位置；若角标图形使用线性，去掉背板后较为单薄，需根据实际情况增加背板）

**切断规则**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251120163648.19812936732543525164243062209271:50001231000000:2800:4DF7350F1EF50548EB25484176553816310684F026B2FFBFD93536CF77902811.png "点击放大")

1.切断效果：两边留白 ； 2. 端口宽度：1.3vp ； 3. 切断面应保持平直的被切效果 ；4. 斜线从左上至右下，角度为45度 ； 5. 根据图标视觉效果，等量切段；

### 自定义Symbol

设计完成后的图标，需要经过专业字体软件的输出，从而达到可变字库的输出要求。同时，还需要制作分层和遮罩效果，为后续颜色和动画配置做好必要的准备工作。

自定义Symbol开发指导文档请参阅[应用加载自定义Symbol](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-config-custom-symbol)。
