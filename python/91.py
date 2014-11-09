
n=50
sum=0

def hcf(i,j):
	x=min(i+1,j+1)
	hcf=0
	while x>=1:
		if i%x==0 and j%x==0 and x>hcf:
			hcf=x
		x-=1
	return hcf

for i in xrange(n+1):
	for j in xrange(i,n+1):
		if i==0 and j>0:
			sum=sum+n
		elif j>0 and i!=j:
			sum=sum+min(int((n-i)/(j/hcf(i,j))),j/(i/hcf(i,j)))+min(int(i/(j/hcf(i,j))),int((n-j)/(i/hcf(i,j))))
#			print "minim",int((n-i)/(j/hcf(i,j))),j
#			print "maxim",int(i/(j/hcf(i,j))),0
		elif j>0:
			sum=sum+min(int((n-i)/(j/hcf(i,j))),j/(i/hcf(i,j)))
#			print "minim",int((n-i)/(j/hcf(i,j))),j
#		print i,j,sum

print "ans",2*sum+n*n

