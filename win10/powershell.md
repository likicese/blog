# powershell

``` powershell
netstat -ano | findstr "8080"  # 查看8080端口是否有人在监听
Get-Command ssh  # 获取ssh命令的存放路径
```

## 脚本安全策略更改

windows个人版本的powershell没有执行脚本的权限，需要主动修改

参考：https://docs.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1

```
set-ExecutionPolicy RemoteSigned  # 脚本可以运行，要求有受信的签名
```

## 命令别名设置

需要按如上所示，修改脚本执行策略，才能在启动终端时执行该文件

``` powershell
echo $PROFILE  # 查看启动的时候会加载的文件，类似于linux中的~/.bashrc
mkdir -p C:\Users\<你的用户名>\Documents\WindowsPowerShell\  # 创建文件存放的文件夹，避免因为文件夹不存在而创建文件失败
vim $(echo $PROFILE)  # 编辑该文件
```

在文件中添加：

``` ps1
function s_dev function vim_hosts {ssh 192.168.1.10}  # 示例。跳到一台服务器上。
```

保存，重开powershll，执行`s_dev`，即可生效

## 删除不用的别名

powershell中的`curl`是`Invoke-WebRequest`的别名，该命令和curl不兼容，需要删除别名设置。

由于没相应设置，只能通过终端启动时预加载文件动态删除……

在前一节中的`$PROFILE`文件中加入如下语句即可

``` powershell
Remove-Item alias:curl
```

## 建立端口转发

注意，以下语句应使用管理员权限运行

``` powershell
# 给远程主机建立ssh转发端口
netsh interface portproxy add v4tov4 listenport=10022 connectport=22 connectaddress=192.168.1.12
```