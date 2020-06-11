# terminal

## 前言

最近在研究windows terminal，感觉还可以。

可以通过设定 `commandline` 指定开启terminal后，运行的程序，从而达到快速跳入莫一台机器的效果。

文件夹中在地址栏里输入“wt”即可打开terminal (配合设置"startingDirectory" = null, 可以在当前目录下打开terminal)

## 参考网址

[所见既所得主题配置](https://terminal.sexy/)

[settings.json 配置文件使用说明](https://github.com/microsoft/terminal/blob/master/doc/user-docs/UsingJsonSettings.md)

[settings.json 配置参数](https://github.com/microsoft/terminal/blob/master/doc/cascadia/SettingsSchema.md)

[主题参考](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/windowsterminal)

## profile

``` json
"scrollbarState":"visible",  /* 隐藏右侧的滚动条，hidden或者visible */

"tabTitle":"str",  /* 用str覆盖name属性的内容 */
"suppressApplicationTitle": true,  /* 禁止应用程序消息修改tabTitle属性的内容 */

"useAcrylic":true,  /* 鼠标在terminal上时，会模糊。移开则清晰 */

"cursorShape": "emptyBox",  /* 光标的形状。此值为空心状 */
"cursorColor": "#000000",  /* 光标的颜色 */

"startingDirectory" = null,  /* 设置打开终端的目录。默认为用户目录。此设置会改为当前目录打开终端 */
```

## 快捷键

shift + alt + w ：关闭当前标签页

ctrl + shift + page-up : 向上翻页

ctrl + shift + page-down : 向下翻页

### 窗口拆分

shift + alt + + ：向右拆分

shift + alt + - ：向下拆分

alt + up|down|left|right ：向左拆分

alt + up|down|left|right ：向右拆分