# sed

## 文本问题

``` bash
sed -i 's/\r$//' <fileName>  # 出现  '\r': command not found 时，用该命令去除win下特殊的换行符号
```

## 指定位置插入文本

```bash
sed -ir "/aaaaaaa/ a bbbbbbb" <fileName>  # 在aaaaaaa后边插入bbbbbbb。-r参数为支持正则
sed -ir "/aaaaaaa/ i bbbbbbb" <fileName>  # 在aaaaaaa前边插入bbbbbbb。-r参数为支持正则
```

