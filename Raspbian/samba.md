# samba

## 安装环境

硬件环境：树莓派3B+  
系统环境：2019-07-10-raspbian-buster

##　安装过程

### 一、安装服务

``` sh
su sudo  # 登入root身份，避免后边一长串的sudo

apt install samba -y  #　安装samba服务
vim /etc/samba/smb.conf  # 编辑samba配置文件，在底部加入如下内容
```

> 