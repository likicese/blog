# mariadb

## 安装

mariadb的安装比较简单。无脑`yum install`即可  
安装命令

``` shell
yum -y install mariadb mariadb-devel mariadb-server  # 安装mariadb
systemctl enable mariadb  # 设置开机启动
systemctl start mariadb  # 启动mariadb

service mysql start  # 另一种启动mariadb的方式
```

## 注意的点

### 1. mariadb安装后，root默认没密码。mysql安装后，密码储存在日志中

仅使用如下命令，即可进入数据库。

``` shell
mysql -uroot
```

### 2.创建用户指定链接地址

如下，创建用户时指定地址为127.0.0.1 。

``` shell
create user 'username'@'127.0.0.1' identified by 'yourpassword';  # 创建用户
```

因为使用`mysql -uusername -p`连入数据库时，默认参数`-hlocalhost`，则数据库认为你是通过127.0.0.1连入的。会疯狂报身份验证的错。此时应该使用`mysql -uusername -hlocalhost -p`去连入。

是的，你没看错。`localhost`并不等于`127.0.0.1`

### 3.指定数据库打开地址

如下，指定用户使用的数据库

``` shell
grant all privileges on databasename.* to 'username'@'127.0.0.1';
```

则只有当用户通过127.0.0.1登录数据库时才能看到databasename这个数据库

### 4.修改密码

直接设置表密码

``` shell
UPDATE user SET password=password('<yourpassword>') WHERE user='root';
flush privileges;
```

### 5.开启远程访问

``` bash
nano /etc/mysql/mariadb.conf.d/50-server.cnf  # 该文件中，指定只监听本地端口，所以要注释掉 bind-address 项
```