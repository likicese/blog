# YouCompleteMe

## 安装

``` bash
apt install build-essential cmake3 python3-dev
git clone https://github.com/Valloric/YouCompleteMe.git
cd YouCompleteMe/
git submodule update --init --recursive  # 安装子仓库
./install.py --all
```

可能需要安装golang