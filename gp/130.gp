
A(n)=if(1<n/=5^valuation(n, 5)<<valuation(n, 2), znorder(Mod(10, n)), 0)

cnt = 0; res = 0;
forcomposite(i=1,10^6,if(gcd(i,10)==1 & (i-1)%A(9*i)==0,cnt+=1;print(i);res=res+i;if(cnt==25,break;)))

res
