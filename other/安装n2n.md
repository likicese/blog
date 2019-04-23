# 安装n2n

## 系统环境

linux：ubuntu 18

## 下载n2n

``` shell
cd ~
git clone https://github.com/ntop/n2n.git
cd n2n

git checkout 2.4-stable  # 切换分支
```

## 安装编译工具

``` shell
apt-get install subversion build-essential libssl-dev
```

## 编译

操作在n2n目录下

``` shell
mkdir build
cd build
cmake ..
make
make install
```

## 运行示例

语法示例

virtualLocalIP别和本地IP同一网段

``` shell
edge -d <edgeName> -a <virtualLocalIP> -s <subnetMask> -c <netName> -k <password> -l <superNodeIP>
```

实例

``` shell
edge -d edge-name -a 192.168.2.2 -s 255.255.255.0 -c netname -k password -l 144.144.144.144
```