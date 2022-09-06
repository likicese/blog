# loki

## 报错解决

### 日志数量太多导致无法接收

报错：server returned HTTP status 429 Too Many Requests (429): Ingestion rate limit exceeded

解决：

```
config:
  limits_config:
    ingestion_rate_strategy: local
    # 每个用户每秒的采样率限制
    ingestion_rate_mb: 15
    # 每个用户允许的采样突发大小
    ingestion_burst_size_mb: 20
```

## 制作loki的rpm包

```bash
# 创建文件夹
mkdir -p SOURCES/target/etc/loki SOURCES/target/var/lib/loki/storage/chunks SOURCES/target/var/lib/loki/storage/rules SOURCES/target/usr/lib/systemd/system SRPMS BUILD RPMS SRPMS
```

### 结构与文件

结构

```
.
├── BUILD
├── BUILDROOT
├── RPMS
├── SOURCES
│   └── target
│       ├── etc
│       │   └── loki
│       │       └── loki.yaml
│       ├── usr
│       │   ├── lib
│       │   │   └── systemd
│       │   │       └── system
│       │   │           └── loki.service
│       │   └── local
│       │       └── loki
│       │           └── loki
│       └── var
│           └── lib
│               └── loki
│                   └── storage
│                       ├── chunks
│                       └── rules
├── SPECS
│   └── loki.spec
└── SRPMS
```



SPECS/loki.spec

```
Name: loki
Version: 2.5.0
Release: 1%{?dist}
Summary:  loki

Group: loki
License: AGPL-3.0 License
URL: https://github.com/grafana/loki
Source0: https://github.com/grafana/loki

%description

%pre
useradd -M --shell /bin/false loki

%install
cp -r %{_sourcedir}/target/* %{buildroot}/
systemctl daemon-reload

%files
%{_prefix}/lib/systemd/system/loki.service
%{_prefix}/local/loki/loki
%config %{_sysconfdir}/loki/loki.yaml
%{_localstatedir}/lib/loki/

%post
chown loki:loki -R /var/lib/loki

%preun
systemctl stop loki

%postun
userdel loki
rm -rf %{_sysconfdir}/loki/
# 删除数据
rm -rf %{_localstatedir}/lib/loki/
systemctl daemon-reload

%changelog
* Sat Apr 30 2022 likicese likicese@gmail.com
- package loki
```



SOURCES/target/usr/lib/systemd/system/loki.service

```
[Unit]
Description= loki
After=syslog.target network.target remote-fs.target nss-lookup.target

[Service]
User=loki
Group=loki
Restart=on-failure
RestartSec=300s

WorkingDirectory=/var/lib/loki/
ExecStart=/usr/local/loki/loki -config.file=/etc/loki/loki.yaml

[Install]
WantedBy=multi-user.target
```



SOURCES/target/etc/loki/loki.yaml

```
auth_enabled: false

server:
  http_listen_port: 3100
  grpc_listen_port: 9096

common:
  path_prefix: /var/lib/loki/storage
  storage:
    filesystem:
      chunks_directory: /var/lib/loki/storage/chunks
      rules_directory: /var/lib/loki/storage/rules
  replication_factor: 1
  ring:
    instance_addr: 127.0.0.1
    kvstore:
      store: inmemory

schema_config:
  configs:
    - from: 2020-10-24
      store: boltdb-shipper
      object_store: filesystem
      schema: v11
      index:
        prefix: index_
        period: 24h

limits_config:
    ingestion_rate_strategy: local
    # 每个用户每秒的采样率限制
    ingestion_rate_mb: 15
    # 每个用户允许的采样突发大小
    ingestion_burst_size_mb: 20

ruler:
  alertmanager_url: http://localhost:9093

table_manager:
  retention_deletes_enabled: true
  # 保存日志的天数。为168的倍数，1008是42天
  retention_period: 1008h
```

### 构建

```
rpmbuild -bb SPECS/loki.spec
```

