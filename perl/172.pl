#!/usr/bin/perl
use Math::BigInt;

$i=18;
$j=fact(18);
$k=comb(18,0);
print "\n$i $j $k\n\n";

$f = Math::BigInt->new('0');

print "x y z\n";
for($x=0;$x<7;$x++){
for($y=0;$y<9;$y++){
for($z=0;$z<6;$z++){
 if(((($x)+(2*$y)+(3*$z)) eq 18)and(($x+$y+$z) < 11)){
 $a = Math::BigInt->new('0');
 $b = Math::BigInt->new('0');
 $c = Math::BigInt->new('0');
 $d = Math::BigInt->new('0');
 $e = Math::BigInt->new('0');
 $a=comb(10,$x)*comb(10-$x,$y)*comb(10-$x-$y,$z)*fact(18)/((2**$y)*(6**$z));
 if(($x-1) >= 0) { $b=comb(9,$x-1)*comb(10-$x,$y)*comb(10-$x-$y,$z)*fact(17)/((2**$y)*(6**$z)); }
 if(($y-1) >= 0) { $c=comb(9,$x)*comb(9-$x,$y-1)*comb(10-$x-$y,$z)*fact(17)/((2**($y-1))*(6**$z)); }
 if(($z-1) >= 0) { $d=comb(9,$x)*comb(9-$x,$y)*comb(9-$x-$y,$z-1)*fact(17)/((2**($y+1))*(6**($z-1))); }
 $e=$a-($b+$c+$d);
 print "$x $y $z   $a $b $c $d $e\n";
 $f=$f+$e;
 }
}
}
}

print "\nf = $f\n\n";

sub fact{
 my $x = Math::BigInt->new(shift);
 my $i=0;
 if($x < 2) {return(1);}
 else{
 for($i=$x-1;$i>0;$i--){ $x=$x*$i;}
 return($x);
 }
}

sub comb{
 my $x = Math::BigInt->new('0');
 my $n=shift;
 my $r=shift;
 $x=fact($n)/(fact($n-$r)*fact($r));
 return($x);
}

