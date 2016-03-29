
idempotent = (n) -> {
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
      if(num*(num+1) % n == 0,\
        return(num+1);
      );
      if(num*(num-1) % n == 0,\
        return(num);
      );
      num = num - max_pr;
    );
    return(1);
  );
}

sum(i=1,10^7,idempotent(i))
