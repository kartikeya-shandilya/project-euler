
from itertools import product

def right_rot(a, b, n):
    mults = range(b/(a+1)+1, (b+1)/a+1)
    num = [None]*n
    num[0] = a
    num[-1] = b
    res = 0
    for m in mults:
        tmp_num = num[:]
        dig = b
        carry = 0
        idx = n-2
        while idx >= 0:
            tmp_dig = (dig*m + carry) % 10
            carry = (dig*m + carry) / 10
            dig = tmp_dig
            if idx:
                tmp_num[idx] = dig
            idx -= 1
            if dig*m + carry == b and dig > 0 and tmp_num[idx+1] == a:
                if (m == 1 and a == b) or (m != 1 and a != b):
                    ans = int("".join(map(str, tmp_num[idx+1:])))
                    res += ans
                    #print 'mult =', m, 'len =', len(str(ans)), 'num =', ans
    return res

ans = 0
for a, b in product(range(1, 10), range(1, 10)):
    ans += right_rot(a, b, 100)
print ans % 10**5
