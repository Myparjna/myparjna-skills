# 选择器

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/picker-0000001956852749
- 抓取时间：2026-04-04T08:23:29.573Z
当需要从单个维度或多个维度进行组合做选择时使用。月历视图日期选择器开发相关描述请参考 [CalendarPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker) 文档。滚动选择器开发相关描述请参考 [DatePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker)、[TimePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker)、[TextPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker)文档。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/5eEfrkszTcCuxVCyI3Hi0Q/zh-cn_image_0000001957104701.jpg?HW-CC-KV=V1&HW-CC-Date=20260404T082327Z&HW-CC-Expire=86400&HW-CC-Sign=674C4B06D040147B5D0D53B0E9ADC529EAB0450213C4E659729F9096DC096F97 "点击放大")

## 如何使用

**通过选择不同的 Picker 组件实现对应效果。**组件提供 TimePicker、DatePicker、TextPicker 三种组件类型，特殊的 Picker 内容可以通过 TextPicker 自定义实现。

**在 CustomContentDialog 内添加 Picker 组件以实现与弹出框的组合。**弹出框组件详细指导见 [Dialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box) 。

<table id="ZH-CN_TOPIC_0000001956852749__X1bef174d8f20d58f2f3d4d5974384d532e23752" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956852749__row132mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001956852749__p3843143614719"><span><img originheight="4160" originwidth="4160" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/SE79emdZQjuz22IIbMxl7A/zh-cn_image_0000002103699257.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FD9B4CE20C6C098C4284476C3D1E6EB0025D65D98C0C7C02F8CD8D627ACEB08" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001956852749__p3817712226"><span><img originheight="4160" originwidth="4160" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/P0rjqvsrQcmktXwvSttDpw/zh-cn_image_0000002068382284.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EF0C006FD51133B0FFDBBD7802BCE15F1B46628B9A9FE10A59E1CA47A2F8DAE" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001956852749__p84630112816"><span><img originheight="4160" originwidth="4160" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/rAKH9JxlTFm_d1skJw0Wxg/zh-cn_image_0000002103579425.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33E5DA0C695331E7421B00AE6382E67F69796EE48D8795F80C49B29C49A67680" title="点击放大" width="162.33333333333331" height="162.33333333333331"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row139mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001956852749__p141mcpsimp"><strong>TimePicker</strong></p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001956852749__p143mcpsimp"><strong>DatePicker</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%"><p id="ZH-CN_TOPIC_0000001956852749__p145mcpsimp"><strong>TextPicker</strong></p></td></tr></tbody></table>

## 类型

<table id="ZH-CN_TOPIC_0000001956852749__X9aaebcf7c70b81290307e60e0bce774cba36c0d" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956852749__row112mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p1921722211213"><span><img originheight="4160" originwidth="4160" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/TersiU8zS_Cw1lPjmRIyJQ/zh-cn_image_0000002104382297.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78194948FCC25BC6749A72DAF063D490A553DA2188C66592291A57EF84B918FC" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p8815181913102"><span><img originheight="2080" originwidth="2080" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/CxfdrTjZQKe7E-sx4rA6PA/zh-cn_image_0000002103704637.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=130A5A7B4B3A4A529D499D54EB2A1919F146FC519BBAFC7A9BF5C57FE24B0B73" title="点击放大" width="268.5" height="268.5"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row117mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p119mcpsimp"><strong>滚动选择器</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p121mcpsimp"><strong>月历视图日期选择器</strong></p></td></tr></tbody></table>

**电脑设备**

月历选择

月历时间段选择

<table id="ZH-CN_TOPIC_0000001956852749__X4c54d0cdd73ec1a174d9830cd4724527641e8cb" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956852749__row151mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p4161848113618"><span><img originheight="2124" originwidth="2124" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/iSeqcw6yQr2lAJz45f-otg/zh-cn_image_0000002103552413.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1CDD200338DB6DEF70F9DD04B8D1FBD1C95D2E5B6F43CE57C194059A4A1D259" title="点击放大" width="268.5" height="268.5"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p1552164511314"><span><img originheight="2562" originwidth="4236" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/b18KMbVNTPW0cjwYYljSWw/zh-cn_image_0000002103667857.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DCA016B357010ADECE09643092E5B23AFF79BEF35AF2F7005C60922B1D2C389" title="点击放大" width="268.5" height="162.39305949008497"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row156mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p158mcpsimp"><strong>单个月历日期面板，用于选择日期。</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p160mcpsimp"><strong>连月历日期面板，在选择日期段时使用。</strong></p></td></tr></tbody></table>

**月历选择**

<table id="ZH-CN_TOPIC_0000001956852749__table17896151323" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956852749__row4789915143218"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p2663551133812"><span><img originheight="2108" originwidth="2436" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/vYRWV67ASVqewYg1ZYEjCg/zh-cn_image_0000002067873966.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082327Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F15CA297257D66442F46518B2DDFB4D96CE7B87A277FFABB5ED4743E6D37FC07" title="点击放大" width="268.5" height="232.3472906403941"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row679012155324"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956852749__p131890297328"><strong>电脑必选月历日期选择入口</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>

<table id="ZH-CN_TOPIC_0000001956852749__X793d3f7373c4f23d04d23e0155c3cdd196fa6f6" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956852749__X7ec89b96cbbd38e08f04d0de9241664f1ec5bd0"><td class="cellrowborder" valign="top" width="12.2%"><p id="ZH-CN_TOPIC_0000001956852749__p181mcpsimp"><strong>序号</strong></p></td><td class="cellrowborder" valign="top" width="17.07%"><p id="ZH-CN_TOPIC_0000001956852749__p183mcpsimp"><strong>元素名称</strong></p></td><td class="cellrowborder" valign="top" width="70.73%"><p id="ZH-CN_TOPIC_0000001956852749__p185mcpsimp">描述</p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row186mcpsimp"><td class="cellrowborder" valign="top" width="12.2%"><p id="ZH-CN_TOPIC_0000001956852749__p188mcpsimp"><strong>1</strong></p></td><td class="cellrowborder" valign="top" width="17.07%"><p id="ZH-CN_TOPIC_0000001956852749__p190mcpsimp"><strong>入口触发方式</strong></p></td><td class="cellrowborder" valign="top" width="70.73%"><p id="ZH-CN_TOPIC_0000001956852749__p192mcpsimp">电脑必选，手机端可自定入口触发方式</p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row193mcpsimp"><td class="cellrowborder" valign="top" width="12.2%"><p id="ZH-CN_TOPIC_0000001956852749__p195mcpsimp"><strong>2</strong></p></td><td class="cellrowborder" valign="top" width="17.07%"><p id="ZH-CN_TOPIC_0000001956852749__p197mcpsimp"><strong>标题区</strong></p></td><td class="cellrowborder" valign="top" width="70.73%"><p id="ZH-CN_TOPIC_0000001956852749__p199mcpsimp">显示选中的年月，单箭头切换月份，双箭头切换年。</p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row200mcpsimp"><td class="cellrowborder" valign="top" width="12.2%"><p id="ZH-CN_TOPIC_0000001956852749__p202mcpsimp"><strong>3</strong></p></td><td class="cellrowborder" valign="top" width="17.07%"><p id="ZH-CN_TOPIC_0000001956852749__p204mcpsimp"><strong>内容区</strong></p></td><td class="cellrowborder" valign="top" width="70.73%"><p id="ZH-CN_TOPIC_0000001956852749__p206mcpsimp">显示日期选项，可左右滑动，可配置显示农历。</p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row207mcpsimp"><td class="cellrowborder" valign="top" width="12.2%"><p id="ZH-CN_TOPIC_0000001956852749__p209mcpsimp"><strong>4</strong></p></td><td class="cellrowborder" valign="top" width="17.07%"><p id="ZH-CN_TOPIC_0000001956852749__p211mcpsimp"><strong>操作区</strong></p></td><td class="cellrowborder" valign="top" width="70.73%"><p id="ZH-CN_TOPIC_0000001956852749__p213mcpsimp">操作为“取消”，“确定”，电脑可选。</p></td></tr><tr id="ZH-CN_TOPIC_0000001956852749__row214mcpsimp"><td class="cellrowborder" valign="top" width="12.2%"><p id="ZH-CN_TOPIC_0000001956852749__p216mcpsimp"><strong>5</strong></p></td><td class="cellrowborder" valign="top" width="17.07%"><p id="ZH-CN_TOPIC_0000001956852749__p218mcpsimp"><strong>容器</strong></p></td><td class="cellrowborder" valign="top" width="70.73%"><p id="ZH-CN_TOPIC_0000001956852749__p220mcpsimp">弹出框。</p></td></tr></tbody></table>

**智能穿戴滑动选择器**

当需要从单维度或多个维度单选进行组合做选择时使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/n-MSmRhPTQOsxTImVmL84w/zh-cn_image_0000002348861249.png?HW-CC-KV=V1&HW-CC-Date=20260404T082327Z&HW-CC-Expire=86400&HW-CC-Sign=DAFB9C63D2791A7F0CBE61A6C817AAA3671BB614CD31521AACAED307805D69B1 "点击放大")

**时间选择器**

时间选择器使用弹出框或者内嵌的方式，在智能穿戴上选择单个时间（小时:分钟:秒的格式）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/wjb2deZXR9CvrYnFRG0YdQ/zh-cn_image_0000002314784336.png?HW-CC-KV=V1&HW-CC-Date=20260404T082327Z&HW-CC-Expire=86400&HW-CC-Sign=16CE4BD87D96F425351836ABAFC4444D8199D2C0E877A2200E6649D64B8C4ECC "点击放大")

例如设置闹钟/计时器

**其他选择器**

· 通常有两种：数字选择器，文本选择器。

· 数字选择器默认按从小到大排序。

· 根据选择项的属性选择合适的默认选项，以减少大多数用户的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/S7Y-VSaoSRqSoT50yPrquQ/zh-cn_image_0000002314946736.png?HW-CC-KV=V1&HW-CC-Date=20260404T082327Z&HW-CC-Expire=86400&HW-CC-Sign=F43D2F7ED519260CC2BBB1CF532950190EDA353DF0027DD8273EC9ADF49B258A "点击放大")

例如设置熄屏时间/高度校准

## 开发文档

[DatePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker)

[TimePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker)

[TextPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker)

[CalendarPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker)
