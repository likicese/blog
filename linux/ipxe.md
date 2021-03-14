# ipxe

## 参考

https://zhuanlan.zhihu.com/p/338634231

## 要点

```
#!ipxe
set base http://mirrors.aliyun.com/centos/8.3.2011/BaseOS/x86_64/os/
kernel ${base}/images/pxeboot/vmlinuz initrd=initrd.img repo=${base}
initrd ${base}/images/pxeboot/initrd.img
boot
```

