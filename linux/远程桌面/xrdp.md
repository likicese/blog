# xdrp

## 系统环境

系统：centos7

## 安装

``` bash
yum install -y epel-release  # 先安装拓展源
yum install xrdp -y
systemctl start xrdp  # 启动
systemctl enable xrdp  # 设置开机启动
```

## 配置文件

配置文件为 `/etc/xrdp/xrdp.ini` ，建议修改其监听端口