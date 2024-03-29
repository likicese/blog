# 自建yum源

## 前言

192.168.1.2：rpm仓库地址

192.168.1.3：需要使用仓库的机器

以创建mysql的rpm仓库为例

## 建立http文件服务器

本处为使用nginx搭建

安装nginx后，配置文件添加：

```
server {
    listen 80;
    charset utf-8;
    autoindex on;
    autoindex_exact_size on;
    autoindex_localtime on;
    location / {
    	alias /srv/www/;
    }
}
```

## 创建repo仓库

```bash
MYSQL_FILE='mysql-8.0.25-1.el7.x86_64.rpm-bundle.tar'

cd /srv/www/
wget https://cdn.mysql.com//Downloads/MySQL-8.0/${MYSQL_FILE}  #　下载mysql
tar -xf ${MYSQL_FILE}
yum install createrepo
createrepo .  # 创建仓库
```

## 添加仓库

在192.168.1.3机器上操作

```
REPO_NAME='mysql'
REPO_HOST='192.168.1.2'

cat >> /etc/yum.repos.d/${REPO_NAME}.repo  < EOF
[${REPO_NAME}]
name=this is private repo
baseurl=http://${REPO_HOST}/
gpgcheck=0
enabled=1
EOF

yum clean all; yum update
```



若是192.168.1.2需要使用yum源，因为在本地，则不需要通过http传输。把`baseurl=http://${REPO_HOST}/`改为`baseurl=file:///srv/www/`即可

## 更新仓库

例如现获得新的xxx.rpm，要加入该仓库

在192.168.1.2机器上操作

```
cd /srv/www/
wget http://xxx.com/xxx.rpm
createrepo --update .
```



在192.168.1.3机器上操作

```
yum clean all; yum update
```
