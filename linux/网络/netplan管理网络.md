# netplan管理网络

## 环境

ubuntu 20.04

## 配置静态IP

编辑`/etc/netplan/01-network-manager-all.yaml`

原文件内容：

```yaml
network:
  version: 2
  renderer: NetworkManager
```

编辑后文件内容：

```yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets:
          eth1:
                  dhcp4: no
                  dhcp6: no
                  addresses: [192.168.1.10/24]
                  gateway4: 192.168.1.1
                  nameservers:
                          addresses: [8.8.8.8, 114.114.114.114]
```

执行命令：`netplan apply`，将配置激活。

