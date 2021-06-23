# WSL

## 设置root进入

打开powerShell

``` powershell
wslconfig /list
wslconfig /setdefault debian
debian config --default-user root
```

## 寻找安装目录

打开注册表，找到如下路径

```
计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss
```

除默认外，每一条均代表一个wsl。

找到自己需要的wsl，到子目录下，找`BasePath`。该键对应的值就是wsl文件存放目录。目录例子如下：

```
C:\Users\用户名\AppData\Local\Packages\TheDebianProject.DebianGNULinux_dfe4gfssgdys\LocalState
```

其中，`rootfs`是根目录

新装系统迁移的时候，直接把文件复制过去覆盖即可。

也可修改该值，将wsl安装目录指向其他位置。

## 笔记

运行程序时，windows直接管辖的磁盘可能会报告无权限的问题。起因是NTFS格式的磁盘没有linux中属主、属组之类的概念。遇到此类情况，将文件复制到linux目录下即可

## 修改挂载windows磁盘默认权限是777的问题

wsl启动后，windows的文件全部是绿色。看着十分不舒服。

新建或修改文件：/etc/wsl.conf，内容如下：

``` config
[automount]
enabled = true
root = /mnt/
options = "metadata,dmask=022,fmask=133"
mountFsTab = false
```

[参考](https://docs.microsoft.com/zh-cn/windows/wsl/wsl-config)