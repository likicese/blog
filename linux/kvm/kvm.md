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

## 磁盘相关

```bash
virsh attach-disk vm_centos /opt/test-disk.qcow2 vdb  # 挂载磁盘，实际在/dev中挂载磁盘的名称不一定是这个，也可能是vdc
virsh detach-disk vm_centos --target vdb

virsh attach-disk vm_centos /opt/test-disk.qcow2 --driver qemu --target vdb --mode shareable  # 另一种更多参数的挂载语法

qemu-img convert -O qcow2 windows.qcow2 windows-1.qcow2  # 压缩磁盘空间。如果磁盘中含有快照，则新磁盘会卡在196K。把磁盘中的快照删除即可
```

