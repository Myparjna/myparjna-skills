# 图案锁

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/patternlock-0000001929853902
- 抓取时间：2026-04-04T08:23:23.877Z
这是一种通过绘制图案的行为作为解锁方式的控件。开发能力相关可参考 [PatternLock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock) 文档。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Xo7-9Kl9TL-GNhu8nOGzBg/zh-cn_image_0000001930016406.jpg?HW-CC-KV=V1&HW-CC-Date=20260404T082321Z&HW-CC-Expire=86400&HW-CC-Sign=3A646739C0E5725767EFBD2BE21F036768AFE9A7BAF40C924BB1886022B44CD3 "点击放大")

## 如何使用

**图案锁作为一种输入类控件，与其他输入型组件最大区别在于通过手势绘制图形作为输入方式。**可用于界面锁屏、私密文件夹、密码验证等场景下使用。也可以和其他密码类型混合使用，如人脸识别、指纹可同时在锁屏解锁时和图案锁使用。

**搭配简要的文字说明。**图案锁的使用需要搭配一定的文本解释，让用户知道当前解锁状态。例如密码输入是否正确，还有几次输入机会等等。

**基于界面的使用场景差异定制适合的颜色样式。**图案锁可以使用在任何界面场景，对于纯色界面、沉浸式界面、包括深浅模式下都需要开发者匹配对应使用场景的颜色，确保界面的美观度。

## 基础构成及场景示意

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/MMkO8bWsTGKUhpj3uUU0_Q/zh-cn_image_0000001929857014.png?HW-CC-KV=V1&HW-CC-Date=20260404T082321Z&HW-CC-Expire=86400&HW-CC-Sign=957664B21B1050CE4AE878396D4D0AFAE33C6A092449115CD298C73BE54604B5 "点击放大")

<table id="ZH-CN_TOPIC_0000001929853902__X3cbaaaee81695ad04d16de2826311761f044533" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929853902__row118mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="ZH-CN_TOPIC_0000001929853902__p120mcpsimp">序号</p></td><td class="cellrowborder" valign="top" width="27%"><p id="ZH-CN_TOPIC_0000001929853902__p122mcpsimp">标题</p></td><td class="cellrowborder" valign="top" width="61%"><p id="ZH-CN_TOPIC_0000001929853902__p124mcpsimp">描述</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853902__row125mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="ZH-CN_TOPIC_0000001929853902__p127mcpsimp">1</p></td><td class="cellrowborder" valign="top" width="27%"><p id="ZH-CN_TOPIC_0000001929853902__p129mcpsimp">操作提示文本</p></td><td class="cellrowborder" valign="top" width="61%"><p id="ZH-CN_TOPIC_0000001929853902__p131mcpsimp">位于图案锁圆点的上方，用于提示操作。</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853902__row132mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="ZH-CN_TOPIC_0000001929853902__p134mcpsimp">2</p></td><td class="cellrowborder" valign="top" width="27%"><p id="ZH-CN_TOPIC_0000001929853902__p136mcpsimp">图案锁圆点</p></td><td class="cellrowborder" valign="top" width="61%"><p id="ZH-CN_TOPIC_0000001929853902__p138mcpsimp">用于连接形成图案的圆点。</p></td></tr><tr id="ZH-CN_TOPIC_0000001929853902__row139mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="ZH-CN_TOPIC_0000001929853902__p141mcpsimp">3</p></td><td class="cellrowborder" valign="top" width="27%"><p id="ZH-CN_TOPIC_0000001929853902__p143mcpsimp">次要操作提示文本</p></td><td class="cellrowborder" valign="top" width="61%"><p id="ZH-CN_TOPIC_0000001929853902__p145mcpsimp">位于图案锁圆点的下方，常用于提示异常操作。</p></td></tr></tbody></table>

**锁屏场景**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/NGn1t1vZTa-Iv9QvNOMBRw/zh-cn_image_0000001957015657.png?HW-CC-KV=V1&HW-CC-Date=20260404T082321Z&HW-CC-Expire=86400&HW-CC-Sign=4AC6C6C693AFCBA7EA98EF7F98D64812FC6D86AF7B87EB4CB039A7EC6FA2DBA7 "点击放大")

**图案录入场景**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/GsETK2eWQeGwo5fCtNGqNQ/zh-cn_image_0000001957095849.png?HW-CC-KV=V1&HW-CC-Date=20260404T082321Z&HW-CC-Expire=86400&HW-CC-Sign=7698BC9A15DEBB51B7104A577C658487B92C81EF162F9DDF42F78F8EE54D9F0C "点击放大")

## 开发文档

[PatternLock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock)
