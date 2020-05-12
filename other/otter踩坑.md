# otter踩坑

## 错误

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