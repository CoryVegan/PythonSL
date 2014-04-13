# -*- coding: utf-8 -*-	
#10.1signal异步系统事件
#10.2.1接收信号
print '10.2.1接收信号\n'
import signal, os, time
def receive_signel(signum, stack):
	print 'Received:', signum
#Register signal handlers
signal.signal(signal.SIGUSR1, receive_signel)
signal.signal(signal.SIGUSR2, receive_signel)
#print the process ID so it can be used with 'kill'
#to send this program signals.
print 'My PID is:', os.getpid()
while True:
	print 'Waiting...'
	time.sleep(3)
#这个脚本会无限循环，每次暂停几秒时间。一个信号到来时，sleep()调用被终端，信号处理程序receive_signel()打印信号编号。信号处理程序返回时，循环继续。可以使用os.kill()或UNIX命令行程序kill向正在运行的程序发送信号
#在一个终端中运行
#$kill -USR1 $pid
#$kill -USR2 $pid
#kill -INT $pid