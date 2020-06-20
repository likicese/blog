# mysql数据库命令

## 前言

1. “用户”并没有那么神秘。对数据库来说，用户也是一张表。
2. 使用 `select` 语句的时候，多查询一列，则多增加一点性能消耗。

## 数据库

``` sql
show databases;  # 查看全部数据库
create database databaseName;  # 创建数据库
drop database databaseName;  ## 删除数据库
```

## 数据表

``` sql
desc tableName;  # 显示表结构
create table tableName(colName1 type [not null] [primary key], colName2 type [not null] [primary key]);  # 创建新数据表
drop table tableName;  # 删除数据表
create table newTableName like oldTableName  # 根据旧表创建新表
```

## 用户

``` sql
create user 'username'@'%' identified by 'yourpassword';  # 创建用户
grant all privileges on databaseName.* to 'username'@'%';  # 给予用户数据库的全部权限。"%" 代表该用户在任意IP地址登录均能看见这个表。完成后，记得刷新
update mysql.user set Host='127.0.0.1', password=password('you password') where User="you name";  # 修改密码
```

## 常用SQL语句

``` sql
insert into tableName(colName1, colName2 ... colNameN) value(value1, value2 ... valueN)  # 增
dalete from tableName where colName = "value"  # 删
update tableName set colName1 = "value" where colName2 = "value"  # 更新表数据
select * from tableName  # 查
```

## 特殊select语句

mysql时间格式化说明：<https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format>

``` sql
SELECT SUM(column1), GROUP_CONCAT(DATE_FORMAT(columnData,'%Y-%M')) FROM test_1 GROUP BY DATE_FORMAT(columnData,'%Y-%M')  # 按月分组
```

### 备份
```
mysqldump \
-u userName \ 
-ppassWord \
--single-transaction  # InnoDB引擎中可用。锁住表结构。可对表中内容进行操作 \
--flush-logs  # 数据库备份后，刷新日志 \
--add-drop-database  # 添加删除表语句 \
-B dbName1 dbName2  # 表名 \
--master-data=2  # 将二进制信息写入到备份文件中 
```

## 其它操作

``` sql
flush privileges;  # 刷新权限。设定用户相关后使用
```