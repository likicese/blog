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
```

