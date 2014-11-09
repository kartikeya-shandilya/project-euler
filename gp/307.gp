
C(n,k)=factorial(n)/(factorial(k)*factorial(n-k))
eq(p,k,n)={res=0;for(i=k,n,res=res+C(n,i)*(p^i)*(1-p)^(n-i));res}
p=solve(p=0,1,eq(p,3,7)- 0.0204081633)

P(p,k,n)=C(n,k)*(p^k)*(1-p)^(n-k)

n=1000000;
k=20000;
P_in=P(p,k-1,n);
a=0;
for(i=k-1,n,P_in=P_in*(n-i)*p/((i+1)*(1-p));a+=P_in;)

