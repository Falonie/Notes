from email.mime.text import MIMEText
msg=MIMEText('Hello,python!','plain','utf-8')
#Email address and password
from_addr=input('From:')
password=input('Password:')
#input receiver's address
to_addr=input('To:')
#input SMTP Server address
smtp_server=input('SMTP server:')

import smtplib
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()