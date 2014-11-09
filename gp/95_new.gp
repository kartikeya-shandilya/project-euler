
sod(n) = sumdiv(n, i, i) - n

upp_lim = 1000000;
smart_sod = matrix(1, upp_lim);
for(i=1, upp_lim,{
	smart_sod[1, i] = sod(i);
});

upp_lim = 1000000;
chck = matrix(1, upp_lim);
chck[1, 1] = ind = flag = cnt = 1;

while(1,{
	x = smart_sod[1, ind];
	if(x>=1 && x<=upp_lim, if(chck[1, x]==1, chck[1, ind]=1; flag=0));
	ind += 1;
	if(ind==upp_lim, print("done, ", cnt); cnt += 1; if(flag==1, break, flag=0; ind=1));
});

