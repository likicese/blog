# git

## 基础操作

``` bash
git init  # 初始化仓库
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

## git自动补全
``` bash
cd ~  # 进入家目录
wget https://github.com/git/git/raw/master/contrib/completion/git-completion.bash  # 拉取补全文件
mv git-completion.bash .git-completion.bash  # 隐藏在ls下的显示
echo "source ~/.git-completion.bash" >> ~/.bashrc  # 打开shell时，加载该文件
source ~/.bashrc  # 立即加载文件生效
```

## git pull

``` bash
git pull --rebase  # 避免当先commit再pull后产生类似 “ Merge branch 'dev' of git@gitlab.1chemic.com:sales/crm.git into dev ” 这种提交
```

## git merge
``` bash
git merge dev  # 将dev分支代码merge到当前分支
```

## git remote
``` bash
git remote  # 列出所有主机
git remote -v  # 列出主机网址
git remote add staging https://github.com/xxx/xxx.git  # 添加一个远程分支
git fetch staging  # 抓取一个远程分支
```

## git checkout
``` bash
git checkout fileName  # 将文件回退到没有提交的版本
git checkout dev  # 将工作分支切到dev，并且追踪远程分支
git checkout -b dev  # 本地新建dev分支
```

## git branch
``` bash
git branch branchName  # 新建分支
git branch -d dev  # 删除本地名为dev的分支
```

## git log

``` bash
git log fileName  # 查看特定文件的提交日志
git log --author userName  # 显示userName用户提交的日志
```

## git push
``` bash
git push origin --delete dev  # 删除远程名为dev分支的代码
```

## git stash
``` bash
git stash  # 将修改保存于暂存区
git stash pop  # 将保存于暂存区的修改取出
git apply @{x}  # 将一个特定的暂存取出
git stash list  # 查看暂存区的修改
```

## git diff
``` bash
git diff  # 查看修改内容
git diff <fileName>  # 比较暂存区文件和当前文件的差异
```

## git config
``` bash
git config --global core.editor "vim"  # 设置vim为编辑器
```

## git rebase

``` bash
git rebase --continue  # 被冲突打断后，在解决冲突的情况下，继续rabase
git rebase --skip  # 跳过某一次补丁
```