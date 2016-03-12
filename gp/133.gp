
# old definition == slow
rep_rem = (k, n) -> {\
  phi_n = eulerphi(n);
  phi_phi_n = eulerphi(phi_n);
  k = lift(Mod(k,phi_phi_n));
  k = lift(Mod(10^k,eulerphi(n)));
  lift(Mod(10^k,n)-1)
}

# old definition == slow
check_rems = (n) -> {\
  rems = Set();
  i = 1;
  while(1,\
      rem = rep_rem(i, n);
      if(rem == 0,\
        return(0),\
        if(setsearch(rems,rem),
          return(n),\
          rems = setunion(rems,Set(rem));
      i += 1;
  )));
}

res = 5; prev = 0;
forprime(i=7, 10^4, if(i\1000>prev,print(i,"..",res);prev=prev+1); if(check_rems(i)>0, res+=i))
res


# new definition
new_check_rems = (p) -> {\
  z = znorder(Mod(10,p));
  l = lcm(z,10);
  if(omega(l)==2, return(0), return(1));
}

res = 10; prev = 0;
forprime(i=7, 10^5, if(i\10000>prev,print(i,"..",res);prev=prev+1); if(new_check_rems(i)>0, res+=i))
