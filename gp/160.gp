
cnt(n,i)={ans=0;while(n\i,\
	ans+=n\i;
	n=n\i);
	return(ans);}

p=Mod(1,100000);
mx=100000;
for(i=1,mx-1,j=i;while(j%5==0,j/=5);while(j%2==0,j/=2);p=p*Mod(j,100000));
p
d=cnt(mx,2)-cnt(mx,5)
p=p*Mod(2,100000)^d


p=Mod(1,100000);
mx=2*100000;
for(i=1,mx-1,j=i;while(j%5==0,j/=5);while(j%2==0,j/=2);p=p*Mod(j,100000));
p
d=cnt(mx,2)-cnt(mx,5)
p=p*Mod(2,100000)^d

