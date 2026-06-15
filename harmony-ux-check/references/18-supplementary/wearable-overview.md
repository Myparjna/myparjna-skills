# 概述

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/wearable-overview-0000002197410498
- 抓取时间：2026-04-04T08:24:48.220Z
智能穿戴已经成为继手机之后，用户生活中极为重要的贴身辅助设备，是我们的生活助手，健康管家，亦是运动教练。

如果要设计出优秀的智能穿戴应用，需要熟悉并充分利用智能穿戴设备特性，这些特性包括硬件特征、使用方式、交互方式、使用场景等。

<table id="ZH-CN_TOPIC_0000002197410498__table1923817395221" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000002197410498__row328393982220"><td class="cellrowborder" valign="top" width="14.719999999999999%"><p id="ZH-CN_TOPIC_0000002197410498__p152832039182217">硬件特性</p></td><td class="cellrowborder" valign="top" width="85.28%"><p id="ZH-CN_TOPIC_0000002197410498__p1628323962211">屏幕：中等至高分辨率的小屏幕。</p><p id="ZH-CN_TOPIC_0000002197410498__p028363972210">音频：较好的音频输入输出能力。</p><p id="ZH-CN_TOPIC_0000002197410498__p122831339142220">地理位置：可通过GPS等获取设备所在的地理位置。</p><p id="ZH-CN_TOPIC_0000002197410498__p7714154083719">传感器：一般配备心率监测、血氧饱和度监测等。</p><p id="ZH-CN_TOPIC_0000002197410498__p228333919229">其它：陀螺仪、加速计等，可获得设备运动状态的信息。</p></td></tr><tr id="ZH-CN_TOPIC_0000002197410498__row22837391224"><td class="cellrowborder" valign="top" width="14.719999999999999%"><p id="ZH-CN_TOPIC_0000002197410498__p17283103914223">使用方式</p></td><td class="cellrowborder" valign="top" width="85.28%"><p id="ZH-CN_TOPIC_0000002197410498__p32831739172214">手表一般穿戴在手腕上，穿戴设备操作采用以下方式：</p><p id="ZH-CN_TOPIC_0000002197410498__p228433922213">· 左手或右手佩戴，另一只手点击操作</p><p id="ZH-CN_TOPIC_0000002197410498__p5284339182215">· 单手操作</p></td></tr><tr id="ZH-CN_TOPIC_0000002197410498__row18284939182214"><td class="cellrowborder" valign="top" width="14.719999999999999%"><p id="ZH-CN_TOPIC_0000002197410498__p728414398228">交互方式</p></td><td class="cellrowborder" valign="top" width="85.28%"><p id="ZH-CN_TOPIC_0000002197410498__p1528413391227">智能穿戴的交互方式是触屏手势与物理按键（表冠及按键），随着语音识别和AI能力的增强，语音交互也变得越来越普遍。</p><p id="ZH-CN_TOPIC_0000002197410498__p1328483912226">当双手操作不方便时，用户也可以通过佩戴的手进行操作。</p></td></tr><tr id="ZH-CN_TOPIC_0000002197410498__row1128433910222"><td class="cellrowborder" valign="top" width="14.719999999999999%"><p id="ZH-CN_TOPIC_0000002197410498__p1284339122213">使用场景</p></td><td class="cellrowborder" valign="top" width="85.28%"><p id="ZH-CN_TOPIC_0000002197410498__p20284183918222">智能穿戴的使用场景主要是生活、运动和健康场景。除此之外，智能穿戴还是用户的腕上装饰品。</p></td></tr></tbody></table>

## 应用设计

在设计智能穿戴应用时，请考虑以下方法，这将帮助您提供优秀的用户体验。智能穿戴设备相比其他大屏幕设备具有独特的应用场景，在设计时需要结合产品小而轻的特征做场景适应性分析。

### 保证基础体验

-   **即时通知：**智能穿戴的天然跟随属性，受时间、空间影响因素较小，有利于即时提醒和告知与用户相关的消息。另外需要考虑部分场景下重复、无效的通知对用户造成的干扰，根据用户真实的佩戴情况做通知处理。
-   **轻量交互：**智能穿戴手表小而轻，应该专注重要且主要的功能体验。同一应用内容，智能穿戴应该发挥移动优势，做其他大屏幕设备的补充和延伸，而非替代者。在具体应用设计中，需要根据智能穿戴手表的尺寸大小、使用场景做轻量化定制，并满足当前设备应用界面易浏览、交互流程易操作。

### 设计应用体验

-   **使用系统控件：**利用系统提供的导航栏、按钮及导航点等标准控件，在保证良好基础体验的同时，减少设计和开发的工作量。必要时自定义控件的样式和大小以体现自己的品牌特征。请参阅控件-[概览](https://developer.huawei.com/consumer/cn/doc/design-guides/general_overview-0000001929599380)。
-   **使用合适的应用架构：**根据业务的特点采用合适的架构。例如，单一功能类应用采用页面横向或纵向平铺的平级架构，以确保主要功能在首屏展示。请参阅[应用架构](https://developer.huawei.com/consumer/cn/doc/design-guides/application-architecture-0000002202799801#section4983154519514)。
-   **保证页面正常显示：**合理根据智能穿戴的屏幕形状进行界面设计，确保界面正常显示，不影响用户的使用。
-   **充分利用表冠和按键交互：**除屏幕手势交互外，表冠和按键交互能够帮助用户在需要盲操场景下快速完成特定操作。例如单击表冠快速开始/暂停运动等。请参阅[表冠](https://developer.huawei.com/consumer/cn/doc/design-guides/human-machine-interaction-0000002167648022#section02103311681)。
-   **考虑单手操作：**在特殊情况下，用户不得不单手对穿戴设备进行操作，应用在设计界面时，应考虑将核心功能适配焦点响应，使用户能够单手操作。请参阅[智慧手势](https://developer.huawei.com/consumer/cn/doc/design-guides/human-machine-interaction-0000002167648022#section239618496133)。
-   **跨设备体验连续：**手机与手表在部分关联任务上存在延续性。任务进行时，界面需要实时引导用户移至相应配对设备进行相关操作。在整个任务延续过程中，多端侧状态的同步和显示要尽量保持一致或关联性。例如添加 eSIM 账号时，可通过手表向手机发送指令，打开界面。

### 支持系统特性

-   **充分利用系统特性：**HarmonyOS 提供了一些系统特性，用户能够通过这些系统特性获得良好的系统体验，其中部分系统特性是开放的，应用可以根据业务属性接入这些系统特性，以获得更多触达用户的机会。例如出行应用可以通过服务卡片来传递状态信息。请参阅[系统特性](/consumer/cn/doc/design-guides/wearable-overview-0000002197410498#section1890474311418)。
-   **遵循系统特性的体验要求：**在接入系统特性时，要遵循系统特性的体验要求。

## 系统特性

-   [通知](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-notification-0000001793074217)
-   [实况窗](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-live-view-0000001955186861)
-   [服务卡片](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-service-widget-0000002087671904)

## 符合HarmonyOS统一设计规范

-   **色彩：**智能穿戴根据穿戴设备应用的特殊性，对部分色彩如系统色进行调整适配。请参阅[色彩](https://developer.huawei.com/consumer/cn/doc/design-guides/color-0000001776857164)。
-   **应用图标：**智能穿戴内的应用图标基本遵循HarmonyOS 应用图标的设计规范，但对于具体绘制规格有所不同，如使用圆形图标。请参阅[应用图标](https://developer.huawei.com/consumer/cn/doc/design-guides/application-icon-0000001953444009)。
-   **系统图标：**智能穿戴内的系统图标基本遵循HarmonyOS 系统图标的设计规范，但在穿戴应用设计中，建议更多使用面性图标以提高小屏幕内容的识别度。请参阅[系统图标](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。
