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
firewall-cmd --zone=public --remove-port=80/tcp --permanent  # 删除80端口
firewall-cmd --add-masquerade --permanent  # 开启端口转发

firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='192.168.1.2' accept"  # 添加一个IP为信任。IP段可用192.168.1.0/24\

firewall-cmd --get-active-zones  # 查看激活的域

firewall-cmd --add-forward-port=port=8081:proto=tcp:toport=80 #  将8081转发到80
```