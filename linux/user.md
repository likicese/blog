# user

## 添加用户

| 用户类型 | UID范围 | 备注 |
| ------| ------: | :----: |
| 管理员 | 0 | 无 |
| 系统用户 | 1 ~ 999 | 无 |
| 一般用户 | 1000 ~ 系统支持的范围 | 无 |

``` shell
useradd -r <userName>  # 创建系统用户，此时不会在/home文件夹下创建用户文件夹
useradd -M <userName>  # 创建普通用户，不在/home文件夹下创建用户文件夹
usermod -G <groupName> <userName>  # 用户添加有效用户组。即用户加入其他组。
```

## 添加公钥

编辑对应用户文件 `用户家目录/.ssh/authorized_keys` ，一行一个公钥。

该文件权限应设定为 `-rw-r--r--` ,即 `644`。

``` bash
chmod 644 ~/.ssh/authorized_keys  # 修改当前用户的公钥文件
```