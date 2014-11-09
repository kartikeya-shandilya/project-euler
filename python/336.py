
def permute(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield ''.join(tuple(pool[i] for i in indices[:r]))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield ''.join(tuple(pool[i] for i in indices[:r]))
                break
        else:
            return

alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphas=[char for char in alpha]

n=4
seq=permute(alpha[:n],n)

def arrange(config):
	
