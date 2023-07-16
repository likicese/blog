# rocketmq

## 安装脚本

```shell
yum install -y java-1.8.0-openjdk
useradd rocketmq -m -s /bin/false
VERSION='4.9.3'
PACKAGE='rocketmq-all-4.9.3-bin-release.zip'
SOFTWARE_NAME='rocketmq-all-4.9.3-bin-release'
wget -P /usr/local/ https://dist.apache.org/repos/dist/release/rocketmq/${VERSION}/${PACKAGE}
cd /usr/local/; unzip -q ${PACKAGE}; rm -f ${PACKAGE}; ln -s ${SOFTWARE_NAME}/ rocketmq
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

## 升级

升级，保留启动配置和配置文件

```
IP=192.168.1.11
PACKAGE=rocketmq-all-4.9.7-bin-release.zip
NEW_SOFTWARE_NAME=rocketmq-all-4.9.7-bin-release
OLD_SOFTWARE_NAME=rocketmq-all-4.9.3-bin-release

scp ${PACKAGE} ${IP}:/usr/local/
ssh ${IP} "cd /usr/local/; unzip -q ${PACKAGE}; rm ${PACKAGE}"
ssh ${IP} "cd /usr/local/; cp -p rocketmq/bin/runbroker.sh rocketmq/bin/runserver.sh ${NEW_SOFTWARE_NAME}/bin/"
ssh ${IP} "cd /usr/local/; cp -rp rocketmq/conf/ ${NEW_SOFTWARE_NAME}/"
ssh ${IP} "systemctl stop mqbroker mqnamesrv"
ssh ${IP} "cd /usr/local/; ln -s ${NEW_SOFTWARE_NAME}/ rocketmq"
ssh ${IP} "systemctl start mqbroker mqnamesrv"
```

