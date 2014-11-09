
mx=100000;
a=listcreate(mx);
n=10^14-1;
for(i=1,mx,while(1,n=nextprime(n+1);if(isprime(n),break,n+=1));listput(a,n));

F=Mod([1,1;1,0],1234567891011);
sum(i=1,mx,(F^a[i])[1,2])
\\ Mod(283988410192, 1234567891011)
