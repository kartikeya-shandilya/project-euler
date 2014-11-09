#!/usr/bin/perl

$max=0;

for ($i=-1000;$i<1000;$i++){
 for ($j=-1000;$j<1000;$j++){
  $cnt=0;
  for ($k=0;$k<100;$k++){
   $val=$k*$k+$i*$k+$j;
   if ($val >= 0 and &isPrime($val)) { $cnt++; }
   else { last; }
  }
  if ($cnt>$max) { 
   $max=$cnt; $a=$i; $b=$j;
   print "$max,$a,$b,",$a*$b,"\n";
  }
 }
}

print "ans: $max,$a,$b,",$a*$b,"\n";

sub isPrime{
 my $y=$_[0];
 chomp $y;
 my $i=0;
# print "isPrime:",$y,"\n";
 my $d=1;
 if ($y>1) {
  if ($y%2 eq 0) { 
#   print "if1\n"; 
   $d=0; return $d; 
  }
  for($i=3;$i<=int(sqrt($y))+1;$i=$i+2) {
   if($y%$i eq 0){
#    print "if2\n";
    $d=0; return $d;
   }
  }
 }
 else { 
#  print "else1\n"; $d=0; 
 }
 return $d;
}

