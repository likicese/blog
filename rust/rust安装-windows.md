# rust安装-windows

[参考](https://blog.csdn.net/zhmh326/article/details/103805485)

## 安装mingw64

这是mingw的代替品。

### 下载

下载网址：https://sourceforge.net/projects/mingw-w64/files/

```
x86_64：64位版本
i686：32位版本

posix：操作系统接口标准为posix，相比win32，posix对C++11标准库支持更好。可以使用多线程。
win32：操作系统接口标准为win32

sjlj：采用sjlj的异常处理，这种方式比起其他异常处理会慢得多
dwarf：采用dwarf的异常处理，这种方式需要在可执行程序中添加额外的调试信息，使得程序体积较大
seh：采用seh的异常处理，即使用windows自身的异常处理机制
```

建议安装x86_64-8.1.0-release-posix-seh-rt_v6-rev0。win32版本编译时候会报错。

### 安装

下载会获得一个7z文件。

将其解压到C盘下，系统变量可配置如下

```
`C:\mingw64\bin`
```

打开cmd，输入`gcc`测试即可