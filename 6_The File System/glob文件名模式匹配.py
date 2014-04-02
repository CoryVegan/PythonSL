# -*- coding: utf-8 -*-	
#6.2glob文件名模式匹配：作用：使用Unix Shell规则查找一个与模式匹配的文件名
#6.2.1示例文件夹
#6.2.2通配符
#星号*匹配一个文件名段中的0个或多个字符，例如，dir/*
import glob
for name in glob.glob('dir/*'):
	print name
print
#这个模式会匹配目录dir中的所有路径名（文件或目录），但不会进一步递归搜索到子目录
#要列出子目录的文件，必须把子目录包含在模式中
print 'Named explicitly:'
for name in glob.glob('dir/subdir/*'):
	print '\t', name
print 'Named with wildcard:'
for name in glob.glob('dir/*/*'):
	print '\t', name
print 
#前面显示的第一种情况显式列出了子目录名，第二种情况则依赖一个通配符查找目录
#6.2.3单字符通配符，问好?也是一个通配符，它会匹配文件名中该位置的单个字符
for name in glob.glob('dir/file?.txt'):
	print name
print 
#6.2.4字符区间
#如果使用字符区间([a-z])而不是问号，可以匹配多个字符中的一个字符。下面这个例子会查找扩展名前名字中有一个数字的所有文件
import glob
for name in glob.glob('dir/*[0-9].*'):
	print name
#字符区间[0-9]会匹配所有单个数字。也可以写作[0123456789]