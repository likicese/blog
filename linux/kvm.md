# kvm

## 基本命令

```bash
virt-install --disk size=128 --name=centos-vm1 --os-variant=centos8 --vcpu=2 --ram=10000 --graphics vnc --cdrom /opt/CentOS-8.1.1911-x86_64-dvd1.iso --network bridge:virbr0  # 动态磁盘128GB，2个cpu，10G内存

virt-clone --auto-clone -o centos-vm1 -n centos-vm2  # 把vm1克隆一份，变成vm2

virsh start centos-vm2
virsh vncdisplay centos-vm2
virsh shutdown centos-vm2
virsh destroy centos-vm2
```

