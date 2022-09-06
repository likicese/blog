# coredns

二进制部署

## 安装

[获取](https://github.com/coredns/coredns/releases)

启动文件：Corefile

```
(common) {
    log
    errors
    cache 120
    loop
    reload  # 每120秒检测配置文件，变动则重载
}
.:53 {
    import common
    forward . 223.5.5.5 114.114.114.114
}
dev.example.org {
    auto {
       directory db.dev.example.org  # 此处为文件名
       reload 60s
    }
    import common
}
```



域名解析文件：db.dev.example.org

```
$ORIGIN dev.example.org.
@       3600 IN SOA ns1.dev.example.org. liki.dev.example.org. 20220104 7200 3600 1209600 3600
        3600 IN NS ns1
        3600 IN NS ns2

www     IN A     192.168.1.5
        IN AAAA  ::1
ns1     IN NS    192.168.1.2
ns2     IN NS    192.168.1.3
```

SOA记录中，ns1.dev.example.org.指多条ns记录中，哪那一条作为主dns进行解析，liki.dev.example.org.为域名管理者邮箱，会被代换为liki@dev.example.org。若名字中含“.”，则用“\”符号代替。



systemd文件：

```systemd
[Unit]
Description=CoreDNS DNS server
Documentation=https://coredns.io
After=network.target

[Service]
User=coredns
Group=coredns
PermissionsStartOnly=true

ExecStartPre=/usr/bin/mkdir -p /opt/software/coredns/
ExecStartPre=/usr/bin/chown -R coredns.coredns /opt/software/coredns/
WorkingDirectory=/opt/software/coredns/

LimitNOFILE=1048576
LimitNPROC=512
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
AmbientCapabilities=CAP_NET_BIND_SERVICE
NoNewPrivileges=true
ExecStart=/opt/software/coredns/coredns
ExecReload=/bin/kill -SIGUSR1 $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## 测试

```bash
dig @192.168.1.2 www.dev.example.org  # coredns安装在192.168.1.2上
sed -i "1i nameserver 192.168.1.2" /etc/resolv.conf  # 更改DNS域名
```

## 踩坑记录

### reload指令无效

需要修改SOA才能生效。若比较着急，可以直接重启

### directory指令无效

对文件名似乎有要求，可能是要求db开头

### coredns已启动，无法解析域名

情况比较多。他的默认配置文件是工作路径下的Corefile，如果工作路径下，不存在该文件，也能启动，此时无法按照配置文件的要求解析域名。

