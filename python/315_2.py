
num = {0:[1,0,1,1,1,1,1],
    1:[0,0,0,0,1,0,1],
    2:[1,1,1,0,1,1,0],
    3:[1,1,1,0,1,0,1],
    4:[0,1,0,1,1,0,1],
    5:[1,1,1,1,0,0,1],
    6:[1,1,1,1,0,1,1],
    7:[1,0,0,1,1,0,1],
    8:[1,1,1,1,1,1,1],
    9:[1,1,1,1,1,0,1]}

# to count number of segments that are "on" in a digit
def count(i):
    return sum(num[i])
ctdict = {str(i): count(i) for i in xrange(10)}

# to find the number of segments that are "on" in a number
def aroot(n):
    result = 0
    for d in str(n):
        result += ctdict[d]
    return result

# to count number of switches required from one digit to another
def subtr(i, j):
    return sum([num[i][k]!=num[j][k] for k in xrange(7)])
chdict = {(`i`,`j`): subtr(i,j) for i in xrange(10) for j in xrange(10)}

# to find digital root of a number
kroot = {str(i):i for i in xrange(10)}
def droot(n):
    return str(sum([kroot[i] for i in str(n)]))

def samclock(n):
    n_copy = str(n)
    droots = [n_copy]
    while int(n_copy)>=10:
        n_copy = droot(n_copy)
        droots.append(n_copy)
    result = 0
    for num in droots:
        result += 2*aroot(num)
    return result

def maxclock(n):
    n_copy = str(n)
    droots = [n_copy]
    while int(n_copy) >= 10:
        n_copy = droot(n_copy)
        droots.append(n_copy)
    result = aroot(droots[0])
    for i, num in enumerate(droots[1:]):
        prev = droots[i]
        cur = num
        diff = len(prev) - len(cur)
        result += aroot(prev[:diff])
        for i, dig in enumerate(cur):
            result += chdict[(prev[diff+i], dig)]
    result += aroot(droots[-1])
    return result

import pyprimesieve as pp
result = 0
for p in pp.primes(2*10**7):
    if p>10**7:
        s = samclock(p)
        m = maxclock(p)
        result += (s-m)
print result
