# -*- coding: utf-8 -*-	
# 12.2.4处理错误
#处理错误时要调用send_error()，并传入适当的错误码和一个可选的错误消息，整个相应（包括首部、状态吗和相应体）会自动生成。
from BaseHTTPServer import BaseHTTPRequestHandler
class ErrorHandler( BaseHTTPRequestHandler ):
    def do_GET(self):
        self.send_error(404)
        return
if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('localhost', 8080), ErrorHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()
#curl -i http://localhost:8080/
#在这里会返回一个404错误。
#这里使用一个HTML文旦将错误消息报告给可会，并提供一个首部指示错误码。
