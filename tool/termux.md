# termux

## 前言



参考：

https://www.sqlsec.com/2018/05/termux.html

## 技巧

### tab补全，机器震动

编辑文件`$HOME/.termux/termux.properties`。配置以下项即可

``` config
bell-character = ignore
```


## 运行其他系统

以下以运行ubuntu为例

```
apt install -y proot git
cd ~
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
bash ./ubuntu.sh -y
./startubuntu.sh  # 启动ubuntu，并切换到ubuntu的终端
```