# X11vnc

## 安装

``` bash
yum install -y x11vnc
```

## 设置密码

``` bash
cd ~
x11vnc -storepasswd
mv ~/.vnc/passwd /etc/x11vnc.pwd
```

## 设置启动文件

``` bash
vim /etc/systemd/system/x11vnc.service
```

启动文件内容入下

``` txt
[Unit]
Description=Remote desktop service (x11VNC)
Requires=display-manager.service
After=display-manager.service

[Service]
Type=forking
ExecStart=/usr/bin/x11vnc -display :0 -forever -shared -bg -rfbauth /etc/x11vnc.pwd -o /var/log/x11vnc.log
ExecStop=/usr/bin/killall x11vnc
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

## 启动

```bash
systemctl daemon-reload
systemctl enable x11vnc.service
systemctl start x11vnc.service
```

其监听的端口为`5900`