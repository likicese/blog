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

## 配置为AP

编辑文件`/etc/network/interfaces`，写入以下内容

```
# 文件：/etc/network/interfaces
allow-hotplug wlan1
iface wlan1 inet static
address 192.168.99.1
netmask 255.255.255.0
```

编辑文件`/etc/dnsmasq.conf`，写入以下内容

```
interface=wlan0
listen-address=192.168.2.1
bind-interfaces
server=8.8.8.8
domain-needed
bogus-priv
dhcp-range=192.168.2.100,192.168.2.200,24h
```

新增文件`/etc/hostapd/hostap-bu.conf`，写入以下内容

```
ssid=wifi123
wpa_passphrase=12345678

interface=wlan1
driver=nl80211
auth_algs=3
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP

# 5GHz
hw_mode=a
channel=149
country_code=US

# N
ieee80211n=1
#require_ht=1
ht_capab=[HT40+]

# AC
ieee80211ac=1
#require_vht=1 # Require stations to support VHT PHY (reject association if they do not)
#vht_capab=[MAX-MPDU-3895][SHORT-GI-80][SU-BEAMFORMEE]
vht_oper_chwidth=1 # 80 MHz channel width
vht_oper_centr_freq_seg0_idx=155

# Other
wmm_enabled=1 # QoS
```

执行`hostapd /etc/hostapd/hostap-bu.conf`即可开启。

### 参考

[Hostapd - Gentoo Wiki](https://wiki.gentoo.org/wiki/Hostapd)

[802.11ac 5Ghz wifi AP in RPI 3 B+ · Issue #2619 · raspberrypi/linux · GitHub](https://github.com/raspberrypi/linux/issues/2619)

[bandwith of 802.11ac hostapd model in R-Pi 4B - Raspberry Pi Forums](https://www.raspberrypi.org/forums/viewtopic.php?t=265646)

[Raspberry Pi 4 - Hotspot - 802.11ac · Issue #450 · RaspAP/raspap-webgui · GitHub](https://github.com/RaspAP/raspap-webgui/issues/450)

### 测试

新卡的速度基本是旧卡速度的2倍。因为周遭wifi过多，时常掉线问题也被解决。

比较奇怪的是，虽然RTL8812BU配置文件是wifi5，但还是无法启动wifi5，可能是哪里不支持吧。

| wifi标准 | 频率   | 原网卡                     | RTL8812BU                  |
| -------- | ------ | -------------------------- | -------------------------- |
| wifi4    | 2.4GHZ | 5MiB/s                     |                            |
| wifi4    | 5GHZ   | 7MiB/s                     | 12MiB/s（协调速率144Mbps） |
| wifi4    | 5GHZ   |                            | 20MiB/s（协调速率300Mbps） |
| wifi5    | 2.4GHZ |                            |                            |
| wifi5    | 5GHZ   | 10MiB/s（协调速率433Mbps） |                            |

## 配置为wlan

注意，做这个配置前，wlan1的dhcp和static配置最好清除掉。

否则机器一旦重启，dhcp服务找不到192.168.2.1，报告失败。则wlan0分享的AP无法分配IP地址。



编辑文件`/etc/network/interfaces`，写入以下内容

```
allow-hotplug wlan1
iface wlan1 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```



编辑文件`/etc/wpa_supplicant/wpa_supplicant.conf`，写入以下内容

```config
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=CN

network={
        ssid="wifi123"
        psk="12345678"
        key_mgmt=WPA-PSK
        priority=1
}
```



执行`ifup wlan1`即可激活