
ulp = (x,y) -> { floor(y*y/x)-(x+1)+(y-1)-ceil(x*x/y) };
cpcnt = (x,y,n) -> { floor(y*y/x)-floor(n/x)+y+1-floor(n/y)-if(n<x*y,2) };

i=2; res=0; mxnum=37;
forprime(j=nextprime(i+1),37,res+=ulp(i,j);i=j);
res = res-cpcnt(31,37,1000);
print(res);


arsum = (x,y) -> { y*(y+1)/2 - x*(x+1)/2 };
ulsum = (x,y) -> { x*arsum(x,floor(y*y/x))+y*arsum(floor(x*x/y),y-1)-2*x*y };
cpsum = (x,y,n) -> { x*arsum(floor(n/x),floor(y*y/x))+y*arsum(floor(n/y),y-1)-if(n<=x*y,2*x*y) };

i=2; res=0; mxnum=1000003;
forprime(j=nextprime(i+1),mxnum,res+=ulsum(i,j);i=j);
res = res-cpsum(999983,mxnum,999966663333);
print(res);
