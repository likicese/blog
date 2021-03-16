# tcp wrappers

## 简介

该工具工作在第七层：应用层。

查看命令

``` bash
man hosts_access
man hosts_options
```

检查配置思路：收到客户端请求后，先去检查/etc/hosts.allow是否有该ip存在，有则接受，无则去匹配/etc/hosts.deny。

若/etc/hosts.deny中有ip存在，则拒绝；否则，接受。

## 例子

只允许192.168.1.0/24访问本机的sshd服务

```
# /etc/hosts.allow

sshd:192.168.1.0/24
```

```
# /etc/hosts.deny

sshd:ALL
```

