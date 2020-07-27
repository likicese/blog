# ip

## ip address

``` bash
ip address show  # 显示全部网卡
ip address show eth0  # 显示名为“eth0”的网卡信息
ip address add 192.168.1.10/24 eth0  # 给eth0网卡添加一个IP地址
ip address del 192.168.1.10/24 eth0  # 给eth0网卡删除一个IP地址
```

## ip route

``` bash
ip route show  # 显示全部的路由表
```

## ip link

``` bash
ip link set eth0 up  # 启用网卡
ip link set eth0 down  # 禁用网卡
```

## ip rule

## addrlable