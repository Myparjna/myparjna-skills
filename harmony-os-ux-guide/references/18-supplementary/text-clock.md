# 文本时钟

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/textclock-0000001929656652
- 抓取时间：2026-04-04T08:23:08.884Z
通过文本形式显示当前日期或时间，支持 12 小时制或 24 小时制的日期或时间显示。相关开发能力可参考 [TextClock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textclock) 文档。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/hQWUP05TRe-NiJVgtoR2Kw/zh-cn_image_0000001929832132.jpg?HW-CC-KV=V1&HW-CC-Date=20260404T082306Z&HW-CC-Expire=86400&HW-CC-Sign=99D0B42017460A84AF9EBE6AA57BE3494440788F81CE7443FF2359A2DD568D80 "点击放大")

## 如何使用

以字符串格式实时显示当前的日期或时间。

**默认样式**

日期 (年月日星期) 与时间 (时分秒) 支持多种子样式拼装组合

<table><tbody><tr><td><p><span><img originheight="4464" originwidth="8240" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/-CJSt3m0Qm28d0qlwMVlxA/zh-cn_image_0000002133529881.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082306Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94C198BD532CA88F995A21626F9932521F1CF852DF245099F093A6E1A90C088D" title="点击放大" height="145.45922330097088"></span></p></td><td><p><span><img originheight="4464" originwidth="8240" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/YyP7wdbERbu-cFL5qIH3hA/zh-cn_image_0000002133450449.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082306Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5779E6BD6F3E112A1E7EBB4B773219AE6D818BDF99C5D1152BC9635AC8D0760F" title="点击放大" height="145.45922330097088"></span></p></td></tr><tr><td><p><strong>24 小时制</strong></p></td><td><p><strong>12 小时制</strong></p></td></tr></tbody></table>

**日期格式**

日期格式默认提供以下子样式供使用

<table><tbody><tr><td><p>默认样式</p></td><td><p>格式</p></td><td><p>效果</p></td></tr><tr><td><p>样式一</p></td><td><p>yyyy 年 M 月 d 日 EEEE</p></td><td><p>2023 年 2 月 4 日 星期六</p></td></tr><tr><td><p>样式二</p></td><td><p>yyyy 年 M 月 d 日</p></td><td><p>2023 年 2 月 4 日</p></td></tr><tr><td><p>样式三</p></td><td><p>M 月 d 日 EEEE</p></td><td><p>2 月 4 日 星期六</p></td></tr><tr><td><p>样式四</p></td><td><p>M 月 d 日</p></td><td><p>2 月 4 日</p></td></tr></tbody></table>

年、月、日支持简写或全写两种方式，星期默认应使用完整星期 (例如：星期六)，显示空间不足时才考虑使用简写星期 (例如：周六)。

<table><tbody><tr><td>&nbsp;&nbsp;</td><td><p>格式</p></td><td><p>效果</p></td></tr><tr><td><p>年</p></td><td><p>yyyy (完整年份)</p></td><td><p>2023 年</p></td></tr><tr><td>&nbsp;&nbsp;</td><td><p>yy (年份后两位)</p></td><td><p>23 年</p></td></tr><tr><td><p>月</p></td><td><p>MM (完整月份)</p></td><td><p>02 月</p></td></tr><tr><td>&nbsp;&nbsp;</td><td><p>M (月份)</p></td><td><p>2 月</p></td></tr><tr><td><p>日</p></td><td><p>dd (完整日期)</p></td><td><p>04 日</p></td></tr><tr><td>&nbsp;&nbsp;</td><td><p>d (日期)</p></td><td><p>4 日</p></td></tr><tr><td><p>星期</p></td><td><p>EEEE (完整星期)</p></td><td><p>星期六</p></td></tr><tr><td>&nbsp;&nbsp;</td><td><p>E、EE、EEE (简写星期)</p></td><td><p>周六</p></td></tr></tbody></table>

**自定义日期格式**

除默认样式外，也允许开发者自行拼接组合显示格式，即：年、月、日、星期可拆分为子元素，开发者可自行排布组合 (下表样式仅作示例，不作为默认样式提供)

<table><tbody><tr><td><p>自定义样式</p></td><td><p>格式</p></td><td><p>效果</p></td></tr><tr><td><p>示例一</p></td><td><p>MM/dd/yyyy</p></td><td><p>02/04/2023</p></td></tr><tr><td><p>示例二</p></td><td><p>EEEE MM 月 dd 日</p></td><td><p>星期六 02 月 04 日</p></td></tr></tbody></table>

日期间隔符提供以下几种格式供选择

\* 除以上间隔符样式外，也允许开发者自定义间隔符样式。例如：自定义间隔符为“，” 则显示为 2023，2，4

<table><tbody><tr><td><p>间隔符</p></td><td><p>格式</p></td><td><p>效果</p></td></tr><tr><td><p>年月日</p></td><td><p>yyyy 年 M 月 d 日</p></td><td><p>2023 年 2 月 4 日</p></td></tr><tr><td><p>/</p></td><td><p>yyyy/M/d</p></td><td><p>2023/2/4</p></td></tr><tr><td><p>-</p></td><td><p>yyyy-M-d</p></td><td><p>2023-2-4</p></td></tr><tr><td><p>.</p></td><td><p>yyyy.M.d</p></td><td><p>2023.2.4</p></td></tr></tbody></table>

**时间格式**

时间格式支持 24 小时制或 12 小时制两种显示方式，默认提供以下子样式供使用

\* 格式说明

-   H：小时 (0~23) h：小时 (1~12)
-   m：分钟
-   s：秒
-   SSS：毫秒
-   a：上午/下午 (仅在 12 小时制中有效)

<table><tbody><tr><td><p>默认样式</p></td><td><p>时制</p></td><td><p>格式</p></td><td><p>效果</p></td></tr><tr><td><p>样式一</p></td><td><p>24 小时制</p></td><td><p>HH:mm:ss (时:分:秒)</p></td><td><p>17:00:04</p></td></tr><tr><td>&nbsp;&nbsp;</td><td><p>12 小时制</p></td><td><p>aa hh:mm:ss (时:分:秒)</p></td><td><p>上午 5:00:04</p></td></tr><tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td><p>hh:mm:ss (时:分:秒)</p></td><td><p>5:00:04</p></td></tr><tr><td><p>样式二</p></td><td><p>24 小时制</p></td><td><p>HH:mm (时:分)</p></td><td><p>17:00</p></td></tr><tr><td>&nbsp;&nbsp;</td><td><p>12 小时制</p></td><td><p>aa hh:mm (时:分)</p></td><td><p>上午 5:00</p></td></tr><tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td><p>hh:mm (时:分)</p></td><td><p>5:00</p></td></tr><tr><td><p>样式三</p></td><td><p>/</p></td><td><p>mm:ss (分:秒)</p></td><td><p>00:04</p></td></tr><tr><td><p>样式四</p></td><td><p>/</p></td><td><p>mm:ss.SS (分:秒:厘秒)</p></td><td><p>00:04.91</p></td></tr><tr><td><p>样式五</p></td><td><p>/</p></td><td><p>mm:ss.SSS (分:秒.毫秒)</p></td><td><p>00:04.536</p></td></tr></tbody></table>

**自定义时间格式**

除默认样式外，也允许开发者自行拼接组合显示格式，即：时、分、秒、毫秒可拆分为子元素，开发者可自行调整顺序或设定显示格式。

<table><tbody><tr><td><p>自定义样式</p></td><td><p>格式</p></td><td><p>效果</p></td></tr><tr><td><p>示例一：上/下午放在时间后</p></td><td><p>hh:mm:ss aa</p></td><td><p>5:00:04 上午</p></td></tr><tr><td><p>示例二：只显示小时数</p></td><td><p>HH</p></td><td><p>17</p></td></tr></tbody></table>

**属性**

-   可配置时制 (12 小时制/24 小时制)
-   可配置时区
-   可配置文本大小、字重、颜色、样式 (继承 Text 的属性)
-   可配置文本时钟的背景颜色

<table><tbody><tr><td><p><span><img originheight="2936" originwidth="4364" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Yd8SsL0yRSWhOANwFMUkeQ/zh-cn_image_0000002097971358.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082306Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08B965D1E48A7DA5DC16617A714E862B4FF46B8DD78409390A57D0670FB02C3E" title="点击放大" height="109.21417659639472"></span></p></td><td><p><span><img originheight="2936" originwidth="4364" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/3r6oAbPLTdqI9lMBIrJjvg/zh-cn_image_0000002097971590.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082306Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B560C23B4C500053AA2AD051887B9A7111FF319B847BD14062C2671E3F0E164" title="点击放大" height="109.21417659639472"></span></p></td><td><p><span><img originheight="2936" originwidth="4364" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/a_AgZmuxRV2Pfws7gFNdxw/zh-cn_image_0000002133530513.png?HW-CC-KV=V1&amp;HW-CC-Date=20260404T082306Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D17F7D0FA182A952105537E6323317BC91E683330240342F555827BC2A1277D9" title="点击放大" height="109.21417659639472"></span></p></td></tr><tr><td><p><strong>浅色模式</strong></p></td><td><p><strong>深色模式</strong></p></td><td><p><strong>沉浸式模式</strong></p></td></tr></tbody></table>

## 开发文档

[TextClock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textclock)
