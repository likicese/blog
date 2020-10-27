# plumbing commands

## git hash-object

```bash
echo "test git" | git hash-object -w --stdin  # 将来自管道的文字写入git的数据库
```

