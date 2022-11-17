# mysql多channel监控

## 前言

由于zabbix-agent2自带的mysql监控对多channel无法监控，故而自写脚本进行监控

对多channel复制有效，单channel可能会报错

## 被监控的服务器

以下为在被监控的服务器上进行的操作

### 监控脚本

建立文件/etc/zabbix/shell/check_mysql_replica.sh，内容如下

``` bash
#!/bin/bash

user='root'
password='123456'
host='localhost'

function find_channel() {
    channel_list=$(mysql -u${user} -p${password} -h ${host} -e "SELECT CHANNEL_NAME, HOST from performance_schema.replication_connection_configuration;" 2>/dev/null | awk '{if (1 < NR) {print "{\"{#CHANNEL_NAME}\":\"" $1 "\"," "\"{#HOST}\":\"" $2 "\"}," }}')
    echo '{"data":['${channel_list%?}']}'  # %? 去除最后一个字符
}

# 参数是channel名字。binlog文件是否能接收，正常则1，异常则0
function get_io_status() {
    status=$(mysql -u${user} -p${password} -h ${host} -e "SELECT SERVICE_STATE FROM performance_schema.replication_connection_status WHERE CHANNEL_NAME='$1';" 2>/dev/null | awk '{if (1 < NR) {print $1 }}')
    if [ ${status} == "ON" ]; then
        echo 1
    else
        echo 0
    fi
}

# 参数是channel名字。sql语句是否能重播，正常则1，异常则0
function get_sql_status() {
    status=$(mysql -u${user} -p${password} -h ${host} -e "SELECT SERVICE_STATE FROM performance_schema.replication_applier_status WHERE CHANNEL_NAME='$1';" 2>/dev/null | awk '{if (1 < NR) {print $1 }}')
    if [ ${status} == "ON" ]; then
        echo 1
    else
        echo 0
    fi
}

# 校验参数的合法性
case ${1} in
    find_channel)
        find_channel
        ;;
    get_io_status)
        get_io_status ${2}
        ;;
    get_sql_status)
        get_sql_status ${2}
        ;;
    *)
        exit
esac
```

### 监控键

建立文件/etc/zabbix/zabbix_agent2.d/check_mysql_replica.conf，内容如下

``` bash
# 使用${1}无法获得变量，只能使用$1
UserParameter=mysql.replica.channels, /etc/zabbix/shell/check_mysql_replica.sh find_channel
UserParameter=mysql.replica.status.io[*], /etc/zabbix/shell/check_mysql_replica.sh get_io_status $1
UserParameter=mysql.replica.status.sql[*], /etc/zabbix/shell/check_mysql_replica.sh get_sql_status $1
```

若是客户端是zabbix-agent，而非zabbix-agent2，则在/etc/zabbix/zabbix_agent.d/文件夹下建立该文件

### 重启

重启zabbix-agent2即可

``` bash
systemctl restart zabbix-agent2
```

## zabbix-server

以下为在zabbix-web上操作，即在浏览器上操作

在本地电脑建立mysql-replication.xml文件，内容如下

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>5.0</version>
    <date>2022-01-21T09:16:07Z</date>
    <groups>
        <group>
            <name>Templates/Databases</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template DB MySQL with replication status</template>
            <name>mysql主从监控</name>
            <description>自动发现mysql主从同步异常，能自动发现多channel</description>
            <groups>
                <group>
                    <name>Templates/Databases</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>mysql replication status</name>
                </application>
            </applications>
            <discovery_rules>
                <discovery_rule>
                    <name>自动发现mysql的chanel</name>
                    <key>mysql.replica.channels</key>
                    <delay>1h</delay>
                    <item_prototypes>
                        <item_prototype>
                            <name>mysql recv binlog with channel {#CHANNEL_NAME}</name>
                            <key>mysql.replica.status.io[{#CHANNEL_NAME}]</key>
                            <applications>
                                <application>
                                    <name>mysql replication status</name>
                                </application>
                            </applications>
                            <trigger_prototypes>
                                <trigger_prototype>
                                    <expression>{last()}&lt;&gt;1</expression>
                                    <name>mysql接收binlog文件异常</name>
                                    <priority>HIGH</priority>
                                </trigger_prototype>
                            </trigger_prototypes>
                        </item_prototype>
                        <item_prototype>
                            <name>mysql sql exec with channel {#CHANNEL_NAME}</name>
                            <key>mysql.replica.status.sql[{#CHANNEL_NAME}]</key>
                            <applications>
                                <application>
                                    <name>mysql replication status</name>
                                </application>
                            </applications>
                            <trigger_prototypes>
                                <trigger_prototype>
                                    <expression>{last()}&lt;&gt;1</expression>
                                    <name>mysql重播sql异常</name>
                                    <priority>HIGH</priority>
                                </trigger_prototype>
                            </trigger_prototypes>
                        </item_prototype>
                    </item_prototypes>
                </discovery_rule>
            </discovery_rules>
        </template>
    </templates>
</zabbix_export>
```

在zabbix-web页面上，将模板导入

选择对应的mysql服务器，连接模板即可

## 排障

在zabbix-server上执行以下命令，看看是否能获取对应的数据

``` bash
zabbix_get -s 192.168.1.10 -k mysql.replica.channels
zabbix_get -s 192.168.1.10 -k mysql.replica.status.io["user"]
zabbix_get -s 192.168.1.10 -k mysql.replica.status.sql["user"]
```