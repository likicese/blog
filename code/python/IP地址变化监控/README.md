# README

## 说明

此脚本为监控脚本。主要是监控外网ip是否发生变化。

请主动在目录`/home/pi/script/external_ip_monitor/`下创建ip.txt文件。当文件ip地址发生变化的时候，会自动更新该文件。

以下语句仅为示例

``` bash
mkdir -p /home/pi/script/external_ip_monitor/
echo 8.8.8.8 > /home/pi/script/external_ip_monitor/ip.txt
```

## 创建定时任务

``` bash
crontab -e  # 编辑定时任务
```

加入如下语句

*/5 * * * * /home/pi/script/external_ip_monitor/monitor_ip.py >> /home/pi/script/external_ip_monitor/monitor_ip.log