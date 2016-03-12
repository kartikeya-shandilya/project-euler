
maxpow = (x, p) -> { sum(i=1,floor(log(x)/log(p)),Mod(floor(x/p^i),1000000008)) }

maxpws = List([]);
forprime(i=2,100000000,listput(maxpws,maxpow(100000000,i)))
squndivsum(maxpws)

simpMod(a, b, n) = if(b>1, if(b%2, Mod(a, n), 1)*(simpMod(a, b\2, n))^2, Mod(a, n))

res = Mod(1,1000000009);
for(i=1,#maxpws,\
  if(i%100==0,print(i));\
  res = res * (Mod(1,1000000009)+ simpMod(prime(i), lift(2*maxpws[i]), 1000000009)))
## slow.. :|


# time-1
sum(i=1, 100, simpMod(prime(5761200+i), lift(2*maxpws[5761200+i]), 1000000009))
# time-2
sum(i=1, 100, Mod(prime(5761200+i), 1000000009)^lift(2*maxpws[5761200+i]))
