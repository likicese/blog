# ansible

## 安装

``` bash
yum install -y python3
pip3 install -U pip
pip3 install ansible
```

### 报错

#### No module named 'setuptools_rust'

原因：pip版本过低

解决：升级pip版本即可

``` bash
pip3 install -U pip 
```

## 使用

### 解决python版本过低，提示DEPRECATION WARNING的问题

``` bash
mkdir /etc/ansible/
cat > /etc/ansible/ansible.cfg << EOF
[defaults]
deprecation_warnings=False
EOF
```

## 添加配置

``` bash
mkdir /var/log/ansible/
cat >> /etc/ansible/ansible.cfg << EOF
host_key_checking = False
log_path = /var/log/ansible/ansible.log
EOF

```

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
ansible testhost1 -m script -a "/opt/1.sh" >> /opt/ansible.log  # 在远程主机上执行脚本 /opt/1.sh
```

## ansible-playbook

创建文件/opt/1.yaml，文件内容如下

``` yaml
- name: 在远程主机上执行命令
  hosts: testhost1
  user: root
  tasks:
    - name: echo str
      command: echo "str" > /tmp/1.txt
````

执行以下命令，即可执行

``` bash
ansible-playbook /opt/1.yaml
ansible-playbook /opt/1.yaml --limit 192.168.1.10  # 只选择192.168.1.10这台机器
ansible-playbook /opt/1.yaml --step  # 每一个task输入y或n在判定是否执行
```

显示执行结果的例子

``` yaml
- name: 显示远程根目录文件（使用debug模式，可以显示结果）
  hosts: testhost1
  user: root
  tasks:
    - name: show root
      command: ls /
      register: shell_result
    - debug:
        var: shell_result.stdout_lines
```

### 在远程主机安装软件

```yaml
- hosts: dev:!192.168.1.11:!192.168.1.15  # 排除掉192.168.1.11和192.168.1.15这两台机器
  gather_facts: no  # 关闭获取硬件信息
  tasks:
  - name: 拷贝文件到远程机器
    copy:
      src: /tmp/downloads/node.rpm
      dest: /tmp/node.rpm
  - name: 安装node
    shell: sudo yum install -y /tmp/node.rpm
  - name: 查看软件
    shell: rpm -q node
    register: show_software
  - name: 启动node
    shell: sudo systemctl start node
  - debug: var=show_software.stdout_lines  # 输出命令执行结果
```

