# -*- coding: utf-8 -*-	
#10.3.7线程间传送信号
#尽管使用多线程的目的是并发地运行单个操作，不过有时也需要在两个或多个线程中同步操作。事件对象是实现线程间安全通信的一种简单方法。Event管理一个内部标志，调用者可以用set()和clear()方法控制这个标志。其他线程可以使用wait()暂停，直到设置这个标志，其效果就是允许继续之前阻塞线程的运行。
import threading, time, logging
logging.basicConfig(level = logging.DEBUG,
					format='(%(threadName)-10s), %(message)s',
					)
def wait_for_event(e):
	"""Wait for the event to be set before doing anything"""
	logging.debug('wait_for_event starting')
	event_is_set = e.wait()
	logging.debug('event set: %s', event_is_set)
def wait_for_event_timeout(e, t):
	"""Wait t seconds and then timeout"""
	while not e.isSet():
		logging.debug('wait_for_event_timeout starting')
		event_is_set = e.wait(t)
		logging.debug('event set: %s', event_is_set)
		if event_is_set:
			logging.debug('processing event')
		else:
			logging.debug('doing other work')
e = threading.Event()
t1 = threading.Thread(name='block',
						target=wait_for_event,
						args=(e,))
t1.start()

t2 = threading.Thread(name='nonblock',
						target=wait_for_event_timeout,
						args=(e, 2))

t2.start()
logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')
#wait()方法取一个参数，表示在超时之前等待时间的时间（秒数）。它会返回一个布尔值，指示事件是否已设置，从而使调用者直到wait()为什么返回。可以对事件单独地使用isSet()方法而不必担心阻塞。
#在这个例子中，wait_for_event_timeout()将检查事件状态而不会无线组则。wait_for_event()在wait()调用阻塞，事件状态改变之前它不会返回。