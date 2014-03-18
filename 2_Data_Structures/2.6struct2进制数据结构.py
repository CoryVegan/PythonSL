# -*- coding: utf-8 -*-	
#struct提供了一组处理结构值的模块级函数，另外还有一个Struct类。格式指示符由字符串格式转换为一种编译表示，这与处理正则表达式的方式类似。这个转换会耗费资源，所以当创建一个Struct实例并在这个实例上调用方法时（而不是使用模块级函数），完成一次转换会更为高效。下面的例子都会使用'Struct'类。
#2.6.2打包和解包
import struct
import binascii
values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)
print 'Original values:', values
print 'Format string  :', s.format
print 'Uses           :', s.size, 'bytes'
print 'Packed Value   :', binascii.hexlify(packed_data)
#这个例子将打包的值转换为一个十六进制字节序列，以便利用binascii.hexlify()打印，因为有些字符是null
print
#使用unpack()可以从打包数据中抽取数据

import struct
import binascii
packed_data = binascii.unhexlify('0100000061620000cdcc2c40')
s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
print 'Unpacked Values:', unpacked_data
print
#2.6.3字节序 某些情况下，值会使用内置c库的字节序来编码。只需在格式串中提供一个显式的字节序指令，就可以很容易地覆盖这个默认选择。
import struct
import binascii
values = (1, 'ab', 2.7)
print 'Original values:', values
endianness = [
	('@', 'native, native'),
	('=', 'native, standard'),
	('<', 'little-endian'),
	('>', 'big-endian'),
	('!', 'network'),
	]
for code, name in endianness:
	s = struct.Struct(code + 'I 2s f')
	packed_data = s.pack(*values)
	print
	print 'Format string  :', s.format, 'for', name
	print 'Uses           :', s.size, 'bytes'
	print 'Packed Value   :', binascii.hexlify(packed_data)
	print 'Original values:', s.unpack(packed_data)
#struct使用的字节序指示符 @内置顺序 =内置标准 <小端 >大端 !网络顺序

#2.6.4缓冲区 通常在重视性能的情况下或者向扩展模块传入或传出数据时才会处理二进制打包数据。通过避免为每个打包结构分配一个新的缓冲器所带来的开销，可以优化这些情况。pack_into()和unpack_from()方法支持直接写入预分配的缓冲区。
import struct
import binascii
s = struct.Struct('I 2s f')
values = (1, 'ab', 2.7)
print 'Origianl:', values
print
print 'ctypes string buffer'
import ctypes
b = ctypes.create_string_buffer(s.size)
print 'Before  :', binascii.hexlify(b.raw)
s.pack_into(b, 0, *values)
print 'After   :', binascii.hexlify(b.raw)
print 'Unpacked:', s.unpack_from(b, 0)
print 
print 'array'
import array
a = array.array('c', '\0' * s.size)
print 'Before  :', binascii.hexlify(a)
s.pack_into(a, 0, *values)
print  'After  :', binascii.hexlify(a)
print 'Unpacked:', s.unpack_from(a, 0)