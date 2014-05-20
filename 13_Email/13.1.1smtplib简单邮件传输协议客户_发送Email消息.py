# -*- coding: utf-8 -*-	
#smtlib与邮件服务器通信来传送消息。smtpd可以用于创建定制的邮件服务器，它提供了一些很有用的类，可以再其他应用中调试Email传输
#imaplib使用IMAP协议管理储存在服务器上的消息。它为IMAP客户提供了一个底层API，可以查询、获取、移动和删除消息
#利用mailbox，可以使用多种标准格式创建和修改本地消息归档，包括流行的mbox和Maildir格式，这时很多Email客户程序使用的格式

#13.1_smtplib简单邮件传输协议客户
print '13.1_smtplib简单邮件传输协议客户\n'
#作用：与SMTP服务器交互，包括发送Email
#smtplib包括一个SMTP类，可以用来与邮件服务器通信发送邮件
#13.1.1发送Email消息
print '13.1.1发送Email消息'
#SMTP最常见的用法就是连接到邮件服务器发送消息。可以把邮件服务器主机名和端口传递到构造函数，也可以显式调用connect()。一旦连接，可以调用sendmail()并提供信封参数和消息体。消息文本要完整并遵循RFC2882,因为smtplib根本不会修改内容或首部。这说明，调用者需要添加From和To首部
import smtplib
import email.utils
from email.mime.text import MIMEText
#Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient','recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author','author@example.com'))
msg['Subject'] = 'Simple test message'
server = smtplib.SMTP('mail')
server.set_debuglevel('Ture') # show communication with the server
try:
	server.sendmail('author@example.com',
					['recipient@example.com'],
					msg.as_string())
finally:
	server.quit()
	
#sendmail()的第二个参数，即接受者，会作为一个列表传递。这个列表中可以包括任意多个地址，将把消息按顺序逐个传送到各个地址。由于信封信息与消息首部是分开的，所以通过把地址包含在方法参数中而不是置于消息首部，可以实现暗送(blind carbon copy, BCC)