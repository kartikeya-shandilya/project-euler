#296.py

x=100

for i in xrange(1,1+x/3):
	for j in xrange(i,min(i*i-i,1+(x-i)/2)):
		for k in xrange(j,min(i+j,x-i-j)):
			if (i*k)%(i+j)==0:
				print i, j, k, i*k/(i+j)
				#else:
				#	print "equi"
			#if (i+j)%k==0:
			#	l=(i+j)/k
			#	if i%l==0:
			#		if i!=j and j!=k:
			#			print i, j, k, i/l
			#		else:
			#			print "equi"

