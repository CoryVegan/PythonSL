# -*- coding: utf-8 -*-	
#10.2.4闹铃
#闹铃是一种特殊的信号，程序要求操作系统在过去一段时间之后再发出这个信号通知。os的标准模块文档指出，这对于避免一个I/O操作或其他系统调用无阻塞很有用
import signal
import time
def receive_alarm(signum, stack):
	print 'Alarm :', time.ctime()
#Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)
print 'Before:', time.ctime()
time.sleep(4)
print 'After :', time.ctime()