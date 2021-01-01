# mysql查询优化

## 索引

### Cardinality

该值可以通过命令`show index for tableName;`显示

意义是该列中不重复的数据个数。假设某表有100行数据，其中有50条是唯一的，则该值为50。

那么，该值比较大的时候，mysql查询优化器就会走索引。

当表中1/16的数据发生变化或数据变化次数超过200 000 0000次时，会自动更新。

这只是个预估值。不准的时候，需要用以下语句手动更新。

``` bash
analyze table tableName;  # Cardinality基准值无法真实反应表的变化时，需要执行此命令，对表直接更新。
select CONCAT("analyze table ", table_name, ";")  table_name from information_schema.tables where table_schema='dataName'  # 拼接出批量更新的语句 
```


