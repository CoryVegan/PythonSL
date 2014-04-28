# -*- coding: utf-8 -*-	
#5.4math数学函数
#5.4.1特殊常量
print '5.4.1特殊常量'
import math, random
print 'π: %.30f' % math.pi
print 'π: %.15f' % math.pi
print 'e: %.30f' % math.e

#5.4.2测试异常值
print '\n5.4.2测试异常值'
#浮点数计算可能导致两种类型的异常值。一种是INF（无穷大），如果用double储存一个浮点数值，而它相对于一个有很大绝对值的值溢出时，就会出现这个异常值。
print '{:^3} {:6} {:6} {:6}'.format('e', 'x', 'x**2', 'isinf')
print '{:-^3} {:-^6} {:-^6} {:-^6}'.format('', '', '', '')
for e in range(0, 201, 20):
	x = 10.0 ** e
	y = x*x
	print '{:3d} {!s:6} {!s:6} {!s:6}'.format(e, x, y, math.isinf(y),)
#不过，并不是所有浮点数溢出都会导致INF值，具体地，用浮点数值计算一个指数时，会生成OverflowError而不是保留INF结果
print
x = 10.0 ** 200
print 'x  =', x
print 'x*x=', x*x
try:
	print 'x**2 =', x**2
except OverflowError, err:
	print err
#这种差异是由C和Python所用库中的实现差别造成的
#使用无穷大值的除法运算未定义。将一个数除以无穷大值的结果是NaN（即不是一个数）
x = x*x
y = x/x
print '\nx        =', x
print 'isnan(x) =', math.isnan(x)
print 'y = x/x  =', x/x
print 'y == nan =', y == float('NaN')
print 'isnan(y) =', math.isnan(y)
print

#5.4.3转换为整数
print '5.4.3转换为整数'
#trunc()截断小数点后的数字
#floor()将其输入转换为不大于它的最大整数
#ceil()(上限)会生成按顺序排在这个输入值后的最小整数
HEADINGS = ('i', 'int', 'trunc', 'floor', 'ceil')
print ' '.join(['{:^5}'] * 5).format(*HEADINGS)
print ' '.join(['{:-^5}'] * 5).format('','','','','',)
fmt = ' '.join(['{:5.1f}'] * 5)
TEST_VALUES = [-1.5, -0.8, -0.5, -0.2, 0, 0.2, 0.5, 0.8, 1,]
for t in sorted(TEST_VALUES):
    print fmt.format(t, int(t), math.trunc(t), math.floor(t), math.ceil(t) )
print

#5.4.4其他表示
print '5.4.4其他表示'
#modf()取一个浮点值，并返回一个tuple，其中包含这个输入值的小数和整数部分,返回值中的两个数都是浮点数
for i in range(6):
	print '{}/2 = {}'.format(i, math.modf(i/2.0))
#frexp()返回一个浮点数的尾数和指数，可以用来对这个值创建一种更可移植的表示
print ' '.join(['{:^7}'] * 3).format('x', 'm', 'e')
print ' '.join(['{:-^7}'] * 3).format('', '', '')
for x in [ 0.1, 0.5, 4.0]:
	m ,e = math.frexp(x)
	print '{:7.2f} {:7.2f} {:7d}'.format(x, m ,e)
#frexp()使用公式x=m*2**e, 并返回值m和e

#5.4.5正号和负号
print '\n5.4.5正号和负号' 
#fabs()
print math.fabs(-1.1)
print math.fabs(-0.0)
print math.fabs( 0.0)
print math.fabs( 1.1)
print
#要确定一个值的符号，比如为一组值给定相同的符号或者要比较两个值，可以使用copysign()来设置正确值的负号。还需要一个蕾丝copysign()的额外函数，因为不能将NaN和-NaN与其他值直接比较
HEADINGS = ('f', 's', '< 0', '> 0', '= 0')
print ' '.join(['{:^5}'] * 5).format(*HEADINGS)
print ' '.join(['{:-^5}'] * 5).format('', '', '', '', '')
for f in [ -1.0, 0.0, 1.0, 
            float('-inf'), 
            float('inf'), 
            float('-nan'), 
            float('nan')
          ]:
    s = int(math.copysign(1, f))
    print '{:5.1f} {:5d} {!s:5} {!s:5} {!s:5}'.format( f, s, f < 0, f > 0, f== 0 )

#5.4.6常用计算
print '\n5.4.6常用计算'
#math包含一个函数来计算一系列浮点数的和，它使用一种高效的算法以尽量减少精度错误
#fsum()用来计算浮点数加法
values = [ 0.1 ] * 10
print "\nInput values:", values
print 'sum()       : {:.20f}'.format(sum(values))
s = 0.0
for i in values:
    s += i
print 'for loop    : {:.20f}'.format(s)
print 'math.fsum() : {:.20f}'.format(math.fsum(values)) 
print

# factorial()常用语计算一系列对象的排列和组合数，它只能处理整数不过它确实接受float参数，只要这个参数可以转换为一个整数而不会丢值
for i in [ 0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.1 ]:
    try:
        print '{:2.0f}  {:6.0f}'.format( i, math.factorial(i) )
    except ValueError, err:
        print 'Error computing factorial(%s):' % i, err
print

# gamma() is similar to factorial, but it also works with real numbers
# gamma = (n-1)!
for i in [ 0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 ]:
    try:
        print '{:2.0f}  {:6.0f}'.format( i, math.gamma(i) )
    except ValueError, err:
        print 'Error computing gamma(%s):' % i, err
print
        
#gamma()类似于factorial()，不过它可以处理实数，而且值会下移一个数(gamma等于(n-1)!)
#lgamma()返回的结果是对输入值求gamma所得绝对值的自然对数
for i in [ 0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6 ]:
    try:
        print '{:2.1f}  {:.20f}  {:.20f}'.format( i, math.lgamma(i), 												math.log(math.gamma(i)) )
    except ValueError, err:
        print 'Error computing lgamma(%s):' % i, err
print

# 求模操作符,fmod()可以为浮点数提供一个更精确的实现
print '{:^4} {:^4} {:^5} {:^5}'.format('x', 'y', '%', 'fmod')
print '{:-^4} {:-^4} {:-^5} {:-^5}'.format('', '', '', '')
for x, y in [ (5, 2), (5, -2), (-5, 2)]:
    print '{:^4.1f} {:^4.1f} {:^5.2f} {:^5.2f}'.format(x, y, x%y, math.fmod(x, y))
print

#5.4.7指数和对数
print '5.4.7指数和对数'
#pow()
for x,y in [
    # Typical Cases
    (2,3), (2.1, 3.2),
    # Always 1
    (1.0, 5), (2.0, 0),
    # NaN
    (2, float('nan')),
    # Roots
    (9.0, 0.5), (27.0, 1.0/3),
    ]:
    print '{:5.1f} ** {:5.3f} = {:6.3f}'.format(x, y, math.pow(x, y))
print

# sqrt(x)
for x in [ 9.0, 3, -1, 144, 145]:
    try:
        print math.sqrt(x)
    except ValueError, err:
        print 'Cannot compute sqrt(%5.2f):' % x, err
print

# log(x, b) ->> x = b**y
# log(x)以自然对数e为底
print math.log(8)
print math.log(8, 2)
print math.log(0.5, 2)
print
# log10(x) 比log(x, 10)更精确
print '{:2} {:^12} {:^10} {:^20} {:8}'.format( 'i', 'x', 'accurate', 'inaccurate', 'mismatch' )
print '{:-^2} {:-^12} {:-^10} {:-^20} {:-^8}'.format( '', '', '', '', '' )
for i in xrange(10):
    x = math.pow(10, i)
    accurate = math.log10(x)
    inaccurate = math.log(x, 10)
    match = '' if int(inaccurate) == i else '*'
    print '{:2d} {:12.1f} {:10.8f} {:20.18f} {:^5}'.format( i, x, accurate, inaccurate, match )
print

# log1p(x)会计算Newton-Mercator序列(1+x的自然对数)
x = 0.00000000000000000000000000000001
print 'x       :', x
print '1 + x   :', 1+x
print 'log(1+x):', math.log(1+x)
print 'log1p(x):', math.log1p(x)
print

# exp(x)计算e**x
x = 2
fmt = '%.20f'
print fmt % (math.e ** 2)
print fmt % math.pow(math.e, 2)
print fmt % math.exp(2)
print

# expm1()计算e**x-1
x = 0.00000000000000000000000000000001
print 'x       :', x
print 'exp(x)-1:', math.exp(x)-1
print 'expm1(x):', math.expm1(x)
print

#5.4.8角
print '5.4.8角'
#把角度转换为弧度,可以使用randians()
print ' '.join(['{:^7}'] * 3).format( 'Degrees', 'Radians', 'Expected' )
print ' '.join(['{:-^7}'] * 3).format( '', '', '' )
for deg, expected in [
    (   0,         0 ),
    (  30, math.pi/6 ),
    (  45, math.pi/4 ),
    (  60, math.pi/3 ),
    (  90, math.pi/2 ),
    ( 180, math.pi   ),
    ( 270, 3 / 2.0 * math.pi ),
    ( 360, 2        * math.pi ),
]:
    print '{:7d} {:7.2f} {:7.2f}'.format( deg, math.radians(deg), expected )
print

# 弧度转换为度，可以使用degrees()
print ' '.join(['{:^8}'] * 3).format( 'Radians', 'Degrees', 'Expected' )
print ' '.join(['{:-^8}'] * 3).format( '', '', '' )
for expected, rad in [
    (   0,         0 ),
    (  30, math.pi/6 ),
    (  45, math.pi/4 ),
    (  60, math.pi/3 ),
    (  90, math.pi/2 ),
    ( 180, math.pi   ),
    ( 270, 3 / 2.0 * math.pi ),
    ( 360, 2        * math.pi ),
]:
    print '{:8.2f} {:8.2f} {:8.2f}'.format( rad, math.degrees(rad), expected )
print

## 5.4.9三角函数
print ' '.join(['{:7}'] * 5).format('Degrees', 'Radians', 'Sine', 'Cosine', 'Tangent')
print ' '.join(['{:-^7}'] * 5).format('', '', '', '', '')

fmt = ' '.join(['{:7.2f}'] * 5)

for deg in xrange(0, 361, 30):
    rad = math.radians(deg)
    if deg in (90, 270):
        t = float('inf')
    else:
        t = math.tan(rad)
    print fmt.format( deg, rad, math.sin(rad), math.cos(rad), t )
print

# 给定一个点(x,y)电[(0,0), (x,0), (x,y)] 构成的三角形的斜边长度可以使用(x**2 + y**2) ** 1/2，hypot()

print '{:^7} {:^7} {:^10}'.format( 'X', 'Y', 'Hypotenuse' )
print '{:-^7} {:-^7} {:-^10}'.format( '', '', '' )
for x, y in [
    # simple points
    (1,1), (-1, -1), 
    # sqrt
    (math.sqrt(2), math.sqrt(2)), 
    # 3-4-5 triangle
    (3,4),
    # on the circle
    (math.sqrt(2)/2, math.sqrt(2)/2), # pi/4 radians
    (0.5, math.sqrt(3)/2) # pi/3 radians
]:
    h = math.hypot(x, y)
    print '{:7.2f} {:7.2f} {:7.2f}'.format( x, y, h )
print

#还可以用[hypot(x,y)]计算两点距离
print ' '.join(['{:^8}'] * 5).format('X1', 'Y1', 'X2', 'Y2', 'Distance')
print ' '.join(['{:-^8}'] * 5).format('', '', '', '', '')

for (x1, y1), (x2, y2) in [ 
    ((  5,  5 ), (  6,  6 )),
    (( -6, -6 ), ( -5, -5 )),
    ((  0,  0 ), (  3,  4 )),    # 3-4-5 triangle
    (( -1, -1 ), (  2,  3 )),    # 3-4-5 triangle
]:
    x = x1 - x2
    y = y1 - y2
    h = math.hypot(x, y)
    print ' '.join(['{:8.2f}'] * 5).format( x1, y1, x2, y2, h )
print

print '{:^3} {:^6} {:^6} {:^6}'.format('R', 'Arcsin', 'Arccos', 'Arctan')
print '{:-^3} {:-^6} {:-^6} {:-^6}'.format('', '', '', '')
for r in [ 0, 0.5, 1 ]:
    print '{:3.1f} {:6.4f} {:6.4f} {:6.4f}'.format( r, math.asin(r), math.acos(r), math.atan(r) )
print

## 5.4.10双曲函数
print '{:^4} {:^6} {:^6} {:^6}'.format('X', 'sinh', 'cosh', 'tanh')
print '{:-^4} {:-^6} {:-^6} {:-^6}'.format('', '', '', '')
for x in xrange(0, 11, 2):
    x = x/10.0
    print '{:4.2f} {:6.4f} {:6.4f} {:6.4f}'.format( x, math.sinh(x), math.cosh(x), math.tanh(x) )
print

## 5.4.11特殊函数
#统计学中经常用到高斯误差函数
#对于误差函数erf(-x)==-erf(x)
print '{:^5} {:7}'.format('X', 'erf(x)')
print '{:-^5} {:-^7}'.format('', '')
for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
    print '{:5.2f} {:7.4f}'.format( x, math.erf(x) )
print
#补余误差函数是1-elf(x)
print '{:^5} {:7}'.format('X', 'erfc(x)')
print '{:-^5} {:-^7}'.format('', '')
for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
    print '{:5.2f} {:7.4f}'.format( x, math.erfc(x) )
print
#如果x值很小，erfc()实现可以避免从1减时可能带来的精度误差