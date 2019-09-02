import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

sender = '541002901@qq.com'
password = 'ecerlujhbaahbdib'
mail_host = 'smtp.qq.com'
receivers = ['541002901@qq.com']
msg = MIMEMultipart()
msg['Subject'] = input('subject:')
msg['From'] = sender
msg_content = input('content:')
msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
pic = 'E:\819bca177f3e67091005c94838c79f3df8dc5519_mh1520659582932.jpg'
with open(pic, 'rb') as f:
    mime = MIMEBase('image', 'jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='mmm.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.set_debuglevel(1)
    s.login(sender, password)
    for item in receivers:
        msg['To'] = to = item
        s.sendmail(sender, to, msg.as_string())
        print('Success!')
    s.quit()
except smtplib.SMTPException as e:
    print('Failed,%s' % e)
