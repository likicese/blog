# pve

## 安装

[下载地址](https://mirrors.tuna.tsinghua.edu.cn/proxmox/iso/)

下载完成后，刻入U盘，在bios中打开虚拟化，逐步安装即可

### amdgpu过新，无法启动xorg

若amd的核显过新，则xorg无法启动，此时应修改org配置文件。

等待终端出现

``` bash
Xorg -configure  # 在家目录生成配置文件
mv ~/xorg.conf.new /etc/X11/xorg.conf

# 编辑配置文件，所有“amdgpu”均改为“fbdev”
vim /etc/X11/xorg.conf

# 改后保存，重启xorg
startx
```

## 集群

### 清除已有的集群信息

```bash
# 停止cluster服务
systemctl stop pve-cluster.service 
systemctl stop corosync.service

# 设置本地模式
pmxcfs  -l

# 删除corosync 配置文件
rm /etc/pve/corosync.conf 
rm -rf /etc/corosync/*

# 重启cluster集群服务
killall pmxcfs
systemctl start pve-cluster.service
```

### 退出集群

```bash
# 先执行清除集群信息的语句，清除信息

# 然后在/etc/pve/nodes文件夹中，删除非本机的机器信息。
# 例如，假设有pve01和pve02这2台机器，可以ssh到pve01上，执行rm -rf pve02，清除pve02的信息
cd /etc/pve/nodes
rm -rf pve02  # 当前处于pve01上
```

## 用cloud-init模板创建虚拟机

cloud-init模板：自带cloud-init软件，可以在制作模板后，直接修改cloud-init，进行初始化动作，如设置IP、注入公钥等

### 获取模板

generic版中有cloud-init，nocloud版中无cloud-init，

- CentOS: https://cloud.centos.org/centos/
- Ubuntu: https://cloud-images.ubuntu.com/releases/
- Debian: https://cloud.debian.org/images/cloud/
- Fedora: https://alt.fedoraproject.org/cloud/
- RedHat: https://access.redhat.com/downloads/
- openSUSE: http://download.opensuse.org/repositories/Cloud:/Images:/

### 创建虚拟机

#### 创建虚拟机

在web页面。

正常创建1个虚拟机，在“操作系统”一页，选择“不使用任何介质”。

创建后，将硬盘（scsi0）先分离，再删除。

#### 导入虚拟机

用ssh进入宿主机后台。

执行以下命令，将下载的qcow2镜像文件导入虚拟机

```bash
# 如果下载的是img格式，则导入时需要添加--format=qcow2参数。204是创建虚拟机时使用的VM ID。local-lvm是本地存储池，若非默认，则需改名
qm importdisk 204 debian-12-generic-amd64.qcow2 local-lvm
```

#### 调整硬件

回到web页面。

在“硬件”界面选择未挂载磁盘，使用SCSI 0控制器将其挂载，并将磁盘大小增加48GB。

在“硬件”界面选择“添加”，添加“CloudInit设备”，选scsi1，选择和该虚拟机一样的存储池即可。

在“选项”界面，修改“引导顺序”，将scsi0调整到第一个，并将其设为“已启用”。

在“选项”界面，修改“QEMU Guest Agent”，选VirtIO，将状态改为“已启用”

点击“CloudInit”界面，将IP、用户等调整为自己需要的属性，点一下“重生成映像”。

#### 启动

按开机按钮，启动即可

#### 初始化

##### 打开root登录

debian12的sshd默认禁止root以密码登录，为了配置系统，可以暂时打开。若注入了公钥或使用非root用户，可以忽略此处。

编辑文件/etc/ssh/sshd_config，改动以下2项

- PermitRootLogin prohibit-password 改为 PermitRootLogin yes
- PermitEmptyPasswords no 改为 PasswordAuthentication yes

输入命令`systemctl restart sshd`，重启sshd服务

##### 个性化设置

1. 设置本地时间

```bash
timedatectl set-timezone Asia/Shanghai
```

2. 设置apt源

参考[debian | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/debian/)进行apt设置

注意，文件`/etc/apt/sources.list.d/debian.sources`依然会去拉取官方源，建议将其内容注释掉

执行`apt update`更新软件包。

如果发生报错“ Could not get lock /var/lib/apt/lists/lock. It is held by process 546 (apt-get)”，则使用ps命令，将正在进行`apt update`进程停止。再执行`apt update`更新软件信息。

3. 安装常用软件

```bash
apt upgrade -y  # 更新软件
apt install -y chrony acpid  # 时间同步、电源管理
systemctl enable --now acpid
apt install -y vim bash-completion mtr net-tools  # 推荐软件

# 记录10000条历史
cat > /etc/profile.d/history.sh << EOF
shopt -s histappend
HISTTIMEFORMAT='%F %T '
HISTSIZE="100000"
HISTFILESIZE=100000
PROMPT_COMMAND='(umask 000; msg=\$(history 1 | { read x y; echo \$y; }); echo [\$(who am i | awk "{print \\\$(NF-2),\\\$(NF-1),\\\$NF}")] [\$(whoami)@\`pwd\`]" \$msg" >> /var/log/.history)'
export HISTTIMEFORMAT HISTSIZE HISTFILESIZE PROMPT_COMMAND
EOF

# 安装qemu监控软件，并设置开机自启动，以便获取IP
apt install qemu-guest-agent -y
systemctl enable --now qemu-guest-agent  # 或/lib/systemd/systemd-sysv-install enable qemu-guest-agent
```

##### 关闭不安全的root登录

将PermitRootLogin 和PermitEmptyPasswords 修改还原，重启sshd

##### 清理

```bash
apt autoclean all
history -c  # 清理历史
poweroff  # 关机
```

### 转换模板

web页面，右键转换成模板即可。

## 装win11要点

[virtIO.iso](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/ )

主板选q35，硬盘选“VirtIO Block”，挂载iso文件时设备选IDE，不要加载网卡。

“选项”一栏，将“QEMU Guest Agent”打开，以便后续安装guest-agent后，宿主机可以获取ip。

找不到硬盘则选“加载驱动程序”，打开挂载的virtIO文件，驱动在`D://amd64/win11`路径下。

跳过联网：组合按键“Shift + F10”，在打开的cmd窗口中输入`oobe\BypassNRO.cmd`，回车即重启安装，出现跳过联网按钮。

之后像正常的win11安装即可。

安装完成，再添加网卡，设备类型选择“virtIO”。如果不打算加载驱动，选择其他类型的网卡亦可。

安装完成，进入系统后，不要卸载`virtIO.iso`镜像

安装`D://guest-agent/qemu-ga-x86_64.exe`

安装`D://virtio-win-gt-x64.exe`

## 模拟aarch64

```bash
# 在宿主机安装
apt install qemu-efi-aarch64
```

web页面创建虚拟机，注意以下选项

```
不用引导介质
控制器改为Virtio scsi
bios改为“OVMF”，但不要EFI磁盘
磁盘大小改为128GB
```

修改虚拟硬件设备

```
添加ＣＤ设备，总线用ＳＣＳＩ
添加串口，默认０
显示改为串口输出
```

引导调整到第一位启动

修改文件

```
# vi /etc/pve/qemu-server/160.conf

增加:
arch: aarch64

注释掉:
#vmgenid xxx...

删除掉：
cpu: xxx...
```

8.0后，拆出pve-edk2-firmware-aarch64，需增加非订阅存储库，新装[proxmox | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/proxmox/)

```
apt install pve-edk2-firmware-aarch64
```

检查模拟器支持什么cpu

```
qemu-system-aarch64 -cpu ?
```

### 选用配置

```bash
# 当没有合适的uefi时，设置启动文件
cat > /boot/efi/startup.nsh << EOF
\EFI\debian\grubaa64.efi
EOF
```