#!/usr/bin/perl

use Math::BigInt;

for($i=1;$i<999999;$i++) {
 if($i eq reverse($i)) { 
  $j=bin($i);
#  print "bin($i) = $j\n";
  if($j eq reverse($j)) {
   print "$i + $j\n";
   $k+=$i;
  }
 }
}
print "ans is $k\n";

sub bin {
 my $x=shift;
 my $y=Math::BigInt->new('0');
 my $z=Math::BigInt->new('1');
 for(;$x>0;) {
  $y=$y+$z*($x%2);
  $x=int($x/2);
  $z*=10;
 }
 return ($y);
}
