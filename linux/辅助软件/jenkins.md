# jenkins

## 安装

### 设置源安装法

```bash
wget -O /etc/yum.repos.d/jenkins.repo     https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
yum install jenkins
```

### 下载rpm包安装法

下载网址：https://mirrors.tuna.tsinghua.edu.cn/jenkins/

```bash
wget https://mirrors.tuna.tsinghua.edu.cn/jenkins/redhat/jenkins-2.274-1.1.noarch.rpm  # 下载
yum install -y jenkins-2.274-1.1.noarch.rpm  # 安装
```

jenkins默认开机启动，不需要重复设置

### 报错

#### 重复安装

```
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
stat: cannot stat ‘/var/cache/jenkins’: No such file or directory
stat: cannot stat ‘/var/log/jenkins’: No such file or directory
stat: cannot stat ‘/var/lib/jenkins’: No such file or directory
error: %pre(jenkins-2.274-1.1.noarch) scriptlet failed, exit status 1
Error in PREIN scriptlet in rpm package jenkins-2.274-1.1.noarch

  Verifying  : jenkins-2.274-1.1.noarch                                                                                                 1/1

Failed:
  jenkins.noarch 0:2.274-1.1

Complete!
```

#### 解决

[参考](https://blog.csdn.net/baidu_33864675/article/details/105015462)

执行以下语句，看看执行结果

```bash
rpm --scripts -qp jenkins-2.274-1.1.noarch.rpm > jenkins.log
```

查看`/etc/sysconfig/jenkins`是否存在，存在则删除。

然后在重新安装。



## 更换清华插件源

### 在web中修改更新源

Manage Jenkins -> Manage Plugins -> Advanced

将`Update Site`的URL改为：

``` url
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
```

或者改为：

```
http://mirror.xmission.com/jenkins/updates/update-center.json
```

点击`submit`，再点击`Check now`。此操作会更新default.json文件

### 在ssh中修改default.json文件

由于是用yum安装，所以配置为`/var/lib/jenkins/updates/default.json`用其他方法安装jenkins，可能配置文件不在这个位置



将`http://www.google.com`换为`http://www.baidu.com/`

将`updates.jenkins.io/download`换为`mirrors.tuna.tsinghua.edu.cn/jenkins`


``` bash
# 可以直接执行以下的替换命令

sed -i 's#updates.jenkins.io/download/plugins#mirrors.tuna.tsinghua.edu.cn/jenkins/plugins#g' default.json && sudo sed -i 's#www.google.com#www.baidu.com#g' default.json
```



### 重启jenkins

```bash
systemctl restart jenkins  # 以非rpm方式安装，可能不是这个命令
```

## 插件

[promoted builds](https://plugins.jenkins.io/promoted-builds)：手动可选择执行命令

[Maven Integration](https://plugins.jenkins.io/maven-plugin)：maven项目构建

[Git plugin](https://plugins.jenkins.io/git)：拉取git的代码

## 凭据

### 添加凭据

Manage Jenkins -> Manage Credentials -> jenkins（Stores scoped to下） -> 全局凭据 (unrestricted) -> Add Credentials

## 项目配置

### 执行脚本的key

ssh到jenkins服务器。

修改/etc/passwd文件，使jenkins可以登录：

`jenkins:x:998:996:Jenkins Automation Server:/var/lib/jenkins:/bin/false`改为`jenkins:x:998:996:Jenkins Automation Server:/var/lib/jenkins:/bin/bash`

执行命令，创建密钥：

```bash
su jenkins
ssh-keygen  # 一路回车
exit
```

etc/passwd文件改回去。

```bash
systemctl restart jenkins  # 重启jenkins
```

如此，就可以直接在脚本中执行shell命令了

### maven

maven是使用yum安装的。

```bash
wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
yum install apache-maven
```



Clobal Tool Configuration -> Maven installations -> Add Maven

`name` 填入 maven

`MAVEN_HOME` 填入 /usr/share/apache-maven

### 加载环境变量/etc/profile

`/etc/sysconfig/jenkins`末尾增加`source /etc/profile`，然后重启Jenkins服务

### ssh指纹认证

若开启ssh指纹认证，则会报告如下错误

```
Host key verification failed
```

此时可以编辑`/etc/ssh/ssh_config`，添加`StrictHostKeyChecking no`。

关闭jenkins部署机器的指纹认证，会引发一定的安全问题。，可能遭受中间人攻击。

若是不关闭，则需要第一次连接机器时确认一次，以将指纹加入`~/.ssh/known_hosts`中。

### node

```bash
wget https://cdn.npm.taobao.org/dist/node/v8.12.0/node-v8.12.0-linux-x64.tar.xz
npm i -g @tarojs/cli@1.3.18  # 指定taro的版本下载
```

## 项目迁移

### jobs

./mv_jenkins.sh /var/lib/jenkins/jobs /opt/jenkins_new

```bash
#!/bin/bash

job_list=$(ls $1)

for job in $job_list
do
echo "复制"$job;
mkdir $2/$job;
cp $1/$job/config.xml $2/$job;

if [ -d "$1/$job/promotions" ];
then
cp -r $1/$job/promotions $2/$job
fi
done

chown -R jenkins.jenkins $2
```

## 自动构建

[参考](https://blog.csdn.net/xlgen157387/article/details/76216351)

### jenkins的操作

在jenkins中安装插件：[Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger)

在项目的`构建触发器`中勾选`Generic Webhook Trigger`

如下参数需要填写：

```
Generic Webhook Trigger
	Post content parameters
		Variable：ref
		Expression：$.ref
		单选：JSONPath
	Token：o8hKE1nRmJk
	Optional filter
		Expression：^(refs/heads/prod)
		Text：$ref
```

### gitlab的操作

在项目的`Settings` -> `Webhooks`页面操作

依照jenkins的提示，URL一栏中填入（以下的JENKINS_URL需要替换为jenkins的IP）：

```
http://JENKINS_URL/generic-webhook-trigger/invoke
```

Secret Token一栏填
```
o8hKE1nRmJk
```

选择触发事件，点击add按钮添加，然后可以开始调试。

可以在web页面手动发起各种时候，观察jenkins是否按预想中自动构建