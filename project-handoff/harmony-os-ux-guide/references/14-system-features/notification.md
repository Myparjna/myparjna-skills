# 通知

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-notification-0000001793074217
- 抓取时间：2026-04-04T08:23:52.462Z
通知旨在让用户以合适的方式及时获得有用的新消息，帮助用户高效地处理任务。

## 通知设计原则

-   为用户提供有价值的通知内容信息。
-   不要重复发送相同内容的通知打扰用户。
-   采用规范布局，不允许自定义复杂布局，以保证通知体验的一致性。
-   不要将通知作为小工具或广告板使用。
-   不要出于商业目的强制改变属性 (如采用实况窗强制置顶显示)，避免损害用户使用体验。

<table id="ZH-CN_TOPIC_0000001793074217__table1944861762719" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001793074217__row1448911713274"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000001793074217__p9638448292"><span><img originheight="976" originwidth="976" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161037.75394390272369857459692037676689:50001231000000:2800:3F0362857BF2369A2604620DA7482B1E44A791488F188A12990BB0FCCAB8C58B.png" title="点击放大" width="162.33333333333337" height="162.33333333333337"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000001793074217__p1453221315308"><span><img originheight="976" originwidth="976" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161037.12438390193175820136206478751804:50001231000000:2800:CCF7A013EE701BDF6EBD55D035487968734E405A7C57104DDE3B5F0949A4708D.png" title="点击放大" width="162.33333333333337" height="162.33333333333337"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000001793074217__p1449884203011"><span><img originheight="976" originwidth="976" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.07352991217714977104022217039566:50001231000000:2800:A974F2FA6C181DEAC58FFFFE894D8D26CEA61936B57EBEA0B9A32430800C24C3.png" title="点击放大" width="162.33333333333337" height="162.33333333333337"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001793074217__row10490101792713"><td class="row-nocellborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000001793074217__p3490191710278">避免自定义复杂布局，破坏通知一致性</p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000001793074217__p17490131762717">不要将通知作为小工具或广告板使用</p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.333333333333336%"><p id="ZH-CN_TOPIC_0000001793074217__p1749041792710">不要强行置顶通知</p></td></tr></tbody></table>

## 通知详情

### 单条通知

**单条通知的基本元素包括图标、主副文本、时间：**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.61660399459545401022152224023428:50001231000000:2800:FC79B3773422225DC9E8D114BF7E9B361B13A09D5C2998976E574AB7E1F5DADC.png "点击放大")

**通知元素**

1.  通知图标：表示通知的功能与类型，由系统统一获取应用或元服务图标。
2.  通知标题：通知内容的简要概括或功能描述。避免直接使用应用或服务的名称。
3.  时间：发送通知的时间，系统默认显示。
4.  内容详情：描述通知的具体内容或详情。最多显示 3 行，超长则“…”截断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.15516799027766058226589603222460:50001231000000:2800:DA8CD44333F1E80FF11C2407AE349C21B13F979A5F8FAF1F8CC3D806375DB370.png "点击放大")

**交互规则**

点击整条通知跳转至对应的详情界面。

### 组合通知

**应用如果发送多条通知，在同一分区内的则需设为一条组合通知。**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.77733012914062923792954631291660:50001231000000:2800:70F38A3B5DAA8371E9CFD35C5A0AB7079B43A7536BEA7C371F35CA78AECC57F3.png "点击放大")

**展开前**

1.  通知图标：表示该组通知的来源，由系统统一获取应用或元服务图标。
2.  通知内容：最新 3 条通知的标题及内容详情。
3.  时间：最新 1 条通知的时间。
4.  条数示意：表示未显示通知的数量，超过 3 条的显示 “ + N”，如为 2-3 条则无此示意。

**展开后**

5.标题区：该组通知的图标、名称和收起箭头。

6.内容区：每条子通知的标题和内容详情。

## 模板样式

### 普通通知

默认采用 3 行普通通知样式。

<table id="ZH-CN_TOPIC_0000001793074217__table199911156203616" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001793074217__row899155673618"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001793074217__p3886192873"></p><p id="ZH-CN_TOPIC_0000001793074217__p1299195618366"><strong>单条通知</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001793074217__row499165653613"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001793074217__p17991056153618"><span><img originheight="294" originwidth="1572" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.03958806665905923769715137247294:50001231000000:2800:BC5DB875FF85D393E0FA182DFD627208A69E7050780623799254CE4439C9A9E8.png" title="点击放大" width="587" height="109.78244274809161"></span></p></td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000001793074217__table1264314263387" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001793074217__row36431726183812"><td class="cell-norowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001793074217__p160mcpsimp"><strong>单条内容超三行</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001793074217__row46442268383"><td class="cellrowborder" style="border: none;" valign="top" width="100%"><p id="ZH-CN_TOPIC_0000001793074217__p5644182612385"><span><img originheight="342" originwidth="1572" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.28699399449020580127496838883507:50001231000000:2800:94F8EBD15C83351C9AE32D2502C2438EC7B02B82D7E5A794806E1F995827FCE1.png" title="点击放大" width="587" height="127.70610687022902"></span></p></td></tr></tbody></table>

### 图片预览通知

适用于有图片预览的通知。

-   图片建议为方形、高质量的图片，其他形状可能会导致内容被裁切。
-   图片需要与通知内容强相关，避免使用与内容无关的图片。
-   不要使用与应用图标重复的图片。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.14971430527344570262284293227378:50001231000000:2800:1813DBDF852BACEE52F1B17FFDAE2ED3F599433D0460635B097E09D37F423BBF.png "点击放大")

### 通讯对话类通知

适用于通讯类或对话类的通知，左侧显示用户头像。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.08360380098949928385027497930911:50001231000000:2800:3F166079C01FF65F1CF32AC50E84C995B7A221F7572605B80B8D8FD6A856681B.png "点击放大")

### 多行文本类通知

适用于需要换行显示的文本内容。

最多可显示 3 行内容详情，每行超长后 “…” 截断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.95768085233767829371605518998771:50001231000000:2800:B5C4D04FD37454EF86A9136F3A885B89F838883EE9466ADD39CB7E2FE3955C26.png "点击放大")

## 通知提示场景

**通知会在不同场景以不同形式提示用户。应用发出一条通知时，可配置通知的提示场景。**

开发指南请参阅[Push Kit简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-kit-introduction)

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.06482491020492175413972992922454:50001231000000:2800:C71BE1DEF11DB173082401730AE6B6716DF8171A1D1521137801405396BD4011.jpg "点击放大")

1.  通知中心：通知浏览界面，通知在通知中心中根据类别排序，每个类别内按时间排序。
2.  锁屏通知：锁屏上仅显示本次锁屏期间接受的通知，显示样式默认为底部图标和数量，可展开成列表。
3.  横幅通知：在界面顶部显示 5s 后消失，非沉浸态显示 3 行高度，沉浸态显示 1 行高度。
4.  桌面图标角标：角标表示本应用或元服务有消息，消息与通知中心的内容不对应，由服务方自己定义。
5.  通知图标：以图标形式显示在状态栏、AOD 界面。

### 通知中心

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.51470219324236356176657932226266:50001231000000:2800:9DEF934DCCA31C7AF3F64760427F75E08B4E096EBFA1D1D1065DFC600E6BDE7F.png "点击放大")

1.  实况窗显示在通知中心顶部，分区内按创建时间排序。
2.  重要通知包括通讯社交和服务提醒类通知，排在实况窗后面，分区内按时间排序。
3.  内容资讯类通知显示在更多通知分区，分区内按时间排序。
4.  通知默认在通知中心显示，应用无需配置。

### 锁屏通知

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161038.03081091994271383722141146733886:50001231000000:2800:B2F256490981A9466F9FEA85C138A51E46DDD1E546FCF68FBCB50746133EA6D9.png "点击放大")

-   锁屏上仅显示本次锁屏期间接收的普通通知。
-   打开 “锁定时显示预览” 开关，通知内容不会被隐藏。
-   应用可配置通知是否显示在锁屏上。锁屏通知受到通知设置中提醒方式的管控。

### 横幅通知

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161039.63206755085200324890424735352539:50001231000000:2800:528A5019E9535F48E2DA04D967F3A811F65A1F302A5123F5F369AD67C861B197.png "点击放大")

1.  横幅通知为高提示性场景，仅开启了横幅提醒方式的应用可生效。
2.  横幅通知在界面顶部显示 5s 后消失。例外：来电、闹钟类横幅通知为长时间停留。
3.  同时接收多条横幅通知时，仅显示最新一条通知。
4.  非沉浸态界面显示 3 行副文本的通知高度。
5.  沉浸态界面下，通知显示单行高度。

### 桌面图标角标

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161039.62365776454976666608255907506874:50001231000000:2800:7CFCDB326E1CC147633FF05E495D10DB6F51148381F7AD30E46850F69FD0C181.png "点击放大")

-   桌面图标角标为数字角标。
-   数字角标是应用新消息的提示，不完全对应通知。
-   数字角标最多显示 “99 + ”。

### 通知图标

-   通知以图标形式显示在状态栏等位置，与通知卡片图标为同一资源。
-   通知图标由系统取应用或服务的图标。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161039.43206545497138909386628167822965:50001231000000:2800:5C508ADDCA59C0349D451A449D6604867785FD5FF4AE8D49CB4CC9E1A3FC591A.png "点击放大")

## 文本超长显示规则

### 通知标题

-   标题最多显示 22 个英文字符，或 15 个中文字。建议完整显示字串。
-   不支持换行，超过 1 行“…”截断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161039.99645420656706024198298303673958:50001231000000:2800:DB7412D6BB865FD4BD2E0D954C85EC6FD1D61FA5234022BEFAC9C43305E34043.png "点击放大")

### 通知内容详情

-   内容详情最多显示 84 个英文字符，或 57 个中文字。建议完整显示字串。
-   最多可显示 3 行，显示不下“…”截断。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20251030161039.97588138237798712222285499991241:50001231000000:2800:23CE476F1815E5F48774201DD091CF51ABAFCEFA5E765BE6E32E634BCD697EB5.png "点击放大")
