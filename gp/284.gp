
sm_b_n(b,n)={if(n==0,return(0));u=b^n-1;l=b^(n-1)-1;return(u*(u+1)/2-l*(l+1)/2)}

sm=0
for(n=1,9,sm+=3*14*sm_b_n(14,n-1)+16)

