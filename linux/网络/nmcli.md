# nmcli

``` bash
nmcli con show  # 查看网卡映射情况
nmcli con show eth0  # 查看name为eth0的网卡详细信息
nmcli device show  # 查看设备连接状态


# 设置静态IP和DNS
nmcli con modify eth0 ipv4.method manual ipv4.addresses 192.168.1.2
nmcli con modify eth0 ipv4.dns 8.8.8.8
nmcli con up eth0  # 修改后重载才能生效


nmcli con down eth0  # 停用网络连接
```