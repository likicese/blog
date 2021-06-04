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

