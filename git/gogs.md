# gogs

## 简介

用golang写就的git服务端，轻量！

支持mysql、sqlite3、postgresql数据库。

支持多种安装方式

[官网](https://gogs.io/)

## 安装

请直接参阅官网

## 设置监听地址

由于部署的机器是网关，http和ssh默认监听 0.0.0.0 比较危险。

故而寻找办法修改监听地址。

[参考资料](https://gitee.com/unknwon/gogs/blob/main/conf/app.ini)

通过查阅源码的配置文件可以发现，初始化后，gogs只提供很少的设置值在app.ini文件中。

更多的值会取源码配置文件的默认值。

则，我们可以通过添加配置值，达到修改监听地址的目的：

```init
HTTP_ADDR        = 192.168.1.10  ; http监听值
HTTP_PORT        = 48931
DISABLE_SSH      = false
SSH_LISTEN_HOST  = 192.168.1.10  ; ssh监听值
SSH_PORT         = 48930
START_SSH_SERVER = true  ; 开启ssh服务
```

