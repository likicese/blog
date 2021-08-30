# hadoop

## 安装脚本

``` bash
function get_file() {
    mkdir /opt/package
    cd /opt/package
    wget https://www.apache.org/dyn/closer.lua/spark/spark-3.0.1/spark-3.0.1-bin-without-hadoop.tgz
    wget https://mirror.bit.edu.cn/apache/spark/spark-3.0.1/spark-3.0.1-bin-without-hadoop.tgz

    tar -xf hadoop-3.2.1.tar.gz
    tar -xf spark-3.0.1-bin-without-hadoop.tgz

    mv hadoop-3.2.1 ../
    mv spark-3.0.1-bin-without-hadoop ../
    cd ..
    ln -s spark-3.0.1-bin-without-hadoop/ spark
    ln -s hadoop-3.2.1/ hadoop
}

function set_variable() {
    HOST_IP_HADOOP01='192.168.1.1'
    HOST_IP_HADOOP02='192.168.1.2'
    HOST_IP_HADOOP03='192.168.1.3'

    HOST_IP_ZOOKEEPER01='192.168.1.4'
    HOST_IP_ZOOKEEPER02='192.168.1.5'
    HOST_IP_ZOOKEEPER03='192.168.1.6'

    cat >>/etc/hosts <<EOF

${HOST_IP_HADOOP01} hadoop01-dev
${HOST_IP_HADOOP02} hadoop02-dev
${HOST_IP_HADOOP03} hadoop03-dev
EOF
}

function hadoop() {
    cat >>/opt/hadoop/etc/hadoop/hadoop-env.sh <<EOF

export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export HADOOP_SHELL_EXECNAME=root
export JAVA_HOME=/usr/java/default
export HADOOP_HOME=/opt/hadoop
export HADOOP_PID_DIR=/opt/hadoop/pid

EOF

    sed -i '/^localhost$/ d' /opt/hadoop/etc/hadoop/workers
    cat >>/opt/hadoop/etc/hadoop/workers <<EOF
hadoop01-dev
hadoop02-dev
hadoop03-dev
EOF

    # 集群中用于应用程序的上限从0.1提高到0.8
    sed -i ':a;N;s/    <name>yarn.scheduler.capacity.maximum-am-resource-percent<\/name>\n    <value>0.1/    <name>yarn.scheduler.capacity.maximum-am-resource-percent<\/name>\n    <value>0.8/' /opt/hadoop/etc/hadoop/capacity-scheduler.xml

    # 设置命令
    echo "export PATH=\$PATH:/opt/hadoop/bin" >>/etc/profile
}

function hdfs() {
    sed -i 's/HADOOP_SHELL_EXECNAME="hdfs"/HADOOP_SHELL_EXECNAME="root"/' /opt/hadoop/bin/hdfs

    HOSTNAME='hadoop01-dev'

    mkdir -p /opt/hadoop_dfs/{name,data,namesecondary,mapred/{local,system}}

    sed -i '/<configuration>/a\
    <property>\
        <name>fs.default.name</name>\
        <value>hdfs://${HOSTNAME}/</value>\
        <final>true</final>\
    </property>\
    <property>\
        <name>hadoop.logfile.size</name>\
        <value>100000000</value>\
        <description>The max size of each log file</description>\
    </property>\
    <property>\
        <name>hadoop.logfile.count</name>\
        <value>10</value>\
        <description>The max number of log files</description>\
    </property>\
' /opt/hadoop/etc/hadoop/core-site.xml

    sed -i '/<configuration>/a\
    <property>\
        <name>dfs.name.dir</name>\
        <value>/opt/hadoop_dfs/name</value>\
        <final>true</final>\
    </property>\
    <property>\
        <name>dfs.data.dir</name>\
        <value>/opt/hadoop_dfs/data</value>\
        <final>true</final>\
    </property>\
    <property>\
        <name>fs.checkpoint.dir</name>\
        <value>/opt/hadoop_dfs/namesecondary</value>\
        <final>true</final>\
    </property>\
' /opt/hadoop/etc/hadoop/hdfs-site.xml

    /opt/hadoop/bin/hadoop namenode -format
}

function yarn() {
    sed -i '/<\/configuration>/d' /opt/hadoop/etc/hadoop/yarn-site.xml

    cat >>/opt/hadoop/etc/hadoop/yarn-site.xml <<EOF
<property>
    <name>yarn.resourcemanager.hostname</name>
    <value>hadoop01-dev</value>
</property>
<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
</property>
<property>
    <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>
<property>
    <description>The address of the applications manager interface in the RM.</description>
    <name>yarn.resourcemanager.address</name>
    <value>\${yarn.resourcemanager.hostname}:8032</value>
</property>
<property>
    <description>The address of the scheduler interface.</description>
    <name>yarn.resourcemanager.scheduler.address</name>
    <value>\${yarn.resourcemanager.hostname}:8030</value>
</property>
<property>
    <description>The http address of the RM web application.</description>
    <name>yarn.resourcemanager.webapp.address</name>
    <value>\${yarn.resourcemanager.hostname}:8088</value>
</property>
<property>
    <description>The https adddress of the RM web application.</description>
    <name>yarn.resourcemanager.webapp.https.address</name>
    <value>\${yarn.resourcemanager.hostname}:8090</value>
</property>
<property>
    <name>yarn.resourcemanager.resource-tracker.address</name>
    <value>\${yarn.resourcemanager.hostname}:8031</value>
</property>
<property>
    <description>The address of the RM admin interface.</description>
    <name>yarn.resourcemanager.admin.address</name>
    <value>\${yarn.resourcemanager.hostname}:8033</value>
</property>
<property>
    <name>yarn.nodemanager.local-dirs</name>
    <value>/opt/hadoop_dfs/yarn/local</value>
</property>
<property>
    <name>yarn.log-aggregation-enable</name>
    <value>true</value>
</property>
<property>
    <name>yarn.nodemanager.remote-app-log-dir</name>
    <value>/opt/hadoop_dfs/data/tmp/logs</value>
</property>
<property>
    <name>yarn.log.server.url</name>
    <value>http://\${yarn.resourcemanager.hostname}:19888/jobhistory/logs</value>
</property>
<property>
    <name>yarn.nodemanager.vmem-check-enabled</name>
    <value>false</value>
</property>
<property>
    <name>yarn.scheduler.capacity.maximum-am-resource-percent</name>
    <value>0.8</value>
</property>
</configuration>
EOF

    cat >>/opt/hadoop/etc/hadoop/yarn-env.sh <<EOF
export YARN_RESOURCEMANAGER_USER=root
export HADOOP_SECURE_DN_USER=yarn
export YARN_NODEMANAGER_USER=root
EOF
}

function spark() {
    cat >>/opt/spark/conf/slaves <<EOF
hadoop01-dev
hadoop02-dev
hadoop03-dev
EOF

    cat >/opt/spark/conf/spark-env.sh <<EOF
export SPARK_DIST_CLASSPATH=$(/opt/hadoop/bin/hadoop classpath)
export JAVA_HOME=/usr/java/default
export HADOOP_HOME=/opt/hadoop
export HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop
export SPARK_WORKER_MEMORY=512m
export SPARK_WORKER_CORES=3
export SPARK_DAEMON_JAVA_OPTS="-Dspark.deploy.recoveryMode=ZOOKEEPER -Dspark.deploy.zookeeper.url=${HOST_IP_ZOOKEEPER01}:2181,${HOST_IP_ZOOKEEPER02}:2181,${HOST_IP_ZOOKEEPER03}:2181 -Dspark.deploy.zookeeper.dir=/spark-test"
export SPARK_EXECUTOR_MEMORY=1.5g
export SPARK_DRIVER_MEMORY=8g
EOF
}



function node_add_start_in_power_on() {
    cat >/etc/rc.local <<EOF

sleep 30
/opt/spark/sbin/start-master.sh
/opt/spark/sbin/start-slave.sh spark://hadoop01-dev:7077,hadoop02-dev:7077,hadoop03-dev:7077
EOF
chmod +x /etc/rc.local
}

function master_add_start_in_power_on() {
    cat >/etc/rc.local <<EOF

/opt/hadoop/sbin/start-dfs.sh
/opt/hadoop/sbin/start-yarn.sh
/opt/spark/sbin/start-master.sh
/opt/spark/sbin/start-slave.sh spark://hadoop01-dev:7077,hadoop02-dev:7077,hadoop03-dev:7077
EOF
chmod +x /etc/rc.local
}

function share_id_rsa() {
# 私钥共享
ssh hadoop02-dev "mkdir -p ~/.ssh/"
scp /root/.ssh/id_rsa hadoop02-dev:~/.ssh/
ssh hadoop03-dev "mkdir ~/.ssh/"
scp /root/.ssh/id_rsa hadoop03-dev:~/.ssh/
}

get_file
set_variable
hdfs
yarn
spark


# 前边大家配置都一样，不同在最后。建议先部署master，再部署node。对应不同的机器，放开不同的注释就行。

########## node请放开以下注释 #########
# node_add_start_in_power_on
########## node请放开以上注释 #########

########## master请放开以下注释 #########
# master_add_start_in_power_on
# share_id_rsa
########## node请放开以上注释 #########
```


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