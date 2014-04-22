# -*- coding: utf-8 -*-	
#10.3threading管理并发操作
#10.3.1Tread对象
print '10.3.1Tread对象\n'
#要使用Thread，最简单的方法就是用一个目标函数实例化一个Thread对象，并调用start()让它开始工作。
import threading
def worker():
	"""thread worker function"""
	print 'Worker'
	return
threads = []
for i in range(5):
	t = threading.Thread(target=worker)
	threads.append(t)
	t.start()
print 
#如果能够创建一个线程，并向它传递参数告诉它要完成什么工作，这会很有用。任何类型的对象都可以作为参数传递到线程。下面的例子传递了一个数，线程将打印出这个数。
def worker(num):
	"""thread worker function"""
	print 'Worker: %s' % num
	return
threads = []
for i in range(5):
	t = threading.Thread(target=worker, args=(i,))
	threads.append(t)
	t.start()
#10.3.2确定当前线程
print '\n10.3.2确定当前线程'
#使用参数来标识或命名线程很麻烦，也没有必要。每个Thread实例都有一个名称，它有个一默认值，可以再创建线程时改变。如果服务器进程由处理不同操作的多个服务线程构成，在这样的服务器进程中，对线程命名就很有用。
import time
def worker():
	print threading.currentThread().getName(), 'Starting'
	time.sleep(2)
	print threading.currentThread().getName(), 'Exiting'
def my_service():
	print threading.currentThread().getName(), 'Starting'
	time.sleep(3)
	print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
#调试输出的每一行中包含有当前线程的名称。线程名称列为Thread-11的行对应未命名的线程w2
time.sleep(5)
print
#大多数程序并不使用print来进行调试。logging模块支持线程名嵌入到各个日志消息中(使用格式化代码%(threadName)s).通过线程名包含在日志消息中，这样就能跟踪这些消息的来源。
import logging
logging.basicConfig(
	level = logging.DEBUG,
	format='[%(levelname)s], (%(threadName)-10s), %(message)s',
	)
def worker():
	logging.debug('Starting')
	time.sleep(2)
	logging.debug('Exiting')
def my_service():
	logging.debug('Starting')
	time.sleep(3)
	logging.debug('Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name
w.start()
w2.start()
t.start()
#logging也是线程安全的，所以来自不同线程的消息在输出中会有所区分






	