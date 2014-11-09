#!/usr/bin/python

def check_perfect(num):
    return cmp(sum(get_divisors(num)[:-1]), num)
 
def euler23(limit):
    is_abundant = lambda x: check_perfect(x) == 1
    counter = lambda: xrange(1, limit+1)
    def getsums(lst):
        condition = lambda n: (n <= limit)
        getsum = lambda x, ix: takewhile(condition, (x+y for y in lst[ix:]))
        return (n for (ix, x) in enumerate(lst) for n in getsum(x, ix))
    set_difference = lambda x, y: set(x).difference(set(y))
    abundants = filter(is_abundant, counter())
    return sum(set_difference(counter(), getsums(abundants)))

ans=euler23(23000)
print ans
