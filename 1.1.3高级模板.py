# -*- coding: utf-8 -*-	
#高级模板，可以修改delimiter和idpattern类属性
import string
#定界符
#替换
#忽略
#在这个例子里，替换规则已经改变，定界符是%不是$，另外变量名必须包含一条下划线
template_text = '''
    Delymiter: %%	
    Replaced : %with_underscore
    Ignored  : %notunderscored
'''
d = { 'with_underscore':'replace', 
      'notunderscored':'not replaced', 
      }
class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z] + '
t = MyTemplate(template_text)
print 'Modified ID pattern:'
print t.safe_substitute(d)

#要完成更复杂的修改，可以覆盖pattern属性，定义一个全新的正则表达式。所提供的模式必须包含4个命名组，分别对应转义定界符，明明变量，用大括号扩住的变量名，以及不合法的定界符模式
#t.pattern是一个已经编译的正则表达式 不过可以通过其pattern属性得到原来的字符串表示
import string
t = string.Template('$var')
print t.pattern.pattern

#例子 定义一个新的模式来创建一个新的模板类型: 使用{{var}}作为变量语法
import re
import string
class MyTemplate(string.Template): 
	delimiter = '{{'
	pattern = r'''
    	\{\{(?:
    	(?P<escaped>\{\{)| (?P<named>[_a-z][_a-z0-9]*)\}\}|
    	(?P<braced>[_a-z][_a-z0-9]*)\}\}|
    	(?P<invalid>)
    	)
    	'''
t = MyTemplate('''
{{{{
{{var}}
''')
print 'MATCHES:', t.pattern.findall(t.template)
print 'SUBSTITUTED', t.safe_substitute(var='replacement')