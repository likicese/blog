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