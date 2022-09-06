# rocketmq

## 安装脚本

```shell
yum install -y java-1.8.0-openjdk
useradd rocketmq -m -s /bin/false
mv /home/centos/rocketmq /usr/local/
chown -R root:root /usr/local/rocketmq

H1='rocketmq01.example.com'
H2='rocketmq02.example.com'
H3='rocketmq03.example.com'
H4='rocketmq04.example.com'
H1_IP='192.168.1.11'
H2_IP='192.168.1.12'
H3_IP='192.168.1.13'
H4_IP='192.168.1.14'

echo "${H1_IP} ${H1}" >> /etc/hosts
echo "${H2_IP} ${H2}" >> /etc/hosts
echo "${H3_IP} ${H3}" >> /etc/hosts
echo "${H4_IP} ${H4}" >> /etc/hosts

echo "namesrvAddr=${H1}:9876;${H2}:9876;${H3}:9876;${H4}:9876" >> /usr/local/rocketmq/conf/2m-2s-sync/broker-a.properties
echo "namesrvAddr=${H1}:9876;${H2}:9876;${H3}:9876;${H4}:9876" >> /usr/local/rocketmq/conf/2m-2s-sync/broker-a-s.properties
echo "namesrvAddr=${H1}:9876;${H2}:9876;${H3}:9876;${H4}:9876" >> /usr/local/rocketmq/conf/2m-2s-sync/broker-b.properties
echo "namesrvAddr=${H1}:9876;${H2}:9876;${H3}:9876;${H4}:9876" >> /usr/local/rocketmq/conf/2m-2s-sync/broker-b-s.properties


cat > /lib/systemd/system/mqbroker.service << EOF
[Unit]
Requisite=network-online.target
After=network-online.target network.target

[Install]
WantedBy=multi-user.target

[Service]
User=rocketmq
Group=rocketmq
Type=idle
RestartSec=2s
WorkingDirectory=/usr/local/rocketmq
ExecStart=/usr/local/rocketmq/bin/mqbroker -c /usr/local/rocketmq/conf/2m-2s-sync/broker-a.properties
TimeoutSec=60s
EOF


cat > /lib/systemd/system/mqnamesrv.service << EOF
[Unit]
Requisite=network-online.target
After=network-online.target network.target

[Install]
WantedBy=multi-user.target

[Service]
User=rocketmq
Group=rocketmq

Type=idle
RestartSec=2s
WorkingDirectory=/usr/local/rocketmq/
ExecStart=/usr/local/rocketmq/bin/mqnamesrv

TimeoutSec=60s
EOF

systemctl start mqnamesrv.service
systemctl start mqbroker.service
systemctl enable mqnamesrv.service
systemctl enable mqbroker.service

echo "是否已修改启动文件？"
```

调整内存

```
/usr/local/rocketmq/bin/runserver.sh
/usr/local/rocketmq/bin/runbroker.sh
```

