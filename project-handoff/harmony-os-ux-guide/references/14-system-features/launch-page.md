# 启动页

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/system-capabilities-launch-page-0000002311335748
- 抓取时间：2026-04-04T08:24:11.038Z
内容类应用启动页是用户开启应用时最先看到的界面。其承担传递品牌形象、获取用户必要权限（如存储、位置、相机等）的重任。设计时，需遵循鸿蒙系统规范，适配各设备屏幕特性，确保快速加载，自然融入授权流程，避免打断用户体验，为用户打造流畅且高效的应用启动开端。

## 最佳实践

**简洁高效**

-   启动页应避免复杂内容，仅展示必要元素（如应用 Logo 或品牌标识）。
-   保持静态设计，减少使用动画或交互元素，以确保快速加载。

**视觉连贯**

-   启动页的设计应与应用首页（如主界面或引导页）风格一致，减少视觉跳跃感。
-   建议使用相同背景色、复用核心视觉组件（如品牌色、图标），确保平滑过渡。

**多设备适配**

-   基于设备或断点布局类型，提供对应启动页配置资源，确保在不同设备上观感最佳。
-   优先使用系统能力提供的启动页布局能力，确保在鸿蒙设备上的启动布局自适应。

**纯净展示**

-   启动页尽量避免包含促销信息、广告或第三方品牌内容，需专注于品牌展示。
-   启动页是短暂延迟，0.3-0.8秒内最佳，延长显示时间会降低体验。

## 启动页资源规格

启动画面的可自定义元素包括应用图标、图标背景和窗口背景。

展开

| 
规格

 | 

维度

 | 

说明

 |
| :-- | :-- | :-- |
| 

必备组件

 | 

配置背景颜色

 | 

可选纯色/渐变/图片背景，需适配多分辨率与安全区，不可透明

 |
| 

可选组件

 | 

App Icon/插画

 | 

可为透明

 |

## 结构分类

**纯图标类**

为进一步强化业务品牌属性，开屏的沉浸式背景色为应用定义的主题色，大多数情况下可以与 icon 背板色彩进行呼应。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201424.26070602016586533709280925766653:50001231000000:2800:AED0562B9D50F623F027FD5A41E5268B912A6A0C58376B5C00E0A18FEF7D57C0.png "点击放大")

纯图标类的需提供图标分层资源，系统会根据默认规格进行缩放适配与界面布局。

**上下布局类**

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201424.49927030983863805590503434186089:50001231000000:2800:0FAB7DA2E7B1C61F30A5CC0FC15E5B8281455301082E26155660DBDA48A9EDB3.png "点击放大")

上下布局类的需提供图插画和品牌标识资源，系统会根据默认规格进行缩放适配与界面布局。

## 多设备适配

当前设备种类繁多，基于断点规则，确保在合适的设备上提供最优的用户体验，同时兼顾不同设备的适配性需求。有关指南，请参阅[布局](https://developer.huawei.com/consumer/cn/doc/design-guides/design-layout-basics-0000001795579413)

图标类

上下布局类

展开

| 
设备/场景

 | 

图例

 |
| :-- | :-- |
| 

穿戴手表

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201424.66732555042240400865466158590613:50001231000000:2800:1B35FE4E250AF03B52F238BAA4F10813C3D3BD68A1B43667712DA29B918D41CD.png "点击放大")

 |
| 

手机竖屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201424.83779975932019179014346531422967:50001231000000:2800:6CEE71369C1A317B916B76CCCDAC0BEE732E539C787D3AEC391A846088228873.png "点击放大")

 |
| 

手机横屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201424.42865310768006054658617608187697:50001231000000:2800:5A4744D0B4461C4E2C3ABB49E6F3BFCA6BBA524290C77DEB0D052C0DA33EB526.png "点击放大")

 |
| 

阔折叠竖屏、阔折叠外屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201425.42195612530173462477113374093285:50001231000000:2800:A93D1D37C8FD1959267EC98076DF956A2E943836B2A47233792CAE9559FFA238.png "点击放大")![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201425.06410883268675586731099553783367:50001231000000:2800:097251C41D99E8448AD6665FA3A35509313AC3A37EC3B06E16E8846295606BC8.png "点击放大")

 |
| 

阔折叠横屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201425.92546858538768555108113729906294:50001231000000:2800:2BAAAE21A33B84699544E079CE9BC21E5A771B65D36B305807C8BBF6C79E66B1.png "点击放大")

 |
| 

折叠屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201425.01497981361944633547574352842603:50001231000000:2800:6932A84B38964E2010C3A4836C5B2B7DD07C883BC914428C9B56CC51DB29DCF3.png "点击放大")

 |
| 

平板竖屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201425.90635543967379888918487174125883:50001231000000:2800:2F655183E525E367CFB4C3F3782EAC09F2FF905C3C913E0A7E3F2661123C3784.png "点击放大")

 |
| 

平板横屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201425.41123526586331065124913625169822:50001231000000:2800:6F6915A21F61BAC6CC0938B2F8D81F4A74DF6371756394FF6FAA480610E9F606.png "点击放大")

 |
| 

电脑

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201425.86741991989828319475605003836189:50001231000000:2800:7633971EC2854DFC05CCCDAC502CBAAC54E36DF0EE952406D00E23C99B2F0769.png "点击放大")

 |

展开

| 
设备/场景

 | 

图例

 |
| :-- | :-- |
| 

穿戴手表

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.26434306959403579638906306725645:50001231000000:2800:4499BE29D3D7C2AB2090165A8F965ECC1A55898CCCCE99FE6065428CE9E70958.png "点击放大")

 |
| 

手机竖屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.33902023786730278785064662767426:50001231000000:2800:EC902C8130F82D77CE19C587543CB8BF5115DCA8AC16061A388192D47833CABA.png "点击放大")

 |
| 

手机横屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.20766740401347520224929853053884:50001231000000:2800:FB30DC83D0C1A118902E2E5C5DD3175603F104AFB70D192990A2179D90CE8A3E.png "点击放大")

 |
| 

阔折叠竖屏，阔折叠外屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.24371725654557531273702943835608:50001231000000:2800:E5F69854959DB1237C0A52AA8744B7B84EB41C520364A0A593F95CF868942E0B.png "点击放大")![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.44451577101707823260893687033971:50001231000000:2800:5306B5170333A6337418D78597523EF375E5978154BE4088B1375B4D7E15CCB7.png "点击放大")

 |
| 

阔折叠横屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.78057305837187033510457222151125:50001231000000:2800:5EFC4929D5B76D95364752AF707CAC94DA86D9763E7C977754E47F4C85003176.png "点击放大")

 |
| 

折叠屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.25863745326849152219698097777650:50001231000000:2800:17D1332E1A9C63D64FD9D2CB836E9C670042FFCEFE2B41D1C7BEC71704D8CFEA.png "点击放大")

 |
| 

平板竖屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201426.32757753725051872575139419091309:50001231000000:2800:6B11F1BEB3B1F3C4B3C4BBFC8E8B7FFD973B530473A5CC6ACB6EBF719212C7D0.png "点击放大")

 |
| 

平板横屏

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201427.99912801737374199555712888665905:50001231000000:2800:DAE82F4F82D04FB147A15C60DD4A115A6F78BC1252CAFF13F46BA03928495D4D.png "点击放大")

 |
| 

电脑

 | 

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201427.52280716365152330124677238846217:50001231000000:2800:98064C260BF4038294F91B3656E7A79EC5313255297C8C962DB30FDCA813793C.png "点击放大")

 |

## 深色模式

建议应用按照自身业务品牌色进行深色模式适配，确保资源结构类型与浅色模式一致，背景色最大限度降低亮度处理，可直接使用黑色。如果是插画类型，可适配深色模式插画资源。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250814201427.90767773176134149385168097953067:50001231000000:2800:5BAB54B0F99C87A357FA48031415A386BD0369AD40BD8AD0DAB25253F6D3E1EB.png "点击放大")

## 资源

请根据需要选择以下格式的设计模板和资源：

[启动页设计资源](https://developer.huawei.com/images/download/next/launch-page.zip)
