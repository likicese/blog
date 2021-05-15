# RTL8812BU编译

## 前言

鸽了2年半，如今补回。

## 环境

硬件环境：树莓派3B+  

执行`uname -a`，显示如下

```display
Linux raspberrypi 5.10.17-v7+ #1403 SMP Mon Feb 22 11:29:51 GMT 2021 armv7l GNU/Linux
```

## 编译

无法编译的版本：[GitHub - diederikdehaas/rtl8812AU: Realtek 8812AU USB WiFi driver](https://github.com/diederikdehaas/rtl8812AU)

```bash
apt install raspberrypi-kernel-headers  # 安装linux头文件
git clone https://github.com/cilynx/rtl88x2bu  # 拉取代码
make -j4  # 4核全开编译
make install  # 安装
```

执行安装命令，显示如下

```txt
install -p -m 644 88x2bu.ko  /lib/modules/5.10.17-v7+/kernel/drivers/net/wireless/
/sbin/depmod -a 5.10.17-v7+
```
