# hadoop

## HDFS

### HDFS设计

1. 超大文件：PB级文件

2. 流式数据访问：一次写入，多次读取

3. 商用硬件：消费级硬件可用

4. 低时间延迟的数据访问：高数据吞吐量应用适合。要求低延迟的应用建议HBase

5. 大量小文件：文件系统的元数据存储于namenode的内存中。故文件数取决于namenode的内存容量

6. 多用户写入：单用户追加写入

### HDFS概念

1. 数据块

小文件不会占满整个块

默认为128MB。最小化寻址开销。简化分布式系统设计。`fsck` 可对文件系统进行检查。

2. namenode 和 datanode

namenode：命名空间镜像文件和编辑日志文件

datanode：工作节点

容灾的2种方法：1、主namenode，从namenode，从滞后于主，主死则从接管主的工作。2、持久元数据，同步写入NFS。

3. 块缓存

频繁读取的文件会被存储于内存中，一块存于一个datanode

4. 联邦HDFS

一个namenode存储一个目录下的元文件

5. HDFS高可用

大型集群，冷启需30分钟

高可用架构修改：namenode之间编辑日志共享。datanonde向两个namenode发送数据块处理报告。客户端特殊设定namenode的转换（对用户透明）。辅助被备用包含，备用给活动的设定周期检查点

高可用共享储存：NFS过滤器、群体日志管理器（QJM，quorum journal manager）

同一时间QJM仅允许一个namenode向编辑日志中写入数据。NFS过滤器则不行

客户端的故障转移则是设定一个URI，客户端应访问每个namenode，直到有回应

