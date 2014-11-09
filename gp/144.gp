
intersect(Sx,Sy,m)={
	\\print("intersect");
	a=m^2+4;
	b=2*m*(Sy-m*Sx);
	c=m^2*Sx^2+Sy^2-2*m*Sx*Sy-100;
	Nx1=(-b+sqrt(b^2-4*a*c))/(2*a);
	Nx2=(-b-sqrt(b^2-4*a*c))/(2*a);
	Ny1=Sy+m*(Nx1-Sx);
	Ny2=Sy+m*(Nx2-Sx);
	if(Nx1-Sx<10^-10,Nx=Nx2,Nx=Nx1);
	Ny=Sy+m*(Nx-Sx);
	return([Nx,Ny]);
}

new_slope(Ix,Iy,m)={
	\\print("new_slope");
	n=Iy/(4*Ix);
	d=abs(atan(n)-atan(m));
	if(n>m,o=atan(n)+d,o=atan(n)-d);
	return(tan(o));
}

Sx=0.0; Sy=10.1;
Dx=1.4; Dy=-9.6;
m=(Dy-Sy)/(Dx-Sx);
m_init=m;
Sx=Dx; Sy=Dy;

z=500; it=z;
while(it, m=new_slope(Sx,Sy,m); pts=intersect(Sx,Sy,m); Sx=pts[1]; Sy=pts[2]; it-=1; if(abs(Sx)<.01&Sy>0,print(z-it+1," Check")))




