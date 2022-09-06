# node

## 安装

官网下载：https://nodejs.org/en/download/

也可以用淘宝的cdn下载

整个脚本如下，可以通过更改版本号下载不同的版本：

``` bash
VERSION="v14.17.5"
PACKAGE_NAME="node-${VERSION}-linux-x64"
wget https://npm.taobao.org/mirrors/node/${VERSION}/${PACKAGE_NAME}.tar.xz

tar -xf ${PACKAGE_NAME}.tar.xz
mv ${PACKAGE_NAME} /usr/local/node

cat >> /etc/profile << EOF

export NODE_HOME=/usr/local/node
export PATH=\$NODE_HOME/bin:\$PATH
EOF
```

## 命令

``` bash
npm install -–unsafe-perm xx  # 强制用root用户执行当前的安装命令。npm不允许用root运行。当使用root运行时，会自动切换到nobody用户。碰到一些需要权限的操作时，则权限不够。
npm install --unsafe-perm=true --allow-root  xx  # 加强版
npm install --registry=https://registry.npm.taobao.org express  # 指定淘宝源安装express
npm install --prefix /opt/lib -g express  # 换一个全局路径安装express，避免版本冲突的q'kuan
```

## 设置变量

### 设置模块安装的位置

``` bash
npm config set registry https://registry.npmmirror.com
npm set cache D:\nodejs\node_cache
npm set prefix D:\nodejs\node_global  # D:\nodejs\node_global 需要设置到环境变量，才能将安装的软件直接在cmd中使用
npm config ls
```