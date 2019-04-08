# Centos7.6安装Mysql

## 环境简述

centos：7.6，mini最小安装
mysql：8.0.15

## 安装过程

### 1、下载安装包

mysql：<https://dev.mysql.com/downloads/mysql/>  
iksemel：<https://centos.pkgs.org/7/puias-unsupported-x86_64/iksemel-1.4-6.sdl7.x86_64.rpm.html>

### 2、卸载mariadb相关的东西

查询（以下仅查出一条，故只删除一条）：
>[root@localhost mysql]# rpm -aq | grep mariad  
>mariadb-libs-5.5.60-1.el7_5.x86_64

卸载：
>[root@localhost mysql]# rpm -e --nodeps mariadb-libs-5.5.60-1.el7_5.x86_64  

### 3、安装mysql

请按以下顺序安装，否则会出现依赖问题
>[root@localhost mysql]# yum install mysql-community-libs-8.0.15-1.el7.x86_64.rpm  
>[root@localhost mysql]# yum install mysql-community-client-8.0.15-1.el7.x86_64.rpm  
>[root@localhost mysql]# yum install mysql-community-server-8.0.15-1.el7.x86_64.rpm  
>[root@localhost mysql]# yum install mysql-community-libs-compat-8.0.15-1.el7.x86_64.rpm  

## 启动

>[root@localhost mysql]# systemctl start mysqld

## 测试

### 1、寻找密码（密码在mysql的创建日志里边）

>[root@localhost mysql]# vi /var/log/mysqld.log  
>2019-03-14T12:04:50.986632Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.15) initializing of server in progress as process 28260  
>2019-03-14T12:04:54.058003Z 5 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: o1)DJeSXOq+p

### 2、进入mysql，密码如上所示，即：o1)DJeSXOq+p

>[root@localhost mysql]# mysql -uroot -p  
>Enter password:

### 3、修改密码（要求一定长度，有大小写字母、特殊字符、数字）

>mysql> set password = 'YOU#password123'  
>mysql> flush privileges

## 数据库基本操作

``` sql
show databases;  # 查看全部数据库
create database databasename;  # 创建数据库
create user 'username'@'%' identified by 'yourpassword';  # 创建用户
grant all privileges on databasename.* to 'username'@'%';  # 给予用户数据库的全部权限。完成后，记得刷新
flush privileges;  # 刷新权限
```

## 错误修正

### 1、未卸载mariadb

Error: Package: zabbix-server-mysql-4.0.5-1.el7.x86_64 (@zabbix)  
           Requires: libmysqlclient.so.18(libmysqlclient_18)(64bit)  
           Removing: 1:mariadb-libs-5.5.60-1.el7_5.x86_64 (@anaconda)  
               libmysqlclient.so.18(libmysqlclient_18)(64bit)  
           Obsoleted By: mysql-community-libs-8.0.15-1.el7.x86_64 (/mysql-community-libs-8.0.15-1.el7.x86_64)  
               Not found  
Error: Package: 2:postfix-2.10.1-7.el7.x86_64 (@anaconda)  
           Requires: libmysqlclient.so.18()(64bit)  
           Removing: 1:mariadb-libs-5.5.60-1.el7_5.x86_64 (@anaconda)  
               libmysqlclient.so.18()(64bit)  
           Obsoleted By: mysql-community-libs-8.0.15-1.el7.x86_64 (/mysql-community-libs-8.0.15-1.el7.x86_64)  
              ~libmysqlclient.so.21()(64bit)  
Error: Package: zabbix-server-mysql-4.0.5-1.el7.x86_64 (@zabbix)  
           Requires: libmysqlclient.so.18()(64bit)  
           Removing: 1:mariadb-libs-5.5.60-1.el7_5.x86_64 (@anaconda)  
               libmysqlclient.so.18()(64bit)  
           Obsoleted By: mysql-community-libs-8.0.15-1.el7.x86_64 (/mysql-community-libs-8.0.15-1.el7.x86_64)  
              ~libmysqlclient.so.21()(64bit)  
Error: Package: 2:postfix-2.10.1-7.el7.x86_64 (@anaconda)  
           Requires: libmysqlclient.so.18(libmysqlclient_18)(64bit)  
           Removing: 1:mariadb-libs-5.5.60-1.el7_5.x86_64 (@anaconda)  
               libmysqlclient.so.18(libmysqlclient_18)(64bit)  
           Obsoleted By: mysql-community-libs-8.0.15-1.el7.x86_64 (/mysql-community-libs-8.0.15-1.el7.x86_64)  
               Not found  
 You could try using --skip-broken to work around the problem  
 You could try running: rpm -Va --nofiles --nodigest  

 修正操作：把mariadb卸载干净

### 2、未输入mysql密码

ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)  
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)  

修正操作：去mysql的安装日志中，寻找密码，输入，并进入

### 3、未启动mysql

ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/my

修正操作：启动mysql

### 4、使用了mysql-server 8.0版本，却用mysql-client 5.4连接

ERROR 2059 (HY000): Authentication plugin 'caching_sha2_password' cannot be loaded: /usr/lib64/mysql/plugin/caching_sha2_password.so: cannot open shared object file: No such fileor directory

使用另一个插件：  
mysql> CREATE USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'pMQiEge1ikst7S_6tlXzBOmt_4b';