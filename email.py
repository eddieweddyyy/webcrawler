import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

#Simple Mail Transfer Protocol

msg = MIMEMultipart('alternative')
content = """
    HTML
"""
part1 = MIMEText(content, "html")
msg.attach(part1)

'''
smtp.gmail.com
Gmail SMTP username:	Your full Gmail address (e.g. you@gmail.com)
Gmail SMTP password:	The password that you use to log in to Gmail
Gmail SMTP port (TLS):	587
Gmail SMTP port (SSL):	465
'''


smtpid = 'tjdals864237@gmail.com'
smtppw = 'ckddnjstkskdl1'
smtp_tls = 587
smtp_ssl = 465

text = 'mail contents'
msg = MIMEText(text)

msg['Subject'] = 'mail title'
msg['From'] = 'email address'
msg['To'] =  'email address'

print(msg.as_string())

with open('file_address', 'rb') as files:
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(files.read())

#files base64 encoding
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="file name w/o address"')
msg.attach(part)

s = smtplib.SMTP('smtp.gmail.com', smtp_tls)
s.starttls()
s.login(smtpid, smtppw)
s.sendmail('tjdals864237@gmail.com', 'tjdals8642@naver.com', msg.as_string())
s.close()