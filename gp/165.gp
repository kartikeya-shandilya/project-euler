
sN=290797;
sNew(sN)={return((sN*sN)%50515093)}

slope(x1,y1,x2,y2)={if(x1==x2,return("Inf"),(y2 - y1)/(x2 - x1))}

segs=listcreate(20000);
slps=listcreate(5000); slp_cnt=1;
for(i=1,20000,sN=sNew(sN);listinsert(segs,sN%500,i);if(i%4==0,listinsert(slps,slope(segs[i-3],segs[i-2],segs[i-1],segs[i]),slp_cnt);slp_cnt+=1))

inSide(x1, y1, x2, y2, x3, y3)={
    chk = (x3<max(x1,x2) && x3>min(x1,x2));
    return(chk)}

iSect(i,j)={
    x1=segs[i]; y1=segs[i+1]; x2=segs[i+2]; y2=segs[i+3];
	p1=segs[j]; q1=segs[j+1]; p2=segs[j+2]; q2=segs[j+3];
    slp1 = slps[(i+3)/4];
    slp2 = slps[(j+3)/4];
    if(slp1==slp2,return(0));
    if(slp1=="Inf",x12 = x1,if(slp2=="Inf",x12 = p1,x12 = (slp2*p1 + y1 - slp1*x1 - q1)/(slp2 - slp1)));
    if(slp1!="Inf",y12 = y1 + slp1 * (x12 - x1),y12 = q1 + slp2 * (x12 - p1));
    \\print(x12," ",y12);
    if(inSide(x1, y1, x2, y2, x12, y12) && inSide(p1, q1, p2, q2, x12, y12),return(1));
    return(0);}

valInt=0;
for(i=1,5000,for(j=i+1,5000,valInt += iSect(4*i-3,4*j-3));if(i%1000==0,print(i," ",valInt)));
print valInt
