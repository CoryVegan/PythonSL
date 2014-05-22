# -*- coding: utf-8 -*-	
#14.1.4一个完整的getopt例子
#这个例子是一个更完整的程序，它有5个选项：-o,-v,--output,--verbose和--version.
#-o,--output,--version选项分别需要一个参数
import getopt
import sys

version = '1.0'
verbose = False
output_filename = 'default.out'

print 'ARGV     :', sys.argv[1:]

try:
	options, remainder = getopt.gnu_getopt( 
	#gnu_getopt允许在命令行上以任意顺序混合选项和非选项参数
		sys.argv[1:],
		'o:v',
		['output=',
		 'verbose',
		 'version=',
		])
except getopt.GetoptError as err:
	print 'ERROR:', err
	sys.exit(1)

print 'OPTIONS   :', options

for opt, arg in options:
	if opt in ('-o', '--output'):
		output_filename = arg
	elif opt in ('-v', '--verbose'):
		verbose = True
	elif opt == '--version':
		version = arg
print 'VERSION   :', version 
print 'VERBOSE   :', verbose
print 'OUTPUT    :', output_filename
print 'REMAINING :', remainder
#可以采用多种不同方式调用这个程序。如果不带任何参数调用这个程序，会使用默认设置
#python file.py -o foo
#python file.py -ofoo
#python file.py --output foo
#python file.py --output=foo
#14.1.5缩写长格式选项
#python file.py --o foo
#14.1.6GNU选项解析
#正常情况下，使用getopt一旦遇到第一个非选项参数，选项处理就会停止
#gnu_getopt允许在命令行上以任意顺序混合选项和非选项参数
#python file.py -v not_an_option --output foo
#14.1.7结束参数处理
#如果getopt()在输入参数中遇到“--”，它会停止，不再将余下的参数作为选项处理，这个特性可以用来传递看上去像选项的参数值，如以一个短横线“-”开头的文件名
