
M(n) = n*(n+2)

isTriang(x) = { chk=8*x+1; return(issquare(chk)); }

cnt=0; n=1; add=0; lst=1; r1=2.093836321; r2=2.783611624;
while(1,{
	flag = 0;
	if(isTriang(M(n)),\
		cnt += 1;
		add += n;
		print("n:", n, " M(n):", M(n), " cnt:", cnt, " add:", add);
		flag = 1;
	);
	if(flag==0, n += 1, n = floor(n*if(cnt%2==0, r2, r1)));
	if(cnt==40, break);
});

