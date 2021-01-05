# 安装n2n

## 安装编译工具

ubuntu:

``` shell
apt-get install subversion build-essential libssl-dev
```

centos:
``` shell
yum install cmake gcc-c++
```

## 编译

### linux下

``` shell
cd ~
git clone https://github.com/ntop/n2n.git  # 获取代码
cd n2n

git checkout 2.8-stable  # 切换分支

mkdir build
cd build
cmake ..
make
make install
```

最后一个命令，会将编译好的内容放入各自目录下。去处如下所示

```
-- Install configuration: ""
-- Installing: /usr/local/sbin/edge
-- Installing: /usr/local/sbin/supernode
-- Installing: /usr/local/bin/n2n-benchmark
-- Installing: /usr/share/man8/edge.8.gz
-- Installing: /usr/share/man1/supernode.1.gz
-- Installing: /usr/share/man7/n2n.7.gz
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

## windows下使用bat运行

将编译出的`edge.exe`文件放到`C:\n2n\`文件夹

创建bat文件，内容如下

```bat
set N2N_WORK="C:\n2n\"

start cmd /k "cd %N2N_WORK% && edge.exe -a 192.168.2.2 -s 255.255.255.0 -c netname -k password -l 144.144.144.144:12345"
```

## 报错处理

### 没安装g++

报错

```
-- The C compiler identification is GNU 8.3.1
-- The CXX compiler identification is unknown
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
CMake Error at CMakeLists.txt:1 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.


-- Configuring incomplete, errors occurred!
See also "/srv/n2n/build/CMakeFiles/CMakeOutput.log".
See also "/srv/n2n/build/CMakeFiles/CMakeError.log".
```

解决

```
yum install gcc-c++
```

