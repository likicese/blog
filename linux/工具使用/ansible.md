# ansible

## hosts

编辑`/etc/ansible/hosts`

### init风格

``` config
[testhost1]
192.168.1.[1:100]  # 表示为1~100的IP地址

[testhost2]
ansible_ssh_port=2222  # 整组通用属性
ansible_ssh_user=admin
ansible_ssh_pass  # ssh的密码
ansible_sudo_pass  # sudo的密码

192.168.1.10
host[a-z]
```

### yaml风格

``` config
vms:
    children:
        vms_1:
            hosts:
                192.168.1.[1:255]:
        vms_2and3:
            hosts:
                192.168.2.[1:255]:
                192.168.3.[1:255]:
```

## 命令

``` bash
ansible testhost1 -m copy -a "src=/opt/1.txt dest=/opt/" >> /opt/ansible.log  # 将本机文件1.txt拷贝到 testhost1主机中
ansible testhost1 -m shell -a "cat /opt/1.txt" >> /opt/ansible.log  # 查看testhost1主机上 /opt/1.txt 文件
```