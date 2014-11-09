
arArcSec(k,sig)={
r=1+sig*(1/2/k);
angle=45*Pi/180-asin(1/r/k);
arc=angle*(r^2)/2;
sec=r*sin(angle)/k/sqrt(2);
arc-sec
}

k=1;
ans=2*arArcSec(k,1)
lim=10^5

for(k=2,lim,ans+=k*2*(arArcSec(k,1)-arArcSec(k,-1)))
