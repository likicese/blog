# ssh

## 无法在ssh中执行su命令

``` bash
ssh root@192.168.1.6 "su admin ; cd ~/"
```

以上指令无法执行。似乎ssh并不支持这种写法，会卡住。