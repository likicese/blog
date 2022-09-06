# http的basic验证

##  安装

``` bash
yum install -y httpd
```

## 命令

``` bash
htpasswd -cb /etc/nginx/auth_basic admin cFhK6LVDZHfOgWfXYQX3  # 创建新用户放在新文件中
htpasswd -b /etc/nginx/auth_basic user1 cFhK6LVDZH  # 增加一个新用户
htpasswd -D /etc/nginx/auth_basic user1  # 删除用户user1
```

第二种生成方式

```bash
printf "user1:$(openssl passwd -crypt cFhK6LVDZH)\n" >> /etc/nginx/auth_basic
```

## 在nginx中使用

可以用于`http，server，location`中

``` conf
server {
    auth_basic "请输入用户名和密码";
    auth_basic_user_file /etc/nginx/auth_basic;
}
```