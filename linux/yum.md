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

