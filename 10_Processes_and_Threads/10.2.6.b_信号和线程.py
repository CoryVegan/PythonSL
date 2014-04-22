# -*- coding: utf-8 -*-	
#10.2.6信号和线程b
#尽管在任何线程中都能设置闹铃，但总是由主线程接收
import signal, threading, time
def signal_handler(num, stack):
	print time.ctime(), 'Alarm in', threading.currentThread().name
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