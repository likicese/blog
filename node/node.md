# node

## 安装

下载：https://nodejs.org/en/download/

将压缩包解压到/usr/local/

做软链接 `ln -s node-v12.18.3-linux-x64/ node`。

在 `/etc/profile` 文件中加入如下文字

``` txt
export NODE=/usr/local/node/bin
export PATH=${NODE}:${PATH}
```

## 命令

``` bash
npm install -–unsafe-perm xx  # 强制用root用户执行当前的安装命令。npm不允许用root运行。当使用root运行时，会自动切换到nobody用户。碰到一些需要权限的操作时，则权限不够。
```