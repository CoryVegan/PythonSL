# -*- coding: utf-8 -*-	
#暂时用不了
#本节构建一个播客客户程序，程序展示了如何用多个线程使用Queue类。这个程序要读入一个或多个RSS提要，对专辑排队来显示最新的5集以供下载，并使用线程并行地处理多个下载。这里没有提供足够的错误处理，所以不能在实际生产环境中使用，不过这个骨架实现可以作为一个很好的例子来说明如何使用Queue模块。
#首先要建立一些操作参数。正常情况下，这些参数来自用户输入(首选项,数据库等)。不过在这个例子中，线程数和要获取的URL列表都使用了硬编码值。
from Queue import Queue
from threading import Thread
import time 
import urllib
import urlparse
import feedparser
#Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()
# A real app wouldn't use hard-coded data...
feed_urls = ['http://advocacy.python.org/podcasts/littlebit.rss',
			 ]
#函数downloadEnclosures()在工作线程中运行，使用urllib来处理下载
def downloadEnclosures(i, q):
	"""This is the worker thread function.
	It processes items in the queue one after 
	another. These daemon threads go into an 	
	infinite loop, and only exit when
	the main thread ends.
	"""
	while True:
		print '%s: Looking for the next enclosure' % i 
		url = q.get()
		parsed_url = urlparse.urlparse(url)
		print '%s: Downloading:' % i, parsed_url.path 
		response = urllib.urlopen(url)
        data = response.read()
		# Save the downloaded file to the current directory
		outfile_name = url.rpartition('/')[-1]
		with open(outfile_name, 'wb') as outfile:
			outfile.write(data)
		q.task_done()
#一旦定义了线程的目标函数，接下来可以启动工作线程。downloadEnclosures()处理语句url = q.get()时，会阻塞并等待，直到队列返回某个结果。这说明，及时队列中没有任何内容，也可以安全的启动线程。



# Set up some threads to fetch the enclosures

for i in range(num_fetch_threads):
	worker = Thread(target=downloadEnclosures,
                    args=(i, enclosure_queue,))
    worker.setDaemon(True)
    worker.start()
#下一步使用Mark Pilgrim的feedparser模块（www.feedparser.org）获取提要内容，并将这些专辑的URL入队。一旦第一个URL增加到队列，就会有某个工作线程提取这个URL,开始下载。这个循环继续增加元素直到提要全部利用，工作线程会依次将URL出队来下载这些提要
# Download the feed(s) and put the enclosure URLs into the queue.
for url in feed_urls:
	response = feedparser.parse(url, agent='fetch_podcasts.py')
for entry in response['entries'][-5:]:
	for enclosure in entry.get('enclosures', []):
		parsed_url = urlparse.urlparse(enclosure['url']) 
		print 'Queuing:', parsed_url.path 
		enclosure_queue.put(enclosure['url'])
#使用join()再次等待队列腾空
# Now wait for the queue to be empty, indicating that we have processed all the downloads.
print '*** Main thread waiting'
enclosure_queue.join()
print '*** Done'










