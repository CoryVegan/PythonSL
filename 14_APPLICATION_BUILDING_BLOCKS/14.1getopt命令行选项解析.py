# -*- coding: utf-8 -*-
#14.1getopt命令行选项解析	
#getopt模块是原来的命令行选项解析器，支持UNIX函数getopt()建立的约定。它会解析一个参数序列，如sys.argv并返回一个元组序列和一个非选项参数序列，元组序列中包含一些（选项，参数）对
#14.1.1函数参数
#getopt()函数有三个参数：
#第1个参数是要解析的参数序列。这通常来自sys.argv[1:]
#第2个参数是单字符选项的选项定义串。如果某个选项需要一个参数，相应字母后面会有一个冒号
#第3个参数应当是一个长格式选项名序列。长格式选项可以包含多个字符，如--noarg或--witharg。序列中的选项名不包括--前缀。如果某个长选项需要一个参数，其名应当有一个后缀“=”
#短格式和长格式选项可以再一个调用中结合使用
#14.1.2短格式选项
print '14.1.2短格式选项'
#这个示例程序接受3个选项。-a是一个简单标志，-b和-c需要一个参数。选项定义串为"ab:c:"
import getopt
opts, args = getopt.getopt(['-a', '-bval', '-c', 'val'], 'ab:c:')
for opt in opts:
	print opt
#这个程序将一个模拟选项值列表传递到getopt()，来显示如何对它们进行处理。
#14.1.3长格式选项
print '14.1.3长格式选项'
#对于一个有两个选项的程序（--noarg和witharg）,长参数序列为['noarg','witharg=']
opts, args = getopt.getopt([ '--noarg', '--witharg', 'val', '--witharg2=another',],
							'', ['noarg', 'witharg=', 'witharg2=' ])
for opt in opts:
	print opt