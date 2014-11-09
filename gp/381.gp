
default(primelimit,100000000);

S_(p)= lift(sum(k=1,5,Mod(truncate(factorial(p-k)),p)))

S(p) = {
  a=Mod(-1,p); 
  b=a; 
  for(k=1,4,
    b=b+a/(p-k); 
    a=a/(p-k)); 
    lift(b)
}

c=0; 
forprime(x=5,10^8,c=c+S(x)); 
c

# c = 139602943319822

# Note: can reduce the calculation from S(p), as first two terms always sum to zero
