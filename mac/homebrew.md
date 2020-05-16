# homebrew

## 安装

官方网址：https://brew.sh

可能会遇上 githubusercontent.com 无法访问的问题。

此时需要主动映射IP。

通过 https://site.ip138.com/ 可以查询IP

然后修改hosts文件，加入如下语句。我找到的是以下IP

``` txt
151.101.76.133 githubusercontent.com
```

修改IP后，执行以下命令等待即可

``` bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
