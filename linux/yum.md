# yum操作

## 1、repo

```bash
yum repolist all  # 查看所有repo源
yum packageName list  --showduplicates  # 查看软件可安装版本
sudo yum install packageName-<VERSION>  # 安装特定版本软件
```
## rpm

``` bash
rpm -e --nodeps  # 强制卸载软件，不检查依赖
```