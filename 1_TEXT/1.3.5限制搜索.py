# -*- coding: utf-8 -*-	
#1.3.5限制搜索，如果提前已经知道只需搜索整个输入的一个子集，可以告诉re限制搜索范围，从而进一步约束正则表达式匹配
print '1.3.5限制搜索\n'
import re 
text = 'This is some text -- with punctuation.'
pattern = 'is'
print 'Text   :', text
print 'Pattern:', pattern
m = re.match(pattern, text)
print 'Match :', m
s = re.search(pattern, text)
print 'Search :', s
print
#已编译正则表达式的search()方法还可以接受可选的start和end位置参数，将搜索限制在输入的一个字串中。
pattern = re.compile(r'\b\w*is\w*\b')
print 'Text:', text
print
pos = 0
while True:
	match = pattern.search(text, pos)
	if not match:
		break
	s = match.start()
	e = match.end()
	print '  %2d : %2d = "%s"' % (s, e-1, text[s:e])
	# Move forward in text for the next search
	pos = e
#这个例子实现了iterall()一种不太高效的形式，每一次找到一个匹配时，该匹配的结束为止将用于下一次搜索
