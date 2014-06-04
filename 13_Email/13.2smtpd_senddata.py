# -*- coding: utf-8 -*-	
import smtplib
import email.utils
from email.mime.text import MIMEText
#Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient','Recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author','Authorg@example.com'))
msg['Subject'] = 'Simple test message'
server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel('Ture') # show communication with the server
try:
	server.sendmail('Recipient@example.com',
					['Authorg@example.com'],
					msg.as_string())
finally:
	server.quit()
