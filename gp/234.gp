
seqsum(x,y)=y*(y+1)/2-x*(x+1)/2

mx=101; b=2; sm=0
forprime(i=3,mx,\
	a=b;b=i;\
	sm+=a*seqsum(a-1,b^2\a)+b*seqsum(a^2\b,b)-a*b);
sm

sm=0
for(i=4,10201,\
	lps=ceil(sqrt(i));\
	while(1,if(isprime(lps),break,lps-=1));\
	ups=nextprime(ceil(sqrt(i)));\
	sm+=if((i%lps==0||i%ups==0)&&i%(ups*lps),i));

