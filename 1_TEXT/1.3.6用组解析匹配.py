# -*- coding: utf-8 -*-	
#1.3.6用组解析匹配
#为模式增加组(group)可以隔离匹配文本的各个部分，进一步扩展这些功能来创建一个解析工具。通过包围在小括号中来分组
print '1.3.6用组解析匹配\n'
from re_test_patterns import test_patterns
test_patterns(
	'abbaaabbbbaaaaa',
	[ ('a(ab)',  'a followed by literal ab'),
	  ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
	  ('a(ab)*', 'a followed by 0-n ab'),
	  ('a(ab)+', 'a followed by 1-n ab'),
	])
	
#要访问一个模式中单个组所匹配的字串，可以使用Match对象的groups()方法
import re 
text = 'This is some text -- with punctuation.'
print text
print
patterns = [
	(r'(^\w+)', 'word at start of string'),
	(r'(\w+)\S*$', 'word at end, with optional puncuation'),
	(r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
	(r'(\w+t)\b', 'word ending with t'),
	]
for pattern, desc in patterns:
	regex = re.compile(pattern)
	match = regex.search(text)
	print 'Pattern %r (%s)\n' % (pattern, desc)
	print '  ', match.groups()
print

#使用group()可以得到某个组的匹配。如果使用分组来查找字符串的各部分，不过结果中不需要某些与组匹配的部分，此时group会很有用。
print 'Input text            :', text
#word starting with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print 'Pattern               :', regex.pattern

match = regex.search(text)
print 'Entire match          :', match.group(0)
#第0组表示与整个表达式匹配的字符串
print 'Word starting with "t":', match.group(1)
print 'Word after "t" word   :', match.group(2)
#Python的命名组。通过名字来指示组，以后就可以更容易地修改模式，而不必同时修改使用了匹配结果的代码。要设置一个组的名字，可以使用一下语法:(?P<name>pattern)
print
print text
print
for pattern in [r'^(?P<first_word>\w+)',
				r'(?P<last_word>\w+)\S*$',
				r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
				r'(?P<ends_with_t>\w+t)\b',
				]:
	regex = re.compile(pattern)
	match = regex.search(text)
	print 'Matching "%s"' % pattern
	print ' ', match.groups()
	print ' ', match.groupdict()
	print
#使用groupdict()可以获取一个字典，它将组名映射到匹配的字串。groups()返回有序序列还包含命名模式


#以下的例子将使用更新后的test_patterns()它会显示与一个模式匹配的编号组和命名组，使后面的例子更容易理解
from re_test_patterns_groups import test_patterns
#组可以嵌套在其他组中构成更复杂的表达式
test_patterns(
	'abbaabbba',
	[ (r'a((a*)(b*))', 'a followed by 0-n a and 0-n b'),
	])
#可以使用管道符号|只是应当匹配某一个或另一个模式
#如果候选组不匹配，但是整个模式匹配，groups()的返回值会在序列中本应出现候选组的位置上包含一个None值
test_patterns(
	'abbaabbba',
	[ (r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),
	  (r'a((a|b)+)', 'a then seq. of [ab]'),
	])
#非捕获组(?:pattern)
test_patterns(
	'abbaabbba',
	[ (r'a((a+)|(b+))',    'capturing form'),
	  (r'a((?:a+)|(?:b+))','noncapturing'),
	])
	
	
	










