# ubuntu

## 色彩管理

### 问题

```
authentication required to create a color managed device
```

### 解决

创建文件：`/etc/polkit-1/localauthority/50-local.d/45-allow-colord.pkla`，填入以下内容

```
[Allow Colord all Users]
Identity=unix-user:*
Action=org.freedesktop.color-manager.create-device;org.freedesktop.color-manager.create-profile;org.freedesktop.color-manager.delete-device;org.freedesktop.color-manager.delete-profile;org.freedesktop.color-manager.modify-device;org.freedesktop.color-manager.modify-profile
ResultAny=no
ResultInactive=no
ResultActive=yes
```

## 设置时区

``` bash
dpkg-reconfigure tzdata
```