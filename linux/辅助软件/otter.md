# otter

## 使用

### 批量添加

例子

在批量添加的框里，填入以下文字，保存即可



``` config
mg,user,5,mc,user,2
mg,group,5,mc,group,2
mg,ip,5,mc,ip,2
```

解释：

source_schema, source_table, source_id（在otter中加入源时获得）, target_schema, target_table, target_id（在otter中加入源时获得）

## canal

填入的应是源库地址、用户名和密码

## 踩坑

1. mysql默认值错误，导致建表异常
   
   错误提示：
   ``` txt
   ERROR 1067 (42000): Invalid default value for 'GMT_CREATE'
   ```

   错误原因：
   用 `show variables like 'sql_mode';` 可知，`NO_ZERO_DATE` 应为 `ALLOW_INVALID_DATES`

   错误解决：
   ``` sql
   set sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,ALLOW_INVALID_DATES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
   ```

   重新登录mysql后，参数设置又会回去