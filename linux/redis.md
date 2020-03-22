# redis

## 简单操作

``` bash
redis-cli -a passWord -h 192.168.1.1 -p 8379  # 登录 redis

# 在新进入的终端中，执行以下操作
keys *pa*  # 通配符
get *pa*  # 通配符
del *keys*

redis-cli -a passWord keys "KEY_*" | xargs redis-cli -a passWord del  # 批量删除keys
```