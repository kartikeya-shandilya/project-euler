
F={}
G={}

def f(n,k):
	if (n,k) in F:
		return F[(n,k)]
	else:
		ret=0
		for i in xrange(1,k+1):
			ret+=g(n,i)
		F[(n,k)]=ret
		return ret

def g(n,k):
	if (n,k) in G:
		return G[(n,k)]
	else:
		ret=0
		if(k==1 or k==n):
			ret=1
		elif k<n-k:
			ret=f(n-k,k)
		else:
			ret=f(n-k,n-k)
		G[(n,k)]=ret
		return ret

def h(n):
	return f(n,n)
	
for i in xrange(1,10001):
	x=h(i)
	if x%1000==0:
		print i,x
	if x%1000000==0:
		break
	

