# tigervnc

``` bash
yum install -y tigervnc-server
```

## 创建启动文件

复制启动文件

``` bash
cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:1.service
```

打开复制的文件，修改 `<USER>` ，将其改为要登陆的用户名

设置登陆密码

``` bash
su admin  # 切换到要登陆的用户名下，此处以admin为例
vncpasswd  # 设置vnc登陆密码
```

启动

``` bash
systemctl daemon-reload
systemctl restart vncserver@\:1.service
systemctl enable vncserver@\:1.service
```

监听的端口应该是590X。例如 5901 、 5902 等

若是无法访问，请检查防火墙是否打开