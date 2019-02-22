import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '263867208@qq.com'
mail_pass = 'hvtagvsynakcbjga'

sender = '263867208@qq.com'

receviers = ['1686886012@qq.com', '263867208@qq.com']

'''
#第一种，简单文本邮件
mail_msg='这是测试'
message=MIMEText(mail_msg,'plain','utf-8')
'''

#第二种，HTML邮件
mail_msg = """
<p>Python 邮件发送测试...</p>

<p><a href="https://blog.csdn.net/nanruitao10">关注我</a></p>
"""
message=MIMEText(mail_msg,'html','utf-8')

subject = 'Python邮箱测试'
message['Subject'] = Header(subject, 'utf-8')

'''
# 第三种，带附件邮件
mail_msg = "python 邮件测试"
message = MIMEMultipart()
message['From'] = Header('南小瓜', 'utf-8')
message['To'] = Header('test', 'utf-8')

subject = 'Python邮箱测试'
message['Subject'] = Header(subject, 'utf-8')

message.attach(MIMEText(mail_msg, 'plain', 'utf-8'))

# 构建附件
att = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="test.txt"'

message.attach(att)
'''
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receviers, message.as_string())
    print("success")
except smtplib.SMTPException as e:
    print("fail"+e.with_traceback())
