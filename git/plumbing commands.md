# plumbing commands

## 命令

```bash
echo "test git" | git hash-object -w --stdin  # 将来自管道的文字写入git的数据库

git cat-file -t 342dfa34a55q  # 输出key为342dfa34a55q的存储类型。
git cat-file -p 342dfa34a55q  # 输出key为342dfa34a55q的内容。

git update-index  # 将文件添加到数据库中
```

