# ip

## ip address （网络层信息）

``` bash
ip address show  # 显示全部网卡
ip address show eth0  # 显示名为“eth0”的网卡信息
ip address add 192.168.1.10/24 eth0  # 给eth0网卡添加一个IP地址
ip address del 192.168.1.10/24 eth0  # 给eth0网卡删除一个IP地址
ip address flush dev eth0  # 清空eth0网卡所有的IP地址
```

## ip route

``` bash
ip route show  # 显示全部的路由表
ip route show dev eth0  # 查看该接口的路由

ip route change default dev eth0 src 192.168.1.2  # 修改原来的默认路由 。 注意，原来路由为 via 192.168.1.1  意为走网关。该修改生效后，可能数据包找不到网关
ip route add to 192.168.2.3/32 dev eth0 src 192.168.1.2  # 添加一条前往192.168.2.3的路由表。从192.168.1.2口出去
```

## ip link （链路层信息）

``` bash
ip link set eth0 up  # 启用网卡,不会配置路由。ifup eth0启用网卡的同时会配置默认路由
ip link set eth0 down  # 禁用网卡
ip link set dev eth0 name new_name  # 重命名接口
```

## ip rule

## ip addrlable