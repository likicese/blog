# 自定义监控key

## 问题

192.168.1.2 ssh连接192.168.1.3不稳定。

断开时需要报警。

## 目标

zabbix-server 每隔30s查询 zabbix-agent 的自定义key值。非0值则触发报警

具体为：监控ssh端口22。

## 在zabbix-agent

新增 /ect/zabbix/shell/ssh_test.sh，内容如下

``` txt
#/bin/bash

# 尝试连接，10秒连不上则视为失败。
ssh 192.168.1.3 -p 22  -o ConnectTimeout=10 "ls ~/anaconda-ks.cfg" > /dev/null ; echo $?
```

编辑 /etc/zabbix/zabbix_agentd.d/ssh_test.conf，内容如下

``` txt
UserParameter=ssh_test,sudo /etc/zabbix/shell/ssh_62200_test.sh
```

因为脚本执行时，是以zabbix身份执行的，而使用root公钥，所以需要sudo。

故而修改文件属性。

``` bash
chown zabbix.zabbix /etc/zabbix/shell/ssh_62200_test.sh
chmod u+x /etc/zabbix/shell/ssh_62200_test.sh
```

添加sudo

执行 `visudo`，添加 `zabbix  ALL=(ALL)       NOPASSWD:/etc/zabbix/shell/ssh_62200_test.sh`

### 重启zabbix-agent

``` bash
systemctl restart zabbix-agent
```

## 在zabbix-server

### 测试key是否正常获取

返回0则说明一切正常

``` bash
zabbix_get -s 192.168.1.2 -k ssh_test
```

## 在zabbix-web

### 创建监控项

配置 -> 主机 -> （选择主机） -> 监控项 -> 创建监控项

在键值一栏，填入`ssh_test`

根据自身需求填写其他信息

### 创建图形

选择图形，然后添加刚刚创建的监控项

### 创建触发器

表达式为：`{192.168.1.2:ssh_test.last()}<>0`

意为返回值非0时报警