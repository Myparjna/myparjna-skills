# 轻量高效

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-overview-0000001939183197
- 抓取时间：2026-04-04T08:24:21.664Z
## 导航清晰，入口明确

1）导航应该提供清晰的路径。用户使用的时候，能够知道当前处在界面的什么位置，操作后将会跳转到什么位置。建议开发者直接调用元服务官方提供的导航栏 ([AtomicServiceNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation)) 控件。提供以下3种样式：纯文本/图形文本、品牌Logo、品牌Logo+名称文本。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165250.45257060555382422677976274002590:50001231000000:2800:C52C4C851A1C6D22AB58B1A093541197613CF44CFF567E1F8EBFB0F179D56C64.png "点击放大")

若开发者选择自行设计开发导航样式，请确保导航简洁清晰，避免以下设计：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165251.30570967998235367842682926995802:50001231000000:2800:CDCFED9E2282D878F32EA7FF1605880B613C61D425027AED505E47844EF2CF0D.png "点击放大")

2）次级页面左上角的返回键交互行为统一定义为“返回上一层”，而非“返回前一个界面”。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165252.20403017411647928884242597816012:50001231000000:2800:91F74B2B574DC7D25EC9EC48A958118D7FB95FC2189EA27C5C5F99623AC8E0E2.png "点击放大")

3）元服务所有界面的标题栏右侧，会统一放置元服务胶囊（Menubar）。开发者在界面设计中请注意合理避让该区域，避免功能冲突。整个标题栏区域的信息应保持简洁易识别，元服务胶囊左侧请勿放置功能图标。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165252.43338345160932669348124810811442:50001231000000:2800:829F56C18DC17967F7B93054B64D042CEC4BFEE7B3753E0C526F0FFFC64F5986.png "点击放大")

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165253.69561045179472694530961073454481:50001231000000:2800:73B91E77A5163D9F12655EEDF42BA964388BEC5F01C47BE922406DF130FDD276.png "点击放大")

4）每个界面中功能的入口和出口必须明确、清晰、稳定， 通过界面元素，帮助用户清晰认知界面层级和当前所在位置。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165254.70011674348684851505646240729185:50001231000000:2800:6B696E99DAC249475BBD553882A94429206FA3BB6702B4AA5771753BA5DDB492.png "点击放大")

## 轻量架构，高效触达

1）轻量架构：元服务的信息架构应保持简洁轻量，界面中只提供对用户有核心价值的内容。

① 一级页面通过底部页签对内容进行组织架构，一级页面顶部导航栏不再使用多页签对内容进行分类。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165254.34392798775783791319851932802808:50001231000000:2800:2D22415C93D81DEA64EE5B228E84DC130765B349EB8DD97F018FE5CE3D104ED5.png "点击放大")

② 元服务底部页签的数量最多不超过5个，最少不少于2个，若页签数量超过上限，建议重新对元服务信息架构进行组织梳理。建议开发者直接调用元服务官方提供的底部页签 ([AtomicServiceTabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicetabs)) 控件，图标/文本样式均支持自定义。

运营图标配置规则：支持在底部页签上配置运营图标，图标运营位最多一个。若底部页签数量为单数，则运营位需位于最中间的页签上。若底部页签数量为双数，则运营位可位于任意页签。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165255.60463382006250696982261358454294:50001231000000:2800:DD51B69F1AAF94219DF625FEC6AEFA2691FD097FD4BBAFC31166082FD023EB50.png "点击放大")

2）功能高效触达：核心功能的关键操作在首屏可发现、易操作。

功能操作是否易发现，可以从复杂操作入口是否有提示、入口发现的困难度这几个维度考虑设计。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165257.89718586465793908836836449900387:50001231000000:2800:008D04536926F3BEF3B93839AD138BB6B969BE4F6CA5441D1DCC105D9F02678B.png "点击放大")

3）页面层级合理：界面跳转关系与转场效果符合层级逻辑，浅层操作减少界面跳转。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165257.10759136699499902930027495831049:50001231000000:2800:233FDA51E18F7106A8A338C2E23FE5001BE400F140C96A01F6AA19588B7FBF76.png "点击放大")

## 直觉交互，符合预期

1) 遵循基础交互与手势，屏幕边缘左右滑动返回与退出。

2) 操作合理性：

① 遵循基础交互与手势，屏幕边缘左右滑动返回与退出。

② 可见性(状态、变化、内容可见)，任何操作都有实时反馈。

③ 不要假设用户的推理能力，要设想用户偏好简单易懂的操作。

④ 运用同理心来衡量设计是否符合用户心智模型，确保交互控件的行为和意图符合用户认知。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165258.19816129473174008773056904897421:50001231000000:2800:3AA36D7E79BC730298AC02A68BCC1DD645E683C5A3CCC75E7B1A33FAF00F66F7.png "点击放大")

3）内容易理解性：界面中的图标、提示信息易于理解，一看就懂。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165258.33661585285507423581602937948577:50001231000000:2800:89A67D3871ADBB579091856469B846D3FA9EE5C9012190D181AABBBA7C4D6D9C.png "点击放大")

4）体验连贯性：使用过程中不应被弹窗、跳转等打断主流程。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165259.71676394829075199738887095098875:50001231000000:2800:5657808472440C8373E2F925C3159E065354DF61E68707FD6DDFBC57044FF138.png "点击放大")

## 容错防呆，消除歧义

1）为用户提供简单易学的引导和提示，降低出错概率。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165259.89558820563905560642921336212024:50001231000000:2800:F3495E1DD98E4D36B674F2A054C3A95704BBFFADB0BDA313E0BB9B0B23579F3D.png "点击放大")

2）不可避免出现错误时，除了告知操作失败，应该给出解决方案的建议。如无网络时，引导用户去设置网络；内容获取失败时，引导用户点击屏幕重试。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165300.84884670130767456530675924706601:50001231000000:2800:A35728DD46639D3614E84245CA5D6BF8AF55499875D7311A5B73444C093F1EA0.png "点击放大")

3）任何需要用户等待的操作，都需要提供暂停或取消的方式。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165301.94279338332750310387366635034215:50001231000000:2800:0A97C1A723F3C8EE97BE12D67E35CC8650A7C6C9FC2A1C47162C72EE4E6B07B3.png "点击放大")

## 友好表达，通俗易懂

1）使用用户容易理解的自然语言，避免技术术语词汇与生僻的缩写。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165301.49211136497821052994214591120886:50001231000000:2800:2C8649DC0B25590FAB72B8EBA691798479D91BA0A0CF8C3B9C3797333DE08EA3.png "点击放大")

2）运营性质的界面用语，避免诱导性用语引导用户点击。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165302.12983360714295905968005541446366:50001231000000:2800:ABEA9E163EB959D1A3BEFF91072F286766CD502676D863581F03604B781249E6.png "点击放大")

## 及时反馈，缓解等待

数据的获取和加载时长应尽可能缩短，以避免用户长时间等待。当不可避免地出现需要加载和等待的场景时，需提供及时的反馈以缓解用户的等待焦虑。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250624165302.49244434316819025976515111122216:50001231000000:2800:202B26A021BD54389A2A19AE41243B4AA31F24B87380D8689674DEAC6EFB4C94.png "点击放大")
