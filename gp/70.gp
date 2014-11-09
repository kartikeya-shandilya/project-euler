
sumOfDig(n)={\
sm=0;\
while(1,\
sm+=n%10;\
n=n\10;\
if(n==0,break;));\
sm;\
}

prodOfDig(n)={\
sm=1;\
while(1,\
sm*=if(n%10!=0,n%10,1);\
n=n\10;\
if(n==0,break;));\
sm;\
}

minRatio=10^7;
for(i=2,10^7,{
j=eulerphi(i);
if(sumOfDig(i)==sumOfDig(j),if(prodOfDig(i)==prodOfDig(j),if(i/j*1.0<minRatio,minRatio=i/j*1.0;print(minRatio," ",i," ",j))));
})
