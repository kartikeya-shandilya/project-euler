
def capCircs(n):
	if(n==1):
		return set([1])
	elif(n==2):
		return set([1.0/2, 2*1])
	z=set([])
	for i in xrange(1,(n+3)/2):
		x=capCircs(i)
		y=capCircs(n-i)
		for xi in x:
			for yi in y:
				z.add(round(xi+yi,10))
				z.add(round(1/(1.0/xi+1.0/yi),10))
	return z
	
def ans(n):
	if n==1:
		return set([1])
	return capCircs(n).union(ans(n-1))


for i in xrange(18):
        print i+1, len(ans(i+1))

# for pari

#capCircs(n)=if(n==1, return(Set([1])), 				if(n==2, return(Set([1/2, 2])), 					z=Set([]);					for(i=1, ceil(n/2),	print("inside for 1");					x=capCircs(i);						y=capCircs(x-i);						for(j=1, length(x),				print("inside for 2");		for(k=1, length(y),			print("inside for 3");					z=setunion(z,[x[j]+y[k]]);								z=setunion(z,[1/(1/x[j]+1/y[k])]);							)						);					);return(z);		)			)

#capCircs(n)= if(n==1, print("n is",n); return(Set([1])), 	if(n==2, print("n is",n); return(Set([1/2, 2])), 		print("n is",n); 		z=Set([]); 		for(i=1, ceil(n/2), 			print("inside for 1"); 			x=capCircs(i); 	print("got x");		y=capCircs(n-i); 	print("got y");		for(j=1, length(x), 				print("inside for 2"); 				for(k=1, length(y), 					print("inside for 3"); 					z=setunion(z,[x[j]+y[k]]); 					z=setunion(z,[1/(1/x[j]+1/y[k])]); 				); 			); 			return(z); 		)			 	) ) 
