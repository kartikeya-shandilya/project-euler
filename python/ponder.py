import numpy

def sum_d(m,n,x1,x2):
	i=m+x1; j=n+x2; res=0
	while (0<=i<q and 0<=j<q):
		res=res+matrix[i][j]
		i=i+x1
		j=j+x2
	i=m; j=n
	while (0<=i<q and 0<=j<q):
		res=res+matrix[i][j]
		i=i-x1
		j=j-x2
	return res

def addqueen():
	import random
	m=random.randrange(q)
	n=random.randrange(q)
	sum_r=0; sum_c=0
	for i in range(q):
		sum_r=sum_r+matrix[m][i]
		sum_c=sum_c+matrix[i][n]
	if (sum_r+sum_c<=0):
		sum_d1=sum_d(m,n,1,1)
		sum_d2=sum_d(m,n,1,-1)
		if (sum_d1+sum_d2<=0):
			matrix[m][n]=1

q=6; sum=0; y=0
while(sum!=q+1):
	y+=1
	matrix = numpy.zeros((q,q),int)
	for i in range(q*q):
		addqueen()
	sum=0
	for i in range(q):
		for j in range(q):
			sum=sum+matrix[i][j]

print y
for i in range(q):
	print matrix[i]

