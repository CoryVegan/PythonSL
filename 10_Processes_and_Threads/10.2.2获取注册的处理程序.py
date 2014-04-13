# -*- coding: utf-8 -*-	
#10.2.2获取注册的处理程序
#要查看为一个信号注册了哪些信号处理程序，可以使用getsignal()。要将信号编号作为参数传入。返回值是已注册的处理程序，或者是以下某个特殊值：SIG_IGN(如果信号被忽略)，SIG_DFL(如果使用默认行为或)，None(如果从C而不是从Python注册现有信号处理程序)。
import signal
def alarm_received(n, stack):
	return
signal.signal(signal.SIGALRM, alarm_received)
signals_to_names = dict(
	(getattr(signal, n), n)
	for n in dir(signal)
	if n.startswith('SIG') and '_' not in n
	)
for s, name in sorted(signals_to_names.items()):
	handler = signal.getsignal(s)
	if handler is signal.SIG_DFL:
		handler = 'SIG_DFL'
	elif handler is signal.SIG_IGN:
		handler = 'SIG_IGN'
	print '%-10s (%2d):' % (name, s), handler