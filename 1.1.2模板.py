# -*- coding: utf-8 -*-	
#标准模板
import string
values = { 'var':'foo'}
t = string.Template("""
Variable          :$var
Escape            :$$
Variable in text  :${var}iable 
""")
print 'TEMPLATE', t.substitute(values)
#标准字符串拼接
s="""
Variable          :%(var)s
Escape            :%%
Variable in text  :%(var)siable
"""
print 'INTERPOLATION:', s % values  
#两者区别在于模板不考虑参数类型，值会转换为字符串再将字符串插入到结果中

#使用safe_substitute()方法，可以避免未能提供模板所需全部参数值时可能产生的异常
import string
values  = {'var':'foo'}
t = string.Template("$var is here but $missing is not provided")

try:
    print 'substitute()    :', t.substitute(values)
except KeyError,  err:
    print 'ERROR:', str(err)

print 'safe_substitute():', t.safe_substitute(values)

