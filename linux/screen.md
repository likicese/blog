# screen

## 常用命令

``` bash
screen -S myScreen  # 创建一个名为myScreen的会话，并进入该会话
screen -ls  # 显示全部会话
screen -r <pid>|<screenName>  # 用上边命令时候，显示的pid。或者创建的名字
screen -dmS dScreen  # 创建一个启动即离线的窗口
screen -d  # 断开正在连接的会话

screen -x -S dScreen -p 0 -X stuff $'aa\n'  # 给名为dScreen的窗口发送 “aa”
```

ctrl + a d  ： 将当前会话放到后台运行
ctrl + a c  ： 在当前的screen会话中创建窗口
ctrl + a p  ： 上一个窗口
ctrl + a n  ： 下一个窗口
ctrl + a w  ： 窗口列表