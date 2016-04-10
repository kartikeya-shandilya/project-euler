
from collections import defaultdict
from fractions import Fraction
import numpy as np

p_shift = {
    -2: Fraction(1, 36),
    -1: Fraction(2, 9),
    0: Fraction(1, 2),
    1: Fraction(2, 9),
    2: Fraction(1, 36),
}

N = 100

p_cache = {}
def p_move(d, n=N):
    if d in p_cache:
        return p_cache[d]
    result = defaultdict(Fraction)
    for i in xrange(-2, 3):
        state = min(abs(d+i), abs(n-(d+i)))
        result[state] += p_shift[i]
    p_cache[d] = result
    return result

# pre-compute all p_moves
for i in xrange(N/2):
    tmp = p_move(i)

# print linear equations
fullmatrix = []
base = [0 for i in xrange(N/2)]
for d in xrange(1, N/2+1):
    prob_move = p_move(d)
    eqtn = base[:]
    for k in prob_move:
        if k == 0:
            continue
        elif k == d:
            eqtn[k-1] = (1. - prob_move[k])
        else:
            eqtn[k-1] = -1. * prob_move[k]
    fullmatrix.append(eqtn)
fullmatrix = np.array(fullmatrix)

# solve equations
rhs = np.ones(N/2)
print np.linalg.solve(fullmatrix, rhs)
