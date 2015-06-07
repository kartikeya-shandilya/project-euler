
set range := 1..14;

param prime {i in range};
param limit {i in range};

var a_coeff {i in range} >=0 integer;
var b_coeff {i in range} >=0 integer;
var c_coeff {i in range} >=0 integer;

minimize ratio : sum{i in range}(log10(prime[i])*(c_coeff[i]-a_coeff[i]));

subject to sm_mx{i in range} : a_coeff[i]+b_coeff[i]+c_coeff[i] = limit[i];

subject to b_c : sum{i in range}(log10(prime[i])*(b_coeff[i]-c_coeff[i]))*1000000 <= 0;
subject to a_b : sum{i in range}(log10(prime[i])*(a_coeff[i]-b_coeff[i]))*1000000 <= 0;
