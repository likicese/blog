# conda

## 下载

[北京外国语大学开源软件镜像站点](https://mirrors.bfsu.edu.cn/anaconda/)

## 添加源

[参考](https://mirrors.bfsu.edu.cn/help/anaconda/)

## 系统环境变量

在环境变量中，添加：

``` path
C:\Users\All Users\Anaconda3\Scripts
```

具体路径，依据个人情况而定。

添加后，打开cmd即可直接使用conda命令

## 命令

``` bash
# 设置清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes

# 查看当前虚拟环境列表
conda env list
conda info -e

conda create -n web python=3.8  # 创建新环境
conda create -n web python=3.8 anaconda  # 附带安装常用的包
conda activate web  # 进入新建名为web的环境

# 切换到名为envName的环境
source activate envName  # linux
activate envName  # windows

# 退出当前环境
source deactivate  # linux
conda deactivate  # windows

# 删除环境
conda remove -n web --all

# 复制环境
conda create --name newEnvName --clone oldEnvName

# 更新
conda update conda  # 先升级conda
conda update anaconda  # 再升级anaconda

# 获取版本号
conda -V

# 包管理，类似pip
conda install numpy  # 安装numpy包
conda remove numpy  # 卸载
conda list  # 显示已安装的包
```
