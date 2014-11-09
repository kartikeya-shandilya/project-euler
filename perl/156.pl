#!/usr/bin/perl

for ($i=0;$i<1000000000;$i++) {
# print $i," ";
 @arr=split//,$i;
 for($j=0;$j<=$#arr;$j++)
 { 
  $fun[$arr[$j]]++; 
  if($fun[$arr[$j]] eq $i) { print $i," ",$arr[$j],"\n"; }
 }
}
print "\n------------\n\n";
for($i=0;$i<=9;$i++) { print $i," ",$fun[$i],"\n"; }
