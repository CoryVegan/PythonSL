# -*- coding: utf-8 -*-	
#12.2BaseHTTPServer实现Web服务器的基类
#BaseHTTPServer使用SocketServer的类创建基类，用来建立HTTP服务器。HTTPServer可以直接使用，不过BaseHTTPRequest需要扩展来处理各个协议方法(GET,POST等等)
#12.2.1HTTP GET
print '12.2.1HTTP GET\n'
#要在一个请求处理器类中添加一个HTTP方法支持，需要实现方法do_METHOD()，这里的METHOD要替换为具体的HTTP方法名(例如，do_GET(),do_POST()等等)。为保持一致，请求处理器方法不带任何参数。请求的所有参数都由BaseHTTPRequestHandler解析，并储存为请求实例的实例属性。
#下面这个示例请求处理器展示了如何向客户返回一个响应，其中包含对构建响应可能有用的一些本地属性，
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		message_parts = [
				'CLIENT VALUES:',
				'client_address=%s (%s)' % (self.client_address,self.address_string()),
				'command=%s' % self.command,
				'path=%s' % self.path,
				'real path=%s' % parsed_path.path,
				'query=%s' % parsed_path.query,
				'request_version=%s' % self.request_version,
				'',
				'SERVER VALUES:',
				'server_version=%s' % self.server_version,
				'sys_version=%s' % self.sys_version,
				'protocol_version=%s' % self.protocol_version,
				'',
				'HEADERS RECEIVERD:'
				]
		for name, value in sorted(self.headers.items()):
			message_parts.append('%s=%s' % (name,value.rstrip()))
		message_parts.append('')
		message = '\r\n'.join(message_parts)
		self.send_response(200)
		self.end_headers()
		self.end_headers()
		self.wfile.write(message)
		return

if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('localhost', 8080), GetHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()

#先组装消息文本，然后写至wfile，这是包装了响应套接字的文件句柄。每个相应需要一个响应码，通过send_response()设置。如果使用了一个错误码(404,501等等)，首部都会包含一个相应的默认错误消息，或许可能会随这个错误码传递一个消息。要在服务器中运行请求处理器，需要将它传递到HTTPServer的构造函数，如示例脚本中__main__c处理部分所示。启动服务器，在另外一个终端使用curl来访问这个服务器。
#curl -i http://localhost:8080/?foo=bar