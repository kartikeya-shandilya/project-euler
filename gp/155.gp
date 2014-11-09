
# for pari

capCircs(n)={
	if(n==1, \
		return(Set([1])),\
		if(n==2, \
			return(Set([1/2, 2])),\
			z=Set([]);\
			for(i=1, ceil(n/2),	print("inside for 1");\
				x=capCircs(i);\
				y=capCircs(x-i);\
				for(j=1, length(x),\
					print("inside for 2");\
					for(k=1, length(y),\
						print("inside for 3");\
						z=setunion(z,[x[j]+y[k]]);\
						z=setunion(z,[1/(1/x[j]+1/y[k])]);)\
					););
			return(z);)
		)}

#capCircs(n)= if(n==1, print("n is",n); return(Set([1])), 	if(n==2, print("n is",n); return(Set([1/2, 2])), 		print("n is",n); 		z=Set([]); 		for(i=1, ceil(n/2), 			print("inside for 1"); 			x=capCircs(i); 	print("got x");		y=capCircs(n-i); 	print("got y");		for(j=1, length(x), 				print("inside for 2"); 				for(k=1, length(y), 					print("inside for 3"); 					z=setunion(z,[x[j]+y[k]]); 					z=setunion(z,[1/(1/x[j]+1/y[k])]); 				); 			); 			return(z); 		)			 	) ) 
