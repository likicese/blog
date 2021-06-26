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

## chrome自动填充

### keepass安装插件

KeePassHttp.plgx

下载地址：https://raw.github.com/pfn/keepasshttp/master/KeePassHttp.plgx

下载后，将文件放入`Plugins`文件夹，重启keepass即可

启动后，该程序将监听127.0.0.1:19455和::1:19455

### chrome安装插件

KeePassHttp-Connector，似乎原名是ChromeIpass

安装后，在拓展中点开`Connect`，将会连接本地的KeePassHttp。弹出一个窗口，填入标识名，该名随意。填写后，即可连入keepass。

### 使用

使用密码：当url匹配时，chrome的插件会向keepass发送一条信息，确认授权请求。此时图标将会发亮。点击允许且记住该操作。以后，每当访问该页面时，chrome插件图标就会亮起，此时可以选择账户。

保存密码：在用户名、密码输入界面，有一把小锁。输入用户名后，点击小锁，输入密码。然后点击`fill in`，登录成功后，chrome插件发亮，询问是否保存密码。保存即可。通过该方式保存的密码，默认放在KeePassHttp Passwords文件夹下。

## 在ubuntu中

### 安装

```
sudo apt install keepass2  # 安装本体
sudo apt install keepass2-plugin-keepasshttp  # 安装http拓展
```



### 解决中文乱码

修改脚本`/usr/bin/keepass2`，使其在启动前先加载语言集。添加以下内容

```
export LANG=zh_CN.utf8
```



修改系统字体设置，在文件`/etc/fonts/conf.avail/65-nonlatin.conf`中，添加以下内容

```
<alias>
	<family>Ubuntu</family>
	<prefer>
		<family>sans-serif</family>
	</prefer>
</alias>
```

重启keepass2即可
