# nexus

## 常用代理

### docker-ce

```
# 阿里云的yum docker-ce源
https://mirrors.aliyun.com/docker-ce/linux/centos/
```

vim /etc/yum.repos.d/your-nexus.repo

```
[docker-ce]
name=Docker-CE Repository
baseurl=http://your-nexus.com/repository/docker-ce-repo/$releasever/$basearch/stable
enabled=1
gpgcheck=1
keepcache=1
gpgkey=http://your-nexus.com/repository/docker-ce-repo/gpg
```

