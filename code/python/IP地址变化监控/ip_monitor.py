#!/usr/bin/python3

import smtplib
import re
from email.mime.text import MIMEText
import requests
import urllib.request as ure
import datetime

ip_file_path = "/home/pi/script/external_ip_monitor/ip.txt"


def get_now_date():
    d = datetime.datetime.now()
    return d.strftime("%Y-%m-%d %H:%M:%S")

def send_email(ip):
    # 你的邮箱地址
    email_name = "userName@126.com"
    # 发邮件的署名
    from_name = "userName@126.com"
    # 你的smtp密码。此密码不等同于登录密码
    password = "passWrod"
    # 使用邮箱服务的地址
    smtp_server = "smtp.126.com"
    
    username = email_name
    sender = email_name
    receiver = [email_name]
    

    subject = "IP地址变更提醒"

    msg = MIMEText("您的IP地址已变更为：" + ip, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_name
    msg['To'] = ";".join(receiver)

    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def get_new_ip():
    my_ip = ure.urlopen('http://ip.42.pl/raw').read()
    return my_ip.decode("utf-8")

def get_old_ip():
    with open(ip_file_path, 'r') as f:
        old_ip = f.read()
    return old_ip

def set_new_ip(ip):
    with open(ip_file_path, 'w') as f:
        f.write(ip)

if __name__ == '__main__':
    print(get_now_date())
    new_ip = get_new_ip()
    print(new_ip, " test ", get_old_ip())
    if new_ip != get_old_ip():
        send_email(new_ip)
        set_new_ip(new_ip)