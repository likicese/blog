# 第二部分-第七章-Linux磁盘与文件系统管理

## 查询ext系列文件系统区块命令

``` bash
dumpe2fs [-bh] /dev/vda1
blkid  # 目前系统被格式化的设备
```

## 目录

目录会记录下文件inode和文件名。

inode 存储文件的时候，不存储文件名字

## 文件存储

数据存放区域：inode对照表、数据区块

元数据：超级区块、区块对照表、inode对照表

## 文件格式

``` bash
ls -l /lib/modules/$(uname -r)/kernel/fs  # 系统支持格式
cat /proc/filesystems  # 已加载到内存支持的文件系统
```

## xfs

三区

1. 数据区：存储数据使用，inode和区块在使用时才配置

2. 文件系统活动登录区：相当于ext的日志区，该区指定可以外挂磁盘

3. 实时运行区：类似磁盘的高速缓存，文件会先写到extent这里，在挪到最终目的地

``` bash
xfs_info /dev/vda1  # 查看xfs文件系统的信息
```

## 文件系统的操作

### 简单命令

``` bash
df -T  # 显示分区类型
du  # 计算使用的磁盘空间
```

### 软硬链接

#### 硬连接

在某个目录下，新增一个inode和文件名的关联

限制：不能跨文件系统、不能链接目录

``` bash
ln sourceFile LinkName
```

#### 软连接

相当于创建快捷方式

软连接文件的大小取决于源文件的文件名长度

``` bash
ln -s sourceFile LinkName
```

#### 新建目录

新建目录时，目录上层连接 +1（folderLink），目录自己+2（.和..）

### 磁盘

#### 查看

``` bash
lsblk [-dfimpt] [device]  # 查看存储设备
blkid  # 列出设备UUID
parted deviceName print  # 列出磁盘信息
parted /dev/vda print
```

#### 分区

``` bash
gdisk /dev/vda  # 开始分区。键入"?"可以查看帮助，"q"退出，"w"写入。

partprobe [-s]  # 分区完成后，此命令主动更新内核分区表的信息。否则，需要重启。
```

`fdisk` 命令使用`m`来获取帮助信息

#### 格式化

``` bash
mkfs -t xfs /dev/vda4  # 和下边的是一样的
mkfs.xfs /dev/vda4  # 都使用默认值的格式化。较重要的是inode和区块大小的数值
```

#### 文件系统校验

1. xfs_repair

用`xfs_repair`校验时，需要卸载该设备

``` bash
# -n 检查而不修改
# -f 后边的其实是个文件
xfs_repair /dev/vda1
```

2. fsck.ext4

``` bash
dumpe2fs /dev/vda1 | grep "Blocks per"  # 寻找超级区块的位置。显示8192，则下语句
fsck.ext4 -b 8192 /dev/vda5  # 以找到的第二个超级区块去校验它
```

#### 挂载系统

``` bash
mount -a  #　将　/etc/fstab 文件内的盘悉数挂载
mount -UUID="xxxxxxxxxxxxxxxxxx" /mnt/usb  # 注意，/mnt/usb
```