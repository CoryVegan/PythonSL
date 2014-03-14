# -*- coding: utf-8 -*-	
#collections_容器数据类型，其包含除内置类型list,dict和tuple以外的其他的数据类型
print 'collections_容器数据类型\n'
# 2.1.1Counter,它作为一个容器，可以跟踪相同的值增加了多少次
import collections
#三种初始化方法
print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print collections.Counter({'a':2, 'b':3, 'c':1})
print collections.Counter(a=2, b=3, c=1)
print
#也可以先构造一个空Counter, 然后通过update()方法填充
c = collections.Counter()
print 'Initial :', c
c.update('abcdaab')
print 'Sequence:', c
c.update({'a':1, 'd':5})
print 'Dict    :', c
print
#访问计数，一旦填充了Counter， 可以使用字典API获取它的值
c = collections.Counter('abcdaab')
for letter in 'abcde':
	print '%s : %d' % (letter, c[letter])
print
#对于未知的元素，其计数为0，而不会产生error
#element()方法返回一个迭代器，将生成Counter知道的所有元素
c = collections.Counter('extremely')
c['z'] = 0
print c
print list(c.elements())
print

#使用most_common()可以生成一个序列，其中包含n个最常遇到的输入值及其相应计数
#这个粒子要统计系统字典里所有单词中出现的字母，来生成一个频度分布
c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
	for line in f:
		c.update(line.rstrip().lower())
print 'Most common:'
for letter, count in c.most_common(3):
	print '%s: %7d' % (letter, count)
#Counter()支持算数和集合操作来完成结果的聚集
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print 'C1:', c1
print 'C2:', c2
print '\nCombined counts:'
print c1 + c2
print '\nSubtraction:'
print c1 - c2
print '\nIntersection (taking positive minimums):'
print c1 & c2
print '\nUnion (taking maximums):'
print c1 | c2

#2.1.2 OrderedDict是一个字典子类，可以记住其内容增加的顺序
#常规dict并不跟踪插入顺序，迭代处理时会根据键在散列表中储存的顺序来生成值。
print
print 'Regular dictionary:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
for k, v in d.items():
	print k, v
#在OrderDict中则相反，它回记住元素插入的顺序，并在创建迭代器时使用这个顺序
print '\nOrderedDict:'
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
	print k, v
#相等性，常规的dict在检查相等性时会查看其内容，OrderDict()还会考虑元素增加的顺序
print
print 'dict'
d1 = {}	
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'OrderedDict:'
d1 = collections.OrderedDict()
d1 = {}	
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = collections.OrderedDict()
d['c'] = 'C'
d['b'] = 'B'
d['a'] = 'A'

print d1 == d2








