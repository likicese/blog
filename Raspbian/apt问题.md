# apt问题

## Errors were encountered while processing: aufs-dkms

``` bash
sudo mv /var/lib/dpkg/info /var/lib/dpkg/info.bak
sudo mkdir /var/lib/dpkg/info
sudo apt upgrade
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info.bak
sudo mv /var/lib/dpkg/info.bak /var/lib/dpkg/info
```

## 文件损坏

[参考](https://bugs.launchpad.net/raspbian/+bug/1619783)

apt: symbol lookup error: /lib/arm-linux-gnueabihf/libstdc++.so.6: undefined symbol: _ZNSt13__future_base19_Async_state_commonD1Ev, version GLIBCXX_3.4.17

解决：

``` bash
gcc --version  # 确定gcc版本
wget http://archive.raspbian.org/raspbian/pool/main/g/gcc-8/libstdc%2B%2B6_8.3.0-6%2Brpi1_armhf.deb
dpkg -i --auto-deconfigure libstdc++6_8.3.0-6+rpi1_armhf.deb
```