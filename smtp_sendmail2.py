import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

sender = '541002901@qq.com'
password = 'fi355690'
mail_host = 'smtp.qq.com'
receivers = ['2014650646@qq.com']
message = MIMEText('content', 'plain', 'utf-8')
message['Subject'] = 'title'
message['From'] = sender
message['To'] = receivers[0]
try:
    smtpObj = smtplib.SMTP()
    # smtpObj.connect(mail_host)
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print('Success!')
except smtplib.SMTPException as e:
    print(e)