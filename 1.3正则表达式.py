# -*- coding: utf-8 -*-	
#1.3.1查找文本中的模式
import re
pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print 'Found "%s"\nin "%s"\nfrom %d to %d ("%s")' % \
	(match.re.pattern, match.string, s, e, text[s:e])
#start()和end()可以给出字符串中的相应索引,指示与模式匹配的文本在字符串中出现的位置