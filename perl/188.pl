#!/usr/bin/perl

use Math::BigInt;
$Fac = Math::BigInt->new('1');

$Hyper=1777;
for($j=1855;$j>0;$j--){
 $Fac=1777;
 for($i=1777;$i>0;$i--)
 {
  $Fac=$Fac*$Hyper;
  $Fac=int($Fac%100000000);
 }
 $Hyper=$Fac;
}

print $Hyper,"\n";
