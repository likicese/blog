# iptables

## 简介

iptables工作在第三层（网络层）、第四层（传输层）

按规则顺序依次匹配

## 四表五链

### 四表

filter:过滤功能、防火墙

nat：网络地址转换

mangle：报文的拆、改、重装

raw：关闭nat表的连接追踪机制

### 五链

input、output、forward、prerouting、postrouting

## 对数据包的处理

ACCEPT 允许

DROP 丢弃

REJECT 拒绝，会回应一个响应

REDIRECT 重定向、映射、透明代理

SNAT 源地址转换

DNAT 目标地址转换

MASQUERADE 用于nat

LOG 先在/var/log/messages文件记录日志信息，再将包传递给下一条规则

## 参数

-A 向规则链中添加

-D 从规则链中删除

-I 指定链中插入一条新规则，默认首行

-R 修改、替换指定链的某条规则，按序号或内容替换

-L 列出指定链的规则

-E 重命名自定义链

-N 新增一条自定义规则链

-F 清空

-X 删除自定义规则链

-Z 将所有表的所有链字节和数据包计数器清零

-P 设置指定链的默认策略

-n 数字化输出结果

-v 查看规则表详情

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

iptables -A INPUT -i lo -j ACCEPT  # 允许环回访问
```

## 开机重载iptables

``` bash
iptables -A INPUT -p tcp --dport 80 -j REJECT  # 拒绝所有的主机访问80端口，策略例子
iptables-save > /etc/sysconfig/iptables-save  # 将策略保存到文件中。每次更改iptables策略后，都需要执行这条语句更新一次

echo 'iptables-restore < /etc/sysconfig/iptables-save' >> /etc/rc.d/rc.local  # 设置开机自动加载策略，仅执行一次即可
```

## 网络转换记录

```bash
cat /proc/net/nf_conntrack
```



## 例子

### 仅允许192.168.1.0/24的流量访问80端口

以下语句将会写入2条规则。一句允许，一句拒绝。

由于iptables按序匹配的特点，允许语句需在拒绝语句之前执行。

若想将规则顺序提前，则需要使用`-I` （从头部插入）替换`-A`（）从尾部插入参数。

```bash
iptables -A INPUT -s 192.168.1.0/24 -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j REJECT
```

### 做DNAT

```bash
# 将发往192.168.1.101:5022的数据包做DNAT，发给192.168.1.100:22。连接192.168.1.101:5022如同连接192.168.1.100:22。回包的时候，自动做SNAT
iptables -t nat -A OUTPUT -p tcp -d 192.168.1.101 --dport 5022 -j DNAT --to-destination 192.168.1.100:22
```

