
read("E:/ImpDocs/Puzzles/proe/python/324.txt");

f(n)={	v=binary(n);
	l=length(v);
	ans=Mod(matid(512),100000007);
	cur=Mod(fullMat,100000007);
	for(i=1,l,\
		j=l+1-i;
		if(v[j]==1,ans=ans*cur);
		cur=cur*cur;);
	return(ans)
}

