getPeriod(n)={
	fr=contfrac(precision(sqrt(n),100));
	a=fr[1];
	cnt=1;
	i=2;
	while(1,\
		if(fr[i]==2*a,break);
		cnt+=1;
		i+=1;
		if(i==length(fr),print("unknown : ",n);break);
	);
	return(cnt);
}

ans=0; 
for(q=1,10000,{
	if(!issquare(q),\
		if(q%10==0,print(q));
		ans+=getPeriod(q)%2;
	);
})