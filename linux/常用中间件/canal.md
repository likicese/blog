# canal

## 报错解决

### mysql的gtid参数设置导致监听失败问题

现象：

```
ERROR c.a.o.c.p.inbound.mysql.rds.RdsBinlogEventParserProxy - dump address /192.168.1.2:3306 has an error, retrying. caused by
java.io.IOException: Received error packet: errno = 1236, sqlstate = HY000 errmsg = Cannot replicate anonymous transaction when @@GLOBAL.GTID_MODE = ON, at file ./mysql-bin.000120, position 367777777.; the first event 'mysql-bin.000120' at 367777777, the last event read from './mysql-bin.000120' at 367777778, the last byte read from './mysql-bin.000120' at 367777778.
```

原因：

似乎是因为同步冲突

[参考](https://github.com/alibaba/canal/issues/1288)

解决：

按参考所示，修改`canal.instance.tsdb.enable = true`为`canal.instance.tsdb.enable = false`，重启canal，依旧报错。

继而判断是本地缓存数据问题。删除`/opt/canal.deployer-1.1.4/conf/xxx/`文件夹下两个文件：`./h2.mv.db`和`./meta.dat`，再次重启，解决。

注意，xxx为实例名字，每个实例都是在conf下有一个文件夹。

### 旧文件导致的冲突

```
2020-12-28 16:14:53.363 [destination = testdb , address = mysql-test.test.com/192.168.1.10:3306 , EventParser] ERROR c.a.o.canal.parse.inbound.mysql.dbsync.DirectLogFetcher - I/O error while reading from client socket
java.io.IOException: Received error packet: errno = 1236, sqlstate = HY000 errmsg = Could not find first log file name in binary log index file
        at com.alibaba.otter.canal.parse.inbound.mysql.dbsync.DirectLogFetcher.fetch(DirectLogFetcher.java:102) ~[canal.parse-1.1.4.jar:na]
        at com.alibaba.otter.canal.parse.inbound.mysql.MysqlConnection.dump(MysqlConnection.java:169) [canal.parse-1.1.4.jar:na]
        at com.alibaba.otter.canal.parse.inbound.AbstractEventParser$3.run(AbstractEventParser.java:279) [canal.parse-1.1.4.jar:na]
        at java.lang.Thread.run(Thread.java:748) [na:1.8.0_152]
2020-12-28 16:14:53.363 [destination = testdb , address = mysql-test.test.com/192.168.1.10:3306 , EventParser] ERROR c.a.o.c.p.inbound.mysql.rds.RdsBinlogEventParserProxy - dump address mysql-test.test.com/192.168.1.10:3306 has an error, retrying. caused by
java.io.IOException: Received error packet: errno = 1236, sqlstate = HY000 errmsg = Could not find first log file name in binary log index file
        at com.alibaba.otter.canal.parse.inbound.mysql.dbsync.DirectLogFetcher.fetch(DirectLogFetcher.java:102) ~[canal.parse-1.1.4.jar:na]
        at com.alibaba.otter.canal.parse.inbound.mysql.MysqlConnection.dump(MysqlConnection.java:169) ~[canal.parse-1.1.4.jar:na]
        at com.alibaba.otter.canal.parse.inbound.AbstractEventParser$3.run(AbstractEventParser.java:279) ~[canal.parse-1.1.4.jar:na]
        at java.lang.Thread.run(Thread.java:748) [na:1.8.0_152]
2020-12-28 16:14:53.364 [destination = testdb , address = mysql-test.test.com/192.168.1.10:3306 , EventParser] ERROR com.alibaba.otter.canal.common.alarm.LogAlarmHandler - destination:testdb[java.io.IOException: Received error packet: errno = 1236, sqlstate = HY000 errmsg = Could not find first log file name in binary log index file
        at com.alibaba.otter.canal.parse.inbound.mysql.dbsync.DirectLogFetcher.fetch(DirectLogFetcher.java:102)
        at com.alibaba.otter.canal.parse.inbound.mysql.MysqlConnection.dump(MysqlConnection.java:169)
        at com.alibaba.otter.canal.parse.inbound.AbstractEventParser$3.run(AbstractEventParser.java:279)
        at java.lang.Thread.run(Thread.java:748)
```

解决：

删除以前留下的文件。

```
rm -f /opt/canal.deployer-1.1.4/conf/testdb/*
```

