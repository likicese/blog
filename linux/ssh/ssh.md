# ssh

## ssh-server

### 保护ssh避免被非法IP访问

编辑文件`/etc/hosts.deny`，加入如下内容

```
# 拒绝来自192.168.1.0/24的IP段访问
sshd: 192.168.1.0/16: deny
```

## 无法在ssh中执行su命令

``` bash
ssh root@192.168.1.6 "su admin ; cd ~/"
```

以上指令无法执行。似乎ssh并不支持这种写法，会卡住。

## 生成公钥和私钥

```bash
ssh-keygen -t rsa -C 'zhansan@company.com'  # 生成公钥和私钥，且附带名字
```

## 配置公钥后ssh连接失败

报错：

```
Authentication refused: bad ownership or modes for directory /home/admin
```

原因：由于rsync操作失误，导致/home/admin的权限变为777，引发权限问题。原来只怀疑到~/.ssh文件夹的权限出问题，最终通过sshd的日志才准确定位。

修复：

```bash
chmod 700 /home/admin
```

## ssh连接机器太慢

排查：

用`ssh root@192.168.1.3 -v`可以发现，在如下显示停留最久

``` debug
debug1: Unspecified GSS failure.  Minor code may provide more information
No Kerberos credentials available (default cache: FILE:/tmp/krb5cc_0)
```

原因：

ssh连接机器的时候，会用如下方法验证顺序：publickey,gssapi-keyex,gssapi-with-mic,password

GSSAPI无法验证，直至超时。

解决：

在`/etc/ssh/ssh_config`添加如下配置

``` config
GSSAPIAuthentication no
```
