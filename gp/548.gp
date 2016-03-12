
gazinga = (x) -> { \
  if(x==1, return(1));\
  if(isprimepower(x), \
    n = factor(x)[1,2];
    return(2^(n-1)),\
    res=0;\
    fordiv(x, d, res=res+(if(d<x, gazinga(d), 0)));\
    return(res))}

for(i=1, 5000, write("gazinga.txt",i, " : ", vecsort(factor(i)[,2]), " => ", gazinga(i), ", # of div: ", numdiv(i)))

maxn = 10^16;
maxexp = List([]);
maxpr = 1;
forprime(i=1,100,\
  maxpr=i*maxpr;\
  if(maxpr>maxn, break());\
  listput(maxexp, floor(log(maxn)/log(i))))

match = (x, y) -> {\
  if(vecsort(factor(x)[,2])==vecsort(factor(y)[,2]), return(1), return(0));\
}

# check defined in 547.txt
for(i=1,#check,x=check[i];y=gazinga(x);if(match(x,y)==1,print(i," ",x),print(i)))


# faster gazinga
gazinga2 = (x) -> { \
  if(x==1, return(1));\
  if(isprimepower(x), \
    n = factor(x)[1,2];
    return(2^(n-1)),\
    res = 2*gazinga2(x/factor(x)[1,1]);\
    fac = factor(x);\
    prpw = fac[1,1]^fac[1,2];\
    num = x/prpw;\
    fordiv(num, d, res=res+if(d<num, gazinga2(prpw*d), 0));\
    return(res))}
