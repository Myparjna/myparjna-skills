# 二维码

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/qrcode-0000001929816020
- 抓取时间：2026-04-04T08:23:07.514Z
可将链接转换生成为二维码的样式来展示，用户使用设备扫描后即可获取链接地址或获得对应信息。相关开发能力参考 [QRCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-qrcode) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213443.60131239825233623586675985913188:50001231000000:2800:120668FA6DD96375DC892355B8C0A5B878CFC105955D2938378732F56D31CC75.jpg "点击放大")

## 如何使用

**二维码控件提供了基础的二维码生成能力，默认规格提供二维码和控件背景色。**开发者可以通过修改二维码的对应色彩参数来适配不同的界面样式。

**结合业务特性进行二次布局。**开发者可根据业务场景需要，选择基础样式或在二维码上增加其他图片样式进行使用。例如可以在账号场景呈现用户头像，或在应用下载场景提供应用图标样式。

**二维码在使用场景中会出现不同的使用状态，例如加载中、不可用状态等等，开发者可以结合业务场景需要自定义控件的交互行为。**需要注意的是，如果控件提供了多种状态，同样需要给出对应的界面布局和状态样式区分，例如通过透明度或色彩配置的方式形成对比。

<table><tbody><tr><td><p><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213443.74165680560425896075452938907518:50001231000000:2800:396C1E55D5A9EEB806F17AA113151242E6E79307C49DDA4DB88C1CF099B04109.png" title="点击放大" height="109.25"></span></p></td><td><p><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213443.29869321363925608400016964225146:50001231000000:2800:CF546B26F85024ED542D85161338E8B23238DDE0D1618CC3228F0EF9959C9791.png" title="点击放大" height="109.25"></span></p></td><td><p><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213443.68983761748347344866029406528461:50001231000000:2800:A66BBB69F05370A98D4765A5450B431762C5C3C6A1BFBBF6BC60432AD78C4586.png" title="点击放大" height="109.25"></span></p></td><td><p><span><img originheight="800" originwidth="800" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213443.21661339823242875637995515283001:50001231000000:2800:17F1BE6C16ACC38BBD2449ECE1F125E1C44CE5C4DC87018A24A3EE9992B6268E.png" title="点击放大" height="109.25"></span></p></td></tr><tr><td><p><strong>基础样式</strong></p><p>仅二维码本身</p></td><td><p><strong>带图片样式</strong></p><p>用户头像、群组头像等</p></td><td><p><strong>带图片样式</strong></p><p>应用图标</p></td><td><p><strong>加载状态</strong></p><p>二维码置灰并显示加载动效</p></td></tr></tbody></table>

**自定义效果**

开发者可以根据自身业务需要配置不同的色彩风格来保证业务的个性化。

<table><tbody><tr><td><p><span><img originheight="1424" originwidth="1892" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213443.84273800017374115633260293616036:50001231000000:2800:69DF4FD2A9CFE9519C9DA5EBC04BAC005499EBE787B1C9DF4FB7DB45B46CD487.png" title="点击放大" height="122.17899929527835"></span></p></td><td><p><span><img originheight="1424" originwidth="1892" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213444.73205291879610456143163612723201:50001231000000:2800:FBAEA5F2E52637238FB4AAC89D3A22954F4E56CC31DC655DB21572869809762B.png" title="点击放大" height="122.17899929527835"></span></p></td><td><p><span><img originheight="1424" originwidth="1892" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213444.65110006449459770007782619162899:50001231000000:2800:7C44B1D5259E6415CB4CCAB0058A696FC0DF24394B904853BA5FEEB97910271B.png" title="点击放大" height="122.17899929527835"></span></p></td></tr></tbody></table>

## 界面布局

在界面中使用时，需要注意二维码控件本身带有一个背景色，如果控件本身与界面风格差异较大可能会造成色块较多的情况。二维码可以展示在全界面中，也可以展示在其他容器布局中，例如弹出框、半模态等等。

<table><tbody><tr><td><p><span><img originheight="1776" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213444.67139656040932774489901857051400:50001231000000:2800:FD35E8557E6FD7A344584106074298D4528710A0656BD27231B23A5C9BFCCF7F.png" title="点击放大" height="331.15000000000003"></span></p></td><td><p><span><img originheight="1776" originwidth="1440" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213444.99481846422323829462588742034322:50001231000000:2800:F432BD2B2CDB1BEE35ACAD190120BD17EE42C0E77F20C834F849F5FDD4697FBE.png" title="点击放大" height="331.15000000000003"></span></p></td></tr><tr><td><p><strong>全页面布局</strong></p></td><td><p><strong>弹出框内布局</strong></p></td></tr></tbody></table>

## 开发文档

[QRCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-qrcode)
