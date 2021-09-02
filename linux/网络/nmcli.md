# nmcli

## 命令

``` bash
nmcli con show  # 查看网卡映射情况
nmcli con show eth0  # 查看name为eth0的网卡详细信息
nmcli device show  # 查看设备连接状态


# 设置静态IP和DNS
nmcli con modify eth0 ipv4.method manual ipv4.addresses 192.168.1.2
nmcli con modify eth0 ipv4.dns 8.8.8.8
nmcli con up eth0  # 修改后重载才能生效

# 设置dhcp
nmcli con modify eth0 ipv4.method auto

nmcli con down eth0  # 停用网络连接
nmcli device disconnect eth0  # 禁用网卡
```

## 例子

### 设置静态IP

``` bash
nmcli con modify eth0 ipv4.addresses 192.168.1.230/24
nmcli con modify eth0 ipv4.gateway 192.168.1.1
nmcli con modify eth0 ipv4.method manual
nmcli con modify eth0 ipv4.dns 8.8.8.8
nmcli con modify eth0 +ipv4.dns 114.114.114.114
nmcli con modify eht0 ipv4.route-metric 99  # 指定网卡优先级。一般有线网卡是100，无线网卡为600。此处设定无线网卡优先
nmcli con up eth0  # 修改后重载才能生效
```

### 添加一个连接

```bash
nmcli con add con-name con-eth0 ifname eth0 type ethernet autoconnect yes  # 添加一个名为con-eth0，使用eth0的网卡，自动连接
nmcli con modify con-eth0 ipv4.address 192.168.1.2/24 ipv4.gateway 192.168.1.1 ipv4.method manual  # 配置
nmcli con up con-eth0  # 启动生效。
```

