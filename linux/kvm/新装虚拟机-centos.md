# 新装虚拟机-centos

## 磁盘自定义

| 路径      | 大小     |
| --------- | -------- |
| /boot     | 512MiB   |
| /boot/efi | 256MiB   |
| /         | 剩余大小 |

## 设置网络

### 安装时预设置

在网线处填入静态IP地址、网关等信息即可

### 安装后设置

```bash
# 设置网卡
cat > /etc/sysconfig/network-scripts/ifcfg-eth0 << EOF
DEVICE=eth0
TYPE=Ethernet
ONBOOT=yes
BOOTPROTO="static"
IPADDR=192.168.1.10
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=223.5.5.5
DNS2=8.8.8.8
IPV6INIT=no
NAME=eth0
EOF

# 设置DNS
cat > /etc/resolv.conf << "EOF"
nameserver 223.5.5.5
nameserver 8.8.8.8
EOF

# 关闭且禁开机启动NetworkManager网络管理软件，若使用图形界面，此举会让wifi图标消失
systemctl disable NetworkManager
systemctl stop NetworkManager

# 启动network
systemctl enable network
systemctl restart network
```

## 常用设置

```bash
# 替换rpm源
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
curl http://mirrors.aliyun.com/repo/Centos-7.repo -o /etc/yum.repos.d/CentOS-Base.repo 
curl http://mirrors.aliyun.com/repo/epel-7.repo -o /etc/yum.repos.d/epel.repo 

sed -i '/mirrors.aliyuncs.com/d' /etc/yum.repos.d/*.repo
sed -i '/mirrors.cloud.aliyuncs.com/d' /etc/yum.repos.d/*.repo

yum clean all

# 时间同步和电源管理。acpid支持虚拟机软关机
yum install -y chrony; systemctl start chronyd; systemctl enable chronyd
yum install -y acpid; systemctl enable acpid

# 网络工具、拓展包、vim、命令补全，设置默认编辑器
yum install -y mtr net-tools epel-release vim bash-completion
echo 'export EDITOR=/usr/bin/vim' >> /etc/profile

# qemu监控
yum install qemu-guest-agent -y
systemctl enable qemu-guest-agent
sed -i 's/BLACKLIST_RPC/# BLACKLIST_RPC/' /etc/sysconfig/qemu-ga  # 令宿主机可以操作虚拟机的文件

# 禁止selinux
sed -i 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/sysconfig/selinux
sed -i 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/selinux/config

# 重制开机启动项
sed -i 's#GRUB_TIMEOUT=5#GRUB_TIMEOUT=3#g' /etc/default/grub
sed -i 's#rhgb quiet#console=tty0 console=ttyS0,115200n8#g' /etc/default/grub
grub2-mkconfig -o /boot/grub2/grub.cfg

# 设置历史信息记录、格式化显示
cat > /etc/profile.d/history.sh << EOF
shopt -s histappend
HISTTIMEFORMAT='%F %T '
HISTSIZE="100000"
HISTFILESIZE=100000
PROMPT_COMMAND='(umask 000; msg=\$(history 1 | { read x y; echo \$y; }); echo [\$(who am i | awk "{print \\\$(NF-2),\\\$(NF-1),\\\$NF}")] [\$(whoami)@\`pwd\`]" \$msg" >> /var/log/.history)'
export HISTTIMEFORMAT HISTSIZE HISTFILESIZE PROMPT_COMMAND
EOF

# 去除、关闭非必要的软件
yum remove libvirt-daemon* -y
yum remove dnsmasq -y
yum remove alsa-utils gssproxy -y
systemctl stop cups
systemctl disable cups
systemctl stop avahi-daemon.socket avahi-daemon.service
systemctl disable avahi-daemon.socket avahi-daemon.service
systemctl stop gssproxy
systemctl disable gssproxy
systemctl stop rpcbind.socket
systemctl disable rpcbind.socket
systemctl stop ksmtuned
systemctl disable ksmtuned
systemctl stop smartd
systemctl disable smartd
systemctl stop abrtd
systemctl disable abrtd
systemctl stop ModemManager
systemctl disable ModemManager
systemctl stop atd
systemctl disable atd
systemctl stop libstoragemgmt
systemctl disable libstoragemgmt
systemctl stop packagekit
systemctl disable packagekit

# 关闭非必要软件，即使mini安装也会存在的软件
systemctl stop postfix
systemctl disable postfix
systemctl stop firewalld  # 防火墙
systemctl disable firewalld
service auditd stop
systemctl disable auditd.service
systemctl stop tuned
systemctl disable tuned
```

## 服务器参数调优

```bash
cat >> /etc/security/limits.conf << EOF
*       soft    nofile  1048560
*       hard    nofile  1048560
*       soft    nproc   1048560
*       hard    nproc   1048560
EOF

sed -i "s/*          soft    nproc     4096/*          soft    nproc     1048560/g" /etc/security/limits.d/20-nproc.conf

cat >> /etc/sysctl.conf << EOF
net.core.somaxconn = 16384
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_syncookies= 1	# 打开TIME-WAIT套接字重用功能，对于存在大量连接的Web服务器非常有效
net.ipv4.tcp_tw_reuse= 1  # 减少处于FIN-WAIT-2连接状态的时间，使系统可以处理更多的连接
net.inet.udp.checksum = 1  # 防止不正确的udp包
EOF
```

## 安全设置

```bash
SSHD_CONFIG='/etc/ssh/sshd_config'
sed -i '/#PasswordAuthentication yes/d' ${SSHD_CONFIG}
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/g' ${SSHD_CONFIG}
sed -i 's/#UseDNS yes/UseDNS no/g' ${SSHD_CONFIG}
```

## 清理

分为两种情况

### 未开启trim

在虚拟机执行：

```bash
yum clean all
rm -rf /var/cache/yum
rm -rf /var/log/*
dd if=/dev/zero of=/boot/zero.file oflag=append conv=notrunc
dd if=/dev/zero of=/boot/efi/zero.file oflag=append conv=notrunc
dd if=/dev/zero of=~/zero.file oflag=append conv=notrunc
rm -f /boot/zero.file
rm -f /boot/efi/zero.file
rm -f ~/zero.file
history -c; history -w
rm -f ~/.bash_history

poweroff
```

### 开启trim

直接在虚拟机执行：

```bash
yum clean all
rm -rf /var/cache/yum
rm -rf /var/log/*
history -c; history -w
rm -f ~/.bash_history
fstrim -av
rm -f ~/.bash_history

poweroff
```