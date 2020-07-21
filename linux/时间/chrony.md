# chrony

## 安装

``` bash
yum install chrony -y
systemctl restart chronyd
systemctl enable chronyd  # 开机启动
systemctl status chronyd
```

## 操作

``` bash
chronyc -a makestep  # 立即同步时间
chronyc sourcestats -v  # ntp源服务器状态
chronyc sources -v  # 查看时间同步源状态
chronyc tracking  # 校准时间服务器
```

