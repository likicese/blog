# ReadTimedOut

## 参考

[应用频繁报出cause java.net.SocketTimeoutException: Read timed out怎么办 (kujiale.com)](https://tech.kujiale.com/ying-yong-pin-fan-bao-chu-cause-java-net-sockettimeoutexception-read-timed-outzen-yao-ban/)

[基于 Nginx 实现 10万+ 并发，你应该做的 Linux 内核优化 - 开发者头条 (toutiao.io)](https://toutiao.io/posts/me0nza/preview)

## 排查

```
netstat -s | egrep "listen|LISTEN"
ss -lnt
```

## 解决

```
echo -e "net.core.somaxconn = 16384\nnet.ipv4.tcp_max_syn_backlog = 8192" >> /etc/sysctl.conf
sysctl -p
```

系统参数改变后，应用也应重启，才能生效