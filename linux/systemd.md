# systemd

## 配置文件
 
配置文件用 `.service` 后缀名结尾，示例如下

``` shell
[Unit]
After=network-online.target

[Service]
Type=idle
User=testuser  # 启动该服务的用户
ExecStart=/tmp/test-service  # 运行服务的命令
TimeoutSec=60s

[Install]
WantedBy=multi-user.target
```