# yum操作

## repo

```bash
yum repolist all  # 查看所有repo源
yum packageName list  --showduplicates | sort -r  # 查看软件可安装版本。后边用管道符排序
sudo yum install packageName-<VERSION>  # 安装特定版本软件
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

