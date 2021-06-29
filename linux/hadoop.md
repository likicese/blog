# hadoop

## 开启日志轮转

编辑文件：${HADOOP_HOME}/etc/hadoop/yarn-site.xml，加入如下内容

``` config
<property>
    <name>yarn.log-aggregation-enable</name>
    <value>true</value>
    <description>打开日志聚集服务</description>
</property>
<property>
    <name>yarn.nodemanager.remote-app-log-dir</name>
    <value>/opt/hadoop/data/logs</value>
    <description>日志的聚集位置</description>
</property>
<property>
    <name>yarn.log.server.url</name>
    <value>http://${yarn.resourcemanager.hostname}:19888/jobhistory/logs</value>
    <description>日志查看</description>
</property>
<property>
    <name>yarn.log-aggregation.retain-seconds</name>
    <value>864000</value>
    <description>日志多久之前算过期。单位为秒，此时设定为10天</description>
</property>
<property>
    <name>yarn.log-aggregation.retain-check-interval-seconds</name>
    <value>-1</value>
    <description>检查日志时间间隔，过期则删除，单位为秒。-1为过期的1/10，即当设定日志保存10天时，则每隔1天检查一次。</description>
</property>
``

执行以下语句，启动jobhistory

``` bash
/opt/hadoop/sbin/mr-jobhistory-daemon.sh start historyserver
```