# -*- coding: utf-8 -*-	
import string
#capwords
s=' The quick brown fox jumped over the lazy dog.'
print s
print string.capwords(s)
#makestrans
leet = string.maketrans('abegiloprstz','463611092572')
print s
print s.translate(leet)
