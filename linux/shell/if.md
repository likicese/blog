# if

## 比较语句

整数

``` txt
-eq 整数相等
-ne 整数不等
-gt A大于B
-lt A小于B
-ge A大于或等于B
-le A小于或等于B
```

字符串

``` txt
== 等于
!= 不等于
> 大于
< 小于
-z 长度为零
-n 长度非零
```

文件

``` txt
-e 文件存在
-f 文件为普通文件
-d 路径存在且为目录
-r、-w、-x 文件对用户可读、可写、可执行
```

## 示例

``` bash
if [ A -eq B];then
    echo "A等于B"
elif [ A -gt B];then
    echo "A大于B"
fi
```