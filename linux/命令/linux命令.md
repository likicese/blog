# linux命令

## host

``` shell
hostnamectl set-hostname hostName  # 设置主机名
```

## 密码

随机密码
``` shell
DB_PASSWORD=`cat /dev/urandom | tr -dc A-Za-z0-9 | head -c 24`  # 生成随机密码
echo -e "\033[31m 你的数据库密码是 $DB_PASSWORD \033[0m"  # 打印出来
```

## 公私钥

``` shell
ssh-keygen  # 重新生成本机公钥和私钥
```