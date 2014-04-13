# -*- coding: utf-8 -*-	
#10.2.6信号和线程a
#信号和线程通常不能很好地结合，因为只有进程的主线程可以接收信号。线面的粒子建立了一个信号处理程序，它在一个线程中等待信号，而从另一个线程发送信号。
import signal, threading, os, time
def signal_handler(num, stack):
	print 'Received signal %d in %s' % (num, threading.currentThread().name)
	
signal.signal(signal.SIGUSR1, signal_handler)

def wait_for_signal():
	print 'Wait for signal in', threading.currentThread().name
	signal.pause()
	print 'Done waiting'
#Start a thread that will not receive the signal
receiver = threading.Thread(target=wait_for_signal, name='receiver')
receiver.start()
time.sleep(0.1)
def send_signal():
	print 'Sending signal in', threading.currentThread().name
	os.kill(os.getpid(), signal.SIGUSR1)
sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()
#Wait for the thread to see the signal (not going to happen!)
print 'Waiting for', receiver.name
signal.alarm(2)
receiver.join()
#信号处理程序都在主线程中注册。尽管接收者线程调用了signal.pause()，但它不会接收信号。这个例子接近结束时的signal.alarm(2)调用避免了无限阻塞，因为接收者线程永远不会退出

#尽管在任何线程中都能设置闹铃，但总是由主线程接收
def signal_handler(num, stack):
	print time.ctime(), 'Alarm in', threading.currentTread().name
signal.signal(signal.SIGALRM, signal_handler)
def use_alarm():
	t_name = threading.currentThread().name
	print time.ctime(), 'Setting alarm in', t_name
	signal.alarm(1)
	print time.ctime(), 'Sleeping in', t_name
	time.sleep(3)
	print time.ctime(), 'Done with sleep in', t_name
#Start a thread that will not receive the signal
alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread')
alarm_thread.start()
time.sleep(0.1)
#Wait for the thread to see the signal (not going to happen!)
print time.ctime(), 'Waiting for', alarm_thread.name
alarm_thread.join()
print time.ctime(), 'Exiting normally'
#闹铃不会终止use_alarm()中的sleep()调用	