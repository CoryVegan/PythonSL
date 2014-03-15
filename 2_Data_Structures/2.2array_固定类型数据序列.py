# -*- coding: utf-8 -*-	
#array模块定义了一个序列数据结构，和list相似，不过所有成员必须是相同的基本类型
#2.2.1初始化
<<<<<<< HEAD
print '2.2.1初始化\n'
=======
>>>>>>> 4dea9305b7ddff0ae003fa8e220a577c0834f105
import array
import binascii
s = 'This is the array.'
a = array.array('c', s)

print 'As string:', s
print 'As array :', a
print 'As hex   :', binascii.hexlify(a)
print
#2.2.2处理数组
<<<<<<< HEAD
print '2.2.2处理数组\n'
=======
>>>>>>> 4dea9305b7ddff0ae003fa8e220a577c0834f105
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
<<<<<<< HEAD
print '2.2.3数组与文件\n'
=======
>>>>>>> 4dea9305b7ddff0ae003fa8e220a577c0834f105
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
<<<<<<< HEAD
#这个例子展示了直接从二进制文件读取原始数据，将它读入一个新的数组，并把字节转换为适当的类型
print
#2.2.4候选字节顺序
print '2.2.4候选字节顺序\n' 
#如果数组中的数据没有采用固有的字节顺序，或者在发送到一个采用不同字节顺序的系统（或在网络上发送）之前需要交换顺序，可以由Python转换整个数组而无需迭代处理每一个元素
import array
import binascii
def to_hex(a):
	chars_per_item = a.itemsize * 2 #2 hex digits
	hex_version = binascii.hexlify(a)
	num_chunks = len(hex_version) / chars_per_item
	for i in xrange(num_chunks):
		start = i*chars_per_item
		end = start + chars_per_item
		yield hex_version[start:end]

a1 = array.array('i', xrange(5))
a2= array.array('i', xrange(5))
a2.byteswap()

fmt = '%10s %10s %10s %10s'
print fmt % ('A1 hex', 'A1', 'A2 hex', 'A2')
print fmt % (('-' * 10,) * 4)
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
	print fmt % values
=======
#这个例子展示了直接从二进制文件读取原始数据，将它读入一个新的数组，并把字节转换为适当的类型
