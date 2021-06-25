#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

stmp_server='192.168.1.4'
stmp_port=25
stmp_username='123456@qq.com'
stmp_password='123456'
from_addr=u'123456@qq.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def send_mail(mailto,mailsubject,mailcontent):
    msg = MIMEText('测试邮件%s',  mailcontent, 'utf-8')
    msg['From'] = _format_addr(u'测试%s' % from_addr)
    msg['To'] = _format_addr(u'邮箱 <%s>' % mailto)
    msg['Subject'] = Header(mailsubject, 'utf-8').encode()

    server = smtplib.SMTP(stmp_server,stmp_port)
    #server.set_debuglevel(1)
    server.starttls()
    # server.login(stmp_username, stmp_password)  # 若有密码，则需要这步，没有则不需要
    server.sendmail(from_addr, [mailto], msg.as_string())
    server.quit()

if __name__ == '__main__':
    send_mail(sys.argv[1],sys.argv[2],sys.argv[3])