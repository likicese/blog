# yum

## yum命令

```bash
yum repolist all  # 查看所有repo源
yum list mysql-community* --showduplicates | sort -r  # 查看mysql软件可安装版本。后边用管道符排序
yum install mysql-community-server-8.0.19-1.el7  # 安装特定版本mysql。注意，当有依赖项的时候，会自动找复合条件的最高版本。此时可能出现版本冲突，需要一步步指定低版本
yum install --downloadonly mysql-community-server  # 先下载到本地，需要的时候可以直接install安装

yum clean all  # 清除缓存目录下的软件包和旧headers
yum info vim  # 查看vim的信息
yum update vim  # 指定vim更新
```
## rpm

``` bash
rpm -e --nodeps  # 强制卸载软件，不检查依赖
```

## 拓展包安装

```bash
yum -y install  epel-release  # 该包为拓展包，安装许多软件必不可少
```

## 问题

### 数据库损坏

报错：

```
error: rpmdb: BDB0113 Thread/process 29633/139682663896896 failed: BDB1507 Thread died in Berkeley DB library
error: db5 error(-30973) from dbenv->failchk: BDB0087 DB_RUNRECOVERY: Fatal error, run database recovery
error: cannot open Packages index using db5 -  (-30973)
error: cannot open Packages database in /var/lib/rpm
CRITICAL:yum.main:

Error: rpmdb open failed
```

解决：

```bash
rm -rf /var/lib/rpm/__db*
rpm --rebuilddb
```

