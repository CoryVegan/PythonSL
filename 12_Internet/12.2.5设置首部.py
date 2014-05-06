# -*- coding: utf-8 -*-	
#12.2.5设置首部
#send_header方法将向HTTP响应添加首部数据。这个方法有两个参数：首部名和值
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, time
class GetHandler( BaseHTTPRequestHandler ):
    def do_GET(self):
		self.send_response(200)
		self.send_header( 'Last-Modified', self.date_time_string(time.time()) )
		self.end_headers()
		self.wfile.write('Response body.\n')
		return
		
if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('localhost', 8080), GetHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()
#curl -i http://localhost:8080/

#这个例子将Last_Modified首部设置为当前时间戳（按照RFC 2822格式化）