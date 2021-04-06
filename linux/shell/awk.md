# awk

## 语法

```bash
awk '{pattern + action}' <fileName>
```

以行为处理单位

## 命令

```bash
awk '{print "'\''" $0}'  # 单引号的输出
awk -F ; '{print $1}'  # 以符号;分割每一行字符串，然后输出第一列
echo "aaa" | awk 'BEGIN{print "bbb"} {print} END{print "ccc"}'  # 三个动作。先打印bbb，再打印aaa，最后打印ccc
awk '{print $NF}'  # 输出每行最后一个字段
```

## 参数

```
$0 所有列
$1 第一列
NF 字段数量
FS 分隔符，相当于-F参数
NR 已读行数
OFS 输出域分隔符
```

