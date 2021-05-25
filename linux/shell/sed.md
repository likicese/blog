# sed

## 文本问题

``` bash
sed -i 's/\r$//' <fileName>  # 出现  '\r': command not found 时，用该命令去除win下特殊的换行符号
sed -n '5,10p'  test.txt  # 输出第5到第10行之间的内容
sed '5,10d'  test.txt  # 删除第5到第10行之间的内容
sed 's/a/b/2' 1.txt  # 用b替换第二次出现的a
sed -n '/5/p' 1.txt  # 只输出第五行，避免sed默认输出全部。诀窍在于-n参数
sed -n 's/a/b/p' 1.txt  # 只输出修改过的行
sed '/^a/s/f/K/g' 1.txt  # 匹配以a开头的行，将f换成K
sed '20,30d' 1.txt  # 删除20~30行
sed 's/a../&kkk/g' 1.txt  # &表示之前匹配的字符。即在a..后边，接上kkk三个字符
echo "abc" | sed 's/\(a\).*/b \1/g'  # 输出结果为“b a”，其将匹配到的“a”暂存于“\1”内，在b后边输出\1
sed '3c\kkkkkkkk' 1.txt  # 将第3行替换为kkkkkkkk
```

## 指定位置插入文本

```bash
sed -ir "/aaaaaaa/ a bbbbbbb" <fileName>  # 在aaaaaaa后边插入bbbbbbb。-r参数为支持正则
sed -ir "/aaaaaaa/ i bbbbbbb" <fileName>  # 在aaaaaaa前边插入bbbbbbb。-r参数为支持正则
```

## 删除

```bash
sed '/2/d' <fileName>  # 删除包含“2”的行
sed '/1/,/5/d'  # 删除第1~5行
sed '/^\s*$/d' <fileName>  # 删除纯空行
```

