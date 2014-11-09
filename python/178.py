
reach=[0]*10
distn=[0]*10

def ways(n):
	for i in xrange(10):
		n_reach=reach[:]; n_reach[i]=1
		n_distn=distn[:]; n_distn[i]=1
		f_reach=[0]*10
		f_distn=[0]*10
		for j in xrange(n):
			for k in xrange(10):
				if k>0:	f_reach[k]+=n_distn[k-1]
				if k<9:	f_reach[k]+=n_distn[k+1]
				if k<i:
				