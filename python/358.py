
# find multiple ============
# for i in xrange(10000):
#     n = (10*i + 1)*56789
#     if n%100000 == 99999:
#         print 10*i+1, n

# def nextprod(mult, prod, size=5):
#     nxt = str(prod)[-size-1]
#     prod += (nxt * 10**size * mult)
#     size += 1
#     return prod, size
#
# mult = 8902
# digs = 56789
# size = 5
# prod = digs * mult
# flag = True
# while flag:
#     prod, size = nextprod(mult, prod, size)
#     if size> str(prod)[-size]


def decimals(number):
    dividend = 1
    while dividend:
        yield dividend // number
        dividend = dividend % number * 10

# PARI code to obtain "nums"
# for(i=72464, 72992, x=10000*i+9891; if(isprime(x), print(x)))

nums = [724949891, 725159891, 725179891, 725369891, 725389891, 725429891,
        725479891, 725509891, 725579891, 725639891, 725729891, 725749891,
        725869891, 725899891, 725929891, 726019891, 726089891, 726169891,
        726179891, 726199891, 726449891, 726509891, 726559891, 726569891,
        726589891, 726599891, 726739891, 726829891, 726859891, 726929891,
        727039891, 727129891, 727219891, 727229891, 727249891, 727429891,
        727439891, 727499891, 727559891, 727679891, 727769891, 727879891,
        727919891, 727949891, 728069891, 728249891, 728269891, 728389891,
        728459891, 728479891, 728549891, 728879891, 728999891, 729029891,
        729079891, 729379891, 729389891, 729449891, 729469891, 729539891,
        729599891, 729719891, 729739891, 729779891, 729799891, 729809891,
        729889891, 729919891]

from itertools import islice
last_7 = lambda x: list(islice(decimals(x), x))[-7:]

rem_nums = []
for num in nums:
    if (num * 56789) % 100000 == 99999:
        rem_nums.append(num)

for num in rem_nums:
    #digs = list(islice(decimals(num), num))
    #print num, digs[-7:], sum(digs)
    print num, 9*(num-1)/2
