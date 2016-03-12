
from sympy import Symbol 

x = Symbol('x')

# 1 : 4 sided dice outcomes:

D4 = sum([x**i for i in xrange(1, 4+1)])
T = D4**1

# T : 6 sided dice outcomes:
## 1 6 sided dice:
D6 = sum([x**i for i in xrange(1, 6+1)])
## T dice
T_dict = T.as_coefficients_dict()
C = 0
for key, value in T_dict.iteritems():
    pwr  = key.as_powers_dict()[x]
    coef = value
    C += coef*(D6**pwr)

C = C.expand()

# C : 8 sided dice outcomes:
## 1 8 sided dice:
D8 = sum([x**i for i in xrange(1, 8+1)])
## T dice
C_dict = C.as_coefficients_dict()
O = 0
for key, value in C_dict.iteritems():
    pwr  = key.as_powers_dict()[x]
    coef = value
    O += coef*(D8**pwr)

O = O.expand()

# C : 8 sided dice outcomes:
## 1 8 sided dice:
D12 = sum([x**i for i in xrange(1, 12+1)])
## T dice
"""
O_dict = O.as_coefficients_dict()
D = 0
for key, value in O_dict.iteritems():
    pwr  = key.as_powers_dict()[x]
    coef = value
    D += coef*(D12**pwr)

D = D.expand()
"""

from code import interact; interact(local=locals()) 
