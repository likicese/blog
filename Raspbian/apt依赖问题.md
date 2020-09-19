# apt依赖问题

## Errors were encountered while processing: aufs-dkms

``` bash
sudo mv /var/lib/dpkg/info /var/lib/dpkg/info.bak
sudo mkdir /var/lib/dpkg/info
sudo apt upgrade
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info.bak
sudo mv /var/lib/dpkg/info.bak /var/lib/dpkg/info
```