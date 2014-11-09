
rep(x)={\
	y=1;
	for(j=1,x-1,y=10*y+1);
	y
}

unite(a,b)={\
	for(k=1,#b,if(b[k]<10^7,a=setunion(a,[b[k]])));
	a
}

prms=Set([])
fordiv(10^9,i,if(i<=10^5,fct=factor(rep(i),2*10^5)[,1]~;prms=unite(prms,fct)));
ans=vecsort(eval(prms))

sum(i=1,40,ans[i])