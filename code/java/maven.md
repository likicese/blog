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