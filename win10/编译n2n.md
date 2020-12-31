# 编译n2n

## 安装openssl

下载网站：https://sourceforge.net/projects/openssl-for-windows/files/

选择`OpenSSL-1.1.1h_win32.zip`下载。

然后解压到目录下。例如，本例中，解压到`C:\tool\openssl`目录下。

将`C:\tool\openssl`添加环境变量`Path`下。

打开cmd，输入`openssl`。反馈如下，即为安装成功。

``` cmd
C:\Users\admin>openssl
OpenSSL>
```

## 安装cmake

官网：https://cmake.org/download/

下载：https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2-win64-x64.msi

下载后，直接安装。

安装时，会询问是否加入环境变量，选是即可

## 编译

进入n2n文件夹，新建文件夹，build，然后编译

``` cmd
cd n2n
git checkout 2.8-stable
mkdir build
cd build
cmake -G "MinGW Makefiles" ..
mingw32-make  ; 此处即make命令
```
编译后完成后，当前文件夹下出现`edge.exe`和`supernode.exe`文件，即为成功

## 报错

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