# nginx

## 关键词

[官网连接](http://nginx.org/)
俄罗斯人编写 | 事件驱动 | 5万并发连接数
分阶段资源分配技术：维持1万个无活动连接，仅需2.5M内存
异步非阻塞：

## URL和URI的区别

### 一、URI

Universal Resource Identifier 统一资源标识符

### 二、URL

Universal Resource Locator 统一资源定位符

### 三、转发错误

如果proxy_pass中包含URI，则会用proxy_pass进行转发。  
如果proxy_pass中不包含URI，则会用外界请求地址进行转发

## 负载均衡

### 一、均衡策略

1. 轮询（默认策略）
   ``` conf
   http {
    upstream appName {
        server example1.com;
        server example2.com;
        server example3.com;
    }
    server {
        listen 80;

        location / {
            proxy_pass http://appName;
        }
    }
   }
   ```
2. 最少连接数
   ``` conf
    upstream appName {
        least_conn;
        server example1.com;
        server example2.com;
        server example3.com;
    }
   ```
3. ip-hash：集群中的服务器 = hash（请求的IP）
   优点：来自同一地址的请求总是会被转发到同一台服务器
   ``` conf
    upstream appName {
        ip_hash;
        server example1.com;
        server example2.com;
        server example3.com;
    }
   ```
4. 加权轮询
   ``` conf
    upstream appName {
        server example1.com weight = 4;
        server example2.com;
        server example3.com;
    }
   ```

## server的格式

server的格式为：server address [parameters]

parameter有许多参数，官网：http://nginx.org/en/docs/http/ngx_http_upstream_module.html#server

简要介绍：
weight = number ：指定负载均衡加权模式时的权重，默认该值为1
max_conns = number ：最大连接数
max_fails = number ：默认为1。值0则不尝试。最大失败次数。达此次数后，nginx会开始查询该服务器是否能够正常提供服务

fail_timeout = time ：默认为10s

backup ：备用服务器。主服务器不可用时，启用备用服务器
down ：标记服务器不可用。
resolve ：监控DNS的修改，并自动跟进修改
route = string ：设定服务器的路由名字
service = name ：
slow_start = time ：
drain ：进入 "draining" 模式。除非被绑定，否则请求不会被处理