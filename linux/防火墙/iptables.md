# iptables

## 四表五链

四表：filter、nat、mangle、raw

五链：input、output、forward、prerouting、postrouting

## 对数据包的处理

ACCEPT 允许

DROP 丢弃

REJECT 拒绝，会回应一个响应

REDIRECT 重定向、映射、透明代理

SNAT 源地址转换

DNAT 目标地址转换

MASQUERADE 用于nat

LOG 先在/var/log/messages文件记录日志信息，再将包传递给下一条规则

## 命令

``` bash
iptables -nL  # 查看防火墙规则
iptable -t filter -F  # 清空filter表规则

# 清除已有的规则
iptables -F
iptables -X
iptables -Z
```

``` bash
iptables -L INPUT --line-numbers  # 打印规则序号
iptables -D INPUT 6  # 删除一条规则，6为上一句打出的规则序号

iptables -A INPUT -s 192.168.1.4 -p all -j ACCEPT  # 开放所有端口给该IP地址

iptables -I INPUT -s 123.45.6.7 -j DROP  # 屏蔽一个IP
iptables -A INPUT -p tcp --dport 80 -j ACCEPT  # 允许访问80端口

iptables -A FORWARD -j REJECT  # 禁止未允许的规则访问
```