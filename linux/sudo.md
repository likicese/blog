# sudo

## 配置

编辑 `/etc/sudoers`

```
%sudo   ALL=(ALL:ALL) ALL  # 切记，要在这一行下添加
%userName  ALL=(ALL:ALL)       NOPASSWD:ALL
```

然后使用:wq! 强制保存