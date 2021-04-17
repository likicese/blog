# vs code配置环境

## 前言

系统：windows 10

vs code的安装不在本文讨论范围之内

## 配置.vscode文件夹（重点）

很多人失败在这一步

[参考1](https://zhuanlan.zhihu.com/p/92175757)

[参考2](https://segmentfault.com/a/1190000020793997)

新建一个文件夹，命名为.vscode，里边新建两个文件，内容如下



tasks.json

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build c program",
      "type": "shell",
      "command": "g++",
      "args": [
        "${fileBasename}",  // 当前打开的文件名
        "-g",  // debug功能需要这个参数
        "-o",
        "${fileBasenameNoExtension}.exe",  // 会将当前打开的文件编译为xx.exe可执行文件
      ]
    }
  ]
}
```



launch.json

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "preLaunchTask": "build c program",
            "name": "(gdb) 启动",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```



选中代码文件，按F5即可启动调试



这么配置会有一个问题，编译的永远是当前打开的文件。若是在修改a文件，b文件才是主文件，则编译失败。此时建议将b文件写到配置文件中去。

## 测试例子

hello.cpp

```cpp
#include <iostream>
using namespace std;
int main()
{
    cout << "Hello world" << endl;
    return 0;
}
```

