
alex=listcreate(1000000) 
x=1; c=1; for(p=1,200000,if(c>=1000*x,print(c," ",p);x=x+1);fordiv(p^2+1,k,if(k>sqrt(p^2+1),break);listput(alex,p*(p+k)*(p+(p^2+1)/k));c=c+1))
listsort(alex);
alex[150000]

#1884161251122450

