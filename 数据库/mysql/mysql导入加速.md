# mysql导入加速

``` mysql
进入 mysql
mysql -u root -p

创建数据库
CREATE DATABASE 数据库名;

设置参数
set sql_log_bin=OFF;  //关闭日志
set autocommit=0;  //关闭 autocommit 自动提交模式

使用数据库
use 数据库名;

开启事务
START TRANSACTION;

引入 SQL 文件
source 文件的路径;

成功后事务提交
COMMIT;
```

根据测算， 22GB数据文件，600张表，表数据分配不均。

一套操作下来，导入速度和`mysql -uroot -p12345678 < 数据文件`命令没差。