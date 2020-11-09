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

## 常用操作

``` bash
# 本地新建分支并推送到远程分支
git checkout -b dev-local
git push origin dev-local:dev  # 不建议不同名字。此操作会在远程新建一个dev分支

# 将本地分支关联到远程分支
cd youProject
git remote rename origin old-origin  # 将原先远程仓库： origin    重命名为： old-origin
git remote add origin https://gitlab.github.com/xxxx/xxxx.git
git push -u origin --all
git push -u origin --tags
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

## 从ssh切换为https

``` bash
git remote set-url --add origin htps://github.com/xxx/xxx.git
git remote set-url --delete origin git@github.com:xxx/xxx.git
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
git pull origin dev  # 推送分支到远程dev分支
```

## git merge
``` bash
git merge dev  # 将dev分支代码merge到当前分支
git merge dev -v  # 显示详细的合并结果信息
git merge --abort  # 抛弃合并过程，尝试重建合并前的状态
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
git branch -D dev  # 强制删除本地名为dev的分支
git branch -v  # 列出本地所有分支，当前分支会带上“*”
git branch -m oldBranchName newBranchName  # 更名。未指定旧分支名，则默认当前所在分支
```

## git log

``` bash
git log fileName  # 查看特定文件的提交日志
git log fileName --pretty=oneline  # 以线性方式查看变更历史
git log --author userName  # 显示userName用户提交的日志
git log --oneline  # 查看简洁的日志
git log --follow fileName  # 查看fileName的提交
```

## git push
``` bash
git push origin --delete dev  # 删除远程名为dev分支的代码
git push origin master  # 指定本地master分支推送到远程名为master的分支。如果不存在，则创建
git push origin  # 若当前分支和远程分支存在追踪关系，则分支名可以省略
```

## git stash
``` bash
git stash  # 将修改保存于暂存区
git stash pop  # 将保存于暂存区的修改取出，会删除缓存栈
git stash apply  # 类似pop，不同的是该命令不删除缓存栈
git stash apply @{x}  # 将一个特定的暂存取出
git stash list  # 查看暂存区的修改
git stash drop  # 删除一个缓存栈
```

## git diff
``` bash
git diff  # 查看未暂存的修改内容，即未暂存的文件和暂存区进行比较
git diff <fileName>  # 比较暂存区文件和当前文件的差异
git diff --cached <filename>  # 查看已暂存的修改内容。即暂存区和仓库进行比较
git diff --stat  # 比较统计信息
git diff dev master  # 比较dev和master的分支差异
```

## git config
``` bash
git config --global core.editor "vim"  # 设置vim为编辑器
git config --global merge.tool <tool>  # 设置冲突解决的工具
git config core.filemode false  # 忽略文件属性改变。默认会跟踪文件属性改变
git config --local core.quotepath false  # 解决本项目下，git status 会乱码问题
git config --local unset user.name  # 取消user.name 配置
git config --list  # 列出所有的配置

git config --system list  # 列出系统配置。/etc/gitconfig
git config --global list  # 列出用户级配置。~/.gitconfig 或 ~/.config/git/config
git config --local list  # 列出仓库级配置。项目文件夹下.git/config
```

## git rebase

``` bash
git rebase --continue  # 被冲突打断后，在解决冲突的情况下，继续rabase
git rebase --skip  # 跳过某一次补丁，以继续rebase
git rebase --abort  # 终止本次rebase的行动
```

## git reset
``` bash
git reset --soft HEAD^  # 撤回commit
git reset --mixed  # 撤回commit和add
git reset --hard HEAD^  # 撤回commit、add和工作区内容
```

## git revert HEAD

``` bash
git revert HEAD  # 新增一次提交，抵消上一次提交带来的变化
```

## git fetch

``` bash
git fetch --all
git fetch master  # 更新远程master分支
```

## git commit

``` bash
git commit --amend  # 修改commit的注释
git commit -m "我是提交日记" -a  # add且commit
git commit --amend  # 将内容追加到前一个commit中，不产生新的commitId
```

## git rm

``` bash
git rm --cached <fileName>  # 撤销掉提交去暂存区的文件
git rm dirName/\*.java  # 删除该目录下所有后缀为.txt的文件
```

## git add

``` bash
git add fileName  # 指定添加到暂存区的文件
```

## git status

``` bash
git status -s  # 查看文件简明情况
```

## git show

```bash
git show commitId  # 查看该次更改的内容
```

## git reflog

```bash
git reflog show # 查看历史切换操作
```

