# win10下git-bash的使用

参考连接：

https://www.codercto.com/a/35063.html

https://mintty.github.io/mintty.1.html

## 修改bash默认主题

在用户根目录下建立 `.minttyrc` 文件

``` bash
vim ~/.minttyrc
```

输入以下内容

``` txt
FontHeight=12
Font=Consolas
Transparency=off  # 透明度
FontSmoothing=full
Locale=zh_CN
Charset=GBK
Columns=100
Rows=30
OpaqueWhenFocused=no
Scrollbar=none
Language=zh_CN

ForegroundColour=215,215,215
BackgroundColour=0,0,0
CursorColour=0,255,64

BoldBlack=128,128,128
Red=255,64,40
BoldRed=255,128,64
Green=64,200,64
BoldGreen=64,255,64
Yellow=190,190,0
BoldYellow=255,255,64
Blue=0,128,255
BoldBlue=128,160,255
Magenta=211,54,130
BoldMagenta=255,128,255
Cyan=64,190,190
BoldCyan=128,255,255
White=200,200,200
BoldWhite=255,255,255
CursorType=block
CursorBlinks=no
BoldAsColour=no
FontWeight=700
FontIsBold=yes
```