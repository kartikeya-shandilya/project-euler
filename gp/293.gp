
default(primelimit,10^9);
admiss(n) = {
ans = 0;
for(j=1, n/2,
	i = 2*j;
	facs = factor(i)[,1];
	if(facs[length(facs)]<=29 && mattranspose(facs)==primes(length(facs)),
		nxp = nextprime(i+2);
		while(!isprime(nxp),
			nxp = nextprime(nxp+1));
		ans = ans + (nxp-i)));
ans
};

admiss2(n) = {
ans = 0;
i = 1;
while(i<log(n)/log(2),
	j = 2^i;
	i = i+1;
	nxp = nextprime(j+2);
	ans = ans + (nxp-j));
for(j=1, n\6,
	i = 6*j;
	facs = factor(i)[,1];
	if(facs[length(facs)]<29 && mattranspose(facs)==primes(length(facs)),
		nxp = nextprime(i+2);
		ans = ans + (nxp-i)));
ans
};

# faster way
# take all powers of 2 upto n
# cross product with all powers of 3
# cross product with all powers of 5
# ... until powers of 29
# 
# iterate over this list and find next prime > i+1
#
