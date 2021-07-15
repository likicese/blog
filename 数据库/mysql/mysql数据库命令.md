# mysql数据库命令

## 前言

1. “用户”并没有那么神秘。对数据库来说，用户也是一张表。
2. 使用 `select` 语句的时候，多查询一列，则多增加一点性能消耗。

## 数据库

``` sql
show databases;  # 查看全部数据库
create database databaseName;  # 创建数据库
drop database databaseName;  # 删除数据库

show create table dataName.tableName\G;  # 查看建表语句
```

## 数据表

``` sql
desc tableName;  # 显示表结构
create table tableName(colName1 type [not null] [primary key], colName2 type [not null] [primary key]);  # 创建新数据表
drop table tableName;  # 删除数据表
create table newTableName like oldTableName  # 根据旧表创建新表
```

## 用户

``` mysql
create user 'username'@'%' identified by 'yourpassword';  # 创建用户
grant all privileges on databaseName.* to 'username'@'%';  # 给予用户数据库的全部权限。"%" 代表该用户在任意IP地址登录均能看见这个表。完成后，记得刷新
update mysql.user set Host='127.0.0.1', password=password('you password') where User="you name";  # 修改密码
ALTER USER 'userName'@'localhost' IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY 'xxxxxxxxxpassword';  # 修改密码
```

## 授权

```mysql
grant update, select on databaseName.tableName to 'userName'@'localhost';  # 授予从localhost登录的userName用户对databaseName数据库tableName表的更新和查询权限。
grant all privileges on databaseName.* to 'userName'@'192.%.%.%';  # 授予该用户全部权限。
show grants for 'userName'@'localhost'  # 查询从localhost登录的userName用户具备的权限
grant grant option on *.* to 'admin'@'%';  # 使该用户能够控制其他用户的权限
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

## 锁的核心表

sys.innodb_lock_waits

performance_schema.events_statements_history

performance_schema.data_locks

performance_schema.data_locks_wait

## 密码相关

mysql8下

```mysql
show variables like 'validate_password%';  # 查看有关密码的设置
set global validate_password.policy=0;  # 密码验证低要求
```

## 其它操作

``` sql
flush privileges;  # 刷新权限。设定用户相关后使用
show processlist;  # 显示当前执行的线程
select * from sys.`innodb_lock_waits`;  # 查找当前等待锁的线程
select * from information_schema.processlist WHERE HOST like '%1.9%'  # 查询192.168.1.9的mysql连接数
```

### 复制一张表

索引、外键一同复制到新表

```
CREATE table user_20210106 like user;
INSERT into user_20210106 SELECT * FROM user;
```

比较快，但会丢失索引、外键等信息

```
CREATE TABLE user_20210106 SELECT * FROM user
```

