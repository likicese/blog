# git

## 基础操作

``` bash
git clone 
git add .
git commit -m "提交说明"
git pull
git push
```

## 疑难操作

``` bash
git config --global --unset user.name  # 清除全局用户名
git config --global --unset user.email  # 清除全局邮箱名
```

## 重置操作

``` bash
git reset --mixed HEAD^  # 不删除工作空间改动代码，撤销commit，撤销add。默认值
git reset --hard HEAD^  # 不删除工作空间改动代码，撤销commit，撤销add
git reset --soft HEAD^  # 删除工作空间改动代码，撤销commit，保留add
```

## 记住密码

``` bash
git config --local credential.helper store  # 执行该命令后，该项目下，只需要输入一次密码，就会被记住。密码以明文方式存储在本地
```

## git pull

``` bash
git pull --rebase  # 避免当先commit再pull后产生类似 “ Merge branch 'dev' of git@gitlab.1chemic.com:sales/crm.git into dev ” 这种提交
```