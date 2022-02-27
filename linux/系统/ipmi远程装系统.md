# ipmi远程装系统

## 前言

|部件|型号|
|---|---|
|产品名|NF5280M5|
|CPU|Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz|
|内存|DDR4 2933MHZ|

## 步骤

1. 登录ipmi
2. 打开Remote Control下拉菜单
3. 打开Console Redirection页面
4. 点击Launch KVM HTML5 Viewer按钮，会弹出一个新页面
5. 在新页面中，右上角处，点击Browser File，选择本地文件，然后点击Start Media
6. 点击右上角的绿色开机按钮，重启设备，等待等待自检和iso文件载入。（网络较差的话，iso文件载入会等待较长时间）