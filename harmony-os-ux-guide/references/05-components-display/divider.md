# 分隔器

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/divider-0000001956815469
- 抓取时间：2026-04-04T08:22:57.894Z
分隔器主要用于区分不同内容元素和组别，可用于列表或界面布局。分割线相关基础属性配置参考 [Divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-divider) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105550.37617872242100269474110279333438:50001231000000:2800:0D93D83B7148C30E0970651F3962067E3828589FC49B2AD491F85C0797A1F071.png "点击放大")

## 如何使用

**明确分类与使用场景。**分隔器是一个可动态定义的展示类组件，开发者可以配置控件的颜色、宽度以及高度，用于不同使用场景。一般情况下，系统界面中对分隔器的使用分为两类：分隔条和分割线。分隔条属于层级较高且显示面积更大的分隔器类型，主要用于成组模块的区分或是有明确功能分类差异的界面结构。分割线的使用场景更为普遍，层级结构也更低，对于界面的布局影响以及显示影响也更小。

<table id="ZH-CN_TOPIC_0000001956815469__table2248135134216" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956815469__row1524895117422"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815469__p67952155434">使用分割线区分列表布局</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815469__p5248115110427"><span><img originheight="960" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105550.46576773390620797275864947557738:50001231000000:2800:675FF7138D2EBBF12B01386F97E30BD5FF4FDDFA47B0EC41A42F12376DE3AAB9.png" title="点击放大" width="268.5" height="179"></span></p></td></tr></tbody></table>

**不要影响层级结构。**无论使用分割线还是分隔条，应避免将该组件展示在内容的最上方或最下方。分隔器作为区分内容的组件，如果内容相邻的布局没有可区分的内容，则不展示。

**合理定义展示参数。**不要定义过粗的分割线和分隔条。无论是哪种分隔器类型，其目的都在于提示用户，可以通过 [strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-divider#strokewidth) 来对分隔器的粗细进行配置。除此之外，请使用低对比度的色彩，可以使用不透明度对色彩进行处理。

<table id="ZH-CN_TOPIC_0000001956815469__table163651203446" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001956815469__row73661908446"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815469__p527010884416">分割线默认使用 1px 高度</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001956815469__p93661503445"><span><img originheight="960" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105550.16845569829765416551967914356416:50001231000000:2800:30356CF2B19EEFB2280EC7FDBDCCBC77C8CB46324A1541C8FFC6A6C980F57BA1.png" title="点击放大" width="268.5" height="179"></span></p></td></tr></tbody></table>

**智能穿戴****分隔器**

分隔不同内容块/内容元素。可用于列表或界面布局。分为分割条和分割线。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105550.82393874900659689410037018541586:50001231000000:2800:0A6B3F5B25C28220D95FB9656F3BE17233599935E11E9830DE6F8A7443134AA4.png "点击放大")

**分割条**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105550.07562875641172579843185107125835:50001231000000:2800:CE572C5CFA5CBEA844673A09EC8985E018422FD5A539EB60541C2BB32B32AB2C.png "点击放大")

**分割线**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250819105550.81273498445534975470675206178649:50001231000000:2800:8AEC82678A8A2D9B560C660C838404FC9D439EB3B64730D66C2B52976B5A5C5E.png "点击放大")

## 开发文档

[Divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-divider)
