# version 1
lim=400; 
cnt=0; 
\\for(a=1,1+lim/3, for(b=a,min(1+(lim-a)/2,a*a-a), smcnt=0; for(c=b,min(a+b-1,lim-a-b), if(Mod(a*c,a+b)==0,cnt+=1; smcnt=smcnt+1;)); print(a," ",b," ",smcnt)));
for(a=1,1+lim/3, for(b=a,min(1+(lim-a)/2,a*a-a), smcnt=0; for(c=b,min(a+b-1,lim-a-b), if(Mod(a*c,a+b)==0,cnt+=1; smcnt=smcnt+1;));));
##
cnt

# version 2
lim=10000; 
cnt=0; 
\\for(a=1,1+lim/3, for(b=a,min(1+(lim-a)/2,a*a-a), fct=(a+b)/gcd(a,a+b); maxc=min(a+b-1,lim-a-b); rng=maxc-b+lift(Mod(b,fct)); smcnt=if(rng<0,0,if(Mod(b,fct)==0,1,0)+floor(rng/fct)); cnt+=smcnt; print(a," ",b," ",fct," ",maxc," ",rng," ",smcnt)));
for(a=1,1+lim/3, for(b=a,min(1+(lim-a)/2,a*a-a), fct=(a+b)/gcd(a,a+b); maxc=min(a+b-1,lim-a-b); rng=maxc-b+lift(Mod(b,fct)); smcnt=if(rng<0,0,if(Mod(b,fct)==0,1,0)+floor(rng/fct)); cnt+=smcnt;));
##
cnt

# version 3
lim=100000; 
cnt=0;
\\for(a=1,floor(lim/3), b=2*a; prms=mattranspose(factor(a)[,1]); mods=prms; for(i=1,length(prms),mods[i]=Mod(b,prms[i])); while(b<=min(a*a,(lim-a)), c=b-a; fct=(a+c)/gcd(a,a+c); maxc=min(a+c-1,lim-a-c); rng=maxc-c+lift(Mod(c,fct)); smcnt=if(rng<0,0,if(Mod(c,fct)==0,1,0)+floor(rng/fct)); cnt+=smcnt; print(a," ",c," ",smcnt); elm=vecmin(prms-lift(mods)); for(i=1,length(prms),mods[i]+=elm); b+=elm;));
{
  for(a=1,1+lim/3,
    b=2*a; 
    prms=mattranspose(factor(a)[,1]); 
    mods=prms; 
    for(i=1,length(prms),
      mods[i]=Mod(b,prms[i])); 
      while(b<=min(a*a,a+(lim-a)/2), 
        c=b-a; 
        fct=(a+c)/gcd(a,a+c); 
        maxc=min(a+c-1,lim-a-c); 
        rng=maxc-c+lift(Mod(c,fct)); 
        smcnt=if(rng<0,0,if(Mod(c,fct)==0,1,0)+floor(rng/fct)
      ); 
      cnt+=smcnt; 
      elm=vecmin(prms-lift(mods)); 
      for(i=1,length(prms),
        mods[i]+=elm
      ); 
      b+=elm;
  ));
}
##
cnt
