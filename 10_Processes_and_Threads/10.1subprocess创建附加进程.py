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