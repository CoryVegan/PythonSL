# -*- coding: utf-8 -*-	
#1.3.4模式语法
print '1.3.4模式语法'
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
	test_patterns(
		'abbaabbba',
		[ ('ab*',    'a followed by zero or more b'),
		  ('ab+',    'a followed by one or more b'), 
		  ('ab?',    'a followed by zero or one b'), 
		  ('ab{3}',  'a followed by three b'),
		  ('ab{2,3}','a followed by two to three b'), 
		])
	#在重复指令后面加上"?"可以关闭贪心行为
	print '在重复指令后面加上"?"可以关闭贪心行为\n'
	test_patterns(
		'abbaabbba',
		[ ('ab*?',    'a followed by zero or more b'),
		  ('ab+?',    'a followed by one or more b'), 
		  ('ab??',    'a followed by zero or one b'), 
		  ('ab{3}?',  'a followed by three b'),
		  ('ab{2,3}?','a followed by two to three b'), 
		])	
	#字符集
	print '字符集\n'
	#字符集是一组字符，包含可以与模式中相应位置匹配的所有字符。例如[ab]可以匹配a或b
	test_patterns(
		'abbaabbba',
		[ ('[ab]', 'either a or b'),
		  ('a[ab]+', 'a followed by 1 or more a or b'), 
		  ('a[ab]+?', 'a followed by 1 or more a or b, not greedy'), 
		])	
	#字符集还可以用来排除某些特定字符，尖字符(^)表示要查找未在随后的字符集中出现的字符
	test_patterns(
		'This is some text -- with punctuation.',
		[ ('[^-. ]+', 'sequences without -, ., or space'),
		])
	#利用字符区间(character range)来定义一个字符集，其中包括一个起点和一个终点之间所有连续的字符，这种方式更加紧凑
	print '利用字符区间\n'
	test_patterns(
		'This is some text -- with punctuation.',
		[ ('[a-z]+', 'sequences of lowcase letters'),
		  ('[A-Z]+', 'sequences of uppercase letters'),
		  ('[a-zA-Z]+', 'sequesnces of lowercase or uppercase letters'),
		  ('[A-Z][a-z]+', 'one uppercase followed by lowercase'),
		])
	#作为字符集的一种特殊情况，元字符"."(点号)指模式应当匹配该位置的任何单字符
	#结合点号与重复可以得到非常长的匹配结果，除非使用非贪心形式
	test_patterns(
		'abbaabbba',
		[ ('a.',    'a followed by any one character'),
		  ('b.',    'b followed by any one character'),
		  ('a.*b',  'a followed by anything, ending in b'),
		  ('a.*?b', 'a followed by anything, ending in b'),
		])
	#转义码Escape Codes 可以对一些预定义的字符集使用转义码。如
	#\d一个数字 \D一个非数字 \s空白符(制表符/空格/换行符等) \S非空白符 \w字母数字 \W非字母数字
	print '转义码Escape Codes\n'
	test_patterns(
		'A prime #1 example!',
		[ (r'\d+', 'sequence of digits'),
		  (r'\D+', 'sequence of nondigits'),
		  (r'\s+', 'sequence of whitespace'),
		  (r'\S+', 'sequence of nonwhitespace'),
		  (r'\w+', 'alphanumeric characters'),
		  (r'\W+', 'nonalphanumeric'),
		])
	#从上例结果可以看出r'\W+'和'\\W+'是一样的。都可以识别转义
	
	#要匹配属于正则表达语法的字符，需要对搜索模式中的字符进行转义
	test_patterns(
		r'\d+ \D+ \s+',
		[ (r'\\.\+', 'escape code'),
		])
	#上例对反斜杠和加号字符进行了转义，因为它们是元字符，在正则表达式中有特殊意义，需要转义才能进行匹配
	
	#锚定,除了描述要匹配的模式的内容外，还可以使用锚定(anchoring)指令输入文本中模式应当出现的相对位置
	#^字符串或行的开始 $字符串或行的结束 \A字符串开始 \Z字符串结束 \b一个单词开头或末尾的空串 \B不在一个单词开头或末尾的空串
	print '锚定\n'
	test_patterns(
		'This is some text -- with punctuation.',
		[ (r'^\w+',     'word at start of string'),
		  (r'\A\w+',    'word at start of string'),
		  (r'\w+\S*$',  'word near end of string, skip punctuation'),
		  (r'\w+\S*\Z', 'word near end of string, skip punctuation'),
		  (r'\w*t\w*',  'word containing t'),
		  (r'\bt\w+',   't at start of word'),
	      (r'\w+t\b',   't at end of word'),
	      (r'\Bt\B',    't, not start or end of word'),
		])