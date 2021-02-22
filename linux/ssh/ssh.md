# ssh

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

