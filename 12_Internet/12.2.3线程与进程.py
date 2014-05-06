# -*- coding: utf-8 -*-	
# 12.2.3线程与进程
#HTTPServer是SocketServer.TCPServer的一个简单子类，并不使用多线程或多进程来处理请求。要增加线程或进程，需要使用相应的mix-in技术从SocketServer创建一个新类。
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
class Handler( BaseHTTPRequestHandler ):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return

class ThreadedHTTPServer( ThreadingMixIn, HTTPServer ):
    """Handle requests in a separate thread."""
if __name__ == '__main__':
	server = ThreadedHTTPServer(('localhost', 8080), Handler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()
#curl http://localhost:8080/
#每次服务器接收到一个请求时，它会开始一个新线程或进程来处理这个请求。
#用ForKingMixIn替换ThreadingMixIn会得到类似的结果，不过会使用单独的进程而不是线程。