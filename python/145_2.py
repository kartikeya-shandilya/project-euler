
def isodd(num):
	res=1
	for i in xrange(len(num)):
		res=res*(int(num[i])%2)
		if res==0:
			break
	return res

cnt=0
for i in xrange(1,1000000000):
	if i%10!=0:
		new=i+int(`i`[::-1])
		cnt=cnt+isodd(`new`)

print cnt
