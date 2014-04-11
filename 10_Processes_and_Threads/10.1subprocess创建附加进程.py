# -*- coding: utf-8 -*-	
#10.1subprocess创建附加进程
#10.1.1运行外部命令
#要运行
print '10.1.1运行外部命令'
import subprocess
subprocess.call(['ls','-l'])
#命令行参数作为一个字符串列表传入，这样就无须对引号或其他可能由shell解释的特殊字符转义
#将shell参数设置为true值会使subprocess创建一个中间shell进程，由这个进程运行命令。默认情况下会直接运行命令
subprocess.call('echo $HOME', shell=True)
#使用一个中间shell意味着在运行命令之前会先处理命令串中的变量、glob模式以及其他特殊shell特性
#错误处理
print '\n错误处理'
#call()返回值是程序退出码
#check_call()类似于call()，除了检查退出码，如果只是发生了一个错误，则会产生一个CalledProcessError异常
try:
    subprocess.check_call(['false'])
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
#false命令退出时总有一个非0的状态吗，check_call()会把它解释为一个错误。
#捕获输出
print '捕获输出'
#对于call()启动的进程，其标准输入和输出通道会绑定到父进程的输入和输出。这说明调用程序无法捕获命令的输出。可以使用check_output()捕获输出，以备以后处理
output = subprocess.check_output(['ls', '-l'])
print 'Have %d bytes in output' % len(output)
print output
#以下例子在一个子shell中运行一系列命令。在命令返回一个错误码并退出之前，消息会发送到标准输出和标准错误输出
try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
    )
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
else:
    print 'Have %d bytes in output' % len(output)
    print output
#为了避免通过check_output()运行的命令将错误消息写至控制台，可以设置stderr参数为常亮STDOUT
try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
else:
    print 'Have %d bytes in output' % len(output)
    print output
#现在错误和标准输出通道合并在一起，所以如果命令打印错误消息，它们会被捕获，而不会发送至控制台
#10.1.2直接处理管道
print '\n10.1.2直接处理管道'
#函数call(),check_call(),check_output()都是Popen类的包装器。直接使用Popen会对如何运行命令以及如何处理其输入和输出流有更多控制。例如，可以通过stdin,stout,stderr传递不同的参数，可以模仿os.popen()的不同变种。
#与进程的单向通信
print '与进程的单向通信'
#要运行一个进程并读取它的所有输出，可以设置stdout值为PIPE并调用communication()
print 'read:'
proc = subprocess.Popen(['echo', '"to stdout"'],
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)
#要建立一个管道，以便调用程序写数据，可以设置stdin为PIPE
print 'write:'
proc = subprocess.Popen(['cat','-'],
                        stdin=subprocess.PIPE,
                        )
proc.communicate('\tstdin: to stdin\n')
#要将数据一次性发送到进程的标准输入通道，可以把数据传递到communicate()。这与基于模式'w'使用popen()类似
#与进程的双向通信
print '与进程的双向通信'
#要建立Popen实例同时完成读写，可以结合使用前面几项技术
print 'popen2:'
proc = subprocess.Popen(['cat', '-'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
msg = 'through stdin to stdout'
stdout_value = proc.communicate(msg)[0]
print '\tpass through:', repr(stdout_value)
#这会建立管道，类似于popen2()

#捕获错误输出
print '\n捕获错误输出'
#还可以见识stdout和stderr数据流，类似于popen3()
print 'popen3:'
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
msg = 'through stdin to stdout'
stdout_value, stderr_value = proc.communicate(msg)
print '\tpass through:', repr(stdout_value)
print '\tstderr      :', repr(stderr_value)
#从stderr读取数据与读取stdout是一样的。传入PIPE则告诉Popen关联到通道，communication()在返回之前会从这个通道读取所有数据。

#结合常规和错误输出
print '\n结合常规和错误输出'
#要把错误输出从进程定向到标准输出通道，stderr要使用STDOUT而不是PIPE
print 'popen4:'
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        )
msg = 'through stdin to stdout'
stdout_value, stderr_value = proc.communicate(msg)
print '\tcombined output:', repr(stdout_value)
print '\tstderr value   :', repr(stderr_value)
#10.1.3连接管道段
print '\n10.1.3连接管道段'
#多个命令可以连接为一个管线，即创建单独的一个Popen实例，把它们的输入和输出串联在一起。一个Popen实例的stdout属性用作管线中下一个Popen实例的stdin参数，而不是常量PIPE。输出从管线中最后一个命令的stdout句柄读取。
subprocess.call(['pwd'])
#ps aux|gawk '{print $1,$4}'|sort -n -k 2|tail   显示最耗内存的10个进程 
ps = subprocess.Popen(['ps', 'aux'],
                       stdout=subprocess.PIPE,
                       )
awk = subprocess.Popen(['awk', '{print $1,$4}'],
                        stdin=ps.stdout,
                        stdout=subprocess.PIPE,
                        )
sort = subprocess.Popen(['sort', '-n', '-k', '2'],
                        stdin=awk.stdout,
                        stdout=subprocess.PIPE,
                        )
tail = subprocess.Popen(['tail'],
                       stdin=sort.stdout,
                       stdout=subprocess.PIPE,
                       )
end_of_pipe = tail.stdout
for line in end_of_pipe:
    print '\t', line.strip()

#10.1.4与其他命令交互
print '\n10.1.4与其他命令交互'
#前面的所有例子都假设交互量是有限的。communication()方法读取所有输出，返回之前要等待子进程退出。也可以在程序运行时从Popen实例使用的单个管道句柄增量地进行读写。这个技术可以用一个简单的应答程序来说明，这个程序从标准输入读，并写至标准输出。
#下一个例子使用repeater.py作为子进程。它从stdin读取，将值写至stdout，一次处理一行，直到再没有更多输入。开始和停止时它还会向stderr写一个消息，显示子进程的生命期。
#下一个交互例子将采用不同方式使用Popen实例的stdin和stdout文件句柄。在第一个例子中，将把一组5个数写至进程的stdin，每写一个数就读回下一行输出。第二个例子中仍然写同样的5个数，但要使用communicate()一次读取全部输出。
print 'One line at a time:'
proc = subprocess.Popen('python repeater.py', 
						shell = True,
						stdin = subprocess.PIPE,
						stdout = subprocess.PIPE,
						)
for i in range(5):
	proc.stdin.write('%d\n' % i)
	output = proc.stdout.readline()
	print output.rstrip()
remainder = proc.communicate()[0]
print remainder
print
print 'All output at once:'
proc = subprocess.Popen('python repeater.py', 
						shell = True,
						stdin = subprocess.PIPE,
						stdout = subprocess.PIPE,
						)
for i in range(5):
	proc.stdin.write('%d\n' % i)
output = proc.communicate()[0]
print output
#对于这两种不同的循环，repeater.py:exiting行出现在输出的不同位置上

#10.1.5进程间传递信号
print '\n10.1.5进程间传递信号' 
## 10.1.5 Signalling Between Processes
#os模块的进程管理例子演示了如何使用os.fork()和os.kill()在进程间传递信号。由于每个Popen实例提供了一个pid属性，其中包含子进程的进程id，所以可以完成类似于subprocess的工作。下一个粒子结合了两个脚本。这个子进程为USR信号建立了一个信号处理程序。
#以下脚本作为父进程运行。它启动signal_child.py然后发送USR1信号
import os, signal, time, sys, tempfile
proc = subprocess.Popen( ['python', 'signal_child.py'] )
print "PARENT       : Pausing before sending signal..."
sys.stdout.flush()
time.sleep(1)
print "PARENT       : Signalling child"
sys.stdout.flush()
os.kill( proc.pid, signal.SIGUSR1 )
print
#进程组/会话
print '进程组/会话\n' 
#如果Popen创建的进程创建了子进程，这些子进程不会接收发送给父进程的信号。这说明，使用Popen的shell参数时，很难通过发送SIGNINT或SIGTERM来终止在shell中启动的命令
script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen( [ 'sh', script_file.name ], close_fds=True)
print "PARENT       : Pausing before sending signal %s..." % proc.pid
sys.stdout.flush()
time.sleep(1)
print "PARENT       : Signalling child %s" % proc.pid
sys.stdout.flush()
os.kill( proc.pid, signal.SIGUSR1 )
time.sleep(3)
print
#发送信号所用的pid与等待信号的shell脚本子进程的pid不匹配，韵味在这个例子中，有三个不同的进程在交互
#1.程序10.1
#2.shell进程，它在运行主Python程序创建的脚本
#3.程序signal_child.py

#如果向子进程发送信号但不知道其他进程id，可以使用一个进程组(process group)关联这些子进程，使它们能一起收到信号。进程组用os.setsid()创建，将“会话id”设置为当前进程的id。所有子进程都会从其父进程继承会话id，由于只能在由Popen及其子进程创建的shell中设置，所以不能在创建Popen的同一进程中调用os.setsid()。实际上，这个函数要作为preexec_fn参数传至Popen，从而在fork()之后在新进程中运行这个函数，之后才能使用exec()运行shell。要向整个进程组发送信号，可以提供Popen实例的pid值来使用os.killpg()
def show_setting_sid():
    print 'Calling os.setsid() from %s' % os.getpid()
    sys.stdout.flush()
    os.setsid()
    
proc = subprocess.Popen([ 'sh', script_file.name ], 
						close_fds=True, 
						preexec_fn=show_setting_sid,
						)
print "PARENT       : Pausing before sending signal %s..." % proc.pid
sys.stdout.flush()
time.sleep(1)
print "PARENT       : Signalling child %s" % proc.pid
sys.stdout.flush()
os.killpg( proc.pid, signal.SIGUSR1 )
time.sleep(3)
print
#事件序列如下
# 1. Parent program instantiates Popen
# 2. Popen forks a new process
# 3. new process runs os.setsid()
# 4. new process runs exec() to start the shell
# 5. the shell runs the shell script
# 6. the shell forks again, and that process execs Python
# 7. Python runs signal-child.py
# 8. Parent program signals the process group using the pid of the shell
# 9. Shell and Python process receive he signal
# 10. Shell ignores the signal
# 11. Python invokes the signal handler