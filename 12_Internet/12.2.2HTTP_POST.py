# -*- coding: utf-8 -*-	
# 12.2.2HTTP POST
#支持POST请求需要多做一些工作，因为基类不会自动解析表单数据。cgi模块提供了FieldStorage类，如果给定了正确的输入，它知道如何解析表单。
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
class PostHandler( BaseHTTPRequestHandler ):
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers=self.headers,
            environ={ 'REQUEST_METHOD':'POST', 
                      'CONTENT_TYPE':self.headers['Content-Type'],
                    }
        )
        
        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Client: %s\n" % str( self.client_address ))
        self.wfile.write("User Agent: %s\n" % str( self.headers['User-Agent'] ))
        self.wfile.write("Path: %s\n" % str( self.path ))
        self.wfile.write("Form data:\n")
        
        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The filename contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write("\t Uploaded %s as '%s' (%d bytes)\n" % \
                    (field, field_item.filename, file_len)
                )
            else:
                # Regular form value
                self.wfile.write( "\t%-10s : %s\n" %( field, form[field].value ) )
         
        return
if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('localhost', 8080), PostHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()
#通过使用-F选项，curl的参数可以包括将提交给服务器的表单数据。最后一个参数将提交文件xx.py的内容，来展示如何从表单读取文件数据
#curl http://localhost:8080/?foo=bar -F name=dhellmann -F foo=bar -F xx.py