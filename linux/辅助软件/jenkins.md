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

