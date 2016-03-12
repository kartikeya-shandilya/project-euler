# manual computation of bernoulli numbers
cache_Z = List([1/2]);
denom_Z = List([]);
Z = (k) -> {\
  if(k==0, return(1));
  if(#cache_Z>=k, return(cache_Z[k]),\
    listput(cache_Z, 1 - sum(i=2, k+1, binomial(k+1, i) * Z(k+1-i)) / (k+1));
    if(denominator(cache_Z[k])==20010, listput(denom_Z, k));
    return(cache_Z[k]);
  );
}

# use pari's implementation
denom_Z = List([]);
for(i = 1, 10^5, \
  tmp = denominator(bernfrac(i));\
  if(tmp==20010, listput(denom_Z, i)))

# Using von Staudt-Clausen Theorem
pcache = List([]);
for(i = 1, 3, \
  p = prime(i); \
  idx = 0; \
  while(1, \
    print(p, " - ", idx); \
    fordiv(308, d, \
      if(d==1, next()); \
      n = p*d + 1; \
      if(isprime(n) & (308%n>0), break()); \
    ); \
    idx = idx + 1; \
  ); \
  listput(pcache, idx);\
)

# Use seive to find number that'll work
pseive = List([1]);
for(i = 1, 9999999, listput(pseive, 1));

idx = 0;
while(idx<#pseive, \
  idx = idx + 1; \
  if(pseive[idx]==0, next(), \
    flag = 1; \
    fordiv(308, d, \
      n = idx*d + 1; \
      if(isprime(n) & (20010%n>0), flag=0; break())); \
    if(flag == 0, \
      j = 1; \
      while(idx*j<#pseive, pseive[idx*j] = 0; j = j + 1))))

for(i=1,313,if(pseive[i],print(i," ",i*308)))

num=0;
for(i=1,#pseive,num=num+pseive[i];if(num==10^5,print(i*308);break()))
