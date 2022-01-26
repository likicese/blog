# openvpn

## 安装

[参考](https://github.com/Nyr/openvpn-install)

## 配置

### client端

```config
route-nopull  # 不接收server的推送配置。因为server默认推送全局走vpn，所以当需要指定ip走vpn时，会让配置这一项
block-outside-dns  # 禁止使用外部DNS。若发现在服务端去掉push "redirect-gateway def1 bypass-dhcp"后，导致ping得通，却无法解析域名，可以去掉此项目

max-routes 1000  # 最高添加100条路由，此参数可以突破限制
route 192.168.1.0 255.255.255.0 vpn_gateway  # 默认网络不走vpn时，指定的目的ip走vpn
route 192.168.1.0 255.255.255.0 net_gateway  # 默认网络走vpn时，指定的目的ip不走vpn

dhcp-option DNS 8.8.8.8  # 设定dns服务器
dhcp-option DOMAIN "dev.example.com"  # 设置搜索域
```

### server端

server.conf

```config
duplicate-cn  # 多个用户共用一个证书
push "route 223.5.5.5 255.255.255.255 net_gateway"  # 223.5.5.5流量走本地，不走vpn
push "route 192.168.1.0 255.255.255.0 vpn_gateway"  # 192.168.1.0/24网络走vpn

push "redirect-gateway def1 bypass-dhcp"  # 所有流量默认走vpn网络。去除这一项后，流量不会默认走vpn
```

