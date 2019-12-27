# BASH

## bash简介

/etc/shells 文件记录了可使用bash

/bin/sh 被连接到了 /bin/bash

命令历史记录放在了 ~/.bash_history 文件中，本次登录执行的命令只有在正常注销后，才会记录进去

选项、参数补全辅助软件：bash-completion

## type

``` bash
type cd  # 查看cd命令是内置的还是外置的
```

## 快捷命令

``` button
[ctrl] + u 删除光标前边的字符串
[ctrl] + k 删除光标后边的字符串
[ctrl] + a 光标移动到最前边
[ctrl] + e 光标移动到最后边
```

## 变量

unset varName  # 取消变量内容

export PATH  # 将变量变为环境变量

``` bash
env  # 获取所有环境变量
set  # 获取所有环境变量和自定义变量
PS1='[\u@\h \w \A \#]\$ '  # 重设命令行显示变量，用户、主机名、文件路径、时间、本bash执行的第几个命令、特权和非特权用户的标识

export envName  # 将envName设为环境变量，以使其能够被bash的子进程使用
```

## 变量含义

$$ 本bash的PID

$? 上个命令执行的结果

## 语系变量

``` bash
locale -a  # 查看所有支持语系变量
# LANG 和 LC_ALL 为语系变量未设置时，默认使用的变量
```

## 变量的键盘读取

``` bash
read -p "we need str" -t 30 varName  # 屏幕提示 “we need str”，并且等待30秒。输入的字符会被给到varName该变量中
```

## declare 和 typeset

``` bash
declare -i sum=100+110+251  # 将其定义为整数类型，并计算。
# -x 将其变为环境变量，类似于export
declare -r sum  # 将 sum 定义为不可修改类型。 -r 变量仅可读，不可改。需要注销登陆后才能修改
# -p 单独列出变量的类型
# -a 将其定义为数组
```