# loki

## 报错解决

### 日志数量太多导致无法接收

报错：server returned HTTP status 429 Too Many Requests (429): Ingestion rate limit exceeded

解决：

```
config:
  limits_config:
    ingestion_rate_strategy: local
    # 每个用户每秒的采样率限制
    ingestion_rate_mb: 15
    # 每个用户允许的采样突发大小
    ingestion_burst_size_mb: 20
```

