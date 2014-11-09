
default(primelimit,100000000)

mx=100000000;
sm=0;
{
  forprime(i=1,mx,
    n=i-1;
    fl=1;
    if(moebius(n)==0,next);
    fordiv(n,j,
      if(isprime(j+n/j)==0,fl=0;break);
      if(j>sqrt(n),break)
    );
    sm+=fl*n
  )
} 
sm

#1739023853137
