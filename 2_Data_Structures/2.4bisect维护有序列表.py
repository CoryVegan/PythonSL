# -*- coding: utf-8 -*-	
#2.4 bisect维护有序列表
#bisect模块实现了一个算法用于向列表中插入元素，同时保持列表有序。某些情况下，这比返回对一个列表排序更搞笑，也比创建一个大列表之后再显式对其排序更为高效。
#2.4.1有序插入
import bisect
import random
print 'New Pos Contents'
print '--- --- --------'

l = []
for i in range(1,15):
	r = random.randint(1, 100)
	position = bisect.bisect(l, r)
	bisect.insort(l, r)
	print '%3d %3d' % (r, position), l
#对于此例所处理的数据量来说，如果直接构建列表然后完成依次排序，可能速度更快，不过对于长列表而言，使用类似这样的一个插入排序算法可以节省大量的时间和内存
print
#2.4.2处理重复bisect模块提供两种方式来处理重复，新值可以插入现有值的左边或右边。insort实际是insort_right()的别名，还有一个insort_left()的函数
import bisect
import random
random.seed(1)
print 'New Pos Contents'
print '--- --- --------'

l = []
for i in range(1,15):
	r = random.randint(1, 100)
	position = bisect.bisect_left(l, r)
	bisect.insort(l, r)
	print '%3d %3d' % (r, position), l