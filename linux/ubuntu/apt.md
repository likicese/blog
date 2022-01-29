# apt

## 不信任不安全的url

将/etc/apt/sources.list做如下修改，增加[trusted=yes]

```
deb [trusted=yes] http://mirrors.ustc.edu.cn/debian/ stable main contrib non-free
```

