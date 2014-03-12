# -*- coding: utf-8 -*-	
#更新后的test_patterns()它会显示与一个模式匹配的编号组和命名组，使后面的例子更容易理解
import re
def test_patterns(text, patterns=[]):
	"""Given source text and a list of patterns, look for
	matches for each pattern within the text and print
	them to stout.
	"""
	# Look for each pattern in the text and print the results
	for pattern, desc in patterns:
		print 'Pattern %r (%s)\n' % (pattern, desc)
		print ' %r' % text
		for match in re.finditer(pattern, text):
			s = match.start()
			e = match.end()
			prefix = ' ' * (s)
			print ' %s%r%s' % (prefix, text[s:e], ' '*(len(text)-e)),
			print match.groups()
			if match.groupdict():
				print '%s%s' % (' ' * (len(text)-s), match.groupdict())
		print
	return