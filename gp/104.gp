
psum(n)={num=n;s=0;while(num,s+=num%10;num\=10);return(s)}
pinvsum(n)={num=n;s=0;while(num,if(num%10,s+=1/(num%10));num\=10);return(s)}
pprod(n)={num=n;s=1;while(num,if(num%10,s*=num%10);num\=10);return(s)}

pandig(n)={if(psum(n)==45&&pinvsum(n)==7129/2520&&pprod(n)==362880,1,0)}

F=Mod([1,1;1,0],10^9);
G=F^2;

FF=[1,1;1,0]
GG=[1,0;0,1]
j=0
for(i=3,10^6,\
	G=G*F;\
	num=lift(G[1,2]);\
	if(pandig(num),\
		GG=GG*FF^(i-j);\
		j=i;\
		fullnum=GG[1,2];\
		len=floor(1+log(fullnum)/log(10));\
		digs=fullnum\10^(len-9);\
		print(i," ",lift(G[1,2])," ",digs);\
		if(pandig(digs),print("FOUND IT!!!!! ",i);break)))
