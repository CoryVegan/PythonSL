# -*- coding: utf-8 -*-	
#12.3urllib网络资源访问
#访问不需要验证的远程资源,cookie等等
#urllib模块为网络资源访问提供了一个简单的借口。它还包括一些函数用于对参数编码和加引号，以便通过HTTP传递到一个服务器。
#12.3.1利用缓存实现简单获取
print '12.3.1利用缓存实现简单获取'
#下载数据是一个很常见的从左，urllib提供了urlretrieve()函数来满足这个需要。urlretrieve()的参数包括一个URL，存放数据的一个临时文件和一个报告下载进度的函数，另外如果URL指示一个表单，要求提交数据，那么urlretrieve()还要有一个参数表示要传递的数据。如果没有给指定文件名，urlretrieve()会创建一个临时文件。调用程序可以直接删除这个文件，或者将这个文件作为一个缓存，使用urlcleanup()将其删除。
#下面这个例子使用HTTP GET请求从一个Web服务器获取数据。
import urllib, os
def reporthook(blocks_read, block_size, total_size):
	"""total_size is reaported in bytes.
	block_size is the amount read each time.
	blocks_read is the number of blocks successfully read.
	"""
	if not blocks_read:
		print 'Conncetion opened'
		return
	if total_size < 0:
		# Unknown size
		print 'Read %d blocks (%d bytes)' % (blocks_read, blocks_read * block_size)
	else:
		amount_read = blocks_read * block_size
		print 'Read %d blocks, or %d/%d' % (blocks_read, amount_read, total_size)
	return


filename, msg = urllib.urlretrieve('http://blog.doughellmann.com/',reporthook=reporthook)
print
print 'File:', filename
print 'Headers:'
print msg
print 'File exists before cleanup:', os.path.exists(filename)

urllib.urlcleanup()
print 'File still exists:', os.path.exists(filename)

#每次从服务器读取数据时，会调用reporthook()报告下载进度。这个函数的3个参数分别是目前为止读取的快熟、快的大小（字节数），以及正在下载的资源的大小（字节数）。服务器没有返回Content-length首部时，urlretrieve()不知道数据有多大，为total_size参数传入-1.

#12.3.2参数编码
print '\n12.3.2参数编码'
#可以对参数编码并追加到URL，从而将它们传递到服务器
query_args = {'q':'query string', 'foo':'bar'}
encoded_args = urllib.urlencode(query_args)
print 'Encoded:', encoded_args

url = 'http://localhost:8000/' + encoded_args
print urllib.urlopen(url).read()
#客户值列表中，查询包含了已编码的查询参数
#要使用变量的不同出现向查询串传入一个值序列，需要在调用urlencode()时将doseq设置为True

query_args = {'foo':['foo1', 'foo2']}
print 'Single  :', urllib.urlencode(query_args)
print 'Sequence:', urllib.urlencode(query_args, doseq=True)
#结果是一个查询串，同一个名称与多个值关联,要对这个查询串解码，参见cgi模块的FieldStorage类。
#查询参数中可能有一些特殊字符，在服务器端对URL解析时这些字符会带来问题，所以在传递到urlencode()时要对这些特殊字符“加引号”。要在本地对特殊字符加引号从而得到字符串的“安全”版本，可以直接shiyongquote()或quote_plus()函数
url = 'http://localhost:8000/~Sterncat/'
print 'urlencode() :', urllib.urlencode({'url':url})
print 'quote()     :', urllib.quote(url)
print 'quote_plus():', urllib.quote_plus(url)
#quote_plus()实现的加引号处理会更大程度地替换相应字符。
#要完成加引号操作的逆过程，可以根据需要相应地使用unqote()或unquote_plus()
print urllib.unquote('http%3A%2F%2Flocalhost%3A8000%2F%7ESterncat%2F')
print urllib.unquote_plus('http%3A%2F%2Flocalhost%3A8000%2F%7ESterncat%2F')
#编码值会转换回一个常规的URL字符串

#12.3.3路径与URL
print '\n12.3.3路径与URL'
#有些操作系统在本地文件和URL中使用不同的值分隔路径的不同部分。为了保证代码可移植，可以使用函数pathname2url()和url2pathname()来回转换
import os
from urllib import pathname2url, url2pathname
print '== Default =='
path = '/a/b/c'
print 'Original:', path
print 'URL     :', pathname2url(path)
print 'Path    :', url2pathname('/d/e/f')
print
from nturl2path import pathname2url, url2pathname
print '== Windows, without drive letter =='
path = r'\a\b\c'
print 'Original:', path
print 'URL     :', pathname2url(path)
print 'Path    :', url2pathname('/d/e/f')
print
print '== Windows, with drive letter =='
path = r'C:\a\b\c'
print 'Original:', path
print 'URL     :', pathname2url(path)
print 'Path    :', url2pathname('/d/e/f')
#这里有两个Windows的例子，其路径前缀中分别包含和不包含驱动器字母