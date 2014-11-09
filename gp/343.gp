
funK1(k) = {\
l=factor(k+1)[1,1];
if(l<=k,funK((k+1-l)/l),k);
}

funK2(k) = {\
if(isprime(k+1),k,l=factor(k+1)[1,1];funK((k+1-l)/l));
}

funK3(k) = {\
if(k%2 & k>1,funK3((k-1)/2),if(isprime(k+1),k,l=factor(k+1)[1,1];funK3((k+1-l)/l)));
}

funK4(k) = {\
if(k%2 & k>1,funK4((k-1)/2),l=factor(k+1)[1,1];if(l<=k,funK4((k+1-l)/l),k));
}

funK5(k) = {\
if(z[1,k]==0,if(isprime(k+1),z[1,k]=k,l=factor(k+1)[1,1];z[1,k]=funK((k+1-l)/l)));
z[1,k];
}

########################################################

funK4(k) = {\
l=factor((k^3+1)/(k+1))[,1];
m=l[length(l)]-1;
l=factor(k+1)[,1];
max(m,l[length(l)]-1)
}

sm1=0;
for(i=2,10^4,sm1+=funK3(i^3));
sm1

sm2=0;
for(i=2,10^6,sm2+=funK4(i));
sm2

sm2=0;
for(i=10^6+1,2*10^6,sm2+=funK4(i));
sm2

35440069342409236

234093382068474946

269533451410884183



