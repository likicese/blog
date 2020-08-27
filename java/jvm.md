# jvm

## 参考

https://www.cnblogs.com/anyehome/p/9071619.html

## 进程占用资源检查

``` bash
jps -lv  # 查看当前正在运行的java程序
jinfo -flags <pid>  # java进程的pid号。检查进程资源设置情况
```

| 参数 | 意义 | 默认值 |
| --- | ---| ---|
| -XX:MaxHeapSize | 最大可用内存 | 1/4 物理内存 |
