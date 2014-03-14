# -*- coding: utf-8 -*-	
#array模块定义了一个序列数据结构，和list相似，不过所有成员必须是相同的基本类型
#2.2.1初始化
import array
import binascii
s = 'This is the array.'
a = array.array('c', s)

print 'As string:', s
print 'As array :', a
print 'As hex   :', binascii.hexlify(a)
print
#2.2.2处理数组
import array
import pprint
a = array.array('i', xrange(3))
print 'Initial :', a
a.extend(xrange(3))
print 'Extended:', a
print 'Slice   :', a[2:5]
print 'Iterator:'
print list(enumerate(a))
print
#2.2.3数组与文件
#可以使用高效读写文件的专用内置方法将数组的内容写入文件或从文件读入数组
import array
import binascii
import tempfile
a = array.array('i', xrange(5))
print 'A1:', a
#Write the array of numbers to a temporary file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file) #must pass an *actual* file
output.flush()
#read the raw data
with open(output.name, 'rb') as input:
	raw_data = input.read()
	print 'Raw Contents:', binascii.hexlify(raw_data)
	#Read the data into an array
	input.seek(0)
	a2 = array.array('i')
	a2.fromfile(input, len(a))
	print 'A2:', a2
#这个例子展示了直接从二进制文件读取原始数据，将它读入一个新的数组，并把字节转换为适当的类型