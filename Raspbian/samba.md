# samba

## 环境

硬件环境：树莓派3B+  
系统环境：2019-07-10-raspbian-buster

##　安装

### 一、安装服务

``` sh
su sudo  # 登入root身份，避免后边一长串的sudo

apt install samba -y  #　安装samba服务
```

### 二、配置

编辑samba配置文件：`/etc/samba/smb.conf`，在底部加入如下内容

```conf
[share]
comment = share folder
browseable = yes
path = /srv/share  # 共享的文件目录
create mask = 0700
directory mask = 0700
valid users = samba1
force user = samba1
force group = samba1
public = yes
available = yes
writable = yes
```

其中`samba`是用户名。可以根据自己情况，随意修改。

### 三、添加用户

```bash
useradd samba1  # 添加samba1用户
smbpasswd -a samba1  # 将samba1用户添加到smb管理中。此处会让你输入密码，即smb的登录密码
```

### 四、启动服务

```
systemctl status smb  # 启动服务
```

