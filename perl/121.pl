#!/usr/bin/perl

$y=1;
$z=0;
#@A="";
$ans=getprob(4,$y,$z,@A);

sub getprob{
 my $x=shift;
 my $y=shift;
 my $z=shift;
 my @B=@_;
 print "Start A: ",$x," ",$y," ",$z,"\n";
 print "Start B: ",@B," ",$#B,"\n";
 
 if($#B eq $x-1) {
   $i=0; $j=0;
   while($i<$x) { $j=$j+$B[$i]; $i++; }
   print "Ends: ",$j," ",$y," ",$z,"\n";
   if($j<3) { return($z); }
   else { return($y+$z); }
 }
 else {
   for(my $i=0;$i<=1;$i++){
     if($#B eq -1) { $y=1; }
#    print "y1: ",$y," ",$i,"\n";
     if ($i eq 1) { $y=$y*(1/($#B+3)); }
     else { $y=$y*(($#B+2)/($#B+3)); }
#    print "y2: ",$y," ",$i,"\n";
     push(@B,$i);
     print "Call: ",$x," ",$y," ",$z,"\n";
     if($#B eq -1) { $y=0.5; }
     $z=getprob($x,$y,$z,@B);
     pop(@B);
   }
 }
}

print "ans: ",$ans,"\n";
