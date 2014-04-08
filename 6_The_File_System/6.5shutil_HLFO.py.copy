# -*- coding: utf-8 -*-
#6.5.1复制文件
print '6.5.1复制文件'
#copyfile()将源的内容复制到目标，如果没有权限写目标文件则产生IOError
from shutil import *
from glob import glob
print 'BEFORE:', glob('6.5shutil_HLFO.*')
copyfile('6.5shutil_HLFO.py', '6.5shutil_HLFO.py.copy')
print 'AFTER:', glob('6.5shutil_HLFO.py.*')
# 某些特殊文件 (如UNIX设备节点)不能用copyfile()复制为新的特殊文件
# copyfile()的实现使用了底层函数copyfileobject()。copyfile()的参数是文件名。
# copyfileobject(input, output[, bufferlength])的参数是打开的文件句柄而不是文件名。还有第三个参数（可选）：用于读入块的一个缓冲区长度
from StringIO import StringIO
import sys
class VerboseStringIO(StringIO):
    def read(self, n=-1):
        next = StringIO.read(self, n)
        print 'read(%d) bytes' % n
        return next

lorem_ipsum = """Lorem ipsum dolor sit amet, novum nemore mel ex, ei eos posse inciderint, docendi tibique sed at. Sumo eruditi eam ut. Prima utamur argumentum duo in, pri cibo erat dolores te. Qui principes intellegat complectitur ea. Delectus percipitur ex est, his malorum epicuri et, tota deserunt vim eu. Sed ea justo saepe vidisse. Cum facer inimicus te, eu vim wisi semper aliquip, aeque numquam ei pro.
Ex nostrud ancillae nominavi nec, duo ea nominati dignissim deterruisset. Ceteros contentiones te his. Has repudiandae dissentiunt cu. Mel eligendi scribentur id, quo oblique mentitum patrioque cu."""

print 'Default:'
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output)
print

print 'All at once:'
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, -1)
print

print '256 bytes:'
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, 128)
print
#默认的行为是使用大数据块读取。使用-1会一次读入所有输入，或者使用其他正数可以设置特定块的大小。注意观察输出中的读入次数
# copy()函数类似于UNIX命令工具cp，如果指定的目标指示一个目录而不是一个文件，会使用源文件的基名在该目录中创建一个新文件。
import os
import time
print 'BEFORE:', os.listdir('example')
copy('6.5shutil_HLFO.py', 'example')
print 'AFTER:', os.listdir('example')
print
#文件的权限会随内容复制
# copy2()的工作类似于copy()，不过复制到新文件的元数据会包含访问和修改时间。
def show_file_info(filename):
    stat_info = os.stat(filename)
    print '\tMode     :', stat_info.st_mode
    print '\tCreated  :', time.ctime(stat_info.st_ctime)
    print '\tAccessed :', time.ctime(stat_info.st_atime)
    print '\tModified :', time.ctime(stat_info.st_mtime)

print 'SOURCE:'
show_file_info('6.5shutil_HLFO2.py')
copy2('6.5shutil_HLFO2.py', 'example')
print 'DEST:'
show_file_info('example/6.5shutil_HLFO2.py')
print

## 6.5.2复制文件元数据
print '6.5.2复制文件元数据'
# 要把权限从一个文件复制到两一个文件，可以使用copymode()
from commands import *
os.chmod('file_to_change.txt', 0444)
print 'BEFORE:'
print getstatus('file_to_change.txt')
copymode('6.5shutil_HLFO.py', 'file_to_change.txt')
print 'AFTER :'
print getstatus('file_to_change.txt')
print

#要复制文件的其他元数据，可以使用copystat()
with open('file_to_change.txt', 'wt') as f:
    f.write('contents')
os.chmod('file_to_change.txt', 0444)
print 'BEFORE:'
show_file_info('file_to_change.txt')
copystat('6.5shutil_HLFO.py', 'file_to_change.txt')
print 'AFTER :'
show_file_info('file_to_change.txt')
print

## 6.5.3处理目录树
print '6.5.3处理目录树'
# shutil包含3个函数来处理目录树。要把一个目录从一个位置复制到另一个位置，可以使用copytree()。这会递归遍历源目录树，将文件复制到目标。目标目录不能已存在。
print 'BEFORE:'
print getoutput('ls -rlast /tmp/example')
copytree('../6_The File System', '/tmp/example')
print '\nAFTER :'
print getoutput('ls -rlast /tmp/example')
print
# 要删除一个目录及其中的内容，可以使用rmtree()
print 'BEFORE:'
print getoutput('ls -rlast /tmp/example')
rmtree('/tmp/example')
print 'AFTER :'
print getoutput('ls -rlast /tmp/example')
print
# 要把一个文件或目录从一个位置移动到另一个位置，可以使用move()

with open('example.txt', 'wt') as f:
    f.write('contents')
print 'BEFORE: ', glob('example*')
move('example.txt', 'example.out')
print 'AFTER : ', glob('example*') 
#其语义与UNIX命令mv相似。如果源和目标都在同一个文件系统内，则会重命名源文件。否则，源文件会复制到目标文件爱你，然后将源文件删除。


