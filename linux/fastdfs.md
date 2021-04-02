# fastdfs

## 简介

开源高性能的分布式文件系统。

storage：存储服务器

tracker：跟踪服务器

1、storage定期沟通tracker

2、client向tracker发送上传文件请求

3、tracker分配group，并查询可用的storage，向client回复信息

4、client直接请求分配下来的storage，storage为其生成一个fileid

5、client发送文件数据，storage接收文件，存入磁盘，向client返回文件信息

6、storage将文件同步到同group的storage

## 安装目标

在本机上安装fastdfs、nginx，能够使用防盗链

环境为 centos7

## 安装过程

安装编译所需：

``` bash
yum install pcre pcre-devel zlib zlib-devel openssl openssl-devel gcc
```

## 安装libfastcommon

libfastcommon和fastdfs编译有关。不安装，则无法编译

项目地址：<https://github.com/happyfish100/libfastcommon.git>

``` bash
# 下载
wget https://github.com/happyfish100/libfastcommon/archive/V1.0.41.tar.gz
tar -xf V1.0.41.tar.gz
cd libfastcommon-1.0.41

# 编译、安装
./make.sh
./make.sh install
```

## 安装fastdfs

要求 `/data/fdfs` 已经建立，否则启动将报错

``` bash
# 下载、解压
wget https://github.com/happyfish100/fastdfs/archive/V6.03.tar.gz
tar -xf V6.03.tar.gz
cd fastdfs-6.03

# 编译、安装
./make.sh
./make.sh install
```

配置文件会存储在 /etc/fdfs 路径下。按照版本的不同，可能配置文件不会复制进来。需要在源代码的文件夹（fastdfs-6.03/conf）下将文件复制出来。

``` bash
# 工作目录为源代码目录
cp ./conf/* /etc/fdfs
```

编辑配置文件 /etc/fdfs/tracker.conf

注意以下几项

``` conf
# 该服务运行端口
port=22122

# 日志文件的存放路径
base_path=/data/fdfs

# web服务的端口
http.server_port=80

# 修改服务启动使用的用户和用户组。创建的文件属主和属组会根据这个来
run_by_group = www
run_by_user = www
```

编辑配置文件 /etc/fdfs/storage.conf

注意以下几项

``` conf
# 该服务运行端口
port=23000

# 日志文件的存放路径
base_path=/data/fdfs

# 数据文件存放路径
store_path0=/data/fdfs/data

# 分组的时候，组名
group_name=group1

# 配置公网IP
tracker_server=公网IP:22122

# web服务的端口
http.server_port=80

# 修改服务启动使用的用户和用户组。创建的文件属主和属组会根据这个来
run_by_group = www
run_by_user = www
```

编辑配置文件 /etc/fdfs/client.conf

该文件和是用来运行测试用的

``` conf
# 日志文件的存放路径
base_path=/data/fdfs

# 同storage.conf的配置
tracker_server=公网IP:22122
```

启动

``` bash
/usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf start  # 启动tracker
/usr/bin/fdfs_storaged /etc/fdfs/storage.conf start  # 启动storage
ps -ef | grep -E "tracker|storage"  # 检查是否启动成功
netstat -nltpu | grep -E "tracker|storage"  # 检查端口是否监听成功
```

若启动失败。则去 `/data/fdfs` 文件夹下去寻找日志。

## 安装nginx

``` bash
./configure --add-module=/opt/package/fastdfs-nginx-module/src/
make
make install
```

## nginx的fdfs模块编译

### 未按序编译fdfs和common

报错

```
In file included from /opt/fastdfs-nginx-module-1.22/src//ngx_http_fastdfs_module.c:6:0:
/opt/fastdfs-nginx-module-1.22/src//common.c:21:31: fatal error: fastcommon/logger.h: No such file or directory
 #include "fastcommon/logger.h 
```

解决：先编译fdfs和common即可

