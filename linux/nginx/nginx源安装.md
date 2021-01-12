# nginx源安装

## 添加yum源

参考网址：http://nginx.org/en/linux_packages.html

vim `/etc/yum.repos.d/nginx.repo`

``` repo
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
```

执行`yum install nginx` 