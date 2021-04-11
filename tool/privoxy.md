# privoxy

这是个代理工具，能将socks5转为http

## windows

[下载](https://sourceforge.net/projects/ijbswa/files/Win32/)

选择zip压缩包下载。

下载后解压，编辑config.txt文件，加入如下内容

```config
listen-address 127.0.0.1:8118
forward-socks5 / 127.0.0.1:1080 .
```

保存修改后，启动即可。