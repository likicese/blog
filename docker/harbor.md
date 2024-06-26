# harbor

## 安装

### 下载

[harbor release](https://github.com/goharbor/harbor/releases)

可以选择offline版本

[docker-compose](https://github.com/docker/compose/releases)

按目标机器芯片架构选择即可，一般选择`docker-compose-linux-x86_64`

### 修改配置文件

```bash
mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
tar -xf harbor-offline-installer-v2.8.4.tgz
cd harbor
cp harbor.yml.tmpl harbor.yml
```

编辑复制出的文件，注意以下几项。

```yaml
hostname: reg.mydomain.com

# http related config
http:
  # port for http, default is 80. If https enabled, this port will redirect to https port
  port: 80

# https related config
https:
  # https port for harbor, default is 443
  port: 443
  # The path of cert and key files for nginx
  certificate: /your/certificate/path
  private_key: /your/private/key/path

--- 省略

harbor_admin_password: Harbor12345

--- 省略

database:
  # The password for the root user of Harbor DB. Change this before any production use.
  password: root123

--- 省略

data_volume: /data
```

指定`xxx.com`域名后，外层还有nginx作代理故需改变端口，且不希望直接开启https，设置密码后，指定文件存储路径在`/data/harbor`下，所以对应配置文件修改如下

```yaml
hostname: xxx.com

# http related config
http:
  # port for http, default is 80. If https enabled, this port will redirect to https port
  port: 8082

# https related config
# https:
  # https port for harbor, default is 443
  # port: 443
  # The path of cert and key files for nginx
  # certificate: /your/certificate/path
  # private_key: /your/private/key/path

--- 省略

harbor_admin_password: 123456

--- 省略

database:
  # The password for the root user of Harbor DB. Change this before any production use.
  password: 123456

--- 省略

data_volume: /data/harbor
```

### 安装且启动

```bash
./install.sh --with-trivy
```

同时拉起一个镜像扫描器

若安装失败，需停止并删除全部容器，清空数据，再重新安装。避免有残余数据影响功能。

## 配置检测启动状态脚本

服务器频繁重启的话，harbor可能重启不了。此时需要进行检测。

脚本文件`/data/script/check_harbor.sh`内容

``` shell
#!/bin/bash

# 定时语句：*/5 * * * * /data/script/check_harbor.sh >> /data/script/check_harbor.log 2>&1

# 定义 URL
URL="http://127.0.0.1:8082"

# 发送 GET 请求并获取状态码
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

# 如果状态码不是 200，则重启 Docker Compose 中的服务
if [ $STATUS -ne 200 ]; then
    echo "Status code is $STATUS. Restarting Docker Compose..."
    cd /data/harbor-install/
    /usr/local/bin/docker-compose start
else
    echo "Status code is $STATUS. No action needed."
fi
```

## 配置docker仓库代理

系统管理 -> 仓库管理 -> 新建目标 -> 填入信息 -> 保存

项目 -> 新建项目 -> 填入信息 -> 打开镜像代理，选择刚刚设置的仓库 -> 保存

假设新建项目名为`docker-hub-proxy`，则拉取命令如下

```bash
docker pull xxx.com/docker-hub-proxy/library/nginx
```

## 常用命令

```bash
USER_NAME='admin'
USER_PASSWORD='123456'
REPO_HOSTNAME='harbor.xxx.com'

# 删除仓库
curl -u "${USER_NAME}:${USER_PASSWORD}" -X DELETE -H "Content-Type: application/json" http://${REPO_HOSTNAME}/api/v2.0/projects/project_name/repositories/repo1

# 根据tag打tag
curl -u "${USER_NAME}:${USER_PASSWORD}" -X POST -H "Content-Type: application/json" -d '{"name": "hi"}' http://${REPO_HOSTNAME}/api/v2.0/projects/project_name/repositories/repo1/artifacts/1.0.0/tags

# 列出所有的tag
curl -u "${USER_NAME}:${USER_PASSWORD}" -X GET -H "Content-Type: application/json"  http://${REPO_HOSTNAME}/api/v2.0/projects/project_name/repositories/repo1/artifacts/1.0.0/tags
/projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags
```

