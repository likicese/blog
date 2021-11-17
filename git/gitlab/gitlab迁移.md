# gitlab迁移

## 前言

由于项目需要，gitlab要从A机器迁移到B机器。

## 迁移准备

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

## 迁移

在旧机器上执行

``` bash
gitlab-rake gitlab:backup:create  # 生成备份文件
```