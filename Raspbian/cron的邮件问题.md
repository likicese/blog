# cron的邮件问题

在终端，时不时会冒出以下内容：

```
You have new mail in /var/mail/pi
```

使用以下任一命令查看：

```
less /var/spool/mail/pi
mail
```

查看，发现多是定时任务的内容。

再细查，发现定时任务把输出给到邮件正文发过来了……

于是，修改定时任务脚本，输出重定向：

```
/home/pi/task1.sh >> /dev/null
```

再删除邮件：

```bash
echo "" > /var/spool/mail/pi
```

最后关闭提示（可选）：

```bash
echo "unset MAILCHECK">> /etc/profile
```

