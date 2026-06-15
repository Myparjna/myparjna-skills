# 子页签

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/chipsgroup-0000001929788350
- 抓取时间：2026-04-04T08:22:50.460Z
子页签控件是展示在应用程序顶部的切换类控件，主要用于在一个组件内切换不同页面内容。在移动端产品上，页签名称应简洁明了，清晰描述分类的内容。在系统中我们提供了传统的下划线样式子页签，开发相关可参考 [Tabs/SubTabBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs) 文档，此外，还有新增胶囊形态子页签，可定义样式及交互规格更丰富，可参阅 [ChipGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup) 描述文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213419.31784761508676611142232417835844:50001231000000:2800:CE58FFE1D6B7908C8199810896666DF4C50B376F181080801185C9A4FED83F46.jpg "点击放大")

## 交互规则

**提供状态反馈**

无论使用系统默认效果，还是通过自定义来实现属于应用自己风格的控件样式，用户都需要在子页签上收到操作的即时反馈，响应时间需小于用户可接受的等待时间，激活状态需要明显区分于其他未激活样式。

**文本信息简练且直接**

控制文本信息的数量，避免文本过长导致阅读困难，在手机等设备上，屏幕宽度可展示的信息非常有限，文本信息过长会直接导致页签的展示数量减少。当文本较长且屏幕内无法展示完整时，请大胆的超出屏幕展示区域，同时提供左右滑动的交互能力，为用户提供可扩展的交互能力。在展示数量的控制上，单一界面的子页签展示数量建议为 3-5个，数量过多会增加产品复杂度，并降低每个标签的可操作空间。

**精简组件结构**

应用出于商业考虑，可能会在子页签右侧添加可操作内容，例如增加搜索入口、子页签的数量编辑入口、子页签排序入口等，这些行为都可能增加界面交互的复杂程度。因此，尽可能少的在复杂界面布局中额外增加入口图标，通过优化界面整体的应用架构，将更高频的入口布局在标题栏区域或是单独提供其他成组的宫格入口。

**使用 HarmonyOS Symbol 来展示图标信息**

在 ChipGroup 中可以替换系统 [Symbol](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs) 样式来更灵活的展示图标信息，这种方式更匹配文本的展示效果，同时提供点击反馈，更直接的展示界面设计的细节。开发者可以在 [HarmonyOS Symbol](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol/) 开源网站上查询目前已经存在的图标样式。

**样式类型**

子页签的类型分为传统下划线样式和胶囊样式，下划线样式提供了横向和竖向两种规格，竖向规格可以通过 配置 [Vertical](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#vertical) 属性来切换。在新增的胶囊样式中，提供了可以多选的规格，开发者可以通过配置 ChipGroup 中的 [Multiple](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup#chipgroup-1) 属性来定义此规格。

<table id="ZH-CN_TOPIC_0000001929788350__X657bee60b2f8530986b2ffa4341f3911894f599" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929788350__row129mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929788350__p131mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213419.81604298264421347032441591578314:50001231000000:2800:156E4284B79BFF6AE635D86A815E6456649F0BE03991BDC63577769A8E82947C.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p41931460540"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213419.18772266424407959242163053589122:50001231000000:2800:9803A032F4E3EA731E555C09EC9C68601DF0F272C1098CBFB98FC8E1AE814C6C.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929788350__row134mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p136mcpsimp">胶囊样式 - 单选</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p138mcpsimp">胶囊样式 - 多选</p></td></tr><tr id="ZH-CN_TOPIC_0000001929788350__row5684164685619"><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001929788350__X5ebfb260f706525c8447b948ee9a79d8fb13205"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p121338184"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213419.65551077128315206918654244155237:50001231000000:2800:2F165A1832C15EDA35ED6630D09511EA8079EB8BBF59D01405923425A651319C.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p class="msonormal" id="ZH-CN_TOPIC_0000001929788350__p142mcpsimp"><span><img originheight="960" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213420.11493354817880920332306331765647:50001231000000:2800:B5F81A979E5654AE96EC7ED901E9418EAEE0ADB2BE3DC161D64A7C0907FD804C.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929788350__row143mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p145mcpsimp">下划线样式 - 横向</p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p147mcpsimp">下划线样式 - 竖向</p></td></tr></tbody></table>

## 视觉规则

在子页签的整体设计上，建议使用品牌色对激活的子页签进行色彩填充，可以保障应用界面整体风格的统一。除此之外，开发者也可以使用特殊的设计样式和形态进行自定义，充分表现应用的个性化。同时，不要使子页签之间的间距过大，会造成界面布局过于稀疏，同时占用了大量的可操作空间。

ChipGroup 提供了两种尺寸规格可供选择普通尺寸和小尺寸，通过 [ChipsItemStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup#chipitemstyle) 中的 Size 属性进行配置可直接获得。

<table id="ZH-CN_TOPIC_0000001929788350__table051141710574" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001929788350__row35126171573"><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p3512101785719"><span><img originheight="720" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213420.86704309452051998288942528181711:50001231000000:2800:8E546B6D4E9270FBA4948E62F2F892DEF58D43D20ADCAD5B62A36583E21E623D.png" title="点击放大" width="268.5" height="134.25"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p55122175575"><span><img originheight="720" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213420.68448563775109722718649783694003:50001231000000:2800:51C3319E300F7D3537E77404FB0D87DA0F0F3E59403E236110983FB62D32FD38.png" title="点击放大" width="268.5" height="134.25"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000001929788350__row651261711573"><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p851217172578"><strong>默认尺寸规格</strong></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001929788350__p161mcpsimp"><strong>小尺寸规格</strong></p></td></tr></tbody></table>

**手机**

在手机场景下存在横屏规则，若你的应用也需要适配横屏场景，可以考虑按照标准规格拉伸适配，也可以考虑通过分栏来区分界面结构，子页签在其可用区域内，按栅格化规则布局。

横屏拉伸场景

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213420.52131774293351391398390838269172:50001231000000:2800:82A8C4AB49C0C5B3BCFEBD7C6FF836BFE377F5280681F386DAC55E2B5B3168D0.png "点击放大")

横屏分栏场景

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213420.94319297140942060866583408429342:50001231000000:2800:52A6E5FB3F3C7593D0E35D2D7A25226B12682371F84AC25AD21DF0E552E98D7C.png "点击放大")

**折叠屏**

子页签的通用规则同样适用于折叠屏设备场景，对齐规则与手机侧一致，开发者可以针对更大尺寸设备定义更宽的边距，来保证界面内展示元素是始终对齐的。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213420.65364870374002132663792047659172:50001231000000:2800:A7AAD58CE39CFDF49EB1EDAC37E9D68783E9C4D2309214BEA3C332CBEAC7F39B.png "点击放大")

**平板**

在平板及更大尺寸屏幕时，子页签的使用规格保持不变，但在界面整体布局上可以尝试使用分栏布局。区分一级和二级目录结构，确保界面内容展示时不会被拉伸或出现展示异常。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213420.59309114083344027274884640603998:50001231000000:2800:FFC5BB3FEF6CDDA4CC614734965D4B0456B0BE82038FFFBCB0AF4BD79CCD9F87.png "点击放大")

## 开发文档

[ChipGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup)

[Tabs/SubTabBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)
