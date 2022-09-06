# anyconnect

## windows记住密码脚本

start.bat文件内容如下

```bat
taskkill -im vpnui.exe -f
set SOFTWARE_PATH="C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\"
set CREDENTIAL_PATH="C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\credential.txt"
%SOFTWARE_PATH%vpncli.exe -s < %CREDENTIAL_PATH%
%SOFTWARE_PATH%vpnui.exe
```

credential.txt文件内容如下，自行替换网址、用户名和密码，放在和脚本对应的密码文件位置

```txt
connect example.com
zhangsan
foaierjoangeoiattn
y
```

