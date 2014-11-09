#!/usr/bin/perl

for($i=1;$i<=1000000;$i++) {
# if($count[$i] > 0) { print "$i = $count[$i]\n";}
# else {
  $count[$i]=calc($i,0);
#  print "$i = $count[$i]\n";
  if($count[$i]>$max) { $max=$count[$i]; $ans=$i; print "$i = $count[$i]\n"; }
# }
}

sub calc {
 $x=shift;
 $y=shift;
 if($x eq 1) { return($y); }
 elsif(($x % 2) eq 0) { $y++; calc($x/2,$y); }
 else { $y+=2; calc((3*$x+1)/2,$y); }
}
