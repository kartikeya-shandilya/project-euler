
mx_lim=100

chk=matrix(mx_lim,mx_lim)

for(i=1,mx_lim,{
	for(j=1,i,\
		k=i+1-j;
		if(isprime(k),\
			if(k==i,\
				chk[i,k]=1,\
				k1=if(nextprime(k+1)<=mx_lim,nextprime(k+1),k+1);
				chk[i,k]=chk[i,k1]+chk[i-k,k]
			), 
			chk[i,k]=0
		);
	);
	if(chk[i,2]>5000,print(i," ",chk[i,2]))
})
