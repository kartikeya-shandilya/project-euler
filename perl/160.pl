#!/usr/bin/perl

#use Math::BigInt;
#$Fac = Math::BigInt->new('1');

$Fac=1;
for($i=1000000;$i>0;$i--)
{
 $Fac=$Fac*$i;
 while($Fac%10 eq 0) {$Fac=$Fac/10;}
 $Fac=int($Fac%100000);
}
print $Fac," ",$k,"\n";

#for($i=99999,$Ans=$Fac;$i>0;$i--)
#{
# $Ans=$Ans*$Fac;
# $Ans=int($Ans%100000);
#}

#print $Ans,"\n";

