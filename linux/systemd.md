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
ExecStop=/bin/kill -s QUIT $MAINPID  # 杀掉进程时执行的命令
Restart=always  # 总是重启。设为on-failure则仅仅异常退出时会重启
TimeoutSec=60s  # 最长启动时间。超时后，首次发送SIGTERM信号，再超相同时长则发送SIGKILL信号

[Install]
WantedBy=multi-user.target
```