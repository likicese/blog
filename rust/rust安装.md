# rust安装

## 官网



## 环境

操作系统：debian

## 步骤

[官网](https://www.rust-lang.org/zh-CN/learn/get-started)

由于网络原因，直接使用官网的安装方式很容易失败，所以需要稍微改一下安装脚本

1. 下载安装脚本

    ``` bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > rust-install.sh
    ```

2. 修改下载安装源

    将
    
    RUSTUP_UPDATE_ROOT="${RUSTUP_UPDATE_ROOT:-https://static.rust-lang.org/rustup}"

    改为

    RUSTUP_UPDATE_ROOT="https://mirrors.ustc.edu.cn/rust-static/rustup"

3. 临时修改组件源

    ``` bash
    export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup
    ```

4. 安装

    ``` bash
    chmod u+x rust-install.sh & ./rust-install.sh
    ```

    启动后，会让你选择默认安装还是其他，按1即可

5. 设置组件服务器国内源

    ``` bash
    echo "RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup"  >> ~/.cargo/env
    ```

## 添加环境变量

```
echo 'export PATH=$HOME/.cargo/bin:$PATH' >> /etc/profile
source /etc/profile
```

## 报错解决

1. 缺少编译工具

当创建工程后，执行cargo run的时候，出现如下报错

``` bash
   Compiling hello v0.1.0 (/mnt/c/code/rust/hello)
error: linker `cc` not found
  |
  = note: No such file or directory (os error 2)

error: aborting due to previous error

error: could not compile `hello`.
```

解决

``` bash
apt install gcc

# 或者
apt install build-essential
```

## 检查

运行一个hello world

编辑一个`hello.rs`，内容如下：

```
fn main() {
    println!("Hello World!");
}
```

编译命令：

```
rustc hello.rs
```

执行编译后的文件：

```
./1
```

## 软件包索引

编辑`~/.cargo/config`文件，添加如下内容：

```
[source.crates-io]
replace-with = 'tuna'

[source.tuna]
registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"
```

