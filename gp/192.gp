
approxFrac(x, d)={\
	rest=matrix(1,100);
	default(realprecision,100);
	cont=contfrac(sqrt(x));
	i=1; den=0;
	while(1,\
		rest[1,i]=cont[i];
		appMat=contfracpnqn(rest[1,]~);
		num=max(appMat[1,1],appMat[1,2]);
		den=max(appMat[2,1],appMat[2,2]);
		approx=0;
		if(den>0,approx=num/den);
		\\print(x," ",i," ",appMat," ",approx);
		if(den<=d,i=i+1;next;,\
			num=min(appMat[1,1],appMat[1,2]);
			den=min(appMat[2,1],appMat[2,2]);
			min_diff=abs(sqrt(x)-num/den); min_num=num; min_den=den;
			if(cont[i]==1,num=min(appMat[1,1],appMat[1,2]);den=min(appMat[2,1],appMat[2,2]);break);\
			for(j=1,cont[i],rest[1,i]=j;\
				appMat=contfracpnqn(rest[1,]~);\
				num=max(appMat[1,1],appMat[1,2]);\
				den=max(appMat[2,1],appMat[2,2]);\
				if(den<d&abs(sqrt(x)-num/den)<min_diff,min_diff=abs(sqrt(x)-num/den);min_num=num;min_den=den;);\
				approx=0;\
				if(den>0,approx=num/den);\
				\\print(x," ",i," ",j," ",appMat," ",approx);\
				if(den>d,num=min_num;den=min_den;break;);););
		break;);
	return(den);}

sm=0; l=1;
for(k=1,100000,{
	if(k==l^2,l=l+1; next;,b=approxFrac(k,10^12);sm=sm+b;);
	if(k%1000==0,print(k," ",b," ",sm));})

\\sm=57060635927998347	
