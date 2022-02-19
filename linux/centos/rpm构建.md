# rpm构建

## 前言

promtail需要在多台机器上安装，希望使用systemd管理。没有成型的rpm包，只能自己构建

参考：

[%file指令 (rpm.org)](http://ftp.rpm.org/max-rpm/s1-rpm-inside-files-list-directives.html)

## 步骤

安装所需工具

```bash
 yum install -y rpmdevtools
```

创建rpm构建根目录

```bash
rpmdev-setuptree
```

生成的目录如下

```
~/rpmbuild/SOURCES              #放置打包资源，包括源码打包文件和补丁文件等
~/rpmbuild/SPECS                #放置SPEC文档
~/rpmbuild/BUILD                #打包过程中的工作目录
~/rpmbuild/RPMS                 #存放生成的二进制包
~/rpmbuild/SRPMS                #存放生成的源码包
```

## spec文件

文件路径 SPECS/promtail.spec

```
Name: promtail
Version: 2.4.2
Release: 1%{?dist}
Summary: watch local log to loki

Group: loki
License: AGPL-3.0 License
URL: https://github.com/grafana/loki
Source0: https://github.com/grafana/loki

%description

Promtail is an agent which ships the contents of local logs to a private Grafana Loki instance or Grafana Cloud. It is usually deployed to every machine that has applications needed to be monitored.

%prep

%install
cp -r %{_sourcedir}/target/* %{buildroot}/

%files
%{_prefix}/lib/systemd/system/promtail.service
%{_prefix}/local/promtail/promtail
%config %{_sysconfdir}/promtail/promtail.yaml  # 表明此为配置文件，升级时不应该删除
%{_localstatedir}/lib/promtail/

%postun

%changelog
* Sat Jan 1 2022 likicese likicese@gmail.com
- package the program to rpm
```

## 目录结构

```
.
├── BUILD
├── RPMS
├── SOURCES
│   └── target
│       ├── etc
│       │   └── promtail
│       │       └── promtail.yaml
│       ├── usr
│       │   ├── lib
│       │   │   └── systemd
│       │   │       └── system
│       │   │           └── promtail.service
│       │   └── local
│       │       └── promtail
│       │           └── promtail
│       └── var
│           └── lib
│               └── promtail
├── SPECS
│   └── promtail.spec
└── SRPMS
```

## 其他文件内容

SOURCES/target/etc/promtail/promtail.yaml

pipeline_stages块是为了增强正则获取日志文件的能力，可以去掉

```
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /var/lib/promtail/positions.yaml

client:
  url: http://loki.xxx.com:3100/api/prom/push

scrape_configs:
- job_name: system
  static_configs:
  - targets:
     - localhost
    labels:
     ip: ${IP}
     hostname: ${HOSTNAME}
     __path__: /var/log/*.log
  pipeline_stages:
    - match:
        selector: '{job="system"}'
        stages:
        - regex:
           source: filename
           expression: "/var/.*/"
        - labels:
             service:
```



SOURCES/target/usr/lib/systemd/system/promtail.service

ExecStartPre是为了获取环境变量，可以去掉

```
[Unit]
Description= promtail
After=syslog.target network.target remote-fs.target

[Service]
Restart=on-failure
RestartSec=300s

WorkingDirectory=/var/lib/promtail/
ExecStartPre=/bin/bash -c "/bin/systemctl set-environment HOSTNAME=$(/bin/cat /etc/hostname) IP=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)"
ExecStart=/usr/local/promtail/promtail -config.file=/etc/promtail/promtail.yaml -config.expand-env

[Install]
WantedBy=multi-user.target
```



可执行文件：SOURCES/target/usr/local/promtail/promtail

## 打包及检查

```
rpmbuild -bb ~/rpmbuild/SPECS/promtail.spec  # 打包
rpm -qpl ~/rpmbuild/RPMS/x86_64/promtail-2.4.2-1.el7.x86_64.rpm  # 检查包含的文件
rpm -ivh ~/rpmbuild/RPMS/x86_64/promtail-2.4.2-1.el7.x86_64.rpm  # 安装
rpm -e promtail  # 卸载
```

## 报错解决

### 安装rpm，报告依赖冲突

报错：/usr/lib from install of  conflicts with file from package filesystem

原因：%file段，直接指定整个文件夹，造成要安装程序要创建/usr/lib/文件夹的情况，导致报错

解决：不要指定宽泛的文件夹，直接指定具体文件

