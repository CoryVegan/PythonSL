# -*- coding: utf-8 -*-	
#10.3.3守护与非守护线程
print '10.3.3守护与非守护线程\n'
#到目前为止，示例程序都隐含地等待所有线程完成工作之后才退出。程序有时会创建一个线程作为守护线程(daemon)，这个线程可以一直运行而不阻塞主程序退出。如果一个服务无法用一种容易的方法来中断线程，或者希望线程工作到一半时中止而不损失或破坏数据（如为一个服务监控工具生成“心跳”的线程），对于这些服务，使用守护线程就很有用。要标志一个线程为守护线程，需调用其setDaemon()方法并提供参数True。默认情况下线程不作为守护线程。
import threading, time, logging
logging.basicConfig(level = logging.DEBUG,
					format='(%(threadName)-10s), %(message)s',
					)
def daemon():
    logging.debug( 'Starting' )
    time.sleep(2)
    logging.debug( 'Exiting' )

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon(  ):
    logging.debug( 'Starting' )
    logging.debug( 'Exiting' )
    return

t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()
#输出中没有守护线程的"Exiting"消息，因为在守护线程从其2秒的睡眠时间唤醒之前，所有非守护线程（包括主线程）已经退出。

# 要等待一个守护线程完成工作，需要使用join()方法
d1 = threading.Thread(name='daemon1', target=daemon)
d1.setDaemon(True)
t1 = threading.Thread(name='non-daemon1', target=non_daemon)

d1.start()
t1.start()

d1.join()
t1.join()
# 使用join()等待守护线程退出，这意味着它将有机会生成它的“Exiting”消息
#默认情况下，join()会无限阻塞。还可以传入一个浮点数值，表示等待线程变为不活动所需的时间（秒数）。即使线程在这个时间段内未完成，join()也会返回。
d2 = threading.Thread(name='daemon2', target=daemon)
t2 = threading.Thread(name='non-daemon2', target=non_daemon)
d2.start()
t2.start()

d2.join(1)
print 'd.isAlive()', d2.isAlive()
t2.join()
#由于传入的超时时间小于守护线程睡眠的时间，所以join()返回之后这个线程仍“存活”