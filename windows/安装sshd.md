# 安装sshd

## 前言

windows10自带ssh服务，默认关闭，打开即可。

[参考链接](https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH#install-win32-openssh-test-release)

## 安装

``` bat
net start sshd  ; 启动服务
sc config sshd start= auto  ; 设置开机自启，等号和值之间要有一个空格
```

## 登录默认powershell作终端

``` powershell
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
```

## 允许公钥登录

公钥应该存放在`C:\ProgramData\ssh\administrators_authorized_keys`或`C:\Users\admin\.ssh\authorized_keys`之中

若是普通用户，则验证`C:\Users\admin\.ssh\authorized_keys`

若是管理员用户，则验证`C:\ProgramData\ssh\administrators_authorized_keys`

首先，排查权限问题。其他人应无文件authorized_keys访问权限。

其次，若登录的用户具备管理员权限，则以下语句不能注释

``` config
Match Group administrators
    AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
```

注释则会导致不验证`C:\ProgramData\ssh\administrators_authorized_keys`文件，使得无法通过公钥登录

以下为修改权限的脚本：

``` powershell
$acl = Get-Acl C:\ProgramData\ssh\administrators_authorized_keys
$acl.SetAccessRuleProtection($true, $false)
$administratorsRule = New-Object system.security.accesscontrol.filesystemaccessrule("Administrators","FullControl","Allow")
$systemRule = New-Object system.security.accesscontrol.filesystemaccessrule("SYSTEM","FullControl","Allow")
$acl.SetAccessRule($administratorsRule)
$acl.SetAccessRule($systemRule)
$acl | Set-Acl
```

## 排错

### xshell5无法连入

解决：在sshd_config文件中，添加

``` config
KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1,diffie-hellman-group1-sha1
```

注意：添加的语句应该在语句Match Group administrators之前，否则将导致报错：Directive 'KexAlgorithms' is not allowed within a Match block