# -*- coding: utf-8 -*-	
#13.1.2认证和加密
#SMTP类还会处理认证和传输层安全(transport layer security, TLS)加密（如果服务器提供支持）。要确定服务器是否支持TLS，可以直接调用ehlo()为服务器标识客户，询问可以得到哪些扩展。然后调用has_entn()来检查结果。启动TLS之后，在认证之前必须再次调用echlo()
import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass
# Prompt the user for connection info
to_email = raw_input('Recipient: ') #收件邮箱
from_email = raw_input('Author: ')
servername = raw_input('Mail server name: ') #对于gmail是smtp.gmail.com
username = raw_input('Mail username: ') #发件邮箱
password = getpass.getpass("%s' s password: " % username) #密码

#Create the message
msg = MIMEText('Hello World From Python!')
msg.set_unixfrom('author')
msg['To'] = email.utils.formataddr(('Recipient',to_email))
msg['From'] = email.utils.formataddr(('Author', from_email))
msg['Subject'] = 'Test from Python'
server = smtplib.SMTP(servername)
try:
	server.set_debuglevel('Ture')
	# indentify ourselves, prompting server for supported features
	server.ehlo()
	#If we can encrypt this session, do it
	if server.has_extn('STARTTLS'):
		server.starttls()
		server.ehlo() #reidentifu ourselves over TLS connection
	server.login(username, password)
	server.sendmail(from_email,
					[to_email],
					msg.as_string())
finally:
	server.quit()
	
#启用TLS后，STARTTLS扩展不会出现在对EHLO的应答中
