
read("E:/ImpDocs/Puzzles/proe/python/213_matrix.txt");

fullMat=mattranspose(fullMat);

func(n)={	v=binary(n);
	l=length(v);
	ans=matid(900);
	cur=fullMat;
	for(i=1,l,\
		j=l+1-i;
		if(v[j]==1,ans=ans*cur);
		cur=cur*cur;);
	return(ans)
}

res=func(5);
sum(i=1,900,prod(j=1,900,1-res[i,j]))
#330.7211540161449713154821364
