# 文本选择菜单

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/textselection-0000001956842049
- 抓取时间：2026-04-04T08:23:19.080Z
选中的文本以高亮的文字块呈现，通过手柄来调整文本的选择范围。操作菜单置于文本之上。开发相关描述请参考 [bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#bindselectionmenu)和 [SelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu) 文档。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213501.51684604860217717961858440230750:50001231000000:2800:29B8888E4A77AD953D9FA81D3899A2AB87572F3BDED00651AF8C3D182DDEB0D5.jpg "点击放大")

## 如何使用

文本编辑时，需支持文本选择工具。例如信息、邮件、备忘录、浏览器等页面。

文本选择具备插件机制，可扩展功能。例如：安装了翻译软件，可动态增加选词翻译功能；安装了搜索软件，可动态增加搜索功能。

菜单主要功能：剪切，复制，粘贴和更多。选择“更多”时，变成二级菜单，显示更多操作。

菜单上的功能操作顺序：剪切，复制，粘贴，全选，翻译，分享，搜索，其他操作。文本选择强相关功能：“剪切”，“复制”，“粘贴”，“全选”，不放入“更多”中。

菜单上三方应用提供的操作，全部放到“更多”中。

## 视觉规格

**手机**

<table><tbody><tr><td><p><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213501.46162641714454467955317151365746:50001231000000:2800:8832367444E470A2F96FF51CC44882F5DECE12C0666C31068501422C2EEEDA46.png" title="点击放大" height="267.38589211618256"></span></p></td><td><p><span><img originheight="1920" originwidth="1928" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213501.08050735198329512627605329567799:50001231000000:2800:00E2F9B6B1CEA7E87FF99C1B37E572908618F65BA4DA242DFC6267BF67F4C32C.png" title="点击放大" height="267.38589211618256"></span></p></td></tr><tr><td><p>文本选择菜单</p></td><td><p>点击”更多“图标出现二级菜单</p></td></tr></tbody></table>

**电脑设备**

<table><tbody><tr><td><p><span><img originheight="1282" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213501.23174445973059980871707258034731:50001231000000:2800:DF5E73D4B9CD9DE9EDFC8756A6819EFC121F29ABD8512AA760AF37FDC29108B5.png" title="点击放大" height="179.2796875"></span></p></td><td><p><span><img originheight="1518" originwidth="1424" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213501.13855547099636951994662320274925:50001231000000:2800:C67C817FFD22A94ED48A76B9A6AC29CC99D64F14A3992CFE4EC61F08E3F7EB1F.png" title="点击放大" height="286.2240168539326"></span></p></td></tr><tr><td><p>文本二级菜单</p></td><td><p>带字体编辑的文本选择</p></td></tr></tbody></table>

**设备差异**

<table><tbody><tr><td><p><span><img originheight="1632" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213502.33098381226851972019827970418272:50001231000000:2800:B60F072B883BB9E5F7C819F4E3384650DC4E02A703C55FDC227E3F7FFAA27076.png" title="点击放大" height="228.225"></span></p></td><td><p><span><img originheight="1282" originwidth="1920" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20250619213502.32680122049220024957124098076816:50001231000000:2800:FEBCC83FAAEA41A34DF11472E642FB88C415D142C45C8E217001EB65721C0B80.png" title="点击放大" height="179.2796875"></span></p></td></tr><tr><td><p><strong>触控操作</strong></p></td><td><p><strong>鼠标操作</strong></p></td></tr></tbody></table>

<table><tbody><tr><td><p><strong>特性</strong></p></td><td><p>手机</p></td><td colspan="2"><p>电脑设备</p></td></tr><tr><td><p><strong>样式</strong></p></td><td><p>文本有手柄</p><p>菜单横向显示</p></td><td colspan="2"><p>文本无手柄</p><p>菜单上下文菜单显示</p></td></tr><tr><td><p><strong>翻译、搜索等扩展功能</strong></p></td><td><p>“更多”里</p></td><td colspan="2"><p>二级菜单</p></td></tr><tr><td><p><strong>可配置项</strong></p></td><td><p>翻译、扩展等功能</p></td><td colspan="2"><p>除翻译、扩展等功能外，还支持可配置项，具体见“菜单”</p></td></tr><tr><td><p><strong>交互</strong></p></td><td><p>点击</p></td><td colspan="2"><p>见“菜单”控件</p></td></tr></tbody></table>

## 开发文档

[SelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu)

[bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#bindselectionmenu)
