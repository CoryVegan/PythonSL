# -*- coding: utf-8 -*-	
#10.2.5忽略信号
#要忽略一个信号，需要注册SIG_IGN作为处理程序。下面这个脚本将SIGINT的默认处理程序替换为SIG_IGN，并为SIGUSR1注册一个处理程序。然后使用Signal.pause()等待接收一个信号
import signal, os, time
def do_exit(sig, stack):
	raise SystemExit('Exiting')
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)
print 'My PID:', os.getpid()
signal.pause()
#正常情况下，SIGINT（用户按下Ctrl-C时shell会向程序发送这个信号）会产生一个KeyboardInterrupt.这个例子将忽略SIGINT，并发现SIGUSR1时产生一个SystemExit.输出中的每个^C表示每一次尝试使用Ctrl-C从终端结束脚本。从另一个终端使用kill -USR1 $pid才能最终退出脚本