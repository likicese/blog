# elasticsearch

## 报错

### 分区文件读取错误

报错：

``` info
[2021-01-04T16:32:51,657][ERROR][o.e.g.GatewayMetaState   ] [node-3] failed to read local state, exiting...
org.elasticsearch.ElasticsearchException: java.io.IOException: failed to read [id:69, legacy:false, file:/var/lib/elasticsearch/nodes/0/indices/aFd6K15nR62PaaKrBjuXZQ/_state/state-69.st]
```

解决：

删除旧的分区文件

``` bash
rm -rf /var/lib/elasticsearch/nodes/0/indices/*
```