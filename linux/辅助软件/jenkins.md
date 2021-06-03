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