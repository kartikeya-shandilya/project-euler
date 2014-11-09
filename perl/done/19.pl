#!/usr/bin/perl

for($i=1901;$i<2001;$i=$i+1){
# print $i,"\n";
 for($j=1;$j<13;$j=$j+1){
  $val=`cal $j $i | grep '^ 1' | wc -l`;
#  print "val = $val\n";
  $sum=$sum+$val;
#  print $j,$i,$val,"\n";
 }
}

print $sum,"\n";
