
g(x,n)=x^3-2^n*x^2+n*x^2

for(i=1,100,a=solve(x=1,2^i,g(x,i));print(i,a))

get(x,n)=if(x>=10^n,x%10^n,x)

pow(a,n)={
if(n==1,ret=a%10^8,
	if(n%2==0,ret=pow(a^2%10^8,n/2)%10^8,
		ret=(a*pow(a^2%10^8,(n-1)/2))%10^8));
print(a," ",n," => ",ret);
ret
}

