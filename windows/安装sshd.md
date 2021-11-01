# 安装sshd

## 前言

windows10自带ssh服务，默认关闭，打开即可。

[参考链接](https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH#install-win32-openssh-test-release)

## 安装

``` bat
net start sshd  ; 启动服务
sc config sshd start= auto  ; 设置开机自启
```