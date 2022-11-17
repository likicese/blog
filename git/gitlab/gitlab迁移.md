# gitlab迁移

## 前言

由于项目需要，gitlab要从A机器迁移到B机器。

旧机器（A）：192.168.1.11
新机器（B）：192.168.1.12

[参考](https://blog.csdn.net/GongMeiyan/article/details/105127409)

## 迁移准备

查询A机器的版本

``` bash
rpm -q gitlab-ee  # 查询A机器的版本，由输出可获知，版本是：gitlab-ee-14.0.11-ee.0.el7.x86_64
```

在B机器安装相同的版本

``` bash
yum install -y curl policycoreutils-python openssh-server
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
yum install gitlab-ee-14.0.11-ee.0.el7.x86_64  # 版本参数由以上可查询出来
```

## 迁移

### 旧机器

``` bash
gitlab-rake gitlab:backup:create  # 生成备份文件，文件存储于/var/opt/gitlab/backups
```

会弹出如下提示：

``` txt
Warning: Your gitlab.rb and gitlab-secrets.json files contain sensitive data 
and are not included in this backup. You will need these files to restore a backup.
Please back them up manually.
```

大意是，gitlab.rb和gitlab-secrets.json是敏感文件，需要手动备份。两个文件存放在/etc/gitlab/文件夹中

### 新机器

需要备份的文件：

/etc/gitlab/gitlab.rb 配置文件

/var/opt/gitlab/nginx/conf nginx配置文件

/etc/postfix/main.cfpostfix 邮件配置备份

``` bash
OLD_IP='192.168.1.11'
scp root@${OLD_IP}:/var/opt/gitlab/backups/1636937419_2021_11_10_14.0.11-ee_gitlab_backup.tar /var/opt/gitlab/backups/
chown git:git /var/opt/gitlab/backups/1636937419_2021_11_10_14.0.11-ee_gitlab_backup.tar
scp root@${OLD_IP}:/etc/gitlab/* /etc/gitlab/

gitlab-ctl reconfigure # 启动gitlab，会创建相应的服务，耗时约7分钟
```

恢复备份

``` bash
# 停止服务
gitlab-ctl stop unicorn
gitlab-ctl stop sidekiq

gitlab-rake gitlab:backup:restore BACKUP=1636937419_2021_11_10_14.0.11-ee  # 2.9GB的备份文件，耗时约40分钟

# 在恢复过程中需要输入2次yes

gitlab-ctl start
gitlab-ctl status

# 恢复nginx配置文件
scp root@${OLD_IP}:/var/opt/gitlab/nginx/conf/* /var/opt/gitlab/nginx/conf
gitlab-ctl hup nginx
```