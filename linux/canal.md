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