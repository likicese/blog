# yum包

## chrony（时间同步工具）

```
yum install chrony -y
systemctl restart chronyd
systemctl enable chronyd
systemctl status chronyd

chronyc sourcestats -v  # ntp源服务器状态
chronyc sources -v  # 查看时间同步源状态

```

## debian系更改时区

``` bash
dpkg-reconfigure tzdata
```

