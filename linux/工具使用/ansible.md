# ansible

## 命令

``` bash
ansible testhost1 -m copy -a "src=/opt/1.txt dest=/opt/" >> /opt/ansible.log  # 将本机文件1.txt拷贝到 testhost1主机中
```