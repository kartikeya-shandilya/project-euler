#!/usr/bin/perl

use Math::BigInt;
$x=Math::BigInt->new('1');

$k=9;$l=0;
for($i=1;$i<7;$i++){
 $l=$l+$i*$k;
 $x=($k*10/9)+(($k*100/9)-$l)/($i+1);
 $k=$k*10;
 print "i k l x : ",$i," ",$k," ",$l," ",$x,"\n"
}

