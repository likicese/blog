# git

## 基础操作

``` bash
git clone 
git add .
git commit -m "提交说明"
git pull
git push
```

##　疑难操作

``` bash
git config --global --unset user.name  # 清除全局用户名
git config --global --unset user.email  # 清除全局邮箱名
```

## 重置操作

``` bash
git reset --hard HEAD^  # 丢弃上一次本地提交
```

## 记住密码

``` bash
git config --local credential.helper store  # 执行该命令后，该项目下，只需要输入一次密码，就会被记住。密码以明文方式存储在本地
```