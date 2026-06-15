# 手机

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/phone-0000001776694632
- 抓取时间：2026-04-04T08:24:28.103Z
手机是用户最常使用的设备，用户使用手机来进行社交、娱乐、购物、理财等各项活动，手机已经渗透到用户工作和生活中的方方面面，系统、应用和服务体验的好坏对用户至关重要。

如果要设计出优秀的手机应用或服务，需要熟悉并充分利用手机的设备特性，这些特性包括硬件特征、使用方式、交互方式、使用场景等。

<table id="ZH-CN_TOPIC_0000001776694632__Xd6c5d12bacfd94807e653e37bbfc69d9c5cc874" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001776694632__row109mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001776694632__p111mcpsimp">硬件特性</p></td><td class="cellrowborder" valign="top" width="85%"><p id="ZH-CN_TOPIC_0000001776694632__p113mcpsimp">屏幕：高分辨率的中等大小屏幕。</p><p id="ZH-CN_TOPIC_0000001776694632__p114mcpsimp">摄像头：一般配备非常好的后置摄像头和较好的前置摄像头。</p><p id="ZH-CN_TOPIC_0000001776694632__p115mcpsimp">音频：较好的音频输入输出能力。</p><p id="ZH-CN_TOPIC_0000001776694632__p116mcpsimp">生物认证识别：一般配备指纹、人脸等。</p><p id="ZH-CN_TOPIC_0000001776694632__p117mcpsimp">地理位置：可通过 GPS 等获取设备所在的地理位置。</p><p id="ZH-CN_TOPIC_0000001776694632__p118mcpsimp">其他：陀螺仪、加速计等，可获得设备运动状态的信息。</p></td></tr><tr id="ZH-CN_TOPIC_0000001776694632__row119mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001776694632__p121mcpsimp">使用方式</p></td><td class="cellrowborder" valign="top" width="85%"><p id="ZH-CN_TOPIC_0000001776694632__p123mcpsimp">用户通常会随身携带手机，随时随地进行使用，根据习惯和场景单手或双手握持，主要竖屏使用，在需要时会切换至横屏。用户使用手机时与手机距离通常在 30 厘米左右。</p></td></tr><tr id="ZH-CN_TOPIC_0000001776694632__row124mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001776694632__p126mcpsimp">交互方式</p></td><td class="cellrowborder" valign="top" width="85%"><p id="ZH-CN_TOPIC_0000001776694632__p128mcpsimp">手机的主要交互方式是触屏手势，随着语音识别和 AI 能力的增强，语音交互也变得越来越普遍。</p><p id="ZH-CN_TOPIC_0000001776694632__p129mcpsimp">当进行多设备协同时，用户也可能用鼠标在手机和其他设备之间进行拖拽交互。</p></td></tr><tr id="ZH-CN_TOPIC_0000001776694632__row130mcpsimp"><td class="cellrowborder" valign="top" width="15%"><p id="ZH-CN_TOPIC_0000001776694632__p132mcpsimp">使用场景</p></td><td class="cellrowborder" valign="top" width="85%"><p id="ZH-CN_TOPIC_0000001776694632__p134mcpsimp">手机的使用场景非常广泛，从通过 AOD/锁屏查看时间，到花几个小时看文章、刷短视频、看长视频等，手机几乎可以胜任在任何场景和任务中使用。</p></td></tr></tbody></table>

## 应用和服务设计

在设计手机应用和服务时，请考虑以下方法，这将帮助您提供优秀的用户体验。

### 保证基础体验

在应用/服务设计中需要遵守一些基础体验要求，如果不满足这些基础要求，则会极大损害用户的使用体验。例如，如果界面元素的响应热区太小会导致用户很难操作成功，从而无法完成要操作的任务。具体要求请参阅[应用 UX 体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-overview-0000001760867048)。

### 设计应用和服务体验

-   **使用系统控件：**利用系统提供的底部页签、标题栏、弹出框等标准控件，在保证良好基础体验的同时，减少设计和开发的工作量。必要时自定义控件的样式和大小以体现自己的品牌特征。
-   **使用合适的应用架构：**根据业务的特点采用合适的架构。例如，内容类应用通常采用底部页签的应用架构，以达到快速在不同类别的内容间切换的作用。
-   **保证页面正常显示：**在合理的场景下支持横屏显示，并针对挖孔进行适配，以保证页面正常显示，不影响用户的使用。
-   **考虑单手操作：**在很多情况下，用户不得不单手握持手机进行使用，应用/服务在设计界面时，应考虑将核心功能放在单手容易触达的区域，使用户能够在单手握持时正常地使用。
-   **尽量不使用多指手势：**手机屏幕一般较小，因此尽量不要使用两指以上的多指手势，在小屏幕上进行多指操作难度较大，很容易失败，会带来较差的用户体验。
-   **充分利用硬件特性：**手机集成了人脸识别、指纹、陀螺仪、加速计等多种硬件能力，可以帮助用户方便地获取某些特定的信息，在合理的场景下通过这些能力获取的信息，可以减少用户操作的负担，提升使用体验，如通过人脸或指纹识别来进行锁屏解锁。

### 支持系统特性

-   **充分利用系统特性：**HarmonyOS 提供了一些系统特性，用户能够通过这些系统特性获得良好的系统体验，其中部分系统特性是开放的，应用/服务可以根据业务属性接入这些系统特性，以获得更多触达用户的机会。例如，外卖应用/服务可以通过实况窗特性实时向用户传递外卖快递的状态。关于手机系统体验清单，请参阅[系统特性](/consumer/cn/doc/design-guides/phone-0000001776694632#section1083190143115)。
-   **遵循系统特性的体验要求：**在接入系统特性时，应用/服务要遵循系统特性的体验要求。例如，在接入实况窗时需要按照模板来设计实况窗的布局和信息，以保证用户使用实况窗特性的良好体验。部分系统特性是为了满足用户对系统整体的某项诉求，应用/服务也应当遵循系统特性的规则进行接入。例如，当用户切换至深色模式时，希望系统中的所有应用/服务都能进行切换，应用/服务应该跟随系统的设置，实时切换至深色显示。

## 系统特性

-   [导航条](https://developer.huawei.com/consumer/cn/doc/design-guides/navigation-0000001957075737)
-   [通知](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-notification-0000001793074217)
-   [实况窗](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-live-view-0000001955186861)
-   [多窗口交互](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-multi-window-interaction-0000001795392917)
-   [画中画](https://developer.huawei.com/consumer/cn/doc/design-guides/pip-0000001927422624)
-   [深色模式](https://developer.huawei.com/consumer/cn/doc/design-guides/dark-mode-0000001823255497)
-   [状态栏](https://developer.huawei.com/consumer/cn/doc/design-guides/status-bar-0000001776775568)
-   [播控中心](https://developer.huawei.com/consumer/cn/doc/design-guides/broadcasting-control-0000001957017133)
