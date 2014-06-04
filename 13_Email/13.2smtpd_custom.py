# -*- coding: utf-8 -*-	
#13.2smtpd示例邮件服务器
#13.2.1邮件服务器基类
import smtpd
import asyncore
class CustomSMTPServer(smtpd.SMTPServer):
	def process_message(self, peer, mailfrom, rcpttos, data):
		print 'Receiving message from:', peer
		print 'Message addressed from:', mailfrom
		print 'Message addressed to  :', rcpttos
		print 'Message length        :', len(data)
		return
server = CustomSMTPServer(('127.0.0.1', 1025), None)
asyncore.loop()
