
powInFac(x, f)={
	a=0;
	while(1,\
		f\=x;
		if(f==0, break);
		a+=f;
	);
	return(a)
}

smallestFac(p, n)={
	b=(p-1)*n;
	pw=powInFac(p, b);
	while(pw<n,\
		b+=1;
		pw=powInFac(p, b);
	);
	return(b);
}

Fact(n)={
	ans=1;
	while(n,\
		ans*=n;
		n-=1;
	);
	return(ans);
}

reqFac(f, n)={
	num=Fact(f);
	factors=factor(num);
	factors[,2]*=n;
	mxm=0;
	for(i=1,length(factors[,1]),\
		minFac=smallestFac(factors[i,1], factors[i,2]);
		print(mxm, " ",factors[i,1]," ", factors[i,2]," ",minFac);
		mxm=max(mxm, minFac);
	);
	return(mxm);
}

ck=0; for(i=10,30,print(i,"...");ck+=reqFac(i,1234567890));


/*
if(f==10,\
	num=Fact(f);
	factors=factor(num);,\
	if(isprime(f),{
		fct=matrix(length(factors[,1])+1,2);
		for(i=1,length(fct[,1])-1,{
			fct[i,]=[factor[i,1], factor[i,2]];
		});
		fct[i+1,]=[f, n];
		factors=fct;,\
		fct=factor(f);
		j=1;
		for(i=1,length(factors[,1]),{
			if(factors[i,1]==fct[j,1],{
				factors[i,2]+=n*fct[j,2];
				if(j<length(fct[,1]),{
					j+=1;,\
					break;
				});
			});
		});
	});
);
*/
