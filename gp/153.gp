
sm=0;
n=5;
for(i=1,n,z=divisors(i+0*I);z=eval(setunion(z,conj(z)));for(x=1,#z,if(real(z[x])>0&imag(z[x])!=0,sm+=real(z[x])));sm+=sigma(i));

sm

ans(n, S=[])=sigma(n)+sumdiv(n*I, d, if(real(d)&imag(d)&!setsearch(S, d=vecsort(abs([real(d), imag(d)]))), S=setunion(S, [d]); (d[1]+d[2])<<(d[1]!=d[2])))
