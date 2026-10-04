# font-family 实际声明名称

font-family 必须以 CDN CSS 中 @font-face 实际声明的名称为准。名称错误时 CSS 仍返回 200，但页面会回退到系统字体。

| 字体中文名 | ❌ 错误 family | ✅ 正确 family（CSS 实测） |
|-----------|---------------|-------------------------|
| 抖音美好体 Bold | `Douyin Sans` | `DouyinSans`（无空格） |
| 爱点风雅黑 | `爱点风雅黑` | `Aidian FengYaHei` |
| 摇醒青年黑 | `摇醒青年黑` | `摇醒青年黑1.0`（带版本后缀） |
| 阿里妈妈东方大楷 | `MaShanZheng` | `Alimama DongFangDaKai` |
| 极影毁片辉宋 | `极影毁片辉宋` | `极影毁片辉宋 Bold` |
| 香萃端庄宋体 | `香萃端庄宋体` | `XCDUANZHUANGSONG` |
| 寒蝉活宋体 | `寒蝉活宋体` | `ChillHuoSong_F` |
| 猫啃网风雅宋 | `猫啃网风雅宋` | `MaoKenWangFengYaSong` |
| 荆南缘默体 | `荆南缘默体` | `Kingnamype Yuanmo SC` |
| 江西拙楷 | `江西拙楷` | `jiangxizhuokai` |
| 女书梧桐 | `女书梧桐` | `Nyushu Firmia` |
| 江城圆体 | `江城圆体` | `JiangChengYuanTi` |
| 莫妮卡像素圆体 | `X12Y16PX Maru Monica` | `x12y16pxMaruMonica` |
| 猫啃珠圆体 | `Maoken Zhuyuan Ti` | `MaokenZhuyuanTi` |
| 悠哉字体 | `Yozai` | `Yozai Medium` |
| 站酷文艺体 | `站酷文艺体` | `zcoolwenyiti` |
| 点点像素体-方形 | `点点像素 方` | `点点像素体-方形` |
| 无界黑 | `无界黑` | `Unbounded Sans` |
| 金字社扁正体 | `金字社扁正体` | `JinzisheBianzheng` |
| 金字社真好体 | `金字社真好体` | `JinzisheZhenhao` |
| 纳米扁界黑 | `纳米扁界黑` | `NanoByongGyeHei` |
| 典迹悦动 | `典迹悦动` | `Monu YueDong` |
| 卓特悦动黑 | `卓特悦动黑` | `ZT YueDongHei` |
| 写意体 | `写意体` | `YShi-Written` |
| 荆南麦圆体 | `荆南麦圆体` | `Kingnammm Maiyuan 2` |
| WD-XL 滑油字 | `WD-XL 滑油字` | `WD-XL Lubrifont SC` |
| 江城解星体 | `江城解星体` | `JiangChengJieXingTi` |

## 验证方法

1. DevTools → Network 打开 CSS，查看 @font-face 中的 font-family。
2. 执行 `document.fonts.load('20px "family名"', '目标文字')`，确认返回数组非空且 status 为 loaded。
3. 在 DevTools 的 Rendered Fonts 中确认目标文字实际使用的字体。
