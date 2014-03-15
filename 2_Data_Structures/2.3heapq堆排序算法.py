# -*- coding: utf-8 -*-	
#2.3 heapq模块实现了一个适用于Python列表的最小堆排序算法。
import heapq
from heapq_heapdata import data
from heapq_showtree import show_tree
#2.3.2创建堆,创建堆有两种基本方式:heappush()和heapify()
#使用heappush()中，从数据源增加新元素时会保持元素的堆顺序
heap = []
print 'random :', data
print
for n in data:
	print 'add %3d:' % n
	heapq.heappush(heap, n)
	show_tree(heap)
#如果数据已经在内存中，使用heaoify()原地重新组织列表中的元素会更高效
from heapq_heapdata import data
print 'random    :', data
heapq.heapify(data)
print 'heapified :'
show_tree(data)	
print
#2.3.3访问堆的内容
#一旦堆已正确组织，就可以使用heappop()删除最小值的元素
from heapq_heapdata import data
heapq.heapify(data)
print 'heapified :'
show_tree(data)
print
for i in xrange(2):
	smallest = heapq.heappop(data)
	print 'pop              %3d:' % smallest
	show_tree(data)

#如果希望在一个操作中删除现有元素并替换为新值，可以使用heapreplace(),通过原地替换元素，这样可以维持一个固定大小的堆，如按优先级排序的作业队列
from heapq_heapdata import data
heapq.heapify(data)
print 'start:'
show_tree(data)
for n in [0, 13]:
	smallest = heapq.heapreplace(data, n)
	print 'replace %2d with %2d:' % (smallest, n)
	show_tree(data)
print
#2.3.4堆数据的极值
#heapq还包括两个检查可迭代对象的函数，查找其中包含的最大值或最小值的范围
from heapq_heapdata import data
print 'all       :', data
print '3 largest :', heapq.nlargest(3, data)
print 'from sort :', list(reversed(sorted(data)[-3:]))
print '3 smallest:', heapq.nsmallest(3, data)
print 'from sort :', sorted(data)[:3]