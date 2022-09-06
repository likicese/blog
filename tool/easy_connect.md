# easy connect in ubuntu

## Harfbuzz version too old (1.3.1)

参考链接：[Ubuntu 20.04下EasyConnect兼容性问题临时解决方案 - HelloGrub - 博客园 (cnblogs.com)](https://www.cnblogs.com/cocode/p/12890684.html)

### 问题原因

electron框架版本太老

### 解决办法

将相关的so库解压到easyconnect同目录下

下载网址：https://packages.ubuntu.com/eoan/libpango-1.0-0

命令：

```bash
# 获取
wget http://security.ubuntu.com/ubuntu/pool/main/p/pango1.0/libpango-1.0-0_1.40.14-1ubuntu0.1_amd64.deb
wget http://security.ubuntu.com/ubuntu/pool/main/p/pango1.0/libpangocairo-1.0-0_1.40.14-1ubuntu0.1_amd64.deb
wget http://security.ubuntu.com/ubuntu/pool/main/p/pango1.0/libpangoft2-1.0-0_1.40.14-1ubuntu0.1_amd64.deb

# 解压
dpkg -X libpango-1.0-0_1.40.14-1ubuntu0.1_amd64.deb ./
dpkg -X libpangocairo-1.0-0_1.40.14-1ubuntu0.1_amd64.deb ./
dpkg -X libpangoft2-1.0-0_1.40.14-1ubuntu0.1_amd64.deb ./

# 移动
cd ./usr/lib/x86_64-linux-gnu/
mv ./libpango* /usr/share/sangfor/EasyConnect
```

此时，可以使用easy connect.

## 流量转发

### 目标

将ubuntu作为路由器，转发前往easy connect的流量

192.168.1.2 为ubuntu的ip
192.168.1.1 为windows的ip

### 操作

运行ubuntu的机器：

```bash
iptables -t nat -A POSTROUTING -o tun0 -j MASQUERADE
```

windows（以管理员身份）：

```bat
route add 10.0.1.0 mask 255.255.255.0 192.168.1.2  # 将前往10.0.1.0/24的流量全部转发给192.168.1.2
```

linux

```
route add -net 10.144.22.0 netmask 255.255.255.0 gw 172.16.180.4
```

## windows打开登录界面

安装启动vcxsrv，允许该应用通过防火墙

```bash
# 用ssh登录服务器，先执行以下语句，定位当打开图形界面的时候，该用哪个端口
export DISPLAY=192.168.1.1:0.0

# 执行以下语句，打开图形界面
firefox
```