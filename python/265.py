
def recRing(i):
	prev = ring[i-m+1:i]
	if i == n-1:
		new=[]
		for k in listAll:
			new.append(k[:])
		allgood = 1
		check = ring[-m:]
		if check not in new:
			new.append(check)
		for j in xrange(1,m):
			check = ring[n-m+j:]+ring[:j]
			if check not in new:
				new.append(check)
			else:
				allgood = 0
		if allgood == 1:
			ans.append(ring[:])
			return
		else:
			return
	for x in [0,1]:
		y = prev+[x]
		if y not in listAll:
			listAll.append(y)
			ring[i]=x
			recRing(i+1)
			z=listAll.pop()

m = 5
n = 2**m
ring = [0]*n
ring[n-1] = 1
o = m

listAll = [[0]*(m)]
ans = []

recRing(o)

finAns = 0
for i in ans:
	elm = 0
	for j in xrange(len(i)):
		elm = elm + (2**(len(i)-j-1) * i[j])
	finAns = finAns + elm
	#print i,":", elm

print len(ans)
print "\n-----\nfinAns:", finAns, "\n-----"