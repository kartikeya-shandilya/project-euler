#!/usr/bin/perl

print "n,k,m,l";

for($n=0;$n<=3;$n++){
for($m=0;$m<=2;$m++){
  print "\n";
  for($k=$n;$k>=0;$k--){
  for($l=$m;$l>=0;$l--){
    if ($n eq $k and $m eq $l) { $mat[$n][$k][$m][$l]=1; }
    else {
      $mat[$n][$k][$m][$l]=$mat[$n-$k][$k][$m][$l+1]+$mat[$n][$k+1][$m][$l+1]+$mat[$n][$k+1][$m-$l][$l]+$mat[$n-$k][$k][$m-$l][$l];
    }
    print "$n,$k,$m,$l:",$mat[$n][$k][$m][$l],"\n";
  }}
  print "\n";
}}

