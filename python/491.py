
from operator import mul
from itertools import product
from collections import Counter

# initialize factorials
factorial = {0: 1}
for i in xrange(1, 11):
    factorial[i] = factorial[i-1]*i

# create combos
combos = [x for x in product(*[range(3)]*10) if sum(x) == 10]

# difference in odd-even sums is multiple of 11
# sum1 can be: 45, 34, 23
possible = [23, 34, 45, 56, 67]
valid = lambda x: sum(reduce(mul, i) for i in zip(x, range(10))) in possible
rem_combos = [list(x) for x in combos if valid(x)]
print len(rem_combos)


def complement(x):
    return [2-i for i in x]


def arrangements(x):
    cx = Counter(x)
    lng = sum(x)
    return factorial[lng]/2**cx[2]


def z_arrangements(x):
    x = x[:]
    if not x[0]:
        return 0
    x[0] -= 1
    return arrangements(x)


# count number of 20 digit doubly-pandigital numbers divisible by 11
result = 0
for x in rem_combos:
    tmp_result = arrangements(x) - z_arrangements(x)
    tmp_result *= arrangements(complement(x))
    result += tmp_result
print result
