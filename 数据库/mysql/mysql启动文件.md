# mysql启动文件

## 启动文件

编辑文件`/etc/my.cnf`

``` conf
default_authentication_plugin=mysql_native_password  # 5.7默认的加密方式
default_authentication_plugin=caching_sha2_password  # 8.0默认的加密方式
```