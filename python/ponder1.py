import numpy

def sum_d(m,n,x1,x2):
	i=m+x1; j=n+x2; res=1
	while (0<=i<q and 0<=j<q):
		if(matrix[i][j]>1 and matrcp[i][j]==1): res=0
		i+=x1; j+=x2;
	i=m; j=n
	while (0<=i<q and 0<=j<q):
		if(matrix[i][j]>1 and matrcp[i][j]==1): res=0
		i-=x1; j-=x2;
	return res

def add_d(m,n,x1,x2):
	i=m+x1; j=n+x2;
	while (0<=i<q and 0<=j<q):
		if(i!=m and j!=n): matrix[i][j]+=1
		i+=x1; j+=x2;
	i=m; j=n
	while (0<=i<q and 0<=j<q):
		if(i!=m and j!=n): matrix[i][j]+=1
		i-=x1; j-=x2;	

def addqueen():
	import random
	m=random.randrange(q)
	n=random.randrange(q)
	rc_flag=1
	for i in range(q):
		if((matrix[m][i]>1 and matrcp[m][i]==1) or (matrix[i][n]>1 and matrcp[i][n]==1)): rc_flag=0
	if(rc_flag==1 and matrcp[m][n]!=1 and matrix[m][n]<2):
		d1_flag=sum_d(m,n,1,1)
		d2_flag=sum_d(m,n,1,-1)
		if (d1_flag+d2_flag==2):
			for i in range(q):
				if(i!=n): matrix[m][i]+=1
				if(i!=m): matrix[i][n]+=1
			add_d(m,n,1,1)
			add_d(m,n,1,-1)
			matrix[m][n]+=1
			matrcp[m][n]=1
			seq.append([m,n])

q=6; sum=0; y=0; max=0;
while(y<=q**6/2):
	y+=1; sum=0;
	matrix = numpy.zeros((q,q),int)
	matrcp = numpy.zeros((q,q),int)
	seq = []
	for i in range(q*q): addqueen()
	for i in range(q):
		for j in range(q): sum=sum+matrcp[i][j]
	if sum>max:
		max=sum
		for i in range(q): print matrcp[i]
		print seq,"\n"
