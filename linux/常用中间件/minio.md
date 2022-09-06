# minio

## 前言

[MinIO | Code and downloads to create high performance object storage](https://min.io/download#/linux)

需要4个都启动，才会去监听9001端口

## 创建

```shell
mkdir /etc/minio/
mkdir /data/minio
useradd minio -M -s /bin/false
chown minio:minio -R /data/minio
```

## 可用性

| 存活/集群节点总数 | 读写状态   |      |
| ----------------- | ---------- | ---- |
| 4/4               | 可读可写   |      |
| 3/4               | 可读可写   |      |
| 2/4               | 可读不可写 |      |
| 1/4               | 不可读     |      |

## 权限

只给某个用户桶（app-uat）的权限

创建一个权限控制

```bash
mc admin policy add minio-uat app-uat-policy app-uat-policy.json  # 添加一个名为app-uat-policy的权限控制，json文件内容如下
```

scm-uat-policy.json文件内容（注意，version是固定的）如下：

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::app-uat/*"
            ]
        }
    ]
}
```

## 客户端

```bash
bash +o history  # 临时禁用命令记录
mc alias set minio-uat http://127.0.0.1:9000 admin 123456  # 设置s3此服务名字为minio-uat。注意，应使用api端口9000，而非console端口9001
mc admin info minio-uat  # 获取信息
```

## 桶

governance模式：除非拥有特殊权限，否则用户无法覆盖或删除对象版本或更改其锁定设置

compliance模式：任何用户都不能覆盖或删除受保护的对象版本，包括AWS账户中的root用户

## 创建新盘

```bash
yum install -y lvm2 gdisk
gdisk /dev/sda  # n新建,回车，回车，w写入，y确认结束
partprobe

pvcreate /dev/sda4
vgcreate vg01 /dev/sda4
lvcreate -n lv01 -l 100%FREE vg01  # 使用全部空间
mkfs.xfs /dev/vg01/lv01
echo "/dev/vg01/lv01 /data xfs defaults 0 0" >> /etc/fstab  # 开机自动挂载
mkdir /data
mount -a  # 挂载
```

## 安装脚本

```shell
mkdir -p /etc/minio/
mkdir -p /data/minio
chown minio:minio -R /data/minio
useradd minio -M -s /bin/false

mv mc /usr/local/bin/
chmod 555 /usr/local/bin/mc
yum install -y minio-20220717154314.0.0.x86_64.rpm

H1='minio01.exp.com'
H2='minio02.exp.com'
H3='minio03.exp.com'
H4='minio04.exp.com'
H1_IP='192.168.1.1'
H2_IP='192.168.1.2'
H3_IP='192.168.1.3'
H4_IP='192.168.1.4'

SYSTEMD_FILE='/etc/systemd/system/minio.service'

echo "${H1_IP} ${H1}" >> /etc/hosts
echo "${H2_IP} ${H2}" >> /etc/hosts
echo "${H3_IP} ${H3}" >> /etc/hosts
echo "${H4_IP} ${H4}" >> /etc/hosts

cat > /etc/minio/minio.conf << EOF
MINIO_VOLUMES="http://${H1}/data/minio http://${H2}/data/minio http://${H3}/data/minio http://${H4}/data/minio"

MINIO_OPTS="--address :9000 --console-address :9001 --json"

MINIO_ACCESS_KEY=admin

MINIO_SECRET_KEY=lJsNmoJvsTn+0NrxpBzZI
EOF

sed -i 's/User=minio-user/User=minio/' ${SYSTEMD_FILE}
sed -i 's/Group=minio-user/Group=minio/' ${SYSTEMD_FILE}
sed -i 's/EnvironmentFile=-\/etc\/default\/minio/EnvironmentFile=-\/etc\/minio\/minio.conf/' ${SYSTEMD_FILE}

systemctl start minio.service
systemctl enable minio.service

echo "是否已修改启动文件？"
```

