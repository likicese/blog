# n2n

## 前言

n2n是一个加密2层专用网络，将公网转换为私网。其使用udp协议，supernode作中转，edge为边缘结点。

注意，n2n的v1和v2不兼容。

[代码](https://github.com/ntop/n2n)

[安卓版本](https://github.com/switch-iot/hin2n)


## 编译

### linux

#### 安装编译工具

ubuntu:

``` shell
apt install cmake gcc-c++ build-essential libssl-dev
```

#### 编译

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

### windows

#### 安装编译工具

##### 安装openssl

下载网站：https://sourceforge.net/projects/openssl-for-windows/files/

选择`OpenSSL-1.1.1h_win32.zip`下载。

然后解压到目录下。例如，本例中，解压到`C:\tool\openssl`目录下。

将`C:\tool\openssl`添加环境变量`Path`下。

打开cmd，输入`openssl`。反馈如下，即为安装成功。

``` cmd
C:\Users\admin>openssl
OpenSSL>
```

##### 安装cmake

官网：https://cmake.org/download/

下载：https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2-win64-x64.msi

下载后，直接安装。

安装时，会询问是否加入环境变量，选是即可

#### 编译

进入n2n文件夹，新建文件夹：build，然后编译

``` cmd
cd n2n
git checkout 2.8-stable
mkdir build
cd build
cmake -G "MinGW Makefiles" ..
mingw32-make  ; 此处即make命令
```

编译后完成后，当前文件夹下出现`edge.exe`和`supernode.exe`文件，即为成功

## 运行

需要先启动supernode，再启动edge。

下为示例。假设现有3个主机，均编译了n2n。

### supernode

新建文件`/etc/n2n/community.conf`，写入以下内容，意为只允许创建3个以下名字的虚拟网络。若不指定，则任意名字都能创建。

```
community1
community2
netname
```

不同community的主机无法相互访问。



在ip地址为`192.168.1.101`的主机A上，执行以下命令

```bash
supernode -l 10000 -c /etc/n2n/community.conf -v -f -t  # 启动supernode，监听端口10000
```

### edge

在ip地址为`192.168.1.102`的主机B上，执行以下命令

```bash
edge -d edge-name -a 192.168.2.2 -s 255.255.255.0 -c netname -k password -l 192.168.1.101:10000  # 创建一个名为netname的网络，密码是password
```

会发现，该主机创建一个网卡，名字是edge-name，ip为192.168.2.2



在ip地址为`192.168.1.110的主机C上，执行以下命令

```bash
edge -d edge-name -a 192.168.2.3 -s 255.255.255.0 -c netname -k password -l 192.168.1.101:10000  # 创建一个名为netname的网络，密码是password
```

会发现，该主机也创建一个网卡，名字是edge-name，ip为192.168.2.3



在主机B上ping主机C的虚拟IP192.168.2.3，发现可以ping通。

## windows

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
apt install gcc-c++
```

### 缺失openssl

报错：

此报错似乎并不影响n2n的编译

```
-- Build from git rev: 2.8.0.r540.53afd3c
CMake Warning at CMakeLists.txt:49 (MESSAGE):
  OpenSSL not found, AES disabled.
```

解决：

安装openssl

### gcc编译器指定错误

报错

```
-- Building for: NMake Makefiles
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
```

解决：

指定编译器

``` cmd
cmake -G "MinGW Makefiles" ..
```

### 旧文件没清除

报错：

```
CMake Error: Error: generator : MinGW Makefiles
Does not match the generator used previously: NMake Makefiles
Either remove the CMakeCache.txt file and CMakeFiles directory or choose a different binary directory.
```

解决：

清除cmake命令生成的文件，重新cmake