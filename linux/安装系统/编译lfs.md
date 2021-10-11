# 编译lfs

## 准备

安装工具

```
dnf install -y texinfo gcc-c++ m4 bison
```

```
dnf install mpfr-devel
```

注意，texinfo在powertools仓库中，需要手动开启

```bash
sed -i 's/enabled=0/enabled=1/g'/etc/yum.repos.d/CentOS-Stream-PowerTools.repo
```

