# iptables

## 四表五链

四表：filter、nat、mangle、raw

五链：input、output、forward、prerouting、postrouting

# 命令

``` bash
iptables -nL  # 查看防火墙规则
iptable -t filter -F  # 清空filter表规则

# 清除已有的规则
iptables -F
iptables -X
iptables -Z
```