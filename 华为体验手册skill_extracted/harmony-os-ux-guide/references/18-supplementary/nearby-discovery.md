# 靠近发现

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/i-connect-0000002354482789
- 抓取时间：2026-04-04T08:24:13.605Z
用户可通过设备靠近，进行设备间的连接或协助新设备快速启用。可发现设备范围包括华为终端设备，鸿蒙智联设备以及开源鸿蒙 (OH) 智能生态设备。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224922.88285315572066501061805921246535:50001231000000:2800:3D99E1A54EFB86E1ADF6C1364CCFCF01C338349419DB8BBF793E8A17D1A66C01.png "点击放大")

## 基本分类与页面构成

可发现设备可以简单归结为两类，一类由华为终端设备和智联生态设备组成，另一类则为开源鸿蒙 (OH) 智能生态设备。界面主要由图片区域、文本区域以及按钮区域组成。

### 华为终端设备以及智联生态设备

华为终端设备包括耳机、音箱、手表、手机、平板、PC、智慧屏、车机。智联生态设备覆盖接入智慧生活 App 的生态设备。界面构成：有屏设备使用真实 ID+版本壁纸，无屏设备图使用真实 ID 图，与设备对应。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224923.03601045048050134435609704785379:50001231000000:2800:FC20F7E0DD34D778DD8BE9284DE92A1BCFCBD3B09F2CF1E5696E0C0B3563FCB8.png "点击放大")

### 开源鸿蒙生态设备

开源鸿蒙 (OH) 生态设备根据功能区分为摄像头类、网关类、商显类以及音箱类设备。界面构成：使用插画示意设备类型，生态需传入设备名称以及设备类型。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224923.84580117318362659441408835232353:50001231000000:2800:18790BEA34D6A85ADC891A3561BA22CA88A924346B77B5FD8E7D97C344B88D59.png "点击放大")

## 视觉规则

### 多端布局规范

手机端：竖屏图片区域宽度默认 328 VP，高度根据产品比例调整。横屏图片区域进行等比缩放，高度自适应，整体比例与竖屏一致。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224923.36212158526015667024857304732536:50001231000000:2800:BD24780B0D57DDBAC5D9AEBBE3359C30517E81B067BA2A16045BC8E1C64018C8.png "点击放大")

折叠屏以及平板：半模态宽度固定 480 VP，高度自适应。图片区域宽度默认 328 VP，高度根据产品比例调整。横竖屏保持一致。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224924.77373842929942977488831464955355:50001231000000:2800:DF2F5B8464D7E919966D77DD5F79284AB7EDD562D1CE0F9F51EEBC0772D9CB28.png "点击放大")

电脑：半模态宽度固定 480 VP，高度自适应。竖屏图片区域宽度默认 328 VP，高度根据产品比例调整。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224924.01964589634109379452555066055288:50001231000000:2800:073771265AB983B604712909786F5C6B43773B3473ABA421F5AA3E730A132211.png "点击放大")

### 文本区域规范

文本区域由标题和辅助文本构成 (生态设备连接弹框辅助文本默认展示为 “基于开源鸿蒙”)。

·标题文本大小：Title\_S (bold)

·标题文本颜色：font\_primary

·辅助文本大小：Body\_M (regular)

·辅助文本颜色：font\_secondary

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619224925.83934180717894415995371504375157:50001231000000:2800:80ED5CC1FE4C53AA28A562CB5AB11AF70F029CC820F4F6D6585703C22EB22F02.png "点击放大")
