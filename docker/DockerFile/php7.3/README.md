# 关于本DockerFile

## 起源

想配置Lychee，搭建一个相册。发现需要php环境。再三考虑，决定在Docker中完成PHP的搭建，以避免污染外部环境。

## 版本

debian作为镜像的基础系统，PHP是7.3的，nginx是1.17.8

## 操作

在已经装了docker的机器上，下载本文件夹下其他三个文件，置于同一文件夹。

进入该文件夹，执行以下命令。

注意，命令后边那个 `.` 符号，千万别丢。

``` bash
docker build -t php73:1.0 .
```

构建完毕后，执行以下命令启动镜像,并且挂载2个目录到外边，并且将宿主机的端口8011映射到容器端口80

``` bash
mkdir /data/nginx-php/logs/
mkdir /data/nginx-php/html/

docker run --name php73 -v /data/nginx-php/logs/:/usr/local/nginx/logs/ -v /data/nginx-php/html/:/usr/local/nginx/html -p 8011:80 -dit php73:1.0
```

## 安装Lychee

将下载的Lychee包解压缩到 `/data/nginx-php/html/` 文件夹，执行以下命令，改变文件属主，让nginx可以访问。

``` bash
chown www-data:www-data -R /data/nginx-php/html/

# 重命名Lychee
mv Lychee-v3.2.16 lychee
```

在浏览器中打开
http://宿主机IP:8011/lychee

## 数据库

打开lychee后，他会让你输入数据库地址、用户名、密码。若数据库安装在宿主机上，数据库地址即容器的网关IP。

请注意。数据库应该允许外网访问。因为这不是装在同一容器中。mariadb默认不允许外网访问，应该进行特殊的设置。