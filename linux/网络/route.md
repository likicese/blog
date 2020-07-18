# route

## 例子

``` bash
route -n  # 查看路由表
route del -net 192.168.0.0 netmask 255.255.0.0 dev eth0  # 删除前往192.168.0.0/16的路由
route add -net 10.10.0.0 netmask 255.255.0.0 gw 10.11.1.1  # 将前往10.10.0.0/16网段的流量朝10.11.1.1网关导去
```