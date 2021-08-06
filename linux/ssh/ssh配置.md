# ssh配置

## 前言

参考文档：https://cherrot.com/tech/2017/01/08/ssh-tunneling-practice.html

确认本机安装了openssh

openssh版本低于7.3，则无法使用ProxyJump配置，只能使用ProxyCommand配置。请执行 `ssh -V` 检查本机版本

windows的powershell使用ProxyCommand配置时，ssh应指定绝对路径。以下命令可寻找ssh程序的绝对路径
``` powershell
Get-Command ssh
```

## 配置文件示例

执行 `vim ~/.ssh/config` ，以编辑配置文件。

``` config
# 网关服务器，最简单的配置
Host route
    Hostname 192.168.1.1
    user admin
    Port 22

# 堡垒机、跳板机。连入各种测试、生产服务器的时候，需要经过该台服务器
Host fort
    Hostname 10.0.0.1
    user go
    Port 5555

# 二级跳板
Host jump
    Hostname 10.2.0.1
    user jumpuser
    Port 22

# 测试环境某一台具体的服务器，通过跳板机进入
Host uat
    Hostname 10.1.0.2
    user root
    Port 22
    ProxyJump fort
    # ProxyCommand ssh fort -W %h:%p

# 生产环境的某一台具体服务器。先跳入fort，再跳入jump，最后才连接到该服务器
Host prod
    Hostname 10.2.0.2
    user admin
    Port 22
    ProxyJump fort, jump

# 通配符。这里和config文件的匹配规则有关。意为以上机器连接时，均使用本Host下的私钥文件
Host *
    IdentityFile ~/.ssh/id_rsa
```

执行 `chmod 700 ~/.ssh/config` 以保证该文件能被ssh顺利认权通过

## 使用

配置完以上文件后，可以执行以下命令使用

``` bash
ssh route  # 跳转到route服务器
ssh uat  # 跳转到uat服务器
```

## 不使用配置直接跳转

``` bash
# 10.1.0.2是目标机，10.1.0.1时跳板机
ssh root@10.1.0.2 -o ProxyCommand='ssh go@10.0.0.1 -p 5555 -W %h:%p'
```

## 强制使用密码连接ssh

```bash
ssh root@192.168.1.1 -o PasswordAuthentication=yes
ssh root@192.168.1.1 -o PreferredAuthentications=password -o PubkeyAuthentication=no
```

## 设置ssh流量转发

```bash
ssh -gNfD 127.0.0.1:1080 root@192.168.1.1  # 设置socket5代理，并且后台运行。去掉f参数则是前台运行。
```

## 批量禁止密码登陆

```
#!/bin/bash

for((i=1;i<=254;i++));
do
ssh 192.168.1.$i "sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config; systemctl restart sshd"
echo $i;
done
```