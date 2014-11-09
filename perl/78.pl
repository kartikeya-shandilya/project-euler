#!/usr/bin/perl

for($n=1;$n<=100;$n++){
  for($k=$n;$k>=1;$k--){
    if ($n eq $k) { $mat[$n][$k]=1; }
    else {
      $mat[$n][$k]=$mat[$n-$k][$k]+$mat[$n][$k+1];
    }
    print $mat[$n][$k],",";
  }
#  if ($mat[$n][0]%1000000 eq 0) { print $n,"\n"; }
  print "\n";
}

