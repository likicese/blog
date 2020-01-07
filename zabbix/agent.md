# agent

## 快速修改agent配置文件

指定了 3.4.14 版本

``` bash
zabbix_host=192.168.1.104
rpm -ivh http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-agent-3.4.14-1.el7.x86_64.rpm
sed -i "s/^Server=127.0.0.1$/Server=$zabbix_host/g" /etc/zabbix/zabbix_agentd.conf
sed -i "s/^ServerActive=127.0.0.1$/ServerActive=$zabbix_host/g"  /etc/zabbix/zabbix_agentd.conf
hostname -I | xargs -i /bin/bash -c "sed -i 's/^Hostname=Zabbix server$/Hostname={}/g' /etc/zabbix/zabbix_agentd.conf"
systemctl enable zabbix-agent
systemctl start zabbix-agent
```