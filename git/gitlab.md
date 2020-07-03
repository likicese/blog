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