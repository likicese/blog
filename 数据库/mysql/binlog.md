# binlog

## 查看

在mysql的命令行中执行以下命令

``` bash
flush logs;  # 重新写入一个日志文件
show binary logs;  # 获取文件列表
show binlog events;  # 查看第一个binlog文件内容
show binlog events in "mysql-binlog.000517";  # 查看指定文件内容
```

在linux命令行中执行一下命令

```bash
mysqlbinlog --start-datetime='2020-12-15 00:00:00' --stop-datetime='2020-12-25 23:23:23' -d mydbname mysql-binlog.000517  # 查看名为mysql-binlog.000517的文件内容
```

## 维护

``` mysql
PURGE MASTER LOGS BEFORE '2021-07-15 00:00:00';  # 删除该日期之前的日志
PURGE MASTER LOGS TO 'binlog.000111';  # 删除这个编号之前的binlog
```

## 日志过期时间

``` mysql
show variables like '%expire%';  # 相关变量
```

mysql8之后，使用变量`binlog_expire_logs_seconds`和`expire_logs_days`

``` mysql
set global binlog_expire_logs_seconds=604800;  # 设置变量，只留7天
flush logs;  # 刷新
mysqlbinlog --start-datetime="2021-09-18 09:15:00" --stop-datetime="2021-09-18 09:55:00" --base64-output=decode-rows --verbose mysql-binlog.000517 > 1.sql  # 导出该时间段的sql
```
