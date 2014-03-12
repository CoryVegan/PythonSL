# -*- coding: utf-8 -*-	
#1.3.4和1.3.6中使用
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
			substr = text[s:e]
			n_backslashes = text[:3].count('\\')
			prefix = '.' * (s + n_backslashes)
			print ' %s%r' % (prefix, substr)
		print
	return

if __name__ == '__main__':
	test_patterns('abbaaabbbbaaaaa',
					[('ab', "'a' followed by 'b'"),
					])