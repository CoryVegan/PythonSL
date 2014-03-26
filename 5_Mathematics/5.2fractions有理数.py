# -*- coding: utf-8 -*-	
#5.2.1创建Fraction实例
print '5.2.1创建Fraction实例\n'
#与decimal模块类似,可以采用多种方式创建新值。一种简便的方式是由单独的分子和分母值来创建。
import fractions
for n, d in [(1,2),(2,4),(3,6)]:
	f = fractions.Fraction(n, d)
	print '%s/%s = %s' % (n, d, f)
#计算新值时要保持最小公分母

#创建Fraction的另一种方法是使用<numerator>/<denominator>字符串表示：
for s in ['1/2', '2/4', '3/6']:
	f = fractions.Fraction(s)
	print '%s = %s' % (s, f)
#字符串还可以使用更常用的小数或浮点数记法，即一个小数点分隔的一系列数字
for s in ['0.5', '1.5', '2.0']:
	f = fractions.Fraction(s)
	print '%s = %s' % (s,f)
#浮点数值表示的分子和分母值会自动计算
#还有一类方法可以从有理数的其他表示（如float或Decimal）直接创建Fraction实例
import fractions
for v in [0.1, 0.5, 1.5, 2.0]:
	print '%s = %s' % (v, fractions.Fraction.from_float(v))
#不能精确表示的浮点数值可能会得到出乎意料的结果，使用值的decimal表示则会给出期望的结果
import decimal
for v in [ decimal.Decimal('0.1'),
		   decimal.Decimal('0.5'),
		   decimal.Decimal('1.5'),
		   decimal.Decimal('2.0'),
		  ]:
	print '%s = %s' % (v, fractions.Fraction.from_decimal(v))
#decimal的内部实现不存在标准浮点数表示的精度错误

#5.2.2算数运算
print '\n5.2.2算数运算'
f1 = fractions.Fraction(1, 2)
f2 = fractions.Fraction(3, 4)
print '%s + %s = %s' % (f1, f2, f1 + f2)
print '%s - %s = %s' % (f1, f2, f1 - f2)
print '%s * %s = %s' % (f1, f2, f1 * f2)
print '%s / %s = %s' % (f1, f2, f1 / f2)

#5.2.3近似值,Fraction有一个有用的特性，它能够将一个浮点数转换为一个近似的有理数值
print '\n5.2.3近似值'
import math
print 'PI     =', math.pi
f_pi = fractions.Fraction(str(math.pi))
print 'No limit =', f_pi
for i in [1, 6, 11, 60, 70, 90, 100]:
	limited = f_pi.limit_denominator(i)
	print '{0:8} = {1}'.format(i, limited)
#注意这里的format方法