# -*- coding: utf-8 -*-	
#作用解析，构建，测试以及处理文件名和路径
#6.1.1解析路径,这些函数的本质是只处理字符串
print '6.1.1解析路径\n'
#路径解析依赖于os中定义的一些变量
#os.sep     路径各部分之间的分隔符(例如"/"或"\")
#os.extsep  文件名与文件“扩展名”之间的分隔符(例如".")
#os.pardir  路径中表示目录树上一级的部分(例如"..")
#os.curdir  路径中只是当前目录的部分(例如".")
#split()函数将路径分解为两个单独的部分，并返回包含这些结果的一个tuple。这个tuple的第二个元素是路径的最后一部分，第一个元素则是最后这个部分之前的所有内容
import os.path
print 'split()'
for path in ['/one/two/three',
			 '/one/two/three/',
			 '/',
			 '.',
			 '']:
	print '%15s : %s' % (path, os.path.split(path))
#输入参数以os.sep结尾时，路径的“最后一个元素”是一个空串
#basename()函数返回的值等价于splite()值的第二部分
print 'basename()'
for path in ['/one/two/three',
			 '/one/two/three/',
			 '/',
			 '.',
			 '']:
	print '%15s : %s' % (path, os.path.basename(path))
#整个路径会剥除到只剩下最后一个元素，不论这指示一个文件还是目录。如果路径以目录分隔符结尾(os.sep)则认为基本部分为空
#dirname()函数返回分解路径得到的第一部分
print 'dirname()'
for path in ['/one/two/three',
			 '/one/two/three/',
			 '/',
			 '.',
			 '']:
	print '%15s : %s' % (path, os.path.dirname(path))
#将basename()和dirname()结合，则可以得到原来的路径
#splitext()的作用类似于split(),不过它会根据扩展名分隔符而不是目录分隔符来分解路径
print 'splitext()'
for path in ['filename.txt',
			 'filename',
			 '/path/to/filename.txt',
			 '/',
			 '',
			 'my-archive.tar.gz',
			 'no-extension.',
			 ]:
	print '%15s : %s' % (path, os.path.splitext(path))
#查找扩展名时，只使用os.extsep的最后一次出现，所以如果一个文件名有多个扩展名，分解这个文件名时，部分扩展名会留在前缀上
#commonprefix()取一个路径列表作为参数，将返回一个字符串，表示所有路径中都出现的公共前缀。这个值可能表示一个根本不存在的路径，而且并不考虑路径分隔符，所以这个前缀可能并不落在一个分隔符边界上
print 'commonprefix()'
paths = ['/one/two/three/four',
		 '/one/two/threefold',
		 '/one/two/three',
		]
for path in paths:
	print 'PATH:', path
print
print 'PREFIX:', os.path.commonprefix(paths)
#在这个例子中，公共前缀字符串是/one/two/three，尽管其中一个路径并不包括一个名为three的目录

#6.1.2建立路径
print '\n6.1.2建立路径'
#除了分解现有的路径，还经常需要从其他字符串建立路径。要将多个路径组成部分结合为一个值，可以使用join()
for parts in [('one','two','three'),
			  ('/','one','two','three'),
			  ('/one','/two','/three'),
			]:
	print parts, ':', os.path.join(*parts)
#如果要连接的某个参数以os.sep开头，前面的左右参数都会丢弃，这个新参数会成为返回值的开始部分
#还可以处理包含“可变”部分的路径，这些“可变”部分可以自动扩展。例如expanduser()可以将波浪线~字符转换为用户主目录名
print '\nexpanduser()'
for user in ['', 'a', 'postgresql']:
	lookup = '~' + user
	print '%12s : %s' % (lookup, os.path.expanduser(lookup))
#expandvars()更为通用，它会扩展路径中出现的所有shell环境变量
print '\nexpandvars()'
import os
os.environ['MYVAR'] = 'VALUE'
print os.path.expandvars('/path/to/$MYVAR')
#这里不会做任何验证来确保变量值能够得到真正已经存在的文件名
#6.1.3规范化路径
print '\n6.1.3规范化路径'
#使用join()或利用嵌入变量由单独的字符串组合路径是，得到的路径最后可能会有多余的分隔符或相对路径部分。使用normpath()可以清楚这些内容
print '\nnormpath()'
for path in ['one//two//three',
			 'one/./two/./three',
			 'one/../alt/two/three',
			 ]:
	print '%20s : %s' % (path, os.path.normpath(path))
#这里会计算并“压缩”由os.curdir和os.pardir构成的路径段

#要把一个相对路径转换为一个绝对文件名，可以使用abspath()
print '\nabspath()'
#os.chdir('/tmp')
for path in ['.',
			 '..',
			 './one/two/three',
			 '../one/two/three',
			 ]:
	print '%17s : %s' % (path, os.path.abspath(path))
#结果是一个从文件系统树最顶层开始的完整的路径

#6.1.4文件时间
print '\n6.1.4文件时间'
#除了处理路径，os.path还包括一些用来获取文件属性的函数类似于os.stat()返回的结果
import time
print 'File         :', __file__
print 'Access time  :', time.ctime(os.path.getatime(__file__))#返回访问时间
print 'Modified time:', time.ctime(os.path.getmtime(__file__))#返回修改时间
print 'Change time  :', time.ctime(os.path.getctime(__file__))#返回创建时间
print 'Size         :', os.path.getsize(__file__)#返回文件中的数据量，以字节为单位表示
#6.1.5测试文件
print '\n6.1.5测试文件'
#程序遇到一个路径名时，通常需要知道这个路径是指示一个文件、目录还是一个符号链接（symlink），另外还要知道它是否确实存在。os.path包含了一些函数来测试所有这些条件
FILENAMES = [__file__,
             os.path.dirname(__file__),
             '/',
             './broken_link',
            ]
for file in FILENAMES:
	print 'File        :', file
	print 'Absolute    :', os.path.isabs(file)
	print 'Is File?    :', os.path.isdir(file)
	print 'Is Link?    :', os.path.islink(file)
	print 'Mountpoint? :', os.path.ismount(file)
	print 'Exists?     :', os.path.exists(file)
	print 'Link Exists?:', os.path.lexists(file)
	print 
#所有这些测试函数都返回布尔值

#6.1.6遍历一个目录树
print '6.1.6遍历一个目录树'
import pprint
def visit(arg, dirname, names):
	print dirname, arg
	for name in names:
		subname = os.path.join(dirname, name)
		if os.path.isdir(subname):
			print ' %s/' % name
		else:
			print ' %s' % name
		print
if not os.path.exists('example'):
	os.mkdir('example')
if not os.path.exists('example/one'):
	os.mkdir('example/one')

with open('example/one/file.txt', 'wt') as f:
	f.write('contents')
with open('example/two.txt', 'wt') as f:
	f.write('contents')
os.path.walk('example', visit, '(User data)')
#这个例子会生成一个递归的目录列表，这里忽略了.svn目录