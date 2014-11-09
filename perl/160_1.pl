#!/usr/bin/perl

#use Math::BigInt;
#$Fac = Math::BigInt->new('1');

$Fac=1;
for($i=10000000;$i>0;$i--)
{
 $j=$i;					#
 while($j%2 eq 0) {$j=$j/2; $k++;}	#
 while($j%5 eq 0) {$j=$j/5; $k--;}	#
 $j=int($j%100000);			#
 $Fac=$Fac*$j;
 $Fac=int($Fac%100000);
}
print $Fac," ",$k,"\n";

while($k>0){
 $Fac=$Fac*2;
 $Fac=int($Fac%100000);
 $k--;
}

print $Fac,"\n";

#for($i=99999,$Ans=$Fac;$i>0;$i--)
#{
# $Ans=$Ans*$Fac;
# $Ans=int($Ans%100000);
#}

#print $Ans,"\n";

