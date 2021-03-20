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

