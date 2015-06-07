
from collections import Counter as ctr

def perm(n,k):
	if k==1:
		return n
	return n*perm(n-1,k-1)

def comb(n,k):
    if k==0:
        return 1
    if k==1:
        return n
    if k>n/2:
        return comb(n,n-k)
    return perm(n,k)/perm(k,k)

def accelAsc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

def getValidPartitions(n,mx_val,mx_cnt):
	z = accelAsc(n)
	flag = 1
	try:
		while flag:
			try:
				x = z.next()
			except:
				flag = 0
				x = None
			if len(x)<=mx_cnt and all(i<=mx_val for i in x):
				yield x
	except:
		yield None


def combAll(n,lst):
	if len(lst):
		return comb(n,lst[-1])*combAll(n,lst[:-1])
	else:
		return 1

def permAll(lst):
	cntr = ctr(lst)
	ans = 1
	for i in cntr.values():
		ans *= perm(i,i)
	return perm(len(lst),len(lst))/ans

def pad(lst,n):
	if len(lst)==n:
		return lst
	else:
		return pad(lst+[0],n)

tot=70
pick=20
mlm=10
mln=7
ans = getValidPartitions(pick,mlm,mln)
curElm = ans.next()

total = 0

while curElm:
	lnElm = len(curElm)
	thElm = pad(curElm,mln)
	thAns = permAll(thElm)*combAll(mlm,curElm)
	total += lnElm*thAns
	print curElm, thAns
	curElm = ans.next()

print total*1.0/(comb(tot,pick))

