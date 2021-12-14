# redis

## 主从

参考

[Redis主从复制(Master/Slave) 与哨兵模式 - 阳荣 - 博客园 (cnblogs.com)](https://www.cnblogs.com/itoyr/p/10069840.html)

## 简单操作

``` bash
redis-cli -a passWord -h 192.168.1.1 -p 8379  # 登录 redis

# 在新进入的终端中，执行以下操作
keys *pa*  # 通配符
get *pa*  # 通配符
del *keys*
info all  # 查询redis全部信息
info Replication  # 查询redis主从信息

redis-cli -a passWord keys "KEY_*" | xargs redis-cli -a passWord del  # 批量删除keys
```

## hashMap

```bash
hget abcd ppp  # 获取键值为abcd，属性值为ppp的值
hgetall abcd  # 获取键值为abcd的所有值
hdel abcd ppp  # 删除键值为abcd，属性值为ppp的值
```

## 命令

```bash
slaveof no one  # 在从库输入，取消从，变为主
```

