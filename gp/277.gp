seq=Vec("UDDDUdddDDUDDddDdDddDDUDDdUUD");

trans(eq, cd)=
{
	if (cd == "D",
        ret=[3*eq[1], 3*eq[2]]);
    if (cd == "U",
        ret=[3*eq[1]/4, (3*eq[2]- 2)/4]);
    if (cd == "d",
        ret=[3*eq[1]/2, (3*eq[2] + 1)/2]);
	ret
}

n(x)=numerator(x)
d(x)=denominator(x)

st=[3,2];
print1(st," ");
for(i=1, length(seq),{
	char = Str(seq[length(seq)-i+1]);
	st = trans(st, char);
	print1(char,"\n");
	print1(st," ");
});

go=10^15

p=n(st[1])
q=lcm(d(st[1]),d(st[2]))
r=n(st[2])*lcm(d(st[1]),d(st[2]))/d(st[2])

in=round((go * q - r)/p)
t=1
while(t,{
	in=in+1;
	try=in*p+r-q;
	if(try%(3*q)==0, t=0);
});
