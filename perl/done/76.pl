#!/usr/bin/perl

for($n=0;$n<=100000;$n++){
#  print $n,":\n"; 
  for($k=$n;$k>=0;$k--){
    if ($n eq $k) { $mat[$n][$k]=1; }
    else {
      $mat[$n][$k]=$mat[$n-$k][$k]+$mat[$n][$k+1];
    }
  }
  if ($n eq 100) {
    print $n,",",$mat[$n][1],"\n";
    last;
  }
#  print "\n";
}

