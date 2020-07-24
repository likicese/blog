# ip

## ip addr

``` bash
ip addr show  # 显示全部网卡
ip addr show eth0  # 显示名为“eth0”的网卡信息
ip addr add 192.168.1.10/24 eth0  # 给eth0网卡添加一个IP地址
ip addr del 192.168.1.10/24 eth0  # 给eth0网卡删除一个IP地址
```

## ip route

``` bash
ip route show  # 显示全部的路由表
```