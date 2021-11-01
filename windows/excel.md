# excel

## 无法用excel直接打开文件的问题

修改注册表

修改路径：计算机\HKEY_CLASSES_ROOT\Excel.Sheet.12\shell\Open\command

将值，从

``` 
"C:\Program Files (x86)\Microsoft Office\Root\Office16\EXCEL.EXE"/d
```

改为：

``` 
"C:\Program Files\Microsoft Office\Root\Office16\EXCEL.EXE" "%1"
```