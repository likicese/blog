# nginx编译

## 编译指令

``` bash
cd nginx
./
```

## 编译报错

1. ./configure: error: the HTTP rewrite module requires the PCRE library.

``` bash
apt install libpcre3 libpcre3-dev
```

2. ./configure: error: the HTTP gzip module requires the zlib library.

``` bash
apt install zlib1g-dev
```


4. nginx: [emerg] the "ssl" parameter requires ngx_http_ssl_module

编译https的时候，未添加ssl模块，导致报错。

应该编译时添加该模块

``` bash
./configure --with-http_ssl_module
```

## 添加systemd

新建文件：/usr/lib/systemd/system/nginx.service

添加以下内容

``` txt
[Unit]
Description=nginx, web server
After=network.target nss-lookup.target

[Service]
Type=forking
PIDFile=/usr/local/nginx/logs/nginx.pid
ExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf
ExecStart=/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/bin/kill -s QUIT $MAINPID

[Install]
WantedBy=multi-user.target
```