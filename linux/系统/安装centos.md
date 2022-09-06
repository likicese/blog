# 安装centos

## 前言

系统：

[centos7.9](http://iso.mirrors.ustc.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso)

## 刻录安装U盘

可选软盘通或[rufus](https://rufus.ie)，推荐rufus

## 设置bios

插入刻好的U盘，启动电脑，进入bios，修改启动顺序，将U盘设为默认启动。

然后启动电脑，进入安装程序

## 分区

可以选择centos的默认设置，也可以选择`custom`，手动分区。

建议分区：

1. /boot/  512MiB
2. /boot/efi  256MiB
3. /  剩余全部大小或按需分配



注意，若bios设为UEFI模式启动，则必须分配/boot/efi分区，否则会报错。

## 编译网卡驱动

注意U盘不要拔掉，从安装U盘里找需要的文件。

### 查找网卡型号

```
yum install pciutils
lspci | grep Eth
```

### 编译驱动

此处以编译`e1000e`驱动为例

``` bash
yum install -y kernel-headers kernel-devel gcc wget epel-release
yum install -y rpm-build
wget https://downloadmirror.intel.com/15817/eng/e1000e-3.8.4.tar.gz
rpmbuild -tb e1000e-3.8.4.tar.gz
```

生成包的位置：/root/rpmbuild/RPMS/x86_64/e1000e-3.8.4-1.x86_64.rpm

### 安装驱动

```bash
yum install /root/rpmbuild/RPMS/x86_64/e1000e-3.8.4-1.x86_64.rpm
modprobe e1000e  # 加载驱动
```

## 网卡设置

### 手动设置静态IP

查看网卡UUID

```bash
nmcli con show
```

文件路径：/etc/sysconfig/network-scripts/ifcfg-xxxx

后边的“xxxx”为网卡名，编辑或创建该文件，插入以下内容

``` cfg
TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="static"         # 使用静态IP地址，默认为dhcp
IPADDR="192.168.1.2"   # 设置的静态IP地址
NETMASK="255.255.255.0"    # 子网掩码
GATEWAY="192.168.1.1"    # 网关地址
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

重启网卡：

```bash
systemctl restart network
```

## 命令设置

```bash
# 若没有连接，则需新建连接
nmcli con add con-name eth0 ifname eth0 type ethernet autoconnect yes

# 确定网络情况，设置静态ip或动态ip。以下命令择一执行。
nmcli con modify eth0 ipv4.address 192.168.1.10/24 ipv4.gateway 192.168.1.1 ipv4.method manual  # 设置静态ip
nmcli con modify eth0 ipv4.method auto  # 设置动态IP

# 启动连接
nmcli con up eth0
```

## 其他设置

```bash
sed -i 's/^ *SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config  # 禁用selinux

# 历史命令设置（最大条数、退出shell保存记录、显示历史记录的格式）
sed -i 's/HISTSIZE=1000/HISTSIZE=10000/g' /etc/profile
cat >> /etc/profile << EOF
shopt -s histappend
export HISTTIMEFORMAT="%F %T "
EOF
```

## 报错

### kernel和kernel-devel版本不匹配

``` eorro
common.mk:85: *** Kernel header files not in any of the expected locations.
common.mk:86: *** Install the appropriate kernel development package, e.g.
common.mk:87: *** kernel-devel, for building kernel modules and try again.  Stop.
```

1. kernel-header的版本不匹配，去centos的历史包中下载对应当前的内核版本的rpm安装包

[下载连接](https://vault.centos.org/7.5.1804/updates/x86_64/Packages/)

2. 没找到相应的文件，做软连接

以下载[kernel-devel](https://vault.centos.org/7.5.1804/updates/x86_64/Packages/kernel-devel-3.10.0-862.11.6.el7.x86_64.rpm)和[kernel-header](https://vault.centos.org/7.5.1804/updates/x86_64/Packages/kernel-headers-3.10.0-862.11.6.el7.x86_64.rpm)为例

``` bash
cd /usr/src/kernels/
ln -s 3.10.0-862.11.6.el7.x86_64/ 3.10.0-862.el7.x86_64
```

解决后，编译时会报几个warning，无伤大雅。

3. 内核寻找有问题，升级最新kernel。此方法非万不得已，不建议使用

``` bash
yum install -y kernel
```


### UEFI模式下，找不到启动文件

报错：

> dracut-initqueue : Warning: dracut-initqueue timeout - starting timeout scripts



解决：

在错误提示页面，按 `ESC` 退出。在命令行中输入 `ls /dev/` 寻找自己的盘符。会出现sdaX、hdbX之类的。我的是sda和sda4。

然后输入 `reboot` 重启 

在 `install Centos` 页面，按 `e` 进入修改启动文件路径模式。将

> vmlinuz initrd=initrd.img inst.stage2=hd:LABEL=CentOS\x207\x20x86_64.check quiet

修改为。最后的盘符是否是sda4每个人情况不同。

> vmlinuz initrd=initrd.img inst.stage2=hd:/dev/sda4 quiet

修改后，按 `ctrl + x` 组合键继续安装cnetos

### UEFI模式下，磁盘空间分配有问题

解决：

选择以下两种方法之一：

1. 修改BIOS，改为传统模式启动。不要用UEFI

2. 设定`/boot/efi`分区


### bios中开启安全模式，禁止加载第三方驱动

执行`modprobe e1000e`报错如下

``` eorro
modprobe: ERROR: could not insert 'e1000e': Required key not available
```



解决：

去bios中将安全模式关闭

### 网卡驱动开机无法正确加载

原因：

内核版本太老



解决：

更新内核版本

## 整盘拷贝

``` bash
dd if=/dev/zero of=/root/test.txt bs=1G count=100  # 测试硬盘速度

dd if=/dev/nvme0n1 of=/dev/nvme1n1  # 将/dev/nvme0n1的文件拷入/dev/nvme1n1
watch -n 5 pkill -USR1 ^dd$  # 查看复制进度
```