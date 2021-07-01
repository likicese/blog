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

## 设置终端代理

```powershell
set http_proxy=socks5://127.0.0.1:1080
set https_proxy=socks5://127.0.0.1:1080
```

## 命令别名设置

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