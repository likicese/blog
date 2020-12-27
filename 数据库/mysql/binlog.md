# binlog

## 查看

在mysql的命令行中执行以下命令

``` bash
flush logs;  # 重新写入一个日志文件
shwo binary logs;  # 获取文件列表
show binlog events;  # 查看第一个binlog文件内容
show biglog events in "mysql-binlog.000517";  # 查看指定文件内容
```

在linux命令行中执行一下命令

```bash
mysqlbinlog --start-datetime='2020-12-15 00:00:00' --stop-datetime='2020-12-25 23:23:23' -d mydbname mysql-binlog.000517  # 查看名为mysql-binlog.000517的文件内容
```

