# -*- coding: utf-8 -*-	
#1.3.1查找文本中的模式
print '1.3.1查找文本中的模式'
import re
pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print 'Found "%s"\nin "%s"\nfrom %d to %d ("%s")' % \
	(match.re.pattern, match.string, s, e, text[s:e])
#注意上例 % 对于值的取用,这种print的用法更加整齐，修改起来也更加容易
	
	
#start()和end()可以给出字符串中的相应索引,指示与模式匹配的文本在字符串中出现的位置
#1.3.2编译表达式，对于程序频繁使用的表达式，便以这些表达式回更为高效。compile()函数会把一个表达式字符串转化为一个RegexObject
print '\n1.3.2编译表达式'
import re
#Precompile the patterns
regexes = [ re.compile(p)
			for p in [ 'this', 'that' ]
			]
text = 'Does this text match the pattern?'
print 'Text: %r\n' % text
for regex in regexes:
	print 'Seeking "%s" ->' % regex.pattern,
	if regex.search(text):
		print 'match!'
	else:
		print 'no match!'
		
#1.3.3多重匹配
print '\n1.3.3多重匹配'	
#findall() 函数回返回输入中与模式匹配而不重叠的所有字串	
import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.findall(pattern, text):
	print 'Found "%s"' % match

#finditer()会返回一个迭代器，它将生成Match实例，而不像findall()返回字符串。
for match in re.finditer(pattern, text):
	s = match.start()
	e = match.end()
	print 'Found "%s" at %d:%d' % (text[s:e], s, e)

















