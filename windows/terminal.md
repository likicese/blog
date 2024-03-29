# terminal

## 前言

最近在研究windows terminal，感觉还可以。

可以通过设定 `commandline` 指定开启terminal后，运行的程序，从而达到快速跳入某一台机器的效果。

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
## 完整的属性建议

``` json
{
    "$schema": "https://aka.ms/terminal-profiles-schema",
    "actions": 
    [
        {
            "command": 
            {
                "action": "sendInput", 
                "input": "ssh 192.168.1.2\ntail -f /var/log/nginx/access.log\n"
            },
            "name": "查看nginx的日志",
            "keys": "ctrl+alt+9"
        }
    ],
    "largePasteWarning": false,  /* 禁用粘贴文字大于5KB时的提醒框 */
    "multiLinePasteWarning": false,  /* 禁用粘贴文字存在换行符时的提醒框 */
}
```

## Git Bash的设置

前提：安装windows版的git

将下面的配置放到配置文件中。

位置：profiles -> list，即和power shell同级

```
{
                // Make changes here to the cmd.exe profile.
                "guid": "{0caa98ad-35be-5e56-a8ff-afceefea61a1}",
                "name": "git",
                "commandline": "C:\\Program Files\\Git\\bin\\bash.exe --login -i",
                "icon": "%SystemDrive%\\Program Files\\Git\\mingw64\\share\\git\\git-for-windows.ico",  /* 直接使用git的图标 */
                "scrollbarState": "hidden",  /* 隐藏滚动条 */
                "cursorShape": "emptyBox",  /* 光标为框 */
                "hidden": false
},
```

## Git-bash闪屏

当前用户生效

``` bat
echo "set bell-style none" >> ~/.inputrc
```

修改Git安装目录下/etc/inputrc文件，一般位于`C:\Program Files\Git`。将`set bell-style visible`改成`set bell-style none`即可

## 快捷键

shift + ctrl + w ：关闭当前标签页

shift + ctrl + page-up : 向上翻页

shift + ctrl + page-down : 向下翻页

### 窗口拆分

shift + alt + + ：向右拆分

shift + alt + - ：向下拆分

alt + up|down|left|right ：拆分后，移动焦点所处位置

## 疑难杂症

### vim后自动进入Replace模式

请打开powershell，把 `选项 -> 快速编辑模式` 的勾选去掉

### ctrl + v 和 vim自身热键冲突

windows terminal将`ctrl + v`设置为粘贴，而这在vim中是块选择热键，两者冲突。

找到`settings.json`文件中如下设置项，注释掉

```
{ "command": "paste", "keys": "ctrl+v" },
```

### WSL找不到

#### 报错：

```
在配置文件列表中找不到你的默认配置文件-使用第一个配置文件。请进行检查以确保 "defaultProfile" 与你的某个配置文件的 GUID 相匹配。
```

terminal报错后，会自动在配置文件中设置一个wsl。此时，该wsl可以打开。

怀疑是更新系统某些东西后，带来的后遗症

#### 解决：

保存好配置文件，重装terminal。

