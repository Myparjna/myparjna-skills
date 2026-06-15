# 键盘

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/hmi-keyboard-0000001928070488
- 抓取时间：2026-04-04T08:23:42.368Z
键盘是一种重要的生产力输入设备，优秀的键盘使用体验应允许用户快速准确输入文本，双手无需离开键盘即可在系统和应用内使用导航、访问所有的功能以及保证无障碍体验，用户通常使用键盘快捷键一步直达某些功能。走焦顺序、走焦交互等设计原则请参考焦点导航章节。

## 快捷键设计策略和原则

### 设计策略

<table id="ZH-CN_TOPIC_0000001928070488__X9915a11056c88a0409170069731b8de055b86e4" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001928070488__row110mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.449999999999996%"><p id="ZH-CN_TOPIC_0000001928070488__p12653937113720"><strong>以传统电脑为兼容对象</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="52.55%"><p class="start(2)" id="ZH-CN_TOPIC_0000001928070488__p15578203533714"><strong>系统功能全局响应</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row115mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="47.449999999999996%"><p id="ZH-CN_TOPIC_0000001928070488__p117mcpsimp">传统电脑有最庞大的用户基础，遵循用户现有使用习惯优先，避免带来学习成本。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="52.55%"><p id="ZH-CN_TOPIC_0000001928070488__p119mcpsimp">保证系统功能全局响应快捷键操作。整体拉通 Pad 和电脑的功能定义，保证用户在 1+8 范围内操作易上手易学习。</p></td></tr></tbody></table>

### 设计原则

<table id="ZH-CN_TOPIC_0000001928070488__Xfca08893eb0ec3f9048dcf5f6ed12460f100656" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001928070488__row125mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.49%"><p id="ZH-CN_TOPIC_0000001928070488__p633814117374"><strong>取功能的英文单词首字母组合快捷键</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="52.51%"><p class="start(2)" id="ZH-CN_TOPIC_0000001928070488__p14891104213714"><strong>应用不能使用含 Logo 键的系统快捷键</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row130mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.49%"><p id="ZH-CN_TOPIC_0000001928070488__p132mcpsimp">面向高效办公人士的文化程度，基于最常见的英文单词首字母，选择含字母键的快捷键组合，便于用户理解记忆。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="52.51%"><p id="ZH-CN_TOPIC_0000001928070488__p134mcpsimp">保证系统级能力调用的稳定性和用户易理解，应用在自定义快捷键时不可调用系统 Logo 键。</p></td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row135mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.49%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="52.51%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row138mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.49%"><p class="start(3)" id="ZH-CN_TOPIC_0000001928070488__p1297084515377"><strong>快捷键组合控制至多 3 个键数</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="52.51%"><p class="start(4)" id="ZH-CN_TOPIC_0000001928070488__p934714442375"><strong>给常用功能分配快捷键</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row143mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.49%"><p id="ZH-CN_TOPIC_0000001928070488__p145mcpsimp">减少手指操作的复杂度，保证所有的快捷键组合键数控制在 3 个及以下。</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="52.51%"><p id="ZH-CN_TOPIC_0000001928070488__p147mcpsimp">常用功能和命令才分配快捷键，使用频率较低的功能不建议使用快捷键。</p></td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row148mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.49%">&nbsp;&nbsp;</td><td class="cell-norowborder" style="border: none;" valign="top" width="52.51%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row151mcpsimp"><td class="nocellnorowborder" style="border: none;" valign="top" width="47.49%"><p class="start(5)" id="ZH-CN_TOPIC_0000001928070488__p158581547203717"><strong>允许用户一次只输入一个按键</strong></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="52.51%">&nbsp;&nbsp;</td></tr><tr id="ZH-CN_TOPIC_0000001928070488__row155mcpsimp"><td class="row-nocellborder" style="border: none;" valign="top" width="47.49%"><p id="ZH-CN_TOPIC_0000001928070488__p157mcpsimp">保证在使用鼠标光标操作，或面向行动有障碍而无法使用传统物理输入设备的用户，提供可抬手按快捷键组合键的操作。</p></td><td class="cellrowborder" style="border: none;" valign="top" width="52.51%">&nbsp;&nbsp;</td></tr></tbody></table>

### 焦点导航快捷键

展开

| 
功能

 | 

电脑

 | 

Pad

 |
| :-- | :-- | :-- |
| 

**激活走焦状态**

 | 

Tab

 | 

Tab

 |
| 

**焦点移至下一个**

 | 

Tab

 | 

Tab

 |
| 

**焦点移至上一个**

 | 

Shift + Tab

 | 

Shift + Tab

 |
| 

**移动相对焦点位置**

 | 

方向键

 | 

方向键

 |
| 

**移动焦点到区域第一个**

 | 

Home

Fn + ←

 | 

Home

Fn + ←

 |
| 

**移动焦点到区域最后一个**

 | 

End

Fn + →

 | 

End

Fn + →

 |
| 

**激活当前焦点操作**

 | 

Space

 | 

Space

 |
| 

**进入焦点内部**

 | 

Enter

 | 

Enter

 |
| 

**取消操作**

 | 

Esc

 | 

Esc

 |
| 

**打开当前项的上下文菜单**

 | 

Shift + F10

 | 

Shift + F10

 |

## 应用通用快捷键

在所有应用中，对于通用功能，快捷键键值的设计应与系统规范的定义一致，应用根据场景设计快捷键响应的范围。另一方面，在应用内避免对通用快捷键的功能进行重新定义，否则将对用户的使用造成混淆。

### 通用编辑

展开

| 
功能分类

 | 

功能

 | 

电脑

 | 

Pad

 |
| :-- | :-- | :-- | :-- |
| 

**内容编辑**

 | 

**复制选中内容至剪贴板**

 | 

Ctrl + C

 | 

Ctrl + C

 |
| 

**粘贴剪贴板内容至光标处**

 | 

Ctrl + V

 | 

Ctrl + V

 |
| 

**剪切选中内容至剪贴板**

 | 

Ctrl + X

 | 

Ctrl + X

 |
| 

**撤销最后一次操作**

 | 

Ctrl + Z

 | 

Ctrl + Z

 |
| 

**恢复最后一次操作**

 | 

Ctrl + Y，Ctrl + Shift + Z

 | 

Ctrl + Y，Ctrl + Shift + Z

 |
| 

**删除**

 | 

Ctrl + D ，Delete

 | 

Ctrl + D ，Delete

 |
| 

**永久删除**

 | 

Shift + Delete

 | 

Shift + Delete

 |
| 

**保存**

 | 

Ctrl + S

 | 

Ctrl + S

 |
| 

**另存为**

 | 

F12 ，Ctrl + Shift + S

 | 

F12 ，Ctrl + Shift + S

 |
| 

**选择**

 | 

**全选窗口中的所有项目**

 | 

Ctrl + A

 | 

Ctrl + A

 |
| 

**连续加减选**

 | 

Shift + ↑↓←→

Shift + 鼠标左键

 | 

Shift + ↑↓←→

Shift + 鼠标左键

 |
| 

**间序加减选**

 | 

Ctrl + 鼠标左键

 | 

Ctrl + 鼠标左键

 |
| 

**其他**

 | 

**应用内搜索**

 | 

Ctrl + F

 | 

Ctrl + F

 |
| 

**缩放**

 | 

Ctrl + ，Ctrl-，Ctrl 滚轮

 | 

Ctrl + ，Ctrl-，Ctrl 滚轮

 |
| 

**上一页/下一页**

 | 

Page Up/Page Down

 | 

Page Up/Page Down

 |
| 

**播放/暂停**

 | 

Space

 | 

Space

 |
| 

**取消当前任务**

 | 

Esc

 | 

Esc

 |

### 文本编辑

展开

| 
功能

 | 

电脑

 | 

Pad

 |
| :-- | :-- | :-- |
| 

**加粗**

 | 

Ctrl + B

 | 

Ctrl + B

 |
| 

**下划线**

 | 

Ctrl + U

 | 

Ctrl + U

 |
| 

**斜体**

 | 

Ctrl + I

 | 

Ctrl + I

 |
| 

**文本选择-词语**

 | 

Ctrl + Shift + ← →

 | 

Ctrl + Shift + ← →

 |
| 

**文本选择-段落**

 | 

Shift + ↑↓← →

 | 

Shift + ↑↓← →

 |
| 

**删除光标左侧的词组**

 | 

Ctrl + Backspace

 | 

Ctrl + Backspace

 |
| 

**去往行首**

 | 

Home

Fn + ←

 | 

Home

Fn + ←

 |
| 

**去往行末**

 | 

End

Fn + →

 | 

End

Fn + →

 |
| 

**前一词**

 | 

Ctrl + ←

 | 

Ctrl + ←

 |
| 

**后一词**

 | 

Ctrl + →

 | 

Ctrl + →

 |
| 

**去往段首**

 | 

Ctrl + ↑

 | 

Ctrl + ↑

 |
| 

**去往段尾**

 | 

Ctrl + ↓

 | 

Ctrl + ↓

 |
| 

**去往文档之首**

 | 

Ctrl + Home

Ctrl + Fn + ←

 | 

Ctrl + Home

Ctrl + Fn + ←

 |
| 

**去往文档之末**

 | 

Ctrl + End

Ctrl + Fn + →

 | 

Ctrl + End

Ctrl + Fn + →

 |
| 

**前一行**

 | 

↑

 | 

↑

 |
| 

**后一行**

 | 

↓

 | 

↓

 |

## 自定义快捷键

1.在一些场景下，用户可能更习惯于通过键盘来访问系统和应用功能，例如在生产力软件中通过键盘快捷键来提高使用效率，部分残障人士也更偏好使用键盘来进行交互。因此，请确保应用中核心功能支持仅通过键盘操作即可访问。

2\. 对菜单中的功能提供键盘快捷键访问支持：键盘快捷键经常和应用内菜单中的功能关联出现，应允许用户通过键盘快捷键访问这些功能。例如图库应用中照片列表支持通过快捷键进行全选、删除、复制、分享等操作。

3.对应用中其他核心功能提供键盘快捷键访问支持：应用中某些常用的功能没有对应的菜单项，也需要相应的快捷键支持，这类功能往往和控件上的直接操作对应。例如在聊天页面中，应将 Enter 键与发送按钮的点击操作相关联，允许用户在文本框输入消息内容后可以通过按 Enter 键来直接发送内容。
