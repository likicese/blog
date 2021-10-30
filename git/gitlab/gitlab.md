# gitlab

## 环境

linux版本：centos8

IP地址：192.168.1.3

gitlab版本：[gitlab-ce-13.1.2-ce.0.el8.x86_64](https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/8/gitlab-ce-13.1.2-ce.0.el8.x86_64.rpm)

gitlab其他版本查看网址：https://packages.gitlab.com/gitlab/gitlab-ce

gitlab-runner：gitlab-runner-13.1.1-1.x86_64

gitlab-runner安装参考网址：https://mirrors.tuna.tsinghua.edu.cn/help/gitlab-runner


## 安装gitlab（源安装）



## 安装gitlab（rpm安装）

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

## gitlab-runner的使用

先去gitlab的web页面，从  项目 -> settings -> CI/CD -> Runners

在 `Set up a specific Runner manually` 一栏，获取URL和token

本例中，获取的URL是 “http://192.168.1.3:8081” 获取的token是 “ADEAFA_BBBBB-dddddddd”

输入 `gitlab-runner register`

按照提示信息输入。交互界面如下。

``` bash
Runtime platform                                    arch=amd64 os=linux pid=14166 revision=6fbc7474 version=13.1.1
Running in system-mode.

Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/):
http://192.168.1.3:8081
Please enter the gitlab-ci token for this runner:
ADEAFA_BBBBB-dddddddd
Please enter the gitlab-ci description for this runner:
[localhost]: gitlab-runner
Please enter the gitlab-ci tags for this runner (comma separated):
m
Registering runner... succeeded                     runner=5XWBBuz-
Please enter the executor: docker-ssh, shell, ssh, docker+machine, kubernetes, custom, parallels, virtualbox, docker-ssh+machine, docker:
shell
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
```

解释一下如上的交互界面。

1. URL
2. token
3. runner的名字
4. runner的标签。在写.gitlab-ci.yml的时候会用到
5. runner执行job的时候用到的控件。此处设定为shell

刷新项目的 settings -> CI/CD ，可以看到有个新的runner注册成功

## 编写.gitlab-ci.yml

在项目的根目录下，编写 `.gitlab-ci.yml` 文件，文件内容如下

``` yml
# 定义阶段 stages
stages:
  - build
  - deploy

job1 - 开始构建:
  # 开始之前需要安装依赖
  stage: build
  tags:
    - m
  script:
    - echo "构建完毕"
    - pwd

job2 - 开始发布:
  stage: deploy
  tags:
    - m
  script:
    - echo "发布完毕"
```

因为runner在注册的时候定义了tags，其值为“m”。所以在yml文件中，需要tags为“m”执行的runner需要显式定义

以上定义了两个任务。在代码变动的时候，会按序执行job。

可以试着更改并push代码，然后在项目的web页面中，左侧部位，CI/CD可以看到job的执行结果

## 登录web页面限制

需求：不允许192.168.1.100访问gitlab登录页面

编辑文件：/var/opt/gitlab/nginx/conf/gitlab-http.conf，加入如下内容：

``` config
location /admin {
    allow 192.168.1.100/32;
    deny all;
    proxy_cache off;
    proxy_pass  http://gitlab-workhorse;
  }

  location /users {
    allow 192.168.1.100/32;
    deny all;
    proxy_cache off;
    proxy_pass  http://gitlab-workhorse;
  }
```

保存编辑后的文件。执行以下命令，重启gitlab的nginx

``` bash
gitlab-ctl hup nginx
```