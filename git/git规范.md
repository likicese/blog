# git规范

## 二进制文件

代码库中，不建议存放非必要的二进制文件，容易造成代码仓库膨胀问题

```bash
find . -path ./.git -prune -o -type f | perl -lne 'print if -B'  # 显示二进制文件
diff -ruNa dir1 dir2  # 比较不同文件夹下文件是否相同
```



