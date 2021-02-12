# sed

## 文本问题

``` bash
sed -i 's/\r$//' <fileName>  # 出现  '\r': command not found 时，用该命令去除win下特殊的换行符号
sed -n '5,10p'  test.txt  # 输出第5到第10行之间的内容
sed '5,10d'  test.txt  # 删除第5到第10行之间的内容

sed 's/a/b/2' 1.txt  # 用b替换第二次出现的a
sed -n '/5/p' 1.txt  # 只输出第五行，避免sed默认输出全部
```

## 指定位置插入文本

```bash
sed -ir "/aaaaaaa/ a bbbbbbb" <fileName>  # 在aaaaaaa后边插入bbbbbbb。-r参数为支持正则
sed -ir "/aaaaaaa/ i bbbbbbb" <fileName>  # 在aaaaaaa前边插入bbbbbbb。-r参数为支持正则
```

## 删除

```bash
sed '/2/d' <fileName>  # 删除包含“2”的行
```

