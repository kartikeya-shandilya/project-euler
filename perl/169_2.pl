#!/usr/bin/perl
use Math::BigInt;

$start = shift;

#$a = Math::BigInt->new('298023223876953125');
$a = Math::BigInt->new('1');
$a=$start;

$b=binary($a);
print "Binary of ",$a," is ",$b,"\n";
#$ans=ways($b);
#print "f(",$a,") = ",$ans,"\n";

sub binary {
	my $x=shift;
	my $a=Math::BigInt->new('0');
	my $b=Math::BigInt->new('1');
	my $c=Math::BigInt->new('0');
	$a=$x;
	while ($a>0) {
		$k=Math::BigInt->new($a/2);
		$l=$a-($k*2);
		if ($l>2) {
			$c=$c+$b*($l%2);
			$a=Math::BigInt->new($a/2+$l/2);
		}
		else {
			$c=$c+$b*($a%2);
			$a=Math::BigInt->new($a/2);
		}
		$b*=10;
		print "$a $b $c $l\n";
	}
	return ($c);
}

sub ispower {
	my $x=shift;
	my @y=split//,$x;
#	print "binary\n",$x," ",$#y,"\n";
	my $i,$j;
	for ($i=0,$j=0;$i<=$#y;$i++) {
		$j=$j+$y[$i];
	}
	if ($j eq $#y+1) { return (1); }
	elsif ($j eq 1) { return ($#y+1); }
	elsif (($j eq 2)and($y[$#y] eq 1)) { return ($#y); }
	else { return (0); }
}

sub minus {
	my $y=shift;
	my @arr=split//,$y;
#	print "minus start ",$y,"\n";
	if ($arr[$#arr] eq 1) { $x=$y-1; }
	else {
		for($i=$#arr,$j=0,$k=1,$x=0;$i>=0;$i--){
	        	if(($arr[$i] eq 0)and($j eq 0)) {
	                	$x=$x+$k*1;
        	        }
	                elsif(($arr[$i] eq 1)and($j eq 0)) {
        	        	$x=$x+$k*0;
	                        $j=1;
        	        }
	                else {
        	        	$x=$x+$k*$arr[$i];
	                }
                	$k=$k*10;
#			print "minus\n",$i," ",$j," ",$k," ",$x,"\n";
        	}
	}
#	print "minus\n",$i," ",$j," ",$k," ",$x,"\n";
	return ($x);
}

sub ways {
	my $x;
	my $y=shift;
	my $z=ispower($y);
	my $k=Math::BigInt->new('1');
#	print "ways\n",$x," ",$y," ",$z,"\n";
	if ($z ne 0) { 
#		print "f(",$y,") = ",$z,"\n";
		return ($z); 
	}
	else {
		if($y%10 eq 1) { 
#			print "f(",$y,") = f(",($y-1)/10,")\n";  
			$ans=ways(($y-1)/10); return($ans); 
		}
		else {
			$x=minus($y/10);
#			print "f(",$y,") = f(",$y/10,") + f(",$x,")\n";
			$ans=ways($y/10)+ways($x); return($ans);
		}
	}
}

