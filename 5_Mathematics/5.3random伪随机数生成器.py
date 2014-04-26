# -*- coding: utf-8 -*-	
#5.3random_伪随机数生成器
#random模块基于Mersenne Twister算法提供了一个快速伪随机数生成器。原先开发这个生成器是为了向蒙特卡洛模拟生成输入，Mersenne Twister算法会生成一个大周期的近均匀分布的数，以适用于各种类型的应用。
#5.3.1生成随机数
print '5.3.1生成随机数'
#random()函数从所生成的序列返回下一个随机的浮点数值。返回的所有值都落在0<=n<1.0区间内。
import random, os, pickle
print 'random()函数'
for i in xrange(5):
	print '%04.3f' % random.random(),
print
#传入最小值和最大值，uniform()会使用公式min+(max-min)*random()来调整random()的返回值
print 'uniform()函数'
for i in xrange(5):
	print '%04.3f' % random.uniform(1,100),
print
#5.3.2指定种子
print '\n5.3.2指定种子'
random.seed(1)
for i in xrange(5):
	print '%04.3f' % random.random(),
print
random.seed(1)
for i in xrange(5):
	print '%04.3f' % random.random(),
print
#seed会控制生成伪随机数所用公式产生的第一个值，由于公式是确定性的，改变种子后也就设置了要生成的整个序列。
#5.3.3保存状态
#random()使用的伪随机算法的内部状态可以保存，并用于控制后续各轮生成的随机数。继续生成随机数之前恢复前一个状态，这回减少由之前输入得到重复的值或值序列的可能性。getstate()函数会返回1一些数据，以后可以用setstate()利用这些数据重新初始化伪随机数生成器。
print '\n5.3.3保存状态'

if os.path.exists('state.dat'):
    #Restore the previously saved state
    print "Found 'state.dat', initializing random module"
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Use a known start state
    print "No 'state.dat', seeding"
    random.seed(1)
# Produce random values
for i in xrange(3):
    print '%04.3f' % random.random(),
print
 
# Save state for next time
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Produce more random values
print "After saving state:"
for i in xrange(3):
    print '%04.3f' % random.random(),
print
#getstate()返回的数据是一个实现细节，所以这个例子用pickle将数据保存到一个文件，不过可以把它当做一个黑盒。如果程序开始时这个文件存在，则加载原来的状态并继续。每次运行时都会在保存状态之前以及之后生成一些数，以展示恢复状态会导致生成器再次生成同样的值。

#5.3.4随机整数
#random()将生成浮点数。可以把结果转换为证书，不过直接使用randint()生成证书会更方便
print '\n5.3.4随机整数'
print '[1, 100]:',
for i in xrange(3):
    print random.randint(1,100),

print '\n[-5 ,5]:',
for i in xrange(3):
    print random.randint(-5, 5),
print
#randrange可以设置一个步长值
for i in xrange(3):
    print random.randrange(0, 101, 15), # random.randrange(min, max, step)
print '\n'

#5.3.5选择随机元素
print '\n5.3.5选择随机元素'
#随机数生成器有一种常见用法，即从一个枚举值序列中选择元素，即使这些值并不是数字。random包括一个choice()函数，可以在一个序列中随机选择。线面这个例子模拟抛硬币10000次，来统计多少次面朝上，多少次面朝下。
import itertools
for j in xrange(2):
    outcomes = { 'heads':0, 'tails':0, }
    sides = outcomes.keys()
    random.seed() # reset the seed to a random value
    for i in xrange(10000):
        outcomes[ random.choice(sides) ] += 1
        
    for key in sides:
        print key,':',outcomes[key]
    print
#5.3.6排列
print '5.3.6排列'
#要模拟一个扑克牌游戏，需要把一副牌混起来，然后向玩家发牌，同一张牌不能多次使用。使用choice()可能导致同一张牌被发出两次，所以，可以用shuffle()来洗牌，然后在发各张牌时阐述所发的牌。
FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

def new_deck():
    return list( itertools.product(
                    itertools.chain( xrange(2, 11), FACE_CARDS ), 
                    SUITS 
                ))
                
def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print '%2s%s' % j,
        print
        
# Make a new deck, with the cards in order
deck = new_deck()
print "\nInitial deck:"
show_deck(deck)

# Shuffle and sisplay the shuffled deck
random.shuffle(deck)
print "\nShuffled Deck:"
show_deck(deck)

# Deal 4 hands of 5 cards
hands = [ [], [], [], [] ]
for i in xrange(5):
    for h in hands:
        h.append(deck.pop())

# Show the hands
print "\nHands:"
for n, h  in enumerate(hands):
    print '%d:' % (n+1)
    for c in h:
        print '%2s%s' % c,
    print

# Show remaining deck
print "\nRemaining deck:"
show_deck(deck)
#这些扑克牌表示为元祖，由面值和一个表示花色的字母组成。要创建已发出“一手牌”，可以一次向四个列表分别增加一张牌，然后从这副牌中将其删除，使这些牌不会再次发出。

#5.3.7采样
print '\n5.3.7采样'
#很多模拟需要大量输入值中得到随机样本。sample()函数可以生成无重复值的样本，且不会修改输入序列。下面的例子会打印系统字典单词的一个随机样本。
with open('/usr/share/dict/words', 'rt') as f:
	words = f.readlines()
words = [w.rstrip() for w in words]
for w in random.sample(words, 5):
	print w
#5.3.8多个并发生生成器
print '\n5.3.8多个并发生生成器'
#除了模块级函数，random还包括一个Random类来管理多个随机数生成器的内部状态。之前介绍的所有函数都可以作为Random实例的方法得到，而且各个实例可以单独初始化和使用，而不会与其他实例返回的值互相干扰。
import time
print "Default Initialization:\n"

r1 = random.Random()
r2 = random.Random()

for i in xrange(3):
    print '%04.3f  %04.3f' % (r1.random(), r2.random())
    
print "\nSame seed:\n"
seed = time.time()
r1 = random.Random(seed)
r2 = random.Random(seed)
for i in xrange(3):
    print '%04.3f  %04.3f' % (r1.random(), r2.random())
#如果系统上设置了很好地内置随机值种子，不同实例会有唯一的初始状态。不过，如果没有一个好的平台随机值生成器，不同实例往往会用当前时间作为种子，因此会生成相同的值

#为了确保生成器从随机周期的不同部分生成值，可以使用junpahead()调整其中一个生成器的初始状态。
print "\nForce jumpahead on r2:\n"
r1 = random.Random()
r2 = random.Random()
r2.jumpahead(1024)
#Force r2 to a different part of the random period than r1
for i in xrange(3):
    print '%04.3f  %04.3f' % (r1.random(), r2.random())
#jumpahead()的参数应当是基于各生成器所需值个数的一个非负整数。生成器的内部状态根据这个输入值调整，但并不只是按给定的步数递增

#5.3.9SystemRandom
print '\n5.3.9SystemRandom'
#有些操作系统提供了一个随机数生成器，可以访问更多能够引入生成器的信息源。random通过SystemRandom类提供了这个特性，这个类与Random的API相同，不过使用os.urandom()生成值，这构成了所有其他算法的基础。
print "Default Initialization:\n"

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in xrange(3):
    print '%04.3f  %04.3f' % (r1.random(), r2.random())
    
print "\nSame seed:\n"
seed = time.time()
r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)
for i in xrange(3):
    print '%04.3f  %04.3f' % (r1.random(), r2.random())
#SystemRandom产生的序列是不可再生的，因为其随机性来自系统，而不是来自软件状态（实际上，seed()和setstate()根本不起作用）

#5.3.10非均匀分布
#引自c4collins
print '\n5.3.10非均匀分布' 
import decimal, math
# Set up context for rounding
c = decimal.getcontext().copy()
c.rounding = 'ROUND_UP'
c.prec = 2

# Normal
mu    = 7.5    # mean
sigma = 2.0    # std. deviation
print "\nNormal(mu=%d, sigma=%d):" % (mu, sigma)
normal = []
for i in xrange(20):
    normal.append(c.create_decimal( random.normalvariate( mu, sigma ) ))
normal = sorted(normal)
for n in normal:
    print "%02.1d" % n,
    
# Gauss-Normal
print "\n(Gauss) Normal(mu=%d, sigma=%d):" % (mu, sigma)
gauss = []
for i in xrange(20):
    gauss.append(c.create_decimal( random.gauss( mu, sigma ) ))
gauss = sorted(gauss)
for g in gauss:
    print "%02.1d" % g,
    
# Log-Normal
print "\n(Logarithmic) Normal(mu=%d, sigma=%d):" % (mu, sigma)
lognormal = []
for i in xrange(15):
    lognormal.append(c.create_decimal( random.lognormvariate( mu, sigma ) ))
lognormal = sorted(lognormal)
for l in lognormal:
    print "%02.1d" % l,    

# Triangular
low  = 0
high = 10
mode = 7.5
print "\nTriangular(low=%d, high=%d, mode=%d)" % ( low, high, mode)
triangular = []
for i in xrange(20):
    triangular.append( c.create_decimal( random.triangular( low, high, mode ) ) )
triangular = sorted(triangular)
for t in triangular:
    print "%02.1d" % t,

# Exponential
lambd = 1.0 / 7.5 # lambd is (1.0 / the desired mean)
print "\nExponential(lambd=%0.4r)" % ( lambd )
exponential = []
for i in xrange(20):
    exponential.append( c.create_decimal( random.expovariate( lambd ) ) )
exponential = sorted(exponential)
for e in exponential:
    print "%02.1d" % e,

# Pareto distribution
alpha = 1     # shape parameter
print "\n(Long Tail) Pareto(alpha=%d)" % ( alpha )
pareto = []
for i in xrange(20):
    pareto.append( c.create_decimal( random.paretovariate( alpha ) ) )
pareto = sorted(pareto)
for p in pareto:
    print "%02.1d" % p,
    
# Angular (Von Mises)
mu    = math.pi * 1.5  # radians between 0 and 2*pi
kappa = 1.5            # concentration, must be >= 0
print "\n(Von Mises) Angular(mu=%d, kappa=%d)" % ( mu, kappa )
angular = []
for i in xrange(20):
    angular.append( c.create_decimal( random.vonmisesvariate( mu, kappa ) ) )
angular = sorted(angular)
for a in angular:
    print "%02.1d" % a,
    
# Beta distribution
alpha = 1
beta  = 2
print "\nBeta(alpha=%d, beta=%d)" % ( alpha, beta )
beta_v = []
for i in xrange(20):
    beta_v.append( random.betavariate( alpha, beta ) )
beta_v = sorted(beta_v)
for b in beta_v:
    print c.create_decimal(b),
    
# Gamma distribution
print "\nGamma(alpha=%d, beta=%d)" % ( alpha, beta )
gamma = []
for i in xrange(20):
    gamma.append( random.gammavariate( alpha, beta ) )
gamma = sorted(gamma)
for g in gamma:
    print c.create_decimal(g),
    
# Weibull distribution
print "\nWeibull(alpha=%d, beta=%d)" % ( alpha, beta )
weibull = []
for i in xrange(20):
    weibull.append( random.weibullvariate( alpha, beta ) )
weibull = sorted(weibull)
for w in weibull:
    print c.create_decimal(w),