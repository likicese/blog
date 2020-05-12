# zabbix安装

## zabbix简介

[zabbix](https://www.zabbix.com/)，用于实现监控线上服务运行状况的监控软件。  

zabbix-sever：服务端，接受agent等监控源传来的信息，并组织信息
zabbix-get：布在服务端。用于测试是否能从agent端获取到信息

zabbix-web：用于展示server端得出的统计信息。可以和zabbix-server不在一台主机上

zabbix-agent：布在被监控的主机上，利用各种方案获取主机信息，传给服务端。传递给服务端时有主动和被动两种模式。
zabbix-sender：布在被监控的主机上，用于测试能否主动向服务端推送信息

zabbix-proxy：可选组件。类似zabbix-server，先收集agent端传来的信息，再统一发送给服务端

## 系统环境

linux版本：`centos7.6`（最小安装的版本）  
zabbix版本：`4.0 x86_64`

## 配置zabbix的官方yum源

[yum源官网地址](http://repo.zabbix.com/) ,  根据自己需要进行选取

在文件夹/etc/yum.repo.d/下，新增文件zabbix.repo

``` shell
[root@localhost ~]# cd /etc/yum.repos.d/
[root@localhost yum.repos.d]# vi zabbix.repo
```

文件中写入如下内容：

> [zabbix]  
> name=zabbix  
> baseurl=<http://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/>  
> gpgcheck=0  
> enabled=1  

清除缓存并重建缓存

``` shell
[root@localhost ~]# yum clean all
[root@localhost yum.repos.d]# yum makecache
```

检查配置是否成功

``` shell
[root@localhost yum.repos.d]# yum repolist all | grep enabled
base/7/x86_64                   CentOS-7 - Base                  enabled: 10,019
extras/7/x86_64                 CentOS-7 - Extras                enabled:    385
updates/7/x86_64                CentOS-7 - Updates               enabled:  1,493
zabbix                          zabbix                           enabled:     93
```

## 安装mysql

[安装mysql教程](/数据库/mysql/Centos7.6安装Mysql.md)  
mysql用于记录zabbix用户名、密码等内容

## 安装zabbix-server

``` shell

```

## 错误修正

### 1. 缺失`fping`

* 错误提示

``` shell
Error: Package: zabbix-server-mysql-4.0.6-1.el7.x86_64 (zabbix)
           Requires: fping
```

* 解决方法  
  安装epel扩展包；更新yum源；安装`fping`

``` shell
[root@localhost ~]# yum list | grep epel
epel-release.noarch                        7-11                        extras
[root@localhost ~]# yum install epel-release
[root@localhost ~]# yum makecache
[root@localhost ~]# yum install fping
```

### 2. 缺失`libiksemel.so`

* 错误提示

``` shell
Error: Package: zabbix-server-mysql-4.0.6-1.el7.x86_64 (zabbix)
           Requires: libiksemel.so.3()(64bit)
```

* 解决方法  
  根据自己系统版本，去centos相关的软件包网站下载软件包。  
  教程所用系统对应网址：<https://centos.pkgs.org/7/puias-unsupported-x86_64/iksemel-1.4-6.sdl7.x86_64.rpm.html>

``` shell
[root@localhost ~]# wget http://springdale.math.ias.edu/data/puias/unsupported/7/x86_64//iksemel-1.4-6.sdl7.x86_64.rpm
```

### 3. 缺失`libgnutls.so`

* 错误提示

``` shell
error: Failed dependencies:
    libgnutls.so.28()(64bit) is needed by iksemel-1.4-6.sdl7.x86_64
```

* 解决方法  
  根据自己系统版本，去centos相关的软件包网站下载软件包。  
  教程所用系统对应网址：<https://centos.pkgs.org/7/centos-updates-x86_64/gnutls-dane-3.3.29-9.el7_6.x86_64.rpm.html>

``` shell
[root@localhost ~]# wget http://mirror.centos.org/centos/7/updates/x86_64/Packages/gnutls-dane-3.3.29-9.el7_6.x86_64.rpm
```
