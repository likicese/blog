# WSL

## 设置root进入

打开powerShell

``` powershell
wslconfig /list
wslconfig /setdefault debian
debian config --default-user root
```

## 安装目录

C:\Users\用户名\AppData\Local\Packages\TheDebianProject.DebianGNULinux_dfe4gfssgdys\LocalState\rootfs

## 笔记

运行程序时，windows直接管辖的磁盘可能会报告无权限的问题。起因是NTFS格式的磁盘没有linux中属主、属组之类的概念。遇到此类情况，将文件复制到linux目录下即可