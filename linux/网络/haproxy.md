# haproxy

## 简述

该软件能承担一个转发的作用。双方可以是非对等的

## 安装

``` bash
yum install centos-release-scl  # 安装源
yum install rh-haproxy18  # 安装
systemctl restart rh-haproxy18-haproxy.service  # 启动
```

## 配置文件

重点在后边的部分

配置文件：/etc/opt/rh/rh-haproxy18/haproxy/haproxy.cfg

``` txt
frontend test_name
  bind *:12222
  mode http
  default_backend test_name_server
  acl white_list src 192.168.2.0/24  # 只允许该网段的IP通过
  tcp-request content reject if ! white_list

backend test_name_server
  mode http
  balance roundrobin
  option log-health-checks
  default-server inter 10s fall 2
  stick-table type ip size 200k expire 30m
  stick on src
  server ser1 10.0.0.52:8080 check  # 远端服务器
```