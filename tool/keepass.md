# keepass

## 简介

keepass是一个开源的密码管理工具，界面原始，支持众多平台。

官网：https://keepass.info/download.html

插件：https://keepass.info/plugins.html

## 设置中文

将语言文件下载到软件目录下的`language`文件夹。

在keepass界面，点击 view -> Change Language -> 选中中文。

## 数据库文件同步

### 直接在软件中设置webdav

使用webdav协议，密码文件存于坚果云。

遇到问题：

1. 保存密码的时候，会全量更改文件，触发dav的上传机制。

2. 断网，则无法读取密码文件。


