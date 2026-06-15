# 交互事件归一

- 来源：https://developer.huawei.com/consumer/cn/doc/design-guides/hmi-interaction-events-0000001795531217
- 抓取时间：2026-04-04T08:23:50.620Z
为了让应用在全场景多设备上都能获得一致自然的交互体验，需要为不同交互状态下的各种输入设备设计适合的交互方式。在传统的开发模式中需要为不同的输入设备进行适配开发，工作量巨大。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170808.17699526271382135962129281892319:50001231000000:2800:AFFE96E2F5D6CC250504CFF4DD5490C671A32A8A307949A98FDED959F984736F.png "点击放大")

针对这一问题，HarmonyOS 提出了交互事件归一，旨在保证全场景下应用交互体验一致性的同时，大幅降低设计和开发的工作量。交互事件归一是一种适配多设备输入的交互响应框架，通过将不同设备的交互行为转化为同一个交互事件，保证控件在不同交互场景下的体验一致性。开发者只需要调用所需的交互事件接口，无需为每个输入设备单独适配，从而大幅简化开发流程。

以缩放操作为例，当应用仅在触屏设备上使用时，可通过双指捏合手势对显示内容进行缩放。而当应用同时需要在电脑上使用时，则需要为键盘、鼠标和触控板设计相应的缩放操作方式。在以往的开发模式下，需要为每个输入设备单独适配，工作量大。使用交互事件归一框架，可以将不同设备的交互操作映射为统一的缩放事件，归一响应缩放相关交互事件。开发者仅需调用控件的缩放事件接口，即可实现交互事件归一中定义好的交互行为。

<table id="ZH-CN_TOPIC_0000001795531217__table5666154016304" style="border-style: none;" class="no-border layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795531217__row1766718404307"><td class="nocellnorowborder" style="border: none;" valign="top" width="25%"><p id="ZH-CN_TOPIC_0000001795531217__p17803140103612"></p><div class="video-box" style="width: 109.25px; height: 109.25px;"><div videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.60887717251667061379870203699884:20260405162346:2800:4698AB14FF6D0D08880EC6C1388891443264510BF2868BDF45088E9D838045BB.mp4" videoid="object17993182017315" preload="none" id="wise_player_0" class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-workinghover vjs-v7 vjs-user-active wise_player_0-dimensions vjs-v8 vjs-error vjs-controls-disabled" tabindex="-1" lang="cn" translate="no" role="region" aria-label="Video Player"><video class="vjs-tech" id="wise_player_0_html5_api" preload="none" videoid="object17993182017315" videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.60887717251667061379870203699884:20260405162346:2800:4698AB14FF6D0D08880EC6C1388891443264510BF2868BDF45088E9D838045BB.mp4" tabindex="-1" loop="" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.60887717251667061379870203699884:20260405162346:2800:4698AB14FF6D0D08880EC6C1388891443264510BF2868BDF45088E9D838045BB.mp4"></video><div class="vjs-poster vjs-hidden" aria-disabled="false"></div><div class="vjs-title-bar vjs-hidden"><div class="vjs-title-bar-title" id="vjs-title-bar-title-776"></div><div class="vjs-title-bar-description" id="vjs-title-bar-description-777"></div></div><div class="vjs-text-track-display" translate="yes" aria-live="off" aria-atomic="true"><div style="position: absolute; inset: 0px; margin: 1.5%;"></div></div><div class="vjs-loading-spinner" dir="ltr"><span class="vjs-control-text">Video Player is loading.</span></div><div class="vjs-control-bar" dir="ltr"><div class="vjs-current-time vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Current Time&nbsp;</span><span class="vjs-current-time-display" role="presentation">0:00</span></div><div class="vjs-progress-control vjs-control"><div tabindex="0" class="vjs-progress-holder vjs-slider vjs-slider-horizontal" role="slider" aria-valuenow="0.00" aria-valuemin="0" aria-valuemax="100" aria-label="Progress Bar" aria-valuetext="0:00 of -:-"><div class="vjs-load-progress"><span class="vjs-control-text"><span>Loaded</span>: <span class="vjs-control-text-loaded-percentage">0%</span></span></div><div class="vjs-mouse-display"><div class="vjs-time-tooltip" aria-hidden="true"></div></div><div class="vjs-play-progress vjs-slider-bar" aria-hidden="true" style="width: 0%;"><div class="vjs-time-tooltip" aria-hidden="true" style="right: 0px;">0:00</div></div></div></div><div class="vjs-duration vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Duration&nbsp;</span><span class="vjs-duration-display" role="presentation">-:-</span></div><div class="vjs-volume-panel vjs-control vjs-volume-panel-vertical"><div class="vjs-volume-control vjs-control vjs-volume-vertical"><div tabindex="0" class="vjs-volume-bar vjs-slider-bar vjs-slider vjs-slider-vertical" role="slider" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Volume Level" aria-live="polite" aria-valuetext="100%"><div class="vjs-mouse-display"><div class="vjs-volume-tooltip" aria-hidden="true"></div></div><div class="vjs-volume-level"><span class="vjs-control-text"></span></div></div></div></div><div class="vjs-playback-rate vjs-menu-button vjs-menu-button-popup vjs-control vjs-button"><div class="vjs-playback-rate-value" id="vjs-playback-rate-value-label-wise_player_0_component_961">1x</div><div class="vjs-menu"><ul class="vjs-menu-content" role="menu"><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.8x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.5x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item vjs-selected" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="true"><span class="vjs-menu-item-text">1x</span><span class="vjs-control-text" aria-live="polite">, selected</span></li></ul></div></div></div><div class="vjs-error-display vjs-modal-dialog" tabindex="-1" aria-describedby="wise_player_0_component_1068_description" aria-hidden="false" aria-label="Modal Window" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_0_component_1068_description">This is a modal window.</p><div class="vjs-modal-dialog-content" role="document">The media could not be loaded, either because the server or network failed or because the format is not supported.</div></div><div class="vjs-modal-dialog vjs-hidden  vjs-text-track-settings" tabindex="-1" aria-describedby="wise_player_0_component_1074_description" aria-hidden="true" aria-label="Caption Settings Dialog" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_0_component_1074_description">Beginning of dialog window. Escape will cancel and close the window.</p><div class="vjs-modal-dialog-content" role="document"><div class="vjs-track-settings-colors"><fieldset class="vjs-fg vjs-track-setting"><legend id="captions-text-legend-wise_player_0_component_1074">Text</legend><span class="vjs-text-color"><label id="captions-foreground-color-wise_player_0_component_1074" for="vjs_select_1100" class="vjs-label">Color</label><select aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074" id="vjs_select_1100"><option id="captions-foreground-color-wise_player_0_component_1074-White" value="#FFF" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-White">White</option><option id="captions-foreground-color-wise_player_0_component_1074-Black" value="#000" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-Black">Black</option><option id="captions-foreground-color-wise_player_0_component_1074-Red" value="#F00" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-Red">Red</option><option id="captions-foreground-color-wise_player_0_component_1074-Green" value="#0F0" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-Green">Green</option><option id="captions-foreground-color-wise_player_0_component_1074-Blue" value="#00F" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-Blue">Blue</option><option id="captions-foreground-color-wise_player_0_component_1074-Yellow" value="#FF0" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-Yellow">Yellow</option><option id="captions-foreground-color-wise_player_0_component_1074-Magenta" value="#F0F" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-Magenta">Magenta</option><option id="captions-foreground-color-wise_player_0_component_1074-Cyan" value="#0FF" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074 captions-foreground-color-wise_player_0_component_1074-Cyan">Cyan</option></select></span><span class="vjs-text-opacity vjs-opacity"><label id="captions-foreground-opacity-wise_player_0_component_1074" for="vjs_select_1101" class="vjs-label">Opacity</label><select aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-opacity-wise_player_0_component_1074" id="vjs_select_1101"><option id="captions-foreground-opacity-wise_player_0_component_1074-Opaque" value="1" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-opacity-wise_player_0_component_1074 captions-foreground-opacity-wise_player_0_component_1074-Opaque">Opaque</option><option id="captions-foreground-opacity-wise_player_0_component_1074-SemiTransparent" value="0.5" aria-labelledby="captions-text-legend-wise_player_0_component_1074 captions-foreground-opacity-wise_player_0_component_1074 captions-foreground-opacity-wise_player_0_component_1074-SemiTransparent">Semi-Transparent</option></select></span></fieldset><fieldset class="vjs-bg vjs-track-setting"><legend id="captions-background-wise_player_0_component_1074">Text Background</legend><span class="vjs-bg-color"><label id="captions-background-color-wise_player_0_component_1074" for="vjs_select_1102" class="vjs-label">Color</label><select aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074" id="vjs_select_1102"><option id="captions-background-color-wise_player_0_component_1074-Black" value="#000" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-Black">Black</option><option id="captions-background-color-wise_player_0_component_1074-White" value="#FFF" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-White">White</option><option id="captions-background-color-wise_player_0_component_1074-Red" value="#F00" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-Red">Red</option><option id="captions-background-color-wise_player_0_component_1074-Green" value="#0F0" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-Green">Green</option><option id="captions-background-color-wise_player_0_component_1074-Blue" value="#00F" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-Blue">Blue</option><option id="captions-background-color-wise_player_0_component_1074-Yellow" value="#FF0" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-Yellow">Yellow</option><option id="captions-background-color-wise_player_0_component_1074-Magenta" value="#F0F" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-Magenta">Magenta</option><option id="captions-background-color-wise_player_0_component_1074-Cyan" value="#0FF" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074 captions-background-color-wise_player_0_component_1074-Cyan">Cyan</option></select></span><span class="vjs-bg-opacity vjs-opacity"><label id="captions-background-opacity-wise_player_0_component_1074" for="vjs_select_1103" class="vjs-label">Opacity</label><select aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-opacity-wise_player_0_component_1074" id="vjs_select_1103"><option id="captions-background-opacity-wise_player_0_component_1074-Opaque" value="1" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-opacity-wise_player_0_component_1074 captions-background-opacity-wise_player_0_component_1074-Opaque">Opaque</option><option id="captions-background-opacity-wise_player_0_component_1074-SemiTransparent" value="0.5" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-opacity-wise_player_0_component_1074 captions-background-opacity-wise_player_0_component_1074-SemiTransparent">Semi-Transparent</option><option id="captions-background-opacity-wise_player_0_component_1074-Transparent" value="0" aria-labelledby="captions-background-wise_player_0_component_1074 captions-background-opacity-wise_player_0_component_1074 captions-background-opacity-wise_player_0_component_1074-Transparent">Transparent</option></select></span></fieldset><fieldset class="vjs-window vjs-track-setting"><legend id="captions-window-wise_player_0_component_1074">Caption Area Background</legend><span class="vjs-window-color"><label id="captions-window-color-wise_player_0_component_1074" for="vjs_select_1104" class="vjs-label">Color</label><select aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074" id="vjs_select_1104"><option id="captions-window-color-wise_player_0_component_1074-Black" value="#000" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-Black">Black</option><option id="captions-window-color-wise_player_0_component_1074-White" value="#FFF" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-White">White</option><option id="captions-window-color-wise_player_0_component_1074-Red" value="#F00" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-Red">Red</option><option id="captions-window-color-wise_player_0_component_1074-Green" value="#0F0" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-Green">Green</option><option id="captions-window-color-wise_player_0_component_1074-Blue" value="#00F" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-Blue">Blue</option><option id="captions-window-color-wise_player_0_component_1074-Yellow" value="#FF0" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-Yellow">Yellow</option><option id="captions-window-color-wise_player_0_component_1074-Magenta" value="#F0F" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-Magenta">Magenta</option><option id="captions-window-color-wise_player_0_component_1074-Cyan" value="#0FF" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074 captions-window-color-wise_player_0_component_1074-Cyan">Cyan</option></select></span><span class="vjs-window-opacity vjs-opacity"><label id="captions-window-opacity-wise_player_0_component_1074" for="vjs_select_1105" class="vjs-label">Opacity</label><select aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-opacity-wise_player_0_component_1074" id="vjs_select_1105"><option id="captions-window-opacity-wise_player_0_component_1074-Transparent" value="0" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-opacity-wise_player_0_component_1074 captions-window-opacity-wise_player_0_component_1074-Transparent">Transparent</option><option id="captions-window-opacity-wise_player_0_component_1074-SemiTransparent" value="0.5" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-opacity-wise_player_0_component_1074 captions-window-opacity-wise_player_0_component_1074-SemiTransparent">Semi-Transparent</option><option id="captions-window-opacity-wise_player_0_component_1074-Opaque" value="1" aria-labelledby="captions-window-wise_player_0_component_1074 captions-window-opacity-wise_player_0_component_1074 captions-window-opacity-wise_player_0_component_1074-Opaque">Opaque</option></select></span></fieldset></div><div class="vjs-track-settings-font"><fieldset class="vjs-font-percent vjs-track-setting"><legend id="captions-font-size-wise_player_0_component_1074">Font Size</legend><select aria-labelledby="captions-font-size-wise_player_0_component_1074" id="vjs_select_1106"><option id="captions-font-size-wise_player_0_component_1074-50" value="0.50" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-50">50%</option><option id="captions-font-size-wise_player_0_component_1074-75" value="0.75" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-75">75%</option><option id="captions-font-size-wise_player_0_component_1074-100" value="1.00" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-100">100%</option><option id="captions-font-size-wise_player_0_component_1074-125" value="1.25" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-125">125%</option><option id="captions-font-size-wise_player_0_component_1074-150" value="1.50" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-150">150%</option><option id="captions-font-size-wise_player_0_component_1074-175" value="1.75" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-175">175%</option><option id="captions-font-size-wise_player_0_component_1074-200" value="2.00" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-200">200%</option><option id="captions-font-size-wise_player_0_component_1074-300" value="3.00" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-300">300%</option><option id="captions-font-size-wise_player_0_component_1074-400" value="4.00" aria-labelledby="captions-font-size-wise_player_0_component_1074 captions-font-size-wise_player_0_component_1074-400">400%</option></select></fieldset><fieldset class="vjs-edge-style vjs-track-setting"><legend id="wise_player_0_component_1074">Text Edge Style</legend><select aria-labelledby="wise_player_0_component_1074" id="vjs_select_1107"><option id="wise_player_0_component_1074-None" value="none" aria-labelledby="wise_player_0_component_1074 wise_player_0_component_1074-None">None</option><option id="wise_player_0_component_1074-Raised" value="raised" aria-labelledby="wise_player_0_component_1074 wise_player_0_component_1074-Raised">Raised</option><option id="wise_player_0_component_1074-Depressed" value="depressed" aria-labelledby="wise_player_0_component_1074 wise_player_0_component_1074-Depressed">Depressed</option><option id="wise_player_0_component_1074-Uniform" value="uniform" aria-labelledby="wise_player_0_component_1074 wise_player_0_component_1074-Uniform">Uniform</option><option id="wise_player_0_component_1074-Dropshadow" value="dropshadow" aria-labelledby="wise_player_0_component_1074 wise_player_0_component_1074-Dropshadow">Drop shadow</option></select></fieldset><fieldset class="vjs-font-family vjs-track-setting"><legend id="captions-font-family-wise_player_0_component_1074">Font Family</legend><select aria-labelledby="captions-font-family-wise_player_0_component_1074" id="vjs_select_1108"><option id="captions-font-family-wise_player_0_component_1074-ProportionalSansSerif" value="proportionalSansSerif" aria-labelledby="captions-font-family-wise_player_0_component_1074 captions-font-family-wise_player_0_component_1074-ProportionalSansSerif">Proportional Sans-Serif</option><option id="captions-font-family-wise_player_0_component_1074-MonospaceSansSerif" value="monospaceSansSerif" aria-labelledby="captions-font-family-wise_player_0_component_1074 captions-font-family-wise_player_0_component_1074-MonospaceSansSerif">Monospace Sans-Serif</option><option id="captions-font-family-wise_player_0_component_1074-ProportionalSerif" value="proportionalSerif" aria-labelledby="captions-font-family-wise_player_0_component_1074 captions-font-family-wise_player_0_component_1074-ProportionalSerif">Proportional Serif</option><option id="captions-font-family-wise_player_0_component_1074-MonospaceSerif" value="monospaceSerif" aria-labelledby="captions-font-family-wise_player_0_component_1074 captions-font-family-wise_player_0_component_1074-MonospaceSerif">Monospace Serif</option><option id="captions-font-family-wise_player_0_component_1074-Casual" value="casual" aria-labelledby="captions-font-family-wise_player_0_component_1074 captions-font-family-wise_player_0_component_1074-Casual">Casual</option><option id="captions-font-family-wise_player_0_component_1074-Script" value="script" aria-labelledby="captions-font-family-wise_player_0_component_1074 captions-font-family-wise_player_0_component_1074-Script">Script</option><option id="captions-font-family-wise_player_0_component_1074-SmallCaps" value="small-caps" aria-labelledby="captions-font-family-wise_player_0_component_1074 captions-font-family-wise_player_0_component_1074-SmallCaps">Small Caps</option></select></fieldset></div><div class="vjs-track-settings-controls"></div></div><p class="vjs-control-text">End of dialog window.</p></div><div videoid="object17993182017315" wiseplayerindex="0" playertype="wise" class="wiseplayershaw"><div class="play-number"><span>39</span><i><svg width="15px" height="11px" viewBox="0 0 15 11" version="1.1"><g id="文档详情页" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="2.3.1Documentation-Desktop-1920" transform="translate(-1334.000000, -2831.000000)"><g id="Group-7" transform="translate(520.000000, 2569.000000)"><g id="ic_view" transform="translate(814.000000, 259.000000)"><rect id="矩形" opacity="0.2" x="0" y="0" width="16" height="16"></rect><path d="M7.83333333,3.33333333 C4.74205364,3.33635162 1.94529498,5.16771838 0.706666667,8 C0.653333333,8.128 0.653333333,8.272 0.706666667,8.4 C1.94529498,11.2322816 4.74205364,13.0636484 7.83333333,13.066713 C10.2799392,13.0751325 12.5854758,11.9223642 14.0466667,9.96 C14.1538464,9.81709376 14.1766449,9.62786327 14.1064743,9.46358983 C14.0363037,9.29931638 13.8838246,9.18495702 13.7064743,9.16358982 C13.529124,9.14222262 13.3538463,9.21709375 13.2466667,9.36 C11.9736331,11.0697245 9.96493305,12.0740745 7.83333333,12.0666667 C5.21930483,12.0625944 2.83949297,10.5590096 1.71333333,8.2 C2.8525202,5.80258442 5.28704761,4.29150533 7.94100578,4.33456577 C10.594964,4.3776262 12.9791884,5.96688947 14.04,8.4 C14.1114531,8.56434218 14.265154,8.67808083 14.4432051,8.69837171 C14.6212561,8.71866258 14.7966072,8.64242301 14.9032051,8.4983717 C15.009803,8.35432039 15.0314531,8.16434217 14.96,8 C13.7213717,5.16771838 10.924613,3.33635162 7.83333333,3.33333333 Z" id="路径" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path><path d="M7.83333333,5.53333195 C6.61080734,5.53209462 5.544019,6.36231359 5.24497492,7.54770128 C4.94593084,8.73308896 5.49123358,9.96999875 6.56804799,10.5488269 C7.64486241,11.1276551 8.97735379,10.9001301 9.80108415,9.99678101 C10.6248145,9.0934319 10.7287787,7.74565879 10.0533333,6.72666667 C9.94736797,6.56325905 9.82201175,6.4132793 9.68,6.28 C9.18399727,5.80192485 8.52222631,5.53434958 7.83333333,5.53333195 Z M7.83333333,9.86666994 C7.08238462,9.86814757 6.42318765,9.36724437 6.22342868,8.64335038 C6.02366972,7.91945638 6.3326892,7.15137329 6.97812252,6.76752177 C7.62355584,6.38367026 8.44598108,6.47886157 8.98666667,7 C9.07498525,7.08401981 9.15328386,7.17797814 9.22,7.28 C9.40392075,7.55143891 9.50152012,7.87212256 9.50001749,8.2 C9.50001749,9.12047458 8.75380792,9.86666994 7.83333333,9.86666994 L7.83333333,9.86666994 Z" id="形状" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path></g></g></g></g></svg></i></div></div></div></div><p></p><p id="ZH-CN_TOPIC_0000001795531217__p10667144011304"><strong>触屏手指输入</strong></p><p id="ZH-CN_TOPIC_0000001795531217__p101971001321">触屏双指捏合</p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="24.97%"><p id="ZH-CN_TOPIC_0000001795531217__p11934743163617"></p><div class="video-box" style="width: 109.059px; height: 109.059px;"><div videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.40869119805811691235003558324360:20260405162346:2800:885195F6D4CA857A1CB6E541907EC3D538092AF941C4F5BEFDBD3433481070E4.mp4" videoid="object6767184763310" preload="none" id="wise_player_1" class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-workinghover vjs-v7 vjs-user-active wise_player_1-dimensions vjs-v8 vjs-error vjs-controls-disabled" tabindex="-1" lang="cn" translate="no" role="region" aria-label="Video Player"><video class="vjs-tech" id="wise_player_1_html5_api" preload="none" videoid="object6767184763310" videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.40869119805811691235003558324360:20260405162346:2800:885195F6D4CA857A1CB6E541907EC3D538092AF941C4F5BEFDBD3433481070E4.mp4" tabindex="-1" loop="" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.40869119805811691235003558324360:20260405162346:2800:885195F6D4CA857A1CB6E541907EC3D538092AF941C4F5BEFDBD3433481070E4.mp4"></video><div class="vjs-poster vjs-hidden" aria-disabled="false"></div><div class="vjs-title-bar vjs-hidden"><div class="vjs-title-bar-title" id="vjs-title-bar-title-1144"></div><div class="vjs-title-bar-description" id="vjs-title-bar-description-1145"></div></div><div class="vjs-text-track-display" translate="yes" aria-live="off" aria-atomic="true"><div style="position: absolute; inset: 0px; margin: 1.5%;"></div></div><div class="vjs-loading-spinner" dir="ltr"><span class="vjs-control-text">Video Player is loading.</span></div><div class="vjs-control-bar" dir="ltr"><div class="vjs-current-time vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Current Time&nbsp;</span><span class="vjs-current-time-display" role="presentation">0:00</span></div><div class="vjs-progress-control vjs-control"><div tabindex="0" class="vjs-progress-holder vjs-slider vjs-slider-horizontal" role="slider" aria-valuenow="0.00" aria-valuemin="0" aria-valuemax="100" aria-label="Progress Bar" aria-valuetext="0:00 of -:-"><div class="vjs-load-progress"><span class="vjs-control-text"><span>Loaded</span>: <span class="vjs-control-text-loaded-percentage">0%</span></span></div><div class="vjs-mouse-display"><div class="vjs-time-tooltip" aria-hidden="true"></div></div><div class="vjs-play-progress vjs-slider-bar" aria-hidden="true" style="width: 0%;"><div class="vjs-time-tooltip" aria-hidden="true" style="right: 0px;">0:00</div></div></div></div><div class="vjs-duration vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Duration&nbsp;</span><span class="vjs-duration-display" role="presentation">-:-</span></div><div class="vjs-volume-panel vjs-control vjs-volume-panel-vertical"><div class="vjs-volume-control vjs-control vjs-volume-vertical"><div tabindex="0" class="vjs-volume-bar vjs-slider-bar vjs-slider vjs-slider-vertical" role="slider" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Volume Level" aria-live="polite" aria-valuetext="100%"><div class="vjs-mouse-display"><div class="vjs-volume-tooltip" aria-hidden="true"></div></div><div class="vjs-volume-level"><span class="vjs-control-text"></span></div></div></div></div><div class="vjs-playback-rate vjs-menu-button vjs-menu-button-popup vjs-control vjs-button"><div class="vjs-playback-rate-value" id="vjs-playback-rate-value-label-wise_player_1_component_1329">1x</div><div class="vjs-menu"><ul class="vjs-menu-content" role="menu"><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.8x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.5x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item vjs-selected" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="true"><span class="vjs-menu-item-text">1x</span><span class="vjs-control-text" aria-live="polite">, selected</span></li></ul></div></div></div><div class="vjs-error-display vjs-modal-dialog" tabindex="-1" aria-describedby="wise_player_1_component_1436_description" aria-hidden="false" aria-label="Modal Window" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_1_component_1436_description">This is a modal window.</p><div class="vjs-modal-dialog-content" role="document">The media could not be loaded, either because the server or network failed or because the format is not supported.</div></div><div class="vjs-modal-dialog vjs-hidden  vjs-text-track-settings" tabindex="-1" aria-describedby="wise_player_1_component_1442_description" aria-hidden="true" aria-label="Caption Settings Dialog" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_1_component_1442_description">Beginning of dialog window. Escape will cancel and close the window.</p><div class="vjs-modal-dialog-content" role="document"><div class="vjs-track-settings-colors"><fieldset class="vjs-fg vjs-track-setting"><legend id="captions-text-legend-wise_player_1_component_1442">Text</legend><span class="vjs-text-color"><label id="captions-foreground-color-wise_player_1_component_1442" for="vjs_select_1468" class="vjs-label">Color</label><select aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442" id="vjs_select_1468"><option id="captions-foreground-color-wise_player_1_component_1442-White" value="#FFF" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-White">White</option><option id="captions-foreground-color-wise_player_1_component_1442-Black" value="#000" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-Black">Black</option><option id="captions-foreground-color-wise_player_1_component_1442-Red" value="#F00" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-Red">Red</option><option id="captions-foreground-color-wise_player_1_component_1442-Green" value="#0F0" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-Green">Green</option><option id="captions-foreground-color-wise_player_1_component_1442-Blue" value="#00F" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-Blue">Blue</option><option id="captions-foreground-color-wise_player_1_component_1442-Yellow" value="#FF0" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-Yellow">Yellow</option><option id="captions-foreground-color-wise_player_1_component_1442-Magenta" value="#F0F" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-Magenta">Magenta</option><option id="captions-foreground-color-wise_player_1_component_1442-Cyan" value="#0FF" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442 captions-foreground-color-wise_player_1_component_1442-Cyan">Cyan</option></select></span><span class="vjs-text-opacity vjs-opacity"><label id="captions-foreground-opacity-wise_player_1_component_1442" for="vjs_select_1469" class="vjs-label">Opacity</label><select aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-opacity-wise_player_1_component_1442" id="vjs_select_1469"><option id="captions-foreground-opacity-wise_player_1_component_1442-Opaque" value="1" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-opacity-wise_player_1_component_1442 captions-foreground-opacity-wise_player_1_component_1442-Opaque">Opaque</option><option id="captions-foreground-opacity-wise_player_1_component_1442-SemiTransparent" value="0.5" aria-labelledby="captions-text-legend-wise_player_1_component_1442 captions-foreground-opacity-wise_player_1_component_1442 captions-foreground-opacity-wise_player_1_component_1442-SemiTransparent">Semi-Transparent</option></select></span></fieldset><fieldset class="vjs-bg vjs-track-setting"><legend id="captions-background-wise_player_1_component_1442">Text Background</legend><span class="vjs-bg-color"><label id="captions-background-color-wise_player_1_component_1442" for="vjs_select_1470" class="vjs-label">Color</label><select aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442" id="vjs_select_1470"><option id="captions-background-color-wise_player_1_component_1442-Black" value="#000" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-Black">Black</option><option id="captions-background-color-wise_player_1_component_1442-White" value="#FFF" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-White">White</option><option id="captions-background-color-wise_player_1_component_1442-Red" value="#F00" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-Red">Red</option><option id="captions-background-color-wise_player_1_component_1442-Green" value="#0F0" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-Green">Green</option><option id="captions-background-color-wise_player_1_component_1442-Blue" value="#00F" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-Blue">Blue</option><option id="captions-background-color-wise_player_1_component_1442-Yellow" value="#FF0" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-Yellow">Yellow</option><option id="captions-background-color-wise_player_1_component_1442-Magenta" value="#F0F" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-Magenta">Magenta</option><option id="captions-background-color-wise_player_1_component_1442-Cyan" value="#0FF" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442 captions-background-color-wise_player_1_component_1442-Cyan">Cyan</option></select></span><span class="vjs-bg-opacity vjs-opacity"><label id="captions-background-opacity-wise_player_1_component_1442" for="vjs_select_1471" class="vjs-label">Opacity</label><select aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-opacity-wise_player_1_component_1442" id="vjs_select_1471"><option id="captions-background-opacity-wise_player_1_component_1442-Opaque" value="1" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-opacity-wise_player_1_component_1442 captions-background-opacity-wise_player_1_component_1442-Opaque">Opaque</option><option id="captions-background-opacity-wise_player_1_component_1442-SemiTransparent" value="0.5" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-opacity-wise_player_1_component_1442 captions-background-opacity-wise_player_1_component_1442-SemiTransparent">Semi-Transparent</option><option id="captions-background-opacity-wise_player_1_component_1442-Transparent" value="0" aria-labelledby="captions-background-wise_player_1_component_1442 captions-background-opacity-wise_player_1_component_1442 captions-background-opacity-wise_player_1_component_1442-Transparent">Transparent</option></select></span></fieldset><fieldset class="vjs-window vjs-track-setting"><legend id="captions-window-wise_player_1_component_1442">Caption Area Background</legend><span class="vjs-window-color"><label id="captions-window-color-wise_player_1_component_1442" for="vjs_select_1472" class="vjs-label">Color</label><select aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442" id="vjs_select_1472"><option id="captions-window-color-wise_player_1_component_1442-Black" value="#000" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-Black">Black</option><option id="captions-window-color-wise_player_1_component_1442-White" value="#FFF" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-White">White</option><option id="captions-window-color-wise_player_1_component_1442-Red" value="#F00" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-Red">Red</option><option id="captions-window-color-wise_player_1_component_1442-Green" value="#0F0" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-Green">Green</option><option id="captions-window-color-wise_player_1_component_1442-Blue" value="#00F" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-Blue">Blue</option><option id="captions-window-color-wise_player_1_component_1442-Yellow" value="#FF0" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-Yellow">Yellow</option><option id="captions-window-color-wise_player_1_component_1442-Magenta" value="#F0F" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-Magenta">Magenta</option><option id="captions-window-color-wise_player_1_component_1442-Cyan" value="#0FF" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442 captions-window-color-wise_player_1_component_1442-Cyan">Cyan</option></select></span><span class="vjs-window-opacity vjs-opacity"><label id="captions-window-opacity-wise_player_1_component_1442" for="vjs_select_1473" class="vjs-label">Opacity</label><select aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-opacity-wise_player_1_component_1442" id="vjs_select_1473"><option id="captions-window-opacity-wise_player_1_component_1442-Transparent" value="0" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-opacity-wise_player_1_component_1442 captions-window-opacity-wise_player_1_component_1442-Transparent">Transparent</option><option id="captions-window-opacity-wise_player_1_component_1442-SemiTransparent" value="0.5" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-opacity-wise_player_1_component_1442 captions-window-opacity-wise_player_1_component_1442-SemiTransparent">Semi-Transparent</option><option id="captions-window-opacity-wise_player_1_component_1442-Opaque" value="1" aria-labelledby="captions-window-wise_player_1_component_1442 captions-window-opacity-wise_player_1_component_1442 captions-window-opacity-wise_player_1_component_1442-Opaque">Opaque</option></select></span></fieldset></div><div class="vjs-track-settings-font"><fieldset class="vjs-font-percent vjs-track-setting"><legend id="captions-font-size-wise_player_1_component_1442">Font Size</legend><select aria-labelledby="captions-font-size-wise_player_1_component_1442" id="vjs_select_1474"><option id="captions-font-size-wise_player_1_component_1442-50" value="0.50" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-50">50%</option><option id="captions-font-size-wise_player_1_component_1442-75" value="0.75" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-75">75%</option><option id="captions-font-size-wise_player_1_component_1442-100" value="1.00" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-100">100%</option><option id="captions-font-size-wise_player_1_component_1442-125" value="1.25" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-125">125%</option><option id="captions-font-size-wise_player_1_component_1442-150" value="1.50" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-150">150%</option><option id="captions-font-size-wise_player_1_component_1442-175" value="1.75" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-175">175%</option><option id="captions-font-size-wise_player_1_component_1442-200" value="2.00" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-200">200%</option><option id="captions-font-size-wise_player_1_component_1442-300" value="3.00" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-300">300%</option><option id="captions-font-size-wise_player_1_component_1442-400" value="4.00" aria-labelledby="captions-font-size-wise_player_1_component_1442 captions-font-size-wise_player_1_component_1442-400">400%</option></select></fieldset><fieldset class="vjs-edge-style vjs-track-setting"><legend id="wise_player_1_component_1442">Text Edge Style</legend><select aria-labelledby="wise_player_1_component_1442" id="vjs_select_1475"><option id="wise_player_1_component_1442-None" value="none" aria-labelledby="wise_player_1_component_1442 wise_player_1_component_1442-None">None</option><option id="wise_player_1_component_1442-Raised" value="raised" aria-labelledby="wise_player_1_component_1442 wise_player_1_component_1442-Raised">Raised</option><option id="wise_player_1_component_1442-Depressed" value="depressed" aria-labelledby="wise_player_1_component_1442 wise_player_1_component_1442-Depressed">Depressed</option><option id="wise_player_1_component_1442-Uniform" value="uniform" aria-labelledby="wise_player_1_component_1442 wise_player_1_component_1442-Uniform">Uniform</option><option id="wise_player_1_component_1442-Dropshadow" value="dropshadow" aria-labelledby="wise_player_1_component_1442 wise_player_1_component_1442-Dropshadow">Drop shadow</option></select></fieldset><fieldset class="vjs-font-family vjs-track-setting"><legend id="captions-font-family-wise_player_1_component_1442">Font Family</legend><select aria-labelledby="captions-font-family-wise_player_1_component_1442" id="vjs_select_1476"><option id="captions-font-family-wise_player_1_component_1442-ProportionalSansSerif" value="proportionalSansSerif" aria-labelledby="captions-font-family-wise_player_1_component_1442 captions-font-family-wise_player_1_component_1442-ProportionalSansSerif">Proportional Sans-Serif</option><option id="captions-font-family-wise_player_1_component_1442-MonospaceSansSerif" value="monospaceSansSerif" aria-labelledby="captions-font-family-wise_player_1_component_1442 captions-font-family-wise_player_1_component_1442-MonospaceSansSerif">Monospace Sans-Serif</option><option id="captions-font-family-wise_player_1_component_1442-ProportionalSerif" value="proportionalSerif" aria-labelledby="captions-font-family-wise_player_1_component_1442 captions-font-family-wise_player_1_component_1442-ProportionalSerif">Proportional Serif</option><option id="captions-font-family-wise_player_1_component_1442-MonospaceSerif" value="monospaceSerif" aria-labelledby="captions-font-family-wise_player_1_component_1442 captions-font-family-wise_player_1_component_1442-MonospaceSerif">Monospace Serif</option><option id="captions-font-family-wise_player_1_component_1442-Casual" value="casual" aria-labelledby="captions-font-family-wise_player_1_component_1442 captions-font-family-wise_player_1_component_1442-Casual">Casual</option><option id="captions-font-family-wise_player_1_component_1442-Script" value="script" aria-labelledby="captions-font-family-wise_player_1_component_1442 captions-font-family-wise_player_1_component_1442-Script">Script</option><option id="captions-font-family-wise_player_1_component_1442-SmallCaps" value="small-caps" aria-labelledby="captions-font-family-wise_player_1_component_1442 captions-font-family-wise_player_1_component_1442-SmallCaps">Small Caps</option></select></fieldset></div><div class="vjs-track-settings-controls"></div></div><p class="vjs-control-text">End of dialog window.</p></div><div videoid="object6767184763310" wiseplayerindex="1" playertype="wise" class="wiseplayershaw"><div class="play-number"><span>34</span><i><svg width="15px" height="11px" viewBox="0 0 15 11" version="1.1"><g id="文档详情页" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="2.3.1Documentation-Desktop-1920" transform="translate(-1334.000000, -2831.000000)"><g id="Group-7" transform="translate(520.000000, 2569.000000)"><g id="ic_view" transform="translate(814.000000, 259.000000)"><rect id="矩形" opacity="0.2" x="0" y="0" width="16" height="16"></rect><path d="M7.83333333,3.33333333 C4.74205364,3.33635162 1.94529498,5.16771838 0.706666667,8 C0.653333333,8.128 0.653333333,8.272 0.706666667,8.4 C1.94529498,11.2322816 4.74205364,13.0636484 7.83333333,13.066713 C10.2799392,13.0751325 12.5854758,11.9223642 14.0466667,9.96 C14.1538464,9.81709376 14.1766449,9.62786327 14.1064743,9.46358983 C14.0363037,9.29931638 13.8838246,9.18495702 13.7064743,9.16358982 C13.529124,9.14222262 13.3538463,9.21709375 13.2466667,9.36 C11.9736331,11.0697245 9.96493305,12.0740745 7.83333333,12.0666667 C5.21930483,12.0625944 2.83949297,10.5590096 1.71333333,8.2 C2.8525202,5.80258442 5.28704761,4.29150533 7.94100578,4.33456577 C10.594964,4.3776262 12.9791884,5.96688947 14.04,8.4 C14.1114531,8.56434218 14.265154,8.67808083 14.4432051,8.69837171 C14.6212561,8.71866258 14.7966072,8.64242301 14.9032051,8.4983717 C15.009803,8.35432039 15.0314531,8.16434217 14.96,8 C13.7213717,5.16771838 10.924613,3.33635162 7.83333333,3.33333333 Z" id="路径" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path><path d="M7.83333333,5.53333195 C6.61080734,5.53209462 5.544019,6.36231359 5.24497492,7.54770128 C4.94593084,8.73308896 5.49123358,9.96999875 6.56804799,10.5488269 C7.64486241,11.1276551 8.97735379,10.9001301 9.80108415,9.99678101 C10.6248145,9.0934319 10.7287787,7.74565879 10.0533333,6.72666667 C9.94736797,6.56325905 9.82201175,6.4132793 9.68,6.28 C9.18399727,5.80192485 8.52222631,5.53434958 7.83333333,5.53333195 Z M7.83333333,9.86666994 C7.08238462,9.86814757 6.42318765,9.36724437 6.22342868,8.64335038 C6.02366972,7.91945638 6.3326892,7.15137329 6.97812252,6.76752177 C7.62355584,6.38367026 8.44598108,6.47886157 8.98666667,7 C9.07498525,7.08401981 9.15328386,7.17797814 9.22,7.28 C9.40392075,7.55143891 9.50152012,7.87212256 9.50001749,8.2 C9.50001749,9.12047458 8.75380792,9.86666994 7.83333333,9.86666994 L7.83333333,9.86666994 Z" id="形状" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path></g></g></g></g></svg></i></div></div></div></div><p></p><p id="ZH-CN_TOPIC_0000001795531217__p366744023013"><strong>键盘+鼠标输入</strong></p><p id="ZH-CN_TOPIC_0000001795531217__p7170161314349">键盘 Ctrl 键+鼠标滚轮</p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="25.03%"><p id="ZH-CN_TOPIC_0000001795531217__p17172104723616"></p><div class="video-box" style="width: 109.441px; height: 109.441px;"><div videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.36796618942567668063340126399060:20260405162346:2800:CC58D36278BE4D3324E30E7F565DAE0DF2B2AD15386279560D01614E55B4F700.mp4" videoid="object422863918344" preload="none" id="wise_player_2" class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-workinghover vjs-v7 vjs-user-active wise_player_2-dimensions vjs-v8 vjs-error vjs-controls-disabled" tabindex="-1" lang="cn" translate="no" role="region" aria-label="Video Player"><video class="vjs-tech" id="wise_player_2_html5_api" preload="none" videoid="object422863918344" videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.36796618942567668063340126399060:20260405162346:2800:CC58D36278BE4D3324E30E7F565DAE0DF2B2AD15386279560D01614E55B4F700.mp4" tabindex="-1" loop="" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.36796618942567668063340126399060:20260405162346:2800:CC58D36278BE4D3324E30E7F565DAE0DF2B2AD15386279560D01614E55B4F700.mp4"></video><div class="vjs-poster vjs-hidden" aria-disabled="false"></div><div class="vjs-title-bar vjs-hidden"><div class="vjs-title-bar-title" id="vjs-title-bar-title-27"></div><div class="vjs-title-bar-description" id="vjs-title-bar-description-28"></div></div><div class="vjs-text-track-display" translate="yes" aria-live="off" aria-atomic="true"><div style="position: absolute; inset: 0px; margin: 1.5%;"></div></div><div class="vjs-loading-spinner" dir="ltr"><span class="vjs-control-text">Video Player is loading.</span></div><div class="vjs-control-bar" dir="ltr"><div class="vjs-current-time vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Current Time&nbsp;</span><span class="vjs-current-time-display" role="presentation">0:00</span></div><div class="vjs-progress-control vjs-control"><div tabindex="0" class="vjs-progress-holder vjs-slider vjs-slider-horizontal" role="slider" aria-valuenow="0.00" aria-valuemin="0" aria-valuemax="100" aria-label="Progress Bar" aria-valuetext="0:00 of -:-"><div class="vjs-load-progress"><span class="vjs-control-text"><span>Loaded</span>: <span class="vjs-control-text-loaded-percentage">0%</span></span></div><div class="vjs-mouse-display"><div class="vjs-time-tooltip" aria-hidden="true"></div></div><div class="vjs-play-progress vjs-slider-bar" aria-hidden="true" style="width: 0%;"><div class="vjs-time-tooltip" aria-hidden="true" style="right: 0px;">0:00</div></div></div></div><div class="vjs-duration vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Duration&nbsp;</span><span class="vjs-duration-display" role="presentation">-:-</span></div><div class="vjs-volume-panel vjs-control vjs-volume-panel-vertical"><div class="vjs-volume-control vjs-control vjs-volume-vertical"><div tabindex="0" class="vjs-volume-bar vjs-slider-bar vjs-slider vjs-slider-vertical" role="slider" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Volume Level" aria-live="polite" aria-valuetext="100%"><div class="vjs-mouse-display"><div class="vjs-volume-tooltip" aria-hidden="true"></div></div><div class="vjs-volume-level"><span class="vjs-control-text"></span></div></div></div></div><div class="vjs-playback-rate vjs-menu-button vjs-menu-button-popup vjs-control vjs-button"><div class="vjs-playback-rate-value" id="vjs-playback-rate-value-label-wise_player_2_component_225">1x</div><div class="vjs-menu"><ul class="vjs-menu-content" role="menu"><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.8x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.5x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item vjs-selected" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="true"><span class="vjs-menu-item-text">1x</span><span class="vjs-control-text" aria-live="polite">, selected</span></li></ul></div></div></div><div class="vjs-error-display vjs-modal-dialog" tabindex="-1" aria-describedby="wise_player_2_component_332_description" aria-hidden="false" aria-label="Modal Window" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_2_component_332_description">This is a modal window.</p><div class="vjs-modal-dialog-content" role="document">The media could not be loaded, either because the server or network failed or because the format is not supported.</div></div><div class="vjs-modal-dialog vjs-hidden  vjs-text-track-settings" tabindex="-1" aria-describedby="wise_player_2_component_338_description" aria-hidden="true" aria-label="Caption Settings Dialog" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_2_component_338_description">Beginning of dialog window. Escape will cancel and close the window.</p><div class="vjs-modal-dialog-content" role="document"><div class="vjs-track-settings-colors"><fieldset class="vjs-fg vjs-track-setting"><legend id="captions-text-legend-wise_player_2_component_338">Text</legend><span class="vjs-text-color"><label id="captions-foreground-color-wise_player_2_component_338" for="vjs_select_364" class="vjs-label">Color</label><select aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338" id="vjs_select_364"><option id="captions-foreground-color-wise_player_2_component_338-White" value="#FFF" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-White">White</option><option id="captions-foreground-color-wise_player_2_component_338-Black" value="#000" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-Black">Black</option><option id="captions-foreground-color-wise_player_2_component_338-Red" value="#F00" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-Red">Red</option><option id="captions-foreground-color-wise_player_2_component_338-Green" value="#0F0" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-Green">Green</option><option id="captions-foreground-color-wise_player_2_component_338-Blue" value="#00F" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-Blue">Blue</option><option id="captions-foreground-color-wise_player_2_component_338-Yellow" value="#FF0" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-Yellow">Yellow</option><option id="captions-foreground-color-wise_player_2_component_338-Magenta" value="#F0F" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-Magenta">Magenta</option><option id="captions-foreground-color-wise_player_2_component_338-Cyan" value="#0FF" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338 captions-foreground-color-wise_player_2_component_338-Cyan">Cyan</option></select></span><span class="vjs-text-opacity vjs-opacity"><label id="captions-foreground-opacity-wise_player_2_component_338" for="vjs_select_365" class="vjs-label">Opacity</label><select aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-opacity-wise_player_2_component_338" id="vjs_select_365"><option id="captions-foreground-opacity-wise_player_2_component_338-Opaque" value="1" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-opacity-wise_player_2_component_338 captions-foreground-opacity-wise_player_2_component_338-Opaque">Opaque</option><option id="captions-foreground-opacity-wise_player_2_component_338-SemiTransparent" value="0.5" aria-labelledby="captions-text-legend-wise_player_2_component_338 captions-foreground-opacity-wise_player_2_component_338 captions-foreground-opacity-wise_player_2_component_338-SemiTransparent">Semi-Transparent</option></select></span></fieldset><fieldset class="vjs-bg vjs-track-setting"><legend id="captions-background-wise_player_2_component_338">Text Background</legend><span class="vjs-bg-color"><label id="captions-background-color-wise_player_2_component_338" for="vjs_select_366" class="vjs-label">Color</label><select aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338" id="vjs_select_366"><option id="captions-background-color-wise_player_2_component_338-Black" value="#000" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-Black">Black</option><option id="captions-background-color-wise_player_2_component_338-White" value="#FFF" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-White">White</option><option id="captions-background-color-wise_player_2_component_338-Red" value="#F00" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-Red">Red</option><option id="captions-background-color-wise_player_2_component_338-Green" value="#0F0" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-Green">Green</option><option id="captions-background-color-wise_player_2_component_338-Blue" value="#00F" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-Blue">Blue</option><option id="captions-background-color-wise_player_2_component_338-Yellow" value="#FF0" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-Yellow">Yellow</option><option id="captions-background-color-wise_player_2_component_338-Magenta" value="#F0F" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-Magenta">Magenta</option><option id="captions-background-color-wise_player_2_component_338-Cyan" value="#0FF" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-color-wise_player_2_component_338 captions-background-color-wise_player_2_component_338-Cyan">Cyan</option></select></span><span class="vjs-bg-opacity vjs-opacity"><label id="captions-background-opacity-wise_player_2_component_338" for="vjs_select_367" class="vjs-label">Opacity</label><select aria-labelledby="captions-background-wise_player_2_component_338 captions-background-opacity-wise_player_2_component_338" id="vjs_select_367"><option id="captions-background-opacity-wise_player_2_component_338-Opaque" value="1" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-opacity-wise_player_2_component_338 captions-background-opacity-wise_player_2_component_338-Opaque">Opaque</option><option id="captions-background-opacity-wise_player_2_component_338-SemiTransparent" value="0.5" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-opacity-wise_player_2_component_338 captions-background-opacity-wise_player_2_component_338-SemiTransparent">Semi-Transparent</option><option id="captions-background-opacity-wise_player_2_component_338-Transparent" value="0" aria-labelledby="captions-background-wise_player_2_component_338 captions-background-opacity-wise_player_2_component_338 captions-background-opacity-wise_player_2_component_338-Transparent">Transparent</option></select></span></fieldset><fieldset class="vjs-window vjs-track-setting"><legend id="captions-window-wise_player_2_component_338">Caption Area Background</legend><span class="vjs-window-color"><label id="captions-window-color-wise_player_2_component_338" for="vjs_select_368" class="vjs-label">Color</label><select aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338" id="vjs_select_368"><option id="captions-window-color-wise_player_2_component_338-Black" value="#000" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-Black">Black</option><option id="captions-window-color-wise_player_2_component_338-White" value="#FFF" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-White">White</option><option id="captions-window-color-wise_player_2_component_338-Red" value="#F00" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-Red">Red</option><option id="captions-window-color-wise_player_2_component_338-Green" value="#0F0" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-Green">Green</option><option id="captions-window-color-wise_player_2_component_338-Blue" value="#00F" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-Blue">Blue</option><option id="captions-window-color-wise_player_2_component_338-Yellow" value="#FF0" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-Yellow">Yellow</option><option id="captions-window-color-wise_player_2_component_338-Magenta" value="#F0F" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-Magenta">Magenta</option><option id="captions-window-color-wise_player_2_component_338-Cyan" value="#0FF" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-color-wise_player_2_component_338 captions-window-color-wise_player_2_component_338-Cyan">Cyan</option></select></span><span class="vjs-window-opacity vjs-opacity"><label id="captions-window-opacity-wise_player_2_component_338" for="vjs_select_369" class="vjs-label">Opacity</label><select aria-labelledby="captions-window-wise_player_2_component_338 captions-window-opacity-wise_player_2_component_338" id="vjs_select_369"><option id="captions-window-opacity-wise_player_2_component_338-Transparent" value="0" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-opacity-wise_player_2_component_338 captions-window-opacity-wise_player_2_component_338-Transparent">Transparent</option><option id="captions-window-opacity-wise_player_2_component_338-SemiTransparent" value="0.5" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-opacity-wise_player_2_component_338 captions-window-opacity-wise_player_2_component_338-SemiTransparent">Semi-Transparent</option><option id="captions-window-opacity-wise_player_2_component_338-Opaque" value="1" aria-labelledby="captions-window-wise_player_2_component_338 captions-window-opacity-wise_player_2_component_338 captions-window-opacity-wise_player_2_component_338-Opaque">Opaque</option></select></span></fieldset></div><div class="vjs-track-settings-font"><fieldset class="vjs-font-percent vjs-track-setting"><legend id="captions-font-size-wise_player_2_component_338">Font Size</legend><select aria-labelledby="captions-font-size-wise_player_2_component_338" id="vjs_select_370"><option id="captions-font-size-wise_player_2_component_338-50" value="0.50" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-50">50%</option><option id="captions-font-size-wise_player_2_component_338-75" value="0.75" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-75">75%</option><option id="captions-font-size-wise_player_2_component_338-100" value="1.00" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-100">100%</option><option id="captions-font-size-wise_player_2_component_338-125" value="1.25" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-125">125%</option><option id="captions-font-size-wise_player_2_component_338-150" value="1.50" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-150">150%</option><option id="captions-font-size-wise_player_2_component_338-175" value="1.75" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-175">175%</option><option id="captions-font-size-wise_player_2_component_338-200" value="2.00" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-200">200%</option><option id="captions-font-size-wise_player_2_component_338-300" value="3.00" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-300">300%</option><option id="captions-font-size-wise_player_2_component_338-400" value="4.00" aria-labelledby="captions-font-size-wise_player_2_component_338 captions-font-size-wise_player_2_component_338-400">400%</option></select></fieldset><fieldset class="vjs-edge-style vjs-track-setting"><legend id="wise_player_2_component_338">Text Edge Style</legend><select aria-labelledby="wise_player_2_component_338" id="vjs_select_371"><option id="wise_player_2_component_338-None" value="none" aria-labelledby="wise_player_2_component_338 wise_player_2_component_338-None">None</option><option id="wise_player_2_component_338-Raised" value="raised" aria-labelledby="wise_player_2_component_338 wise_player_2_component_338-Raised">Raised</option><option id="wise_player_2_component_338-Depressed" value="depressed" aria-labelledby="wise_player_2_component_338 wise_player_2_component_338-Depressed">Depressed</option><option id="wise_player_2_component_338-Uniform" value="uniform" aria-labelledby="wise_player_2_component_338 wise_player_2_component_338-Uniform">Uniform</option><option id="wise_player_2_component_338-Dropshadow" value="dropshadow" aria-labelledby="wise_player_2_component_338 wise_player_2_component_338-Dropshadow">Drop shadow</option></select></fieldset><fieldset class="vjs-font-family vjs-track-setting"><legend id="captions-font-family-wise_player_2_component_338">Font Family</legend><select aria-labelledby="captions-font-family-wise_player_2_component_338" id="vjs_select_372"><option id="captions-font-family-wise_player_2_component_338-ProportionalSansSerif" value="proportionalSansSerif" aria-labelledby="captions-font-family-wise_player_2_component_338 captions-font-family-wise_player_2_component_338-ProportionalSansSerif">Proportional Sans-Serif</option><option id="captions-font-family-wise_player_2_component_338-MonospaceSansSerif" value="monospaceSansSerif" aria-labelledby="captions-font-family-wise_player_2_component_338 captions-font-family-wise_player_2_component_338-MonospaceSansSerif">Monospace Sans-Serif</option><option id="captions-font-family-wise_player_2_component_338-ProportionalSerif" value="proportionalSerif" aria-labelledby="captions-font-family-wise_player_2_component_338 captions-font-family-wise_player_2_component_338-ProportionalSerif">Proportional Serif</option><option id="captions-font-family-wise_player_2_component_338-MonospaceSerif" value="monospaceSerif" aria-labelledby="captions-font-family-wise_player_2_component_338 captions-font-family-wise_player_2_component_338-MonospaceSerif">Monospace Serif</option><option id="captions-font-family-wise_player_2_component_338-Casual" value="casual" aria-labelledby="captions-font-family-wise_player_2_component_338 captions-font-family-wise_player_2_component_338-Casual">Casual</option><option id="captions-font-family-wise_player_2_component_338-Script" value="script" aria-labelledby="captions-font-family-wise_player_2_component_338 captions-font-family-wise_player_2_component_338-Script">Script</option><option id="captions-font-family-wise_player_2_component_338-SmallCaps" value="small-caps" aria-labelledby="captions-font-family-wise_player_2_component_338 captions-font-family-wise_player_2_component_338-SmallCaps">Small Caps</option></select></fieldset></div><div class="vjs-track-settings-controls"></div></div><p class="vjs-control-text">End of dialog window.</p></div><div videoid="object422863918344" wiseplayerindex="2" playertype="wise" class="wiseplayershaw"><div class="play-number"><span>28</span><i><svg width="15px" height="11px" viewBox="0 0 15 11" version="1.1"><g id="文档详情页" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="2.3.1Documentation-Desktop-1920" transform="translate(-1334.000000, -2831.000000)"><g id="Group-7" transform="translate(520.000000, 2569.000000)"><g id="ic_view" transform="translate(814.000000, 259.000000)"><rect id="矩形" opacity="0.2" x="0" y="0" width="16" height="16"></rect><path d="M7.83333333,3.33333333 C4.74205364,3.33635162 1.94529498,5.16771838 0.706666667,8 C0.653333333,8.128 0.653333333,8.272 0.706666667,8.4 C1.94529498,11.2322816 4.74205364,13.0636484 7.83333333,13.066713 C10.2799392,13.0751325 12.5854758,11.9223642 14.0466667,9.96 C14.1538464,9.81709376 14.1766449,9.62786327 14.1064743,9.46358983 C14.0363037,9.29931638 13.8838246,9.18495702 13.7064743,9.16358982 C13.529124,9.14222262 13.3538463,9.21709375 13.2466667,9.36 C11.9736331,11.0697245 9.96493305,12.0740745 7.83333333,12.0666667 C5.21930483,12.0625944 2.83949297,10.5590096 1.71333333,8.2 C2.8525202,5.80258442 5.28704761,4.29150533 7.94100578,4.33456577 C10.594964,4.3776262 12.9791884,5.96688947 14.04,8.4 C14.1114531,8.56434218 14.265154,8.67808083 14.4432051,8.69837171 C14.6212561,8.71866258 14.7966072,8.64242301 14.9032051,8.4983717 C15.009803,8.35432039 15.0314531,8.16434217 14.96,8 C13.7213717,5.16771838 10.924613,3.33635162 7.83333333,3.33333333 Z" id="路径" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path><path d="M7.83333333,5.53333195 C6.61080734,5.53209462 5.544019,6.36231359 5.24497492,7.54770128 C4.94593084,8.73308896 5.49123358,9.96999875 6.56804799,10.5488269 C7.64486241,11.1276551 8.97735379,10.9001301 9.80108415,9.99678101 C10.6248145,9.0934319 10.7287787,7.74565879 10.0533333,6.72666667 C9.94736797,6.56325905 9.82201175,6.4132793 9.68,6.28 C9.18399727,5.80192485 8.52222631,5.53434958 7.83333333,5.53333195 Z M7.83333333,9.86666994 C7.08238462,9.86814757 6.42318765,9.36724437 6.22342868,8.64335038 C6.02366972,7.91945638 6.3326892,7.15137329 6.97812252,6.76752177 C7.62355584,6.38367026 8.44598108,6.47886157 8.98666667,7 C9.07498525,7.08401981 9.15328386,7.17797814 9.22,7.28 C9.40392075,7.55143891 9.50152012,7.87212256 9.50001749,8.2 C9.50001749,9.12047458 8.75380792,9.86666994 7.83333333,9.86666994 L7.83333333,9.86666994 Z" id="形状" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path></g></g></g></g></svg></i></div></div></div></div><p></p><p id="ZH-CN_TOPIC_0000001795531217__p9667124073014"><strong>键盘输入</strong></p><p id="ZH-CN_TOPIC_0000001795531217__p24835317354">键盘 Ctrl 键+“+/-”键</p></td><td class="cell-norowborder" style="border: none;" valign="top" width="25%"><p id="ZH-CN_TOPIC_0000001795531217__p275344915361"></p><div class="video-box" style="width: 109.25px; height: 109.25px;"><div videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.27395149442192392098706498438646:20260405162346:2800:E478D2A25E3A34C0933206C20BF36D46C1D974E087AE4C1AC8BD353B9A0B2B7D.mp4" videoid="object10542123320354" preload="none" id="wise_player_3" class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-workinghover vjs-v7 vjs-user-active wise_player_3-dimensions vjs-v8 vjs-error vjs-controls-disabled" tabindex="-1" lang="cn" translate="no" role="region" aria-label="Video Player"><video class="vjs-tech" id="wise_player_3_html5_api" preload="none" videoid="object10542123320354" videodata="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.27395149442192392098706498438646:20260405162346:2800:E478D2A25E3A34C0933206C20BF36D46C1D974E087AE4C1AC8BD353B9A0B2B7D.mp4" tabindex="-1" loop="" src="https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/publicContent/011/111/111/0000000000011111111.20260205170810.27395149442192392098706498438646:20260405162346:2800:E478D2A25E3A34C0933206C20BF36D46C1D974E087AE4C1AC8BD353B9A0B2B7D.mp4"></video><div class="vjs-poster vjs-hidden" aria-disabled="false"></div><div class="vjs-title-bar vjs-hidden"><div class="vjs-title-bar-title" id="vjs-title-bar-title-408"></div><div class="vjs-title-bar-description" id="vjs-title-bar-description-409"></div></div><div class="vjs-text-track-display" translate="yes" aria-live="off" aria-atomic="true"><div style="position: absolute; inset: 0px; margin: 1.5%;"></div></div><div class="vjs-loading-spinner" dir="ltr"><span class="vjs-control-text">Video Player is loading.</span></div><div class="vjs-control-bar" dir="ltr"><div class="vjs-current-time vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Current Time&nbsp;</span><span class="vjs-current-time-display" role="presentation">0:00</span></div><div class="vjs-progress-control vjs-control"><div tabindex="0" class="vjs-progress-holder vjs-slider vjs-slider-horizontal" role="slider" aria-valuenow="0.00" aria-valuemin="0" aria-valuemax="100" aria-label="Progress Bar" aria-valuetext="0:00 of -:-"><div class="vjs-load-progress"><span class="vjs-control-text"><span>Loaded</span>: <span class="vjs-control-text-loaded-percentage">0%</span></span></div><div class="vjs-mouse-display"><div class="vjs-time-tooltip" aria-hidden="true"></div></div><div class="vjs-play-progress vjs-slider-bar" aria-hidden="true" style="width: 0%;"><div class="vjs-time-tooltip" aria-hidden="true" style="right: 0px;">0:00</div></div></div></div><div class="vjs-duration vjs-time-control vjs-control"><span class="vjs-control-text" role="presentation">Duration&nbsp;</span><span class="vjs-duration-display" role="presentation">-:-</span></div><div class="vjs-volume-panel vjs-control vjs-volume-panel-vertical"><div class="vjs-volume-control vjs-control vjs-volume-vertical"><div tabindex="0" class="vjs-volume-bar vjs-slider-bar vjs-slider vjs-slider-vertical" role="slider" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Volume Level" aria-live="polite" aria-valuetext="100%"><div class="vjs-mouse-display"><div class="vjs-volume-tooltip" aria-hidden="true"></div></div><div class="vjs-volume-level"><span class="vjs-control-text"></span></div></div></div></div><div class="vjs-playback-rate vjs-menu-button vjs-menu-button-popup vjs-control vjs-button"><div class="vjs-playback-rate-value" id="vjs-playback-rate-value-label-wise_player_3_component_593">1x</div><div class="vjs-menu"><ul class="vjs-menu-content" role="menu"><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.8x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.5x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="false"><span class="vjs-menu-item-text">1.2x</span><span class="vjs-control-text" aria-live="polite"></span></li><li class="vjs-menu-item vjs-selected" tabindex="-1" role="menuitemradio" aria-disabled="false" aria-checked="true"><span class="vjs-menu-item-text">1x</span><span class="vjs-control-text" aria-live="polite">, selected</span></li></ul></div></div></div><div class="vjs-error-display vjs-modal-dialog" tabindex="-1" aria-describedby="wise_player_3_component_700_description" aria-hidden="false" aria-label="Modal Window" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_3_component_700_description">This is a modal window.</p><div class="vjs-modal-dialog-content" role="document">The media could not be loaded, either because the server or network failed or because the format is not supported.</div></div><div class="vjs-modal-dialog vjs-hidden  vjs-text-track-settings" tabindex="-1" aria-describedby="wise_player_3_component_706_description" aria-hidden="true" aria-label="Caption Settings Dialog" role="dialog" aria-live="polite"><p class="vjs-modal-dialog-description vjs-control-text" id="wise_player_3_component_706_description">Beginning of dialog window. Escape will cancel and close the window.</p><div class="vjs-modal-dialog-content" role="document"><div class="vjs-track-settings-colors"><fieldset class="vjs-fg vjs-track-setting"><legend id="captions-text-legend-wise_player_3_component_706">Text</legend><span class="vjs-text-color"><label id="captions-foreground-color-wise_player_3_component_706" for="vjs_select_732" class="vjs-label">Color</label><select aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706" id="vjs_select_732"><option id="captions-foreground-color-wise_player_3_component_706-White" value="#FFF" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-White">White</option><option id="captions-foreground-color-wise_player_3_component_706-Black" value="#000" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-Black">Black</option><option id="captions-foreground-color-wise_player_3_component_706-Red" value="#F00" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-Red">Red</option><option id="captions-foreground-color-wise_player_3_component_706-Green" value="#0F0" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-Green">Green</option><option id="captions-foreground-color-wise_player_3_component_706-Blue" value="#00F" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-Blue">Blue</option><option id="captions-foreground-color-wise_player_3_component_706-Yellow" value="#FF0" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-Yellow">Yellow</option><option id="captions-foreground-color-wise_player_3_component_706-Magenta" value="#F0F" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-Magenta">Magenta</option><option id="captions-foreground-color-wise_player_3_component_706-Cyan" value="#0FF" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706 captions-foreground-color-wise_player_3_component_706-Cyan">Cyan</option></select></span><span class="vjs-text-opacity vjs-opacity"><label id="captions-foreground-opacity-wise_player_3_component_706" for="vjs_select_733" class="vjs-label">Opacity</label><select aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-opacity-wise_player_3_component_706" id="vjs_select_733"><option id="captions-foreground-opacity-wise_player_3_component_706-Opaque" value="1" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-opacity-wise_player_3_component_706 captions-foreground-opacity-wise_player_3_component_706-Opaque">Opaque</option><option id="captions-foreground-opacity-wise_player_3_component_706-SemiTransparent" value="0.5" aria-labelledby="captions-text-legend-wise_player_3_component_706 captions-foreground-opacity-wise_player_3_component_706 captions-foreground-opacity-wise_player_3_component_706-SemiTransparent">Semi-Transparent</option></select></span></fieldset><fieldset class="vjs-bg vjs-track-setting"><legend id="captions-background-wise_player_3_component_706">Text Background</legend><span class="vjs-bg-color"><label id="captions-background-color-wise_player_3_component_706" for="vjs_select_734" class="vjs-label">Color</label><select aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706" id="vjs_select_734"><option id="captions-background-color-wise_player_3_component_706-Black" value="#000" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-Black">Black</option><option id="captions-background-color-wise_player_3_component_706-White" value="#FFF" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-White">White</option><option id="captions-background-color-wise_player_3_component_706-Red" value="#F00" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-Red">Red</option><option id="captions-background-color-wise_player_3_component_706-Green" value="#0F0" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-Green">Green</option><option id="captions-background-color-wise_player_3_component_706-Blue" value="#00F" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-Blue">Blue</option><option id="captions-background-color-wise_player_3_component_706-Yellow" value="#FF0" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-Yellow">Yellow</option><option id="captions-background-color-wise_player_3_component_706-Magenta" value="#F0F" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-Magenta">Magenta</option><option id="captions-background-color-wise_player_3_component_706-Cyan" value="#0FF" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-color-wise_player_3_component_706 captions-background-color-wise_player_3_component_706-Cyan">Cyan</option></select></span><span class="vjs-bg-opacity vjs-opacity"><label id="captions-background-opacity-wise_player_3_component_706" for="vjs_select_735" class="vjs-label">Opacity</label><select aria-labelledby="captions-background-wise_player_3_component_706 captions-background-opacity-wise_player_3_component_706" id="vjs_select_735"><option id="captions-background-opacity-wise_player_3_component_706-Opaque" value="1" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-opacity-wise_player_3_component_706 captions-background-opacity-wise_player_3_component_706-Opaque">Opaque</option><option id="captions-background-opacity-wise_player_3_component_706-SemiTransparent" value="0.5" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-opacity-wise_player_3_component_706 captions-background-opacity-wise_player_3_component_706-SemiTransparent">Semi-Transparent</option><option id="captions-background-opacity-wise_player_3_component_706-Transparent" value="0" aria-labelledby="captions-background-wise_player_3_component_706 captions-background-opacity-wise_player_3_component_706 captions-background-opacity-wise_player_3_component_706-Transparent">Transparent</option></select></span></fieldset><fieldset class="vjs-window vjs-track-setting"><legend id="captions-window-wise_player_3_component_706">Caption Area Background</legend><span class="vjs-window-color"><label id="captions-window-color-wise_player_3_component_706" for="vjs_select_736" class="vjs-label">Color</label><select aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706" id="vjs_select_736"><option id="captions-window-color-wise_player_3_component_706-Black" value="#000" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-Black">Black</option><option id="captions-window-color-wise_player_3_component_706-White" value="#FFF" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-White">White</option><option id="captions-window-color-wise_player_3_component_706-Red" value="#F00" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-Red">Red</option><option id="captions-window-color-wise_player_3_component_706-Green" value="#0F0" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-Green">Green</option><option id="captions-window-color-wise_player_3_component_706-Blue" value="#00F" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-Blue">Blue</option><option id="captions-window-color-wise_player_3_component_706-Yellow" value="#FF0" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-Yellow">Yellow</option><option id="captions-window-color-wise_player_3_component_706-Magenta" value="#F0F" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-Magenta">Magenta</option><option id="captions-window-color-wise_player_3_component_706-Cyan" value="#0FF" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-color-wise_player_3_component_706 captions-window-color-wise_player_3_component_706-Cyan">Cyan</option></select></span><span class="vjs-window-opacity vjs-opacity"><label id="captions-window-opacity-wise_player_3_component_706" for="vjs_select_737" class="vjs-label">Opacity</label><select aria-labelledby="captions-window-wise_player_3_component_706 captions-window-opacity-wise_player_3_component_706" id="vjs_select_737"><option id="captions-window-opacity-wise_player_3_component_706-Transparent" value="0" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-opacity-wise_player_3_component_706 captions-window-opacity-wise_player_3_component_706-Transparent">Transparent</option><option id="captions-window-opacity-wise_player_3_component_706-SemiTransparent" value="0.5" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-opacity-wise_player_3_component_706 captions-window-opacity-wise_player_3_component_706-SemiTransparent">Semi-Transparent</option><option id="captions-window-opacity-wise_player_3_component_706-Opaque" value="1" aria-labelledby="captions-window-wise_player_3_component_706 captions-window-opacity-wise_player_3_component_706 captions-window-opacity-wise_player_3_component_706-Opaque">Opaque</option></select></span></fieldset></div><div class="vjs-track-settings-font"><fieldset class="vjs-font-percent vjs-track-setting"><legend id="captions-font-size-wise_player_3_component_706">Font Size</legend><select aria-labelledby="captions-font-size-wise_player_3_component_706" id="vjs_select_738"><option id="captions-font-size-wise_player_3_component_706-50" value="0.50" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-50">50%</option><option id="captions-font-size-wise_player_3_component_706-75" value="0.75" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-75">75%</option><option id="captions-font-size-wise_player_3_component_706-100" value="1.00" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-100">100%</option><option id="captions-font-size-wise_player_3_component_706-125" value="1.25" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-125">125%</option><option id="captions-font-size-wise_player_3_component_706-150" value="1.50" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-150">150%</option><option id="captions-font-size-wise_player_3_component_706-175" value="1.75" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-175">175%</option><option id="captions-font-size-wise_player_3_component_706-200" value="2.00" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-200">200%</option><option id="captions-font-size-wise_player_3_component_706-300" value="3.00" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-300">300%</option><option id="captions-font-size-wise_player_3_component_706-400" value="4.00" aria-labelledby="captions-font-size-wise_player_3_component_706 captions-font-size-wise_player_3_component_706-400">400%</option></select></fieldset><fieldset class="vjs-edge-style vjs-track-setting"><legend id="wise_player_3_component_706">Text Edge Style</legend><select aria-labelledby="wise_player_3_component_706" id="vjs_select_739"><option id="wise_player_3_component_706-None" value="none" aria-labelledby="wise_player_3_component_706 wise_player_3_component_706-None">None</option><option id="wise_player_3_component_706-Raised" value="raised" aria-labelledby="wise_player_3_component_706 wise_player_3_component_706-Raised">Raised</option><option id="wise_player_3_component_706-Depressed" value="depressed" aria-labelledby="wise_player_3_component_706 wise_player_3_component_706-Depressed">Depressed</option><option id="wise_player_3_component_706-Uniform" value="uniform" aria-labelledby="wise_player_3_component_706 wise_player_3_component_706-Uniform">Uniform</option><option id="wise_player_3_component_706-Dropshadow" value="dropshadow" aria-labelledby="wise_player_3_component_706 wise_player_3_component_706-Dropshadow">Drop shadow</option></select></fieldset><fieldset class="vjs-font-family vjs-track-setting"><legend id="captions-font-family-wise_player_3_component_706">Font Family</legend><select aria-labelledby="captions-font-family-wise_player_3_component_706" id="vjs_select_740"><option id="captions-font-family-wise_player_3_component_706-ProportionalSansSerif" value="proportionalSansSerif" aria-labelledby="captions-font-family-wise_player_3_component_706 captions-font-family-wise_player_3_component_706-ProportionalSansSerif">Proportional Sans-Serif</option><option id="captions-font-family-wise_player_3_component_706-MonospaceSansSerif" value="monospaceSansSerif" aria-labelledby="captions-font-family-wise_player_3_component_706 captions-font-family-wise_player_3_component_706-MonospaceSansSerif">Monospace Sans-Serif</option><option id="captions-font-family-wise_player_3_component_706-ProportionalSerif" value="proportionalSerif" aria-labelledby="captions-font-family-wise_player_3_component_706 captions-font-family-wise_player_3_component_706-ProportionalSerif">Proportional Serif</option><option id="captions-font-family-wise_player_3_component_706-MonospaceSerif" value="monospaceSerif" aria-labelledby="captions-font-family-wise_player_3_component_706 captions-font-family-wise_player_3_component_706-MonospaceSerif">Monospace Serif</option><option id="captions-font-family-wise_player_3_component_706-Casual" value="casual" aria-labelledby="captions-font-family-wise_player_3_component_706 captions-font-family-wise_player_3_component_706-Casual">Casual</option><option id="captions-font-family-wise_player_3_component_706-Script" value="script" aria-labelledby="captions-font-family-wise_player_3_component_706 captions-font-family-wise_player_3_component_706-Script">Script</option><option id="captions-font-family-wise_player_3_component_706-SmallCaps" value="small-caps" aria-labelledby="captions-font-family-wise_player_3_component_706 captions-font-family-wise_player_3_component_706-SmallCaps">Small Caps</option></select></fieldset></div><div class="vjs-track-settings-controls"></div></div><p class="vjs-control-text">End of dialog window.</p></div><div videoid="object10542123320354" wiseplayerindex="3" playertype="wise" class="wiseplayershaw"><div class="play-number"><span>27</span><i><svg width="15px" height="11px" viewBox="0 0 15 11" version="1.1"><g id="文档详情页" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="2.3.1Documentation-Desktop-1920" transform="translate(-1334.000000, -2831.000000)"><g id="Group-7" transform="translate(520.000000, 2569.000000)"><g id="ic_view" transform="translate(814.000000, 259.000000)"><rect id="矩形" opacity="0.2" x="0" y="0" width="16" height="16"></rect><path d="M7.83333333,3.33333333 C4.74205364,3.33635162 1.94529498,5.16771838 0.706666667,8 C0.653333333,8.128 0.653333333,8.272 0.706666667,8.4 C1.94529498,11.2322816 4.74205364,13.0636484 7.83333333,13.066713 C10.2799392,13.0751325 12.5854758,11.9223642 14.0466667,9.96 C14.1538464,9.81709376 14.1766449,9.62786327 14.1064743,9.46358983 C14.0363037,9.29931638 13.8838246,9.18495702 13.7064743,9.16358982 C13.529124,9.14222262 13.3538463,9.21709375 13.2466667,9.36 C11.9736331,11.0697245 9.96493305,12.0740745 7.83333333,12.0666667 C5.21930483,12.0625944 2.83949297,10.5590096 1.71333333,8.2 C2.8525202,5.80258442 5.28704761,4.29150533 7.94100578,4.33456577 C10.594964,4.3776262 12.9791884,5.96688947 14.04,8.4 C14.1114531,8.56434218 14.265154,8.67808083 14.4432051,8.69837171 C14.6212561,8.71866258 14.7966072,8.64242301 14.9032051,8.4983717 C15.009803,8.35432039 15.0314531,8.16434217 14.96,8 C13.7213717,5.16771838 10.924613,3.33635162 7.83333333,3.33333333 Z" id="路径" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path><path d="M7.83333333,5.53333195 C6.61080734,5.53209462 5.544019,6.36231359 5.24497492,7.54770128 C4.94593084,8.73308896 5.49123358,9.96999875 6.56804799,10.5488269 C7.64486241,11.1276551 8.97735379,10.9001301 9.80108415,9.99678101 C10.6248145,9.0934319 10.7287787,7.74565879 10.0533333,6.72666667 C9.94736797,6.56325905 9.82201175,6.4132793 9.68,6.28 C9.18399727,5.80192485 8.52222631,5.53434958 7.83333333,5.53333195 Z M7.83333333,9.86666994 C7.08238462,9.86814757 6.42318765,9.36724437 6.22342868,8.64335038 C6.02366972,7.91945638 6.3326892,7.15137329 6.97812252,6.76752177 C7.62355584,6.38367026 8.44598108,6.47886157 8.98666667,7 C9.07498525,7.08401981 9.15328386,7.17797814 9.22,7.28 C9.40392075,7.55143891 9.50152012,7.87212256 9.50001749,8.2 C9.50001749,9.12047458 8.75380792,9.86666994 7.83333333,9.86666994 L7.83333333,9.86666994 Z" id="形状" fill="#FFFFFF" fill-rule="nonzero" opacity="0.5"></path></g></g></g></g></svg></i></div></div></div></div><p></p><p id="ZH-CN_TOPIC_0000001795531217__p13667124083017"><strong>触控板输入</strong></p><p id="ZH-CN_TOPIC_0000001795531217__p15600413103618">触控板双指捏合</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row5667154015304"><td class="row-nocellborder" style="border: none;" valign="top" width="25%">&nbsp;&nbsp;</td><td class="row-nocellborder" style="border: none;" valign="top" width="24.97%">&nbsp;&nbsp;</td><td class="row-nocellborder" style="border: none;" valign="top" width="25.03%">&nbsp;&nbsp;</td><td class="cellrowborder" style="border: none;" valign="top" width="25%">&nbsp;&nbsp;</td></tr></tbody></table>

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170808.45739856367490839183984242325310:50001231000000:2800:3A2A8C602B7B0C98B7AC6740FE439617F63A71AC88ABD19963C74ACC8BE95BD2.png "点击放大")

## 交互规范

本章节介绍了在交互归一框架中，不同的交互事件下对应的各种输入设备的交互行为。

### 悬浮

**应用场景**

用户通过在某个元素上悬浮可以预览到更多信息或功能。

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

N/A

 |
| 

手写笔

 | 

笔尖靠近屏幕悬浮。

 |
| 

鼠标

 | 

光标移动到物体上。

 |
| 

触控板

 | 

光标移动到物体上。

 |
| 

键盘

 | 

N/A

 |
| 

灵犀指向遥控

 | 

光标移动到物体上。

 |
| 

灵犀悬浮触控

 | 

N/A

 |

手写笔的悬浮交互需要手写笔硬件支持悬浮能力

### 点击

**应用场景**

用户通过点击某个元素激活控件、访问新页面、或改变自身状态。

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

单指单击。

 |
| 

手写笔

 | 

笔尖单击屏幕。

 |
| 

鼠标

 | 

按压鼠标左键。

 |
| 

触控板

 | 

单指轻点/单指按压。

 |
| 

键盘

 | 

走焦状态下，移动焦点到对象上后按下回车键/空格键。

 |
| 

灵犀指向遥控

 | 

点击 OK 键。

 |
| 

灵犀悬浮触控

 | 

单指单击。

 |

一般地，触屏手指的按下/抬起行为对应于光标的按下/抬起行为。

在一些特殊场景，可能会存在使用鼠标/触摸板双击打开对象的交互方案，例如电脑模式下打开桌面应用或文件。此类情况需由应用单独特殊处理，且同一功能不能同时支持单击和双击两种交互方式。

### 双击

**应用场景**

用户通过双击进行某些快捷操作，如快速放大图片、点赞等。

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

单指点击两下。

 |
| 

手写笔

 | 

笔尖双击屏幕。

 |
| 

鼠标

 | 

快速点击鼠标左键两下。

 |
| 

触控板

 | 

单指轻点两下/单指按压两下。

 |
| 

键盘

 | 

走焦状态下，移动焦点到对象上后按压两次回车键/空格键。

 |
| 

灵犀指向遥控

 | 

快速点击 OK 键两下。

 |
| 

灵犀悬浮触控

 | 

单指点击两下。

 |

### 长按

**应用场景**

用户通过长按进行某些快捷操作，如长按视频倍速播放等。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170808.30939961283126132264501822746341:50001231000000:2800:E88002FED879462DDA324BF6AC68F7B38B69CDEC6D421A4147EB7963CA76B432.jpg "点击放大")

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

单指长按。

 |
| 

手写笔

 | 

笔尖长时间接触屏幕。

 |
| 

鼠标

 | 

长按左键。

 |
| 

触控板

 | 

单指长按。

 |
| 

键盘

 | 

走焦状态下，移动到对象上长按回车键/空格键。

 |
| 

灵犀指向遥控

 | 

长按 OK 键。

 |
| 

灵犀悬浮触控

 | 

单指长按。

 |

### 上下文菜单

**应用场景**

某个元素上显示弹出菜单或快捷方式菜单。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170809.70794878227775713278585509292445:50001231000000:2800:8B1C9873CE198C9B801F65211A6841DA87B35E85777D6BC3029E76DEB258859C.jpg "点击放大")

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

单指长按。

 |
| 

手写笔

 | 

笔尖长时间触控屏幕。

 |
| 

鼠标

 | 

单击右键。

 |
| 

触控板

 | 

双指轻点/按压 (与 PC 一致)。

 |
| 

键盘

 | 

Shift + F10 或 LOGO+M。

 |
| 

灵犀指向遥控

 | 

长按 OK 键

 |
| 

灵犀悬浮触控

 | 

单指长按

 |

这里的菜单指的是广义的菜单，即用于展示用户可执行的操作的临时性弹出窗口。

凡是在触屏上通过长按显示的菜单，都需要支持鼠标右键单击和触摸板双指单击的触发方式。

### 拖拽

**应用场景**

移动某个元素位置或者移动某个元素用于发送等。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170809.16050125483089962636538600897702:50001231000000:2800:63144D14265E385B9368602C2A59B86E8EBF304BA97330FF603ABB9BAB1299FE.jpg "点击放大")

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

长按并移动。

 |
| 

手写笔

 | 

笔尖长时间接触屏幕后滑动。

 |
| 

鼠标

 | 

按压左键并移动鼠标 (无需长按等待)。

 |
| 

触控板

 | 

按压并移动。

 |
| 

键盘

 | 

N/A

 |
| 

灵犀指向遥控

 | 

长按 OK 键并移动。

 |
| 

灵犀悬浮触控

 | 

长按并移动。

 |

### 滚动/平移

应用场景

滚动列表或页面。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170809.24885517910938685215808613990195:50001231000000:2800:16D5A6958520F6473A7F8169705CFC7D5AC36266A4DD8B4928E6A21CBC689A1A.jpg "点击放大")

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

单指接触屏幕后滑动。

 |
| 

手写笔

 | 

笔尖屏幕滑动。

 |
| 

鼠标

 | 

上下滚动滚轮/shift+上下滚动滚轮可以实现上下/左右滚动，指针不动。

有上下滚动时，通过 shift +滚轮左右滚动。无上下滚动时，滚轮可响应左右滚动。

自然滚动时，

滚轮向上滚动，显示页面上方内容。

滚轮向下滚动，显示页面下方内容。

滚轮每滚动 1 个刻痕，页面相应滚动一段距离，默认为 64vp，应用也可自行设定。

 |
| 

触控板

 | 

自然滚动时，触摸板上双指滑动行为与触屏上单指滑动行为一致。

双指向上滑动，显示页面下方内容。

双指向下滑动，显示页面上方内容。

双指滑动时，页面进行精细、连续的滚动；当双指离开触摸板时，页面根据离手速度继续进行减速滑动直到停止。

若列表是横向列表，则双指向左滑动，显示页面右边内容；双指向右滑动，显示页面左边内容。

 |
| 

键盘

 | 

N/A

 |
| 

灵犀指向遥控

 | 

在触控区滑动/按下 OK 键后滑动/按下方向键。

 |
| 

灵犀悬浮触控

 | 

单指接触触控板面后滑动。

 |

在鼠标、触控板滚动过程中，仅页面元素发生变化，光标不发生移动。

### 轻扫

**应用场景**

将一个页面切换至下一个页面或快速滚动页面。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170809.16116456909935677760972478816248:50001231000000:2800:BE0EC55E1AD43E1FA631CF8D2C0D9F833284D484ECF91BC4924FE1FEEFB15575.jpg "点击放大")

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

单指快速滑动。

 |
| 

手写笔

 | 

笔尖屏幕快速滑动。

 |
| 

鼠标

 | 

滚动一格或快速滚动后停止。

 |
| 

触控板

 | 

双指快速移动。

 |
| 

键盘

 | 

N/A

 |
| 

灵犀指向遥控

 | 

触控区快速滑动。

 |
| 

灵犀悬浮触控

 | 

单指快速滑动。

 |

在鼠标、触控板轻扫过程中，仅页面元素发生变化，光标不发生移动。

### 缩放对象

**应用场景**

查看图片或浏览页面时调整对象大小

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170809.57653161067288300208193616955833:50001231000000:2800:573D9CCE9D7F99FB7F15E8C7A7635A9D214FC336EDB64A8B1CCF57B9A20661E0.jpg "点击放大")

展开

| 
输入设备/方式

 | 

交互行为

 |
| :-- | :-- |
| 

触屏

 | 

双指张开为放大，双指捏合为缩小。

 |
| 

手写笔

 | 

N/A

 |
| 

鼠标

 | 

按下 Ctrl 键同时滚动鼠标滚轮，可按照光标位置放大或缩小内容。

\- 鼠标滚轮上滚，每滚动 1 个刻痕，以光标位置作为中心对象放大 N%。

\- 鼠标滚轮下滚，每滚动 1 个刻痕，对象缩小 N%。

 |
| 

触控板

 | 

触摸板上双指捏合行为与触屏上双指捏合行为一致，当光标移动到对象上后：

\- 触摸板双指向外扩展以放大内容。

\- 触摸板双指向内收拢以缩小内容。

优化显控比，以使用户能够轻松、快速、准确地调节到目标尺寸。

 |
| 

键盘

 | 

Ctrl+加号键：以对象的中心点使对象放大 N%。

Ctrl+减号键：以对象的中心点使对象缩小 N%。

 |
| 

灵犀指向遥控

 | 

N/A

 |
| 

灵犀悬浮触控

 | 

双指张开为放大，双指捏合为缩小。

 |

### 旋转对象

**应用场景**

编辑图片时旋转图片。

<table id="ZH-CN_TOPIC_0000001795531217__table106mcpsimp" class="layoutFixed idpTab"><tbody><tr id="ZH-CN_TOPIC_0000001795531217__row111mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__X235a1405d19570c57c7f14a68db40af36477484">输入设备/方式</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p114mcpsimp">交互行为</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row115mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p117mcpsimp">触屏</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p119mcpsimp">两个手指在屏幕旋转，对象跟随旋转。</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row120mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p122mcpsimp">手写笔</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p124mcpsimp">N/A</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row125mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p127mcpsimp">鼠标</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p129mcpsimp">N/A</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row130mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p132mcpsimp">触摸板</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p186731497564">N/A</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row137mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p139mcpsimp">键盘</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p141mcpsimp">N/A</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row142mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p144mcpsimp">灵犀指向遥控</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p146mcpsimp">N/A</p></td></tr><tr id="ZH-CN_TOPIC_0000001795531217__row147mcpsimp"><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p149mcpsimp">灵犀悬浮触控</p></td><td class="cellrowborder" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000001795531217__p151mcpsimp">两个手指在触控板面旋转，对象跟随旋转。</p></td></tr></tbody></table>

有些场景中触屏上双指可以同时进行缩放和旋转操作 (如图片/地图浏览)，触摸板应同步支持。

## 交互事件归一接口

为了保障用户在不同交互设备上的交互体一致，同时又尽量减少不同输入设备适配工作，建议使用交互事件归一接口。该接口涵盖用户基础的交互任务，并遵循了用户在触控、鼠标、触控板等设备的交互习惯。请参阅[交互事件归一开发文档](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-interaction)。

如用户有自定义响应的需求，也可根据开发文档中提供的接口做相应的修改。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260205170810.82238170994724542396293537417903:50001231000000:2800:BF0B94F3C14C65720F9B69283E6292A6920B72985C7D9A31FEFF05E9846D5FCE.png "点击放大")
