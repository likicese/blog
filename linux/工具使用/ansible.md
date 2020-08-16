# ansible

## host
``` config
[testhost1]
192.168.1.[1:100]  # 表示为1~100的IP地址
```

## 命令

``` bash
ansible testhost1 -m copy -a "src=/opt/1.txt dest=/opt/" >> /opt/ansible.log  # 将本机文件1.txt拷贝到 testhost1主机中
ansible testhost1 -m shell -a "cat /opt/1.txt" >> /opt/ansible.log  # 查看testhost1主机上 /opt/1.txt 文件
```