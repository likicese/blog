# crontab

## 安装

``` bash
# dpkg
apt install bcron -y

# rpm
yum install cronie -y
```

## 定时任务

``` bash
10 2 * * * find /opt/logs/ -mtime +7 -exec /usr/bin/rm -f {} \;  # 每天凌晨2点10分，删除7天前的日志
10 2 * * * find /opt/soft/*/logs/ -maxdepth 1 -type f -mtime +7 -exec /usr/bin/rm -f {} \;  # 模糊搜索，不递归，仅找文件。删除7天前日志
```