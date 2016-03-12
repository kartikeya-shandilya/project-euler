
from collections import defaultdict


def is_valid(n, maxdig=2):
    num = str(n)
    for d in num:
        if int(d) > maxdig:
            return False
    return True


dict_sz = 1000
mod_dict = defaultdict(list)
for num in xrange(dict_sz):
    for mult in xrange(dict_sz):
        if is_valid((num * mult) % dict_sz):
            mod_dict[num].append(mult)


def next_mul(n, prev_mul):
    mod = n % dict_sz
    q, r = prev_mul/dict_sz, prev_mul % dict_sz
    try:
        r_idx = mod_dict[mod].index(r)
        r_idx += 1
    except:
        r_idx = 0
        while r_idx < len(mod_dict[mod]):
            if mod_dict[mod][r_idx] > r:
                break
            r_idx += 1
    if r_idx > len(mod_dict[mod])-1:
        q += 1
        r = mod_dict[mod][0]
    else:
        r = mod_dict[mod][r_idx]
    return dict_sz*q + r


def next_valid(n):
    num = '0'+str(n+1)
    ret = ''
    for i, dig in enumerate(num):
        if int(dig) > 2:
            ret = ret[:-1] + str(int(ret[-1])+1)
            ret += '0'*(len(num)-i)
            break
        else:
            ret += dig
    ret = int(ret)
    if is_valid(ret):
        return ret
    else:
        return next_valid(ret)


def find_mult(n):
    mult = mod_dict[n % dict_sz][1]
    cnt = 0
    while True:
        if is_valid(n*mult):
            break
        mult1 = next_mul(n, mult)
        mult2 = next_valid(n*mult-1)/n
        mult = max(mult1, mult2)
        cnt += 1
    return mult, cnt


res = 0
for i in xrange(1, 10001):
    mult, _ = find_mult(i)
    print i, mult
    res += mult
print res
