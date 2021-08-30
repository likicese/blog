# mysql5

mysql5的操作和mysql8的操作略有不同

``` mysql
grant all on test_db.* to 'admin'@'192.168.%.%';  # 授权语句，相比mysql8缺少privileges
flush privileges;  # 刷新权限表。mysql5必须刷新一下，才能正确授权。mysql8不需要。
```