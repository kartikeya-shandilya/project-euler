
default(primelimit,10000000);

sm=0;
forprime(i=1,3162,\
	sm+=primepi(floor(10000000.0/i))-primepi(i));
sm

\\a=factor(75)[,1];prod(x=1,#a,a[x])


n=10000000;
sm=0;
{
  forprime(i=1,floor(sqrt(n)),
    forprime(j=i+1,(floor(n/i)),
		  pr=i*j;
		  k=n-n%pr;
		  while(1, 
        fac=factor(k)[,1];	
        prd=prod(l=1,#fac,fac[l]); 	
        if(prd==pr,sm+=k;break); 
        k-=pr;
  )))
}

