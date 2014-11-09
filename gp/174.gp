
mx=32;
N=listcreate(mx);
for(i=1,mx,listput(N,0);n=0;fordiv(i,j,if(j>sqrt(i),break);if(j%2==0 && i/j%2==0,n+=1));N[i]=n);

L=listcreate(10);
for(i=1,10,listput(L,0));
for(i=1,mx,if(N[i]>0 && N[i]<11,L[N[i]]+=1));


\\ Solution below:

mx=10^6;
L=listcreate(15);
for(i=1,15,listput(L,0));
for(k=1,mx/4,\
	i=4*k; n=0;\
	fordiv(i,j,if(j>=sqrt(i) || n>15,break);if(j%2==0 && i/j%2==0,n+=1));\
	if(n>0 && n<16,L[n]+=1));
sum(i=1,10,L[i])
\\ 209566
