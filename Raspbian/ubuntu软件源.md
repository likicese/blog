# ubuntu

## 软件源

在树莓派上，请使用arm64源。

### 清华源

[清华大学](https://mirror.tuna.tsinghua.edu.cn/help/ubuntu-ports/)

### 华为源

国外用户：

```
deb http://ports.ubuntu.com/ bionic main restricted universe multiverse

deb-src http://ports.ubuntu.com/ bionic main restricted universe multiverse

deb http://ports.ubuntu.com/ bionic-updates main restricted universe multiverse

deb-src http://ports.ubuntu.com/ bionic-updates main restricted universe multiverse

deb http://ports.ubuntu.com/ bionic-security main restricted universe multiverse

deb-src http://ports.ubuntu.com/ bionic-security main restricted universe multiverse

deb http://ports.ubuntu.com/ bionic-backports main restricted universe multiverse

deb-src http://ports.ubuntu.com/ bionic-backports main restricted universe multiverse

deb http://ports.ubuntu.com/ubuntu-ports/ bionic main universe restricted

deb-src http://ports.ubuntu.com/ubuntu-ports/ bionic main universe restricted
```

国内用户可使用华为arm源：

sudo wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-bionic.list

### 中科院源

[ISRC 镜像站 · ISRC - 镜像站 (iscas.ac.cn)](https://mirror.iscas.ac.cn/)