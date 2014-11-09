#!/usr/bin/perl

$max=0;

for ($i=23;$i<1000000;$i++){
 $flag=1;
# print "$i : \n";
 for ($j=0;$j<length($i);$j++){
  $p1=int(substr $i, $j, length($i));
  $p2=int(substr $i, 0, ($j+1));
#  print "$i,$p1,$p2 ";
  if (&isPrime($p1) and &isPrime($p2)) { 
#   print " ok\n"; 
  }
  else { 
   $flag=0; 
#   print " not good\n"; 
   last; 
  }
 }
 if ($flag eq 1) { print "$i is good\n"; }
}

sub isPrime{
 my $y=$_[0];
 chomp $y;
 my $i=0;
# print "isPrime:",$y,"\n";
 my $d=1;
 if ($y>2) {
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
   if ($y eq 1){
    $d=0;
   }
#  print "else1\n"; $d=0; 
 }
 return $d;
}

