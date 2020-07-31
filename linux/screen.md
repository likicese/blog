# screen

## 常用命令

``` bash
screen -S myScreen  # 创建一个名为myScreen的会话，并进入该会话
screen -ls  # 显示全部会话
screen -r <pid>|<screenName>  # 用上边命令时候，显示的pid。或者创建的名字
screen -d dScreen  # 创建一个启动即离线的窗口
```

ctrl + a d  ： 将当前会话放到后台运行