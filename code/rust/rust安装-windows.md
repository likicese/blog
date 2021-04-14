# rust安装-windows

[参考](https://blog.csdn.net/zhmh326/article/details/103805485)

## 安装mingw64

这是mingw的代替品。

### 下载

下载网址：https://sourceforge.net/projects/mingw-w64/files/

```
x86_64：64位版本
i686：32位版本

posix：操作系统接口标准为posix，相比win32，posix对C++11标准库支持更好。可以使用多线程。
win32：操作系统接口标准为win32

sjlj：采用sjlj的异常处理，这种方式比起其他异常处理会慢得多
dwarf：采用dwarf的异常处理，这种方式需要在可执行程序中添加额外的调试信息，使得程序体积较大
seh：采用seh的异常处理，即使用windows自身的异常处理机制
```

建议安装x86_64-8.1.0-release-posix-seh-rt_v6-rev0。win32版本编译时候会报错。

### 安装

下载会获得一个7z文件。

将其解压到C盘下，系统变量可配置如下

```
`C:\mingw64\bin`
```

打开cmd，输入`gcc`测试即可

## 配置环境变量

目的是更改下载源

新建两个系统环境变量，值如下

| 变量名             | 值                                             |
| ------------------ | ---------------------------------------------- |
| RUSTUP_DIST_SERVER | https://mirrors.ustc.edu.cn/rust-static        |
| RUSTUP_UPDATE_ROOT | https://mirrors.ustc.edu.cn/rust-static/rustup |



## 安装rust

### 确认windows上已安装mingw编译器

```
Rust Visual C++ prerequisites

Rust requires the Microsoft C++ build tools for Visual Studio 2013 or
later, but they don't seem to be installed.

The easiest way to acquire the build tools is by installing Microsoft
Visual C++ Build Tools 2019 which provides just the Visual C++ build
tools:

  https://visualstudio.microsoft.com/visual-cpp-build-tools/

Please ensure the Windows 10 SDK and the English language pack components
are included when installing the Visual C++ Build Tools.

Alternately, you can install Visual Studio 2019, Visual Studio 2017,
Visual Studio 2015, or Visual Studio 2013 and during install select
the "C++ tools":

  https://visualstudio.microsoft.com/downloads/

Install the C++ build tools before proceeding.

If you will be targeting the GNU ABI or otherwise know what you are
doing then it is fine to continue installation without the build
tools, but otherwise, install the C++ build tools before proceeding.

Continue? (Y/n) y
```

输入y即可

### 自定义安装选项

```
Welcome to Rust!

This will download and install the official compiler for the Rust
programming language, and its package manager, Cargo.

Rustup metadata and toolchains will be installed into the Rustup
home directory, located at:

  C:\Users\admin\.rustup

This can be modified with the RUSTUP_HOME environment variable.

The Cargo home directory located at:

  C:\Users\admin\.cargo

This can be modified with the CARGO_HOME environment variable.

The cargo, rustc, rustup and other commands will be added to
Cargo's bin directory, located at:

  C:\Users\admin\.cargo\bin

This path will then be added to your PATH environment variable by
modifying the HKEY_CURRENT_USER/Environment/PATH registry key.

You can uninstall at any time with rustup self uninstall and
these changes will be reverted.

Current installation options:


   default host triple: x86_64-pc-windows-msvc
     default toolchain: stable (default)
               profile: default
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
>2
```

此处脚本自动确定的版本不对，需要修改，输入`2`

```
I'm going to ask you the value of each of these installation options.
You may simply press the Enter key to leave unchanged.

Default host triple?
x86_64-pc-windows-gnu
```

此处需要修改安装版本，输入`x86_64-pc-windows-gnu`

```
Default toolchain? (stable/beta/nightly/none)
stable
```

是否稳定版本，输入`stable`

```
Profile (which tools and data to install)? (minimal/default/complete)
default
```

需要安装的工具，输入`default`

```
Modify PATH variable? (y/n)
y
```

是否允许修改环境变量，输入`y`

```
Current installation options:


   default host triple: x86_64-pc-windows-gnu
     default toolchain: stable
               profile: default
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
>1
```

确认安装选项，输入`1`，开始安装

```
info: profile set to 'default'
info: setting default host triple to x86_64-pc-windows-gnu
info: syncing channel updates for 'stable-x86_64-pc-windows-gnu'
info: latest update on 2020-11-19, rust version 1.48.0 (7eac88abb 2020-11-16)
info: downloading component 'cargo'
info: downloading component 'clippy'
info: downloading component 'rust-docs'
 13.3 MiB /  13.3 MiB (100 %)   6.6 MiB/s in  2s ETA:  0s
info: downloading component 'rust-mingw'
info: downloading component 'rust-std'
 20.3 MiB /  20.3 MiB (100 %)   3.8 MiB/s in  5s ETA:  0s
info: downloading component 'rustc'
 67.0 MiB /  67.0 MiB (100 %)   4.7 MiB/s in 14s ETA:  0s
info: downloading component 'rustfmt'
  6.1 MiB /   6.1 MiB (100 %)   4.6 MiB/s in  1s ETA:  0s
info: installing component 'cargo'
info: using up to 500.0 MiB of RAM to unpack components
info: installing component 'clippy'
info: installing component 'rust-docs'
 13.3 MiB /  13.3 MiB (100 %)   1.4 MiB/s in 10s ETA:  0s
info: installing component 'rust-mingw'
info: installing component 'rust-std'
 20.3 MiB /  20.3 MiB (100 %)   7.9 MiB/s in  2s ETA:  0s
info: installing component 'rustc'
 67.0 MiB /  67.0 MiB (100 %)   7.9 MiB/s in  8s ETA:  0s
info: installing component 'rustfmt'
info: default toolchain set to 'stable-x86_64-pc-windows-gnu'

  stable-x86_64-pc-windows-gnu installed - rustc 1.48.0 (7eac88abb 2020-11-16)


Rust is installed now. Great!

To get started you need Cargo's bin directory (%USERPROFILE%\.cargo\bin) in
your PATH environment variable. Future applications will automatically
have the correct environment, but you may need to restart your current shell.

Press the Enter key to continue.
```

安装完成，随意输入一个按键，然后退出

## 配置vs code

安装`rust-analyaer`和`CodeLLDB`

配置文件如下：

```
    "configurations": [

        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug",
            "program": "${workspaceFolder}/target/debug/projectName.exe",
            "args": [],
            "cwd": "${workspaceFolder}"
        }
    ]
```

若不修改program一项，则会报找不到程序错误。