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

运行vs code（以下命令在ubuntu的终端中执行）

```
apt update; apt upgrade
apt install wget
cd /opt
wget https://github.com/cdr/code-server/releases/download/v3.10.2/code-server-3.10.2-linux-arm64.tar.gz
tar -xf code-server-3.10.2-linux-arm64.tar.gz
echo "export PATH=$PATH:/opt/code-server/bin" >> /etc/profile
ln -s ./code-server-3.10.2-linux-arm64/ code-server

exit  # 退出
./startubuntu.sh  # 重进
code-server  # 启动
cat ~/.config/code-server/config.yaml  # 密码在这
```