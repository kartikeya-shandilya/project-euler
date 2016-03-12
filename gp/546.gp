
f = (k,n) -> { if(n==0,1,sum(i=0,n,f(k,floor(i/k)))) }

g = (k,n) -> { if(n==0,1,k*sum(i=0,n\k-1,g(k,i))+(1+n%k)*g(k,n\k)) }

for(i=0,32,print(i,"=",g(2,i)))

for(i=0,3^4,print(i,"=",g(3,i)))
