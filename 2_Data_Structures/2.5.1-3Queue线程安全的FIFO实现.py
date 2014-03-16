# -*- coding: utf-8 -*-	
#Queue提供了一个线程安全的FIFO实现，它提供了一个数据结构，可以用来在生产者和消费者线程之间安全地传递消息或其他数据。它会为调用者处理锁定，是多个线程可以安全滴处理同一个Queue实例。Queue的大小（其中包含的元素个数）可能要受限，以限制内存使用或处理
#2.5.1基本FIFO队列
#Queue类实现了一个底本的先进先出容器，使用put()将元素增加到序列一端，使用get()从另一端删除。
import Queue
q = Queue.Queue()
for i in range(5):
	q.put(i)
while not q.empty():
	print q.get(),
print
#2.5.2 LIFO
#LifoQueue使用了后进先出顺序（通常与栈数据结构关联）
import Queue
q = Queue.LifoQueue()
for i in range(5):
	q.put(i)
while not q.empty():
	print q.get(),
print
#2.5.3优先队列
#有些情况下，队列中的元素的处理顺序需要根据这些元素的特性来决定，而不只是在队列中创建或插入的顺序。例如，财务部门的打印作业可能要优先于一个开发人员打印的代码清单。PriorityQueue使用队列内容的有序顺序来决定获取哪一个元素
import Queue
import threading
class Job(object):
	def __init__(self, priority, description):
		self.priority = priority
		self.description = description
		print 'New Job:', description
		return
	def __cmp__(self, other):
		return cmp(self.priority, other.priority)
		
q = Queue.PriorityQueue()

q.put( Job(3,  'Mid-level job'))
q.put( Job(10, 'Low-level job'))
q.put( Job(1,  'Important job'))

def process_job(q):
	while True:
		next_job = q.get()
		print 'Processing job:', next_job.description
		q.task_done()
		
workers = [ threading.Thread(target = process_job, args=(q,)),
		    threading.Thread(target = process_job, args=(q,)),
			]	
for w in workers:
	w.setDaemon(True)
	w.start()
	
q.join()