# jenkins

## 疑难解答

### 1. 一个项目的构建会引起另外若干个项目的构建

#### 原因

jenkins会自动比较项目之间的上下游关系

发现两个项目具备上下游关系的话，会自动进行依赖构建

#### 解决

上下游项目均取消勾选`Build whenever a SNAPSHOT dependency is built`

### 2. 强制停止一个程序

在执行脚本中应该如下所示

``` bash
ssh root@192.168.1.1 "ps -ef | grep java | grep programName | grep -v bash | awk '{print \$2}' | xargs -i kill -9 {}"
```