# docker

## 安装

参考文档：https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/

``` bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -  # 信任Docker 的 GPG 公钥

# 增加 docker-ce 源
echo "deb [arch=armhf] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian \
     $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list

apt update
apt install -y docker-ce
```

## 推荐镜像

由于树莓派是arm架构。所以装好树莓派后，多数镜像可能是无法使用的，此处附上树莓派能使用的镜像连接

https://hub.docker.com/u/arm32v7/

https://hub.docker.com/u/armhf

https://hub.docker.com/r/izone/arm/tags/