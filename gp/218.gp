
a^2 + b^2 = c^2
(m^2-n^2)^2 + (2*m*n)^2 = (m^2+n^2)^2

given that 
m^2 + n^2 = o^2
(p^2-q^2)^2 + (2*p*q)^2 = (p^2+q^2)^2

therefore
((p^2-q^2)^2-(2*p*q)^2)^2 + (4*p*q*(p^2-q^2))^2 = (p^2+q^2)^4
(p^4+q^4-6*q^2*p^2)^2 + (4*p*q*(p^2-q^2))^2 = (p^2+q^2)^4

given that
1/2 * (p^4+q^4-6*q^2*p^2) * (4*p*q*(p^2-q^2))
divides 6*28

therefore
q*p^7 - 7*q^3*p^5 + 7*q^5*p^3 - q^7*p
divides 84

chk(p,q)=q*p^7 - 7*q^3*p^5 + 7*q^5*p^3 - q^7*p

cnt=0;
for(i=1,3828,\	
	if(i%100==0,print(i," ",cnt));\
	for(j=ceil(i*(1+sqrt(2))),10^8,\
		if(i^2+j^2>10^8,break);\
		m=j^2-i^2; n=2*i*j;\
		a=m^2-n^2; b=2*m*n; c=m^2+n^2;\
		num=chk(j,i);\
		if(cnt>20,break);\
		if(num%42==0&&num>0,cnt+=1;print(cnt," : ",m," ",n," ",a," ",b," ",c))));

p^2 - 2*p*q - q^2 > 0 ??
p = 2*q +- sqrt(4*q^2 + 4*q^2) / 2
p = q +- sqrt(2)*q
p = q*(1 +- sqrt(2))


q*p^7 - 7*q^3*p^5 + 7*q^5*p^3 - q^7*p
p*q*(p^2-q^2)*(p^4+q^4-p^2*q^2) - 7*p^3*q^3*(p^2-q^2)

p*q*(p^2-q^2)*(p^4+q^4-6*p^2*q^2)
X*D*(D^2-2*X^2)

# 3 minutes
# 14721176
