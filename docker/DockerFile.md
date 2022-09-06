# DockerFile

## 命令

``` bash
 docker build -f Dockerfile --build-arg HTTPS_PROXY=http://192.168.1.1:8118 .  # 构建时设置环境变量
```

## 常用的DockerFile

### 基础镜像

``` dockerfile
FROM centos:7.9.2009

LABEL MAINTAINER="likicese likicese@gmail.com"
LABEL COMPANY="www.company.com"
LABEL PROJECT="项目名"

# 设置时区和工作目录
WORKDIR /opt/${APP_NAME}/
ENV TZ Asia/Shanghai

# 1 解决时间显示问题
# 2-4 安装常用软件和清理yum缓存
# 5 将构建时间放在镜像内
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8 && \
    yum install -y vim net-tools unzip zip bind-utils less lsof epel-release && \
    yum clean all && \
    rm -rf /var/cache/yum/* && \
    echo "build date: $(date +%Z--%Y-%m-%d-%H:%M:%S)" >> /build_info.txt && \
```

### node

``` dockerfile
FROM centos:7.9.2009

ARG NODE_VERSION=v14.19.2

# 设置时区和工作目录
WORKDIR /usr/local/
ENV TZ Asia/Shanghai

RUN localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8 && \
    curl -L https://registry.npmmirror.com/-/binary/node/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz -o node-${NODE_VERSION}-linux-x64.tar.xz && \
    tar -xf node-${NODE_VERSION}-linux-x64.tar.xz && \
    rm -rf node-${NODE_VERSION}-linux-x64.tar.xz && \
    mv node-${NODE_VERSION}-linux-x64 node

ENV LC_ALL zh_CN.UTF-8
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/node/bin

# docker build -t node:v14.19.2-centos7.9
```

## tomcat

``` dockerfile
FROM adoptopenjdk/openjdk8:x86_64-centos-jdk8u322-b06

ARG TOMCAT_VERSION=9.0.62

ENV TZ Asia/Shanghai
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
ENV CATALINA_OUT /dev/stdout
WORKDIR $CATALINA_HOME

RUN mkdir -p ${ATALINA_HOME}
    curl https://mirrors.cnnic.cn/apache/tomcat/tomcat-9/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -o apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    tar -xf apache-tomcat-${TOMCAT_VERSION}.tar.gz --strip-components 1 -C /usr/local/tomcat && \
    rm -f apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm -rf /usr/local/tomcat/webapps/* && \

CMD ["catalina.sh", "run"]
```

