# conda

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


# 退出当前环境
conda deactivate

# 删除环境
conda remove -n web --all
```