# grep

## 命令

```bash
grep "aa" -A 10 1.txt  # 查看“aa”字符串后10行，-B为前10行，-C为前后各10行
grep "aa" -v 1.txt  # 不输出有aa的行
grep -c 1.txt  # 计算匹配的数量
grep -n 1.txt  # 显示行数
```

## 参数

```
-o 只显示匹配的部分
-c 计算符合搜索条件的行数
-f 指定正则表达式文件。文件中可以有多个表达式
-h 不显示文件名
-H 显示文件名
-i 忽略大小写
-n 列出该列编号
-E 相当于使用egrep
-v 对结果进行反转
--exclude 排除某个文件
-s 取消错误信息的显示
```

