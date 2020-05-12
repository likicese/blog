# linux命令

## host

``` shell
hostnamectl set-hostname hostName  # 设置主机名
```

## 密码

随机密码
``` shell
DB_PASSWORD=`cat /dev/urandom | tr -dc A-Za-z0-9 | head -c 24`  # 生成随机密码
echo -e "\033[31m 你的数据库密码是 $DB_PASSWORD \033[0m"  # 打印出来
```

## 公私钥

``` shell
ssh-keygen  # 重新生成本机公钥和私钥
```

## 查看信息

``` shell
cat /etc/*-release
```

## wget

某些网站设置检查，只有通过浏览器才能下载文件。加入下列参数，即可模拟浏览器

``` shell
wget --no-check-certificate --user-agent="Mozilla/5.0 (X11;U;Linux i686;en-US;rv:1.9.0.3) Geco/2008092416 Firefox/3.0.3" https://storage.googleapis.com/harbor-releases/release-1.7.0/harbor-offline-installer-v1.7.5.tgz
```

## curl

参数说明：

-m 最大处理时长
-s 不打印加载进度等信息
-o 指定输出文件名称
-w 格式化输出
-I 仅仅返回头部信息

``` bash
curl baidu.com/path/show -I -w %{http_code} -o /dev/null -s -m 5  # 获取网页状态码，最多等5秒
```

## wget

``` bash
wget --http-user=userName --http-passwd=passWord https://test.com/fileName.txt  # 用于度过http中的auth验证
```

## ssh

``` bash
ssh -o stricthostkeychecking=no  # 首次登陆免输入yes
``` 