# -*- coding: utf-8 -*-	
#6.4tempfile临时文件系统对象
#作用创建临时文件系统对象
#6.4.1临时文件
print '6.4.1临时文件'
import tempfile, os
#如果应用需要临时文件来储存数据，而不需要与其他程序共享这些文件，就应当使用TemporaryFile()函数创建文件。这个函数会创建一个文件，而且如果平台支持，它就会立即断开文件链接。这样一来其他程序就不可能找到或打开这个文件了，因为文件系统表中根本没有这个文件的引用。对于TemporaryFile()创建的文件，不论通过调用close()还是结合使用上下文管理器API和wit语句来关闭文件，文件都会在关闭时自动删除。
print "Building a filename with PID:"
filename = '/tmp/guess_my_name.%s.txt' % os.getpid()
temp = open(filename, 'w+b')
try:
	print 'temp:'
	print ' ',temp
	print 'temp.name:'
	print ' ', temp.name
finally:
	temp.close()
	os.remove(filename)
	#手动清除文件
print "\nTemporaryFile:"
temp = tempfile.TemporaryFile() 
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
    print
finally:
    temp.close()
	#自动清除文件
#这个例子展示了采用不同方法创建临时文件的差别。TemporaryFile()返回的文件没有文件名

#默认地，文件句柄采用模式'w+b'创建，使之在所有平台上都表现一直，而且调用者可以读写这个文件。
with tempfile.TemporaryFile() as temp:
    temp.write('Some data:')
    temp.seek(0)
    print temp.read()
# 写文件之后，必须使用seek()回转文件句柄，从而能够从文件读回数据
# 要以文本模式打开文件，创建文件时要设置模式为'w+t'
with tempfile.TemporaryFile() as f:
    f.writelines(['first\n', 'second\n'])
    f.seek(0)
    for line in f:
        print line.rstrip()
#这个文件句柄将数据处理为文本

#6.4.2命名文件
print '\n6.4.2命名文件'
#很多情况下都需要有一个命名的临时文件。对于跨多个进程甚至主机的应用来说，为文件命名是在应用不同部分之间传递文件的最简单的方法。NamedTemporaryFile()函数会创建一个文件，但不会段开其链接，所以会保留其文件名（用name属性访问）
print "TemporaryFile:"
with tempfile.NamedTemporaryFile() as temp:
	print 'temp:'
	print ' ', temp
	print 'temp.name:'
	print ' ', temp.name
print 'Exists after close:', os.path.exists(temp.name)
print
#句柄关闭后，文件会被删除

#6.4.3临时目录
print '6.4.3临时目录'
#需要多个临时文件时，可以更方便的做法是用mkdtemp()创建一个临时目录，并打开该目录中的所有文件
directory_name = tempfile.mkdtemp()
print directory_name
os.removedirs(directory_name)
#由于这个目录事实上并不是"打开的"，不过需要它是必须显式地将其删除

#6.4.4预测名
print '\n6.4.4预测名'
#虽然没有严格匿名的临时文件那么安全，但有时也需要在名字中包含一个可预测的部分，从而能否查找和监察文件来进行调试。目前为止介绍的所有函数都取3个参数，可以在某种程序上控制文件。文件名使用以下公式生成。
#dir+prefix+random+suffix
#除了random外，所有其他值都可以作为参数传递给TemporaryFile()，NameTemporaryFile()和mkdtemp()
with tempfile.NamedTemporaryFile(
	suffix='_suffix', prefix='prefix_', dir='/tmp'
	) as temp:
	print 'temp:'
	print ' ', temp
	print 'temp.name:'
	print ' ', temp.name
#前缀(prefix)和后缀(suffix)参数与一个随机的字符串结合来生成文件名，dir参数保持不变，用作新文件的位置
	
#6.4.5临时文件位置
print '\n6.4.5临时文件位置'
#如果没有使用dir参数制定明确的目标位置，临时文件使用的路径会根据当前平台和设置而有所不同。tempfile模块包含两个函数来查询运行时使用的设置。
print 'gettempdir():', tempfile.gettempdir()
print 'gettempprefix():', tempfile.gettempprefix()
#gettempdir()返回包含所有临时文件的默认目录，gettempprefix()返回新文件和目录名的字符串前缀
#gettempdir()返回的值根据一个简单算法来设置，它会查找5个位置，寻找允许当前进程创建文件的第一个位置。上搜索列表如下：
#1.环境变量TEMDIR
#2.环境变量TEMP
#3.环境变量TMP
#4.作为“后路”的位置，取决于具体平台，如windows下的C:\TEMP,C:\TEMP,C:\TMP,其他平台的/tmp,/var/tmp,/usr/tmp,RiscOS的Wimp$ScrapDir
#5.如果找不到其他目录，则使用当前目录
tempfile.tempdir = '/i/changed/this/path'
print 'gettempdir():', tempfile.gettempdir()
#如果程序需要对所有临时文件使用一个全局位置，但不使用以上任何环境变量，则应当直接设置tempfile.tempdir为该变量赋一个值