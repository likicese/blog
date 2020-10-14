# conda

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

# 创建新环境
conda create -n web python=3.8
conda activate web  # 进入新建名为web的环境

# 切换到名为envName的环境
activate envName

# 退出当前环境
conda deactivate

# 删除环境
conda remove -n web --all

# 复制环境
conda create --name newEnvName --clone oldEnvName

# 更新
conda update conda

# 获取版本号
conda -V
```
