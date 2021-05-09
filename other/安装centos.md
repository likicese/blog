# 安装centos

## 1. 软碟通刻盘

## 2. bios设置

修改启动顺序，将U盘设为默认启动

## 3. UEFI模式下，找不到启动文件

### 1. 报错提示

> dracut-initqueue : Warning: dracut-initqueue timeout - starting timeout scripts

### 2. 解决方法

在错误提示页面，按 `ESC` 退出。在命令行中输入 `ls /dev/` 寻找自己的盘符。会出现sdaX、hdbX之类的。我的是sda和sda4。

然后输入 `reboot` 重启 

在 `install Centos` 页面，按 `e` 进入修改启动文件路径模式。将

> vmlinuz initrd=initrd.img inst.stage2=hd:LABEL=CentOS\x207\x20x86_64.check quiet

修改为。最后的盘符是否是sda4每个人情况不同。

> vmlinuz initrd=initrd.img inst.stage2=hd:/dev/sda4 quiet

修改后，按 `ctrl + x` 组合键继续安装cnetos

## 4. UEFI模式下，磁盘空间分配有问题

### 1.解决办法

修改BIOS，改为传统模式。不要用UEFI

## 5. 网卡型号查找

安装：yum install pciutils

使用：lspci | grep Eth

## 6. 驱动编译问题

安装gcc、kernel-headers、kernel-devel

切目录

> cd e10001-x.x.x/src

安装

> make install

加载模块

> modprobe e1000e

## 7. 网卡驱动开机无法正确加载

### 1. 问题原因

内核版本太老

### 2. 问题解决

更新内核

## 8. 静态网卡设置

查看网卡UUID

> nmcli con show

文件路径：/etc/sysconfig/network-scripts/ifcfg-xxxx

后边的“xxxx”为网卡名，编辑或创建该文件，插入以下内容

``` cfg
TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="static"         # 使用静态IP地址，默认为dhcp
IPADDR="192.168.1.2"   # 设置的静态IP地址
NETMASK="255.255.255.0"    # 子网掩码
GATEWAY="192.168.241.2"    # 网关地址
DNS1="8.8.8.8"
DNS2="8.8.8.8"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="eno2"
UUID="XXXXXXXXXXXXXXXXXXXXXXXX"
DEVICE="eno2"
ONBOOT="yes"             #是否开机启用
```

重启网卡命令：

> systemctl restart network

## 报错

### kernel和kernel-devel版本不匹配

``` eorro
common.mk:85: *** Kernel header files not in any of the expected locations.
common.mk:86: *** Install the appropriate kernel development package, e.g.
common.mk:87: *** kernel-devel, for building kernel modules and try again.  Stop.
```

内核寻找有问题。升级kernel即可

``` bash
yum install -y kernel
```
