# -*- coding: utf-8 -*-	
#6.3linecache高效读取文本文件
#作用：从文件或导入的Python模块获取文本行，维护一个结果缓存，从而可以更高效地从相同文件读取多行文本
#处理Python源文件时，linecache模块会在Python标准库的其他部分中用到。缓存实现将在内存中保存文件的内容（解析为单独的行）。API通过索引一个list返回所请求的行，与反复地读取文件并解析文本来查找所需文本行相比，这样可以节省时间。这个方法在查找同一文件中的多行时尤其有用，比如为一个错误报告生生一个跟踪记录（traceback）
#6.3.1测试数据
#6.3.2读取特定行
#linecache模块读取的文件行号从1开始，不过通常列表的数组索引会从0开始
import linecache
from linecache_data import *
filename = make_tempfile()
#Pick out tha same line from source and cache.
#(Notice that linecache counts from 1)
print 'SOURCE:'
print '%r' % lorem.split('\n')[4]
print
print 'CACHE'
print '%r' % linecache.getline(filename, 5)
cleanup(filename)
print
#6.3.3处理空行
#返回值通常在行末尾都包括一个换行符，所以如果文本行为空，那么返回值就是一个换行符
filename = make_tempfile()
#Blank lines include the newline
print 'BLANK : %r' % linecache.getline(filename, 8)
cleanup(filename)
#6.3.4错误处理
#如果所请求的行号超出了文件中合法行号的范围，getline()会返回一个空串
filename = make_tempfile()
#The cache always returns a string, and uses
#an empty string to indicate a line which does
#not exist
not_there = linecache.getline(filename, 500)
print 'NOT THERE: %r includes %d characters' % \
(not_there, len(not_there))
print
#输入文件只有12行，所以请求第500行就像是试图与越过文件末尾继续读文件
#读取一个不存在的文件时，也采用同样的方式处理
#调用者使用读取数据时，这个模块不会产生异常
no_such_file = linecache.getline('this_file_does_not_exist.txt', 1)
print 'NO FILE : %r' % no_such_file
#6.3.5读取Python源文件
#由于linecache在生成traceback跟踪记录时使用相当频繁，其关键特性之一就是能通过指定模块的基名在导入路径中查找Python源模块
import os
#Look for the linecache module, using
#the built in sys.path search
module_line = linecache.getline('linecache.py', 3)
print 'MODULE:'
print repr(module_line)
# Look at the linecache module source directly
file_src = linecache.__file__
if file_src.endswith('.pyc'):
	file_src = file_src[:-1]
print '\nFILE:'
with open(file_src, 'r') as f:
	file_line = f.readlines()[2]
print repr(file_line)
#如果linecache中的缓存填充代码在当前目录中无法找到指定名的文件，它会在sys.path中搜索制定名的模块。