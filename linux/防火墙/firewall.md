# firewall

## 服务启动

``` shell
systemctl start firewalld  # 启动服务
```

| 命令 | 动作 |
|:----- | :----- |
| start | 启动服务 |
| stop | 停止服务 |
| restart | 重启服务 |
| status | 检查服务状态 |
| enable | 开启自启 |
| disable | 开机禁止服务 |
| is-enable | 检查是否开机自启 |

## 基本操作

``` shell
firewall-cmd --zone=public --add-port=80/tcp --permanent  # 添加80端口
firewall-cmd --reload  # 重启防火墙
```