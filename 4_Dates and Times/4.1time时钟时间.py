# -*- coding: utf-8 -*-	
#4.1.1挂壁钟时间
#time模块的核心函数之一是time()，它会把纪元开始以来的秒数作为一个浮点数返回。
import time
print 'The time is:', time.time()
print 'The time is:', time.ctime()
later = time.time() + 15
print '15 secs from now:', time.ctime(later)
#4.1.2处理器时钟时间
#clock()会返回处理器始终时间。clock()返回的值应当用于性能测试、基准测试等，因为它们反映了程序使用的实际时间，可能比time()返回的值更精确。
import hashlib
import time
data = open(__file__, 'rt').read()
for i in range(5):
	h = hashlib.sha1()
	print time.ctime(), ': %0.3f %0.3f' % (time.time(), time.clock())
	for i in range(300000):
		h.update(data)
	cksum = h.digest()
#在这个例子中，每次循环迭代时会打印格式化的ctime()时间，以及time()和clock()返回的浮点数值

#一般地，如果程序什么也没有做，处理器时钟不会“滴答”的
for i in range(6, 1, -1):
	print '%s %0.2f %0.2f' % (time.ctime(),
							  time.time(),
							  time.clock())
	print 'Sleeping', i
	time.sleep(i)
#在这个例子中，循环几乎不做什么工作，每次迭代后都会睡眠。及时应用睡眠，time()值也会增加，但是clock()值不会增加。调用sleep()会从当前线程交出控制，要求它等待系统将其再次唤醒。如果程序只有一个线程，这实际就会阻塞应用，什么也不做。

#4.1.3时间组成
#有些情况下需要将时间储存为过去了多少秒，但是还有一些情况，程序员需要访问一个日期的各个字段。time模块定义了struct_time来维护日期和时间值，其中分开储存各个组成部分，以便于访问。很多函数都要处理struct_time值而不是浮点数值。
import time
def show_struct(s):
	print ' tm_year :', s.tm_year
	print ' tm_mon  :', s.tm_mon
	print ' tm_mday :', s.tm_mday
	print ' tm_hour :', s.tm_hour
	print ' tm_min  :', s.tm_min
	print ' tm_sec  :', s.tm_sec
	print ' tm_wday :', s.tm_wday
	print ' tm_yday :', s.tm_yday
	print ' tm_isdst:', s.tm_isdst
	print 'gmtime:'
show_struct(time.gmtime())
print '\nlocaltime:'
show_struct(time.localtime())
print '\nmktime:', time.mktime(time.localtime())
#gmtime()函数以UTC格式返回当前时间。localtime()会返回应用了当前市区的当前时间。mktime()取一个struct_time实例，将它转换为浮点数表示。

#4.1.4处理时区
#修改时区不会改变具体的时间，只是会改变表示时间的方式。要改变时区，需要设置环境变量TZ,然后调用tzset()。设置是趋势可以指定很多细节，甚至细致到日光节省时间的开始和结束时间。不过，通常更容易的做法是使用时区名，并由底层库推导出其他信息。下面这个示例程序将修改时区值，并说明这些改变对time模块中的其他设置有什么影响。
import os
import time
def show_zone_info():
	print ' TZ    :', os.environ.get('TZ', '(not set)')
	print ' tzname:', time.tzname
	print ' Zone  :', '%d (%d)' % (time.timezone,
									(time.timezone / 3600))
	print ' DST   :', time.daylight
	print ' Time  :', time.ctime()
print 'Default :'
show_zone_info()
ZONES = ['GMT',
		 'Europe/Amsterdam',
		]
for zone in ZONES:
	os.environ['TZ'] = zone
	time.tzset()
	print zone, ':'
	show_zone_info()	
print
#4.1.5解析和格式化时间
#time模块提供了两个函数strptime()和strftime()，可以在struct_time和时间值字符串表示之间转换。模块提供了大量格式化指令来支持以不同方式输入和输出。
#下面这个例子将当前时间从一个字符串转换为一个struct_time实例，然后再转换回一个字符串。
import time
now = time.ctime()
print 'Now:', now
parsed = time.strptime(now)
print '\nParsed:'
show_struct(parsed)
print '\nFormatted:', time.strftime("%a %b %d %H:%M:%S %Y", parsed)