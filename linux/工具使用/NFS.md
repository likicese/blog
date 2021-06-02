# NFS

## 例子情况介绍

服务端IP：192.168.1.100

客户端IP：192.168.1.101

## 服务端

### 安装

``` bash
yum install nfs-utils
yum install rpcbind
```

### 修改配置文件 /etc/exports

配置文件内容解释：仅192.168.1.101服务器连入，连入身份id为1000

```txt
/opt/share    192.168.1.101(insecure,rw,sync,root_squash,all_squash,anonuid=1000,anongid=1000)
```

### 启动服务器

``` bash
systemctl start rpcbind
systemctl start nfs
systemctl enable nfs  # 设置开机启动
```

## 客户端

### 连入NFS服务

``` bash
yum install nfs-utils
showmount -e 192.168.1.100  # 查看nfs主机允许挂载的情况
mount -t nfs 192.168.1.100:/opt/share /opt/share  # 挂载

df -Th  # 查看挂载的nfs
```

### 设置自动挂载NFS

编辑配置文件 /etc/fstab

``` txt
192.168.1.100:/opt/share /opt/share nfs defaults 0 0
```