import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

mail_host = 'smtp.qq.com'
mail_user = '263867208@qq.com'
mail_pass = 'hvtagvsynakcbjga'

sender = '263867208@qq.com'

receviers = ['1686886012@qq.com']



mail_msg = """
<p>Python 邮件发送测试...</p>

<p><a href="https://blog.csdn.net/nanruitao10">关注我</a></p>
<p><img src="cid:image1"></p>
"""

message=MIMEMultipart('related')

subject = 'Python邮箱测试'
message['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receviers, message.as_string())
    print("success")
except smtplib.SMTPException as e:
    print("fail"+e.with_traceback())
