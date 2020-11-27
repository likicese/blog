# electron

## Harfbuzz version too old (1.3.1)

### 问题原因

electron框架版本太老

### 解决办法

将相关的so库解压相应的软件夹下

```bash
# 获取
wget http://security.ubuntu.com/ubuntu/pool/main/p/pango1.0/libpango-1.0-0_1.40.14-1ubuntu0.1_amd64.deb
wget http://security.ubuntu.com/ubuntu/pool/main/p/pango1.0/libpangocairo-1.0-0_1.40.14-1ubuntu0.1_amd64.deb
wget http://security.ubuntu.com/ubuntu/pool/main/p/pango1.0/libpangoft2-1.0-0_1.40.14-1ubuntu0.1_amd64.deb
```

