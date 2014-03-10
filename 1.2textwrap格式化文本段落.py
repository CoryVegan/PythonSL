# -*- coding: utf-8 -*-	
sample_text = '''
	The textwrap module can be used to format text for output in 
	situations where pretty-printing is desired. It offers 
	programmatic functionality similar to the paragraph wrapping
	or filling features found in many text editors.
    '''
#填充段落
import textwrap
print 'No dedent:\n'
print textwrap.fill(sample_text,width=50)
#去除现有缩进
dedented_text = textwrap.dedent(sample_text)
print 'Dedented:'
print dedented_text
#结合dedent和fill
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45,70]:
	print '%d Columes:\n' %width
	print textwrap.fill(dedented_text, width=width)
	print
#悬挂缩进
dedented_text = textwrap.dedent(sample_text).strip()
print textwrap.fill(dedented_text,
					initial_indent = '*',#悬挂前加项目符号
					subsequent_indent=' ' * 4,
					width=50,
					)
