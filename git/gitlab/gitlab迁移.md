# gitlab迁移和升级

## 迁移

### 前言

由于项目需要，gitlab要从A机器迁移到B机器。

迁移时，A机器和B机器必须安装相同版本

### 迁移准备

查询A机器的版本

``` bash
rpm -q gitlab-ee  # 查询A机器的版本，由输出可获知，版本是：gitlab-ee-13.2.6-ee.0.el7.x86_64
```

在B机器安装相同的版本

``` bash
yum install -y curl policycoreutils-python openssh-server
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
yum install gitlab-ee-13.2.6-ee.0.el7.x86_64  # 版本参数由以上可查询出来
```

### 开始迁移

在旧机器上执行

``` bash
gitlab-rake gitlab:backup:create  # 生成备份文件
```

## 升级

不能跨版本升级，需按照官网指示，小版本逐步升级。

[Upgrading GitLab | GitLab](https://docs.gitlab.com/ee/update/index.html#upgrade-paths)

以本次为例，本地版本为14.0.11，需要升级到15.1.0，则升级历程如下：

```
14.0.11 -> 14.0.12 -> 14.6.2 -> 14.9.4 -> 14.10.3 -> 15.0.0 -> 15.1.0
```

### 开始升级

```bash
# 备份
rpm -q gitlab-ee  # 查询本地版本
gitlab-rake gitlab:backup:create  # 备份

yum install -y gitlab-ee-14.0.12
```

