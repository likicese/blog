# binlog

## 查看

在mysql的命令行中执行以下命令

``` bash
shwo binary logs;  # 获取文件列表
show binlog events;  # 查看第一个binlog文件内容
show biglog events in "mysql-binlog.000517";  # 查看指定文件内容
```