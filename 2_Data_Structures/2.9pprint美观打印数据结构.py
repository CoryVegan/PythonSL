# -*- coding: utf-8 -*-	
#pretty printer用于生成数据结构的一个美观试图。格式化工具会生成数据结构的一些表示，不仅可以由解释器正确地解析，而且便于人类阅读。输出尽可能放在一行上，分解为多行时则需要缩进。
data = [(1, {'a':'A', 'b':'B', 'c':'C', 'd':'D'}),
		(2, {'e':'E', 'f':'F', 'g':'G', 'h':'H',
			 'i':'I', 'j':'J', 'k':'K', 'l':'L',
			}),
		]

#2.9.1打印
#pprint()格式化一个对象，并把它写至一个数据流，这个数据流作为参数传入
print('2.9.1打印')
from pprint import pprint
print 'PRINT:'
print data
print
print 'PPRINT:'
pprint(data)

#2.9.2格式化
#要格式化一个数据结构而不是把它直接写至一个流（例如用于日志记录），可以使用pformat()来构造一个字符串表示
print('2.9.2格式化')
import logging
from pprint import pformat
logging.basicConfig(level=logging.DEBUG,
					format='%(levelname) - 8s %(message)s',)
logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
	logging.debug(line.rstrip())

#2.9.3任意类
#如果定制类定义了一个__repr__(),pprint()使用PrettyPrinter类还可以处理这些定制类
print '2.9.3任意类'
class node(object):
	def __init__(self, name, contents=[]):
		self.name = name
		self.contents = contents[:]
	def __repr__(self):
		return ('node(' + repr(self.name) + ', '+
				repr(self.contents) + ')'
				)
trees = [	node('node-1'),
			node('node-2', [node('node-2-1')]),
			node('node-3', [node('node-3-1')]),
		]
pprint(trees)

#2.9.4递归 递归数据结构由指向元数据的引用来表示，形式为<Recursion on typename with id=number>
print '2.9.4递归'
from pprint import pprint
local_data = ['a', 'b', 1, 2]
local_data.append(local_data)
print 'id(local_data) =>', id(local_data)
pprint(local_data)
#这个例子中，列表local_data增加到其自身，这回创建一个递归应用

#2.9.5限制嵌套输出 对于非常深的数据结构，可能不要求输出包含所有细节，有可能数据没有适当地格式化，也可能格式化文本过大而无法管理，或者某些数据是多余的
print '2.9.5限制嵌套输出' 
pprint(data, depth=1)
#使用depth参数可以控制pprint递归处理嵌套数据结构的深度。输出中未包含的层次由一个省略号表示

#2.9.6控制输出宽度 使用参数width
print '2.9.6控制输出宽度'
for width in [80,5]:
	print 'WIDTH =', width
	pprint(data, width=width)
	print
#宽度太小不能适应格式化数据结构时，如果截断或转行会引入非法的语法，就不会进行截断或转行