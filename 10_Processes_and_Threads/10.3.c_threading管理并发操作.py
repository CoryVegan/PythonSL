# -*- coding: utf-8 -*-	
#10.3.4列举所有线程
#没有必要为所有守护线程维护一个显式句柄来确保它们在退出主进程之前已经完成。enumerate()会返回活动Thread实例的一个列表。这个列表也包括当前进程，由于等待当前线程结束会引入一种死锁情况，所以必须将其跳过。
print '10.3.4列举所有线程'
import threading, random, time, logging
logging.basicConfig(level = logging.DEBUG,
					format='(%(threadName)-10s), %(message)s',
					)
def worker():
	"""thread worker function"""
	t = threading.currentThread()
	pause = random.randint(1,5)
	logging.debug('sleeping %s', pause)
	time.sleep(pause)
	logging.debug('ending')
	return
for i in range(3):
	t = threading.Thread(target=worker)
	t.setDaemon(True)
	t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
	if t is main_thread:
		continue
	logging.debug('joining %s', t.getName())
	t.join()

#10.3.5派生线程
print '\n10.3.5派生线程'
#开始时，Thread要完成一些基本初始化，然后调用其run()方法，这会调用传递到构造函数的目标函数。要创建Thread的一个子类，需要覆盖run()来完成所需的工作
class MyThread(threading.Thread):
	def run(self):
		logging.debug('running')
		return
for i in range(5):
	t = MyThread()
	t.start()
#run()的返回值将忽略
print
#由于传递到Thread构造函数的args和kwargs值要保存在私有变量中（这些变量名都有前缀'__'）,所以不能很容易地从子类访问这些值。要向一个地ing值得线程类型传递参数，需要冲洗定义构造函数，将这些值保存在子类可见的一个实例属性中
class MyThreadWithArgs(threading.Thread):
	def __init__(self, group=None, target=None, name=None,
					args=(), kwargs=None, verbose=None):
		threading.Thread.__init__(self, group=group,
										target=target,
										name=name,
										verbose=verbose)
		self.args = args
		self.kwargs = kwargs
		return
	def run(self):
		logging.debug('running with %s and %s',
						self.args, self.kwargs)
		return
for i in range(5):
	t = MyThreadWithArgs(args=(i,),
							kwargs={'a':'A','b':'B'})
	t.start()

#10.3.6 定时器线程
print '\n10.3.6 定时器线程'
#有时出于某种原因需要派生Thread,Timer就是这样一个例子，Timer包含在threading中。Timer在一个延迟之后开始工作，可以在这个延迟期间内的任意时刻取消。
def delayed():
	logging.debug('worker running')
	return
t1 = threading.Timer(3, delayed)
t1.setName('t1')
t2 = threading.Timer(3, delayed)
t2.setName('t2')
logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.getName())
time.sleep(2)
logging.debug('canceling %s', t2.getName())
t2.cancel()
logging.debug('done')

#第二个定时器永远不会运行，第一个定时器会在其余的主程序完成之后运行。由于这不是一个守护线程，主线程完成时它会隐式退出







