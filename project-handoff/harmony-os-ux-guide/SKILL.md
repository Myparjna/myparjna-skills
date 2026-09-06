---
name: harmony-os-ux-guide
description: HarmonyOS / 华为UX设计指南全量参考（152篇），覆盖设计原则、组件、布局、交互、多设备适配、动效、响应式等行业案例。适用于 HarmonyOS 应用UX评审、设计走查、组件选型、跨设备适配方案输出。
version: 1.0.0
author: scraped from developer.huawei.com
tags: [harmonyos, ux, design-guide, components, multi-device, responsive]
---

# HarmonyOS UX 设计指南

本 skill 包含华为 HarmonyOS 官方 UX 设计指南的全量抓取内容（152 篇），按主题分为 18 个子目录。适用于：

- HarmonyOS 应用 UX 评审与设计走查
- 组件选型与交互规范查询
- 多设备（手机/平板/折叠屏/PC/智慧屏/穿戴）适配方案
- 响应式布局与行业案例参考
- 动效设计与系统特性集成

## 使用方式

查询特定主题时，直接读取对应 `references/` 子目录中的 `.md` 文件。每个文件包含原始指南的完整内容（含来源链接）。

---

## 目录导航

### 01 - 设计原则 (`references/01-design-principles/`)
设计概念总览、通用设计原则、UX设计原则、动效原则、轻量高效、极简高级感、安全可靠、包容通用。
- `design-overview.md` / `design-concepts.md` / `design-principles-general.md` / `design-principles-ux.md` / `design-principles-animation.md` / `lightweight-efficient.md` / `minimalist-premium.md` / `safety-reliability.md` / `universal-friendly.md`

### 02 - 视觉设计 (`references/02-visual-design/`)
色彩体系、字体排版、间距规范、深色模式、HarmonyOS Symbol图标、视觉风格、留白规范。
- `color.md` / `typography.md` / `spacing.md` / `dark-mode.md` / `harmonyos-symbol.md` / `visual-style.md` / `blank.md`

### 03 - 操作类组件 (`references/03-components-action/`)
按钮、芯片、菜单、分段按钮、选择按钮、切换按钮等操作型组件的使用规范。
- `action-overview.md` / `button.md` / `chips.md` / `menu.md` / `segment-button.md` / `select-button.md` / `toggle-button.md`

### 04 - 输入类组件 (`references/04-components-input/`)
复选框、计数器、输入框、选择器、单选按钮、滑块、文本输入、开关等输入型组件。
- `input-overview.md` / `checkbox.md` / `counter.md` / `picker.md` / `radio.md` / `slider.md` / `text-input.md` / `toggle-switch.md`

### 05 - 展示类组件 (`references/05-components-display/`)
字母索引、徽标、数据面板、分割线、图片、列表、进度条、评分、滚动条、文本等展示型组件。
- `display-overview.md` / `alphabet-indexer.md` / `badge.md` / `data-panel.md` / `divider.md` / `image.md` / `list.md` / `progress.md` / `rating.md` / `scrollbar.md` / `text.md`

### 06 - 导航类组件 (`references/06-components-navigation/`)
底部Tab、导航栏、子Tabs、滑动指示点、标题栏、工具栏等导航型组件。
- `navigation-overview.md` / `bottom-tab.md` / `navigation-bar.md` / `sub-tabs.md` / `swiper-dots.md` / `titlebar.md` / `toolbar.md`

### 07 - 容器类组件 (`references/07-components-container/`)
对话框、半屏弹窗、弹出层等容器型组件。
- `container-overview.md` / `dialog.md` / `half-sheet.md` / `popup.md`

### 08 - 反馈类组件 (`references/08-components-feedback/`)
操作栏、预览、轻量提示、吐司提示等反馈型组件。
- `action-bar.md` / `preview.md` / `snackbar.md` / `toast.md`

### 09 - 布局 (`references/09-layout/`)
应用架构、布局基础、响应式架构、响应式方法、窗口框架等布局规范。
- `layout.md` / `layout-basics.md` / `app-architecture.md` / `responsive-architecture.md` / `responsive-method.md` / `window-framework.md`

### 10 - 交互 (`references/10-interaction/`)
通用交互、光标、拖拽、焦点导航、手势、人机交互概览、交互事件、选择等交互规范。
- `common-interaction.md` / `cursor.md` / `drag.md` / `focus-navigation.md` / `gesture.md` / `hmi-overview.md` / `interaction-events.md` / `selection.md`

### 11 - 多设备 (`references/11-multi-device/`)
手机、平板、折叠屏（含双折/三折/宽折）、PC、智慧屏、穿戴等设备形态的设计要点。
- `phone.md` / `tablet.md` / `foldable.md` / `dual-fold.md` / `tri-fold.md` / `wide-fold.md` / `foldable-pc.md` / `pc.md` / `smart-screen.md` / `wearable.md`

### 12 - UX标准 (`references/12-ux-standards/`)
通用UX标准、折叠屏标准、大屏标准、PC标准、智慧屏标准、穿戴标准、元服务标准。
- `general-ux-standard.md` / `foldable-standard.md` / `large-screen-standard.md` / `pc-standard.md` / `smart-screen-standard.md` / `wearable-standard.md` / `meta-service-standard.md`

### 13 - 元服务 (`references/13-meta-service/`)
元服务概述、元服务要素、元服务场景、服务卡片UX。
- `meta-service-overview.md` / `meta-service-elements.md` / `meta-service-scenarios.md` / `service-widget-ux.md`

### 14 - 系统特性 (`references/14-system-features/`)
启动页、实况窗、多窗口、通知、画中画、服务卡片、状态栏、系统能力等系统级特性。
- `system-features.md` / `launch-page.md` / `live-view.md` / `multi-window.md` / `notification.md` / `pip.md` / `service-widget-system.md` / `statusbar.md` / `system-capabilities.md`

### 15 - 输入设备 (`references/15-input-devices/`)
触控手势动画、键盘、鼠标、文本选择、触控板等输入设备交互规范。
- `gesture-animation.md` / `keyboard.md` / `mouse.md` / `text-selection.md` / `touchpad.md`

### 16 - 动效 (`references/16-animation/`)
动效概述、动效属性、动效引力、转场动画等动效设计规范。
- `animation-overview.md` / `animation-attributes.md` / `animation-gravity.md` / `transition-animation.md`

### 17 - 响应式行业案例 (`references/17-responsive-examples/`)
汽车、相机、日常生活、电商、娱乐、金融、游戏、新闻、办公、社交、文旅、出行等行业的响应式设计案例。
- `responsive-overview.md` / `automotive.md` / `camera.md` / `daily-life.md` / `ecommerce.md` / `entertainment.md` / `finance.md` / `game.md` / `news.md` / `office.md` / `social.md` / `tourism.md` / `travel.md`

### 18 - 补充内容 (`references/18-supplementary/`)
账号、应用设计、应用图标、最佳实践、广播控制、更新日志、组件概览、全球化、华为账号、华为支付、近场发现、NFC碰一碰、图案锁、隐私、二维码、智慧握持、文字时钟、UI语言、UX标准概览、穿戴概览等。
- `account.md` / `app-design.md` / `app-icon.md` / `best-practices.md` / `broadcasting-control.md` / `changelog.md` / `component-overview.md` / `globalization.md` / `hmi-overview.md` / `huawei-account.md` / `huawei-pay.md` / `nearby-discovery.md` / `nfc-hop.md` / `pattern-lock.md` / `privacy.md` / `qrcode.md` / `smart-grip.md` / `text-clock.md` / `ui-language.md` / `ux-standard-overview.md` / `wearable-overview.md`

---

## 快速查询示例

| 场景 | 推荐查阅 |
|------|----------|
| 新建 HarmonyOS 应用，不确定用什么布局 | `09-layout/app-architecture.md`, `09-layout/responsive-architecture.md` |
| 设计一个折叠屏适配方案 | `11-multi-device/foldable.md`, `12-ux-standards/foldable-standard.md` |
| 选择合适的按钮类型 | `03-components-action/button.md` |
| 了解深色模式适配 | `02-visual-design/dark-mode.md` |
| 查询动效转场规范 | `16-animation/transition-animation.md` |
| 了解元服务设计 | `13-meta-service/meta-service-overview.md`, `13-meta-service/service-widget-ux.md` |
| 参考电商行业响应式案例 | `17-responsive-examples/ecommerce.md` |

## 数据来源

所有内容抓取自 `developer.huawei.com/consumer/cn/doc/design-guides/`，抓取时间 2026-04-04。每个文件头部包含原始来源 URL。
