# -*- coding: utf-8 -*-

def triangles():
    L=[1]
    n=0
    while n<50:
        yield L
        LT=L[:1]
        i=0
        while i<len(L)-1:
            LT.append(L[i]+L[i+1])
            i=i+1
        LT.append(1)
        L=LT
#以上语句练习by yangtao20200506
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

from functools import reduce;
def fn(x,y):
    return x*10+y
def char2num(s):
    digts={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digts[s]

reduce(fn,map(char2num,'45678'))

def str2int(s):
    return reduce(fn,map(char2num,s))

def str2intA(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

reduce(fn,map(char2num,'13579'))

def is_odd(n):
    return n%2==1
list(filter(is_odd,[1,2,3,4,5]))

def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(),it)

for n in primes():
    if n<50:
        print(n)
    else:
        break

