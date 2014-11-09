
mx=51; 
for(i=2,mx,{
	for(j=1,floor(i/2),\
		num=binomial(i,j);
		if(issquarefree(num),\
			print(i,",",j,",",num);
			ans+=num
		)
	)
})



