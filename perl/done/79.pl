#!usr/bin/perl

use Math::BigInt;

open FILE, "<keylog.txt";

@Array;
$i=0;

foreach(<FILE>){
 chomp;
 $Array[$i]=$_;
 print $Array[$i],"\n";
 $i++;
}

close FILE;
$j=Math::BigInt->new('1000000000');

for(;$j<=1000000000000;$j++) {
 if($j % 10000 eq 0) { print "j = $j\n"; }
 $k=1;
 for($i=0;$i<=$#Array;$i++) {
#  print $j," :: ",$Array[$i];
  $res=ind($Array[$i],$j);
#  print " $res\n";
  if($res ne 1) { $k=0; last; }
 }
 if($k eq 1) { print "ans : $j\n"; last;}
}

sub ind {
 $x=shift;
 $y=Math::BigInt->new(shift);
 @Xarr=split//,$x;
 @Yarr=split//,$y;
# print "$x , $y :: ";
 for($a=0,$b=0;($a<=$#Xarr)and($b<=$#Yarr);) {
  if($Xarr[$a] eq $Yarr[$b]) { $a++; $b++; }
  else { $b++; }
 }
 if($a eq $#Xarr+1) { 
  #print "1\n"; 
  return(1); 
 }
 else { 
  #print "0\n"; 
  return(0); 
 }
}
