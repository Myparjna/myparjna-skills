# 全球化

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/design-globalization-0000001748539688
- 抓取时间：2026-04-04T08:22:45.736Z
产品和应用要在全球发布，需考虑全球化流程，即**“**国际化**”**和**“**本地化**”**。

国际化简称「i18n」，是一种趋同的设计方式，通过一种方案去满足不同国家的需求。

本地化简称「L10n」，是针对各个国家的个性化解决方案。

本指南对国际化和本地化设计常遇到的问题进行归纳总结，遵循以下规则可以有效提升产品和应用的全球化质量。

## 视觉

### 文字与图片

不要将文字直接嵌入图片中。

图片上的文字需要采用分层展示，这样可以在不替换图片的情况下，通过简单替换字符串即可满足不同国家的展示需求。

<table id="ZH-CN_TOPIC_0000001748539688__X8a2ef6100dd11a8cffe56400b4c90bbc558fd1b" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001748539688__row122mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p124mcpsimp"><span><img originheight="1200" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.90320194740127827880111988337584:50001231000000:2800:3BA35146309E0AAC7FCA3006457556FB009151E76D0B9921CDA05EAA704ACA07.jpg" title="点击放大" width="268.5" height="223.75"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p126mcpsimp"><span><img originheight="1200" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.27811762797942662881073672513702:50001231000000:2800:3B4DABDE257B1F1B89954030CCB1BECBD20A34C774161BBA33C88CE9602E9187.jpg" title="点击放大" width="268.5" height="223.75"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001748539688__row127mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p129mcpsimp">系统语言切换成英文</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p131mcpsimp">系统语言切换为日文</p></td></tr></tbody></table>

### 颜色

使用 HarmonyOS 系统推荐的颜色。

不使用其他国家或地区禁忌的颜色 ，例如：

展开

| 
国家

 | 

禁忌色

 | 

不建议使用场景

 |
| :-- | :-- | :-- |
| 

俄罗斯

 | 

黄色：俄罗斯男人如果送女人黄色的花表示分手的意思

 | 

情侣场景：如情人节时，注意不要涉及黄色的花

 |
| 

巴西

 | 

紫色：表示悲伤

 | 

喜庆节日

 |
| 

英国

 | 

紫色：表示不吉利

 | 

喜庆节日

 |

### 图标

设计图标时，应避免禁忌内容。例如：宗教符号、法西斯及反政府反人类组织符号、动物、植物、手势、人体部位、肤色、性别等。

-   在通用版本中，应避免使用对某一国家或某种文化有特殊意义的样例、图案、用词。
-   避免使用宗教、种族、政治导向的词语、图标、旗帜等。
-   避免使用特定文化的比喻 (如用米饭代表消耗的卡路里)。

<table id="ZH-CN_TOPIC_0000001748539688__Xc9e55e9cb6e1e3bc9a910fadbf15c6bd4d59d80" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001748539688__row178mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p180mcpsimp"><span><img originheight="1172" originwidth="1276" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.94358980959335007957503893393387:50001231000000:2800:890897E1556C94BF41744016B5C66EED1221F9DBB6D671670D9514DF0148B68A.jpg" title="点击放大" width="268.5" height="246.61598746081506"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p182mcpsimp"><span><img originheight="1171" originwidth="1276" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.70265584034755730039577057599213:50001231000000:2800:741F1D892B32C31082DCB09BADEC0D0AEA3FDD6C35B1D2E965EC25EEF59C981C.jpg" title="点击放大" width="268.5" height="246.40556426332287"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001748539688__row183mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p185mcpsimp">线性图标</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p187mcpsimp">填充图标</p></td></tr></tbody></table>

在 RTL (如阿语) 语言系统中，如果图标包含方向性的图标，需要单独提供一套资源。

注意：图标上尽量不要加文字。

<table id="ZH-CN_TOPIC_0000001748539688__Xd0620a4f776f4c168280b8840fbae7c20f9cef7" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001748539688__row194mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p196mcpsimp"><span><img originheight="1080" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.62759130705305467423767524020236:50001231000000:2800:314CDF7FEA1E7EE5D8E605F17576A49374B4AC2DE651DABB2F61F8CE79C58E20.png" title="点击放大" width="268.5" height="201.375"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p198mcpsimp"><span><img originheight="1080" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.83838465077621238700941265915703:50001231000000:2800:35E38D29290AB61B5E3958D1475C75DB046FB9ADFAF49A160C3A6FF6B943FCD5.png" title="点击放大" width="268.5" height="201.375"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001748539688__row199mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p201mcpsimp">一般图标资源</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p203mcpsimp">RTL 语言系统下提供的图标资源</p></td></tr></tbody></table>

### 插画

插画的人物风格尽可能中性，不能太暴露、太个性化及带有地域特色的人物。例如：

<table id="ZH-CN_TOPIC_0000001748539688__X295ccb1ae11fa4bd2c7e9e664c1be1f9493ed72" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001748539688__row210mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p212mcpsimp"><span><img originheight="1200" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.24897655931633372590508351910250:50001231000000:2800:28DAB952F648AAB5EC94FA5B4780DAFAC543549876C46306785FDEAFC061D67F.png" title="点击放大" width="268.5" height="223.75"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p214mcpsimp"><span><img originheight="1200" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.68267744202483938945666180792416:50001231000000:2800:F36493AE585E466F7193B147789AAFD01E71935CF3A60C68C2B85BDBABEEFF2C.png" title="点击放大" width="268.5" height="223.75"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001748539688__row215mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p217mcpsimp">涉及禁忌元素：女士</p><p id="ZH-CN_TOPIC_0000001748539688__p218mcpsimp">具体内容：女性形象过于暴露，在中东北非国家地区会引起不适，建议替换成长款运动装。</p><p id="ZH-CN_TOPIC_0000001748539688__p219mcpsimp">风险程度：高</p><p id="ZH-CN_TOPIC_0000001748539688__p220mcpsimp">受影响国家地区：中东北非国家</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p222mcpsimp">涉及禁忌元素：男士胡子</p><p id="ZH-CN_TOPIC_0000001748539688__p223mcpsimp">具体内容：图中人物展示出小胡子等嘻哈形象特征，建议去掉胡子。</p><p id="ZH-CN_TOPIC_0000001748539688__p224mcpsimp">风险程度：低</p><p id="ZH-CN_TOPIC_0000001748539688__p225mcpsimp">受影响国家地区：新加坡</p></td></tr></tbody></table>

在 RTL (如阿语) 语言系统中，如果插画包含方向性的图案，需单独提供一套插画。

<table id="ZH-CN_TOPIC_0000001748539688__Xfa715bb0e6fac2be99fdb770e57f7c6b0a9d133" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001748539688__row231mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p233mcpsimp"><span><img originheight="1440" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214100.16379250051888684076187167267954:50001231000000:2800:6F38C94BDB9ED97D86C12E6ABC0CD57D79A573CB349DDBF33131DAD3871F8CAD.jpg" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001748539688__p235mcpsimp"><span><img originheight="1440" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619214101.05441492865961351282757869874450:50001231000000:2800:F83BD5A1242080A5B9E7E94E286AB3BED5B114300A48F06E31DDA6F1CC27ECEB.jpg" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001748539688__row236mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p238mcpsimp">一般插画资源</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001748539688__p240mcpsimp">RTL 语言系统下提供的插画资源</p></td></tr></tbody></table>

### Emoji 表情

-   风格要积极阳光。
-   不要使用色情、暴力相关内容，需注意赌博、瘾品等内容。
-   尽量保持用户认知习惯，不要采用另类图案隐喻。
-   尽可能包含各个国家/地区的人。
-   不要出现手势 (若需要，建议加上人的背景，以清晰传递要表达的意思) 或带有性暗示的图形。
-   避免用国旗代表语言。
-   避免使用宗教、神话相关的内容和符号等。
-   避免涉及民族、地缘、宗教、政治的敏感信息。

## 手势

避免使用手势来传递某种含义

身体和手势自古就被用于信息沟通，他们和语言一样，在不同文化中常常代表着不同的含义。像竖拇指在某些文化中却可能具有非常粗鲁或否定的含义。

## 布局

**空间预留**

为了避免界面上的字符串翻译成其他语言后因过长被截断，应在界面设计时，为字符串预留足够的空间。控件文字显示要在英文的基础上预留至少 30% 的空白空间，利于翻译成全球化其他语言而不出现截断。最理想的安全空间是预留比英文长度多 2 倍左右的空间长度。扩展比例以英语为基准按照如下表格执行。

展开

| 
**英文字符个数**

 | 

**至少预留的空间比率**

 |
| :-- | :-- |
| 

≤ 10

 | 

100%

 |
| 

＞ 10，≤ 20

 | 

50%

 |
| 

＞ 20

 | 

30%

 |

**事件发展顺序**

全球化产品要能正确显示 RTL 语言 (阿拉伯语、希伯来语、波斯语等)。

RTL (Right to Left，从右到左) 语言的普遍特征有：

事件发展顺序从右到左进行。

## 动效

层级跳转动效在 LTR 语言下，进入下一层级，跳转动效从右向左滑动；返回上一层级，跳转动效从左向右滑动；RTL 语言 (阿语) 层级跳转动效方向相反。

## 音效

音效不能出现宗教、政治等敏感音轨或音乐元素。

## 界面用语

**字体**

界面用语字体少用或慎用粗体、斜体、下划线等样式。

除网页超链接外，不建议界面文本使用下划线。

**默认语言**

海外产品无法匹配语言时，默认使用英文，因此设计时应基于英文进行设计。

**文本描述**

界面用语尽量采用简洁的描述。预留足够空间，避免某些语言出现文字截断。清晰完整度第一，美观第二。

**标点**

一般会基于英文将标点符号转换为本地方案。

注意某些语言的标点使用特点。

如：中文一般不用空格作为间隔。

**大小写**

界面用语本地化确保使用标准接口，基于语言类型，判断是否需要大小写转换。

## 其他

**排序和内容组织**

涉及字符排序或首字母分组时，不仅需要考虑「A-Z」规则，还需考虑如多音字 (中文)、变音符号等。

**ISO/CLDR/UTC**

基于 ISO 标准显示：日期、数字、货币、语言、复数、性别、键盘布局、区域代码等。

基于 CLDR 中各区域数值的格式显示。

基于 UTC 统一时间基础上，使各地用户能够清晰理解所表达的时间。

**周时间**

展开

| 
标准类型

 | 

每周第一天

 | 

适用地区

 |
| :-- | :-- | :-- |
| 

ISO 标准

 | 

星期一

 | 

亚欧大陆

 |
| 

北美标准

 | 

星期天

 | 

美洲大陆

 |
| 

伊斯兰标准

 | 

星期六

 | 

中东

 |

**长度单位**

仅美国、利比里亚、缅甸使用英制单位 (英里、英寸、加仑、盎司等)。其他国家或地区使用国际单位制 (即米制，又称公制)。中国香港、加拿大混合使用两种单位。

**温度单位**

包括我国在内的世界上绝大多数国家都使用摄氏度，世界上仅存 5 个国家使用华氏度，包含巴哈马、伯利兹、英属开曼群岛、帕劳、美利坚合众国及其他附属领土 (波多黎各、关岛、美属维京群岛)。

**货币**

货币要调用标准接口，配合本地语言使用。

**知识产权**

需要验证所有商标声明，确定获取当地运营所需要的知识产权和市场许可。
