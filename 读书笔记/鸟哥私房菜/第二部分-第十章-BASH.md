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
declare -i sum=100+110+251  # "-i" 将其定义为整数类型。 定义的里头可以计算。
# -x 将其变为环境变量，类似于export
declare -r sum  # 将 sum 定义为不可修改类型。 -r 变量仅可读，不可改。需要注销登陆后才能修改
# -p 单独列出变量的类型
# -a 将其定义为数组
```

## 变量继承

自定义变量不会存在于子进程

子进程会将父进程的环境变量区域的内存信息拷贝到子进程

``` bash
export varName  # 此命令可以让子进程继承父进程的varName环境变量
```

## 语系

```bash
locale  # 显示当前设置的语系
```

如果没有设置语系，则会用 `LANG` 和 `LC_ALL` 来替换显示的语系

## 文件和程序的限制 ulimit

``` bash
ulimit -a  # 查看所有的限制。0值意为无限制
ulimit -H  # 严格限制，不允许超过此值
ulimit -S  # 警告限制，超过此值则警告
```

ulimit后，只有注销重登录或重新ulimit才能恢复变量值

## 变量的删除、取代和替换

``` bash
path=${PATH}  # 输出为：/usr/lib64/qt-3.3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
echo ${path#/*local}  # 输出为：/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin

# # 从头开始删，选取最短
# ## 从头开始删，选取最长
# % 从尾开始删，选取最短
# %% 从尾开始删，选取最长

echo ${path/bin/BIN}  # 替换第一个遇到的bin
echo ${path//bin/BIN}  # 替换所有bin

varName=${varName-expr}  # 当varName没赋值时，赋予expr值。varName被赋予空字符串则不动
varName=${varName:-expr}  # 当varName没赋值或者赋值为空字符串时，赋予expr值
# 类似的符号：+、:+、-、:-、=、:=、?、:?
```

## 别名

alias：建立别名

unalias：取消别名

```bash
alias log='cat'  # 设定cat的别名为log
unalias log  # 取消log别名设置
```

## history

多用户登录的时候，最后一个注销的用户历史命令才会被记录

``` bash
history -w  # 立刻将历史记录写入 histfiles 文件中
history -r  # 将histfiles的内容读入当前shell
history -c  # 将目前shell的history全部清除
history 3  # 显示最后3条命令

!!  # 执行上一条命令
!95  # 执行第95条命令
!vi  # 执行最后一条以“vi”开头的命令

echo ${HISTFILESIZE}  # 输出历史记录最大存储条数
```