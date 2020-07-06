# gitlab

## 环境

linux版本：centos8

IP地址：192.168.1.3

gitlab版本：[gitlab-ce-13.1.2-ce.0.el8.x86_64](https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/8/gitlab-ce-13.1.2-ce.0.el8.x86_64.rpm)

gitlab其他版本查看网址：https://packages.gitlab.com/gitlab/gitlab-ce

gitlab-runner：gitlab-runner-13.1.1-1.x86_64

gitlab-runner安装参考网址：https://mirrors.tuna.tsinghua.edu.cn/help/gitlab-runner


## gitlab安装

``` bash
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/8/gitlab-ce-13.1.2-ce.0.el8.x86_64.rpm/download.rpm  # 下载安装包
dnf localinstall gitlab-ce-13.1.2-ce.0.el8.x86_64.rpm/download.rpm
```

编辑 /etc/gitlab/gitlab.rb 文件，找到`external_url`修改为`external_url 'http://192.168.1.3:8081'`

``` bash
gitlab-ctl reconfigure  # 加载配置
gitlab-ctl restart  # 重启gitlab。首次安装的时候，会初始化很多东西，会卡一段时间

# 开放防火墙
firewall-cmd --zone=public --add-port=8081/tcp --permanent
firewall-cmd --reload
```


## gitlab修改root密码

强制修改root密码。修改后，即可在web页面用root用户登陆

``` bash
gitlab-rails console  # 访问数据库,会卡约10s才能加载出来

# 以下操作均在rails的命令行内
user = User.where(id:1).first
user.password='12345678'  # 密码要求最短8个字符，密码设为12345678
user.save!
```

## gitlab-runner安装

gitlab-runner可以和gitlab不安装在同一台机器上。

需要保证安装gitlab-runner的机器上，git的版本较新

可以参考网址https://mirrors.tuna.tsinghua.edu.cn/help/gitlab-runner ， 进行安装
``` bash
yum makecache
yum install gitlab-runner -y

systemctl status gitlab-runner  #确定gitlab-runner已经运行
```

## git安装

centos默认的git比较老，约为1.18版本。

若是不安装新git，在使用gitlab-runner跑任务的时候，会提示 “fatal: git fetch-pack: expected shallow list”

``` bash
rpm -e --nodeps git  # 卸载老git
rpm -e --nodeps perl-Git  # 卸载会冲突的依赖。这是在安装gitlab-runner的时候带进来的依赖。

curl https://setup.ius.io | sh  # 安装ius源
yum makecache
yum install git224  # 安装2.24版本的git
```