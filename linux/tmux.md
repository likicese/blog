# tmux

## 命令

```
tmux new -s go  # 建立一个名为go的tmux，并且直接进入
tmux attach -t go  # 意外断开后，接入一个名为go的tmux
```

## 快捷键

ctrl + b   %：划分左右两个窗格

ctrl + b   “：划分上下两个窗格

## 特殊操作

### 给所有窗口发送命令

输入`ctrl + b :`

进入命令模式

输入`setw synchronize-panes on`开启全控命令。

输入`setw synchronize-panes off`可以关闭该命令。

