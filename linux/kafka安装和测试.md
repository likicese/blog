# kafka安装和测试

## 安装

### 一、下载和解压 压缩包

[Apache官网](http://kafka.apache.org/downloads.html)

下载命令：wget

``` sh
tar -xzf kafka_2.12-2.2.0.tgz  # 解压
```

### 二、启动服务

tips ：命令后面的 "&" 表示当前程序后台运行。

``` sh
cd kafka_2.12-2.2.0
./bin/zookeeper-server-start.sh config/zookeeper.properties &  # 启动zookeeper
./bin/kafka-server-start.sh config/server.properties &  # 启动kafka
```

## 测试

注意：我的kafka和zookeeper都运行在一台服务器上

### 一、创建topic

``` sh
./bin/kafka-topics.sh --create --zookeeper localhsot:2181 --replication-factor 1 --partitions 1 --topic testtopic

# topic列表
./bin/kafka-topics.sh --zookeeper localhsot:2181 --list
```

### 二、创建生产者

会阻塞当前shell，接受键盘输入的消息

``` sh
./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testtopic
```

### 三、创建消费者

会阻塞当前shell，打印生产者提供的消息

``` sh
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testtopic --from-beginning
```