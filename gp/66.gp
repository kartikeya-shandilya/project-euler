pell(x, y, n) = x^2-n*y^2

next_trms(n,p,q)={
	x=floor(p*sqrt(n)+q);
	p_new=p/(p^2*n-(q-x)^2);
	q_new=(x-q)/(p^2*n-(q-x)^2);
	return([x,p_new,q_new]);
}

max_X=0; n_val=0;
for(n=1,1000,{
	if(issquare(n),next);
	p_val=1; q_val=0;
	arr=[];
	while(1,\
		tmp_arr=next_trms(n,p_val,q_val);
		arr=concat(arr,tmp_arr[1]);
		p_val=tmp_arr[2]; q_val=tmp_arr[3];
		z=contfracpnqn(arr);
		a=z[1,1]; b=z[2,1];
		chk=pell(a,b,n);
		if(chk==1,if(n%100==0,print(n));if(a>max_X,max_X=a; n_val=n);break);
	);
})
print(max_X," ",n_val);