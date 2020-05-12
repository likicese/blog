# python核心编程

## python基础

### 增量运算

a = a + 1   等价于   a += 1

后者不会新产生一个“a”变量，而是在原来的变量上进行加减。

### 查看文档

[变量|类|模块名].`__doc__`

要求：文档写在块内

``` python
class a:
    "this is description"

    def fun_a(self):
        "this is fun description"
        print("fun")

if __name__ == "__main__":
    print(a.__doc__)
    print(a.fun_a.__doc__)
```

### 代码结构

``` python
#！/bin/python

"this is a test module"

import sys

var_a = "test"

class a():
    "this is a class"
    pass

def fun_b():
    "this is b funtion"
    pass

if __name__ == "__main__"
    fun_b()
```

### __name__相关注解

如果被导入，`__name__`的值为模块名字

如果直接执行，`__name__`的值为`"__main__"`

### 内存管理

1. 动态内存。运行时才确定变量的类型和所占内存
2. python代码会被编译成字节码。但他还是一种解释型语言。
3. 引用计数。python中，所有变量都有引用计数器。
4. 引用计数增加：新对象、对象别名、被作为参数传递给函数、成为一个容器对象的元素
5. 引用计数减少：本地引用离开作用域、显示销毁（del a）、被从容器对象中移除、容器对象被销毁

### pip

``` bash
python3 -m pip install xxx -i https://xxx.com  # 指定源安装软件
```