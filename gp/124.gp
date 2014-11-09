
rad(n) = {prm_fctrs=mattranspose(factor(n)[,1]); ans=prod(i=1,length(prm_fctrs),prm_fctrs[i]); return(ans)}

fullarr=matrix(2,100000); 
for(j=1, 100000, fullarr[1,j]=j; fullarr[2,j]=rad(j));
vecsort(vecsort(fullarr,1),2)[,10000];
