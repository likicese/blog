# maven

## 仓库说明

snapshot仓库（频繁变动的jar，从此仓库总能取到最新jar）

release仓库（已完成阶段性功能开发或bug修复）

第三方jar仓库（存放非公有，其他人开发的jar）

## 命令

``` bash
mvn help:effective-settings  # 查看settings文件的配置，可以获取仓库的地址
```

## 项目创建

``` bash
mvn archetype:generate -DgroupId=com.company.code -DartifactId=testdevops -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false  # 创建项目
```

添加编译指定版本，解决`不再支持源选项 5。请使用 7 或更高版本`之类的问题

``` xml
<project>
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.target>17</maven.compiler.target>
    <maven.compiler.source>17</maven.compiler.source>
  </properties>
</project>
```

## 配置

项目的pom.xml文件中可增加如下配置，即可用命令`mvn deploy`推包。否则需要指定推包地址。

```xml
<project>
    <distributionManagement>
        <repository>
            <id>exmple-release</id>
            <name>display</name>
            <url>https://nexus.exmple.com/repository/release/</url>
        </repository>
        <snapshotRepository>
            <id>exmple-snapshot</id>
            <name>display</name>
            <url>https://nexus.exmple.com/repository/snapshot/</url>
        </snapshotRepository>
    </distributionManagement>
</project>
```

## 推包

根据pom.xml文件设置，版本号带snapshot的包会被推到snapshot仓库。

若要推到release仓库，请执行如下命令，“0.0.2-release”版本号根据项目自身版本号指定，更改版本号进行推送

```bash
mvn deploy versions:set -DnewVersion=0.0.2-release
```
## 上传文件

在settings.xml的servers模块中添入以下内容，以验证用户名和密码

``` xml
<server>
    <id>exmple-release</id>
    <username>exmple-release</username>
    <password>123456</password>
</server>
```

执行以下的shell命令

``` bash
mvn deploy:deploy-file \
-DgroupId=test \
-DartifactId=test \
-Dversion=1.0.0 \
-Dpackaging=jar \
-Dfile=test-1.0.0.jar \
-Durl=https://nexus.exmple.com/repository/release/ \
-DrepositoryId=exmple-release
```