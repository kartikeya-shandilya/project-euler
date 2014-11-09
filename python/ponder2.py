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

def addqueen(m,n):
	import random
	rc_flag=1
	for i in range(q): print matrcp[i]
	print
	for i in range(q): print matrix[i]
	print "-"
	for i in range(q):
		if((matrix[m][i]>1 and matrcp[m][i]==1) or (matrix[i][n]>1 and matrcp[i][n]==1)): rc_flag=0
	if(rc_flag==1 and matrcp[m][n]!=1):
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

q=8
matrix = numpy.zeros((q,q),int)
matrcp = numpy.zeros((q,q),int)
seq=[[5, 2], [7, 7], [4, 0], [2, 7], [4, 2], [0, 1], [3, 5], [6, 5], [1, 4], [0, 3]]
for i in range(10): addqueen(seq[i][0],seq[i][1])


