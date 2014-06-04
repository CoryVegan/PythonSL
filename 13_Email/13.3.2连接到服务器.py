# -*- coding: utf-8 -*-	
#13.3.2连接到服务器
#要建立与一个IMAP服务器的连接，首先建立套接字连接本身。其次，用服务器上的一个账户作为用户完成认证。该例子会从一个配置文件读取服务器和用户信息。
import imaplib
import ConfigParser
import os
os.chdir('/Users/a')
def open_connection(verbose=False):
	# Read the config file
	config = ConfigParser.ConfigParser()
	config.read([os.path.expanduser('~/.pymotw')])

	#Connect to the server
	hostname = config.get('server', 'smtp.gmail.com')
	if verbose: print 'Connecting to', hostname
	connection = imaplib.IMAP4_SSL(hostname)
	
	#Login to our account
	username = config.get('acount', 'Alex.Fanxing@gmail.com')
	password = config.get('acount', 'fx624418')
	if verbose: print 'Logging in as', username
	conncetion.login(username, password)
	return connection
	
if __name__ == '__main__':
	c = open_connection(verbose=True)
	try:
		print c
	finally:
		c.logout()

