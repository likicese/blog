# dsystemd

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

参考配置文件

```bash
useradd e-job -M -s /bin/false  # 创建一个名为e-job的用户，不允许登录和无家目录
```



```
[Unit]
Description=job
After=syslog.target

[Service]
User=e-job
Group=e-job
Environment=JAVA_HOME=/usr/java/default
WorkingDirectory=/opt/job
ExecStartPre=/usr/bin/chown -R e-job:e-job /opt/job
PermissionsStartOnly=true
ExecStart=/usr/java/default/bin/java -Xms512m -Xmx3096m -jar /opt/job/job.jar
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```

