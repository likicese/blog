# zookeeper

## 报错

### myid配置文件有误

报错：

Invalid config, exiting abnormally

原因：

myid的文件必须位于dataDir所配置的路径之下，且内容正确。有一台虚拟机经过重启后，myid文件内容丢失，导致报错。

解决：

将myid文件恢复即可。