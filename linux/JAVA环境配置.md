# JAVA环境配置

## 一、下载

[JDK下载地址](https://www.oracle.com/technetwork/java/javase/downloads/index.html)  

选择合适自己的发行版本，同意条款后，即可下载。  

本教程用的JDK包是：jdk-8u191-linux-x64.tar.gz

## 二、检查系统的JAVA环境

``` shell
[user@localhost ~]$ rpm -qa | grep java
python-javapackages-3.4.1-11.el7.noarch
java-1.7.0-openjdk-headless-1.7.0.171-2.6.13.2.el7.x86_64
java-1.7.0-openjdk-1.7.0.171-2.6.13.2.el7.x86_64
java-1.8.0-openjdk-headless-1.8.0.161-2.b14.el7.x86_64
java-1.8.0-openjdk-1.8.0.161-2.b14.el7.x86_64
tzdata-java-2018c-1.el7.noarch
javapackages-tools-3.4.1-11.el7.noarch
```

由于安装的是GNOME版本的CentOS，所以带有openjdk，得卸载

## 三、卸载openjdk

``` shell
[user@localhost ~]$ sudo rpm -e --nodeps java-1.7.0-openjdk-1.7.0.171-2.6.13.2.el7.x86_64
[user@localhost ~]$ sudo rpm -e --nodeps java-1.8.0-openjdk-1.8.0.161-2.b14.el7.x86_64
[user@localhost ~]$ sudo rpm -e --nodeps java-1.8.0-openjdk-headless-1.8.0.161-2.b14.el7.x86_64
[user@localhost ~]$ sudo rpm -e --nodeps java-1.7.0-openjdk-headless-1.7.0.171-2.6.13.2.el7.x86_64
```

## 四、检查卸载状况

``` shell
[user@localhost ~]$ rpm -qa | grep java
python-javapackages-3.4.1-11.el7.noarch
tzdata-java-2018c-1.el7.noarch
javapackages-tools-3.4.1-11.el7.noarch
[user@localhost ~]$ java -version
bash: java: command not found...
```

## 五、释放JDK文件

将文件解压到/usr/local/目录下

``` shell
[user@localhost ~]$ sudo tar -zxf jdk-8u191-linux-x64.tar.gz -C /usr/local
```

## 六、配置环境变量

编辑系统环境变量文件：/etc/profile

 ``` shell
 [user@localhost ~]$ sudo vi /etc/profile
 ```

到最底部，加入如下内容：

> #set java environment  
> export JAVA_HOME=/usr/local/jdk1.8.0_191  
> export JRE_HOME=${JAVA_HOME}/jre  
> export CLASSPATH=.:${JAVA_HOME}/lib/dt.JAVA_HOME/lib/tools.jar:${JRE_HOME}/lib  
> export PATH=${JAVA_HOME}/bin:${PATH}  

重新加载环境变量

``` shell
[user@localhost ~]$ source /etc/profile
```

## 七、检查安装结果

如下，则安装成功

``` shell
[user@localhost ~]$ java -version
java version "1.8.0_191"
Java(TM) SE Runtime Environment (build 1.8.0_191-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.191-b12, mixed mode)
```