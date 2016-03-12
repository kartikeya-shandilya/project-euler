
def gcd_10(n):
    if n%2 == 0 or n%5 == 0:
        return False
    return True

def long_div(n):
    if not gcd_10(n):
        return 0
    k = 1
    d = 1
    while k:
        k = (10*k + 1) % n
        d += 1
    return d


if __name__ == "__main__":
    for i in xrange(10**6, 10**6+10000):
        k = long_div(i)
        if k>10**6:
            print i, k
            break
