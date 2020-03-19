#!/usr/bin/env python
#coding:utf8
#发送带附件的邮件到指定邮箱

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

filedir='/data/ops/script/sendmai/'
name=time.strftime('%Y%m%d',time.localtime())
file =filedir+name+".xls"

mail_host="smtp.qq.com"  #设置发送邮箱的服务器
mail_user="1300543352@qq.com" #发送邮件的邮箱地址
mail_pass="dqfffznsnojhicae"  #邮箱授权码，非邮箱密码
receivers=['zhumin@qtone.cn','guanruirong@qtone.cn']  #邮件接收人

#创建邮件部分
msg=MIMEMultipart()  # 创建一个带附件的实例
msg["Subject"]=u"贵州黔东南数据邮件" #指定邮件主题，中文值前面要加u，否则邮件乱码
msg["From"]=mail_user  #邮件发送人
msg["To"]=','.join(receivers)  #邮件接收人，如果存在多个收件人，可用join连接

#编辑邮件部分
#-----文字部分-----
part=MIMEText(u"请查收邮件，谢谢",'plain', 'utf-8')
msg.attach(part)

#-----附件部分-----
part=MIMEApplication(open(file,'rb').read())
part.add_header('Content-Disposition', 'attachment', filename=name+".xls")
msg.attach(part)

try:
    s=smtplib.SMTP(mail_host,timeout=30)  # 连接smtp邮件服务器,端口默认是25
    s.login(mail_user,mail_pass)  # 登陆服务器
    s.sendmail(mail_user,receivers,msg.as_string()) # 发送邮件
    s.close()
except Exception as e:
    print "error",e