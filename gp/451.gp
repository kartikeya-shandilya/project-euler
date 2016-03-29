
modinv = (n) -> {
  if(isprime(n) || n==1, return(1),\
    pr_facts = mattranspose(factor(n));
    max_pr = 0;
    for(i = 1, #pr_facts,\
      max_prnum = pr_facts[1,i];
      max_prpow = pr_facts[2,i];
      tmp_pr = max_prnum^max_prpow;
      max_pr = max(max_pr, tmp_pr);
    );
    num = n - max_pr;
    while(num>1,\
      if(num*(num+2) % n == 0,\
        return(num+1);
      );
      if(num*(num-2) % n == 0,\
        return(num-1);
      );
      num = num - max_pr;
    );
    return(1);
  );
}

fastmodinv = (n) -> {
  if(isprime(n) || n==1, return(1),\
    res = 0;
    fordiv(n, d, \
      mygcd = gcd(n/d, d);
      if(Mod(1, mygcd)==Mod(n/d-1, mygcd), \
        tmp = chinese(Mod(1, d), Mod(-1, n/d));
        tmplift = lift(tmp);
        tmpchar = characteristic(tmp);
        ans = n - tmpchar + tmplift;
        if(ans < n-1,
          res = max(res, ans)
        );
      );
    );
  );
  return(res);
}

sum(i=3,2*10^7,fastmodinv(i))
