# -*- coding: utf-8 -*-	
#SMTP协议包括一个命令来询问服务器地址是否合法。通常,VRFY是禁用的，以避免垃圾邮件工具(spammer)查找到合法的Email地址。不过，如果启用这个命令，客户可以询问服务器一个地址是否合法，并接收一个状态吗指示其合法性，同时提供用户的全名（如果有）。
import smtplib
server = smtplib.SMTP('mail')
server.set_debuglevel(True) #Show communication with server
try:
	dhellmann_result = server.verify('dhellmann')
	notthere_result = server.verify('notthere')
finally:
	server.quit()
print 'dhellmann:', dhellmann_result
print 'notthere', notthere_result