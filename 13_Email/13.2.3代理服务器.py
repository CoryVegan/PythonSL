# -*- coding: utf-8 -*-	
#13.2.3代理服务器
import smtpd
import asyncore
server = smtpd.PureProxy(('127.0.0.1', 1025), ('mail', 25))
asyncore.loop()