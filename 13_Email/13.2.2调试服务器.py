# -*- coding: utf-8 -*-	
#13.2.2调试服务器
import smtpd
import asyncore
server = smtpd.DebuggingServer(('127.0.0.1', 1025), None)
asyncore.loop()