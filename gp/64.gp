contFrac(n)={
	f=floor(n);
	d=n-f;
	[f,precision(1.0/d,1000)];}

cnt=0; lim=10000;

for(i=1,13,{
	if(i%1000==0,print(i));
	x=precision(sqrt(i),1000);
	a=floor(x);
	ln=0;
	if(x!=a,\
		n=1.0/(x-a);\
		t=1;\
		while(t,\
			ans=contFrac(n);\
			f=ans[1]; n=ans[2];\
			ln+=1;\
			if(f==2*a, t=0);\
		);\
	);
	print(i," ",ln);
	cnt+=ln%2;});

print(cnt);



contFrac(n, i, j, res)={
	print("i:",i," j:",j," res:",res);
	if(i==j,return(res));
	f=floor(n);
	d=n-f;
	listput(res, i, f);
	contFrac(precision(1.0/d,1000), i+1, j, res);
}


ln=0;
x=precision(sqrt(1669),1000);
a=floor(x);
n=precision(1.0/(x-a),1000);
t=1;
while(t,{
	ans=contFrac(n);
	f=ans[1]; n=ans[2];
	ln+=1;
	print(ln, " ", f);
	if(f==2*a, t=0);
	if(ln>69,break);
});

res=listcreate(60)
contFrac(precision(sqrt(1669),1000), 1, 60, res)
